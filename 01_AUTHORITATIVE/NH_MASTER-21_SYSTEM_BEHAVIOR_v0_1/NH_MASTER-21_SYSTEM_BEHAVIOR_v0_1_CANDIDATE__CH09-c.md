# Chapter 9-c — Group G: C-SIA

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-c.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece contains speaker identity assessment: session and stream records, ranked identity evidence, acoustic spoofing evidence, assessment triggers, profile eligibility and protection, uncertainty responses and the SIA side of provisional enrollment. Existing Person-Box linking conditions, acoustic-note fields and TSC reference records retain their earlier owners. Access calculation and delivery belong to CH09-d, biometric authority to CH09-e, full enrollment coordination to CH09-h, modes to CH09-i and phone capture to CH10-d.

[SOURCE CONFLICT: V10 §25.1 / Acoustic Condition Notes Amendment and §25.3 / Natural Voice Variation still describe acoustic_condition_notes as proposed/pending. A15 v1_1 and its package-complete receipt accept the optional physical-context record. The V10 proposal wording and accepted consumer boundary retain their respective stamps; no additional BOP interpretation authority is inferred.]

[SOURCE CONFLICT: V10 §25.4 Gate 2 lists disqualifying imitation-risk flags, while Option A and §25.5 preserve recognized_ness when imitation_risk blocks top_security. SIA reports the evidence; the unresolved access wording remains with CH09-d.]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.

<!-- BEGIN BEHAVIOR -->

### C-SIA — Speaker Identity Assessment (§25.3)
Stamp: DESIGNED    Source: [V10 §25.3] [MAP C-SIA]

ALONE
- What it is: DESIGNED — The component assessing who is probably speaking and whether audio appears replayed, synthetic, converted or non-live. [V10 §25.3 / What SIA Is and Is Not]
- Takes in: DESIGNED — BOP roots, Person-Box-linked profile readings and the current session's stream, conversational and biometric evidence. [V10 §25.3]
- Does: DESIGNED — Assesses each detected stream independently, keeps ranked candidates and separate acoustic suspicion, updates in-memory session state and emits one assessment output per cycle. [V10 §25.3]
- Gives out: DESIGNED — `SIA_output` containing `speaker_session_state`, `assessment_event_id` and `assessment_confidence_note`, plus security audit events. [V10 §25.3 / SIA Output Interface] [V10 §25.3 / What SIA Is and Is Not]
- Must never: DESIGNED — Decide access, interpret meaning, store content, merge identity authority, silently discard qualifying candidates, treat conversational divergence as acoustic spoofing or use identity assessment as wellbeing assessment. [V10 §25.3] [V10 §25.5]
- Fails closed by: DESIGNED — On restart loses SSS; identity returns to unknown and SACL applies guest. Ambiguous leading candidates yield `assessed_person_box_id = null`. [V10 §25.3 / Speaker Session State (SSS)] [V10 §25.3 / Speaker Assessment Object] [MAP C-SIA]

TOGETHER
- Fed by: DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): physical observation roots; C-7L — Person-Boxes (§7L): independently linked profile readings; C-BAI — Biometric Authorization Interface (§25.6): biometric evidence remains an independent factor. [V10 §25.3] [MAP C-SIA]
- Gated by: DESIGNED — C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting): wellbeing is never identity or access authority; C-WIS-SEP.1 — Identity assessment is not wellbeing assessment: identity certainty stays in its own domain; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected acoustic and profile evidence remains within authorized use. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.5]
- Gated by: CANDIDATE — C-WIS-SEP.9 — Producing-component records: actual results and attempted or actual separation violations are recorded through the producing component's normal operational/security logging. [MAP C-SIA] [MAP C-WIS-SEP]
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): provides assessments rather than an access decision; C-TSC — Temporary Session Cache (§7E-TSC): assessment-event references support capture-time attribution without a TSC call into SIA. [V10 §25.3 / SIA Output Interface] [V10 §7E-TSC / 29. Integration Boundaries]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | Current per-stream identity, biometric and acoustic-suspicion evidence. | Calculates access under its own gates. | Speaker access is computed by SACL. | [V10 §25.3 / Multi-Speaker State] [MAP C-SIA] |
| 2 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | Existing assessment-event references. | Links capture-time attribution without calling SIA. | Authoritative assessments stay in the security audit log. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 3 · DESIGNED | C-TSC.6 — Participant record | SIA stream and person-assessment references. | Carries the participant's identity assessment separately from a declared role. | Participant attribution retains its evidence. | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] |
| 4 · DESIGNED | C-TSC.6.10 — sia_stream_id_ref | The assessed stream identifier or null. | Stores the participant's SIA reference. | No independent identity conclusion is created. | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] |
| 5 · DESIGNED | C-TSC.7 — Attribution assessment | Capture-time identity, certainty, dimensions, flags and suspicion. | Preserves the assessment at capture without retrospective upgrading. | Attribution remains tied to the observed moment. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 6 · DESIGNED | C-TSC.7.11 — sia_assessment_event_id | The assessment event's stable identifier. | References the event used for attribution. | The identity evidence stays traceable. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 7 · DESIGNED | C-TSC.9 — BOP and SIA links | Existing SIA event identities and contribution timing. | Keeps references without promoting SIA events as roots. | Assessment authority remains in the security audit log. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| 8 · DESIGNED | C-TSC.9.2 — SIA event link record | An existing event and its session/contribution relationship. | Stores the referential association. | No SIA event becomes a root. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| 9 · DESIGNED | C-TSC.9.2.3 — sia_assessment_event_id | The audit-held event identifier. | Identifies the linked SIA assessment. | The reference carries no copied assessment authority. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| 10 · DESIGNED | C-TSC.29.3 — SIA reference boundary | Existing assessment references. | Links them without calling SIA. | Audit records remain authoritative. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 11 · DESIGNED | C-7L — Person-Boxes (§7L) | Identity assessments and independent profile comparisons. | Keeps voice readings linked to the correct separate Person-Box under proposal rules. | No shared identity authority or silent reassignment follows. | [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 12 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Attributed evidence and capture-time certainty. | Applies all minimum linking conditions. | Unknown-speaker material cannot silently merge into a box. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 13 · DESIGNED | C-7L.10.2 — Unknown-speaker capture-time certainty minimum | Certainty at capture. | Requires the attributed material's minimum certainty. | Later confidence cannot substitute for capture-time evidence. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 14 · DESIGNED | C-7L.10.3 — Unknown-speaker no-spoofing condition | Spoofing flags on attributed material. | Requires their absence for linking eligibility. | Flagged material cannot satisfy the condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 15 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | SIA's profile-consumer boundary. | Hands off only after its committed provisional link. | A link does not itself create a profile or grant access. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 16 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | SIA's requirement for current committed link truth. | Blocks profile creation on refused, pending, stale, contradictory or unverifiable results. | Only a committed link permits the SIA handoff. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 17 · DESIGNED | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Continuous identity and suspicion assessments. | Keeps disclosure inside the speaker's SACL-calculated limits. | Internal understanding does not become disclosure authority. | [V10 §25.2 / Continuous Speaker Security] |
| 18 · DESIGNED | C-OTHER.12 — Continuous speaker security | Updated speaker evidence. | Uses current assessments for access recalculation. | Uncertainty and suspicion retain distinct responses. | [V10 §25.2 / Continuous Speaker Security] |
| 19 · DESIGNED | C-WIS-SEP.3 — Access decisions exclude wellbeing | Current identity and suspicion evidence. | Keeps access decisions independent of wellbeing. | Wellbeing does not supply permission. | [V10 §25.5] |
| 20 · DESIGNED | C-WIS-SEP.5 — Temporary behavioral divergence | Behavioral divergence and identity evidence. | Keeps temporary divergence separate from acoustic spoofing. | No automatic wellbeing-to-security conversion occurs. | [V10 §25.5] |
| 21 · DESIGNED | C-WIS-SEP.6 — Acoustic spoofing security outcome | Acoustic-only suspicion evidence. | Preserves the distinct spoofing route. | Conversational differences are excluded from that assessment. | [V10 §25.3 / Anti-Spoofing Assessment Object] [V10 §25.5] |
| 22 · DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | Current identity evidence through its access boundary. | Keeps use and disclosure within privacy authority. | Recognition alone supplies no privacy permission. | [V10 §7Q] [MAP C-SIA] |
| 23 · ACCEPTED | C-7Q.11.2 — Established identity and private-context boundary | Current identity assessment. | Separates established identity from authority to use private context. | Recognition does not open Personal Mode or waive privacy. | [04/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md §4] |
| 24 · DESIGNED | C-2.15.3.2 — Record identity boundary | Identity evidence for protected operational-record access. | Keeps record access subject to identity and security boundaries. | A log record does not grant access. | [MAP C-2] |
| 25 · DESIGNED | C-7B.10.8.4 — Identity and security condition | Current identity evidence. | Keeps Meaning Engine operational records within identity/security rules. | Operational history does not bypass access. | [V10 §0B] |
| 26 · DESIGNED | C-LEARN.10 — Protected connected learning-operation history | Identity evidence for access checks. | Keeps learning-operation history protected. | The history is not independently accessible because it exists. | [V10 §0B] [MAP C-LEARN] |
| 27 · ACCEPTED | C-7R.15.7 — Declaration Logging / audit requirement | Identity evidence at the protected logging boundary. | Keeps declaration records under normal privacy/security access. | Logging adds no access permission. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| 28 · DESIGNED | C-OOP.10 — Outcome and route operational logging | Identity evidence for protected log access. | Retains component privacy/security limits on operational records. | Outcome logs do not become an alternate disclosure path. | [V10 §0B] [MAP C-OOP] |
| 29 · ACCEPTED | C-7P.2.6 — Strictest-rule and specialist authority boundary | Specialist identity evidence. | Leaves identity assessment with SIA while applying the strictest applicable permission rule. | Permission coordination does not take identity authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] |
| 30 · ACCEPTED | C-LMAC.8.4 — Control-query identity access purpose and logging | Current identity evidence. | Checks the control query's identity/access/purpose boundary. | A control query is not a permission bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 31 · ACCEPTED | C-LMAC.11.4 — Shared operational logging and access protection | Identity evidence for operational-record access. | Keeps shared logging inside component protection rules. | Shared logging creates no authority. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 32 · DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | Identity evidence at the protected feedback boundary. | Keeps use of affirmation material within identity/security rules. | Feedback does not become an access credential. | [V10 §0B] [MAP C-AFFIRM] |
| 33 · ACCEPTED | C-AFFIRM.8 — Protected append-only affirmation living record | Identity evidence for protected record access. | Keeps the affirmation record subject to privacy/security boundaries. | The living record does not authorize disclosure. | [V10 §0B] [MAP C-AFFIRM] |
| 34 · ACCEPTED | C-BOP.12.3 — Bounded acoustic-note downstream context | SIA's interpretation boundary. | Supplies physical notes without concluding identity or spoofing itself. | SIA retains the downstream assessment. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |
| 35 · DESIGNED | C-BOP.16 — Shared observation logging and protected access | Identity evidence for access to observation records. | Keeps logging under component privacy/security limits. | Observation history is not a separate permission path. | [V10 §0B] [MAP C-BOP] |
| 36 · DESIGNED | C-7Q.3.1 — Deletion dependency and location discovery | The original root and its known or discoverable derivatives and locations. | Proceeds only when governance discovery runs only under artifact §7Q authorization and §25 identity and security. | Nothing in this card. | [V10 §7Q] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.2] |
| 37 · ACCEPTED | C-SACL.33.1 — Proposed output_operation | Proposed output_operation_id and proposed delivery_idempotency_key. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 38 · ACCEPTED | C-SACL.33.2 — Proposed output_stage_event | The stage owner's gate-result/decision reference, with the common epoch and committed generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 39 · ACCEPTED | C-SACL.33.3 — Proposed retrieval_intersection_record | §7Q eligibility reference, SACL scope reference and identities of admitted material, with common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 40 · ACCEPTED | C-SACL.33.5 — Proposed delivery_attempt_event [proposed] | Proposed delivery_attempt_id, the exact claim reference and dispatch-intent reference, with common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §12] |
| 41 · ACCEPTED | C-SACL.33.6 — Proposed delivery_confirmation_receipt | Positive channel acknowledgment, both attempt and claim references, and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 42 · ACCEPTED | C-SACL.33.7 — Proposed delivery_non_delivery_receipt [proposed] | Positive non-delivery proof, both attempt and claim references, and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 43 · ACCEPTED | C-SACL.33.8 — Proposed delivery_uncertainty_record [proposed] | Both attempt and claim references, what remains unknown, what was not done, the permitted resolution routes and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 44 · ACCEPTED | C-SACL.33.10 — Proposed duplicate_delivery_prevented | Proposed delivery_idempotency_key, relevant proposed delivery_claim_id and proposed delivery_attempt_id. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 45 · ACCEPTED | C-SACL.33.11 — Proposed output_recovery_event | The crash boundary, committed truth found and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 46 · ACCEPTED | C-SACL.33.12 — Proposed delivery_claim_state_event | The affected claim, status spent, invalidated or abandoned, its basis and time, plus common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6F] |
| 47 · ACCEPTED | C-ENROLL.9.7 — Immutable enrollment segment identity | The particular captured segment's reference identity. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 48 · ACCEPTED | C-ENROLL.9.8 — Per-segment eligibility decision record | The six-check outcome and actual source references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 49 · ACCEPTED | C-ENROLL.13.1 — Enrollment parent operation record | Operation/session identities, process state, terminal reason and audit references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 50 · ACCEPTED | C-ENROLL.13.2 — Enrollment stage checkpoint | The actual stage's owner-returned outcome and references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 51 · ACCEPTED | C-ENROLL.13.3 — Enrollment recovery operation and event | The actual crash boundary and surviving committed owner facts. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 52 · ACCEPTED | C-ENROLL.13.4 — Absorbed enrollment duplicate record | A replay recognized by the relevant stable identity. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 53 · ACCEPTED | C-7G.11.1.18 — evidence_locator_record_ref [proposed] | Full evidence locators and any authorized necessary bounded quote held under the governed record boundary. | Locator access needs privacy and identity/security authorization. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §2.9] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §2.2] |
| 54 · ACCEPTED | C-7G.14 — Acceptance operation history | Each proposal and assessment, actual use/omission, criterion findings, operation terminal and recovery action. | Operation history is used only within the privacy, identity/security, TSC, compartment and influence-removal boundaries. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §7.4] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §7.6] |
| 55 · ACCEPTED | C-ENROLL.9.6.3 — No material stream split or merge condition | Segment stream split/merge facts. | Supplies stream-structure facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 56 · ACCEPTED | C-ENROLL.7 — Mid-session protective stop | Trust loss/replacement/revocation, invalid recovery/setup, QR/secret contradiction, medium-or-higher spoofing, missing/contradictory Person-Box, BAI/session integrity failure, privacy exclusion or restart. | Supplies spoofing changes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 57 · DESIGNED | C-9.1.4.6 — Soft voice factor | Voice/speaking-pattern evidence for SIA. | Supplies what this place relies on: current evidence interpretation remains at its owner. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6] [V10 §9] |
| 58 · ACCEPTED | C-ENROLL.9.6.1 — Full-segment diarization-confidence condition | Diarization confidence over the entire segment. | Supplies diarization facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 59 · DESIGNED | C-SACL.4.2.7 — No imitation-risk flag for top-security | `active_flags`. | Supplies the active imitation-risk flag. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 60 · DESIGNED | C-SACL.4.1.2 — Active spoofing-suspected flag | `active_flags`. | Supplies the assessment's active flags. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 61 · DESIGNED | C-SACL.4.4.2 — Known-person certainty threshold | `assessed_certainty` and `known_person_certainty_threshold`. | Supplies assessed certainty. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 62 · ACCEPTED | C-9.12 — Proposed mode coordination records | References to owner-held identity assessments, access decisions/PBRs, biometric tokens/leases, privacy decisions and audit events. | Supplies identity assessments. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12] |
| 63 · DESIGNED | C-SACL.7 — Separate identity wellbeing and access mechanisms | Identity and security evidence. | Supplies identity and acoustic-security assessment. | Nothing in this card. | [V10 §25.4 / Three Mechanisms Kept Separate] |
| 64 · DESIGNED | C-SACL.4.3 — Gate 2 recognized-Ness qualification | Assessed person/certainty, leading separation, spoofing/imitation-risk flags and active disqualifiers. | Supplies current identity and flag evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 65 · ACCEPTED | C-ENROLL.9.6.5 — Stream spoofing-evidence condition | Actual segment spoofing evidence. | Supplies actual spoofing facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 66 · ACCEPTED | C-STORE.4.14.1 — Authority and privacy | NOT DECIDED | Gates this place: access also passes §25 identity and security authorization. | Nothing in this card. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §15] |
| 67 · ACCEPTED | C-ENROLL.9.2 — Segment spoofing check | SIA's segment-scoped spoofing assessment. | Supplies the actual spoofing fact. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 68 · ACCEPTED | C-9.8.3.3 — Stale or failed assessment state | The owners' current failure or freshness state. | Supplies assessment state. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §8] |
| 69 · ACCEPTED | C-ENROLL.9.1 — Consistent live-speaker stream check | The segment's stream-consistency evidence. | Supplies actual stream/diarization facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 70 · DESIGNED | C-SACL.4.2.2 — Assessed Ness Person-Box | `assessed_person_box_id`. | Supplies assessed person reference. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 71 · ACCEPTED | C-ENROLL.9.3 — Overlapping-speaker contamination check | The actual segment overlap assessment. | Supplies owned speaker-stream assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 72 · DESIGNED | C-SACL.16.2 — Unknown and uncertain speakers are guests | Unknown or uncertain speaker evidence. | Supplies unknown or uncertain identity evidence. | Nothing in this card. | [V10 §25.4 / Protected-Core Rules (Unconditional)] |
| 73 · DESIGNED | C-SACL.5 — Independent biometric factor | `biometric_state = "verified"` and independent speaker-recognition evidence. | Supplies independent recognition and suspicion evidence. | Nothing in this card. | [V10 §25.4 / Fingerprint as One Independent Factor] |
| 74 · DESIGNED | C-SACL.4.4.1 — Confirmed non-Ness Person-Box | `assessed_person_box_id`. | Supplies assessed person reference. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 75 · DESIGNED | C-SACL.16.3 — Medium-high spoofing guest and alert | Medium or high acoustic spoofing suspicion. | Supplies acoustic-suspicion evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 76 · DESIGNED | C-SACL.1 — Speaker-authorization scope | SIA's assessments. | Supplies what this place relies on: assessments remain evidence for authorization. | Nothing in this card. | [V10 §25.4 / What SACL Is and Is Not] |
| 77 · DESIGNED | C-SACL.4.1.1 — Medium-or-high acoustic suspicion | `anti_spoofing.suspicion_level`. | Supplies acoustic-suspicion evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 78 · DESIGNED | C-SACL.6 — Imitation-risk Option A | The imitation_risk flag, which may arise from stress, tiredness, illness, emotion or overload without an attack. | Supplies the distinct behavioral imitation-risk evidence. | Nothing in this card. | [V10 §25.4 / Imitation Risk Policy (Ness's Decision — Option A)] |
| 79 · DESIGNED | C-SACL.4.3.1 — Recognized-Ness certainty threshold | `assessed_certainty` and `recognized_ness_certainty_threshold`. | Supplies assessed certainty. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 80 · DESIGNED | C-SACL.4.2.3 — Top-security certainty threshold | `assessed_certainty` and `top_security_certainty_threshold`. | Supplies assessed certainty. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 81 · ACCEPTED | C-ENROLL.2 — Six-owner prerequisite check | I2 request `{ operation_ref }` and each real owner's `{ owner_ref, owner_version, satisfied }` response. | Supplies spoofing assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 82 · DESIGNED | C-SACL.4.4 — Gate 3 known-person qualification | Confirmed non-Ness person reference, certainty, separation, active PBR, required-presence result and disqualifiers. | Supplies identity, certainty and separation. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 83 · DESIGNED | C-SACL.4.2.5 — Exactly no acoustic suspicion | `anti_spoofing.suspicion_level`. | Supplies acoustic-suspicion assessment. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 84 · ACCEPTED | C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition | Actual second-speaker uncertainty. | Supplies second-speaker assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 85 · DESIGNED | C-SACL.4.2 — Gate 1 top-security qualification | Verified biometric timing, assessed person/certainty, candidate separation, suspicion, active disqualifiers and imitation-risk flags. | Supplies current speaker evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 86 · DESIGNED | C-SACL.4.3.2 — Gate 2 disqualifying-flag wording | Spoofing and imitation-risk flags. | Supplies the distinct flags at issue. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 87 · ACCEPTED | C-ENROLL.2.5 — Clean current spoofing prerequisite | SIA's assessment and SACL's Gate 0 disqualifier effect. | Supplies current assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 88 · DESIGNED | C-SACL.15.2 — Stale SIA assessment failure | Stale SIA assessment evidence. | Supplies assessment evidence and the fresh output needed to leave staleness handling. | Nothing in this card. | [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] |
| 89 · ACCEPTED | C-9.1.4.4 — SIA evidence role | The current SIA assessment. | Supplies the actual identity evidence owner. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6] |
| 90 · DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9) | Deliberate access requests, ordinary and stronger authentication results, voice input and requests for speech output. | Supplies current identity evidence. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §4] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [V10 §9] [MAP C-9] |
| 91 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Readings and their `reads`, `derived_from`, `produced_by` and confidence. | Gates this place: the checks remain subject to identity and security authorization. | Nothing in this card. | [V10 §0B] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |
| 92 · ACCEPTED | C-9.5.1 — Recognition and opening separation | Identity evidence and Ness's distinct opening choice. | Supplies recognition evidence without permission. | Nothing in this card. | [04/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md §4.1] |
| 93 · ACCEPTED | C-BAI.19.2 — Enrollment prerequisite revalidation | Six owner facts: final permanent trusted-owner phone status (BAI state 4). | Supplies acoustic-spoofing assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 94 · ACCEPTED | C-ENROLL.9 — Initial-corpus eligibility gate | Reading references, root provenance and actual owner facts for each immutable segment identity [proposed]. | Supplies spoofing/diarization facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 95 · CANDIDATE | C-SACL.17 — Access operational records | Each per-stream access calculation, gate outcome/downgrade, in-progress discard signal and queued Ness alert. | Gates this place: identity evidence at protected record access. | Nothing in this card. | [MAP C-SACL] |
| 96 · ACCEPTED | C-ENROLL.9.6.2 — Resolved speaker-transition condition | Segment transition evidence. | Supplies transition assessment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 97 · ACCEPTED | C-STORE.5.2.8 — Operation logging | NOT DECIDED | Gates this place: access also passes §25 identity and security authorization. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 98 · DESIGNED | C-SACL.4.2.4 — Sufficient candidate separation | Candidate score separation from the identity assessment. | Supplies ranked candidate evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 99 · ACCEPTED | C-ENROLL.9.6 — Full-segment stream-integrity check | Actual diarization confidence, transition, split/merge, second-speaker uncertainty and spoofing evidence. | Supplies actual diarization and spoofing facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 100 · DESIGNED | C-SACL.4.5 — Guest fallback | A stream that has not qualified for a higher level. | Supplies what this place relies on: identity evidence may remain unknown or uncertain. | Nothing in this card. | [V10 §25.4 / Protected-Core Rules (Unconditional)] |
| 101 · DESIGNED | C-SACL.8 — Multi-speaker disclosure | All active stream levels, output-path observability and applicable PBR presence requirement. | Supplies active stream shape. | Nothing in this card. | [V10 §25.4 / Multi-Speaker Sessions] |
| 102 · DESIGNED | C-SACL.4 — Ordered per-stream access calculation | Each stream's SIA evidence, biometric state, PBR eligibility and active disqualifiers. | Supplies every assessment event and stream evidence. | Nothing in this card. | [V10 §25.4 / Access Level Calculation] |
| 103 · ACCEPTED | C-ENROLL.7.4 — Spoofing safety change | SIA's assessment and SACL Gate 0 effect. | Supplies actual suspicion. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 104 · ACCEPTED | C-7B.9.7.2 — Identity and authorization protections | Selected Wonder material and the intake operation. | Gates this place: selected Wonder intake passes the existing identity and authorization protections unchanged. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §4] |
| 105 · DESIGNED | C-SACL.15.3 — SIA component failure | SIA component failure. | Supplies the component failure at this boundary. | Nothing in this card. | [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] |

SUB-PARTS: C-SIA.1 — Identity-assessment scope; C-SIA.2 — speaker_session_state; C-SIA.3 — voice_stream_record; C-SIA.4 — speaker_assessment; C-SIA.5 — anti_spoofing_assessment; C-SIA.6 — SIA_output; C-SIA.7 — Assessment update cadence; C-SIA.8 — Per-stream diarization; C-SIA.9 — Independent voice profiles; C-SIA.10 — Natural voice variation; C-SIA.11 — Ordinary voice-training eligibility; C-SIA.12 — Conservative profile calibration; C-SIA.13 — Protected raw voice and readings; C-SIA.14 — Uncertainty and spoofing responses; C-SIA.15 — False lockout recovery; C-SIA.16 — Multi-speaker evidence handoff; C-SIA.17 — Unknown-speaker linking evidence; C-SIA.18 — Compact inference representation; C-SIA.19 — Assessment records and TSC references; C-SIA.20 — Provisional enrollment profile handoff; C-SIA.21 — Synthetic output voice separation

### C-SIA.1 — Identity-assessment scope
Stamp: DESIGNED    Source: [V10 §25.3 / What SIA Is and Is Not]

ALONE
- What it is: DESIGNED — The boundary around identity probability and non-live-audio assessment. [V10 §25.3 / What SIA Is and Is Not]
- Takes in: DESIGNED — BOP roots. [V10 §25.3 / What SIA Is and Is Not]
- Does: DESIGNED — Assesses probable speaker identity and replayed, synthetic, converted or non-live characteristics. [V10 §25.3 / What SIA Is and Is Not]
- Gives out: DESIGNED — Identity assessments and security audit events. [V10 §25.3 / What SIA Is and Is Not]
- Must never: DESIGNED — Make access decisions, interpret meaning or store content. [V10 §25.3 / What SIA Is and Is Not]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): the observation roots assessed here. [V10 §25.3 / What SIA Is and Is Not]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies assessments for its independent access decision. [V10 §25.3 / What SIA Is and Is Not]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | Physical observations and their identity context. | Retains meaning interpretation as its own responsibility. | SIA does not substitute identity assessment for meaning. | [V10 §25.3 / What SIA Is and Is Not] |

SUB-PARTS: NONE

### C-SIA.2 — speaker_session_state
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — SSS, the in-memory record maintained throughout an active phone session. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — `session_id`, `session_mode`, `active_voice_stream_set`, `primary_addressed_stream`, `biometric_state`, `biometric_verified_at` and `assessment_history`. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Maintains the current session and its independent streams with an append-only assessment history inside the session. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — The full SSS object in each assessment output. [V10 §25.3 / SIA Output Interface]
- Must never: DESIGNED — Treat the previous in-memory SSS as surviving a restart. [V10 §25.3 / Speaker Session State (SSS)]
- Fails closed by: DESIGNED — Restart loses SSS; streams return to unknown identity and SACL guest access. [V10 §25.3 / Speaker Session State (SSS)] [MAP C-SIA]

TOGETHER
- Fed by: DESIGNED — C-SIA.2.1 — Session identity: `session_id`; C-SIA.2.2 — Session mode: `session_mode`; C-SIA.2.3 — Active voice stream set: per-stream records; C-SIA.2.4 — Primary addressed stream: the response recipient; C-SIA.2.5 — Session biometric state: biometric status; C-SIA.2.6 — Biometric verification time: timestamp or null; C-SIA.2.7 — Session assessment history: append-only assessments. [V10 §25.3 / Speaker Session State (SSS)]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.6.1 — Output speaker session state: supplies the full current SSS. [V10 §25.3 / SIA Output Interface]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2.1 — Session identity | The active session record. | Supplies its `session_id`. | SSS identifies the session. | [V10 §25.3 / Speaker Session State (SSS)] |
| 2 · DESIGNED | C-SIA.2.2 — Session mode | The active session's modality. | Supplies its permitted mode value. | SSS records voice, text or mixed use. | [V10 §25.3 / Speaker Session State (SSS)] |
| 3 · DESIGNED | C-SIA.2.3 — Active voice stream set | The session's detected streams. | Supplies a list of stream records. | Parallel streams remain represented. | [V10 §25.3 / Speaker Session State (SSS)] |
| 4 · DESIGNED | C-SIA.2.4 — Primary addressed stream | The stream receiving the response. | Supplies its stream ID. | The recipient is explicit. | [V10 §25.3 / Speaker Session State (SSS)] |
| 5 · DESIGNED | C-SIA.2.5 — Session biometric state | Current biometric evidence. | Supplies the status value. | Biometric state remains separate from identity certainty. | [V10 §25.3 / Speaker Session State (SSS)] |
| 6 · DESIGNED | C-SIA.2.6 — Biometric verification time | Available verification time. | Supplies a timestamp or null. | The record carries its temporal evidence. | [V10 §25.3 / Speaker Session State (SSS)] |
| 7 · DESIGNED | C-SIA.2.7 — Session assessment history | Assessments within the active session. | Adds them to the session history. | The list remains append-only within that session. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: C-SIA.2.1 — Session identity; C-SIA.2.2 — Session mode; C-SIA.2.3 — Active voice stream set; C-SIA.2.4 — Primary addressed stream; C-SIA.2.5 — Session biometric state; C-SIA.2.6 — Biometric verification time; C-SIA.2.7 — Session assessment history

### C-SIA.2.1 — Session identity
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — The `session_id` field in SSS. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — The active phone session's identity. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Identifies the session represented by SSS. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — `session_id`. [V10 §25.3 / Speaker Session State (SSS)]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the session identity field. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | `session_id`. | Associates the state with its active session. | Session identity is explicit. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: NONE

### C-SIA.2.2 — Session mode
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — The `session_mode` field. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — The active session's modality. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Distinguishes `voice`, `text` and `mixed`. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — `session_mode` with one of those three values. [V10 §25.3 / Speaker Session State (SSS)]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the modality value. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | The mode value. | Represents the session modality. | Voice, text and mixed sessions remain distinguishable. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: NONE

### C-SIA.2.3 — Active voice stream set
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — `active_voice_stream_set`, a list of `voice_stream_record`. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — One record per detected voice stream. [V10 §25.3 / Multi-Speaker State]
- Does: DESIGNED — Retains the streams as separately assessed entries, including parallel streams during overlap or interruption. [V10 §25.3 / Diarization]
- Gives out: DESIGNED — The session's multi-stream evidence set. [V10 §25.3 / Multi-Speaker State]
- Must never: DESIGNED — Silently collapse independently detected streams into one assessment. [V10 §25.3 / Diarization]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.3 — voice_stream_record: one independently assessed record per detected stream. [V10 §25.3 / Multi-Speaker State]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the stream-record list. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | The stream set. | Maintains the session's independent voice streams. | The full set remains available in SSS. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: NONE

### C-SIA.2.4 — Primary addressed stream
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — The `primary_addressed_stream` field. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — The `stream_id` of the stream N.H is responding to. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Identifies the addressed stream within multi-speaker state. [V10 §25.3 / Multi-Speaker State]
- Gives out: DESIGNED — `primary_addressed_stream`. [V10 §25.3 / Multi-Speaker State]
- Must never: DESIGNED — Use the addressed stream to replace SACL's shared-output minimum across active streams. [V10 §25.3 / Multi-Speaker State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: identifies the response recipient. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | The addressed stream ID. | Carries it separately from the stream set. | Response direction is explicit. | [V10 §25.3 / Multi-Speaker State] |

SUB-PARTS: NONE

### C-SIA.2.5 — Session biometric state
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — SSS `biometric_state`. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — Current biometric verification evidence. [V10 §25.3 / False Lockout Recovery]
- Does: DESIGNED — Represents `verified`, `not_verified` or `expired`. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — One biometric-state value independently of speaker recognition. [V10 §25.3 / False Lockout Recovery]
- Must never: DESIGNED — Treat `verified` alone as restored top-security when recognition remains uncertain or suspicious. [V10 §25.3 / False Lockout Recovery]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): biometric-factor verification. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the biometric status. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | The biometric-state value. | Carries the factor separately from identity evidence. | Verification does not become an access decision. | [V10 §25.3 / False Lockout Recovery] |

SUB-PARTS: NONE

### C-SIA.2.6 — Biometric verification time
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — `biometric_verified_at` in SSS. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — A verification timestamp or null. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Carries the recorded verification time when present. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — `biometric_verified_at: timestamp or null`. [V10 §25.3 / Speaker Session State (SSS)]
- Must never: DESIGNED — Invent a timestamp for null. [V10 §25.3 / Speaker Session State (SSS)]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the verification-time field. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | Timestamp or null. | Retains the verification time. | The time is present without inventing one for null. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: NONE

### C-SIA.2.7 — Session assessment history
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Session State (SSS)]

ALONE
- What it is: DESIGNED — SSS `assessment_history`. [V10 §25.3 / Speaker Session State (SSS)]
- Takes in: DESIGNED — Assessments made within the session. [V10 §25.3 / Speaker Session State (SSS)]
- Does: DESIGNED — Maintains an append-only list within the active session. [V10 §25.3 / Speaker Session State (SSS)]
- Gives out: DESIGNED — The session's assessment history. [V10 §25.3 / Speaker Session State (SSS)]
- Must never: DESIGNED — Rewrite existing entries in this append-only session list or treat it as a restart-persistent SSS. [V10 §25.3 / Speaker Session State (SSS)]
- Fails closed by: DESIGNED — The in-memory history is lost with SSS at restart. [V10 §25.3 / Speaker Session State (SSS)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.2 — speaker_session_state: supplies the assessment-history list. [V10 §25.3 / Speaker Session State (SSS)]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2 — speaker_session_state | The append-only assessment list. | Keeps the active session's assessment sequence. | Existing entries remain unchanged during that session. | [V10 §25.3 / Speaker Session State (SSS)] |

SUB-PARTS: NONE

### C-SIA.3 — voice_stream_record
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — The independently assessed record for one detected voice stream. [V10 §25.3 / Diarization]
- Takes in: DESIGNED — `stream_id`, `onset_event_id`, `speaker_assessment`, `anti_spoofing`, `stream_status`, `last_assessment_at` and `last_assessment_trigger`. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Keeps stream identity, opening observation, identity and acoustic assessments, status and last-assessment timing/trigger together for that stream. [V10 §25.3 / Voice Stream Record]
- Gives out: DESIGNED — One `voice_stream_record` in SSS for each detected stream. [V10 §25.3 / Multi-Speaker State]
- Must never: DESIGNED — Merge independent stream assessments during overlap or interruption. [V10 §25.3 / Diarization]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.3.1 — Stream identity: `stream_id`; C-SIA.3.2 — Stream onset reference: opening BOP root; C-SIA.3.3 — Stream speaker assessment: identity object; C-SIA.3.4 — Stream anti-spoofing assessment: acoustic object; C-SIA.3.5 — Stream status: active, paused or ended; C-SIA.3.6 — Last assessment time: timestamp; C-SIA.3.7 — Last assessment trigger: named trigger. [V10 §25.3 / Voice Stream Record]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.2.3 — Active voice stream set | One stream record per detected stream. | Keeps the records in a list. | Independent evidence remains available for multi-speaker access. | [V10 §25.3 / Multi-Speaker State] |
| 2 · DESIGNED | C-SIA.3.1 — Stream identity | The detected stream record. | Supplies its identifier. | The record has a stable referent within the stream set. | [V10 §25.3 / Voice Stream Record] |
| 3 · DESIGNED | C-SIA.3.2 — Stream onset reference | The stream's opening observation. | Supplies the BOP root reference. | The opening event is traceable. | [V10 §25.3 / Voice Stream Record] |
| 4 · DESIGNED | C-SIA.3.3 — Stream speaker assessment | The stream's identity assessment. | Supplies the identity object. | Candidates stay specific to the stream. | [V10 §25.3 / Voice Stream Record] |
| 5 · DESIGNED | C-SIA.3.4 — Stream anti-spoofing assessment | The stream's acoustic assessment. | Supplies the separate spoofing object. | Acoustic suspicion stays distinct from identity divergence. | [V10 §25.3 / Voice Stream Record] |
| 6 · DESIGNED | C-SIA.3.5 — Stream status | The detected stream's status. | Supplies its status value. | Activity, pause and end remain distinguishable. | [V10 §25.3 / Voice Stream Record] |
| 7 · DESIGNED | C-SIA.3.6 — Last assessment time | The most recent assessment time. | Supplies the timestamp. | The latest assessment is temporally identified. | [V10 §25.3 / Voice Stream Record] |
| 8 · DESIGNED | C-SIA.3.7 — Last assessment trigger | The latest assessment's named trigger. | Records why that update ran. | The record retains the trigger name. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: C-SIA.3.1 — Stream identity; C-SIA.3.2 — Stream onset reference; C-SIA.3.3 — Stream speaker assessment; C-SIA.3.4 — Stream anti-spoofing assessment; C-SIA.3.5 — Stream status; C-SIA.3.6 — Last assessment time; C-SIA.3.7 — Last assessment trigger

### C-SIA.3.1 — Stream identity
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — `stream_id` in a voice-stream record. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — The identity of one detected voice stream. [V10 §25.3 / Diarization]
- Does: DESIGNED — Identifies the stream assessed independently of parallel streams. [V10 §25.3 / Diarization]
- Gives out: DESIGNED — The record's `stream_id`. [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the stream identity. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | `stream_id`. | Identifies the stream represented by the record. | Parallel records remain separately addressable. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.2 — Stream onset reference
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — `onset_event_id`, the reference to the opening observation. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — The BOP root ID of the `voice_onset` that opened this stream. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Links the stream to its opening voice-onset root. [V10 §25.3 / Voice Stream Record]
- Gives out: DESIGNED — `onset_event_id`. [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.1 — voice_onset: the opening physical observation root ID. [V10 §25.3 / Voice Stream Record]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the opening-event reference. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | The onset root ID. | Retains the event that opened the stream. | Stream origin remains traceable. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.3 — Stream speaker assessment
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — The stream's `speaker_assessment` field. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — A `speaker_assessment` object. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Carries the identity assessment for this stream. [V10 §25.3 / Diarization]
- Gives out: DESIGNED — The nested identity object. [V10 §25.3 / Voice Stream Record]
- Must never: DESIGNED — Silently choose one profile where comparable candidates require an unresolved identity. [V10 §25.3 / Diarization] [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: DESIGNED — Carries a null assessed identity when the minimum certainty or separation requirement is not met. [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: DESIGNED — C-SIA.4 — speaker_assessment: ranked identity evidence and assessed identity. [V10 §25.3 / Voice Stream Record]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the stream's identity object. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | The identity object. | Keeps it with the matching stream. | Identity uncertainty is preserved. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.4 — Stream anti-spoofing assessment
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — The `anti_spoofing` field in a stream record. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — An `anti_spoofing_assessment` object. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Carries the stream's acoustic-only non-live-audio assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — The nested anti-spoofing object. [V10 §25.3 / Voice Stream Record]
- Must never: DESIGNED — Put conversational divergence into this acoustic assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.5 — anti_spoofing_assessment: acoustic suspicion and its evidence. [V10 §25.3 / Voice Stream Record]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the separate acoustic object. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | The acoustic suspicion object. | Keeps it distinct from speaker identity evidence. | Non-live-audio suspicion is represented separately. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.5 — Stream status
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — `stream_status` in the stream record. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — The stream's current activity status. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Distinguishes `active`, `paused` and `ended`. [V10 §25.3 / Voice Stream Record]
- Gives out: DESIGNED — One of the three named status values. [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies `stream_status`. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | The status value. | Distinguishes stream activity from its identity evidence. | Stream state is explicit. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.6 — Last assessment time
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — `last_assessment_at`. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — The last assessment's timestamp. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Carries when this stream was last assessed. [V10 §25.3 / Voice Stream Record]
- Gives out: DESIGNED — `last_assessment_at: timestamp`. [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the latest assessment time. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | Assessment timestamp. | Retains the time of its latest assessment. | The assessment's recency is represented. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.3.7 — Last assessment trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Stream Record]

ALONE
- What it is: DESIGNED — `last_assessment_trigger`. [V10 §25.3 / Voice Stream Record]
- Takes in: DESIGNED — The named trigger for the latest assessment. [V10 §25.3 / Voice Stream Record]
- Does: DESIGNED — Carries the trigger name alongside the assessment timestamp. [V10 §25.3 / Voice Stream Record]
- Gives out: DESIGNED — `last_assessment_trigger: named trigger`. [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.7 — Assessment update cadence: the named event causing an update. [V10 §25.3 / Assessment Update Cadence]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.3 — voice_stream_record: supplies the latest trigger name. [V10 §25.3 / Voice Stream Record]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3 — voice_stream_record | The named trigger. | Identifies why the latest assessment occurred. | Trigger provenance accompanies the result. | [V10 §25.3 / Voice Stream Record] |

SUB-PARTS: NONE

### C-SIA.4 — speaker_assessment
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — The identity-assessment object for one stream. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — `identity_candidates`, `assessed_person_box_id`, `assessed_certainty`, `active_flags` and `profile_status`. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Retains ranked qualifying candidates and leading/near-competing flags, and reports a leading identity only with sufficient certainty and separation. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — A `speaker_assessment` with either an assessed person and certainty or a null assessed identity and certainty. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Silently discard candidates above the reporting threshold or resolve insufficient separation into a chosen identity. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: DESIGNED — No qualifying certainty, inadequate separation or two candidates within the minimum separation threshold makes `assessed_person_box_id` null; SACL treats null as unknown and applies guest. [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: DESIGNED — C-SIA.4.1 — Ranked identity candidates: all reportable candidates; C-SIA.4.2 — Assessed Person-Box identity: leading ID or null; C-SIA.4.3 — Assessed identity certainty: confidence or null; C-SIA.4.4 — Active identity flags: leading and near-competing flags; C-SIA.4.5 — Leading profile status: status or null. [V10 §25.3 / Speaker Assessment Object]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3.3 — Stream speaker assessment | The full identity object. | Carries it in the stream record. | Identity evidence remains stream-specific. | [V10 §25.3 / Voice Stream Record] |
| 2 · DESIGNED | C-SIA.4.1 — Ranked identity candidates | The candidate evidence for this assessment. | Supplies every reportable candidate in rank order. | Competition remains visible. | [V10 §25.3 / Speaker Assessment Object] |
| 3 · DESIGNED | C-SIA.4.2 — Assessed Person-Box identity | Candidate certainty and separation. | Supplies an identity only where both are sufficient. | Ambiguity yields null. | [V10 §25.3 / Speaker Assessment Object] |
| 4 · DESIGNED | C-SIA.4.3 — Assessed identity certainty | The assessed ID and certainty. | Uses null certainty when the ID is null. | Certainty cannot imply an identity absent from the assessment. | [V10 §25.3 / Speaker Assessment Object] |
| 5 · DESIGNED | C-SIA.4.4 — Active identity flags | Flags across leading and near-competing candidates. | Supplies their union. | Competing uncertainty remains represented. | [V10 §25.3 / Speaker Assessment Object] |
| 6 · DESIGNED | C-SIA.4.5 — Leading profile status | The leading candidate's profile status. | Supplies that status or null. | Profile maturity is visible independently of assessed certainty. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: C-SIA.4.1 — Ranked identity candidates; C-SIA.4.2 — Assessed Person-Box identity; C-SIA.4.3 — Assessed identity certainty; C-SIA.4.4 — Active identity flags; C-SIA.4.5 — Leading profile status

### C-SIA.4.1 — Ranked identity candidates
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `identity_candidates`, the ranked candidate list. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — All Person-Box candidates above the minimum reporting threshold. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Retains each qualifying `candidate_record` in the ranked list, including near-competing candidates. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The complete reportable candidate list. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Silently discard a candidate above the minimum reporting threshold. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.4.1.1 — Identity candidate record: per-candidate scores, flags and profile status. [V10 §25.3 / Speaker Assessment Object]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4 — speaker_assessment: supplies `identity_candidates`. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4 — speaker_assessment | The ranked list. | Preserves qualifying identity alternatives. | The leading result does not erase competition. | [V10 §25.3 / Speaker Assessment Object] |
| 2 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | One qualifying Person-Box candidate. | Supplies its candidate-specific record. | Each candidate remains separately described. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: C-SIA.4.1.1 — Identity candidate record

### C-SIA.4.1.1 — Identity candidate record
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `candidate_record`, one entry in `identity_candidates`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — `person_box_id`, `match_score`, `evidence_dimension_scores`, `uncertainty_flags` and `profile_status`. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Keeps the candidate's identity, combined score, separate dimensions, named uncertainty flags and profile state together. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — One candidate-specific assessment record. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Merge one candidate's identity authority with another profile's authority. [V10 §25.3 / Voice Profile Architecture]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.4.1.1.1 — Candidate Person-Box identity: `person_box_id`; C-SIA.4.1.1.2 — Candidate match score: `match_score`; C-SIA.4.1.1.3 — Candidate evidence dimensions: separate evidence values; C-SIA.4.1.1.4 — Candidate uncertainty flags: named candidate flags; C-SIA.4.1.1.5 — Candidate profile status: profile state. [V10 §25.3 / Speaker Assessment Object]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1 — Ranked identity candidates: contributes one candidate record. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1 — Ranked identity candidates | The candidate record. | Ranks it with all other reportable candidates. | No qualifying candidate is silently removed. | [V10 §25.3 / Speaker Assessment Object] |
| 2 · DESIGNED | C-SIA.4.1.1.1 — Candidate Person-Box identity | The candidate represented by the record. | Supplies its Person-Box ID. | The assessment refers to that candidate. | [V10 §25.3 / Speaker Assessment Object] |
| 3 · DESIGNED | C-SIA.4.1.1.2 — Candidate match score | The candidate's match evidence. | Supplies a score in the decided range. | Candidates can be ranked and compared. | [V10 §25.3 / Speaker Assessment Object] |
| 4 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | The candidate's distinct evidence dimensions. | Keeps them separately named. | The combined score retains its dimensions. | [V10 §25.3 / Speaker Assessment Object] |
| 5 · DESIGNED | C-SIA.4.1.1.4 — Candidate uncertainty flags | Candidate-specific uncertainty. | Supplies named flags. | The candidate's uncertainty stays explicit. | [V10 §25.3 / Speaker Assessment Object] |
| 6 · DESIGNED | C-SIA.4.1.1.5 — Candidate profile status | The candidate's profile state. | Supplies the permitted state value. | Maturity, staleness and absence remain distinguishable. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: C-SIA.4.1.1.1 — Candidate Person-Box identity; C-SIA.4.1.1.2 — Candidate match score; C-SIA.4.1.1.3 — Candidate evidence dimensions; C-SIA.4.1.1.4 — Candidate uncertainty flags; C-SIA.4.1.1.5 — Candidate profile status

### C-SIA.4.1.1.1 — Candidate Person-Box identity
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `person_box_id` in a candidate record. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The candidate's Person-Box identifier. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Identifies which candidate the accompanying evidence concerns. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — `person_box_id`. [V10 §25.3 / Speaker Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1 — Identity candidate record: identifies the candidate. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | The Person-Box ID. | Associates the evidence with its candidate. | Candidate identity is explicit. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.2 — Candidate match score
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — The candidate's `match_score`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The assessed match for this candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents the match in the interval `[0.0, 1.0]`. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The numeric `match_score`. [V10 §25.3 / Speaker Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1 — Identity candidate record: supplies the candidate's match score. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | A score from zero through one. | Retains the candidate's match strength. | Candidate comparison has an explicit value. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3 — Candidate evidence dimensions
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `evidence_dimension_scores` inside a candidate record. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — `voice_acoustic_match`, `behavioral_pattern_match`, `branch_continuity_score`, `session_continuity_score`, `timing_rhythm_score`, `wording_pattern_score` and `device_biometric_state`. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Keeps acoustic, behavioral, branch, session, timing, wording and biometric evidence distinct for that candidate. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The seven named dimensions. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Move branch discontinuity, timing changes, wording differences or conversational divergence into `anti_spoofing_assessment`; those belong here or in a separate imitation-risk assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.4.1.1.3.1 — Voice acoustic match: acoustic evidence; C-SIA.4.1.1.3.2 — Behavioral pattern match: behavioral evidence; C-SIA.4.1.1.3.3 — Branch continuity score: branch evidence; C-SIA.4.1.1.3.4 — Session continuity score: session evidence; C-SIA.4.1.1.3.5 — Timing rhythm score: timing evidence; C-SIA.4.1.1.3.6 — Wording pattern score: wording evidence; C-SIA.4.1.1.3.7 — Device biometric state: independent biometric status. [V10 §25.3 / Speaker Assessment Object]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1 — Identity candidate record: supplies the separate evidence dimensions. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | The dimension set. | Retains it alongside the combined score. | The candidate's evidence is not reduced to an unexplained total. | [V10 §25.3 / Speaker Assessment Object] |
| 2 · DESIGNED | C-SIA.4.1.1.3.1 — Voice acoustic match | The candidate's acoustic evidence. | Supplies its acoustic-match dimension. | Acoustic comparison remains separately represented. | [V10 §25.3 / Speaker Assessment Object] |
| 3 · DESIGNED | C-SIA.4.1.1.3.2 — Behavioral pattern match | The candidate's behavioral evidence. | Supplies its behavioral dimension. | Behavior is not relabeled acoustic spoofing. | [V10 §25.3 / Speaker Assessment Object] |
| 4 · DESIGNED | C-SIA.4.1.1.3.3 — Branch continuity score | Branch continuity evidence. | Supplies its branch dimension. | Branch divergence remains identity evidence. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 5 · DESIGNED | C-SIA.4.1.1.3.4 — Session continuity score | Session continuity evidence. | Supplies its session dimension. | Session evidence stays distinct. | [V10 §25.3 / Speaker Assessment Object] |
| 6 · DESIGNED | C-SIA.4.1.1.3.5 — Timing rhythm score | Timing and rhythm evidence. | Supplies its timing dimension. | Timing changes do not become acoustic spoofing. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 7 · DESIGNED | C-SIA.4.1.1.3.6 — Wording pattern score | Wording-pattern evidence. | Supplies its wording dimension. | Wording differences stay outside acoustic suspicion. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 8 · DESIGNED | C-SIA.4.1.1.3.7 — Device biometric state | The device's biometric status. | Supplies its independent factor value. | Biometric evidence does not replace speaker recognition. | [V10 §25.3 / False Lockout Recovery] |

SUB-PARTS: C-SIA.4.1.1.3.1 — Voice acoustic match; C-SIA.4.1.1.3.2 — Behavioral pattern match; C-SIA.4.1.1.3.3 — Branch continuity score; C-SIA.4.1.1.3.4 — Session continuity score; C-SIA.4.1.1.3.5 — Timing rhythm score; C-SIA.4.1.1.3.6 — Wording pattern score; C-SIA.4.1.1.3.7 — Device biometric state

### C-SIA.4.1.1.3.1 — Voice acoustic match
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — The `voice_acoustic_match` evidence dimension. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The current voice's acoustic match to the candidate's profile range. [V10 §25.3 / Natural Voice Variation]
- Does: DESIGNED — Contributes acoustic evidence separately from other identity dimensions; a low acoustic match can coexist with sufficient combined certainty when the other dimensions remain strong. [V10 §25.3 / Natural Voice Variation]
- Gives out: DESIGNED — `voice_acoustic_match` within the candidate's evidence dimensions. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Treat a profile as a single fixed acoustic point. [V10 §25.3 / Natural Voice Variation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies acoustic match separately. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | The acoustic-match dimension. | Retains it alongside the other evidence. | Natural variation need not erase stronger combined evidence. | [V10 §25.3 / Natural Voice Variation] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.2 — Behavioral pattern match
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `behavioral_pattern_match`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Behavioral-pattern evidence for the candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Carries the behavioral match as an identity-evidence dimension. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The named behavioral dimension. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Treat conversational divergence as acoustic spoofing. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies the behavioral match. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | Behavioral-pattern match. | Keeps the dimension separate from acoustic suspicion. | Identity evidence retains its domain. | [V10 §25.3 / Speaker Assessment Object] [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.3 — Branch continuity score
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `branch_continuity_score`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Branch-continuity evidence for the candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents branch continuity within identity evidence. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The branch-continuity dimension. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Put `branch_discontinuity` in the acoustic-only anti-spoofing object. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies branch continuity. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | Branch continuity. | Keeps the evidence in the identity assessment. | Branch differences are not acoustic spoofing signals. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.4 — Session continuity score
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `session_continuity_score`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Session-continuity evidence for this candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents continuity across the current session as its own dimension. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The session-continuity score. [V10 §25.3 / Speaker Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies session continuity. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | Session continuity. | Retains the separate dimension. | Session evidence remains explicit. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.5 — Timing rhythm score
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `timing_rhythm_score`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Timing and rhythm evidence for the candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents timing/rhythm within identity evidence. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The timing-rhythm dimension. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Treat timing changes as acoustic spoofing evidence. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies timing/rhythm evidence. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | Timing-rhythm score. | Keeps timing evidence in the candidate assessment. | Timing changes remain outside anti-spoofing. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.6 — Wording pattern score
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `wording_pattern_score`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The candidate's wording-pattern evidence. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents wording as a separate identity dimension. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The wording-pattern score. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Put wording differences or conversational divergence into acoustic spoofing assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies wording evidence. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | The wording-pattern score. | Keeps wording evidence separate from acoustic suspicion. | Conversational differences retain their proper domain. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.3.7 — Device biometric state
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `device_biometric_state` in the candidate evidence dimensions. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The device's biometric-factor state. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Represents `verified`, `not_verified` or `expired`. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The named biometric-state value alongside the other dimensions. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Substitute biometric success for independently sufficient speaker recognition and absence of spoofing. [V10 §25.3 / False Lockout Recovery]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): evidence of the independent biometric factor. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1.3 — Candidate evidence dimensions: supplies biometric status. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1.3 — Candidate evidence dimensions | Verified, not-verified or expired status. | Keeps biometric evidence alongside independent identity dimensions. | A verified device does not decide access by itself. | [V10 §25.3 / Speaker Assessment Object] [V10 §25.3 / False Lockout Recovery] |

SUB-PARTS: NONE

### C-SIA.4.1.1.4 — Candidate uncertainty flags
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `uncertainty_flags` for one candidate. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Named uncertainty flags applying to that candidate. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Keeps a candidate-specific list. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — `uncertainty_flags: list of named flags for this candidate`. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Let the score erase uncertainty. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1 — Identity candidate record: supplies the candidate's uncertainty list. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | The candidate's named flags. | Retains uncertainty with the candidate evidence. | The score does not erase uncertainty. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.1.1.5 — Candidate profile status
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `profile_status` within a candidate record. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The state of that candidate's profile. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Distinguishes `enrollment_provisional`, `enrollment_active`, `calibrated`, `stale` and `absent`. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — One of those five profile-status values. [V10 §25.3 / Speaker Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4.1.1 — Identity candidate record: supplies the candidate's profile state. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4.1.1 — Identity candidate record | The profile-status value. | Distinguishes provisional, active, calibrated, stale and absent profiles. | Profile state remains visible with the evidence. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.2 — Assessed Person-Box identity
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `assessed_person_box_id`, the leading candidate ID or null. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Candidate certainty and score separation. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Reports the leading candidate only when a candidate reaches minimum certainty and the leader has sufficient separation from competitors. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The leading ID, or null when either condition fails. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Select a person when two candidates are within the minimum separation threshold. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: DESIGNED — Reports null for insufficient certainty or separation; SACL interprets null as unknown and applies guest. [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4 — speaker_assessment: supplies the assessed identity or null. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4 — speaker_assessment | A leading ID or null. | Preserves an unresolved result when certainty or separation is insufficient. | No convenient winner is fabricated. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.3 — Assessed identity certainty
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `assessed_certainty` for the assessed identity. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The assessed person's certainty and the null/non-null identity result. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Carries a value in `[0.0, 1.0]`, or null when `assessed_person_box_id` is null. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — Numeric certainty or null. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Retain a non-null assessed certainty when the assessed Person-Box ID is null. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: DESIGNED — A null assessed identity carries null certainty. [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4 — speaker_assessment: supplies the certainty/null field. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4 — speaker_assessment | Numeric certainty or null. | Keeps certainty consistent with the assessed identity. | An unresolved identity does not retain an asserted certainty. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.4 — Active identity flags
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — `active_flags` for the assessment. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — Flags active across the leading and near-competing candidates. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Forms their union using the vocabulary `speaker_change_possible`, `spoofing_suspected`, `imitation_risk`, `profile_provisional`, `profile_stale`, `low_evidence` and `degraded_signal_conditions`. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The union of active flags. [V10 §25.3 / Speaker Assessment Object]
- Must never: DESIGNED — Drop a near-competing candidate's active flags merely because another candidate leads. [V10 §25.3 / Speaker Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4 — speaker_assessment: supplies the combined active-flag set. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4 — speaker_assessment | Leading and near-competing active flags. | Retains their union. | Candidate competition remains represented in uncertainty. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.4.5 — Leading profile status
Stamp: DESIGNED    Source: [V10 §25.3 / Speaker Assessment Object]

ALONE
- What it is: DESIGNED — The outer `profile_status` field in `speaker_assessment`. [V10 §25.3 / Speaker Assessment Object]
- Takes in: DESIGNED — The leading candidate's profile status or null. [V10 §25.3 / Speaker Assessment Object]
- Does: DESIGNED — Carries the leader's status independently of the per-candidate status fields. [V10 §25.3 / Speaker Assessment Object]
- Gives out: DESIGNED — The leading profile status or null. [V10 §25.3 / Speaker Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.4 — speaker_assessment: supplies the outer profile-status field. [V10 §25.3 / Speaker Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.4 — speaker_assessment | The leader's profile status or null. | Carries it alongside the assessed identity and active flags. | The current leading profile's state remains explicit. | [V10 §25.3 / Speaker Assessment Object] |

SUB-PARTS: NONE

### C-SIA.5 — anti_spoofing_assessment
Stamp: DESIGNED    Source: [V10 §25.3 / Anti-Spoofing Assessment Object]

ALONE
- What it is: DESIGNED — The assessment of evidence that audio may be replayed, synthetic, converted or non-live. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Takes in: DESIGNED — `suspicion_level`, `suspicion_basis`, `suspicion_source` and `assessment_certainty`, using acoustic spoofing signals only. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Does: DESIGNED — Keeps acoustic suspicion separate from identity-evidence differences and imitation-risk assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — An `anti_spoofing_assessment` object for the stream. [V10 §25.3 / Voice Stream Record]
- Must never: DESIGNED — Include `branch_discontinuity`, timing changes, wording differences or conversational divergence; those belong in identity evidence dimensions or a separate imitation-risk assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.5.1 — Acoustic suspicion level: the four-level value; C-SIA.5.2 — Acoustic suspicion basis: named acoustic signals; C-SIA.5.3 — Acoustic suspicion source: producing reading IDs; C-SIA.5.4 — Acoustic assessment certainty: certainty in the assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gated by: DESIGNED — C-WIS-SEP.6 — Acoustic spoofing security outcome: conversational divergence is excluded from acoustic suspicion. [V10 §25.3 / Anti-Spoofing Assessment Object] [V10 §25.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3.4 — Stream anti-spoofing assessment | The acoustic-only object. | Carries it separately in the stream record. | Suspicion stays stream-specific. | [V10 §25.3 / Voice Stream Record] |
| 2 · DESIGNED | C-SIA.5.1 — Acoustic suspicion level | Acoustic evidence strength. | Supplies the named suspicion level. | None, low, medium and high stay distinguishable. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 3 · DESIGNED | C-SIA.5.2 — Acoustic suspicion basis | Detected acoustic signals. | Supplies the list of acoustic bases. | Conversational differences are excluded. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 4 · DESIGNED | C-SIA.5.3 — Acoustic suspicion source | The readings producing the assessment. | Supplies their IDs. | The acoustic assessment has source references. | [V10 §25.3 / Anti-Spoofing Assessment Object] |
| 5 · DESIGNED | C-SIA.5.4 — Acoustic assessment certainty | Confidence in this acoustic assessment. | Supplies the certainty value. | Suspicion level and certainty remain separate fields. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: C-SIA.5.1 — Acoustic suspicion level; C-SIA.5.2 — Acoustic suspicion basis; C-SIA.5.3 — Acoustic suspicion source; C-SIA.5.4 — Acoustic assessment certainty

### C-SIA.5.1 — Acoustic suspicion level
Stamp: DESIGNED    Source: [V10 §25.3 / Anti-Spoofing Assessment Object]

ALONE
- What it is: DESIGNED — `suspicion_level` in the acoustic assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Takes in: DESIGNED — Acoustic evidence of replayed, synthetic, converted or non-live audio. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Does: DESIGNED — Distinguishes `none`, `low`, `medium` and `high`. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — One of the four named suspicion levels. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Must never: DESIGNED — Treat conversational divergence as a basis for this acoustic level. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.5 — anti_spoofing_assessment: supplies `suspicion_level`. [V10 §25.3 / Anti-Spoofing Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.5 — anti_spoofing_assessment | The suspicion-level value. | Represents the acoustic suspicion separately from its certainty. | The level is available to the access owner. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.5.2 — Acoustic suspicion basis
Stamp: DESIGNED    Source: [V10 §25.3 / Anti-Spoofing Assessment Object]

ALONE
- What it is: DESIGNED — `suspicion_basis`, a list of acoustic spoofing signals. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Takes in: DESIGNED — Acoustic findings named `playback_artifact_detected`, `compression_artifact_detected`, `synthetic_speech_trace`, `microphone_room_inconsistency` or `pattern_too_uniform`. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Does: DESIGNED — Lists the acoustic signals supporting suspicion. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — The `suspicion_basis` list. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Must never: DESIGNED — Include branch discontinuity, timing changes, wording differences or conversational divergence as acoustic bases. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.5 — anti_spoofing_assessment: supplies acoustic-only suspicion bases. [V10 §25.3 / Anti-Spoofing Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.5 — anti_spoofing_assessment | The acoustic-basis list. | Keeps suspicion grounded in non-live-audio evidence. | Conversational divergence stays outside the object. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.5.3 — Acoustic suspicion source
Stamp: DESIGNED    Source: [V10 §25.3 / Anti-Spoofing Assessment Object]

ALONE
- What it is: DESIGNED — `suspicion_source`. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Takes in: DESIGNED — IDs of the readings that produced these acoustic assessments. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Does: DESIGNED — References the assessment-producing readings. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — Reading IDs in `suspicion_source`. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.5 — anti_spoofing_assessment: supplies the source-reading references. [V10 §25.3 / Anti-Spoofing Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.5 — anti_spoofing_assessment | Producing reading IDs. | Keeps the assessment traceable to its readings. | Acoustic conclusions retain their sources. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.5.4 — Acoustic assessment certainty
Stamp: DESIGNED    Source: [V10 §25.3 / Anti-Spoofing Assessment Object]

ALONE
- What it is: DESIGNED — `assessment_certainty` for acoustic suspicion. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Takes in: DESIGNED — Certainty in the acoustic assessment. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Does: DESIGNED — Represents it in `[0.0, 1.0]`. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Gives out: DESIGNED — The numeric certainty value. [V10 §25.3 / Anti-Spoofing Assessment Object]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.5 — anti_spoofing_assessment: supplies certainty separately from suspicion level. [V10 §25.3 / Anti-Spoofing Assessment Object]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.5 — anti_spoofing_assessment | A value from zero through one. | Keeps assessment certainty explicit. | Certainty remains distinct from the named suspicion level. | [V10 §25.3 / Anti-Spoofing Assessment Object] |

SUB-PARTS: NONE

### C-SIA.6 — SIA_output
Stamp: DESIGNED    Source: [V10 §25.3 / SIA Output Interface]

ALONE
- What it is: DESIGNED — SIA's output interface, emitted once per assessment cycle. [V10 §25.3 / SIA Output Interface]
- Takes in: DESIGNED — The full `speaker_session_state`, stable `assessment_event_id` and `assessment_confidence_note`. [V10 §25.3 / SIA Output Interface]
- Does: DESIGNED — Packages the cycle's evidence with its stable ID and audit-only confidence label. [V10 §25.3 / SIA Output Interface]
- Gives out: DESIGNED — One `SIA_output` per cycle. [V10 §25.3 / SIA Output Interface]
- Must never: DESIGNED — Include access decisions or use the confidence note as a decision input. [V10 §25.3 / SIA Output Interface]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.6.1 — Output speaker session state: full SSS; C-SIA.6.2 — Assessment event identity: stable cycle ID; C-SIA.6.3 — Assessment confidence note: audit-only label. [V10 §25.3 / SIA Output Interface]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies identity and suspicion evidence for access calculation. [V10 §25.3 / Multi-Speaker State]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.6.1 — Output speaker session state | The cycle's full session state. | Supplies that object without an access decision. | Output retains the complete stream set. | [V10 §25.3 / SIA Output Interface] |
| 2 · DESIGNED | C-SIA.6.2 — Assessment event identity | The assessment cycle identity. | Supplies a stable event ID. | The assessment can be referenced. | [V10 §25.3 / SIA Output Interface] |
| 3 · DESIGNED | C-SIA.6.3 — Assessment confidence note | The cycle's audit context. | Supplies the audit-only confidence label. | The label cannot become decision authority. | [V10 §25.3 / SIA Output Interface] |

SUB-PARTS: C-SIA.6.1 — Output speaker session state; C-SIA.6.2 — Assessment event identity; C-SIA.6.3 — Assessment confidence note

### C-SIA.6.1 — Output speaker session state
Stamp: DESIGNED    Source: [V10 §25.3 / SIA Output Interface]

ALONE
- What it is: DESIGNED — The `speaker_session_state` field in `SIA_output`. [V10 §25.3 / SIA Output Interface]
- Takes in: DESIGNED — The full current SSS object. [V10 §25.3 / SIA Output Interface]
- Does: DESIGNED — Carries the complete session state, including the independent stream set. [V10 §25.3 / SIA Output Interface] [V10 §25.3 / Multi-Speaker State]
- Gives out: DESIGNED — Full SSS as `speaker_session_state`. [V10 §25.3 / SIA Output Interface]
- Must never: DESIGNED — Replace this evidence handoff with an SIA access decision. [V10 §25.3 / SIA Output Interface]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.6 — SIA_output: supplies its full-SSS field. [V10 §25.3 / SIA Output Interface]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.6 — SIA_output | The full SSS object. | Emits the complete session evidence. | All active streams remain represented. | [V10 §25.3 / SIA Output Interface] |
| 2 · DESIGNED | C-SIA.2 — speaker_session_state | The output interface's requirement for full SSS. | Supplies its whole current object. | The handoff does not collapse the session to one access value. | [V10 §25.3 / SIA Output Interface] |

SUB-PARTS: NONE

### C-SIA.6.2 — Assessment event identity
Stamp: DESIGNED    Source: [V10 §25.3 / SIA Output Interface]

ALONE
- What it is: DESIGNED — `assessment_event_id`. [V10 §25.3 / SIA Output Interface]
- Takes in: DESIGNED — The identity of the current assessment cycle. [V10 §25.3 / SIA Output Interface]
- Does: DESIGNED — Provides a stable ID for that cycle. [V10 §25.3 / SIA Output Interface]
- Gives out: DESIGNED — The stable assessment-event identifier. [V10 §25.3 / SIA Output Interface]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.6 — SIA_output: supplies the stable cycle ID. [V10 §25.3 / SIA Output Interface]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.6 — SIA_output | The assessment ID. | Identifies the emitted cycle. | Consumers can refer to that assessment. | [V10 §25.3 / SIA Output Interface] |

SUB-PARTS: NONE

### C-SIA.6.3 — Assessment confidence note
Stamp: DESIGNED    Source: [V10 §25.3 / SIA Output Interface]

ALONE
- What it is: DESIGNED — `assessment_confidence_note`, an audit label only. [V10 §25.3 / SIA Output Interface]
- Takes in: DESIGNED — The assessment's audit context. [V10 §25.3 / SIA Output Interface]
- Does: DESIGNED — Labels it `normal`, `degraded_conditions`, `provisional_profile` or `low_evidence`. [V10 §25.3 / SIA Output Interface]
- Gives out: DESIGNED — One of the four confidence-note values. [V10 §25.3 / SIA Output Interface]
- Must never: DESIGNED — Use the audit label as decision input. [V10 §25.3 / SIA Output Interface]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.6 — SIA_output: supplies the audit-only confidence note. [V10 §25.3 / SIA Output Interface]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.6 — SIA_output | The confidence note. | Includes the audit label without decision authority. | Audit context remains distinct from access inputs. | [V10 §25.3 / SIA Output Interface] |

SUB-PARTS: NONE

### C-SIA.7 — Assessment update cadence
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — The continuous and event-triggered assessment schedule. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — Active speech across bounded windows and the eight named triggers. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Assesses continuously while speech is active and on `voice_onset`, `acoustic_window`, `meaningful_acoustic_change`, `overlap_detected`, `speaker_transition`, `confirmed_text_sent`, `biometric_event` and `session_state_change`. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — Updated assessments with their named trigger. [V10 §25.3 / Assessment Update Cadence] [V10 §25.3 / Voice Stream Record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-SIA.7.1 — Voice-onset assessment trigger: stream onset; C-SIA.7.2 — Periodic acoustic-window trigger: bounded active-speech windows; C-SIA.7.3 — Meaningful acoustic-change trigger: significant measurement shift; C-SIA.7.4 — Overlap-detected trigger: overlapping voices; C-SIA.7.5 — Speaker-transition trigger: speaker transition; C-SIA.7.6 — Confirmed-text trigger: confirmed text sent; C-SIA.7.7 — Biometric-event trigger: biometric event; C-SIA.7.8 — Session-state-change trigger: session-state change. [V10 §25.3 / Assessment Update Cadence]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.3.7 — Last assessment trigger | The named update trigger. | Stores it for the stream's latest assessment. | The assessment retains its trigger name. | [V10 §25.3 / Voice Stream Record] |
| 2 · DESIGNED | C-SIA.7.1 — Voice-onset assessment trigger | The cadence's onset rule. | Triggers assessment on voice onset. | New speech initiates an update. | [V10 §25.3 / Assessment Update Cadence] |
| 3 · DESIGNED | C-SIA.7.2 — Periodic acoustic-window trigger | The active-speech cadence. | Triggers bounded periodic updates. | Assessments continue while the stream is active. | [V10 §25.3 / Assessment Update Cadence] |
| 4 · DESIGNED | C-SIA.7.3 — Meaningful acoustic-change trigger | The measurement-change rule. | Triggers on significant acoustic shift. | Changed conditions prompt reassessment. | [V10 §25.3 / Assessment Update Cadence] |
| 5 · DESIGNED | C-SIA.7.4 — Overlap-detected trigger | The overlap update rule. | Triggers when overlap is detected. | Parallel speech receives reassessment. | [V10 §25.3 / Assessment Update Cadence] |
| 6 · DESIGNED | C-SIA.7.5 — Speaker-transition trigger | The transition update rule. | Triggers on speaker transition. | Speaker changes prompt reassessment. | [V10 §25.3 / Assessment Update Cadence] |
| 7 · DESIGNED | C-SIA.7.6 — Confirmed-text trigger | The confirmed-text rule. | Triggers when confirmed text is sent. | Text interaction updates the assessment. | [V10 §25.3 / Assessment Update Cadence] |
| 8 · DESIGNED | C-SIA.7.7 — Biometric-event trigger | The biometric update rule. | Triggers on a biometric event. | New factor evidence prompts reassessment. | [V10 §25.3 / Assessment Update Cadence] |
| 9 · DESIGNED | C-SIA.7.8 — Session-state-change trigger | The session-state update rule. | Triggers on session-state change. | Session changes prompt reassessment. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: C-SIA.7.1 — Voice-onset assessment trigger; C-SIA.7.2 — Periodic acoustic-window trigger; C-SIA.7.3 — Meaningful acoustic-change trigger; C-SIA.7.4 — Overlap-detected trigger; C-SIA.7.5 — Speaker-transition trigger; C-SIA.7.6 — Confirmed-text trigger; C-SIA.7.7 — Biometric-event trigger; C-SIA.7.8 — Session-state-change trigger

### C-SIA.7.1 — Voice-onset assessment trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — The `voice_onset` assessment trigger. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A voice onset. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers an assessment update. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — An assessment cycle caused by `voice_onset`. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.1 — voice_onset: the physical onset event. [V10 §25.3 / Voice Stream Record] [V10 §25.3 / Assessment Update Cadence]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the onset-triggered update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | `voice_onset`. | Runs an assessment update. | Onset is included among update causes. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.2 — Periodic acoustic-window trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — The `acoustic_window` trigger. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — Bounded audio windows while the stream is active. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Produces periodic assessment updates during active speech; window size remains an empirical implementation decision. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — Periodic acoustic-window assessment cycles. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: supplies periodic updates while the stream is active. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | Bounded active-speech windows. | Continues assessment periodically. | Updating is not confined to discrete speaker onsets. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.3 — Meaningful acoustic-change trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `meaningful_acoustic_change`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A significant shift in acoustic measurements. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers reassessment on that shift. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — An acoustic-change assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts a measurement-change update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | Significant acoustic shift. | Updates the assessment. | Changed measurements are reassessed. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.4 — Overlap-detected trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `overlap_detected`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — Detected overlapping speech. [V10 §25.3 / Assessment Update Cadence] [V10 §25.3 / Diarization]
- Does: DESIGNED — Triggers assessment while parallel streams remain independently represented. [V10 §25.3 / Assessment Update Cadence] [V10 §25.3 / Diarization]
- Gives out: DESIGNED — An overlap-triggered assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: DESIGNED — Collapse overlapping streams into one identity assessment. [V10 §25.3 / Diarization]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the overlap update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | Detected overlap. | Reassesses independent streams. | Parallel speech is an explicit update trigger. | [V10 §25.3 / Assessment Update Cadence] [V10 §25.3 / Diarization] |

SUB-PARTS: NONE

### C-SIA.7.5 — Speaker-transition trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `speaker_transition`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A speaker transition. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers an assessment update. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — A transition-triggered assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the speaker-transition update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | A speaker transition. | Runs an assessment cycle. | Transition is an explicit update cause. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.6 — Confirmed-text trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `confirmed_text_sent`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A confirmed-text-sent event. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers an assessment update. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — A confirmed-text assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the confirmed-text update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | Confirmed text sent. | Runs an assessment update. | Text interaction is included in the cadence. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.7 — Biometric-event trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `biometric_event`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A biometric event. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers reassessment with the independent biometric evidence. [V10 §25.3 / Assessment Update Cadence] [V10 §25.3 / False Lockout Recovery]
- Gives out: DESIGNED — A biometric-event assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: DESIGNED — Make the biometric event alone a top-security grant. [V10 §25.3 / False Lockout Recovery]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): biometric-factor events. [V10 §25.3 / Assessment Update Cadence] [MAP C-SIA]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the biometric-event update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | A biometric event. | Reassesses the session evidence. | Factor changes prompt an update without deciding access. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.7.8 — Session-state-change trigger
Stamp: DESIGNED    Source: [V10 §25.3 / Assessment Update Cadence]

ALONE
- What it is: DESIGNED — `session_state_change`. [V10 §25.3 / Assessment Update Cadence]
- Takes in: DESIGNED — A change in session state. [V10 §25.3 / Assessment Update Cadence]
- Does: DESIGNED — Triggers an assessment update. [V10 §25.3 / Assessment Update Cadence]
- Gives out: DESIGNED — A session-state-change assessment cycle. [V10 §25.3 / Assessment Update Cadence]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.7 — Assessment update cadence: starts the session-change update. [V10 §25.3 / Assessment Update Cadence]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.7 — Assessment update cadence | A session-state change. | Runs a new assessment cycle. | Session changes are explicit update causes. | [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-SIA.8 — Per-stream diarization
Stamp: DESIGNED    Source: [V10 §25.3 / Diarization]

ALONE
- What it is: DESIGNED — Independent assessment of each detected voice stream. [V10 §25.3 / Diarization]
- Takes in: DESIGNED — Detected voices, including overlapping and interrupted speech. [V10 §25.3 / Diarization]
- Does: DESIGNED — Maintains one `voice_stream_record` per stream; parallel streams coexist and are assessed independently. [V10 §25.3 / Diarization]
- Gives out: DESIGNED — Separate stream assessments and both profiles when comparison scores are similar. [V10 §25.3 / Diarization]
- Must never: DESIGNED — Silently resolve similar profiles into one selected identity. [V10 §25.3 / Diarization]
- Fails closed by: DESIGNED — `assessed_person_box_id` may remain null; it is null whenever candidates lie within the minimum separation threshold. [V10 §25.3 / Diarization] [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): voice observation roots. [V10 §25.3 / What SIA Is and Is Not]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies independent evidence for each stream, without choosing the access result. [V10 §25.3 / Multi-Speaker State]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC) | Existing stream and assessment references. | Preserves participant and capture-time attribution links. | Parallel speakers retain distinct provenance. | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |

SUB-PARTS: NONE

### C-SIA.9 — Independent voice profiles
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Profile Architecture]

ALONE
- What it is: DESIGNED — Profiles formed from shared-store readings linked to individual Person-Boxes. [V10 §25.3 / Voice Profile Architecture]
- Takes in: DESIGNED — Sets of profile readings linked through §7L. [V10 §25.3 / Voice Profile Architecture]
- Does: DESIGNED — Compares profiles in a common technical embedding space while keeping each comparison and each identity authority independent. [V10 §25.3 / Voice Profile Architecture]
- Gives out: DESIGNED — Independent profile-comparison evidence. [V10 §25.3 / Voice Profile Architecture]
- Must never: DESIGNED — Merge profiles, share identity authority or silently reassign a profile to another person. [V10 §25.3 / Voice Profile Architecture]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7L — Person-Boxes (§7L): independently linked reading sets. [V10 §25.3 / Voice Profile Architecture]
- Gated by: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: unknown-speaker linkage must satisfy the decided minimum evidence and proposal rules. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | The independent-profile boundary. | Keeps linked voice readings separate by identity authority. | Technical comparison never silently merges people. | [V10 §25.3 / Voice Profile Architecture] |

SUB-PARTS: NONE

### C-SIA.10 — Natural voice variation
Stamp: DESIGNED    Source: [V10 §25.3 / Natural Voice Variation]

ALONE
- What it is: DESIGNED — A voice profile represents a range across natural recording and personal conditions. [V10 §25.3 / Natural Voice Variation]
- Takes in: DESIGNED — Readings from BOP roots across time, room, device position and state; proposed `acoustic_condition_notes` provide physical context. [V10 §25.3 / Natural Voice Variation] [SOURCE CONFLICT: 04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §§3–5 and its package-complete receipt accept the optional physical-context record; V10's proposal wording is retained here.]
- Does: DESIGNED — Builds the range from varied conditions. When acoustic match falls but other dimensions remain strong, combined certainty may stay above threshold. [V10 §25.3 / Natural Voice Variation]
- Gives out: DESIGNED — Identity assessment that can retain sufficient combined certainty despite a weaker acoustic match. [V10 §25.3 / Natural Voice Variation]
- Must never: DESIGNED — Reduce the voice profile to one fixed point. [V10 §25.3 / Natural Voice Variation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): observation roots across varied conditions. [V10 §25.3 / Natural Voice Variation]
- Fed by: ACCEPTED — C-SIA.10.1 — Bounded acoustic-condition context: optional physical context retains measurement provenance and no independent identity authority. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies combined identity evidence for its own access calculation. [V10 §25.3 / Natural Voice Variation] [V10 §25.3 / Settled Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-SIA.10.1 — Bounded acoustic-condition context | The range-based identity assessment. | Contextualizes weak acoustic match under SIA's own rules. | Physical measurements remain one bounded input. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |

SUB-PARTS: C-SIA.10.1 — Bounded acoustic-condition context

### C-SIA.10.1 — Bounded acoustic-condition context
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — SIA's bounded use of optional `acoustic_condition_notes` inside voice `signal_measurements`. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — Records with `condition_name`, `detection_method`, `detection_version`, `threshold_value`, `measured_value` and `certainty`; the five allowed names are `high_ambient_noise`, `close_microphone`, `far_microphone`, `room_reverb_present` and `signal_compression_heavy`. Canonical field and value owners remain the BOP acoustic-note cards. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — May weigh a note as physical recording-condition context under SIA's own rules, for example to contextualize a low acoustic-match score. Every use preserves the original measurement, detection method, version, threshold, measured value, certainty scope and source provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Bounded physical context alongside other lawful evidence; the note remains a DUMB observation and `certainty` remains certainty about the physical classification. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Let the note assert, or serve alone as sufficient evidence of, identity, speaker change, spoofing, imitation risk, emotion, intention, communicative meaning, importance, behavioral pattern or causation; silently turn a measurement into interpretation or use the amendment to authorize recording. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.12 — Optional acoustic_condition_notes amendment: the optional physical records; C-BOP.12.3 — Bounded acoustic-note downstream context: the provenance-preserving use boundary. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.10 — Natural voice variation: contributes bounded context while SIA retains the identity assessment. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.10 — Natural voice variation | Provenance-bearing acoustic-condition notes. | Weighs physical context alongside other evidence under its own rules. | Low acoustic match can be contextualized without a note deciding identity. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-SIA.11 — Ordinary voice-training eligibility
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The six jointly required conditions for a BOP acoustic root to contribute to a voice profile. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — Session authorization; capture-time stream certainty and spoofing state; security-audit flags; Ness-session continuity where applicable; and completion of the root's §7E → §7G path. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Permits contribution only when all six conditions hold; the Ness-specific condition applies to Ness's profile. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — Eligible profile evidence after the reading path, or no permitted training contribution. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Use psychiatric or medical appointment records as voice-identity training evidence, skip a condition or substitute later certainty for certainty at capture. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — A root cannot contribute when any applicable condition is unsatisfied. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): acoustic roots whose eligibility is assessed; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): readings after the normal intake and meaning path. [V10 §25.3 / Training Eligibility Rules]
- Gated by: DESIGNED — C-SIA.11.1 — Authorized training session: session authorization; C-SIA.11.2 — Capture-time training certainty: threshold met at capture; C-SIA.11.3 — Capture-time no-spoofing condition: suspicion exactly none; C-SIA.11.4 — Clean training audit history: no spoofing-related audit flag; C-SIA.11.5 — Ness training-session continuity: continuous qualifying Ness-session authority without identity uncertainty; C-SIA.11.6 — Completed reading path for training: §7E → §7G complete. [V10 §25.3 / Training Eligibility Rules]
- Gated by: DESIGNED — C-WIS-SEP.4 — Appointment records have a wellbeing-only purpose: appointment material is not voice-identity training evidence. [V10 §25.3 / Training Eligibility Rules] [V10 §25.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11.1 — Authorized training session | The all-conditions eligibility rule. | Requires an authorized session. | Unauthorized session material is ineligible. | [V10 §25.3 / Training Eligibility Rules] |
| 2 · DESIGNED | C-SIA.11.2 — Capture-time training certainty | The all-conditions rule and capture-time certainty. | Requires the training threshold at capture. | Later confidence cannot repair this condition. | [V10 §25.3 / Training Eligibility Rules] |
| 3 · DESIGNED | C-SIA.11.3 — Capture-time no-spoofing condition | The all-conditions rule and capture-time suspicion. | Requires suspicion none. | Suspicious capture cannot qualify for ordinary training. | [V10 §25.3 / Training Eligibility Rules] |
| 4 · DESIGNED | C-SIA.11.4 — Clean training audit history | The all-conditions rule and audit flags. | Excludes spoofing-flagged evidence. | Audit contamination blocks contribution. | [V10 §25.3 / Training Eligibility Rules] |
| 5 · DESIGNED | C-SIA.11.5 — Ness training-session continuity | The all-conditions rule for Ness's profile. | Requires biometric verification or uninterrupted recognized_ness without identity uncertainty. | Ness-specific evidence retains its session condition. | [V10 §25.3 / Training Eligibility Rules] |
| 6 · DESIGNED | C-SIA.11.6 — Completed reading path for training | The all-conditions rule and root-processing state. | Requires completion of §7E → §7G. | Raw roots alone cannot train the profile. | [V10 §25.3 / Training Eligibility Rules] |
| 7 · ACCEPTED | C-SIA.20.4 — Provisional evidence weighting | Ordinary training eligibility for subsequent evidence. | Applies every ordinary condition without an enrollment shortcut. | Provisional weighting does not authorize ineligible evidence. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 8 · DESIGNED | C-SIA.20.6 — Enrollment association strengthening | Ordinary eligibility rules for later evidence. | Uses only qualifying subsequent material to strengthen the association. | Enrollment roots gain no later-training exception. | [V10 §25.11 / SIA Integration] |
| 9 · ACCEPTED | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | SIA's committed provisional profile, with `profile_status="enrollment_provisional"`. | Gates this place: all later contributions obey ordinary conditions. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: C-SIA.11.1 — Authorized training session; C-SIA.11.2 — Capture-time training certainty; C-SIA.11.3 — Capture-time no-spoofing condition; C-SIA.11.4 — Clean training audit history; C-SIA.11.5 — Ness training-session continuity; C-SIA.11.6 — Completed reading path for training

### C-SIA.11.1 — Authorized training session
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The ordinary-training session-authorization condition. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — The authorization of the session producing the acoustic root. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires production during an authorized session. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — Satisfaction or non-satisfaction of this training condition. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Admit unauthorized-session material as eligible training evidence. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — Without an authorized session, the root cannot contribute to the voice profile. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the authorized-session condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Session authorization. | Requires this condition with the other five. | Unauthorized-session material cannot contribute. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.11.2 — Capture-time training certainty
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The capture-time certainty condition for ordinary training. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — SIA certainty for the specific stream at capture time. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires certainty ≥ `training_eligibility_threshold`. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — The threshold comparison for captured material. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Replace capture-time certainty with a later assessment or admit a below-threshold root. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — Below-threshold capture-time certainty prevents contribution. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the capture-time threshold condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Capture-time certainty against the training threshold. | Requires the minimum at capture. | Later recognition cannot retrospectively qualify the root. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.11.3 — Capture-time no-spoofing condition
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The ordinary-training acoustic-suspicion condition. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — Anti-spoofing `suspicion_level` at capture time. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires the value `none`. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — A satisfied condition only for capture-time suspicion none. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Treat low, medium or high suspicion as none for ordinary training. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — Any non-none capture-time suspicion prevents contribution. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the no-spoofing-at-capture condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Capture-time suspicion. | Requires exactly none. | Suspicious acoustic material is excluded from ordinary training. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.11.4 — Clean training audit history
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The security-audit condition on training material. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — Spoofing-related security-audit flags on the acoustic root. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires that the material is not flagged by spoofing-related audit events. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — The clean-audit eligibility condition. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Train from a root flagged with spoofing-related audit events. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — Such a flag prevents profile contribution. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the audit-history condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Spoofing-related audit flags. | Excludes flagged material. | Audit evidence is honored independently of the current match. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.11.5 — Ness training-session continuity
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The additional session condition when training Ness's profile. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — Biometric verification, continuous `recognized_ness` status and identity-uncertainty flags. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires a biometric-verified session or `recognized_ness` continuously throughout, with no identity uncertainty flags. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — The Ness-specific session-eligibility condition. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Treat intermittent recognized_ness or identity-uncertain material as satisfying continuous qualifying Ness-session evidence. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — Failure of this condition prevents contribution to Ness's profile. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the actual recognized_ness classification and its continuity; C-BAI — Biometric Authorization Interface (§25.6): biometric verification evidence. [V10 §25.3 / Training Eligibility Rules] [V10 §25.3 / Settled Rules]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the Ness-session condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | The qualifying Ness-session evidence. | Applies it when the target profile is Ness's. | Training preserves the additional session requirement. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.11.6 — Completed reading path for training
Stamp: DESIGNED    Source: [V10 §25.3 / Training Eligibility Rules]

ALONE
- What it is: DESIGNED — The completed-reading-path condition for profile contribution. [V10 §25.3 / Training Eligibility Rules]
- Takes in: DESIGNED — The acoustic root's §7E → §7G processing state. [V10 §25.3 / Training Eligibility Rules]
- Does: DESIGNED — Requires completion of that reading path before contribution. [V10 §25.3 / Training Eligibility Rules]
- Gives out: DESIGNED — Eligibility only after the root has completed intake and reading. [V10 §25.3 / Training Eligibility Rules]
- Must never: DESIGNED — Train from the raw root before its §7E → §7G path completes. [V10 §25.3 / Training Eligibility Rules]
- Fails closed by: DESIGNED — An incomplete reading path prevents contribution. [V10 §25.3 / Training Eligibility Rules]

TOGETHER
- Fed by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): normal intake processing; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed reading. [V10 §25.3 / Training Eligibility Rules]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: supplies the reading-path completion condition. [V10 §25.3 / Training Eligibility Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Completed §7E → §7G processing. | Requires a reading before training contribution. | Intake/meaning processing cannot be bypassed. | [V10 §25.3 / Training Eligibility Rules] |

SUB-PARTS: NONE

### C-SIA.12 — Conservative profile calibration
Stamp: DESIGNED    Source: [V10 §25.3 / The 6–10 Month Learning Period]

ALONE
- What it is: DESIGNED — The 6–10 month learning/calibration period. [V10 §25.3 / The 6–10 Month Learning Period]
- Takes in: DESIGNED — Accumulating authorized profile evidence across acoustic and other identity dimensions. [V10 §25.3 / The 6–10 Month Learning Period]
- Does: DESIGNED — Sets certainty thresholds conservatively; behavioral, branch and contextual dimensions carry proportionally more weight than acoustic match. Conservativeness reduces gradually as evidence accumulates. [V10 §25.3 / The 6–10 Month Learning Period]
- Gives out: DESIGNED — Conservative identity assessments with `recognized_ness` as the highest achievable access level for a provisional profile. [V10 §25.3 / The 6–10 Month Learning Period]
- Must never: DESIGNED — Permit a provisional profile to support an access level above recognized_ness. [V10 §25.3 / The 6–10 Month Learning Period]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its calculated access remains at or below the provisional-profile ceiling. [V10 §25.3 / The 6–10 Month Learning Period] [V10 §25.3 / Settled Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The provisional ceiling and conservative weighting. | Leaves access calculation to SACL while the profile remains provisional. | Enrollment cannot establish top-security. | [V10 §25.11 / SIA Integration] |

SUB-PARTS: NONE

### C-SIA.13 — Protected raw voice and readings
Stamp: DESIGNED    Source: [V10 §25.3 / Raw Voice Data Protection]

ALONE
- What it is: DESIGNED — Protection of acoustic roots, voice-profile readings and anti-spoofing readings. [V10 §25.3 / Raw Voice Data Protection]
- Takes in: DESIGNED — Raw acoustic roots in the sealed root store, Layer 3 Full Protected, and profile readings in the readings store under the same protection rules. [V10 §25.3 / Raw Voice Data Protection]
- Does: DESIGNED — Requires at least `recognized_ness` for access; permits transmission outside the local device only through the Full Mode tunnel under biometric-verified conditions. [V10 §25.3 / Raw Voice Data Protection]
- Gives out: DESIGNED — Access and permitted transmission within those protection limits. [V10 §25.3 / Raw Voice Data Protection]
- Must never: DESIGNED — Expose a voice-profile reading, acoustic root or anti-spoofing reading below recognized_ness, or transmit it outside the device outside the biometric-verified Full Mode tunnel. [V10 §25.3 / Raw Voice Data Protection]
- Fails closed by: DESIGNED — Below-threshold access cannot obtain the protected material; transmission without the required route and biometric condition is prohibited. [V10 §25.3 / Raw Voice Data Protection]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): at least recognized_ness is required for material access; C-BAI — Biometric Authorization Interface (§25.6): transmission requires biometric verification; C-23 — Mobile App, three modes (§23): external transmission uses only the Full Mode tunnel; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected handling remains binding. [V10 §25.3 / Raw Voice Data Protection]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Protected raw voice and linked-reading evidence. | Keeps enrollment material under the same privacy and transmission limits. | Bootstrap is not a raw-voice disclosure exception. | [V10 §25.3 / Raw Voice Data Protection] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| 2 · DESIGNED | C-23.7 — Protected voice-material transmission | Protected identity/voice material under its local store protections. | Supplies the protected-material boundary. | Nothing in this card. | [V10 §25.3 / Raw Voice Data Protection] |

SUB-PARTS: NONE

### C-SIA.14 — Uncertainty and spoofing responses
Stamp: DESIGNED    Source: [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

ALONE
- What it is: DESIGNED — The distinct outcomes for identity uncertainty, low acoustic suspicion and medium-or-high acoustic suspicion. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Takes in: DESIGNED — Identity certainty and the separately assessed acoustic suspicion level. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Does: DESIGNED — Keeps uncertainty eligible for natural recovery without an alert; low spoofing means guest and closer monitoring without an alert; medium/high means immediate guest, top-security relock and a private alert. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Gives out: DESIGNED — Identity/suspicion evidence for SACL and the distinct settled response requirements. [V10 §25.3 / Settled Rules]
- Must never: DESIGNED — Merge identity uncertainty with acoustic spoofing or issue routine live voice challenges. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]
- Fails closed by: DESIGNED — Suspicion lowers access through SACL; medium-or-higher suspicion relocks top-security immediately and silently. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]

TOGETHER
- Fed by: DESIGNED — C-SIA.14.1 — Identity-uncertain response: low certainty without a spoofing assertion; C-SIA.14.2 — Low-spoofing response: low acoustic suspicion; C-SIA.14.3 — Medium-or-high-spoofing response: medium/high acoustic suspicion. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): applies access changes from the distinct assessed conditions. [V10 §25.3 / Settled Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.14.1 — Identity-uncertain response | The separate uncertainty rule. | Continues assessment without a private Ness alert. | Natural recovery remains possible. | [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] |
| 2 · DESIGNED | C-SIA.14.2 — Low-spoofing response | The low-suspicion rule. | Monitors closely while SACL lowers access to guest. | No alert is yet queued. | [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] |
| 3 · DESIGNED | C-SIA.14.3 — Medium-or-high-spoofing response | The medium/high response rule. | Supplies evidence requiring immediate guest/relock and private alert. | The conversation gives no indication of the security action. | [V10 §25.3 / Settled Rules] |

SUB-PARTS: C-SIA.14.1 — Identity-uncertain response; C-SIA.14.2 — Low-spoofing response; C-SIA.14.3 — Medium-or-high-spoofing response

### C-SIA.14.1 — Identity-uncertain response
Stamp: DESIGNED    Source: [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

ALONE
- What it is: DESIGNED — The response to identity certainty below threshold. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Takes in: DESIGNED — Low certainty potentially caused by natural variation, an unknown speaker or noise. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Does: DESIGNED — Continues assessing and permits natural recovery of recognition. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Gives out: DESIGNED — Updated identity assessments without a private Ness alert for uncertainty alone. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Must never: DESIGNED — Queue the spoofing alert merely because identity is uncertain or issue a routine voice challenge. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]
- Fails closed by: DESIGNED — Insufficient identity certainty yields no assessed identity; SACL applies guest to the null result. [V10 §25.3 / Speaker Assessment Object]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.14 — Uncertainty and spoofing responses: supplies the uncertainty-only branch. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.14 — Uncertainty and spoofing responses | Below-threshold identity certainty. | Keeps natural recovery and no-alert behavior distinct from spoofing. | Uncertainty is not converted into an acoustic suspicion event. | [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] |

SUB-PARTS: NONE

### C-SIA.14.2 — Low-spoofing response
Stamp: DESIGNED    Source: [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

ALONE
- What it is: DESIGNED — The response to low acoustic spoofing suspicion. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Takes in: DESIGNED — Present acoustic evidence with suspicion level low. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Does: DESIGNED — Continues close monitoring while SACL reduces access to guest. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]
- Gives out: DESIGNED — Current low-suspicion evidence; no private alert yet. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Must never: DESIGNED — Queue a private alert solely for the low-suspicion branch or issue routine live voice challenges. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]
- Fails closed by: DESIGNED — Access drops to guest under SACL while SIA monitors closely. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.14 — Uncertainty and spoofing responses: supplies the low-suspicion branch. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.14 — Uncertainty and spoofing responses | Low acoustic suspicion. | Keeps guest reduction and monitoring separate from the private-alert threshold. | Low suspicion has its own response. | [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] |

SUB-PARTS: NONE

### C-SIA.14.3 — Medium-or-high-spoofing response
Stamp: DESIGNED    Source: [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]

ALONE
- What it is: DESIGNED — The response to medium or high acoustic spoofing suspicion. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Takes in: DESIGNED — Acoustic suspicion at medium or high. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Does: DESIGNED — Requires immediate guest access, top-security relock and a queued private Ness alert. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected]
- Gives out: DESIGNED — The acoustic security condition requiring that response, without an in-conversation indication. [V10 §25.3 / Settled Rules]
- Must never: DESIGNED — Reveal the security action in the conversation or issue a routine live voice challenge. [V10 §25.3 / Settled Rules]
- Fails closed by: DESIGNED — SACL immediately drops access to guest and relocks top-security; the alert remains private. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA.14 — Uncertainty and spoofing responses: supplies the medium/high acoustic branch; C-SACL — Speaker Access-Control Layer (§25.4): the assessed suspicion requires immediate guest/relock and private-alert handling. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SIA.14 — Uncertainty and spoofing responses | Medium/high acoustic suspicion. | Keeps the immediate silent security response distinct. | Private alert and relock apply at this threshold. | [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] |

SUB-PARTS: NONE

### C-SIA.15 — False lockout recovery
Stamp: DESIGNED    Source: [V10 §25.3 / False Lockout Recovery]

ALONE
- What it is: DESIGNED — Recovery through independent biometric and speaker-recognition factors. [V10 §25.3 / False Lockout Recovery]
- Takes in: DESIGNED — Thumbprint verification, current speaker recognition and spoofing flags. [V10 §25.3 / False Lockout Recovery]
- Does: DESIGNED — Uses thumbprint as the primary recovery route for the biometric factor. Top-security still requires biometric success, independently sufficient speaker recognition and no spoofing flag; monitoring may also recover naturally. [V10 §25.3 / False Lockout Recovery]
- Gives out: DESIGNED — Updated independent factors for SACL's access decision. [V10 §25.3 / False Lockout Recovery] [V10 §25.3 / Settled Rules]
- Must never: DESIGNED — Restore top-security from fingerprint alone while recognition remains uncertain or suspicious, or demand routine voice challenges. [V10 §25.3 / False Lockout Recovery]
- Fails closed by: DESIGNED — Top-security remains unavailable when sufficient independent recognition or absence of spoofing is not established despite biometric success. [V10 §25.3 / False Lockout Recovery]

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): thumbprint verification of the biometric factor. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): top-security restoration requires all independent conditions, not the fingerprint alone. [V10 §25.3 / False Lockout Recovery]
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies updated speaker evidence alongside the biometric factor. [V10 §25.3 / Settled Rules]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI — Biometric Authorization Interface (§25.6) | A thumbprint verification request. | Satisfies the biometric factor only. | Verification cannot by itself restore top-security. | [V10 §25.3 / False Lockout Recovery] |

SUB-PARTS: NONE

### C-SIA.16 — Multi-speaker evidence handoff
Stamp: DESIGNED    Source: [V10 §25.3 / Multi-Speaker State]

ALONE
- What it is: DESIGNED — SIA's multi-stream evidence boundary with SACL. [V10 §25.3 / Multi-Speaker State]
- Takes in: DESIGNED — `active_voice_stream_set`, one record per detected stream, and `primary_addressed_stream`. [V10 §25.3 / Multi-Speaker State]
- Does: DESIGNED — Supplies the complete stream evidence and identifies who receives the response. [V10 §25.3 / Multi-Speaker State]
- Gives out: DESIGNED — Evidence for SACL's per-stream levels and the minimum across all active streams for output visible to all. [V10 §25.3 / Multi-Speaker State]
- Must never: DESIGNED — Calculate access inside SIA or replace the shared-output minimum with the addressed speaker's level. [V10 §25.3 / Multi-Speaker State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies the stream evidence; SACL owns per-stream and shared-output calculations. [V10 §25.3 / Multi-Speaker State]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Current speaker evidence through SACL's own calculation. | Limits shared disclosure to the permitted audience. | Addressing Ness does not hide output from other active streams. | [V10 §25.3 / Multi-Speaker State] |

SUB-PARTS: NONE

### C-SIA.17 — Unknown-speaker linking evidence
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The six minimum evidence conditions before an unknown speaker may be linked to a Person-Box. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Requires minimum quantity; attribution certainty above minimum at capture; no spoofing flags; fingerprint-authorized TSC promotion followed by §7G; reading support above minimum confidence; and satisfied §7L proposal-based creation rules. The six canonical condition cards remain under C-7L.10. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — Evidence eligible for proposal-based Person-Box linking when every condition holds. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Link silently, merge people silently or omit one of the six conditions. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — Unknown-speaker linkage is not permitted before the six conditions are met. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion provenance; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): supporting readings. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Changes: DESIGNED — C-7L — Person-Boxes (§7L): supplies eligible identity evidence without granting silent-link authority. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Identity evidence satisfying the minimum conditions. | Uses the normal proposal-based linking rules. | A qualifying assessment is not a silent merge. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-SIA.18 — Compact inference representation
Stamp: DESIGNED    Source: [V10 §25.3 / Compact Profile Representation]

ALONE
- What it is: DESIGNED — A compact profile representation derived from authoritative readings. [V10 §25.3 / Compact Profile Representation]
- Takes in: DESIGNED — The source profile readings. [V10 §25.3 / Compact Profile Representation]
- Does: DESIGNED — Keeps a locally protected, versioned, rebuildable and non-authoritative representation for inference only. [V10 §25.3 / Compact Profile Representation]
- Gives out: DESIGNED — Derived inference material that can be rebuilt from its readings. [V10 §25.3 / Compact Profile Representation]
- Must never: DESIGNED — Replace original evidence, become authoritative, become a second profile store or serve purposes beyond inference. [V10 §25.3 / Compact Profile Representation]
- Fails closed by: DESIGNED — The representation is invalidated when source readings change or become stale. [V10 §25.3 / Compact Profile Representation]

TOGETHER
- Fed by: DESIGNED — C-7L — Person-Boxes (§7L): the linked authoritative profile-reading set. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Compact Profile Representation]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the derived representation remains locally protected under the source material's protection rules. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.3 / Compact Profile Representation]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | SIA evidence derived under the authoritative-reading boundary. | Makes its own access decision without treating a compact representation as authority. | Derived inference material cannot become an access grant. | [V10 §25.3 / Compact Profile Representation] [V10 §25.3 / Settled Rules] |

SUB-PARTS: NONE

### C-SIA.19 — Assessment records and TSC references
Stamp: CANDIDATE    Source: [MAP C-SIA]

ALONE
- What it is: CANDIDATE — SIA's operational record of its own identity-assessment operation. [MAP C-SIA]
- Takes in: CANDIDATE — Each assessment cycle/event, each anti-spoofing assessment, each training-eligibility decision and SIA's security audit events. [MAP C-SIA]
- Does: CANDIDATE — Records each of those operations under the shared logging law. The resulting voice/identity records are accessible only at or above recognized_ness, subject to privacy access/authorization and identity/security authorization. [MAP C-SIA]
- Does: DESIGNED — Keeps authoritative SIA assessment events in the security audit log; TSC links existing events by reference and never calls SIA. Events are not promoted as roots. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] [V10 §7E-TSC / 29. Integration Boundaries]
- Gives out: DESIGNED — Existing `sia_assessment_event_id` references for `sia_event_links`; timing relationships remain in the TSC table and relevant pre-ingest `source_metadata`, linked through identifiers without extra fields on seven-field roots. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Must never: DESIGNED — Promote SIA assessment events as roots, move their authority into the TSC or add session provenance as extra sealed-root fields. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Must never: CANDIDATE — Expose voice/identity operational records below recognized_ness or bypass applicable privacy and identity/security authorization. [MAP C-SIA]
- Fails closed by: CANDIDATE — Voice/identity operational records remain inaccessible below recognized_ness and outside applicable privacy and identity/security authorization. [MAP C-SIA]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): operational-record access requires its applicable privacy authorization; C-SACL — Speaker Access-Control Layer (§25.4): voice/identity operational records require at least recognized_ness and the applicable identity/security authorization. [MAP C-SIA] [V10 §0B]
- Changes: DESIGNED — C-TSC.9.2 — SIA event link record: links existing audit-event IDs with session/contribution timing; C-TSC.29.3 — SIA reference boundary: retains reference-only use without a TSC call into SIA. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] [V10 §7E-TSC / 29. Integration Boundaries]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | Existing audit-held assessment-event references. | Links contribution timing without taking assessment authority. | SIA events stay outside root promotion. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |

SUB-PARTS: NONE

### C-SIA.20 — Provisional enrollment profile handoff
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — SIA's profile-creation boundary after the provisional enrollment material has a current committed Person-Box link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — Current §7L-owned committed link truth, the linked eligible accepted reading set, the proposed `enrollment_profile_input_bundle` and the build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Uses the linked readings as one input under SIA's own rules and only then commits its provisional profile. Readiness, a proposal or acknowledgment alone cannot create the profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — A committed provisional profile or refusal, with duplicate profile creation absorbed by the build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create a profile before committed linkage, build it from copied raw audio or logs, create a second profile database, or treat enrollment provenance as proof that the captured voice is Ness's. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — A refused, pending, stale, contradictory or unverifiable link blocks profile creation. Unestablished readiness creates neither a profile nor a link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligible accepted reading references, proposed coordination bundle and build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current §7L-owned committed link to Ness's confirmed Person-Box is required before profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): only SIA's actual commit permits the profile-created enrollment event; C-SACL — Speaker Access-Control Layer (§25.4): receives assessments under the normal boundary, with a provisional ceiling rather than a grant. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-SIA.20.1 — Eligible enrollment reading input | The SIA handoff's reading-only boundary. | Consumes only eligible accepted readings and provenance as one input. | Raw voice and logs do not become a profile. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-SIA.20.2 — Provisional profile commit identity | The SIA-owned commit boundary. | Uses the build identity to prevent duplicate profiles. | The result is committed truth or refusal. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-SIA.20.3 — Provisional status and access ceiling | The provisional profile state. | Keeps recognized_ness as a ceiling without automatic access. | Acoustic match cannot exceed that ceiling. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-SIA.20.4 — Provisional evidence weighting | The provisional profile's weighting rule. | Keeps behavioral, branch, session, timing and wording dimensions heavier than acoustic match. | Conservative weighting lasts until enrollment_active. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-SIA.20.5 — Provisional restart boundary | Loss of active identity state on restart. | Returns identity to unknown. | SACL applies guest until a valid fresh assessment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 6 · DESIGNED | C-SIA.20.6 — Enrollment association strengthening | The provisional association boundary. | Strengthens the association only through the named later evidence. | Enrollment provenance does not establish identity alone. | [V10 §25.11 / What Enrollment Does Not Establish] |
| 7 · ACCEPTED | C-SIA.20.7 — Profile-commit enrollment notification | SIA's actual profile commitment. | Permits the enrollment owner to write its profile-created event only afterward. | Readiness cannot masquerade as a profile commit. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 8 · ACCEPTED | C-SIA.20.8 — Enrollment authority limits | The profile's bounded authority. | Preserves every access, mode, biometric and disclosure boundary. | A profile is evidence, never an authority replacement. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] |
| 9 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | An explicit begin action on the permanently trusted owner phone, all six prerequisites, a purpose-bound biometric token and physical enrollment observations. | Takes this place's change: supplies the linked eligible reading set and build identity [proposed] after current committed linkage. | Supplies the linked eligible reading set and build identity [proposed] after current committed linkage. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [V10 §25.11] [MAP C-ENROLL] |
| 10 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Gates this place: SIA owns actual profile creation under its rules. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: C-SIA.20.1 — Eligible enrollment reading input; C-SIA.20.2 — Provisional profile commit identity; C-SIA.20.3 — Provisional status and access ceiling; C-SIA.20.4 — Provisional evidence weighting; C-SIA.20.5 — Provisional restart boundary; C-SIA.20.6 — Enrollment association strengthening; C-SIA.20.7 — Profile-commit enrollment notification; C-SIA.20.8 — Enrollment authority limits

### C-SIA.20.1 — Eligible enrollment reading input
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The eligible accepted reading input for SIA's provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — Eligible accepted readings with honest provisional confidence and their provenance; the immutable proposed `enrollment_profile_input_bundle` names the exact reading references, eligibility decisions, operation/session references, prerequisite/authorization evidence and readiness reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Uses linked readings as one input. Accepted readings remain quarantine readings unless separately promoted normally; declared enrollment attribution remains declared. The proposed bundle is coordination only, not a profile and adds no identity evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Reading-based input under SIA's existing profile rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Use copied raw audio, logs, rejected proposals, invented `insufficient_context` readings or the proposed coordination bundle itself as a profile; create a second independent profile database; or count a reading twice in readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Unavailable readiness rules, an unverifiable counted set or a missing eligibility decision prevents both profile creation and link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): frozen eligible-reading references and proposed `enrollment_profile_readiness`, with `counted_reading_refs` as a set keyed by reading identity, one eligibility-decision reference per reading and the readiness outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: actual profile use waits for current committed Person-Box linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Readiness rules owned by SIA/profile integrity. | Determines readiness without inventing numbers, durations, thresholds, calibration values or acoustic algorithms. | Readiness produces the proposed input bundle, no profile and no profile audit event. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-ENROLL.10 — Profile readiness record | Eligible accepted quarantine readings, each linked to an eligibility decision, and the actual SIA/profile-integrity readiness rule. | Gates this place: actual profile-integrity/SIA rule and values, with no chosen number, duration, score, confidence, calibration or acoustic algorithm here. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-ENROLL.10.3 — Readiness outcome | A verifiable eligible accepted reading set and the owner's readiness rule. | Gates this place: the real readiness rule and its values. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-SIA.20.2 — Provisional profile commit identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — SIA's idempotent provisional-profile commit under interface I13. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Current committed link truth, the linked reading set, proposed input bundle and build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Commits the actual profile under SIA ownership; the build identity prevents a duplicate profile. Required security-audit events are written and flushed under their owner's rules before that owner reports success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Committed provisional profile or refusal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create duplicate profiles on replay or report profile success based on readiness, a proposal or an acknowledgment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Refused, pending, stale, contradictory or unverifiable linkage blocks creation; the response may be refused rather than committed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: the current committed-link and reading-input requirements apply before profile commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): returns SIA-owned commitment or refusal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The actual SIA commit result. | Records profile creation only after commitment. | Retries cannot fabricate duplicate profiles or earlier success. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.11.2 — Provisional profile-build identity | The committed link and its exact linked reading set. | Supplies idempotent actual profile result. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.15 — Enrollment crash recovery | The real interruption point and authoritative committed owner facts. | Supplies actual profile truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 4 · ACCEPTED | C-ENROLL.15.19 — Recovery during SIA profile creation | Whatever SIA actually committed. | Supplies actual recoverable SIA result. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 5 · ACCEPTED | C-ENROLL.6 — Enrollment process lifecycle | Actual committed facts from each stage's owner. | Supplies profile truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-SIA.20.3 — Provisional status and access ceiling
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The committed provisional profile's status and maximum access effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — A provisional profile committed by SIA after its required Person-Box link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Uses `profile_status = "enrollment_provisional"`; `recognized_ness` is the maximum achievable classification while provisional regardless of acoustic-match score. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — A profile-status ceiling for SACL, never automatic recognized_ness access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Grant recognized_ness automatically or exceed the ceiling because the acoustic match is strong. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — SACL still applies its own gates; the ceiling does not establish that even recognized_ness is reached. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: the committed profile remains provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its independent gates determine actual access within the ceiling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The provisional profile-status ceiling. | Computes actual access through its gates. | Provisional status limits access without granting it. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | SIA's committed provisional profile, with `profile_status="enrollment_provisional"`. | Supplies the provisional maximum: while the profile is `enrollment_provisional`, `recognized_ness` is the highest achievable classification regardless of acoustic-match score. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-SIA.20.4 — Provisional evidence weighting
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Conservative weighting while the profile is provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — Behavioral, branch, session-continuity, timing, wording and acoustic-match dimensions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Weights behavioral, branch, session-continuity, timing and wording dimensions more heavily than acoustic match until accepted rules move the profile to `enrollment_active`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Conservative combined identity evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Substitute strong acoustic match for the provisional weighting rule or bypass ordinary training eligibility for later enrollment material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: the provisional profile and linked-reading input. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: every subsequent contribution follows all ordinary eligibility conditions without an enrollment shortcut. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | SIA's conservatively weighted evidence. | Applies its access rules to the resulting assessment. | The evidence's maturity does not become a separate grant. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | SIA's committed provisional profile, with `profile_status="enrollment_provisional"`. | Supplies the five stronger dimensions. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-SIA.20.5 — Provisional restart boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The identity/access boundary after an SIA restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — Restart and loss of current SIA session assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Returns SIA identity to unknown; SACL applies guest until a valid fresh assessment exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Unknown identity after restart, followed only by fresh assessment evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat the existence of the provisional profile as surviving session recognition or access authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — SACL guest access remains until valid fresh assessment exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: profile existence supplies no restart-persistent recognition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): unknown identity requires guest until a fresh valid assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Unknown identity following restart. | Applies guest until valid fresh assessment. | A stored profile does not restore the lost session's authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | SIA's committed provisional profile, with `profile_status="enrollment_provisional"`. | Supplies fresh assessment requirement. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-SIA.20.6 — Enrollment association strengthening
Stamp: DESIGNED    Source: [V10 §25.11 / What Enrollment Does Not Establish]

ALONE
- What it is: DESIGNED — The gradual strengthening of a provisional enrollment association. [V10 §25.11 / What Enrollment Does Not Establish]
- Takes in: DESIGNED — Later SIA evidence, repeated authorized sessions, anti-spoofing-clean material, candidate separation and accepted profile-integrity rules. [V10 §25.11 / What Enrollment Does Not Establish]
- Does: DESIGNED — Strengthens the association only through those later evidence sources and rules. [V10 §25.11 / §7L Integration]
- Gives out: DESIGNED — A progressively supported association rather than enrollment-alone identity proof. [V10 §25.11 / What Enrollment Does Not Establish]
- Must never: DESIGNED — Treat one enrollment session or its authorized provenance as establishing that the voice belongs to Ness. [V10 §25.11 / What Enrollment Does Not Establish]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: the provisional profile begins with authorized provenance, not confirmed voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: subsequent profile evidence obeys every ordinary training condition. [V10 §25.11 / SIA Integration]
- Changes: DESIGNED — C-7L — Person-Boxes (§7L): later evidence can strengthen the provisional association under accepted profile-integrity and linking rules. [V10 §25.11 / §7L Integration]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The limited meaning of enrollment provenance. | Leaves identity strengthening to later evidence and accepted rules. | Bootstrap completion does not establish who was speaking. | [V10 §25.11 / What Enrollment Does Not Establish] |

SUB-PARTS: NONE

### C-SIA.20.7 — Profile-commit enrollment notification
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The profile-commit prerequisite for the enrollment owner's creation event and parent completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — SIA-owned committed provisional-profile truth, following the §7L-owned committed link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Permits `enrollment_provisional_profile_created` only after SIA commits. Parent `completed` requires the committed link, committed profile and both `enrollment_provisional_link_proposed` and `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Profile commitment as the enrollment component's event prerequisite. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Write the profile-created event merely on readiness or proposal existence, or complete the parent without both owner commits and both required enrollment events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Missing SIA commitment prevents the profile-created event; missing any completion requirement prevents completed parent state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: SIA's actual committed profile result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: commitment must precede event emission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): permits its owned creation event only after the profile commits. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | SIA commitment and the remaining parent-completion facts. | Writes its profile-created event after the commit and completes only with all requirements. | Audit ownership and commit ordering remain intact. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-ENROLL.6.24 — Provisional profile created state | SIA's committed profile after committed linkage, then `enrollment_provisional_profile_created`. | Supplies actual commit before event emission. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-ENROLL.14.9 — Provisional profile created enrollment event | SIA's actual committed provisional profile after committed linkage. | Gates this place: actual commitment must precede this event. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-ENROLL.6.25 — Completed parent state | All four facts: Person-Box-owned committed link, SIA-owned committed profile, `enrollment_provisional_link_proposed` and `enrollment_provisional_profile_created`. | Supplies profile commitment and event ordering. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-SIA.20.8 — Enrollment authority limits
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The authority limits on provisional enrollment and its profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Takes in: ACCEPTED — Enrollment provenance, provisional profile evidence and any requested access, mode or visible output. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Does: ACCEPTED — Preserves separate identity, biometric, access, mode, privacy, PBR and delivery ownership. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Gives out: ACCEPTED — Bounded profile evidence and status/failure output only through the privacy-first, SACL-second chain with final gates, mode-fence revalidation and no indirect disclosure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Must never: ACCEPTED — Let enrollment alone prove the voice belongs to Ness, automatically grant recognized_ness, exceed its provisional ceiling, grant top-security, create a BAI lease, open Personal Mode, turn a shared/observable channel private, replace PIN/fingerprint/SACL/PBR or another accepted factor, make voice a hard lockout or sole identity proof, authorize external actions, or bypass B-INT-5/B-INT-6. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Visible enrollment status or failure remains subject to both final output gates and the mode fence; no profile bypasses them. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20 — Provisional enrollment profile handoff: provisional evidence, not transferred authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy gate; C-SACL — Speaker Access-Control Layer (§25.4): second, final access gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): the current mode fence and accepted authentication rules remain binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The profile's authority limits. | Preserves specialist ownership and gated visible output. | Enrollment success grants no additional authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-ENROLL.12 — Enrollment authority and privacy limits | Enrollment provenance, references, provisional profile evidence and status/failure output. | Gates this place: canonical profile authority constraints. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-SIA.21 — Synthetic output voice separation
Stamp: CANDIDATE    Source: [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]

ALONE
- What it is: CANDIDATE — The distinction between N.H's synthetic speaking voice and Ness's identity/enrollment profile. [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]
- Takes in: CANDIDATE — The selection of `voices/daniel.json` as N.H's speech-output voice. [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]
- Does: CANDIDATE — Keeps that selection distinct from speaker identity assessment, access control, enrollment, acoustic-condition notes and the existing physical-observation rules for N.H's output. [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]
- Gives out: CANDIDATE — A speech-output choice that changes none of those identity/security/observation boundaries. [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]
- Must never: CANDIDATE — Treat the synthetic voice choice as a change to Ness's identity profile, enrollment evidence or access authority. [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9) | The distinct synthetic speech-output selection. | Keeps speech synthesis separate from identity/enrollment authority. | Voice output changes no SIA or enrollment rule. | [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5] |
| 2 · CANDIDATE | C-9.2.11.7.2 — Speaking voice distinct from Ness | The selected synthetic output voice. | Gates this place: output voice is not identity or enrollment authority. | Nothing in this card. | [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5] |
| 3 · CANDIDATE | C-9.2.11.8 — Speech and language-model separation | The selected speech-synthesis setup. | Gates this place: the identity distinction remains explicit. | Nothing in this card. | [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These continuation rows preserve the current TOGETHER relationships at their other endpoint. Earlier files are not edited. Future owners incorporate the rows when written; the register retains both exact endpoint names. Conditions and citations remain in the identified current field.

| USED BY owner | Using card | Current TOGETHER field | Exact current relationship | Disposition |
|---|---|---|---|---|
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-SIA — Speaker Identity Assessment (§25.3) | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): physical observation roots; C-7L — Person-Boxes (§7L): independently linked profile readings; C-BAI — Biometric Authorization Interface (§25.6): biometric evidence remains an independent factor. [V10 §25.3] [MAP C-SIA] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-SIA — Speaker Identity Assessment (§25.3) | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): physical observation roots; C-7L — Person-Boxes (§7L): independently linked profile readings; C-BAI — Biometric Authorization Interface (§25.6): biometric evidence remains an independent factor. [V10 §25.3] [MAP C-SIA] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA — Speaker Identity Assessment (§25.3) | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): physical observation roots; C-7L — Person-Boxes (§7L): independently linked profile readings; C-BAI — Biometric Authorization Interface (§25.6): biometric evidence remains an independent factor. [V10 §25.3] [MAP C-SIA] | Pending endpoint placement |
| C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting) | C-SIA — Speaker Identity Assessment (§25.3) | Gated by | DESIGNED — C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting): wellbeing is never identity or access authority; C-WIS-SEP.1 — Identity assessment is not wellbeing assessment: identity certainty stays in its own domain; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected acoustic and profile evidence remains within authorized use. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.5]; CANDIDATE — C-WIS-SEP.9 — Producing-component records: actual results and attempted or actual separation violations are recorded through the producing component's normal operational/security logging. [MAP C-SIA] [MAP C-WIS-SEP] | Pending endpoint placement |
| C-WIS-SEP.1 — Identity assessment is not wellbeing assessment | C-SIA — Speaker Identity Assessment (§25.3) | Gated by | DESIGNED — C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting): wellbeing is never identity or access authority; C-WIS-SEP.1 — Identity assessment is not wellbeing assessment: identity certainty stays in its own domain; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected acoustic and profile evidence remains within authorized use. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.5]; CANDIDATE — C-WIS-SEP.9 — Producing-component records: actual results and attempted or actual separation violations are recorded through the producing component's normal operational/security logging. [MAP C-SIA] [MAP C-WIS-SEP] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-SIA — Speaker Identity Assessment (§25.3) | Gated by | DESIGNED — C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting): wellbeing is never identity or access authority; C-WIS-SEP.1 — Identity assessment is not wellbeing assessment: identity certainty stays in its own domain; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected acoustic and profile evidence remains within authorized use. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.5]; CANDIDATE — C-WIS-SEP.9 — Producing-component records: actual results and attempted or actual separation violations are recorded through the producing component's normal operational/security logging. [MAP C-SIA] [MAP C-WIS-SEP] | Pending endpoint placement |
| C-WIS-SEP.9 — Producing-component records | C-SIA — Speaker Identity Assessment (§25.3) | Gated by | DESIGNED — C-WIS-SEP — Wellbeing / Identity / Security Separation (§25.5; cross-cutting): wellbeing is never identity or access authority; C-WIS-SEP.1 — Identity assessment is not wellbeing assessment: identity certainty stays in its own domain; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected acoustic and profile evidence remains within authorized use. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.5]; CANDIDATE — C-WIS-SEP.9 — Producing-component records: actual results and attempted or actual separation violations are recorded through the producing component's normal operational/security logging. [MAP C-SIA] [MAP C-WIS-SEP] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA — Speaker Identity Assessment (§25.3) | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): provides assessments rather than an access decision; C-TSC — Temporary Session Cache (§7E-TSC): assessment-event references support capture-time attribution without a TSC call into SIA. [V10 §25.3 / SIA Output Interface] [V10 §7E-TSC / 29. Integration Boundaries] | Pending endpoint placement |
| C-TSC — Temporary Session Cache (§7E-TSC) | C-SIA — Speaker Identity Assessment (§25.3) | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): provides assessments rather than an access decision; C-TSC — Temporary Session Cache (§7E-TSC): assessment-event references support capture-time attribution without a TSC call into SIA. [V10 §25.3 / SIA Output Interface] [V10 §7E-TSC / 29. Integration Boundaries] | Pending endpoint placement |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-SIA.1 — Identity-assessment scope | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): the observation roots assessed here. [V10 §25.3 / What SIA Is and Is Not] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.1 — Identity-assessment scope | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies assessments for its independent access decision. [V10 §25.3 / What SIA Is and Is Not] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.2.5 — Session biometric state | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): biometric-factor verification. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Pending endpoint placement |
| C-BOP.2.1 — voice_onset | C-SIA.3.2 — Stream onset reference | Fed by | DESIGNED — C-BOP.2.1 — voice_onset: the opening physical observation root ID. [V10 §25.3 / Voice Stream Record] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.4.1.1.3.7 — Device biometric state | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): evidence of the independent biometric factor. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Pending endpoint placement |
| C-WIS-SEP.6 — Acoustic spoofing security outcome | C-SIA.5 — anti_spoofing_assessment | Gated by | DESIGNED — C-WIS-SEP.6 — Acoustic spoofing security outcome: conversational divergence is excluded from acoustic suspicion. [V10 §25.3 / Anti-Spoofing Assessment Object] [V10 §25.5] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.6 — SIA_output | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies identity and suspicion evidence for access calculation. [V10 §25.3 / Multi-Speaker State] | Pending endpoint placement |
| C-BOP.2.1 — voice_onset | C-SIA.7.1 — Voice-onset assessment trigger | Fed by | DESIGNED — C-BOP.2.1 — voice_onset: the physical onset event. [V10 §25.3 / Voice Stream Record] [V10 §25.3 / Assessment Update Cadence] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.7.7 — Biometric-event trigger | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): biometric-factor events. [V10 §25.3 / Assessment Update Cadence] [MAP C-SIA] | Pending endpoint placement |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-SIA.8 — Per-stream diarization | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): voice observation roots. [V10 §25.3 / What SIA Is and Is Not] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.8 — Per-stream diarization | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies independent evidence for each stream, without choosing the access result. [V10 §25.3 / Multi-Speaker State] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-SIA.9 — Independent voice profiles | Fed by | DESIGNED — C-7L — Person-Boxes (§7L): independently linked reading sets. [V10 §25.3 / Voice Profile Architecture] | Pending endpoint placement |
| C-7L.10 — Voice-profile Person-Box linking boundary | C-SIA.9 — Independent voice profiles | Gated by | DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: unknown-speaker linkage must satisfy the decided minimum evidence and proposal rules. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-SIA.10 — Natural voice variation | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): observation roots across varied conditions. [V10 §25.3 / Natural Voice Variation]; ACCEPTED — C-SIA.10.1 — Bounded acoustic-condition context: optional physical context retains measurement provenance and no independent identity authority. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.10 — Natural voice variation | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies combined identity evidence for its own access calculation. [V10 §25.3 / Natural Voice Variation] [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-BOP.12 — Optional acoustic_condition_notes amendment | C-SIA.10.1 — Bounded acoustic-condition context | Fed by | ACCEPTED — C-BOP.12 — Optional acoustic_condition_notes amendment: the optional physical records; C-BOP.12.3 — Bounded acoustic-note downstream context: the provenance-preserving use boundary. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BOP.12.3 — Bounded acoustic-note downstream context | C-SIA.10.1 — Bounded acoustic-condition context | Fed by | ACCEPTED — C-BOP.12 — Optional acoustic_condition_notes amendment: the optional physical records; C-BOP.12.3 — Bounded acoustic-note downstream context: the provenance-preserving use boundary. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-SIA.11 — Ordinary voice-training eligibility | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): acoustic roots whose eligibility is assessed; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): readings after the normal intake and meaning path. [V10 §25.3 / Training Eligibility Rules] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-SIA.11 — Ordinary voice-training eligibility | Fed by | DESIGNED — C-BOP — Behavioral Observation Processing (§25.1/§26): acoustic roots whose eligibility is assessed; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): readings after the normal intake and meaning path. [V10 §25.3 / Training Eligibility Rules] | Pending endpoint placement |
| C-WIS-SEP.4 — Appointment records have a wellbeing-only purpose | C-SIA.11 — Ordinary voice-training eligibility | Gated by | DESIGNED — C-SIA.11.1 — Authorized training session: session authorization; C-SIA.11.2 — Capture-time training certainty: threshold met at capture; C-SIA.11.3 — Capture-time no-spoofing condition: suspicion exactly none; C-SIA.11.4 — Clean training audit history: no spoofing-related audit flag; C-SIA.11.5 — Ness training-session continuity: continuous qualifying Ness-session authority without identity uncertainty; C-SIA.11.6 — Completed reading path for training: §7E → §7G complete. [V10 §25.3 / Training Eligibility Rules]; DESIGNED — C-WIS-SEP.4 — Appointment records have a wellbeing-only purpose: appointment material is not voice-identity training evidence. [V10 §25.3 / Training Eligibility Rules] [V10 §25.5] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.11.5 — Ness training-session continuity | Fed by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the actual recognized_ness classification and its continuity; C-BAI — Biometric Authorization Interface (§25.6): biometric verification evidence. [V10 §25.3 / Training Eligibility Rules] [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.11.5 — Ness training-session continuity | Fed by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the actual recognized_ness classification and its continuity; C-BAI — Biometric Authorization Interface (§25.6): biometric verification evidence. [V10 §25.3 / Training Eligibility Rules] [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-SIA.11.6 — Completed reading path for training | Fed by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): normal intake processing; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed reading. [V10 §25.3 / Training Eligibility Rules] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-SIA.11.6 — Completed reading path for training | Fed by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): normal intake processing; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed reading. [V10 §25.3 / Training Eligibility Rules] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.12 — Conservative profile calibration | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its calculated access remains at or below the provisional-profile ceiling. [V10 §25.3 / The 6–10 Month Learning Period] [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.13 — Protected raw voice and readings | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): at least recognized_ness is required for material access; C-BAI — Biometric Authorization Interface (§25.6): transmission requires biometric verification; C-23 — Mobile App, three modes (§23): external transmission uses only the Full Mode tunnel; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected handling remains binding. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.13 — Protected raw voice and readings | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): at least recognized_ness is required for material access; C-BAI — Biometric Authorization Interface (§25.6): transmission requires biometric verification; C-23 — Mobile App, three modes (§23): external transmission uses only the Full Mode tunnel; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected handling remains binding. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-23 — Mobile App, three modes (§23) | C-SIA.13 — Protected raw voice and readings | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): at least recognized_ness is required for material access; C-BAI — Biometric Authorization Interface (§25.6): transmission requires biometric verification; C-23 — Mobile App, three modes (§23): external transmission uses only the Full Mode tunnel; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected handling remains binding. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-SIA.13 — Protected raw voice and readings | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): at least recognized_ness is required for material access; C-BAI — Biometric Authorization Interface (§25.6): transmission requires biometric verification; C-23 — Mobile App, three modes (§23): external transmission uses only the Full Mode tunnel; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected handling remains binding. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.14 — Uncertainty and spoofing responses | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): applies access changes from the distinct assessed conditions. [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.14.3 — Medium-or-high-spoofing response | Changes | DESIGNED — C-SIA.14 — Uncertainty and spoofing responses: supplies the medium/high acoustic branch; C-SACL — Speaker Access-Control Layer (§25.4): the assessed suspicion requires immediate guest/relock and private-alert handling. [V10 §25.3 / Identity Uncertain vs. Spoofing Suspected] [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.15 — False lockout recovery | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): thumbprint verification of the biometric factor. [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.15 — False lockout recovery | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): top-security restoration requires all independent conditions, not the fingerprint alone. [V10 §25.3 / False Lockout Recovery] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.15 — False lockout recovery | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies updated speaker evidence alongside the biometric factor. [V10 §25.3 / Settled Rules] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.16 — Multi-speaker evidence handoff | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies the stream evidence; SACL owns per-stream and shared-output calculations. [V10 §25.3 / Multi-Speaker State] | Pending endpoint placement |
| C-TSC — Temporary Session Cache (§7E-TSC) | C-SIA.17 — Unknown-speaker linking evidence | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion provenance; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): supporting readings. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-SIA.17 — Unknown-speaker linking evidence | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion provenance; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): supporting readings. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.1 — Unknown-speaker attributed-material minimum | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.2 — Unknown-speaker capture-time certainty minimum | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.3 — Unknown-speaker no-spoofing condition | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.4 — Unknown-speaker authorized-promotion condition | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.5 — Unknown-speaker reading-confidence minimum | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L.10.6 — Unknown-speaker Person-Box rule condition | C-SIA.17 — Unknown-speaker linking evidence | Gated by | DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: minimum quantity across authorized sessions; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: certainty above minimum at capture; C-7L.10.3 — Unknown-speaker no-spoofing condition: no spoofing flags on the material; C-7L.10.4 — Unknown-speaker authorized-promotion condition: fingerprint-authorized promotion and §7G processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading support above minimum confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: proposal rules and no silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-SIA.17 — Unknown-speaker linking evidence | Changes | DESIGNED — C-7L — Person-Boxes (§7L): supplies eligible identity evidence without granting silent-link authority. [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-SIA.18 — Compact inference representation | Fed by | DESIGNED — C-7L — Person-Boxes (§7L): the linked authoritative profile-reading set. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Compact Profile Representation] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-SIA.18 — Compact inference representation | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the derived representation remains locally protected under the source material's protection rules. [V10 §25.3 / Raw Voice Data Protection] [V10 §25.3 / Compact Profile Representation] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-SIA.19 — Assessment records and TSC references | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): operational-record access requires its applicable privacy authorization; C-SACL — Speaker Access-Control Layer (§25.4): voice/identity operational records require at least recognized_ness and the applicable identity/security authorization. [MAP C-SIA] [V10 §0B] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.19 — Assessment records and TSC references | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): operational-record access requires its applicable privacy authorization; C-SACL — Speaker Access-Control Layer (§25.4): voice/identity operational records require at least recognized_ness and the applicable identity/security authorization. [MAP C-SIA] [V10 §0B] | Pending endpoint placement |
| C-TSC.9.2 — SIA event link record | C-SIA.19 — Assessment records and TSC references | Changes | DESIGNED — C-TSC.9.2 — SIA event link record: links existing audit-event IDs with session/contribution timing; C-TSC.29.3 — SIA reference boundary: retains reference-only use without a TSC call into SIA. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] [V10 §7E-TSC / 29. Integration Boundaries] | Pending endpoint placement |
| C-TSC.29.3 — SIA reference boundary | C-SIA.19 — Assessment records and TSC references | Changes | DESIGNED — C-TSC.9.2 — SIA event link record: links existing audit-event IDs with session/contribution timing; C-TSC.29.3 — SIA reference boundary: retains reference-only use without a TSC call into SIA. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] [V10 §7E-TSC / 29. Integration Boundaries] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20 — Provisional enrollment profile handoff | Fed by | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligible accepted reading references, proposed coordination bundle and build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11.13 — Enrollment committed-link handoff gate | C-SIA.20 — Provisional enrollment profile handoff | Gated by | ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current §7L-owned committed link to Ness's confirmed Person-Box is required before profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20 — Provisional enrollment profile handoff | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): only SIA's actual commit permits the profile-created enrollment event; C-SACL — Speaker Access-Control Layer (§25.4): receives assessments under the normal boundary, with a provisional ceiling rather than a grant. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.20 — Provisional enrollment profile handoff | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): only SIA's actual commit permits the profile-created enrollment event; C-SACL — Speaker Access-Control Layer (§25.4): receives assessments under the normal boundary, with a provisional ceiling rather than a grant. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.1 — Eligible enrollment reading input | Fed by | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): frozen eligible-reading references and proposed `enrollment_profile_readiness`, with `counted_reading_refs` as a set keyed by reading identity, one eligibility-decision reference per reading and the readiness outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.2 — Provisional profile commit identity | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): returns SIA-owned commitment or refusal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.20.3 — Provisional status and access ceiling | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its independent gates determine actual access within the ceiling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.20.5 — Provisional restart boundary | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): unknown identity requires guest until a fresh valid assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-SIA.20.6 — Enrollment association strengthening | Changes | DESIGNED — C-7L — Person-Boxes (§7L): later evidence can strengthen the provisional association under accepted profile-integrity and linking rules. [V10 §25.11 / §7L Integration] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.7 — Profile-commit enrollment notification | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): permits its owned creation event only after the profile commits. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-SIA.20.8 — Enrollment authority limits | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy gate; C-SACL — Speaker Access-Control Layer (§25.4): second, final access gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): the current mode fence and accepted authentication rules remain binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-SIA.20.8 — Enrollment authority limits | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy gate; C-SACL — Speaker Access-Control Layer (§25.4): second, final access gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): the current mode fence and accepted authentication rules remain binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-SIA.20.8 — Enrollment authority limits | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy gate; C-SACL — Speaker Access-Control Layer (§25.4): second, final access gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): the current mode fence and accepted authentication rules remain binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] | Pending endpoint placement |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-SIA — Speaker Identity Assessment (§25.3) | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | 1 · DESIGNED | [V10 §25.3 / Multi-Speaker State] [MAP C-SIA] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | 2 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.6 — Participant record | 3 · DESIGNED | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.6.10 — sia_stream_id_ref | 4 · DESIGNED | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.7 — Attribution assessment | 5 · DESIGNED | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.7.11 — sia_assessment_event_id | 6 · DESIGNED | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.9 — BOP and SIA links | 7 · DESIGNED | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.9.2 — SIA event link record | 8 · DESIGNED | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.9.2.3 — sia_assessment_event_id | 9 · DESIGNED | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-TSC.29.3 — SIA reference boundary | 10 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L — Person-Boxes (§7L) | 11 · DESIGNED | [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L.10 — Voice-profile Person-Box linking boundary | 12 · DESIGNED | [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L.10.2 — Unknown-speaker capture-time certainty minimum | 13 · DESIGNED | [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L.10.3 — Unknown-speaker no-spoofing condition | 14 · DESIGNED | [V10 §25.3 / Minimum Evidence for Person-Box Linking] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L.11 — Provisional enrollment Person-Box link | 15 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7L.11.13 — Enrollment committed-link handoff gate | 16 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | 17 · DESIGNED | [V10 §25.2 / Continuous Speaker Security] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-OTHER.12 — Continuous speaker security | 18 · DESIGNED | [V10 §25.2 / Continuous Speaker Security] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-WIS-SEP.3 — Access decisions exclude wellbeing | 19 · DESIGNED | [V10 §25.5] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-WIS-SEP.5 — Temporary behavioral divergence | 20 · DESIGNED | [V10 §25.5] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-WIS-SEP.6 — Acoustic spoofing security outcome | 21 · DESIGNED | [V10 §25.3 / Anti-Spoofing Assessment Object] [V10 §25.5] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | 22 · DESIGNED | [V10 §7Q] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7Q.11.2 — Established identity and private-context boundary | 23 · ACCEPTED | [04/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md §4] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-2.15.3.2 — Record identity boundary | 24 · DESIGNED | [MAP C-2] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7B.10.8.4 — Identity and security condition | 25 · DESIGNED | [V10 §0B] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-LEARN.10 — Protected connected learning-operation history | 26 · DESIGNED | [V10 §0B] [MAP C-LEARN] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7R.15.7 — Declaration Logging / audit requirement | 27 · ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-OOP.10 — Outcome and route operational logging | 28 · DESIGNED | [V10 §0B] [MAP C-OOP] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-7P.2.6 — Strictest-rule and specialist authority boundary | 29 · ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-LMAC.8.4 — Control-query identity access purpose and logging | 30 · ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-LMAC.11.4 — Shared operational logging and access protection | 31 · ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | 32 · DESIGNED | [V10 §0B] [MAP C-AFFIRM] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-AFFIRM.8 — Protected append-only affirmation living record | 33 · ACCEPTED | [V10 §0B] [MAP C-AFFIRM] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-BOP.12.3 — Bounded acoustic-note downstream context | 34 · ACCEPTED | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] | Existing TOGETHER relationship checked in earlier card |
| C-SIA — Speaker Identity Assessment (§25.3) | C-BOP.16 — Shared observation logging and protected access | 35 · DESIGNED | [V10 §0B] [MAP C-BOP] | Existing TOGETHER relationship checked in earlier card |
| C-SIA.1 — Identity-assessment scope | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | 1 · DESIGNED | [V10 §25.3 / What SIA Is and Is Not] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.8 — Per-stream diarization | C-TSC — Temporary Session Cache (§7E-TSC) | 1 · DESIGNED | [V10 §7E-TSC / 6. Participant and Speaker-Attribution Record Schema] [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.9 — Independent voice profiles | C-7L — Person-Boxes (§7L) | 1 · DESIGNED | [V10 §25.3 / Voice Profile Architecture] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.12 — Conservative profile calibration | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [V10 §25.11 / SIA Integration] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.13 — Protected raw voice and readings | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [V10 §25.3 / Raw Voice Data Protection] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.15 — False lockout recovery | C-BAI — Biometric Authorization Interface (§25.6) | 1 · DESIGNED | [V10 §25.3 / False Lockout Recovery] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.16 — Multi-speaker evidence handoff | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | 1 · DESIGNED | [V10 §25.3 / Multi-Speaker State] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.17 — Unknown-speaker linking evidence | C-7L.10 — Voice-profile Person-Box linking boundary | 1 · DESIGNED | [V10 §25.3 / Minimum Evidence for Person-Box Linking] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.18 — Compact inference representation | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.3 / Compact Profile Representation] [V10 §25.3 / Settled Rules] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.19 — Assessment records and TSC references | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | 1 · DESIGNED | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.1 — Eligible enrollment reading input | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.3 — Provisional status and access ceiling | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.4 — Provisional evidence weighting | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.5 — Provisional restart boundary | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.6 — Enrollment association strengthening | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [V10 §25.11 / What Enrollment Does Not Establish] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.7 — Profile-commit enrollment notification | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.20.8 — Enrollment authority limits | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 1 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-SIA.21 — Synthetic output voice separation | C-9 — Access/authentication model + voice I/O + phone modes (§9) | 1 · DESIGNED | [05/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md §5] | TOGETHER continuation at using endpoint; preserve current use and its source |

## Source-to-card coverage added by CH09-c

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

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-SIA — Speaker Identity Assessment (§25.3) | USED BY row 66 / Takes in there |
| C-SIA — Speaker Identity Assessment (§25.3) | USED BY row 97 / Takes in there |
| C-SIA.1 — Identity-assessment scope | Fails closed by |
| C-SIA.1 — Identity-assessment scope | Gated by |
| C-SIA.2 — speaker_session_state | Gated by |
| C-SIA.2.1 — Session identity | Must never |
| C-SIA.2.1 — Session identity | Fails closed by |
| C-SIA.2.1 — Session identity | Fed by |
| C-SIA.2.1 — Session identity | Gated by |
| C-SIA.2.2 — Session mode | Must never |
| C-SIA.2.2 — Session mode | Fails closed by |
| C-SIA.2.2 — Session mode | Fed by |
| C-SIA.2.2 — Session mode | Gated by |
| C-SIA.2.3 — Active voice stream set | Fails closed by |
| C-SIA.2.3 — Active voice stream set | Gated by |
| C-SIA.2.4 — Primary addressed stream | Fails closed by |
| C-SIA.2.4 — Primary addressed stream | Fed by |
| C-SIA.2.4 — Primary addressed stream | Gated by |
| C-SIA.2.5 — Session biometric state | Fails closed by |
| C-SIA.2.5 — Session biometric state | Gated by |
| C-SIA.2.6 — Biometric verification time | Fails closed by |
| C-SIA.2.6 — Biometric verification time | Fed by |
| C-SIA.2.6 — Biometric verification time | Gated by |
| C-SIA.2.7 — Session assessment history | Fed by |
| C-SIA.2.7 — Session assessment history | Gated by |
| C-SIA.3 — voice_stream_record | Fails closed by |
| C-SIA.3 — voice_stream_record | Gated by |
| C-SIA.3 — voice_stream_record | Changes |
| C-SIA.3.1 — Stream identity | Must never |
| C-SIA.3.1 — Stream identity | Fails closed by |
| C-SIA.3.1 — Stream identity | Fed by |
| C-SIA.3.1 — Stream identity | Gated by |
| C-SIA.3.2 — Stream onset reference | Must never |
| C-SIA.3.2 — Stream onset reference | Fails closed by |
| C-SIA.3.2 — Stream onset reference | Gated by |
| C-SIA.3.3 — Stream speaker assessment | Gated by |
| C-SIA.3.4 — Stream anti-spoofing assessment | Fails closed by |
| C-SIA.3.4 — Stream anti-spoofing assessment | Gated by |
| C-SIA.3.5 — Stream status | Must never |
| C-SIA.3.5 — Stream status | Fails closed by |
| C-SIA.3.5 — Stream status | Fed by |
| C-SIA.3.5 — Stream status | Gated by |
| C-SIA.3.6 — Last assessment time | Must never |
| C-SIA.3.6 — Last assessment time | Fails closed by |
| C-SIA.3.6 — Last assessment time | Fed by |
| C-SIA.3.6 — Last assessment time | Gated by |
| C-SIA.3.7 — Last assessment trigger | Must never |
| C-SIA.3.7 — Last assessment trigger | Fails closed by |
| C-SIA.3.7 — Last assessment trigger | Gated by |
| C-SIA.4 — speaker_assessment | Gated by |
| C-SIA.4 — speaker_assessment | Changes |
| C-SIA.4.1 — Ranked identity candidates | Fails closed by |
| C-SIA.4.1 — Ranked identity candidates | Gated by |
| C-SIA.4.1.1 — Identity candidate record | Fails closed by |
| C-SIA.4.1.1 — Identity candidate record | Gated by |
| C-SIA.4.1.1.1 — Candidate Person-Box identity | Must never |
| C-SIA.4.1.1.1 — Candidate Person-Box identity | Fails closed by |
| C-SIA.4.1.1.1 — Candidate Person-Box identity | Fed by |
| C-SIA.4.1.1.1 — Candidate Person-Box identity | Gated by |
| C-SIA.4.1.1.2 — Candidate match score | Must never |
| C-SIA.4.1.1.2 — Candidate match score | Fails closed by |
| C-SIA.4.1.1.2 — Candidate match score | Fed by |
| C-SIA.4.1.1.2 — Candidate match score | Gated by |
| C-SIA.4.1.1.3 — Candidate evidence dimensions | Fails closed by |
| C-SIA.4.1.1.3 — Candidate evidence dimensions | Gated by |
| C-SIA.4.1.1.3.1 — Voice acoustic match | Fails closed by |
| C-SIA.4.1.1.3.1 — Voice acoustic match | Fed by |
| C-SIA.4.1.1.3.1 — Voice acoustic match | Gated by |
| C-SIA.4.1.1.3.2 — Behavioral pattern match | Fails closed by |
| C-SIA.4.1.1.3.2 — Behavioral pattern match | Fed by |
| C-SIA.4.1.1.3.2 — Behavioral pattern match | Gated by |
| C-SIA.4.1.1.3.3 — Branch continuity score | Fails closed by |
| C-SIA.4.1.1.3.3 — Branch continuity score | Fed by |
| C-SIA.4.1.1.3.3 — Branch continuity score | Gated by |
| C-SIA.4.1.1.3.4 — Session continuity score | Must never |
| C-SIA.4.1.1.3.4 — Session continuity score | Fails closed by |
| C-SIA.4.1.1.3.4 — Session continuity score | Fed by |
| C-SIA.4.1.1.3.4 — Session continuity score | Gated by |
| C-SIA.4.1.1.3.5 — Timing rhythm score | Fails closed by |
| C-SIA.4.1.1.3.5 — Timing rhythm score | Fed by |
| C-SIA.4.1.1.3.5 — Timing rhythm score | Gated by |
| C-SIA.4.1.1.3.6 — Wording pattern score | Fails closed by |
| C-SIA.4.1.1.3.6 — Wording pattern score | Fed by |
| C-SIA.4.1.1.3.6 — Wording pattern score | Gated by |
| C-SIA.4.1.1.3.7 — Device biometric state | Fails closed by |
| C-SIA.4.1.1.3.7 — Device biometric state | Gated by |
| C-SIA.4.1.1.4 — Candidate uncertainty flags | Fails closed by |
| C-SIA.4.1.1.4 — Candidate uncertainty flags | Fed by |
| C-SIA.4.1.1.4 — Candidate uncertainty flags | Gated by |
| C-SIA.4.1.1.5 — Candidate profile status | Must never |
| C-SIA.4.1.1.5 — Candidate profile status | Fails closed by |
| C-SIA.4.1.1.5 — Candidate profile status | Fed by |
| C-SIA.4.1.1.5 — Candidate profile status | Gated by |
| C-SIA.4.2 — Assessed Person-Box identity | Fed by |
| C-SIA.4.2 — Assessed Person-Box identity | Gated by |
| C-SIA.4.3 — Assessed identity certainty | Fed by |
| C-SIA.4.3 — Assessed identity certainty | Gated by |
| C-SIA.4.4 — Active identity flags | Fails closed by |
| C-SIA.4.4 — Active identity flags | Fed by |
| C-SIA.4.4 — Active identity flags | Gated by |
| C-SIA.4.5 — Leading profile status | Must never |
| C-SIA.4.5 — Leading profile status | Fails closed by |
| C-SIA.4.5 — Leading profile status | Fed by |
| C-SIA.4.5 — Leading profile status | Gated by |
| C-SIA.5 — anti_spoofing_assessment | Fails closed by |
| C-SIA.5 — anti_spoofing_assessment | Changes |
| C-SIA.5.1 — Acoustic suspicion level | Fails closed by |
| C-SIA.5.1 — Acoustic suspicion level | Fed by |
| C-SIA.5.1 — Acoustic suspicion level | Gated by |
| C-SIA.5.2 — Acoustic suspicion basis | Fails closed by |
| C-SIA.5.2 — Acoustic suspicion basis | Fed by |
| C-SIA.5.2 — Acoustic suspicion basis | Gated by |
| C-SIA.5.3 — Acoustic suspicion source | Must never |
| C-SIA.5.3 — Acoustic suspicion source | Fails closed by |
| C-SIA.5.3 — Acoustic suspicion source | Fed by |
| C-SIA.5.3 — Acoustic suspicion source | Gated by |
| C-SIA.5.4 — Acoustic assessment certainty | Must never |
| C-SIA.5.4 — Acoustic assessment certainty | Fails closed by |
| C-SIA.5.4 — Acoustic assessment certainty | Fed by |
| C-SIA.5.4 — Acoustic assessment certainty | Gated by |
| C-SIA.6 — SIA_output | Fails closed by |
| C-SIA.6 — SIA_output | Gated by |
| C-SIA.6.1 — Output speaker session state | Fails closed by |
| C-SIA.6.1 — Output speaker session state | Fed by |
| C-SIA.6.1 — Output speaker session state | Gated by |
| C-SIA.6.2 — Assessment event identity | Must never |
| C-SIA.6.2 — Assessment event identity | Fails closed by |
| C-SIA.6.2 — Assessment event identity | Fed by |
| C-SIA.6.2 — Assessment event identity | Gated by |
| C-SIA.6.3 — Assessment confidence note | Fails closed by |
| C-SIA.6.3 — Assessment confidence note | Fed by |
| C-SIA.6.3 — Assessment confidence note | Gated by |
| C-SIA.7 — Assessment update cadence | Must never |
| C-SIA.7 — Assessment update cadence | Fails closed by |
| C-SIA.7 — Assessment update cadence | Gated by |
| C-SIA.7 — Assessment update cadence | Changes |
| C-SIA.7.1 — Voice-onset assessment trigger | Must never |
| C-SIA.7.1 — Voice-onset assessment trigger | Fails closed by |
| C-SIA.7.1 — Voice-onset assessment trigger | Gated by |
| C-SIA.7.2 — Periodic acoustic-window trigger | Must never |
| C-SIA.7.2 — Periodic acoustic-window trigger | Fails closed by |
| C-SIA.7.2 — Periodic acoustic-window trigger | Fed by |
| C-SIA.7.2 — Periodic acoustic-window trigger | Gated by |
| C-SIA.7.3 — Meaningful acoustic-change trigger | Must never |
| C-SIA.7.3 — Meaningful acoustic-change trigger | Fails closed by |
| C-SIA.7.3 — Meaningful acoustic-change trigger | Fed by |
| C-SIA.7.3 — Meaningful acoustic-change trigger | Gated by |
| C-SIA.7.4 — Overlap-detected trigger | Fails closed by |
| C-SIA.7.4 — Overlap-detected trigger | Fed by |
| C-SIA.7.4 — Overlap-detected trigger | Gated by |
| C-SIA.7.5 — Speaker-transition trigger | Must never |
| C-SIA.7.5 — Speaker-transition trigger | Fails closed by |
| C-SIA.7.5 — Speaker-transition trigger | Fed by |
| C-SIA.7.5 — Speaker-transition trigger | Gated by |
| C-SIA.7.6 — Confirmed-text trigger | Must never |
| C-SIA.7.6 — Confirmed-text trigger | Fails closed by |
| C-SIA.7.6 — Confirmed-text trigger | Fed by |
| C-SIA.7.6 — Confirmed-text trigger | Gated by |
| C-SIA.7.7 — Biometric-event trigger | Fails closed by |
| C-SIA.7.7 — Biometric-event trigger | Gated by |
| C-SIA.7.8 — Session-state-change trigger | Must never |
| C-SIA.7.8 — Session-state-change trigger | Fails closed by |
| C-SIA.7.8 — Session-state-change trigger | Fed by |
| C-SIA.7.8 — Session-state-change trigger | Gated by |
| C-SIA.8 — Per-stream diarization | Gated by |
| C-SIA.9 — Independent voice profiles | Fails closed by |
| C-SIA.9 — Independent voice profiles | Changes |
| C-SIA.10 — Natural voice variation | Fails closed by |
| C-SIA.10 — Natural voice variation | Gated by |
| C-SIA.10.1 — Bounded acoustic-condition context | Fails closed by |
| C-SIA.10.1 — Bounded acoustic-condition context | Gated by |
| C-SIA.11 — Ordinary voice-training eligibility | Changes |
| C-SIA.11.1 — Authorized training session | Fed by |
| C-SIA.11.1 — Authorized training session | Gated by |
| C-SIA.11.2 — Capture-time training certainty | Fed by |
| C-SIA.11.2 — Capture-time training certainty | Gated by |
| C-SIA.11.3 — Capture-time no-spoofing condition | Fed by |
| C-SIA.11.3 — Capture-time no-spoofing condition | Gated by |
| C-SIA.11.4 — Clean training audit history | Fed by |
| C-SIA.11.4 — Clean training audit history | Gated by |
| C-SIA.11.5 — Ness training-session continuity | Gated by |
| C-SIA.11.6 — Completed reading path for training | Gated by |
| C-SIA.12 — Conservative profile calibration | Fails closed by |
| C-SIA.12 — Conservative profile calibration | Fed by |
| C-SIA.12 — Conservative profile calibration | Gated by |
| C-SIA.13 — Protected raw voice and readings | Fed by |
| C-SIA.13 — Protected raw voice and readings | Changes |
| C-SIA.14 — Uncertainty and spoofing responses | Gated by |
| C-SIA.14.1 — Identity-uncertain response | Fed by |
| C-SIA.14.1 — Identity-uncertain response | Gated by |
| C-SIA.14.2 — Low-spoofing response | Fed by |
| C-SIA.14.2 — Low-spoofing response | Gated by |
| C-SIA.14.3 — Medium-or-high-spoofing response | Fed by |
| C-SIA.14.3 — Medium-or-high-spoofing response | Gated by |
| C-SIA.16 — Multi-speaker evidence handoff | Fails closed by |
| C-SIA.16 — Multi-speaker evidence handoff | Fed by |
| C-SIA.16 — Multi-speaker evidence handoff | Gated by |
| C-SIA.18 — Compact inference representation | Changes |
| C-SIA.19 — Assessment records and TSC references | Fed by |
| C-SIA.20.1 — Eligible enrollment reading input | Changes |
| C-SIA.20.2 — Provisional profile commit identity | Fed by |
| C-SIA.20.3 — Provisional status and access ceiling | Changes |
| C-SIA.20.4 — Provisional evidence weighting | Fails closed by |
| C-SIA.20.4 — Provisional evidence weighting | Changes |
| C-SIA.20.5 — Provisional restart boundary | Gated by |
| C-SIA.20.6 — Enrollment association strengthening | Fails closed by |
| C-SIA.20.8 — Enrollment authority limits | Changes |
| C-SIA.21 — Synthetic output voice separation | Fails closed by |
| C-SIA.21 — Synthetic output voice separation | Fed by |
| C-SIA.21 — Synthetic output voice separation | Gated by |
| C-SIA.21 — Synthetic output voice separation | Changes |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. Each positive scan hit below is retained for its named reason.

| Card / line | Flag | Reason |
|---|---|---|
| C-SIA.3.3 — Stream speaker assessment; line 448 | prerequisite_review / Gated by | The 'require' hit describes the nested identity object's intrinsic minimum-certainty/separation rule. Fails closed by already carries its null result; this field card has no separate outside gate. Its record producer and containing stream are explicitly linked. |
| C-SIA.11.1 — Authorized training session; line 1572 | prerequisite_review / Gated by | Authorized-session status is this condition card's own predicate, not an extra gate on the predicate. Its failure outcome is filled and the parent lists it as a gate. No additional enforcement is invented. |
| C-SIA.11.2 — Capture-time training certainty; line 1595 | prerequisite_review / Gated by | The capture-time threshold is this card's comparison, so it stays in Does. Fails closed by rejects below-threshold contribution and the parent names this condition as a gate; no separate external gate is stated. |
| C-SIA.11.3 — Capture-time no-spoofing condition; line 1618 | prerequisite_review / Gated by | Exactly-none suspicion defines this condition. Its failure outcome and parent gate are explicit. The condition is not turned into a second gate on itself. |
| C-SIA.11.4 — Clean training audit history; line 1641 | prerequisite_review / Gated by | Absence of spoofing-related audit flags is this condition's own test. Fails closed by carries the blocked contribution and the parent names this condition as a gate. |
| C-SIA.11.5 — Ness training-session continuity; line 1664 | prerequisite_review / Gated by | The required Ness-session evidence is the intrinsic condition. Actual SACL and biometric producers are named, failure is explicit and the parent uses the condition as a gate; no additional authority is specified. |
| C-SIA.11.6 — Completed reading path for training; line 1687 | prerequisite_review / Gated by | Completion before contribution defines this condition. Intake/reading producers are named, Fails closed by blocks incomplete processing and the parent lists the condition as a gate. The condition has no second external prerequisite in source. |
| C-SIA.14.3 — Medium-or-high-spoofing response; line 1828 | prerequisite_review / Gated by | The word 'requires' introduces the required guest/relock/alert outcome after medium/high suspicion; it is not a precondition that can gate that response. Fails closed by and the SACL change link already carry the response. |
| C-SIA.20.5 — Provisional restart boundary; line 2100 | prerequisite_review / Gated by | The fresh-assessment requirement belongs to SACL's later access calculation, explicitly carried in Does, Fails closed by and the Changes link. It does not gate SIA's unconditional reset to unknown on restart. |
| C-SIA.21 — Synthetic output voice separation; line 2196 | empty_together | This is the candidate decision record's separation invariant, not an executable step or a producer/consumer mechanism. The source states no external input, authorizer or state mutation for the invariant; the actual speech-output consumer is preserved as a cross-piece use. No mechanism is invented to fill TOGETHER. |

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

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §25.3 and §25.11; §7E-TSC complete §§6/7/9 and SIA boundary in §29; §0B/§25.5 governing boundaries retained from earlier current-round reads. No whole-file credit. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-SIA, complete adjacent C-SACL discovery, C-WIS-SEP record law and existing component logging dependencies. No whole-file credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete embedded §3 SIA, including the opening recovered in a bounded follow-up; no whole-file credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Whole-file reread; all field/value/context/provenance/must-never boundaries checked. Existing whole-read credit retained. | `9010e9e7b66118436acaa90bb0bf3e681b5aef229b06dbbc792563b85c859a6c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole receipt reread; acceptance evidence, not a new claim about implementation. | `3db1015eabf7f157fff4c48a81ed4e1e70c992b4eb6eecc95ae35f5059c32e15` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Scoped: complete §§11–16 and §§18–19, including all interfaces. Current profile consumer written; full coordinator lifecycle and its proposed records remain CH09-h. No whole-file credit. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole receipt reread; acceptance and frozen notes retained; conditional independent formal-closeout audit not asserted complete. | `df028286c89b7c0a4bea3bb1403d910b11f993bac010d03320f55eeec71d636a` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped: complete §13 retrieval/output handoff; no SIA access authority inferred. Full mode owner remains CH09-i. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Scoped: complete §§4.1–4.3, identity ownership and authenticated private-context boundary. Prior whole read not claimed repeated. | `41e1f67d635a0e07a73ad572e8931bceaffd3cf6f44d88c3eaea9872818d339b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped: complete §5 Path 7 enrollment consistency boundary and discovery of relevant package/authority rows; remaining whole-file obligation retained. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped: §5 table items 3–7, participant/attribution/branch/BOP/SIA references; existing TSC atoms retained. | `46cf463389ea339bb3a908177dda8d1548095e21da6abebcd2efeb6a8a54c0ff` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: complete §5.6 shared logging and its identity/security boundary for existing declaration consumer. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Scoped: complete §9.1; specialist identity/security authority retained, underlying authority atoms remain CH07-c. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: complete §§3/12 for existing LMAC logging and control-query consumers; no other bundle behavior re-owned here. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | Whole file read; §5 separation placed here at CANDIDATE status, speech setup reserved for CH09-i/CH10-d. Closes one inherited pending whole read. | `af3c531803f8988f8131061d4d61f8856f1156c2e83dc95dc65dd4597a779cfd` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Discovery only: SIA governing-law and source-list matches; no new SIA behavior imported and no whole-file credit. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |

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

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

53 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
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

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)

§1.3 no history/actions/roles/workflow in this chapter: PASS — checked the entire behavior block. The records and rules describe N.H operation; delivery metadata is outside that block. The whole behavior scan found 0 workflow hits.

§1.4 every gap written as NOT DECIDED: PASS — 209 empty fields and 2 empty USED BY cells are exactly NOT DECIDED and all 211 appear in this piece's Appendix A carry-forward; no populated field remains in that register and no filled field contains mixed gap text.

§1.5 conflicts marked, none resolved: PASS — the V10 proposed acoustic-note wording versus accepted A15 status is marked in the header and C-SIA.10; the Gate-2 imitation-risk wording conflict remains in the header for CH09-d and Appendix D. No access gate is reconciled here.

§3 exactly one stamp per line: PASS — checked all 788 field lines and 272 USED BY rows. Populated lines carry one applicable stamp; named-target lines take the target's status. There are 0 BUILT lines and 1 DECIDED-2026-09-25 line (the USED BY row for C-READ.8, which cites the deciding buckets record) in the behavior block.

§4 every behavior line cited in the exact format: PASS — all populated fields and use rows are cited; all 95 distinct citation locations resolve in the pinned local source files. Source claims were compared with the scoped passages in the READ RECORD. Empty fields carry no citation.

§5.4 one name per thing: PASS — all target names match the earlier naming/card indexes or the current cards. Existing acoustic-note, TSC and Person-Box atoms retain their canonical identities. No new top-level component or path ID is introduced.

§6 all template fields present, in order, for every part: PASS — 87 cards, 788 field lines, all nine fields present in the required order. Repeated field labels separate source/target statuses. Every USED BY row names one using part and at most one path; no card lists itself in SUB-PARTS.

§6.3 reciprocity within this chapter: PASS — all 130 internal TOGETHER relationships have their reverse USED BY entries, and all internal uses have a forward relationship. The 72 outgoing relationships and 54 of the 143 external uses have 126 rows naming both endpoints; the other 89 external uses are answered by the using cards' own TOGETHER lines. All 35 earlier TOGETHER references to the C-SIA root have current root USED BY rows. Earlier bytes remain unchanged; further cross-piece obligations are explicit.

§6.4 every decided detail written in, no citation used in place of content: PASS for the mapped SIA scope — 92 selected source names/values checked present with 0 missing; the 20 source-map rows account for all covered sections. Every session, stream, candidate, evidence, acoustic and output field is written; cadence, thresholds' named boundaries, eligible inputs, protection, three response classes, restart and profile handoff are stated. Full enrollment coordination, mode wiring and access/delivery mechanics remain with their named later owners, not claimed complete here.

§6.5 sub-parts recursed to the bottom: PASS — SSS, stream, candidate, dimension, acoustic and output records recurse into field cards; eight triggers, six ordinary training conditions and three response branches each have cards. Existing six Person-Box condition cards are reused. Values remain on their owning field cards; no unprovided transition, threshold or enforcement mechanism is invented.

§9 coverage matrix rows added for every file used: PASS — 20 current source-placement rows supplement the cumulative 145-file inventory; every inventory path exists at the pin. The READ RECORD has 16 source fingerprints, full instruction/carry-forward fingerprints and all 48 preceding chapter fingerprints. One new whole-file read closes one inherited obligation; 53 pending whole-file obligations remain explicitly listed.

§10.11 no recommendation, no sentence addressed to Ness: PASS — whole behavior scan and manual wording review; 0 recommendation/formula hits, 0 wording hits, 0 empty stamps, 0 mixed-gap lines. Ness's acts mentioned in source-derived behavior are system preconditions or inputs, not instructions to the reader.

Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (three rereads); `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` (new whole read). Full hashes and actual scoped reads are in the READ RECORD.

Lessons §§8/11 additional checks: PASS — all 788 boxes and all 272 use rows reviewed for misplaced restrictions/gates/failure behavior, including 261 distinct Must never/Fails closed by/Gated by slots across 264 such lines. Ten positive flags are named by card, line, field and reason in Named review dispositions: nine intrinsic-condition/outcome prerequisite hits and one non-executable separation invariant with empty TOGETHER. There are no unnamed exceptions. No behavior box was generated by script; scripts counted, checked identifiers/citations/hashes and assembled metadata only. All totals above were recounted from the finished file. These are writer checks, not an independent audit or adoption claim.
