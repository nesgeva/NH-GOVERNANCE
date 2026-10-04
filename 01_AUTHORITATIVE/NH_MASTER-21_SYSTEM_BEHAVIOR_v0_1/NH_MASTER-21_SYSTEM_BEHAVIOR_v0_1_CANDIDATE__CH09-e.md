# Chapter 9-e — Group G: C-BAI

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-e.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers C-BAI's OS-result boundary, purpose-bound pending state, one-time tokens, revocable leases, key separation, audit ownership and accepted consumer interfaces. Existing TSC, BOP and evaluation field/protocol cards retain their canonical IDs. Full maintenance, device trust, enrollment and access-mode owners remain CH09-f, CH09-g, CH09-h and CH09-i respectively; the complete execution kernel remains CH10-b. Conditional evaluation mechanics do not select the still-open NHD-B16EEB-D16 option or scope. B-INT-5 §5B prints the proposed purpose with `<personal_mode_open_operation_id>`; §§6 and 17 print `<open_operation_id>`. Both source spellings are retained without selecting a serialization.

[SOURCE CONFLICT: V10 §25.6 says that SACL queries the top-security lease repeatedly and never consumes it; 04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6 labels that lease's “Reusable?” cell “No — time-bounded, revocable, purpose-bound”. The V10 query/consumption rule is retained; the differing matrix label is not silently changed.]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`, restricted to expressly restored text.

<!-- BEGIN BEHAVIOR -->

### C-BAI — Biometric Authorization Interface (§25.6)
Stamp: DESIGNED    Source: [V10 §25.6] [MAP C-BAI]

ALONE
- What it is: DESIGNED — The narrow interface from native phone biometric authentication results to local purpose-bound authorization artifacts, without biometric data. [V10 §25.6]
- Takes in: DESIGNED — An OS result and the single locally prepared pending record with a declared purpose and requester. [V10 §25.6]
- Does: DESIGNED — Binds the purpose before prompting; matches the returned result to the unexpired pending record; creates the appropriate one-time token or revocable top-security lease on success; audits and delivers it to the requester. [V10 §25.6]
- Gives out: DESIGNED — Purpose-bound one-time authorization tokens, a queried top-security lease, requester notifications and separate physical-command and security-audit facts. [V10 §25.6]
- Must never: DESIGNED — Receive or process fingerprint data; become an authentication, access-control or session-management system; let one purpose satisfy another; reuse consumed or expired tokens; retain multiple pending records; override immutable roots or protected safeguards; query wellbeing. [V10 §25.6]
- Fails closed by: DESIGNED — Rejecting unmatched, delayed, duplicate or malformed results; creating no artifact for a failed match; terminating and notifying on every non-success result without automatic retry; clearing volatile state on restart and requiring reauthentication. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): requests the exact session-promotion purpose; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests `voice_enrollment_ness`; C-BGMM — Biometric-Gated Maintenance Mode (§25.13): uses session-and-purpose-bound maintenance confirmation. [V10 §25.6]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): fresh recognized-Ness confirmation must hold at TSC token consumption, and its relock or lost lease conditions revoke top-security authority. [V10 §25.6]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to BAI security records remains subject to privacy authorization. [MAP C-BAI]
- Changes: ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: receives only physical prompt/result facts with session identity and trusted local time. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-2.15.3.2 — Record identity boundary | Applicable biometric authority for record access. | Requires the existing identity/security boundary. | Record access receives no biometric bypass. | [MAP C-2] |
| 2 · DESIGNED | C-7B.10.8.4 — Identity and security condition | The applicable BAI authorization result. | Requires it alongside the other identity/security conditions. | The operation remains subject to its existing authorization. | [V10 §0B] |
| 3 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC) | An exact-session promotion token. | Requires purpose `tsc_promotion:<session_id>`. | A token for another session cannot authorize promotion. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] |
| 4 · DESIGNED | C-TSC.15 — Inspection prohibition | The permitted session-promotion purpose. | Uses no inspection-purpose BAI call. | The sealed cache gains no inspection route. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 5 · DESIGNED | C-TSC.16 — Session authorization | The exact purpose-bound token and actual BAI consumption evidence. | Requires valid session-purpose authority and uses BAI's own consumption/audit truth. | Authorization cannot arise from token possession alone. | [V10 §7E-TSC / 29. Integration Boundaries] [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] |
| 6 · DESIGNED | C-TSC.16.1 — Purpose-bound token condition | Live BAI token validity and consumption truth. | Requires the exact bound unused token. | A failed token condition prevents consumption. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] |
| 7 · ACCEPTED | C-TSC.16.5.3 — bai_token_id | The actual BAI token identity. | References that token in the authorization operation. | The coordinator does not become token owner. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] |
| 8 · ACCEPTED | C-TSC.16.7 — Durable consumption receipt | BAI's actual one-time consumption event. | Binds the complete durable receipt to that consumption. | Surviving proof belongs to flushed audit history. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 9 · ACCEPTED | C-TSC.16.7.3 — Receipt token identity | The identity of the token actually consumed. | Retains its exact BAI provenance in the receipt. | Token identity cannot be manufactured from coordination state. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 10 · ACCEPTED | C-TSC.16.7.7 — Receipt consumption timestamp | The time of BAI's consumption event. | Binds that actual time into the receipt. | Consumption time remains distinct from recognition time. | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 11 · DESIGNED | C-TSC.26 — Security and operational records | BAI-owned token audit events. | Uses the events their actual owner wrote. | Operational records cannot fabricate biometric facts. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 12 · DESIGNED | C-TSC.26.20 — BAI consume-blocked event | A live BAI refusal while the token remains unconsumed. | Records the actual consume-blocked event. | Recovery cannot backfill a refusal that did not occur. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 13 · DESIGNED | C-TSC.26.20.1 — token_purpose | The token purpose in the actual blocked attempt. | Records `token_purpose` from BAI's binding. | The refusal remains attributable to its real purpose. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 14 · DESIGNED | C-TSC.26.20.2 — reason | BAI's actual live refusal reason. | Records that reason with the blocked consumption. | An invented recovery reason cannot masquerade as BAI audit. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 15 · DESIGNED | C-TSC.28.3 — Expired or revoked token | Expired or revoked token state from BAI. | Refuses promotion authority from that token. | No consumption or promotion is authorized. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 16 · DESIGNED | C-TSC.29 — Integration boundaries | BAI consumption and its audit facts. | Preserves BAI's owner boundary. | The integration does not take over token authority. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 17 · DESIGNED | C-TSC.29.1 — BAI consume boundary | Live validity, purpose binding and consumption result. | Uses the BAI-owned C1 response. | A coordinator response alone cannot establish consumed authority. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 18 · ACCEPTED | C-TSC.29.1.1 — token_state | The current BAI token state. | Carries `token_state` in C1. | The interface preserves the owner's state rather than guessing. | [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 19 · ACCEPTED | C-TSC.29.1.2 — purpose_binding | BAI's purpose-validation result. | Carries `purpose_binding` in C1. | The consume response retains the exact purpose boundary. | [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 20 · ACCEPTED | C-TSC.29.1.3 — validity | BAI's live validity result. | Carries `validity` in C1. | Invalid authority cannot be replaced by coordination state. | [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 21 · ACCEPTED | C-TSC.29.1.5 — refusal_reason | BAI's actual refusal. | Returns its `refusal_reason`. | The caller receives the real failed condition. | [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2] |
| 22 · ACCEPTED | C-GOLD.1.6.3 — Linked protected-judgment protocol | BAI's current token check and separate durable consumption proof, conditionally. | Requires rechecking immediately before consumption within the linked protocol. | The later proposed E9 commit cannot trust an advance-only check. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 23 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning token's validity and exact accepted purpose/scope. | Requires BAI to recheck immediately before consumption. | A failing conditional token check prevents judgment authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 24 · ACCEPTED | C-GOLD.1.6.4.6 — BAI replay and reuse refusal | BAI state showing already consumed, expired or revoked authority. | Refuses reuse for another proposed O-JUDGE. | A prior token cannot authorize another judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 25 · ACCEPTED | C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt | Lookup of actual BAI security-audit receipts bound to the claim. | Requires positive proof that no verified bound receipt exists before no-receipt release. | A receipt-bearing claim cannot be released as though unconsumed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 26 · ACCEPTED | C-7L.11.5 — Enrollment provisional link basis | Durable consumed-token and setup authorization references. | Uses the actual enrollment authorization basis for the provisional link. | Provisional provenance does not become confirmed identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 27 · ACCEPTED | C-7P.2.6 — Strictest-rule and specialist authority boundary | The biometric token required by the specialist operation. | Keeps BAI authorization inside the strictest applicable authority boundary. | A general action level cannot weaken specialist protection. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] |
| 28 · ACCEPTED | C-7Q.11.2 — Established identity and private-context boundary | Required live security lease and current SACL gate. | Requires both compatible owner truths for Top-security use. | Privacy handling cannot treat mode state or a copied lease reference as authority. | [04/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md §4] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §13] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §5] |
| 29 · ACCEPTED | C-7Q.11.8 — Outward exposure and no-signal boundary | A current required top-security lease. | Requires it in addition to SACL Gate 1 before outward exposure. | Delivery cannot proceed on one owner alone. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |
| 30 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | BAI's actual prompt/result command fact. | Records only the permitted physical fact with session ID and local time. | Security details and authorization conclusions stay outside the root. | [V10 §25.6 / BOP vs. Security Audit Separation] |
| 31 · ACCEPTED | C-BOP.15.4 — Single enrollment biometric success observation | Committed opening truth referencing BAI's durable consumed proof. | Records the single BAI-sourced `biometric:result:success` fact. | The coordinator cannot fabricate or duplicate the observation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 32 · DESIGNED | C-SIA — Speaker Identity Assessment (§25.3) | Independent biometric evidence. | Keeps that factor separate from speaker assessment. | Biometric success does not replace identity assessment. | [V10 §25.3] [MAP C-SIA] |
| 33 · DESIGNED | C-SIA.2.5 — Session biometric state | BAI's biometric-factor verification. | Carries session biometric state as an independent factor. | Voice identity is not inferred from a successful device biometric. | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] |
| 34 · DESIGNED | C-SIA.4.1.1.3.7 — Device biometric state | Device biometric-factor evidence. | References that evidence independently of voice-profile assessment. | The device factor remains separate from voice recognition. | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] |
| 35 · DESIGNED | C-SIA.7.7 — Biometric-event trigger | A BAI biometric-factor event. | Uses the event as an assessment-update trigger. | The event does not itself decide speaker identity. | [V10 §25.3 / Assessment Update Cadence] [MAP C-SIA] |
| 36 · DESIGNED | C-SIA.11.5 — Ness training-session continuity | Biometric verification with SACL's actual recognition continuity. | Requires the sourced training-session basis. | Biometric evidence alone cannot supply continuous recognized-Ness state. | [V10 §25.3 / Training Eligibility Rules] [V10 §25.3 / Settled Rules] |
| 37 · DESIGNED | C-SIA.13 — Protected raw voice and readings | Biometric verification required for external transmission. | Applies it alongside recognized-Ness access, privacy and Full Mode routing. | Protected raw voice gains no biometric bypass. | [V10 §25.3 / Raw Voice Data Protection] |
| 38 · DESIGNED | C-SIA.15 — False lockout recovery | Thumbprint verification of the independent biometric factor. | Uses it in false-lockout recovery without declaring voice identity. | Recovery preserves the separation of biometric and voice factors. | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] |
| 39 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Independent BAI biometric authority. | Uses it alongside SIA evidence and Person-Box information. | The biometric factor does not replace SACL's own access decision. | [V10 §25.4] |
| 40 · DESIGNED | C-SACL.4.2.1 — Verified biometric within timeout | Independent biometric verification within the required timeout. | Uses the actual verification for Gate 1's biometric condition. | Old or absent verification cannot satisfy current top-security qualification. | [V10 §25.4 / Fingerprint as One Independent Factor] [MAP C-SACL] |
| 41 · DESIGNED | C-SACL.5 — Independent biometric factor | BAI biometric verification. | Keeps the factor independent of recognition and suspicion evidence. | Fingerprint success cannot erase unresolved identity/security conditions. | [V10 §25.4 / Fingerprint as One Independent Factor] |
| 42 · ACCEPTED | C-SACL.18 — Proposed Output Delivery Coordinator | Live lease truth when required by the output operation. | Requires the actual BAI owner decision alongside privacy and access gates. | The output coordinator gains no lease authority of its own. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E] |
| 43 · ACCEPTED | C-SACL.20.14 — Handoff required BAI lease | The actual required BAI lease reference. | Retains BAI as the live authority owner. | The handoff cannot copy current authority into a static field. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 44 · ACCEPTED | C-SACL.26 — Stage checkpoints preserve owner authority | BAI's owner lease truth. | Keeps checkpoints referential. | Stage completion does not become biometric authority. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E] |
| 45 · ACCEPTED | C-SACL.40 — Fresh TSC recognition-confirmation interface | The current recognition-confirmation binding requested for consumption. | Supplies BAI the exact fresh confirmation identity and time. | BAI can require current recognition at the actual consume boundary. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] |
| 46 · DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9) | The exact proposed Personal-mode opening proof or separately required current lease. | Keeps the opening token and top-security owner pair distinct. | Other purposes cannot open Personal Mode or restore its volatile state. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 47 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The voice_enrollment_ness token and flushed consumed proof. | Requires BAI's real purpose-bound authority before committing the session opening. | Biometric success alone neither opens capture nor establishes voice identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 48 · DESIGNED | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Biometric confirmation bound to the maintenance session and purpose. | Uses bgmm_confirmation:<session_id>:<purpose>. | Another token purpose cannot satisfy the maintenance confirmation. | [V10 §25.6 / Purpose Binding] |
| 49 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | Purpose-bound biometric lease authority alongside independent recognition. | Applies the security/identity cycle's top-security conjunction. | Voice alone does not unlock top-security. | [MAP CY-I] [V10 §25.6] |
| 50 · DESIGNED | C-7Q.3.1 — Deletion dependency and location discovery | The original root and its known or discoverable derivatives and locations. | Proceeds only when governance discovery runs only under artifact §7Q authorization and §25 identity and security. | Nothing in this card. | [V10 §7Q] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.2] |
| 51 · DESIGNED | C-PAIR.2.1.3 — Phone-only timed visibility | The code decrypted on the paired phone after biometric approval. | Proceeds only when the code becomes visible only after biometric-approved decryption on the paired phone. | Nothing in this card. | [V10 §25.8 / First Recovery Code Creation] |
| 52 · ACCEPTED | C-SACL.33.1 — Proposed output_operation | Proposed output_operation_id and proposed delivery_idempotency_key. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 53 · ACCEPTED | C-SACL.33.2 — Proposed output_stage_event | The stage owner's gate-result/decision reference, with the common epoch and committed generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 54 · ACCEPTED | C-SACL.33.3 — Proposed retrieval_intersection_record | §7Q eligibility reference, SACL scope reference and identities of admitted material, with common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 55 · ACCEPTED | C-SACL.33.5 — Proposed delivery_attempt_event [proposed] | Proposed delivery_attempt_id, the exact claim reference and dispatch-intent reference, with common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §12] |
| 56 · ACCEPTED | C-SACL.33.6 — Proposed delivery_confirmation_receipt | Positive channel acknowledgment, both attempt and claim references, and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 57 · ACCEPTED | C-SACL.33.7 — Proposed delivery_non_delivery_receipt [proposed] | Positive non-delivery proof, both attempt and claim references, and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 58 · ACCEPTED | C-SACL.33.8 — Proposed delivery_uncertainty_record [proposed] | Both attempt and claim references, what remains unknown, what was not done, the permitted resolution routes and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 59 · ACCEPTED | C-SACL.33.10 — Proposed duplicate_delivery_prevented | Proposed delivery_idempotency_key, relevant proposed delivery_claim_id and proposed delivery_attempt_id. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 60 · ACCEPTED | C-SACL.33.11 — Proposed output_recovery_event | The crash boundary, committed truth found and common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §11] |
| 61 · ACCEPTED | C-SACL.33.12 — Proposed delivery_claim_state_event | The affected claim, status spent, invalidated or abandoned, its basis and time, plus common epoch/generation. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6F] |
| 62 · ACCEPTED | C-ENROLL.9.7 — Immutable enrollment segment identity | The particular captured segment's reference identity. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 63 · ACCEPTED | C-ENROLL.9.8 — Per-segment eligibility decision record | The six-check outcome and actual source references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 64 · ACCEPTED | C-ENROLL.13.1 — Enrollment parent operation record | Operation/session identities, process state, terminal reason and audit references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 65 · ACCEPTED | C-ENROLL.13.2 — Enrollment stage checkpoint | The actual stage's owner-returned outcome and references. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 66 · ACCEPTED | C-ENROLL.13.3 — Enrollment recovery operation and event | The actual crash boundary and surviving committed owner facts. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 67 · ACCEPTED | C-ENROLL.13.4 — Absorbed enrollment duplicate record | A replay recognized by the relevant stable identity. | Proceeds only when the record is used only under §7Q privacy and §25 identity and security authorization. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 68 · ACCEPTED | C-7G.11.1.18 — evidence_locator_record_ref [proposed] | Full evidence locators and any authorized necessary bounded quote held under the governed record boundary. | Locator access needs privacy and identity/security authorization. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §2.9] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §2.2] |
| 69 · ACCEPTED | C-7G.14 — Acceptance operation history | Each proposal and assessment, actual use/omission, criterion findings, operation terminal and recovery action. | Operation history is used only within the privacy, identity/security, TSC, compartment and influence-removal boundaries. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §7.4] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §7.6] |
| 70 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Readings and their `reads`, `derived_from`, `produced_by` and confidence. | Gates this place: the checks remain subject to identity and security authorization. | Nothing in this card. | [V10 §0B] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |
| 71 · ACCEPTED | C-9.5 — Separate authorities and effective permission | Current mode permission, SACL access/PBR limits, §7Q purpose/privacy/restriction/exclusion/compartment rules and a separately required top-security lease. | Supplies any required current higher authority. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §4] |
| 72 · ACCEPTED | C-ENROLL.9 — Initial-corpus eligibility gate | Reading references, root provenance and actual owner facts for each immutable segment identity [proposed]. | Supplies durable token-consumption truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 73 · ACCEPTED | C-STORE.5.2.8 — Operation logging | NOT DECIDED | Gates this place: access also passes §25 identity and security authorization. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 74 · DESIGNED | C-PAIR.6 — Pairing and recovery audit boundary | Every actual pairing-state transition, recovery-code creation/verification/activation/rotation, replacement and emergency step, including aborts with failed step/reason. | Gates this place: applicable biometric authorization remains required. | Nothing in this card. | [MAP C-PAIR] [V10 §0B] [V10 §25.8 / Save Verification] |
| 75 · ACCEPTED | C-9.12.7.5 — Actual top-security lease reference | The actual BAI-owned lease. | Supplies actual live lease. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 76 · ACCEPTED | C-9.12 — Proposed mode coordination records | References to owner-held identity assessments, access decisions/PBRs, biometric tokens/leases, privacy decisions and audit events. | Supplies token and lease owner references. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12] |
| 77 · DESIGNED | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | The first phone's hardware-backed identity. | Supplies the native biometric authorization boundary and hardware-backed app trust. | Nothing in this card. | [V10 §25.6] [V10 §25.13 / Purpose-Specific Authorization] |
| 78 · DESIGNED | C-PAIR.2.1.2 — Biometric-approved phone decryption | The encrypted code and biometric approval on the paired phone. | Gates this place: biometric approval remains within its native device boundary. | Nothing in this card. | [V10 §25.8 / First Recovery Code Creation] [V10 §25.6] |
| 79 · ACCEPTED | C-PAIR.5.2 — Pairing-owned enrollment safety events | Trusted-phone loss, replacement or revocation. | Supplies its owned trust/security facts. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 80 · ACCEPTED | C-7B.9.7.2 — Identity and authorization protections | Selected Wonder material and the intake operation. | Gates this place: selected Wonder intake passes the existing identity and authorization protections unchanged. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §4] |
| 81 · ACCEPTED | C-9.9 — Explicit mode close | A close request and the current session, generation and dependent-operation references. | Takes this place's change: requests the actual owner's required lease ending. | Requests the actual owner's required lease ending. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §9] |
| 82 · ACCEPTED | C-ENROLL.7.6 — BAI or session integrity failure | The actual security owner's failure event. | Supplies actual security integrity truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 83 · ACCEPTED | C-ENROLL.7 — Mid-session protective stop | Trust loss/replacement/revocation, invalid recovery/setup, QR/secret contradiction, medium-or-higher spoofing, missing/contradictory Person-Box, BAI/session integrity failure, privacy exclusion or restart. | Supplies security/session integrity events. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 84 · ACCEPTED | C-STORE.4.14.1 — Authority and privacy | NOT DECIDED | Gates this place: access also passes §25 identity and security authorization. | Nothing in this card. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §15] |

SUB-PARTS: C-BAI.1 — Narrow biometric-result boundary; C-BAI.2 — OS biometric result; C-BAI.3 — Pending authorization record; C-BAI.4 — One-time authorization token; C-BAI.5 — One-time token lifecycle; C-BAI.6 — Top-security biometric lease; C-BAI.7 — Lease lifecycle; C-BAI.8 — Independent key purposes; C-BAI.9 — Biometric result handling; C-BAI.10 — Simultaneous TSC consume conditions; C-BAI.11 — Immediate lease revocation; C-BAI.12 — Volatile BAI state; C-BAI.13 — Physical-command and security-audit separation; C-BAI.14 — Restart and invalid-result failures; C-BAI.15 — Protected-core biometric laws; C-BAI.16 — Durable TSC consumption producer; C-BAI.17 — Personal-mode biometric opening boundary; C-BAI.18 — Current top-security owner pair; C-BAI.19 — Enrollment authorization producer; C-BAI.20 — Conditional evaluation-judgment proof producer; C-BAI.21 — Owner proof across coordination boundaries

### C-BAI.1 — Narrow biometric-result boundary
Stamp: DESIGNED    Source: [V10 §25.6 / What BAI Is and Is Not]

ALONE
- What it is: DESIGNED — A result-binding and local-proof interface to the phone's native biometric hardware. [V10 §25.6 / What BAI Is and Is Not]
- Takes in: DESIGNED — OS authentication results, never fingerprint data. [V10 §25.6 / What BAI Is and Is Not]
- Does: DESIGNED — Receives results, binds purposes, creates local proofs and audits. [V10 §25.6 / What BAI Is and Is Not]
- Gives out: DESIGNED — Authorization tokens or a revocable top-security lease containing no biometric data. [V10 §25.6 / What BAI Is and Is Not]
- Must never: DESIGNED — Act as an authentication system, access-control system or session manager, or own fingerprint data at any stage. [V10 §25.6 / What BAI Is and Is Not]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.2 — OS biometric result
Stamp: DESIGNED    Source: [V10 §25.6 / What BAI Receives From the OS]

ALONE
- What it is: DESIGNED — `os_biometric_result`, with `outcome`, `os_error_code` and `os_lockout_type`. [V10 §25.6 / What BAI Receives From the OS]
- Takes in: DESIGNED — The OS's native authentication result. [V10 §25.6 / What BAI Receives From the OS]
- Does: DESIGNED — Uses BAI's own trusted local clock; relies on neither OS-provided timestamps nor OS device-ID fields. [V10 §25.6 / What BAI Receives From the OS]
- Gives out: DESIGNED — The result facts used by BAI's local handling and audit. [V10 §25.6 / What BAI Receives From the OS]
- Must never: DESIGNED — Expose `os_error_code` to components or substitute OS timestamp/device-ID fields for local clock and app-key trust. [V10 §25.6 / What BAI Receives From the OS] [V10 §25.6 / Purpose Binding]
- Fails closed by: DESIGNED — Malformed results are rejected without logging potentially biometric fields, with `bai_malformed_result_rejected`. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.2.1 — OS outcome: supplies the six-value result; C-BAI.2.2 — OS audit error code: supplies string-or-null audit detail; C-BAI.2.3 — OS lockout type: supplies temporary, permanent or null lockout classification. [V10 §25.6 / What BAI Receives From the OS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.9 — Biometric result handling | The OS outcome and audit-only details. | Selects the success or non-success result branch. | No OS timestamp or device-ID field supplies local trust. | [V10 §25.6] |

SUB-PARTS: C-BAI.2.1 — OS outcome; C-BAI.2.2 — OS audit error code; C-BAI.2.3 — OS lockout type

### C-BAI.2.1 — OS outcome
Stamp: DESIGNED    Source: [V10 §25.6 / What BAI Receives From the OS]

ALONE
- What it is: DESIGNED — `outcome`, with the six permitted values `success`, `failure`, `cancelled`, `timeout`, `lockout`, `error`. [V10 §25.6 / What BAI Receives From the OS]
- Takes in: DESIGNED — The OS authentication outcome. [V10 §25.6 / What BAI Receives From the OS]
- Does: DESIGNED — Distinguishes successful authentication from the five non-success outcomes. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Retry any non-success outcome automatically. [V10 §25.6]
- Fails closed by: DESIGNED — Every non-success outcome terminates the pending record, notifies the requester and is audited without automatic retry. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.2 — OS biometric result | The OS outcome. | Carries one of the six declared result values. | Result handling can distinguish success and non-success. | [V10 §25.6 / What BAI Receives From the OS] |

SUB-PARTS: NONE

### C-BAI.2.2 — OS audit error code
Stamp: DESIGNED    Source: [V10 §25.6 / What BAI Receives From the OS]

ALONE
- What it is: DESIGNED — `os_error_code`, a string or null, for audit only. [V10 §25.6 / What BAI Receives From the OS]
- Takes in: DESIGNED — The error-code field of the OS result. [V10 §25.6 / What BAI Receives From the OS]
- Does: DESIGNED — Retains the error detail within the audit boundary. [V10 §25.6 / What BAI Receives From the OS]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Expose this field to components. [V10 §25.6 / What BAI Receives From the OS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.2 — OS biometric result | String-or-null OS error detail. | Keeps it audit-only. | Components receive no OS error-code field. | [V10 §25.6 / What BAI Receives From the OS] |

SUB-PARTS: NONE

### C-BAI.2.3 — OS lockout type
Stamp: DESIGNED    Source: [V10 §25.6 / What BAI Receives From the OS]

ALONE
- What it is: DESIGNED — `os_lockout_type`, with values `temporary`, `permanent` or null. [V10 §25.6 / What BAI Receives From the OS]
- Takes in: DESIGNED — The lockout-type field of the OS result. [V10 §25.6 / What BAI Receives From the OS]
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.2 — OS biometric result | Temporary, permanent or null lockout type. | Carries the OS lockout classification. | The result retains its stated lockout field. | [V10 §25.6 / What BAI Receives From the OS] |

SUB-PARTS: NONE

### C-BAI.3 — Pending authorization record
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `pending_authorization_record`, the single pre-prompt record binding a declared purpose to its requester and app instance. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — A declared purpose and named requesting component. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Generates a uuid4 `pending_id` and cryptographically random `challenge`; records `purpose`, `requester`, trusted-local `requested_at`, `expires_at = requested_at + pending_expiry_window`, `status` and `app_session_key_ref` before showing the OS prompt. [V10 §25.6 / Purpose Binding]
- Gives out: DESIGNED — One pending record whose device/app trust rests on a hardware-backed app-instance key in the phone's secure keystore. [V10 §25.6 / Purpose Binding]
- Must never: DESIGNED — Bind purpose after the prompt, keep concurrent pending records, or bind device/app trust through OS device-ID fields. [V10 §25.6 / Purpose Binding]
- Fails closed by: DESIGNED — An absent, expired or device-mismatched pending record yields `bai_unmatched_result` and no artifact. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.1 — Pending identity: supplies pre-prompt uuid4 identity; C-BAI.3.2 — Pending challenge: supplies the random nonce; C-BAI.3.3 — Pending purpose: supplies declared scope; C-BAI.3.4 — Pending requester: supplies component identity; C-BAI.3.5 — Pending request time: supplies trusted-local request time; C-BAI.3.6 — Pending expiry: supplies the request-expiry boundary; C-BAI.3.7 — Pending status: carries pending or terminal status; C-BAI.3.8 — App-instance key reference: supplies hardware-backed app trust. [V10 §25.6 / Purpose Binding]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.9 — Biometric result handling | Current purpose, requester, expiry and app binding. | Matches the result to the single local request. | A failed match creates no artifact. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.9.1 — Matched success | The unexpired matching request. | Requires that local match before artifact creation. | OS success alone does not create authority. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.12.1 — Current pending record | The single purpose-bound pending request. | Stores it as `pending_record`. | Current pending state remains singular and volatile. | [V10 §25.6] |

SUB-PARTS: C-BAI.3.1 — Pending identity; C-BAI.3.2 — Pending challenge; C-BAI.3.3 — Pending purpose; C-BAI.3.4 — Pending requester; C-BAI.3.5 — Pending request time; C-BAI.3.6 — Pending expiry; C-BAI.3.7 — Pending status; C-BAI.3.8 — App-instance key reference; C-BAI.3.9 — Purpose vocabulary

### C-BAI.3.1 — Pending identity
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `pending_id`, a uuid4 generated by BAI before the OS prompt. [V10 §25.6 / Purpose Binding]
- Takes in: NOT DECIDED
- Does: DESIGNED — Identifies the pending authorization record. [V10 §25.6 / Purpose Binding]
- Gives out: DESIGNED — The `pending_id` retained in the resulting token or lease. [V10 §25.6]
- Must never: DESIGNED — Generate the pending identity only after the OS prompt has opened. [V10 §25.6 / Purpose Binding]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | A BAI-generated uuid4. | Identifies the request before prompting. | The pending record has its local identity. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BAI.4 — One-time authorization token | The originating `pending_id`. | Carries the request reference into the token. | The token retains its pending-request binding. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.6 — Top-security biometric lease | The lease's originating `pending_id`. | Preserves the pending-request reference. | The lease retains the request that produced it. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.3.2 — Pending challenge
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `challenge`, a cryptographically random nonce generated by BAI. [V10 §25.6 / Purpose Binding]
- Takes in: NOT DECIDED
- Does: DESIGNED — Binds the local pending authorization; the one-time token carries the challenge. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Enter a BOP system-command root. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | A cryptographically random nonce. | Binds the pending challenge. | The request retains its BAI-generated challenge. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BAI.4 — One-time authorization token | The pending challenge. | Carries the same nonce into the token. | The token remains bound to the local challenge. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.3.3 — Pending purpose
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `purpose`, the declared authorization-purpose identifier. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The purpose declared before prompting. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Fixes the scope that must match on every token-consume call. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Satisfy another purpose or appear in a BOP biometric-command root. [V10 §25.6]
- Fails closed by: DESIGNED — A TSC purpose mismatch prevents consumption and promotion. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | The declared purpose. | Records it before the OS prompt. | Later authority remains purpose-bound. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BAI.4 — One-time authorization token | The purpose declared before prompting. | Carries it into the one-time artifact. | Every consume must match that purpose. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.15.2 — No cross-purpose authority | The predeclared purpose. | Compares it with every requested consumption purpose. | Cross-purpose authority is refused. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.3.4 — Pending requester
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `requester`, the named component requesting authorization. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The component identity at purpose binding. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Identifies the recipient of the appropriate artifact or non-success notification; requester identity is security-audit material. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: ACCEPTED — Place requester identity in the narrow BOP biometric-command observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | The named requesting component. | Records the recipient of the artifact or failure notification. | The authorization retains requester identity. | [V10 §25.6 / Purpose Binding] |
| 2 · ACCEPTED | C-ENROLL.4.3.9 — Bound requester identity | The requester associated with the BAI operation. | Supplies the BAI requester's identity. | Nothing in this card. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |

SUB-PARTS: NONE

### C-BAI.3.5 — Pending request time
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `requested_at`, taken from N.H's trusted local clock. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — Local time when the request is recorded. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Supplies the starting time for `pending_expiry_window`. [V10 §25.6 / Purpose Binding]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Rely on an OS-provided timestamp. [V10 §25.6 / What BAI Receives From the OS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | Trusted-local request time. | Records `requested_at`. | Pending expiry has a local-clock origin. | [V10 §25.6 / Purpose Binding] |

SUB-PARTS: NONE

### C-BAI.3.6 — Pending expiry
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `expires_at = requested_at + pending_expiry_window`; the source gives no numerical window. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The trusted-local request time and pending expiry window. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Limits the time within which a matched successful result can create an artifact. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Authorize from an expired pending record. [V10 §25.6]
- Fails closed by: DESIGNED — Expiry makes the result unmatched; BAI rejects it, writes `bai_unmatched_result` and creates no artifact. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | Request time plus `pending_expiry_window`. | Records the expiry boundary. | An expired request cannot produce an artifact. | [V10 §25.6 / Purpose Binding] |

SUB-PARTS: NONE

### C-BAI.3.7 — Pending status
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `status`, expressed as `pending` or `[terminal states]`; no terminal-state enumeration is supplied. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The result of the pending biometric request. [V10 §25.6]
- Does: DESIGNED — On any non-success outcome, moves to terminal status before requester notification and audit; an already-resolved pending record rejects a duplicate result. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat a resolved pending record as a fresh matching request. [V10 §25.6]
- Fails closed by: DESIGNED — Duplicate results are rejected with `bai_duplicate_result_rejected`. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | Pending or terminal request state. | Retains the current pending-record status. | A resolved request cannot accept a duplicate result. | [V10 §25.6 / Purpose Binding] |

SUB-PARTS: NONE

### C-BAI.3.8 — App-instance key reference
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `app_session_key_ref`, a reference to the hardware-backed key for this app instance. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The app-instance key reference in the phone's secure keystore. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Binds device and app trust through that key. [V10 §25.6 / Purpose Binding]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Substitute OS-provided device-ID fields for hardware-backed app-instance trust. [V10 §25.6 / Purpose Binding]
- Fails closed by: DESIGNED — Device mismatch prevents a matched result and creates no artifact. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3 — Pending authorization record | The hardware-backed app-instance key reference. | Binds device/app trust through the secure keystore. | OS device-ID fields do not establish that trust. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BAI.12 — Volatile BAI state | The app-instance key reference. | Carries `app_session_key_ref` in current memory. | BAI state retains the local trust reference without OS device-ID trust. | [V10 §25.6] |
| 3 · DESIGNED | C-PAIR.1.2.3 — Hardware-backed phone binding | The successfully paired phone's hardware-backed key identity. | Preserves the hardware-backed app-instance reference. | Nothing in this card. | [V10 §25.7 / Four States] [V10 §25.6] |
| 4 · ACCEPTED | C-ENROLL.4.3.6 — Bound hardware phone key reference | The phone's hardware-backed key reference. | Supplies the hardware-backed phone binding. | Nothing in this card. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |

SUB-PARTS: NONE

### C-BAI.3.9 — Purpose vocabulary
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — The declared purpose vocabulary: `top_security_access`, `tsc_promotion:<session_id>`, `voice_enrollment_ness`, `bgmm_confirmation:<session_id>:<purpose>` and `extended:<purpose_id>`. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The requested protected purpose before the OS prompt. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Keeps authorization bound to that purpose; every consume call verifies it. [V10 §25.6]
- Gives out: DESIGNED — A purpose-specific token or the top-security lease. [V10 §25.6]
- Must never: DESIGNED — Let an artifact created for one purpose satisfy another. [V10 §25.6]
- Fails closed by: DESIGNED — Wrong-purpose TSC authorization is not consumed and cannot promote. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.9.1 — Top-security purpose: names the lease purpose; C-BAI.3.9.2 — Exact-session TSC purpose: binds one session's promotion; C-BAI.3.9.3 — Ness enrollment purpose: names initial voice enrollment; C-BAI.3.9.4 — Maintenance confirmation purpose: binds session and maintenance purpose; C-BAI.3.9.5 — Extended purpose namespace: carries an exact extension identifier. [V10 §25.6 / Purpose Binding]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-BAI.3.9.1 — Top-security purpose; C-BAI.3.9.2 — Exact-session TSC purpose; C-BAI.3.9.3 — Ness enrollment purpose; C-BAI.3.9.4 — Maintenance confirmation purpose; C-BAI.3.9.5 — Extended purpose namespace

### C-BAI.3.9.1 — Top-security purpose
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `top_security_access`, the purpose of the top-security biometric lease. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Binds ongoing top-security authority to the revocable lease rather than a spent one-time token. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Be satisfied by a token for another purpose. [V10 §25.6]
- Fails closed by: DESIGNED — Expiry or revocation ends the active lease. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9 — Purpose vocabulary | `top_security_access`. | Names the ongoing lease purpose. | The vocabulary distinguishes lease authority. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BAI.6 — Top-security biometric lease | `top_security_access`. | Fixes the lease purpose. | The lease cannot stand for another purpose. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.3.9.2 — Exact-session TSC purpose
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `tsc_promotion:<session_id>`, binding promotion to the exact named session. [V10 §25.6]
- Takes in: DESIGNED — The session identity requiring promotion authorization. [V10 §25.6]
- Does: DESIGNED — Requires a valid unconsumed token of this exact purpose together with fresh current SACL recognition at consumption. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Use another session's purpose or a different purpose to authorize promotion. [V10 §25.6]
- Fails closed by: DESIGNED — If either condition fails, the token remains unconsumed and promotion does not proceed. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-TSC.16.2 — Fresh recognized-Ness condition: current non-stale recognition for the Ness stream must hold at consumption. [V10 §25.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9 — Purpose vocabulary | `tsc_promotion:<session_id>`. | Names one exact session's promotion. | Another session cannot share this purpose. | [V10 §25.6 / Purpose Binding] |

SUB-PARTS: NONE

### C-BAI.3.9.3 — Ness enrollment purpose
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `voice_enrollment_ness`, the one-time authorization purpose for initial Ness voice enrollment. [V10 §25.6]
- Takes in: ACCEPTED — An explicit begin action and the verified enrollment prerequisites. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: DESIGNED — Binds the token to voice enrollment rather than another protected operation. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: ACCEPTED — Open Personal Mode, unlock top-security or prove Ness's voice identity from enrollment authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §5]
- Fails closed by: ACCEPTED — Failed or changed prerequisites prevent enrollment opening; changed prerequisites after issue require revocation without consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the enrollment request under its explicit-action and prerequisite boundary. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: all six prerequisites must be verified before the BAI request and revalidated before consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9 — Purpose vocabulary | `voice_enrollment_ness`. | Names initial voice-enrollment approval. | The vocabulary keeps enrollment separate from other purposes. | [V10 §25.6 / Purpose Binding] |
| 2 · ACCEPTED | C-ENROLL.4.3.5 — Bound enrollment purpose | BAI's purpose-bound consumption fact. | Supplies the existing purpose owner. | Nothing in this card. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-BAI.3.9.4 — Maintenance confirmation purpose
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `bgmm_confirmation:<session_id>:<purpose>`, the session-and-purpose-bound maintenance confirmation identifier. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The session and maintenance purpose to be confirmed. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Declares that purpose before the OS prompt. [V10 §25.6 / Purpose Binding]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Let a token for another purpose satisfy this confirmation. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM — Biometric-Gated Maintenance Mode (§25.13): requests its bounded biometric confirmation. [V10 §25.6 / Purpose Binding]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9 — Purpose vocabulary | `bgmm_confirmation:<session_id>:<purpose>`. | Carries the maintenance confirmation's session and purpose. | Maintenance authority remains specifically bound. | [V10 §25.6 / Purpose Binding] |
| 2 · DESIGNED | C-BGMM.8.3 — Trusted-phone confirmation | A purpose-bound request sent by the motherbase to the trusted paired phone, carrying the declared purpose and nonprivate change description. | Gates this place: requires the exact maintenance session/purpose binding. | Nothing in this card. | [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance] |

SUB-PARTS: NONE

### C-BAI.3.9.5 — Extended purpose namespace
Stamp: DESIGNED    Source: [V10 §25.6 / Purpose Binding]

ALONE
- What it is: DESIGNED — `extended:<purpose_id>`, the declared extension-purpose form. [V10 §25.6 / Purpose Binding]
- Takes in: DESIGNED — The specific extension purpose identifier. [V10 §25.6 / Purpose Binding]
- Does: DESIGNED — Retains purpose binding before the OS prompt and at token consumption. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat the namespace as interchangeable authority across purposes. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9 — Purpose vocabulary | `extended:<purpose_id>`. | Names the exact extension purpose. | Extension does not remove purpose separation. | [V10 §25.6 / Purpose Binding] |
| 2 · ACCEPTED | C-BAI.17 — Personal-mode biometric opening boundary | The exact proposed Personal-mode opening extension purpose. | Binds it before the OS prompt. | Other token purposes cannot open the mode. | [V10 §25.6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |

SUB-PARTS: NONE

### C-BAI.4 — One-time authorization token
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `one_time_authorization_token`, with `token_id`, `pending_id`, `challenge`, `purpose`, `authenticated_at`, `created_at`, `expires_at` and `status`. [V10 §25.6]
- Takes in: DESIGNED — Successful OS authentication matched to an unexpired pending record. [V10 §25.6]
- Does: DESIGNED — Creates the purpose-bound token, delivers it to the requester and consumes it before the protected action begins; verifies purpose on every consume call. [V10 §25.6]
- Gives out: DESIGNED — One authorization for the declared protected action; the token becomes permanently unusable after consumption. [V10 §25.6]
- Must never: DESIGNED — Carry biometric data, satisfy another purpose, or reuse a consumed or expired token. [V10 §25.6]
- Fails closed by: DESIGNED — Unmatched results produce no token; failed TSC token or current-recognition conditions leave it unconsumed and prevent promotion. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.1 — Pending identity: supplies the originating `pending_id`; C-BAI.3.2 — Pending challenge: supplies the generated nonce; C-BAI.3.3 — Pending purpose: supplies the predeclared purpose. [V10 §25.6]
- Fed by: DESIGNED — C-BAI.4.1 — Token identity: supplies `token_id`; C-BAI.4.2 — Artifact authentication time: supplies `authenticated_at`; C-BAI.4.3 — Artifact creation time: supplies `created_at`; C-BAI.4.4 — Artifact expiry: supplies `expires_at`; C-BAI.4.5 — Token status: supplies the four-state token status. [V10 §25.6]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): fresh SACL recognition holds at consume time. [V10 §25.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.5 — One-time token lifecycle | The complete purpose-bound token. | Creates, delivers and consumes it under the one-time lifecycle. | Consumption leaves it permanently unusable. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.12.3 — Active one-time token map | One-time token records. | Places them under their token identities. | The map contains actual current tokens. | [V10 §25.6] |
| 3 · DESIGNED | C-BGMM.8.3 — Trusted-phone confirmation | A purpose-bound request sent by the motherbase to the trusted paired phone, carrying the declared purpose and nonprivate change description. | Gates this place: the phone requires its own purpose-bound token before sending confirmation. | Nothing in this card. | [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance] |

SUB-PARTS: C-BAI.4.1 — Token identity; C-BAI.4.2 — Artifact authentication time; C-BAI.4.3 — Artifact creation time; C-BAI.4.4 — Artifact expiry; C-BAI.4.5 — Token status

### C-BAI.4.1 — Token identity
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `token_id`, the identity field of a one-time authorization token; no primitive format is specified. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Keys `active_one_time_tokens`, whose values are the corresponding token records. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Enter a BOP biometric-command root. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.4 — One-time authorization token | `token_id`. | Identifies this token. | The token is addressable by its own identity. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.12.3 — Active one-time token map | `token_id`. | Uses it as the map key. | Each entry addresses its corresponding token. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.4.2 — Artifact authentication time
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `authenticated_at`, carried by both the one-time token and top-security lease. [V10 §25.6]
- Takes in: DESIGNED — Authentication time from BAI's trusted local clock. [V10 §25.6]
- Does: DESIGNED — Supplies the lease's timeout origin. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Rely on an OS-provided timestamp. [V10 §25.6 / What BAI Receives From the OS]
- Fails closed by: DESIGNED — Reaching the lease timeout since `authenticated_at` immediately revokes the lease. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.4 — One-time authorization token | `authenticated_at`. | Carries the local authentication time. | The token preserves that time separately from creation. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.6 — Top-security biometric lease | The local authentication time. | Carries `authenticated_at` as the timeout origin. | The lease retains its biometric timing boundary. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.11.5 — Lease timeout trigger | `authenticated_at`. | Measures lease timeout from authentication. | The revocation uses the stated time origin. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.4.3 — Artifact creation time
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `created_at`, carried by the one-time token and top-security lease. [V10 §25.6]
- Takes in: DESIGNED — BAI's trusted local clock. [V10 §25.6 / What BAI Receives From the OS]
- Does: DESIGNED — Records the artifact's creation time. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Rely on an OS-provided timestamp. [V10 §25.6 / What BAI Receives From the OS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.4 — One-time authorization token | `created_at`. | Carries the token creation time. | The artifact records when it was created. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.6 — Top-security biometric lease | The lease creation time. | Carries `created_at`. | The lease records its creation separately from authentication. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.4.4 — Artifact expiry
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `expires_at`, present in each one-time token and top-security lease; no artifact expiry duration or formula is selected here. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Bounds the artifact's usable lifetime. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Permit reuse of an expired token. [V10 §25.6]
- Fails closed by: DESIGNED — An expired token cannot authorize TSC promotion; an expired lease is no longer active. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.4 — One-time authorization token | `expires_at`. | Bounds token usability. | Expired authority cannot be reused. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.6 — Top-security biometric lease | The lease expiry. | Carries `expires_at`. | Active authority ends at expiry. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.4.5 — Token status
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Token `status`: `valid`, `consumed`, `expired` or `revoked`. [V10 §25.6]
- Takes in: DESIGNED — The token's creation, consumption, expiry or revocation state. [V10 §25.6]
- Does: DESIGNED — Distinguishes live one-time authority from spent, expired or revoked authority. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Make consumed or expired tokens reusable. [V10 §25.6]
- Fails closed by: DESIGNED — TSC consumption requires a valid unconsumed token; otherwise no consumption or promotion occurs. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.4 — One-time authorization token | Valid, consumed, expired or revoked status. | Carries the token's current state. | The artifact distinguishes usable and unusable authority. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.15.3 — No spent-token reuse | Current token state. | Keeps consumed and expired states unusable. | Spent authority cannot authorize another action. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.5 — One-time token lifecycle
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Creation on OS success, delivery to the requester, consumption before the protected action and permanent non-reuse. [V10 §25.6]
- Takes in: DESIGNED — A matched unexpired successful request and later purpose-specific consume calls. [V10 §25.6]
- Does: DESIGNED — Creates and delivers a valid token; verifies purpose at every consumption; spends the token before the action begins. Expired tokens cannot be reused. [V10 §25.6]
- Gives out: DESIGNED — A single authorized use or an unusable consumed, expired or revoked token. [V10 §25.6]
- Must never: DESIGNED — Consume for a different purpose or reuse a spent token. [V10 §25.6]
- Fails closed by: ACCEPTED — If consumption is uncertain because its required durable receipt cannot be written or verified, the token is terminal and never retried. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

TOGETHER
- Fed by: DESIGNED — C-BAI.4 — One-time authorization token: supplies the bound token and its state. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.5.1 — Valid token state | Matched authentication success. | Enters valid state and delivers the token. | The requester receives an unconsumed purpose-bound artifact. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.5.2 — Consumed token state | A permitted purpose-matched consumption. | Spends the token before the action. | The token cannot authorize another use. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.5.3 — Expired token state | The token reaching expiry. | Ends valid token authority. | Expired state cannot be reused. | [V10 §25.6] |
| 4 · DESIGNED | C-BAI.5.4 — Revoked token state | Token revocation. | Keeps revoked state outside valid one-time authority. | A revoked token cannot satisfy the valid-token condition. | [V10 §25.6] |

SUB-PARTS: C-BAI.5.1 — Valid token state; C-BAI.5.2 — Consumed token state; C-BAI.5.3 — Expired token state; C-BAI.5.4 — Revoked token state

### C-BAI.5.1 — Valid token state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `valid`, the live one-time-token state created on a matched successful OS result. [V10 §25.6]
- Takes in: DESIGNED — Successful authentication within the pending record's expiry. [V10 §25.6]
- Does: DESIGNED — Delivers the token to the requester for a purpose-verified consumption before the action. [V10 §25.6]
- Gives out: DESIGNED — A valid token that has not yet been consumed. [V10 §25.6]
- Must never: DESIGNED — Treat validity alone as sufficient for TSC consumption without simultaneous fresh SACL recognition. [V10 §25.6]
- Fails closed by: DESIGNED — Failed TSC conditions leave the token unconsumed and prevent promotion. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.5 — One-time token lifecycle: creates and delivers the purpose-bound token on matched success. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.5.2 — Consumed token state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `consumed`, the permanently unusable state after the one authorized consumption. [V10 §25.6]
- Takes in: DESIGNED — A valid purpose-matched token whose required consume-time conditions hold. [V10 §25.6]
- Does: DESIGNED — Spends the token before the protected action begins and records consumption in security audit. [V10 §25.6]
- Gives out: DESIGNED — A consumed token that cannot authorize another action. [V10 §25.6]
- Must never: DESIGNED — Return to reusable authority or satisfy a second consume call. [V10 §25.6]
- Fails closed by: ACCEPTED — Recovery uses verified durable proof for the same already-authorized operation, never reconstitutes or consumes the token again. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

TOGETHER
- Fed by: DESIGNED — C-BAI.5 — One-time token lifecycle: fixes consumption before action and permanent non-reuse afterward. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.5.3 — Expired token state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `expired`, the token state beyond its usable lifetime. [V10 §25.6]
- Takes in: DESIGNED — The token's expiry boundary. [V10 §25.6]
- Does: DESIGNED — Removes the possibility of using that token as valid one-time authority. [V10 §25.6]
- Gives out: DESIGNED — An unusable expired token. [V10 §25.6]
- Must never: DESIGNED — Reuse the token after expiry. [V10 §25.6]
- Fails closed by: DESIGNED — No TSC consumption or promotion can proceed from an expired token. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.5 — One-time token lifecycle: preserves the expiry and non-reuse boundary. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.5.4 — Revoked token state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `revoked`, a non-valid one-time-token state. [V10 §25.6]
- Takes in: ACCEPTED — For enrollment, changed prerequisites detected between token issue and consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Revokes that issued enrollment token, writes BAI's `bai_token_revoked` audit event and leaves it unconsumed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gives out: DESIGNED — A revoked token rather than valid authorization. [V10 §25.6]
- Must never: ACCEPTED — Consume the revoked enrollment token or open the enrollment session from it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Changed enrollment prerequisites prevent consumption and opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: DESIGNED — C-BAI.5 — One-time token lifecycle: distinguishes revoked state from usable one-time authority. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.19.2 — Enrollment prerequisite revalidation | The issued token subject to changed prerequisites. | Revokes it through BAI without consumption. | The enrollment session cannot open from that token. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-ENROLL.4.2 — Final owner recheck and revocation | The issued token and freshly reread six prerequisite owners. | Takes this place's change: BAI revokes the issued token and owns `bai_token_revoked`. | BAI revokes the issued token and owns `bai_token_revoked`. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-BAI.6 — Top-security biometric lease
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `top_security_lease`, with `lease_id`, `pending_id`, `purpose = top_security_access`, `authenticated_at`, `created_at`, `expires_at`, `status` and `session_id`. [V10 §25.6]
- Takes in: DESIGNED — A successful OS result matched to its unexpired top-security pending request. [V10 §25.6]
- Does: DESIGNED — Creates a revocable lease; keeps it active until expiry or revocation; answers repeated SACL queries without consuming it. [V10 §25.6] [SOURCE CONFLICT: 04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6 labels the lease's Reusable? cell No — time-bounded, revocable, purpose-bound.]
- Gives out: DESIGNED — Current ongoing top-security biometric authority while the lease is active. [V10 §25.6]
- Must never: DESIGNED — Consume the lease as a one-time token or preserve it across a BAI restart. [V10 §25.6]
- Fails closed by: DESIGNED — Any immediate revocation trigger ends the lease; expiry or restart removes active lease authority. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.1 — Pending identity: retains the originating `pending_id`; C-BAI.3.9.1 — Top-security purpose: fixes `purpose` to `top_security_access`; C-BAI.4.2 — Artifact authentication time: carries `authenticated_at`; C-BAI.4.3 — Artifact creation time: carries `created_at`; C-BAI.4.4 — Artifact expiry: carries `expires_at`. [V10 §25.6]
- Fed by: DESIGNED — C-BAI.6.1 — Lease identity: supplies `lease_id`; C-BAI.6.2 — Lease status: supplies active, expired or revoked state; C-BAI.6.3 — Lease session identity: supplies `session_id`. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies a repeatedly queried independent biometric factor, subject to current SACL access conditions. [V10 §25.6] [V10 §25.4]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.7 — Lease lifecycle | The session-bound lease. | Keeps it queryable until expiry or revocation. | Queries do not consume the artifact. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.11 — Immediate lease revocation | The active lease. | Revokes it immediately on any listed trigger. | Current lease authority ends. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.12.2 — Current active lease | The current top-security lease. | Holds it as `active_lease`. | A restart clears the lease field. | [V10 §25.6] |
| 4 · ACCEPTED | C-BAI.18 — Current top-security owner pair | The actual current BAI lease. | Pairs it with the separately current compatible Gate 1 decision. | Neither owner alone grants top-security. | [V10 §25.6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 5 · DESIGNED | C-9.1.3 — Graduated temporary step-up | A sensitive operation requested inside an authenticated session. | Gates this place: a required top-security lease remains current, purpose-bound and revocable. | Nothing in this card. | [V10 §25.6] |

SUB-PARTS: C-BAI.6.1 — Lease identity; C-BAI.6.2 — Lease status; C-BAI.6.3 — Lease session identity

### C-BAI.6.1 — Lease identity
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `lease_id`, the lease's identity field; no primitive format is specified. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Identifies the top-security biometric lease being queried. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.6 — Top-security biometric lease | `lease_id`. | Identifies the top-security lease. | Queries refer to the actual artifact. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.6.2 — Lease status
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Lease `status`, one of `active`, `expired` or `revoked`. [V10 §25.6]
- Takes in: DESIGNED — The current lease lifecycle state. [V10 §25.6]
- Does: DESIGNED — Distinguishes ongoing queryable authority from ended authority. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat a queried lease as a consumed token. [V10 §25.6]
- Fails closed by: DESIGNED — Expired or revoked state supplies no active lease. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.6 — Top-security biometric lease | Active, expired or revoked status. | Carries current lease state. | Ended authority is distinguishable from active authority. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.6.3 — Lease session identity
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `session_id`, the session identity carried in the lease. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Keeps the lease associated with its session; session close is an immediate revocation trigger. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Keep the associated lease active after session close. [V10 §25.6]
- Fails closed by: DESIGNED — Closing the session immediately revokes its lease. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.6 — Top-security biometric lease | The lease's `session_id`. | Associates the lease with its session. | Session closure can revoke that lease. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.7 — Lease lifecycle
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — OS success → active lease → expiry or revocation, with repeated queries and no consumption. [V10 §25.6]
- Takes in: DESIGNED — A matched successful result, later SACL queries, expiry and revocation conditions. [V10 §25.6]
- Does: DESIGNED — Creates the lease on success; allows repeated queries while active; ends active authority on expiry or revocation. [V10 §25.6]
- Gives out: DESIGNED — The current active, expired or revoked lease state. [V10 §25.6]
- Must never: DESIGNED — Spend the lease during a query or keep it active through an immediate revocation trigger. [V10 §25.6]
- Fails closed by: DESIGNED — Any named revocation condition fires immediately; restart clears the lease. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.6 — Top-security biometric lease: supplies the session-bound artifact. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.7.1 — Active lease state | Successful creation of the lease. | Maintains its active queryable phase. | SACL may query repeatedly while authority remains current. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.7.2 — Expired lease state | Lease expiry. | Ends the active phase. | The lease becomes expired. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.7.3 — Revoked lease state | A revocation trigger. | Ends active authority immediately. | The lease becomes revoked. | [V10 §25.6] |

SUB-PARTS: C-BAI.7.1 — Active lease state; C-BAI.7.2 — Expired lease state; C-BAI.7.3 — Revoked lease state

### C-BAI.7.1 — Active lease state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `active`, the lease state established by matched successful authentication. [V10 §25.6]
- Takes in: DESIGNED — OS success for the bound top-security request. [V10 §25.6]
- Does: DESIGNED — Remains active until expiry or revocation and answers SACL queries repeatedly. [V10 §25.6]
- Gives out: DESIGNED — A current biometric lease factor. [V10 §25.6]
- Must never: DESIGNED — Be consumed by querying. [V10 §25.6]
- Fails closed by: DESIGNED — Expiry or any revocation trigger ends active authority. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.7 — Lease lifecycle: establishes the queryable active phase after successful authentication. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.7.2 — Expired lease state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `expired`, the lease's ended-lifetime state. [V10 §25.6]
- Takes in: DESIGNED — The lease reaching expiry. [V10 §25.6]
- Does: DESIGNED — Ends the active lease. [V10 §25.6]
- Gives out: DESIGNED — An expired lease. [V10 §25.6]
- Must never: DESIGNED — Supply ongoing authority as an active lease after expiry. [V10 §25.6]
- Fails closed by: ACCEPTED — Lease expiry ends Top-security; any fallback still requires a valid Personal Mode and current SACL/privacy intersection. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: DESIGNED — C-BAI.7 — Lease lifecycle: ends the active phase at expiry. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.7.3 — Revoked lease state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `revoked`, the lease state after a revocation trigger. [V10 §25.6]
- Takes in: DESIGNED — Any one of the immediate revocation conditions. [V10 §25.6]
- Does: DESIGNED — Revokes the lease immediately and records revocation in security audit. [V10 §25.6]
- Gives out: DESIGNED — A revoked lease without active authority. [V10 §25.6]
- Must never: DESIGNED — Keep top-security lease authority through a trigger. [V10 §25.6]
- Fails closed by: ACCEPTED — Revocation ends Top-security; a historical lease reference cannot reopen it. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: DESIGNED — C-BAI.7 — Lease lifecycle: defines immediate revocation as an end of active authority. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.8 — Independent key purposes
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The separation of manifest-signing and rollback-sealing keys. [V10 §25.6]
- Takes in: DESIGNED — Authorized manifest versions or rollback packages, according to the corresponding key's role. [V10 §25.6]
- Does: DESIGNED — Uses one key only for signing authorized manifests and the other only for rollback encryption and integrity protection; neither key derives from the other and compromise of one does not compromise the other. Specific hardware implementation remains a build-time decision. [V10 §25.6]
- Does: DECIDED-2026-09-25 — Uses different BAI keys for different token purposes; manifest-signing and rollback-sealing keys in BGMM remain separate. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 11] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]
- Gives out: DESIGNED — Signed authorized manifest versions or encrypted, integrity-protected rollback packages, with independent key compromise boundaries. [V10 §25.6]
- Must never: DESIGNED — Use either key outside its stated signing or rollback-protection role, derive either key from the other, export either private key or write either private key to a log. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI.8.1 — Manifest-signing key: signs only authorized manifest versions; C-BAI.8.2 — Rollback-sealing key: independently encrypts and integrity-protects rollback packages. [V10 §25.6]
- Fed by: DECIDED-2026-09-25 — C-BAI.8.3 — Different keys per token purpose: keeps BAI token-purpose keys different and BGMM signing/sealing keys separate. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 11] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-BAI.8.1 — Manifest-signing key; C-BAI.8.2 — Rollback-sealing key; C-BAI.8.3 — Different keys per token purpose

### C-BAI.8.1 — Manifest-signing key
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The key used only to sign authorized manifest versions. [V10 §25.6]
- Takes in: DESIGNED — An authorized manifest version. [V10 §25.6]
- Does: DESIGNED — Signs that version with a key independent of the rollback-sealing key. [V10 §25.6]
- Gives out: DESIGNED — A signed authorized manifest version. [V10 §25.6]
- Must never: DESIGNED — Sign an unauthorized version, derive from the rollback-sealing key, export the private key or log it. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — The manifest version must be authorized before signing. [V10 §25.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.8 — Independent key purposes | The manifest-only signing key. | Keeps authorized-manifest signing separate from rollback protection. | Compromise does not transfer through key derivation. | [V10 §25.6] |
| 2 · DESIGNED | C-BGMM.18.2 — Hardware-backed key mechanism | Available motherbase hardware and its protected-key capabilities. | Gates this place: keeps its independent signing role. | Nothing in this card. | [V10 §25.6] [V10 §25 / Build-Time Implementation Settings] |
| 3 · DESIGNED | C-BGMM.10.5 — Update and sign the manifest | The recorded changed-file hash and authorized manifest-signing key. | Signs the authorized new version. | Nothing in this card. | [V10 §25.13 / Change Application] |
| 4 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | Protected-file hashes and versions, the authorized signing key and the pinned public verification key. | Signs only authorized versions with the separated hardware-backed key. | Nothing in this card. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.8.2 — Rollback-sealing key
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The key used only to encrypt and integrity-protect rollback packages. [V10 §25.6]
- Takes in: DESIGNED — Rollback packages. [V10 §25.6]
- Does: DESIGNED — Encrypts and integrity-protects those packages with a key independent of manifest signing. [V10 §25.6]
- Gives out: DESIGNED — Protected rollback packages. [V10 §25.6]
- Must never: DESIGNED — Use this key outside rollback encryption/integrity protection, derive it from the manifest-signing key, export the private key or log it. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.8 — Independent key purposes | The independent rollback-sealing key. | Limits it to encryption and integrity of rollback packages. | Signing and sealing remain separate roles. | [V10 §25.6] |
| 2 · DESIGNED | C-BGMM.18.2 — Hardware-backed key mechanism | Available motherbase hardware and its protected-key capabilities. | Gates this place: keeps its separate non-derivable, non-exportable protection role. | Nothing in this card. | [V10 §25.6] [V10 §25 / Build-Time Implementation Settings] |
| 3 · DESIGNED | C-BGMM.6.4 — Package sealing and integrity | The complete rollback package and the separate rollback-sealing key. | Supplies the independent hardware-backed protection. | Nothing in this card. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 4 · DESIGNED | C-BGMM.6 — Encrypted rollback package | `session_id`, `change_description`, `file_entries` and `created_at`. | Gates this place: only its separated hardware-backed rollback protection is used. | Nothing in this card. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance] |

SUB-PARTS: NONE

### C-BAI.8.3 — Different keys per token purpose
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 11] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]

ALONE
- What it is: DECIDED-2026-09-25 — BAI key separation across token purposes, restored as FR-0003. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]
- Takes in: NOT DECIDED
- Does: DECIDED-2026-09-25 — Uses different keys for different BAI token purposes, with separate manifest-signing and rollback-sealing keys in BGMM. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]
- Gives out: NOT DECIDED
- Must never: DECIDED-2026-09-25 — Share one BAI key across different token purposes or collapse manifest signing and rollback sealing onto one key. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.8 — Independent key purposes | The restored different-keys-per-purpose rule. | Keeps BAI token-purpose keys different and BGMM signing/sealing keys separate. | The two key-separation requirements remain explicit. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 11] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §6] [98/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md §3D] |

SUB-PARTS: NONE

### C-BAI.9 — Biometric result handling
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The matched-success, unmatched-result and non-success branches of BAI result processing. [V10 §25.6]
- Takes in: DESIGNED — The OS result and current pending authorization record. [V10 §25.6]
- Does: DESIGNED — On matched success within expiry, creates the appropriate artifact, writes audit events and delivers it. An absent, expired or device-mismatched pending record yields `bai_unmatched_result` without an artifact. Any non-success outcome sets terminal pending status, notifies the requester and writes audit events. [V10 §25.6]
- Gives out: DESIGNED — The purpose-bound artifact, a rejection or a non-success notification. [V10 §25.6]
- Must never: DESIGNED — Retry a non-success biometric outcome automatically or manufacture an artifact from an unmatched result. [V10 §25.6]
- Fails closed by: DESIGNED — Creating no artifact on a failed match and terminating the pending record for `failure`, `cancelled`, `timeout`, `lockout` or `error`. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.2 — OS biometric result: supplies the outcome and audit-only OS details; C-BAI.3 — Pending authorization record: supplies the predeclared purpose, requester, expiry and app binding. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.9.1 — Matched success | A matched unexpired success. | Creates the artifact, audits, then delivers. | The requester receives the bound authorization artifact. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.9.2 — Unmatched result | Absent, expired or device-mismatched pending state. | Rejects with `bai_unmatched_result`. | No token or lease is created. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.9.3 — Authentication failure | The failure outcome. | Terminates, notifies and audits. | No automatic retry occurs. | [V10 §25.6] |
| 4 · DESIGNED | C-BAI.9.4 — Cancelled authentication | The cancelled outcome. | Ends the pending request and notifies its requester. | Cancellation is audited without automatic retry. | [V10 §25.6] |
| 5 · DESIGNED | C-BAI.9.5 — Authentication timeout | The timeout outcome. | Makes pending state terminal and records the notification/audit. | The timeout does not trigger an automatic retry. | [V10 §25.6] |
| 6 · DESIGNED | C-BAI.9.6 — Authentication lockout | The lockout outcome. | Applies terminal non-success handling. | The requester is notified and no retry starts automatically. | [V10 §25.6] |
| 7 · DESIGNED | C-BAI.9.7 — Authentication error | The error outcome. | Terminates and notifies without exposing audit-only error detail. | The error is audited and not automatically retried. | [V10 §25.6] |

SUB-PARTS: C-BAI.9.1 — Matched success; C-BAI.9.2 — Unmatched result; C-BAI.9.3 — Authentication failure; C-BAI.9.4 — Cancelled authentication; C-BAI.9.5 — Authentication timeout; C-BAI.9.6 — Authentication lockout; C-BAI.9.7 — Authentication error

### C-BAI.9.1 — Matched success
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The successful-result branch with a matching pending record still within expiry. [V10 §25.6]
- Takes in: DESIGNED — `success` and the matching live request. [V10 §25.6]
- Does: DESIGNED — Creates the appropriate lease or one-time token, writes audit events, then delivers it to the requester. [V10 §25.6]
- Gives out: DESIGNED — The artifact for the purpose declared before prompting. [V10 §25.6]
- Must never: DESIGNED — Convert OS success without a matching unexpired record into authorization. [V10 §25.6]
- Fails closed by: DESIGNED — An absent, expired or device-mismatched record causes rejection without artifact creation. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: supplies the success branch and its ordered creation, audit and delivery. [V10 §25.6]
- Gated by: DESIGNED — C-BAI.3 — Pending authorization record: the result must match an unexpired locally bound request. [V10 §25.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.2 — Unmatched result
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A result without a matching pending record because the record is expired, absent or device-mismatched. [V10 §25.6]
- Takes in: DESIGNED — The result and the failed local request match. [V10 §25.6]
- Does: DESIGNED — Rejects the result and writes `bai_unmatched_result`. [V10 §25.6]
- Gives out: DESIGNED — Rejection with no artifact. [V10 §25.6]
- Must never: DESIGNED — Create a token or lease from this result. [V10 §25.6]
- Fails closed by: DESIGNED — Withholding artifact creation. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: defines the unmatched-result rejection branch. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.3 — Authentication failure
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The OS `failure` outcome. [V10 §25.6]
- Takes in: DESIGNED — Failure of the pending biometric authentication. [V10 §25.6]
- Does: DESIGNED — Sets the pending record to terminal status, notifies the requester and writes audit events. [V10 §25.6]
- Gives out: DESIGNED — A notified and audited non-success result. [V10 §25.6]
- Must never: DESIGNED — Retry automatically. [V10 §25.6]
- Fails closed by: DESIGNED — Terminating the request without a successful artifact. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: applies the non-success terminal, notification and audit rule. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.4 — Cancelled authentication
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The OS `cancelled` outcome. [V10 §25.6]
- Takes in: DESIGNED — Cancellation of the pending biometric request. [V10 §25.6]
- Does: DESIGNED — Makes the pending record terminal, sends the requester a notification and audits the outcome. [V10 §25.6]
- Gives out: DESIGNED — A cancelled result with no successful authorization artifact. [V10 §25.6]
- Must never: DESIGNED — Automatically reopen or retry the request. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the pending request on cancellation. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: includes cancellation among terminal non-success outcomes. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.5 — Authentication timeout
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The OS `timeout` outcome. [V10 §25.6]
- Takes in: DESIGNED — A timed-out biometric request. [V10 §25.6]
- Does: DESIGNED — Sets terminal pending status, notifies the requester and records audit events. [V10 §25.6]
- Gives out: DESIGNED — A notified timeout rather than an authorization artifact. [V10 §25.6]
- Must never: DESIGNED — Retry the biometric request automatically. [V10 §25.6]
- Fails closed by: DESIGNED — Terminating the pending authorization on timeout. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: routes timeout through the non-success branch. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.6 — Authentication lockout
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The OS `lockout` outcome, with `os_lockout_type` represented separately as temporary, permanent or null. [V10 §25.6]
- Takes in: DESIGNED — The lockout result of the biometric request. [V10 §25.6]
- Does: DESIGNED — Terminates the pending record, notifies the requester and writes audit events. [V10 §25.6]
- Gives out: DESIGNED — An audited lockout outcome. [V10 §25.6]
- Must never: DESIGNED — Automatically retry following lockout. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the pending authorization without creating successful authority. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: treats lockout as a terminal non-success outcome. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.9.7 — Authentication error
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The OS `error` outcome; its optional error-code detail stays audit-only. [V10 §25.6]
- Takes in: DESIGNED — The authentication error and `os_error_code` string or null. [V10 §25.6]
- Does: DESIGNED — Sets the pending record terminal, notifies the requester and writes audit events. [V10 §25.6]
- Gives out: DESIGNED — An error notification that does not expose `os_error_code` to components. [V10 §25.6]
- Must never: DESIGNED — Retry automatically or expose audit-only error-code details to components. [V10 §25.6]
- Fails closed by: DESIGNED — Terminating the pending request on error. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.9 — Biometric result handling: supplies the error branch's terminal, notification and audit sequence. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10 — Simultaneous TSC consume conditions
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The joint token-validity and fresh recognized-Ness condition at TSC promotion consumption. [V10 §25.6]
- Takes in: DESIGNED — A valid unconsumed `one_time_authorization_token` for `tsc_promotion:<session_id>` and SACL's current fresh, non-stale recognized_ness assessment for the Ness stream. [V10 §25.6]
- Does: DESIGNED — Requires both conditions together at consume time. Speaker change, stale SIA assessment, medium-or-higher spoofing suspicion, access below recognized_ness, session end or a relevant security event invalidates the recognition condition. [V10 §25.6]
- Gives out: DESIGNED — A permitted exact-session consumption only when both conditions hold. [V10 §25.6]
- Must never: DESIGNED — Substitute token possession or earlier recognition for the simultaneous live conditions. [V10 §25.6]
- Fails closed by: DESIGNED — If either condition is unmet, leaves the token unconsumed and prevents promotion. [V10 §25.6]

TOGETHER
- Fed by: ACCEPTED — C-SACL.40 — Fresh TSC recognition-confirmation interface: supplies the current confirmation and its binding. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Gated by: DESIGNED — C-TSC.16.1 — Purpose-bound token condition: requires the valid unconsumed exact-session token; C-TSC.16.2 — Fresh recognized-Ness condition: requires fresh current recognition at consumption. [V10 §25.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.10.1 — TSC speaker-change invalidation | Detected speaker change. | Invalidates fresh recognized-Ness authorization. | The token stays unconsumed and promotion stops. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.10.2 — TSC stale-assessment invalidation | A stale SIA assessment. | Rejects stale recognition at consumption. | Neither consumption nor promotion proceeds. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.10.3 — TSC spoofing invalidation | Medium-or-higher spoofing suspicion. | Invalidates the recognition condition. | The token remains unconsumed. | [V10 §25.6] |
| 4 · DESIGNED | C-BAI.10.4 — TSC access-level invalidation | SACL level below recognized_ness. | Refuses to use the lower level as current recognition. | Promotion receives no consumption authority. | [V10 §25.6] |
| 5 · DESIGNED | C-BAI.10.5 — TSC session-end invalidation | Session end. | Invalidates the ended session's recognition. | Past recognition cannot authorize a new consume. | [V10 §25.6] |
| 6 · DESIGNED | C-BAI.10.6 — TSC security-event invalidation | A relevant security event. | Invalidates the required recognition condition. | Consumption and promotion remain stopped. | [V10 §25.6] |
| 7 · ACCEPTED | C-BAI.16 — Durable TSC consumption producer | Exact-session token validity and fresh SACL recognition together. | Requires both at consumption. | Either failing condition prevents the durable consumption path. | [V10 §25.6] |

SUB-PARTS: C-BAI.10.1 — TSC speaker-change invalidation; C-BAI.10.2 — TSC stale-assessment invalidation; C-BAI.10.3 — TSC spoofing invalidation; C-BAI.10.4 — TSC access-level invalidation; C-BAI.10.5 — TSC session-end invalidation; C-BAI.10.6 — TSC security-event invalidation

### C-BAI.10.1 — TSC speaker-change invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Detection of speaker change invalidates the fresh recognized-Ness condition. [V10 §25.6]
- Takes in: DESIGNED — A detected speaker change. [V10 §25.6]
- Does: DESIGNED — Prevents the changed-speaker state from satisfying TSC consume-time recognition. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Consume the token while this required condition is unmet. [V10 §25.6]
- Fails closed by: DESIGNED — Leaves the token unconsumed and promotion stopped. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: defines speaker change as recognition invalidation. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10.2 — TSC stale-assessment invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A stale SIA assessment invalidates consume-time recognized-Ness freshness. [V10 §25.6]
- Takes in: DESIGNED — Staleness of the identity assessment. [V10 §25.6]
- Does: DESIGNED — Makes the second TSC authorization condition unsatisfied. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Use the stale assessment to consume the token. [V10 §25.6]
- Fails closed by: DESIGNED — Performs no consumption and no promotion. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: requires non-stale recognition at the actual consume boundary. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10.3 — TSC spoofing invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Medium-or-higher spoofing suspicion invalidates TSC recognized-Ness authorization. [V10 §25.6]
- Takes in: DESIGNED — Spoofing suspicion at medium or above. [V10 §25.6]
- Does: DESIGNED — Prevents the live recognition condition from being met. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Consume the promotion token through this invalidation. [V10 §25.6]
- Fails closed by: DESIGNED — Keeps the token unconsumed and promotion blocked. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: applies the medium-or-higher suspicion boundary. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10.4 — TSC access-level invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — SACL access for the Ness stream below `recognized_ness` invalidates the second consumption condition. [V10 §25.6]
- Takes in: DESIGNED — The current SACL level of the Ness stream. [V10 §25.6]
- Does: DESIGNED — Disallows consumption based on a lower current level. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat a previous higher level as current recognition. [V10 §25.6]
- Fails closed by: DESIGNED — Leaves the token unconsumed and promotion unable to proceed. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: fixes recognized_ness as the required live level. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10.5 — TSC session-end invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Session end invalidates the current recognized-Ness condition for consumption. [V10 §25.6]
- Takes in: DESIGNED — The session ending. [V10 §25.6]
- Does: DESIGNED — Removes that ended session's ability to satisfy the live recognition condition. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Consume on recognition inherited from an ended session. [V10 §25.6]
- Fails closed by: DESIGNED — Refuses consumption and promotion while the required current condition is absent. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: includes session end among recognition invalidators. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.10.6 — TSC security-event invalidation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A relevant security event invalidates the TSC recognized-Ness condition; no additional event enumeration is selected. [V10 §25.6]
- Takes in: DESIGNED — The relevant security event. [V10 §25.6]
- Does: DESIGNED — Prevents that recognition condition from authorizing consumption. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Consume while the security event has invalidated the required condition. [V10 §25.6]
- Fails closed by: DESIGNED — Leaves the token unconsumed and promotion stopped. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: defines this security-event invalidation. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11 — Immediate lease revocation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Eight independently sufficient immediate lease revocation triggers. [V10 §25.6]
- Takes in: DESIGNED — Session close; certainty below recognized_ness_threshold; any active security-level spoofing, speaker-change or imitation-risk flag; anti-spoofing suspicion at medium or above; timeout since authenticated_at; major session break; branch continuity below threshold; explicit SACL relock. [V10 §25.6]
- Does: DESIGNED — Fires revocation immediately when any one trigger holds. [V10 §25.6]
- Gives out: DESIGNED — A revoked lease and security-audit revocation evidence. [V10 §25.6]
- Must never: DESIGNED — Wait for all triggers, continue lease authority through a trigger or use wellbeing as an input. [V10 §25.6]
- Fails closed by: DESIGNED — Ending active lease authority immediately. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies explicit relock and the applicable current access/security conditions. [V10 §25.6] [V10 §25.4]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BAI.6 — Top-security biometric lease: changes the active lease to revoked when a trigger fires. [V10 §25.6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.11.1 — Lease session-close trigger | Session close. | Treats close as independently sufficient for revocation. | The lease no longer remains active. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.11.2 — Lease certainty trigger | Certainty below recognized_ness_threshold. | Revokes at the threshold crossing. | The prior active lease ends immediately. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.11.3 — Lease security-flag trigger | Any listed active security flag. | Revokes without waiting for other flags. | Top-security lease authority ends. | [V10 §25.6] |
| 4 · DESIGNED | C-BAI.11.4 — Lease anti-spoofing trigger | Suspicion at medium or above. | Applies immediate anti-spoofing revocation. | The active lease is removed. | [V10 §25.6] |
| 5 · DESIGNED | C-BAI.11.5 — Lease timeout trigger | Timeout since authenticated_at. | Revokes at that timeout. | Authority cannot continue through timeout. | [V10 §25.6] |
| 6 · DESIGNED | C-BAI.11.6 — Lease session-break trigger | A major session break. | Revokes immediately on the break. | The lease cannot carry authority across it. | [V10 §25.6] |
| 7 · DESIGNED | C-BAI.11.7 — Lease continuity trigger | Branch continuity below threshold. | Applies the continuity revocation rule. | The active lease ends. | [V10 §25.6] |
| 8 · DESIGNED | C-BAI.11.8 — Lease explicit-relock trigger | Explicit SACL relock. | Revokes the lease immediately. | The relock removes current lease authority. | [V10 §25.6] |

SUB-PARTS: C-BAI.11.1 — Lease session-close trigger; C-BAI.11.2 — Lease certainty trigger; C-BAI.11.3 — Lease security-flag trigger; C-BAI.11.4 — Lease anti-spoofing trigger; C-BAI.11.5 — Lease timeout trigger; C-BAI.11.6 — Lease session-break trigger; C-BAI.11.7 — Lease continuity trigger; C-BAI.11.8 — Lease explicit-relock trigger

### C-BAI.11.1 — Lease session-close trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Session close as an immediate lease-revocation trigger. [V10 §25.6]
- Takes in: DESIGNED — The session closing. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the lease on session close. [V10 §25.6]
- Gives out: DESIGNED — Revoked lease authority. [V10 §25.6]
- Must never: DESIGNED — Retain the lease as active after session close. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the active lease. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: establishes session close as independently sufficient. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.2 — Lease certainty trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `assessed_certainty` dropping below `recognized_ness_threshold`. [V10 §25.6]
- Takes in: DESIGNED — The current assessed certainty and recognized-Ness threshold; no numerical threshold is selected here. [V10 §25.6]
- Does: DESIGNED — Revokes the lease immediately when certainty falls below the threshold. [V10 §25.6]
- Gives out: DESIGNED — A revoked lease. [V10 §25.6]
- Must never: DESIGNED — Continue lease authority below that threshold. [V10 §25.6]
- Fails closed by: DESIGNED — Ending active authority at the threshold crossing. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: supplies the certainty comparison as a sufficient trigger. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.3 — Lease security-flag trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Any active spoofing, speaker-change or imitation-risk flag at security level. [V10 §25.6]
- Takes in: DESIGNED — The active security-level flag. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the top-security lease. [V10 §25.6]
- Gives out: DESIGNED — Revoked lease authority. [V10 §25.6]
- Must never: DESIGNED — Treat the three flag classes as a requirement that all occur together. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the lease when any listed active flag exists. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: gives each listed active security flag revocation effect. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.4 — Lease anti-spoofing trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Anti-spoofing `suspicion_level` rising to medium or above. [V10 §25.6]
- Takes in: DESIGNED — Medium-or-higher anti-spoofing suspicion. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the lease. [V10 §25.6]
- Gives out: DESIGNED — An ended active-lease factor. [V10 §25.6]
- Must never: DESIGNED — Preserve top-security lease authority at medium or higher suspicion. [V10 §25.6]
- Fails closed by: DESIGNED — Revocation at the specified suspicion level. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: defines the medium-or-above trigger. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.5 — Lease timeout trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Timeout measured since `authenticated_at`; no duration is specified here. [V10 §25.6]
- Takes in: DESIGNED — The authentication time and elapsed lease timeout. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the lease when the timeout is reached. [V10 §25.6]
- Gives out: DESIGNED — Revoked lease authority. [V10 §25.6]
- Must never: DESIGNED — Extend authority through the timeout. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the active lease on timeout. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: fixes the timeout origin at authentication; C-BAI.4.2 — Artifact authentication time: supplies `authenticated_at`. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there |Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.6 — Lease session-break trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A major session break as an immediate revocation trigger. [V10 §25.6]
- Takes in: DESIGNED — The major session break; no duration or classifier is chosen here. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the lease. [V10 §25.6]
- Gives out: DESIGNED — A revoked lease. [V10 §25.6]
- Must never: DESIGNED — Carry active lease authority through a major session break. [V10 §25.6]
- Fails closed by: DESIGNED — Ending the active lease on the break. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: gives a major session break independent revocation effect. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.7 — Lease continuity trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Branch continuity below threshold as an immediate lease-revocation trigger. [V10 §25.6]
- Takes in: DESIGNED — Branch continuity and its threshold; no numerical threshold is specified here. [V10 §25.6]
- Does: DESIGNED — Revokes immediately when continuity falls below threshold. [V10 §25.6]
- Gives out: DESIGNED — Ended active lease authority. [V10 §25.6]
- Must never: DESIGNED — Preserve the lease below the continuity threshold. [V10 §25.6]
- Fails closed by: DESIGNED — Immediate lease revocation. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: supplies the branch-continuity comparison. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.11.8 — Lease explicit-relock trigger
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Explicit relock from SACL. [V10 §25.6]
- Takes in: DESIGNED — SACL's relock instruction. [V10 §25.6]
- Does: DESIGNED — Immediately revokes the top-security lease. [V10 §25.6]
- Gives out: DESIGNED — A revoked lease. [V10 §25.6]
- Must never: DESIGNED — Leave active lease authority after the explicit relock. [V10 §25.6]
- Fails closed by: DESIGNED — Immediate revocation on relock. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.11 — Immediate lease revocation: establishes the relock effect; C-SACL — Speaker Access-Control Layer (§25.4): issues the explicit relock. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.12 — Volatile BAI state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `BAI_state`, held in memory only, with nothing retained across restarts. [V10 §25.6]
- Takes in: DESIGNED — `pending_record`, `active_lease`, `active_one_time_tokens`, `lockout_state`, `lockout_since`, `app_session_key_ref`, `session_id` and `last_audit_event_id`. [V10 §25.6]
- Does: DESIGNED — Holds at most one pending record, one active lease and a token-ID-to-token map; on restart clears all state and moves `biometric_state` to `not_verified`. [V10 §25.6]
- Gives out: DESIGNED — Current volatile biometric authorization state. [V10 §25.6]
- Must never: DESIGNED — Restore volatile authorization through a restart. [V10 §25.6]
- Fails closed by: DESIGNED — Clearing state and requiring reauthentication after restart. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.8 — App-instance key reference: supplies the `app_session_key_ref` held in current BAI state. [V10 §25.6]
- Fed by: DESIGNED — C-BAI.12.1 — Current pending record: holds one record or null; C-BAI.12.2 — Current active lease: holds the lease or null; C-BAI.12.3 — Active one-time token map: maps token identities to records; C-BAI.12.4 — Current lockout state: holds none, temporary or permanent; C-BAI.12.5 — Lockout start time: carries timestamp or null; C-BAI.12.6 — BAI session identity: carries current session identity; C-BAI.12.7 — Last audit-event identity: carries the current audit reference. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.14 — Restart and invalid-result failures | Memory-only BAI state. | Applies clearing and invalid-result rules. | A restart supplies no surviving token or lease authority. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.14.1 — Restart state clearing | All current volatile BAI fields. | Clears every field on restart. | Pending requests, leases and tokens do not survive. | [V10 §25.6] |

SUB-PARTS: C-BAI.12.1 — Current pending record; C-BAI.12.2 — Current active lease; C-BAI.12.3 — Active one-time token map; C-BAI.12.4 — Current lockout state; C-BAI.12.5 — Lockout start time; C-BAI.12.6 — BAI session identity; C-BAI.12.7 — Last audit-event identity

### C-BAI.12.1 — Current pending record
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `pending_record`, a single pending authorization record or null. [V10 §25.6]
- Takes in: DESIGNED — The current locally prepared request. [V10 §25.6]
- Does: DESIGNED — Holds that request in volatile BAI state. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Hold more than one pending record. [V10 §25.6]
- Fails closed by: DESIGNED — Losing the pending record on restart; delayed results cannot recover it. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3 — Pending authorization record: supplies the one purpose-bound pending request. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | One pending record or null. | Holds the current request. | Multiple pending records cannot accumulate. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.2 — Current active lease
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `active_lease`, a `top_security_lease` or null. [V10 §25.6]
- Takes in: DESIGNED — The current top-security lease. [V10 §25.6]
- Does: DESIGNED — Holds the lease in memory for current repeated queries. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Preserve active lease state across restart. [V10 §25.6]
- Fails closed by: DESIGNED — Clearing the lease on restart. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.6 — Top-security biometric lease: supplies the lease held by BAI state. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | A top-security lease or null. | Holds current lease state in memory. | Restart preserves no active lease. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.3 — Active one-time token map
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `active_one_time_tokens`, a map from `token_id` to `one_time_authorization_token`. [V10 §25.6]
- Takes in: DESIGNED — Current token identities and token records. [V10 §25.6]
- Does: DESIGNED — Keeps the token map in memory only. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: ACCEPTED — Treat the vanished map as surviving authority or reconstruct a consumed token from a durable receipt. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Fails closed by: DESIGNED — Clearing all token state on restart. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.4 — One-time authorization token: supplies each map value; C-BAI.4.1 — Token identity: supplies its key. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | The token-ID-to-token map. | Keeps live one-time token records in memory. | The map disappears on restart. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.4 — Current lockout state
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `lockout_state`, with values `none`, `temporary` or `permanent`. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Retains current lockout state in memory. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Persist this BAI state across restart. [V10 §25.6]
- Fails closed by: DESIGNED — Restart clears all BAI state and requires biometric reauthentication. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | None, temporary or permanent lockout state. | Retains the current lockout label. | The label remains volatile BAI state. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.5 — Lockout start time
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `lockout_since`, a timestamp or null. [V10 §25.6]
- Takes in: DESIGNED — BAI's trusted local clock rather than an OS-provided timestamp. [V10 §25.6 / What BAI Receives From the OS]
- Does: DESIGNED — Carries the lockout time in volatile BAI state. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Persist as BAI state across restart. [V10 §25.6]
- Fails closed by: DESIGNED — On restart all BAI state is cleared, `biometric_state` becomes `not_verified`, and reauthentication is required. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | Lockout timestamp or null. | Carries `lockout_since`. | The lockout time is part of current state only. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.6 — BAI session identity
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `session_id` in `BAI_state`; no additional type or serialization is selected. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Carries current session identity in BAI's memory-only state. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Persist this BAI state through restart. [V10 §25.6]
- Fails closed by: DESIGNED — On restart all BAI state is cleared, `biometric_state` becomes `not_verified`, and reauthentication is required. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | Current session identity. | Carries the BAI session field. | Restart clears that volatile identity. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.12.7 — Last audit-event identity
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — `last_audit_event_id`, the final named field of `BAI_state`; no primitive format is supplied. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Holds the last audit-event reference in volatile state. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Preserve this volatile field through restart. [V10 §25.6]
- Fails closed by: DESIGNED — The volatile field does not persist through restart. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.12 — Volatile BAI state | Last audit-event identity. | Retains the current event reference. | The volatile field does not persist through restart. | [V10 §25.6] |

SUB-PARTS: NONE

### C-BAI.13 — Physical-command and security-audit separation
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The boundary between BOP's minimal physical-command roots and BAI's security audit. [V10 §25.6]
- Takes in: DESIGNED — Biometric prompt/results and local security operations. [V10 §25.6]
- Does: DESIGNED — Sends BOP only `prompt_opened` and the six `result:` outcomes, with session ID and trusted-local timestamp. Keeps purpose binding, challenge creation, artifact creation, consumption, revocation, purpose mismatch, requester identity and security-policy consequences in security audit. [V10 §25.6]
- Gives out: DESIGNED — Distinct physical facts and security-audit facts. [V10 §25.6]
- Must never: DESIGNED — Put token identity, challenge, purpose or authorization conclusions in a BOP biometric-command root. [V10 §25.6]
- Fails closed by: DESIGNED — Malformed-result rejection does not log potentially biometric fields. [V10 §25.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: receives only the permitted physical-command fact. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.13.1 — Permitted biometric physical facts | The seven permitted physical command facts. | Provides only session identity and local time with the event. | BOP receives no security conclusions or token detail. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.13.2 — BAI security-audit ownership | Purpose and authorization facts. | Records them inside BAI's separate security audit. | Physical-command roots do not become security-audit records. | [V10 §25.6] |

SUB-PARTS: C-BAI.13.1 — Permitted biometric physical facts; C-BAI.13.2 — BAI security-audit ownership

### C-BAI.13.1 — Permitted biometric physical facts
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The seven BOP biometric `system_command` facts: `prompt_opened`, `result:success`, `result:failure`, `result:cancelled`, `result:timeout`, `result:lockout`, `result:error`. [V10 §25.6]
- Takes in: DESIGNED — The actual prompt/result fact, `session_id` and N.H local-clock timestamp. [V10 §25.6]
- Does: DESIGNED — Provides the physical fact with only those two contextual fields. [V10 §25.6]
- Gives out: DESIGNED — A minimal BOP system-command root. [V10 §25.6]
- Must never: DESIGNED — Include `token_id`, `challenge`, `purpose` or authorization conclusions. [V10 §25.6]
- Must never: ACCEPTED — Claim that biometric success identifies Ness by name or include requester/lease security details. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Without an actual committed enrollment opening and its BAI fact, no enrollment success observation is fabricated. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-BAI.13 — Physical-command and security-audit separation: fixes the minimal observable event vocabulary and boundary. [V10 §25.6]
- Gated by: DESIGNED — The committed enrollment success exists before the facts are opened. [V10 §25.6]
- Changes: ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: records the physical command without security conclusions. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.13.2 — BAI security-audit ownership
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Security-audit recording of BAI's purpose and authorization facts. [V10 §25.6]
- Takes in: DESIGNED — Purpose binding; challenge creation; token and lease creation; consumption; revocation; purpose mismatch; requester identity; security-policy consequences. [V10 §25.6]
- Does: DESIGNED — Records these facts in security audit, separately from BOP physical-command observations. [V10 §25.6]
- Does: ACCEPTED — Alone writes actual BAI consumption and revocation audit events; a coordinator retains references rather than manufacturing BAI events. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gives out: DESIGNED — Audit evidence of the actual security operation and consequences. [V10 §25.6]
- Must never: ACCEPTED — Put biometric data, challenges, private keys or raw token material into any log. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Failure to write or verify a required durable consumption receipt supplies no surviving authorization; the uncertain token is terminal. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

TOGETHER
- Fed by: DESIGNED — C-BAI.13 — Physical-command and security-audit separation: assigns security facts to BAI's audit boundary. [V10 §25.6]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): security-record access must meet privacy and authorization rules; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization remains required for those records. [MAP C-BAI]
- Changes: ACCEPTED — C-TSC.16.7 — Durable consumption receipt: supplies BAI's actual committed and flushed consumption evidence. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.14 — Restart and invalid-result failures
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Restart, delayed-result, duplicate-result and malformed-result handling. [V10 §25.6]
- Takes in: DESIGNED — A restart or the corresponding invalid result. [V10 §25.6]
- Does: DESIGNED — Clears state on restart and writes `bai_restart_state_cleared`; rejects delayed, duplicate and malformed results with their respective rejection events. [V10 §25.6]
- Gives out: DESIGNED — Fail-closed state or an audited rejection. [V10 §25.6]
- Must never: DESIGNED — Restore vanished biometric authority, accept a resolved pending request again or log potentially biometric fields from malformed results. [V10 §25.6]
- Fails closed by: DESIGNED — Reauthentication after restart and rejection of invalid results. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.12 — Volatile BAI state: clears rather than persists on restart. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.14.1 — Restart state clearing | A BAI restart. | Clears state and records `bai_restart_state_cleared`. | Biometric state becomes not_verified and requires reauthentication. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.14.2 — Delayed-result rejection | A delayed result without a pending match. | Rejects it as `bai_delayed_result_rejected`. | No old request is restored. | [V10 §25.6] |
| 3 · DESIGNED | C-BAI.14.3 — Duplicate-result rejection | A repeated result after pending resolution. | Rejects it as `bai_duplicate_result_rejected`. | The request cannot create another artifact. | [V10 §25.6] |
| 4 · DESIGNED | C-BAI.14.4 — Malformed-result rejection | A malformed result. | Rejects it without logging potentially biometric fields. | The audit records `bai_malformed_result_rejected` only within its safe boundary. | [V10 §25.6] |

SUB-PARTS: C-BAI.14.1 — Restart state clearing; C-BAI.14.2 — Delayed-result rejection; C-BAI.14.3 — Duplicate-result rejection; C-BAI.14.4 — Malformed-result rejection

### C-BAI.14.1 — Restart state clearing
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The fail-closed BAI restart transition. [V10 §25.6]
- Takes in: DESIGNED — Restart of BAI. [V10 §25.6]
- Does: DESIGNED — Clears all `BAI_state`, sets `biometric_state` to `not_verified`, requires reauthentication and writes `bai_restart_state_cleared`. [V10 §25.6]
- Gives out: DESIGNED — No surviving volatile biometric authorization. [V10 §25.6]
- Must never: DESIGNED — Retain pending requests, leases or active tokens across restart. [V10 §25.6]
- Fails closed by: DESIGNED — Requiring a new biometric authentication for new authority. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.14 — Restart and invalid-result failures: defines the restart rule. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BAI.12 — Volatile BAI state: clears every field on restart. [V10 §25.6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.14.2 — Delayed-result rejection
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A delayed result with no matching pending record. [V10 §25.6]
- Takes in: DESIGNED — The delayed result. [V10 §25.6]
- Does: DESIGNED — Rejects it as `bai_delayed_result_rejected`. [V10 §25.6]
- Gives out: DESIGNED — Rejection rather than recovered authorization. [V10 §25.6]
- Must never: DESIGNED — Accept it without a matching pending record. [V10 §25.6]
- Fails closed by: DESIGNED — Rejecting the delayed result. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.14 — Restart and invalid-result failures: supplies the delayed-result rejection rule. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.14.3 — Duplicate-result rejection
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — A duplicate result whose pending record is already resolved. [V10 §25.6]
- Takes in: DESIGNED — The repeated result. [V10 §25.6]
- Does: DESIGNED — Rejects it as `bai_duplicate_result_rejected`. [V10 §25.6]
- Gives out: DESIGNED — A duplicate-result rejection. [V10 §25.6]
- Must never: DESIGNED — Resolve the same pending request into a second authorization artifact. [V10 §25.6]
- Fails closed by: DESIGNED — Rejecting the duplicate after pending resolution. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.14 — Restart and invalid-result failures: identifies the already-resolved-request rejection. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.14.4 — Malformed-result rejection
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Rejection of a malformed biometric result. [V10 §25.6]
- Takes in: DESIGNED — The malformed result. [V10 §25.6]
- Does: DESIGNED — Rejects it and writes `bai_malformed_result_rejected`, without logging potentially biometric fields. [V10 §25.6]
- Gives out: DESIGNED — An audited malformed-result rejection. [V10 §25.6]
- Must never: DESIGNED — Log potentially biometric fields from the rejected payload. [V10 §25.6]
- Fails closed by: DESIGNED — Rejecting malformed input without exposing those fields. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.14 — Restart and invalid-result failures: defines the rejection and restricted logging. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15 — Protected-core biometric laws
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The six protected-core boundaries on BAI's data, authority and purpose. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Keeps biometric data outside BAI, purposes distinct, consumed/expired tokens unusable, pending requests singular, protected safeguards unoverrideable and wellbeing outside authorization. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Receive, store, inspect, reconstruct or process fingerprint data; cross purposes; reuse consumed or expired tokens; allow multiple pending records; expose root/safeguard override; query §22. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-BAI.15.1 — No fingerprint-data handling; C-BAI.15.2 — No cross-purpose authority; C-BAI.15.3 — No spent-token reuse; C-BAI.15.4 — One pending request; C-BAI.15.5 — No protected-core override; C-BAI.15.6 — No wellbeing query

### C-BAI.15.1 — No fingerprint-data handling
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — The absolute fingerprint-data boundary. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Leaves fingerprint data outside the BAI interface at every stage. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Receive, store, inspect, reconstruct or process fingerprint data. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15.2 — No cross-purpose authority
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — An artifact's creation purpose cannot authorize another purpose. [V10 §25.6]
- Takes in: DESIGNED — The purpose bound before prompting and the purpose requested at consumption. [V10 §25.6]
- Does: DESIGNED — Verifies purpose on every consume call. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Accept a token for a different purpose. [V10 §25.6]
- Fails closed by: DESIGNED — Wrong-purpose TSC tokens remain unconsumed and cannot promote. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.3 — Pending purpose: supplies the purpose fixed before the prompt. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15.3 — No spent-token reuse
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Consumed and expired tokens cannot be reused. [V10 §25.6]
- Takes in: DESIGNED — The token's current state. [V10 §25.6]
- Does: DESIGNED — Keeps consumption permanently single-use and expiry non-reusable. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Reuse a consumed token or an expired token. [V10 §25.6]
- Fails closed by: DESIGNED — A non-valid or already-consumed token fails the TSC token condition and cannot promote. [V10 §25.6]

TOGETHER
- Fed by: DESIGNED — C-BAI.4.5 — Token status: supplies validity, consumption, expiry and revocation state. [V10 §25.6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15.4 — One pending request
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — At most one pending authorization record at a time. [V10 §25.6]
- Takes in: DESIGNED — Requests for biometric authorization. [V10 §25.6]
- Does: DESIGNED — Holds a single pending record. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Maintain concurrent pending biometric requests. [V10 §25.6]
- Fails closed by: ACCEPTED — The enrollment authorization interface refuses a concurrent pending request, without automatic retry. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15.5 — No protected-core override
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — BAI has no interface for overriding immutable roots or protected safeguards. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Preserves the protected-core boundary across biometric authorization. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Expose an override of immutable roots or protected safeguards. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.15.6 — No wellbeing query
Stamp: DESIGNED    Source: [V10 §25.6]

ALONE
- What it is: DESIGNED — Wellbeing is outside BAI's authorization inputs. [V10 §25.6]
- Takes in: NOT DECIDED
- Does: DESIGNED — Keeps the wellbeing system uninvolved in BAI. [V10 §25.6]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Query §22 or use wellbeing in biometric authorization. [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.16 — Durable TSC consumption producer
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — BAI's live validation/consumption boundary and durable security-audit proof for the separately committed TSC authorization. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Takes in: ACCEPTED — C1 request fields `session_id`, `bai_token_id`, exact `purpose = tsc_promotion:<session_id>` and proposed `authorization_operation_id`; current SACL recognition accompanies the consume boundary. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Does: ACCEPTED — Consumes only the winning claim's attached token after live validation; commits and flushes `bai_token_consumed` before reporting success. BAI and B15 remain separate stores. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gives out: ACCEPTED — C1 response `token_state`, `purpose_binding`, `validity`, and `consumption_evidence_ref` or `refusal_reason`. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Must never: ACCEPTED — Consume to test downstream feasibility, report success before receipt durability, merge stores into a simulated transaction or recover authority from the vanished token map. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Fails closed by: ACCEPTED — Missing, partial, contradictory, wrong-session, wrong-purpose or unverifiable receipts permit neither authorization nor promotion; the waiting session remains untouched. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

TOGETHER
- Fed by: DESIGNED — C-TSC.29.1 — BAI consume boundary: carries the C1 request and response at the existing canonical interface. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Gated by: DESIGNED — C-BAI.10 — Simultaneous TSC consume conditions: requires exact-session token validity and fresh SACL recognition together. [V10 §25.6]
- Changes: ACCEPTED — C-TSC.16.7 — Durable consumption receipt: writes the complete verified, committed and flushed consumption evidence. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.16.1 — Winning-claim consumption boundary | The one-winner claim/consume protocol. | Consumes only the winning attached token. | A second token cannot establish a second receipt for the session. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] |
| 2 · ACCEPTED | C-BAI.16.2 — Live TSC validation | The live request before A2. | Validates read-only before spending authority. | Downstream feasibility is not tested by consumption. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] |
| 3 · ACCEPTED | C-BAI.16.3 — Flushed receipt commit point | The validated winning consumption. | Commits and flushes its complete receipt before success. | Only durable proof survives restart. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] |
| 4 · ACCEPTED | C-BAI.16.4 — Uncertain-consumption failure | An absent or unverifiable consumption receipt. | Treats the uncertain token as terminal and keeps B15 unauthorized. | Continuation needs new biometric authority through linked claim closure. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] |
| 5 · ACCEPTED | C-BAI.16.5 — Receipt-bound TSC recovery | A verified durable receipt and actual B15 state. | Completes only missing work for the same authorized operation. | No second fingerprint, consume or authorization event is created. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] |
| 6 · ACCEPTED | C-BAI.16.6 — Live consume-blocked audit event | A failed live consume condition with the token still unconsumed. | Writes BAI's own blocked-consume event. | Recovery can reference the event but cannot fabricate it. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] |
| 7 · ACCEPTED | C-BAI.21 — Owner proof across coordination boundaries | Actual flushed TSC consumption proof. | Keeps the receipt as surviving authority across coordinator references. | A claim or checkpoint cannot replace the proof. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |

SUB-PARTS: C-BAI.16.1 — Winning-claim consumption boundary; C-BAI.16.2 — Live TSC validation; C-BAI.16.3 — Flushed receipt commit point; C-BAI.16.4 — Uncertain-consumption failure; C-BAI.16.5 — Receipt-bound TSC recovery; C-BAI.16.6 — Live consume-blocked audit event

### C-BAI.16.1 — Winning-claim consumption boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

ALONE
- What it is: ACCEPTED — The requirement that only the token attached to the one winning session/purpose claim is consumed. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Takes in: ACCEPTED — Proposed `authorization_claim_id`, keyed by `session_id` plus `purpose`, and its attached proposed `authorization_operation_id`, deterministically derived from `session_id` plus `bai_token_id`. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Does: ACCEPTED — Requires the coordination-only claim before touching the token. Allows at most one active-or-successful authorization per session/purpose. A second token for an already claimed or authorized session is not consumed; the request returns the existing reference or fails closed. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gives out: ACCEPTED — At most one successful durable consumption receipt for the session authorization. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Must never: ACCEPTED — Grant authority from the claim alone, consume a losing token or replace a durably consumed token with another for the same authorization. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Fails closed by: ACCEPTED — Replacement requires a durably terminal pre-consumption operation, or a revoked unconsumed token and safely superseded old claim; releases and supersessions are append-only and explicitly linked. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies the consumption protocol; C-TSC.16.4 — Authorization claim record: supplies the already-written session/purpose winner. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gated by: ACCEPTED — C-TSC.16.4 — Authorization claim record: only its winning attached token may be consumed, with safe linked closure before any replacement. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.16.3 — Flushed receipt commit point | The already-written winning claim and attached token. | Requires the winner before A2. | Losing or replacement tokens cannot create duplicate authority. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] |

SUB-PARTS: NONE

### C-BAI.16.2 — Live TSC validation
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.1] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

ALONE
- What it is: ACCEPTED — Read-only validation at A1 before the protected A2 consumption. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Takes in: ACCEPTED — The winning attached token, fresh SACL confirmation now and B15 confirmation that the session is `sealed` or `interrupted`. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Does: ACCEPTED — Checks the token is valid, unconsumed, unexpired, unrevoked, purpose-matched and for this exact session; requires current non-stale recognized Ness at consumption. The SACL response carries `recognized_ness_confirmed`, `confirmation_id`, `confirmed_at` and `freshness_state`. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.1] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Gives out: ACCEPTED — A validated pending consumption or refusal without consuming the token. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Must never: ACCEPTED — Spend authority to test whether later work might succeed or inherit stale recognition for a new consume after restart. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing, stale, conflicting or unverifiable current conditions prevent consumption. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies the A1-before-A2 boundary. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gated by: DESIGNED — C-TSC.16.1 — Purpose-bound token condition: the attached token must pass all current token checks; C-TSC.16.2 — Fresh recognized-Ness condition: supplies the required live SACL recognition. [V10 §25.6] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.16.3 — Flushed receipt commit point | Current successful token and recognition checks. | Requires the validated consume boundary. | No receipt success is reported from failed live conditions. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] |

SUB-PARTS: NONE

### C-BAI.16.3 — Flushed receipt commit point
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

ALONE
- What it is: ACCEPTED — A2 consumption plus the committed and flushed `bai_token_consumed` receipt, the durable authorization commit point. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Takes in: ACCEPTED — At minimum: proposed `authorization_operation_id`; exact `session_id`; exact `bai_token_id`; exact `tsc_promotion:<session_id>` purpose; SACL confirmation identity; SACL confirmation timestamp; BAI consumption timestamp; requester/coordinator identity; receipt schema/version; integrity reference. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Does: ACCEPTED — Consumes the winning token in the live process and commits and flushes the complete verified receipt before returning success. A receipt already durable for the same proposed `authorization_operation_id` yields idempotent success without consuming again. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gives out: ACCEPTED — Durable consumption proof independent of BAI's volatile token map. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Must never: ACCEPTED — Return consumption success before the receipt is durable, bind another operation/session to this receipt or retry the original token across a restart. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Fails closed by: ACCEPTED — Failed or unverifiable receipt writing leaves B15 unauthorized and the uncertain token terminal; wrong-operation or wrong-session binding is refused. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies A2's receipt-producing boundary. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Gated by: ACCEPTED — C-BAI.16.1 — Winning-claim consumption boundary: only the attached winning token can reach A2; C-BAI.16.2 — Live TSC validation: current token and recognition checks must pass. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]
- Changes: ACCEPTED — C-TSC.16.7 — Durable consumption receipt: produces the complete proof whose ten binding atoms retain their canonical ownership. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.16.4 — Uncertain-consumption failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

ALONE
- What it is: ACCEPTED — Consumption without a verified durable receipt, before a crash or after an in-process receipt-write failure. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — An absent or unverifiable consumption receipt and the actual prior waiting state. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Does: ACCEPTED — Grants no authority. The old operation becomes durably `failed`; its claim becomes `released` or `superseded` through an explicitly linked append. Proposed `tsc_authorization_stage_event` records the exact reason and proposed `tsc_crossstore_recovery_event` records `action_taken = blocked_fail_closed`. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — An unchanged `sealed` or `interrupted` session waiting indefinitely; continuation needs a new biometric flow, new token and new proposed `authorization_operation_id` through linked claim supersession. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Retry or resurrect the uncertain original token, infer safe reuse from missing audit, turn claim state into authority or fabricate `bai_token_consume_blocked` during recovery. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Fails closed by: ACCEPTED — Keeping B15 unauthorized and the original token unusable; after restart that token no longer exists. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: distinguishes live token state from durable authority. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-TSC.16.9 — Authorization crash recovery: receives the no-receipt failure boundary and preserves the waiting session. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.16.5 — Receipt-bound TSC recovery
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

ALONE
- What it is: ACCEPTED — Recovery whose authority is the flushed receipt, followed by B15's committed transaction. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — Verified receipt bindings for operation, session, purpose, token, SACL identity/time and integrity, plus actual B15 committed state. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Does: ACCEPTED — After receipt commit but before B15 commit, forward-completes B15 exactly once. After B15 commit, repairs only a missing external acknowledgment idempotently. The B15 transaction is whole: authorized lifecycle, authorization time, token ID, SACL confirmation time, lifecycle event and `cache_authorization_received` reference. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — Completion of the same already-authorized transition, not new biometric authority. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Request a second fingerprint, reconsume the token, create a second authorization event or use a receipt for another session/purpose. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Fails closed by: ACCEPTED — Missing, partial, contradictory, wrong-session, wrong-purpose or unverifiable proof permits neither authorization nor promotion and leaves the session untouched. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies the durability boundary. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gated by: ACCEPTED — C-TSC.16.7 — Durable consumption receipt: exact complete binding and integrity must verify before forward completion. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Changes: ACCEPTED — C-TSC.16.9 — Authorization crash recovery: permits only the missing authorized completion or external-acknowledgment repair. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.16.6 — Live consume-blocked audit event
Stamp: ACCEPTED    Source: [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] [V10 §7E-TSC / 29. Integration Boundaries]

ALONE
- What it is: ACCEPTED — `bai_token_consume_blocked`, owned only by BAI for a live in-process consume attempt whose required condition failed while the token remained unconsumed. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Takes in: DESIGNED — `session_id`, `token_purpose` and the actual `reason` for refusing consumption. [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.2]
- Does: ACCEPTED — Records the actual live BAI refusal; later recovery may reference a genuine pre-crash event. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — Audit evidence of that blocked live consume attempt. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Be created or backfilled by recovery, stand for receipt-write uncertainty after possible consumption, or be inferred from absent audit history. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Fails closed by: DESIGNED — Refusing consumption while a required live condition fails. [V10 §7E-TSC / 29. Integration Boundaries]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: owns the actual live refusal boundary. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-TSC.26.20 — BAI consume-blocked event: supplies the genuine BAI event and its three canonical fields. [V10 §7E-TSC / 29. Integration Boundaries]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.17 — Personal-mode biometric opening boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

ALONE
- What it is: ACCEPTED — The purpose-bound BAI proof used by the explicit Personal Mode opening path. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Takes in: ACCEPTED — An explicit opening action, the stable proposed `personal_mode_open_operation_id`, mode session, runtime epoch, base generation and reserved target generation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Does: ACCEPTED — Binds proposed `extended:personal_mode_open:<personal_mode_open_operation_id>` before the OS prompt; on successful verification produces a one-time proof, consumed once for that exact opening before mode activation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gives out: ACCEPTED — Biometric proof for the one Personal Mode opening operation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Must never: ACCEPTED — Open Personal Mode from `top_security_access`, `tsc_promotion:<session_id>`, `voice_enrollment_ness`, `bgmm_confirmation:…` or any other purpose; use this opening proof to unlock top-security; retain biometric data in mode records. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Fails closed by: ACCEPTED — Absent, expired, revoked, wrong-purpose or unverifiable BAI proof does not satisfy this gate; BAI unavailability blocks this fingerprint path while an unrelated BAI outage does not block PIN-only opening. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies the explicit opening request and its mode-operation bindings. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gated by: DESIGNED — C-BAI.3.9.5 — Extended purpose namespace: the opening uses its exact declared extension purpose, bound before prompting. [V10 §25.6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Changes: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies one consumed opening proof, with activation still dependent on fresh SACL and explicit-action binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.17.1 — Exact Personal-mode opening purpose | The stable exact opening operation. | Binds the proposed operation-specific purpose before prompting. | The proof is restricted to this opening. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 2 · ACCEPTED | C-BAI.17.2 — Mode proof validation before activation | The opening proof with current operation/session/epoch/generation context. | Requires complete validation, consumption, fresh SACL and explicit-action binding. | Only the validated transition may activate. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 3 · ACCEPTED | C-BAI.17.3 — Consumed opening proof after crash | Consumed proof followed by a crash before activation. | Keeps mode dry and requires a new explicit action and token. | Durable audit cannot restore volatile Personal Mode. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 4 · DESIGNED | C-9.1.4.3 — Stronger fingerprint alternative | The exact purpose-bound opening proof produced and consumed by BAI. | Supplies, as the biometric owner, the exact consumed proof. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [V10 §9] |
| 5 · ACCEPTED | C-9.6 — Personal Mode opening sequence | A deliberate action from an accepted trusted surface, stable personal_mode_open_operation_id [proposed], current mode_runtime_epoch_id [proposed], base_mode_generation [proposed], reserved target_mode_generation [proposed], owner-held factor proof and fresh atomic SACL/observability truth. | Supplies what this place relies on: exact consumed proof when fingerprint is used. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 6 · ACCEPTED | C-9.6.13 — Fingerprint opening consumer path | Explicit opening action, stable parent/session, current epoch/base/reserved target and BAI's exact-purpose proof. | Supplies what this place relies on: BAI remains the proof owner. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 7 · ACCEPTED | C-9.6.2 — Opening factor verification | PIN verification or the exact consumed purpose-bound biometric proof. | Supplies a consumed exact-purpose alternative. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |

SUB-PARTS: C-BAI.17.1 — Exact Personal-mode opening purpose; C-BAI.17.2 — Mode proof validation before activation; C-BAI.17.3 — Consumed opening proof after crash

### C-BAI.17.1 — Exact Personal-mode opening purpose
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

ALONE
- What it is: ACCEPTED — The proposed purpose `extended:personal_mode_open:<personal_mode_open_operation_id>` printed in §5B; §§6 and 17 print the proposed placeholder form `extended:personal_mode_open:<open_operation_id>`. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]
- Takes in: ACCEPTED — The exact opening-operation identity supplied by the mode coordinator after the explicit action. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Does: ACCEPTED — Declares and binds this operation-specific purpose before the OS prompt. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gives out: ACCEPTED — A purpose-bound opening proof for that operation alone. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Must never: ACCEPTED — Substitute another purpose or use an opening token for top-security. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Fails closed by: ACCEPTED — A proof carrying any other purpose gives no opening authority. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: ACCEPTED — C-BAI.17 — Personal-mode biometric opening boundary: supplies the stable operation and pre-prompt binding order. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9.12.4.5 — Opening biometric purpose field | Exactly `extended:personal_mode_open:<personal_mode_open_operation_id>` [proposed]. | Supplies purpose-bound owner proof. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 2 · ACCEPTED | C-9.6.13 — Fingerprint opening consumer path | Explicit opening action, stable parent/session, current epoch/base/reserved target and BAI's exact-purpose proof. | Supplies the exact proposed purpose string. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 3 · ACCEPTED | C-9.17.14 — Wrong-purpose biometric opening proof | Wrong-purpose biometric proof. | Gates this place: proof is tied to this opening purpose. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |
| 4 · ACCEPTED | C-9.1.4.7 — Other-purpose biometric exclusion | A proposed biometric artifact and its actual purpose. | Gates this place: only its exact proposed opening purpose is valid. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |


SUB-PARTS: NONE

### C-BAI.17.2 — Mode proof validation before activation
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

ALONE
- What it is: ACCEPTED — Mode-owner validation of the BAI proof before activation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Takes in: ACCEPTED — Exact purpose, requester, operation identity, session identity, runtime epoch, base generation, reserved target generation, validity, expiry and revocation state. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Does: ACCEPTED — Requires all bindings to verify before activation, consumes the proof once for the exact opening, and permits mode commit only after successful consumption, a fresh SACL check and the explicit-action binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gives out: ACCEPTED — An opening proof usable only within that validated mode transition. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Must never: ACCEPTED — Treat a proof from another operation, session, purpose, device boundary, epoch or generation as current opening authority. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — Missing or unverifiable bindings, a non-current base generation or unavailable required authority prevent activation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: ACCEPTED — C-BAI.17 — Personal-mode biometric opening boundary: supplies the BAI proof and the bounded opening context. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gated by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the explicit action and current mode-operation bindings must verify; C-SACL — Speaker Access-Control Layer (§25.4): a fresh check is required before activation commit. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9.6.13 — Fingerprint opening consumer path | Explicit opening action, stable parent/session, current epoch/base/reserved target and BAI's exact-purpose proof. | Gates this place: every proof dimension must verify. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] |


SUB-PARTS: NONE

### C-BAI.17.3 — Consumed opening proof after crash
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

ALONE
- What it is: ACCEPTED — A crash after token consumption and before Personal Mode activation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Takes in: ACCEPTED — The consumed proof and durable BAI audit history without committed mode activation. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Does: ACCEPTED — Keeps mode `dry`; requires a new explicit action and new token. Durable audit remains proof of what occurred and cannot restore volatile mode. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gives out: ACCEPTED — Dry mode with historical consumption evidence. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Must never: ACCEPTED — Forward-complete or restore Personal Mode from the consumed token after crash. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Fails closed by: ACCEPTED — Requiring the new explicit action and fresh token before a later opening attempt. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

TOGETHER
- Fed by: ACCEPTED — C-BAI.17 — Personal-mode biometric opening boundary: fixes the pre-activation crash rule for this purpose. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): stays dry; the audit cannot restore its volatile session. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9.10.3 — Crash after factor before mode commit | The owner's verification result or BAI's durable consumption audit, solely as history of what occurred. | Supplies what this place relies on: consumed proof is history, not renewed authority. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §10 / After factor verification, before mode commit] |
| 2 · ACCEPTED | C-9.12.4.6 — Opening proof consumption reference | BAI's durable audit of the single proof consumption. | Supplies durable consumption history and nonrestoration rule. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §10 / After factor verification, before mode commit] |


SUB-PARTS: NONE

### C-BAI.18 — Current top-security owner pair
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The conjunction of the actual BAI lease and current SACL Gate 1 decision at top-security use time. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Takes in: ACCEPTED — Current, mutually compatible `bai_lease_ref` and `sacl_gate1_decision_ref`, owned separately by BAI and SACL. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Does: ACCEPTED — Requires both live truths. SACL Gate 1 retains biometric verification within timeout, Ness's Person-Box at high certainty, sufficient score separation, no spoofing suspicion, no `imitation_risk` and no active disqualifiers. Authority remains purpose-, session- and time-bound and revocable. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Gives out: ACCEPTED — Current top-security access only within the complete owner intersection. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Must never: ACCEPTED — Grant access from either owner alone, let a copied observed state override owner truth or silently open a future Personal Mode session from step-up success. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Absent, expired, revoked, wrong-purpose or unverifiable lease, missing/incompatible Gate 1, restart, SACL downgrade or required-owner failure removes Top-security authority immediately. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: DESIGNED — C-BAI.6 — Top-security biometric lease: supplies actual current lease authority. [V10 §25.6] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Gated by: DESIGNED — C-SACL.4.2 — Gate 1 top-security qualification: its complete current decision must coexist compatibly with the live BAI lease. [V10 §25.4] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Changes: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies a separate step-up owner truth without rewriting its underlying session. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.18.1 — Step-up reference is not authority | The two actual owner truths. | References them as observations only. | Copied observed_active state creates no live authority. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-BAI.18.2 — Top-security ending and fallback | Loss of either required current owner truth. | Ends Top-security and uses the still-valid ordinary intersection. | Effective access falls to the applicable stricter state. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-BAI.21 — Owner proof across coordination boundaries | Current lease and SACL owner truth. | Requires the current owner pair for operations that need it. | Static references cannot copy live top-security authority. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-9.15 — Mode semantic indicators | Committed state and, for step-up/top-security, both owner-verified current lease and Gate 1 result. | Supplies actual current stronger-authority truth. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §15] |
| 5 · ACCEPTED | C-9.17.20 — Incomplete or incompatible top-security owners | Either missing truth or an incompatible owner pair. | Gates this place: both actual owners remain necessary. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 6 · ACCEPTED | C-9.1.4.8 — Separate lease role | The current compatible lease and Gate 1 references. | Supplies the two live, mutually compatible authorities. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-9.12.7.5 — Actual top-security lease reference | The actual BAI-owned lease. | Gates this place: both current compatible truths are required. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 8 · ACCEPTED | C-9.15.5 — Stronger-authority semantic indication | Both the actual current owner-verified lease and Gate 1 result. | Supplies verified current pair. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §15] |
| 9 · ACCEPTED | C-9.12.7 — Proposed step-up observation link | `stepup_link_id` [proposed], `mode_session_ref` [proposed], `mode_boundary_ref` [proposed], required `mode_runtime_epoch_id` [proposed], `observed_under_committed_mode_generation` [proposed], `purpose` [proposed], `observed_at` [proposed], `authority_state_event_refs` [proposed] and `observed_authority_state` [proposed]. | Supplies the complete actual BAI/SACL pair. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 10 · ACCEPTED | C-9.12.7.6 — Actual SACL Gate 1 reference | The current SACL-owned Gate 1 decision. | Gates this place: current lease and Gate 1 must agree. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 11 · ACCEPTED | C-9.14 — Separate step-up use | The actual BAI lease and current SACL Gate 1 decision. | Supplies actual mutually compatible lease and Gate 1. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |

SUB-PARTS: C-BAI.18.1 — Step-up reference is not authority; C-BAI.18.2 — Top-security ending and fallback

### C-BAI.18.1 — Step-up reference is not authority
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The proposed `personal_mode_stepup_link` as a reference/history observation of separately owned authority, never a second live authority. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Takes in: ACCEPTED — Both actual owner references and their `authority_state_event_refs`; the observation retains required `purpose` and `observed_at` and the mode's epoch/generation binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Does: ACCEPTED — Observes `requested`, `observed_active`, `observed_expired`, `observed_revoked` or `observed_refused` as `observed_authority_state`; appends observations without rewriting a second authority. The effective-access snapshot references the complete owner set, and the indicator verifies both owners. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Gives out: ACCEPTED — Historical owner references and observations; other step-up types retain their own exact accepted owner set. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Must never: ACCEPTED — Let one `authority_ref` stand for both top-security owners, grant access from copied `observed_active` or let history defeat expiry, revocation, restart, downgrade or owner failure. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — A lease without current Gate 1, or Gate 1 without a live lease, grants nothing. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-BAI.18 — Current top-security owner pair: supplies two independent current truths for reference-only observations. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9.12.7 — Proposed step-up observation link | `stepup_link_id` [proposed], `mode_session_ref` [proposed], `mode_boundary_ref` [proposed], required `mode_runtime_epoch_id` [proposed], `observed_under_committed_mode_generation` [proposed], `purpose` [proposed], `observed_at` [proposed], `authority_state_event_refs` [proposed] and `observed_authority_state` [proposed]. | Gates this place: observation grants nothing. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 2 · ACCEPTED | C-9.12.7.8 — Observed step-up state | `requested` [proposed], `observed_active` [proposed], `observed_expired` [proposed], `observed_revoked` [proposed] or `observed_refused` [proposed]. | Gates this place: live owner verification remains necessary. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |


SUB-PARTS: NONE

### C-BAI.18.2 — Top-security ending and fallback
Stamp: ACCEPTED    Source: [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The access result when separate step-up authority ends. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Takes in: ACCEPTED — Expiry, revocation, restart, SACL downgrade or required-owner failure and the still-current ordinary access facts. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Does: ACCEPTED — Falls back to the still-valid Personal Mode / SACL / privacy intersection; if mode or identity access is lost too, uses the more restrictive state. Attaching or removing step-up advances mode generation whenever effective access changes. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Gives out: ACCEPTED — Current reduced effective access without an automatic future mode opening. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Must never: ACCEPTED — Deliver output before correcting the current access state or treat unknown owner truth as success. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — Withholding Top-security whenever either required owner truth is absent or unverifiable. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §17]

TOGETHER
- Fed by: ACCEPTED — C-BAI.18 — Current top-security owner pair: determines whether both owner truths still permit use. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Gated by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): fallback requires a still-valid mode; C-SACL — Speaker Access-Control Layer (§25.4): current access remains a ceiling; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy permission remains binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9.12.7 — Proposed step-up observation link | `stepup_link_id` [proposed], `mode_session_ref` [proposed], `mode_boundary_ref` [proposed], required `mode_runtime_epoch_id` [proposed], `observed_under_committed_mode_generation` [proposed], `purpose` [proposed], `observed_at` [proposed], `authority_state_event_refs` [proposed] and `observed_authority_state` [proposed]. | Gates this place: ending defeats stale observations. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §12 / `personal_mode_stepup_link`] |
| 2 · ACCEPTED | C-9.10.14 — Crash after revocation before indicator | The committed revocation. | Supplies current revocation truth. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §10 / After step-up revocation, before the indicator updates] |
| 3 · ACCEPTED | C-9.8.2 — Safe lower-ceiling continuation | Top-security falling to recognized_ness. | Supplies actual higher-authority ending and still-valid ordinary intersection. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-9.14 — Separate step-up use | The actual BAI lease and current SACL Gate 1 decision. | Gates this place: owner ending wins. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §7B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] |


SUB-PARTS: NONE

### C-BAI.19 — Enrollment authorization producer
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — BAI's purpose-bound token, durable consumption and physical-success interfaces for initial voice enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — A dedicated trusted-phone enrollment begin action and six verified owner prerequisites, followed by the exact `voice_enrollment_ness` request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Creates its own single pending record and native prompt; issues one short-lived token on matched success; requires owner revalidation immediately before consuming; flushes the bound consumption proof before enrollment-session opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — The token or refusal, durable consumption evidence and the sole BAI-sourced biometric-success command at committed opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Let the enrollment coordinator create BAI pending state, fabricate BAI audit facts, become a second authority or interpret biometric success as identification of Ness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Failed prerequisites prevent the BAI call; changed prerequisites after issue revoke without consumption; absent or unverifiable flushed consumption proof prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests authorization for the explicit begin operation and prospective session. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: all six owner facts must hold before asking BAI and again immediately before consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the durable proof required before session opening, without becoming the session owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.19.1 — Enrollment BAI request interface | The enrollment request under BAI ownership. | Uses one pending record and returns actual pending/token or failure truth. | The coordinator cannot create parallel pending state. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-BAI.19.3 — Enrollment durable consumption proof | The bound enrollment consumption operation. | Consumes once and flushes proof before opening. | No session opens on volatile token state alone. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-BAI.19.5 — Enrollment consumed-proof crash boundary | The consumption/opening/capture boundary. | Stops honestly at the actual committed stage after crash. | No microphone starts or resumes automatically. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-BAI.19.7 — Biometric success identity limit | Device biometric acceptance on the trusted phone. | Keeps it as purpose approval rather than voice identity. | The artifact cannot identify Ness by name. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-ENROLL.15.4 — Recovery after token issue before final checks | No durable token authority. | Supplies volatile token ownership. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 6 · ACCEPTED | C-ENROLL.6.4 — Token issued process state | BAI's single-use `voice_enrollment_ness` token. | Supplies actual token issuance. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |

SUB-PARTS: C-BAI.19.1 — Enrollment BAI request interface; C-BAI.19.2 — Enrollment prerequisite revalidation; C-BAI.19.3 — Enrollment durable consumption proof; C-BAI.19.4 — Enrollment proof binding without new authority; C-BAI.19.5 — Enrollment consumed-proof crash boundary; C-BAI.19.6 — BAI-owned enrollment success observation; C-BAI.19.7 — Biometric success identity limit

### C-BAI.19.1 — Enrollment BAI request interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I3, enrollment coordinator → BAI, owned by BAI. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `{ purpose = voice_enrollment_ness, requester, operation_ref, session_ref }`, after six prerequisites are verified. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Uses BAI's one-pending-record rule; refuses a second request while one is pending; returns pending identity or refusal, followed by token reference or failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — `{ pending_id | refusal }`, then `{ token_ref | failure }`; no challenge, key or biometric datum crosses the interface. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Retry automatically, accept concurrent pending requests or expose challenge/key/biometric data. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Failure makes the pending record terminal and notifies the requester; no token survives restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: owns the single pending request and token result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: the six prerequisites must be verified before this call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.3 — Recovery with BAI pending | The fact that the pending record was in memory only. | Supplies BAI's volatile pending boundary. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.4.5.8 — Concurrent BAI-pending barrier | An enrollment request while BAI already holds a pending record. | Gates this place: its single-pending rule controls admission. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.6.3 — Biometric pending process state | BAI's single pending record and active OS prompt. | Supplies actual pending status. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-ENROLL.4.1 — Enrollment BAI request fields | Exactly `purpose = "voice_enrollment_ness"`, `requester`, `operation_ref` and `session_ref`. | Owns the response and one-pending rule. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-ENROLL.16.2 — Fresh enrollment-session requirements | A new explicit begin, fresh prerequisite checks, a new BAI pending record, a fresh token and a new session identity. | Supplies new pending and fresh token. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] |
| 6 · ACCEPTED | C-ENROLL.4.5.4 — Unmatched biometric-result barrier | An expired, absent or mismatched BAI pending/result relationship. | Supplies actual pending/result truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 7 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | Explicit trusted-phone begin, prospective operation/session identities and six live prerequisite facts. | Supplies BAI-owned pending and token responses. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 8 · ACCEPTED | C-ENROLL.4.3.4 — Bound pending-record reference | The pending identity associated with the actual matched biometric result. | Supplies the original pending identity. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |


SUB-PARTS: NONE

### C-BAI.19.2 — Enrollment prerequisite revalidation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Verification before the BAI call and owner revalidation immediately before token consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — Six owner facts: final permanent trusted-owner phone status (BAI state 4); first recovery code saved, verified, locally tested and activated; original QR and temporary pairing secret permanently inert; original setup finalized with QR path permanently closed (`bai_initial_setup_finalized`); no current medium-or-higher acoustic spoofing suspicion; confirmed Ness Person-Box. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Reads actual owners, with their current versions/event identities; the proposed `enrollment_prerequisite_snapshot` is reference evidence, not authority. Re-reads owners immediately before consumption rather than trusting the prior snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Current permission to continue only while all six still hold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Consume after any prerequisite changed, replace owner truth with the snapshot or expose private material in failure evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Changed prerequisites cause BAI revocation with `bai_token_revoked`, no consumption and no opening; enrollment records `enrollment_token_revoked_prereq_changed` and `enrollment_prerequisite_failed` with the failing prerequisite by reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current phone/recovery/QR/setup owner facts; C-SIA — Speaker Identity Assessment (§25.3): supplies acoustic-spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 disqualifier effect; C-7L — Person-Boxes (§7L): supplies confirmed Ness Person-Box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BAI.5.4 — Revoked token state: a changed prerequisite revokes the issued token without consuming it. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI.3.9.3 — Ness enrollment purpose | The six verified enrollment prerequisites. | Requires initial verification and owner revalidation before consumption. | Changed prerequisites revoke the issued token without opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-BAI.19 — Enrollment authorization producer | All six current owner prerequisites. | Requires initial verification and immediate pre-consume revalidation. | Changed prerequisites revoke without opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-BAI.19.1 — Enrollment BAI request interface | The six verified prerequisites. | Requires them before calling BAI. | Prerequisite failure prevents the call. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-BAI.19.3 — Enrollment durable consumption proof | All six owner facts immediately before consumption. | Requires their current satisfaction. | Any change prevents consumption and opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-ENROLL.4.2 — Final owner recheck and revocation | The issued token and freshly reread six prerequisite owners. | Gates this place: BAI's required revalidation boundary. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 6 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | Explicit trusted-phone begin, prospective operation/session identities and six live prerequisite facts. | Gates this place: changed prerequisites prohibit consumption. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-BAI.19.3 — Enrollment durable consumption proof
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The flushed BAI-owned `bai_token_consumed` event for `voice_enrollment_ness`, the durable consumption proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The bound explicit begin-event reference, prerequisite snapshot and owner versions, pending reference, token reference, enrollment operation and prospective session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Consumes exactly once after revalidation; flushes and verifies proof before returning and before `enrollment_session_opened` can commit. The opening is keyed to one proof bound to one operation/session. A second different proof for an opened session or one proof reused for a second session is refused and recorded. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Durable audit proof, independent of vanished BAI memory after restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Open the enrollment session without verified flushed proof or use a coordination claim as substitute authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — If proof cannot be flushed and verified, no durable authority exists and the session does not open. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: supplies the purpose-bound consumption operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: all six live owner facts must still hold immediately before consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.19.4 — Enrollment proof binding without new authority | The actual flushed BAI event. | Binds the proof directly or by an integrity-protected companion reference. | The companion never becomes another BAI authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-BAI.19.5 — Enrollment consumed-proof crash boundary | The surviving consumed-token proof. | Keeps the token spent when opening never committed. | A later attempt needs a new begin and token. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-BAI.19.6 — BAI-owned enrollment success observation | Actual durable BAI consumption referenced by session opening. | Provides BAI's success fact at the committed opening boundary. | One deterministic observation can be recorded without fabrication. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-ENROLL.4.4 — Proof-bound session-open commit | A flushed `bai_token_consumed` bound to this operation and prospective session. | Gates this place: the BAI-owned event must be flushed and verified. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-ENROLL.4.5.6 — Missing durable-proof barrier | The proposed session-open commit and its consumption reference. | Gates this place: actual flushed evidence is required. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 6 · ACCEPTED | C-ENROLL.9.5 — Declared authorization and durable-token check | `authorization_type="enrollment_declared"` and the segment's `session_id`. | Gates this place: actual durable consumption must be linked to the session. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-ENROLL.4.3.3 — Bound token reference | The BAI-owned token identity by reference. | Supplies token consumption truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 8 · ACCEPTED | C-ENROLL.6.6 — Token durably consumed state | Flushed `bai_token_consumed` and its verified integrity-protected binding. | Supplies flushed owner truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-ENROLL.4.3.10 — Bound audit schema and version | The actual audit record's schema and version identity. | Supplies the real audit record. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 10 · ACCEPTED | C-ENROLL.4.3 — Durable authorization chain and binding | Begin-event reference, snapshot and owner versions, pending reference, token reference, flushed purpose-specific consumption proof, operation/session identities and opening commit. | Supplies the actual flushed event. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 11 · ACCEPTED | C-ENROLL.4.5 — Opening duplicate barriers | The begin claim, BAI pending/result, live prerequisites, consumption proof and current session identity. | Supplies the actual proof. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 12 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | Explicit trusted-phone begin, prospective operation/session identities and six live prerequisite facts. | Supplies actual flushed proof. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 13 · ACCEPTED | C-ENROLL.4.3.8 — Bound trusted-local timestamps | The actual authorization timestamps. | Supplies BAI's actual audit times. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |

SUB-PARTS: NONE

### C-BAI.19.4 — Enrollment proof binding without new authority
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The verifiable binding between BAI's consumption event and exactly one enrollment operation/session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Proposed `enrollment_operation_id` and proposed `enrollment_session_id`, token and pending-record references, exact purpose, trusted-phone `app_session_key_ref`, prerequisite-snapshot reference, BAI trusted-local timestamps, requester identity, audit schema/version and integrity reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Binds these directly or through the append-only integrity-protected proposed `enrollment_authorization_binding`, which references the BAI event and is referenced by it or by the session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A binding verifiable after restart while the consumption fact remains BAI-owned. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Create a second BAI authority or put biometric data, challenges, private keys or raw token material into a log. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unverified binding cannot satisfy the session-open consumption-proof precondition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: supplies the BAI event being bound. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): receives the verifiable binding for its separately owned opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | Explicit trusted-phone begin, prospective operation/session identities and six live prerequisite facts. | Supplies verifiable operation/session binding. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 2 · ACCEPTED | C-ENROLL.4.3 — Durable authorization chain and binding | Begin-event reference, snapshot and owner versions, pending reference, token reference, flushed purpose-specific consumption proof, operation/session identities and opening commit. | Supplies direct or companion binding semantics. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |


SUB-PARTS: NONE

### C-BAI.19.5 — Enrollment consumed-proof crash boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Recovery after enrollment consumption and around the separate session-open/capture boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Actual durable consumed-token proof, session-open commit and capture-start owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — If proof exists without session-open commit, leaves the token spent, opens no session, starts no capture and records proposed `enrollment_aborted_before_capture`; a later attempt needs a new explicit begin and fresh token. If opening committed but capture never began, closes honestly with zero segments and `enrollment_session_closed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — The truthful stopped outcome; a later attempt uses fresh prerequisites, new pending record, fresh token and new session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently open the session, restart the microphone automatically, claim material exists without capture or infer non-start from absent BOP observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No recovery path activates capture without a current explicit session opened through the settled flow; unknown capture-start reality remains unknown, and committed observations are preserved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: supplies the spent-proof boundary before capture; C-BAI.19.3 — Enrollment durable consumption proof: supplies actual surviving consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): stops rather than silently completing a missing opening or resuming capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.6 — Spent proof without an opened session | Verified durable consumed-token proof without an opening. | Supplies actual spent-proof truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] |


SUB-PARTS: NONE

### C-BAI.19.6 — BAI-owned enrollment success observation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5C, BAI → BOP, triggered by committed enrollment-session opening that references BAI's durable consumed-token proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual session-open truth and command identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Emits `biometric:result:success` with exactly two fields, session ID and N.H trusted-local timestamp. Uses stable deterministic `capture_id` derived from session-open truth plus command identity so recovery cannot create it twice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — One BAI-sourced physical success fact passed to BOP. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Let the coordinator fabricate or become the source; include purpose, token ID, biometric data, authorization conclusions or a claim of identified Ness; duplicate the observation during recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Without actual committed opening and BAI consumption truth, supplies no fabricated success command. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: supplies BAI's actual proof referenced by opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the session-open commit must actually exist and reference the consumed proof; coordination affects timing only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: ACCEPTED — C-BOP.15.4 — Single enrollment biometric success observation: receives the one stable BAI-sourced command fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.7 — Recovery before the biometric system-command observation | Actual `enrollment_session_opened` truth referencing durable BAI proof. | As the sole source, emits `biometric:result:success` with exactly two fields (session ID and N.H trusted-local timestamp) under a stable `capture_id`, so recovery cannot create it twice. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.5.7 — Enrollment biometric-observation timing | The committed session opening referencing durable consumed-token proof. | As the sole source, emits `biometric:result:success` with exactly two fields (session ID and N.H trusted-local timestamp) under a stable `capture_id`, so recovery cannot create it twice. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |


SUB-PARTS: NONE

### C-BAI.19.7 — Biometric success identity limit
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — OS biometric success proves only acceptance of an enrolled device biometric on the permanently trusted phone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — Trusted-phone binding and the purpose-bound token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Keeps trusted-phone binding as outer bootstrap authority and the token as inner approval. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Biometric authorization evidence without an assertion of voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Identify Ness by name from biometric success, make BAI a voice-identity authority or treat enrollment provenance as confirmed voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: supplies bounded purpose approval without identity inference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.20 — Conditional evaluation-judgment proof producer
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [04/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §6] [NHD-B16EEB-D16]

ALONE
- What it is: ACCEPTED — Conditional BAI mechanics if NHD-B16EEB-D16 selects a one-time BAI artifact or the combined BAI/SACL option; the choice remains open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Takes in: ACCEPTED — The winning proposed `judgment_authorization_claim`, its attached token and the exact accepted judging purpose/scope, if such an option is selected. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Does: ACCEPTED — Uses the linked protocol: committed claim → separate BAI consumption and flushed receipt → atomic proposed E9 + proposed E16 through proposed O-APPEND. BAI rechecks at consumption; proposed O-APPEND re-verifies bound proof at commit. The SACL-only option has no BAI-consumption stage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gives out: ACCEPTED — A receipt bound to the one authorized judgment if all selected conditions hold; no option, purpose identifier or judging scope is chosen here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Must never: ACCEPTED — Describe the protected parent protocol as one atomic transaction, trust an earlier validity check, infer authority from a bare annotator name or model assistance, or select NHD-B16EEB-D16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Fails closed by: ACCEPTED — Refusing every Ness judgment until NHD-B16EEB-D16 is accepted; if a combined option is selected, failure of either proof refuses or makes the judgment indeterminate under the accepted lifecycle. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: supplies the already-defined conditional claim/receipt/commit sequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gated by: ACCEPTED — C-GOLD.1.11.17 — NHD-B16EEB-D16 authority-proof choice: an accepted choice of proof kind, purpose and scope must exist before any Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Changes: ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: supplies BAI's actual conditional consumption fact and its durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.20.1 — Judgment consume-time checks | The conditionally selected BAI judgment option. | Checks the winning token's current validity and exact purpose/scope. | Earlier checks cannot authorize consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |
| 2 · ACCEPTED | C-BAI.20.2 — Judgment durable receipt | The separate BAI receipt stage. | Consumes the winner and flushes proof before reporting success. | The later judgment commit receives durable bound evidence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |
| 3 · ACCEPTED | C-BAI.20.3 — Judgment no-receipt failure | No verified receipt for the attempted judgment consumption. | Terminates the uncertain-token attempt without new authority. | A later judgment needs a new flow and token. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: C-BAI.20.1 — Judgment consume-time checks; C-BAI.20.2 — Judgment durable receipt; C-BAI.20.3 — Judgment no-receipt failure; C-BAI.20.4 — Judgment post-receipt recovery

### C-BAI.20.1 — Judgment consume-time checks
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

ALONE
- What it is: ACCEPTED — BAI's immediate pre-consumption checks under a selected BAI judgment-proof option. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Takes in: ACCEPTED — The winning attached token and its pending-record/challenge binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Does: ACCEPTED — Requires `valid`, unexpired, unrevoked, unconsumed, purpose-matched status, and binding to the exact judgment operation or accepted judging scope, nothing wider; repeats both validity and scope checks immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gives out: ACCEPTED — Consume-time proof eligibility within the selected scope only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Must never: ACCEPTED — Trust earlier checks, consume a losing token or broaden the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Fails closed by: ACCEPTED — A second judgment using an existing receipt or a consumed, expired or revoked token is refused as proposed `judgment_refused_authority`, non-retryably and logged; BAI's delayed/duplicate result rules still apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

TOGETHER
- Fed by: ACCEPTED — C-BAI.20 — Conditional evaluation-judgment proof producer: supplies the selected-option boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: all six canonical token conditions must hold now. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.20.2 — Judgment durable receipt | All current token validity and scope checks. | Requires them immediately before consuming the winner. | Failed conditions cannot produce successful consumption authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: NONE

### C-BAI.20.2 — Judgment durable receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

ALONE
- What it is: ACCEPTED — The flushed `bai_token_consumed` receipt as conditional judgment authorization's durable commit point. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Takes in: ACCEPTED — The token attached to the winning committed claim and its exact purpose/scope binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Does: ACCEPTED — Consumes that token and commits and flushes the receipt before reporting success. Proposed E9 binds the receipt identity, integrity and consumed-for claim; the proposed claim states proceed from proposed `claimed` to proposed `consumed_pending_commit`, then proposed `judgment_committed` only after proposed O-APPEND's proposed E9 + proposed E16 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gives out: ACCEPTED — Durable proof for one judgment unless an accepted decision explicitly selects a separately defined session-scoped mechanism. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Must never: ACCEPTED — Reuse the original token as proof, report consumption before durability or treat the expected post-success `consumed` state as invalidating a committed judgment; currentness concerns ledger heads. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Fails closed by: ACCEPTED — No verified durable receipt means no committed consumption authority for the judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

TOGETHER
- Fed by: ACCEPTED — C-BAI.20 — Conditional evaluation-judgment proof producer: separates BAI's receipt stage from the claim and proposed E9 + proposed E16 transaction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gated by: ACCEPTED — C-BAI.20.1 — Judgment consume-time checks: the winning token must pass current validity and exact scope checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Changes: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: supplies the receipt identity, integrity and exact claim binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BAI.20.4 — Judgment post-receipt recovery | The actual durable judgment receipt. | Verifies the binding and completes only its named judgment. | No second consumption or redirected authority is permitted. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: NONE

### C-BAI.20.3 — Judgment no-receipt failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

ALONE
- What it is: ACCEPTED — Crash before a durable judgment receipt, or receipt-write failure within the running process. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Takes in: ACCEPTED — No verified durable consumption proof, including an uncertain in-memory consume attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Does: ACCEPTED — Ends proposed O-JUDGE as proposed `judgment_authorization_failed`, one terminal and one log; releases its claim by linked append subject to the claim's no-receipt release proofs. A later attempt needs a new flow, new token and new proposed O-JUDGE through linked supersession. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16]
- Gives out: ACCEPTED — No judgment authority from the failed attempt; the uncertain original token is terminal and vanishes on restart. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Must never: ACCEPTED — Retry, reconstruct or resurrect the token, fabricate a BAI-owned event during recovery or infer that consumption occurred from missing BAI history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Fails closed by: ACCEPTED — Refusing to proceed with the old token or record a judgment without durable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

TOGETHER
- Fed by: ACCEPTED — C-BAI.20 — Conditional evaluation-judgment proof producer: supplies the conditional consumption/recovery boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-GOLD.1.7 — Judgment-authorization claims and protected recovery: receives the no-receipt fact and applies its protected linked release rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.20.4 — Judgment post-receipt recovery
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

ALONE
- What it is: ACCEPTED — Conditional recovery once the judgment's consumption receipt is durable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Takes in: ACCEPTED — The flushed receipt and its chain, expected head, proposed E9 content identity, purpose/scope, token and integrity binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Does: ACCEPTED — Preserves the claim in proposed `consumed_pending_commit` and forward-completes exactly its named proposed E9 once through proposed O-APPEND. Unrelated ledger movement permits only a B9-admitted new proposed O-APPEND with new ID and unchanged proposed E9 key/content. A judgment-head breach records contradiction, makes the chain proposed `judgment_indeterminate` and closes the receipt-bearing claim in proposed `closed_after_breach`, linked and non-replaceable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gives out: ACCEPTED — Exact authorized completion or truthful unavailable/indeterminate proof status. An orphaned receipt whose claim is absent or mismatched is recorded and commits nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Must never: ACCEPTED — Consume again, fabricate or redirect a judgment, force stale proposed E9 through a breach, admit a replacement claim/token for a receipt-bearing breach closure or let another judgment use an orphaned receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Fails closed by: ACCEPTED — Unreadable, missing, mismatched or contradictory later proof leaves an uncommitted judgment unavailable or a committed chain in proposed `judgment_indeterminate` until verified by lookup; a receipt-bearing breach cannot be extended without a future accepted resolution policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]

TOGETHER
- Fed by: ACCEPTED — C-BAI.20.2 — Judgment durable receipt: supplies the surviving authorization proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16]
- Gated by: ACCEPTED — C-GOLD.1.7 — Judgment-authorization claims and protected recovery: retains the scope fence and forbids replacement of receipt-bearing ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BAI.21 — Owner proof across coordination boundaries
Stamp: ACCEPTED    Source: [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §F.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2]

ALONE
- What it is: ACCEPTED — BAI authority remains with the live owner or actual durable consumed-token proof across coordinator and kernel references. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §F.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2]
- Takes in: ACCEPTED — Actual owner references, verified flushed consumption receipts and current lease facts where the operation requires them. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E]
- Does: ACCEPTED — Uses the receipt as post-crash TSC authority and keeps step-up/lease truth with BAI; coordinator stages and output delivery references neither copy nor replace that truth. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E]
- Gives out: ACCEPTED — Owner-verifiable evidence or the honest absence of required authority. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2]
- Must never: ACCEPTED — Convert a coordination claim, checkpoint or copied reference into biometric authority; fabricate BAI's live blocked-consume event during recovery; treat the volatile token map as durable proof. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §F.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2]
- Fails closed by: ACCEPTED — Unverified required receipt or current lease truth cannot authorize the dependent TSC or output operation. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies actual flushed consumption proof; C-BAI.18 — Current top-security owner pair: supplies the required current lease/SACL conjunction. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K.2] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-SACL.26 — Stage checkpoints preserve owner authority: exposes BAI-owned truth without transferring authority to output checkpoints. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These continuation rows preserve the current TOGETHER relationships at their other endpoint. Earlier files are not edited. Future owners incorporate the rows when written; the register retains both exact endpoint names. Conditions and citations remain in the identified current field.

| USED BY owner | Using card | Current TOGETHER field | Exact current relationship | Disposition |
|---|---|---|---|---|
| C-TSC — Temporary Session Cache (§7E-TSC) | C-BAI — Biometric Authorization Interface (§25.6) | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): requests the exact session-promotion purpose; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests `voice_enrollment_ness`; C-BGMM — Biometric-Gated Maintenance Mode (§25.13): uses session-and-purpose-bound maintenance confirmation. [V10 §25.6] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI — Biometric Authorization Interface (§25.6) | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): requests the exact session-promotion purpose; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests `voice_enrollment_ness`; C-BGMM — Biometric-Gated Maintenance Mode (§25.13): uses session-and-purpose-bound maintenance confirmation. [V10 §25.6] | Pending endpoint placement |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-BAI — Biometric Authorization Interface (§25.6) | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): requests the exact session-promotion purpose; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests `voice_enrollment_ness`; C-BGMM — Biometric-Gated Maintenance Mode (§25.13): uses session-and-purpose-bound maintenance confirmation. [V10 §25.6] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI — Biometric Authorization Interface (§25.6) | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): fresh recognized-Ness confirmation must hold at TSC token consumption, and its relock or lost lease conditions revoke top-security authority. [V10 §25.6]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to BAI security records remains subject to privacy authorization. [MAP C-BAI] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-BAI — Biometric Authorization Interface (§25.6) | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): fresh recognized-Ness confirmation must hold at TSC token consumption, and its relock or lost lease conditions revoke top-security authority. [V10 §25.6]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to BAI security records remains subject to privacy authorization. [MAP C-BAI] | Pending endpoint placement |
| C-BOP.15.3 — Biometric system-command and security-audit separation | C-BAI — Biometric Authorization Interface (§25.6) | Changes | ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: receives only physical prompt/result facts with session identity and trusted local time. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-TSC.16.2 — Fresh recognized-Ness condition | C-BAI.3.9.2 — Exact-session TSC purpose | Gated by | DESIGNED — C-TSC.16.2 — Fresh recognized-Ness condition: current non-stale recognition for the Ness stream must hold at consumption. [V10 §25.6] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.3.9.3 — Ness enrollment purpose | Fed by | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the enrollment request under its explicit-action and prerequisite boundary. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-BAI.3.9.4 — Maintenance confirmation purpose | Fed by | DESIGNED — C-BGMM — Biometric-Gated Maintenance Mode (§25.13): requests its bounded biometric confirmation. [V10 §25.6 / Purpose Binding] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.6 — Top-security biometric lease | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies a repeatedly queried independent biometric factor, subject to current SACL access conditions. [V10 §25.6] [V10 §25.4] | Pending endpoint placement |
| C-SACL.40 — Fresh TSC recognition-confirmation interface | C-BAI.10 — Simultaneous TSC consume conditions | Fed by | ACCEPTED — C-SACL.40 — Fresh TSC recognition-confirmation interface: supplies the current confirmation and its binding. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] | Pending endpoint placement |
| C-TSC.16.1 — Purpose-bound token condition | C-BAI.10 — Simultaneous TSC consume conditions | Gated by | DESIGNED — C-TSC.16.1 — Purpose-bound token condition: requires the valid unconsumed exact-session token; C-TSC.16.2 — Fresh recognized-Ness condition: requires fresh current recognition at consumption. [V10 §25.6] | Pending endpoint placement |
| C-TSC.16.2 — Fresh recognized-Ness condition | C-BAI.10 — Simultaneous TSC consume conditions | Gated by | DESIGNED — C-TSC.16.1 — Purpose-bound token condition: requires the valid unconsumed exact-session token; C-TSC.16.2 — Fresh recognized-Ness condition: requires fresh current recognition at consumption. [V10 §25.6] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.11 — Immediate lease revocation | Fed by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies explicit relock and the applicable current access/security conditions. [V10 §25.6] [V10 §25.4] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.11.8 — Lease explicit-relock trigger | Fed by | DESIGNED — C-BAI.11 — Immediate lease revocation: establishes the relock effect; C-SACL — Speaker Access-Control Layer (§25.4): issues the explicit relock. [V10 §25.6] | Pending endpoint placement |
| C-BOP.15.3 — Biometric system-command and security-audit separation | C-BAI.13 — Physical-command and security-audit separation | Changes | ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: receives only the permitted physical-command fact. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.3 — Biometric system-command and security-audit separation | C-BAI.13.1 — Permitted biometric physical facts | Changes | ACCEPTED — C-BOP.15.3 — Biometric system-command and security-audit separation: records the physical command without security conclusions. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-BAI.13.2 — BAI security-audit ownership | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): security-record access must meet privacy and authorization rules; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization remains required for those records. [MAP C-BAI] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.13.2 — BAI security-audit ownership | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): security-record access must meet privacy and authorization rules; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization remains required for those records. [MAP C-BAI] | Pending endpoint placement |
| C-TSC.16.7 — Durable consumption receipt | C-BAI.13.2 — BAI security-audit ownership | Changes | ACCEPTED — C-TSC.16.7 — Durable consumption receipt: supplies BAI's actual committed and flushed consumption evidence. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] | Pending endpoint placement |
| C-TSC.29.1 — BAI consume boundary | C-BAI.16 — Durable TSC consumption producer | Fed by | DESIGNED — C-TSC.29.1 — BAI consume boundary: carries the C1 request and response at the existing canonical interface. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] | Pending endpoint placement |
| C-TSC.16.7 — Durable consumption receipt | C-BAI.16 — Durable TSC consumption producer | Changes | ACCEPTED — C-TSC.16.7 — Durable consumption receipt: writes the complete verified, committed and flushed consumption evidence. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] | Pending endpoint placement |
| C-TSC.16.4 — Authorization claim record | C-BAI.16.1 — Winning-claim consumption boundary | Fed by | ACCEPTED — C-BAI.16 — Durable TSC consumption producer: supplies the consumption protocol; C-TSC.16.4 — Authorization claim record: supplies the already-written session/purpose winner. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] | Pending endpoint placement |
| C-TSC.16.4 — Authorization claim record | C-BAI.16.1 — Winning-claim consumption boundary | Gated by | ACCEPTED — C-TSC.16.4 — Authorization claim record: only its winning attached token may be consumed, with safe linked closure before any replacement. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] | Pending endpoint placement |
| C-TSC.16.1 — Purpose-bound token condition | C-BAI.16.2 — Live TSC validation | Gated by | DESIGNED — C-TSC.16.1 — Purpose-bound token condition: the attached token must pass all current token checks; C-TSC.16.2 — Fresh recognized-Ness condition: supplies the required live SACL recognition. [V10 §25.6] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.1] | Pending endpoint placement |
| C-TSC.16.2 — Fresh recognized-Ness condition | C-BAI.16.2 — Live TSC validation | Gated by | DESIGNED — C-TSC.16.1 — Purpose-bound token condition: the attached token must pass all current token checks; C-TSC.16.2 — Fresh recognized-Ness condition: supplies the required live SACL recognition. [V10 §25.6] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.1] | Pending endpoint placement |
| C-TSC.16.7 — Durable consumption receipt | C-BAI.16.3 — Flushed receipt commit point | Changes | ACCEPTED — C-TSC.16.7 — Durable consumption receipt: produces the complete proof whose ten binding atoms retain their canonical ownership. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.4] | Pending endpoint placement |
| C-TSC.16.9 — Authorization crash recovery | C-BAI.16.4 — Uncertain-consumption failure | Changes | ACCEPTED — C-TSC.16.9 — Authorization crash recovery: receives the no-receipt failure boundary and preserves the waiting session. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] | Pending endpoint placement |
| C-TSC.16.7 — Durable consumption receipt | C-BAI.16.5 — Receipt-bound TSC recovery | Gated by | ACCEPTED — C-TSC.16.7 — Durable consumption receipt: exact complete binding and integrity must verify before forward completion. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] | Pending endpoint placement |
| C-TSC.16.9 — Authorization crash recovery | C-BAI.16.5 — Receipt-bound TSC recovery | Changes | ACCEPTED — C-TSC.16.9 — Authorization crash recovery: permits only the missing authorized completion or external-acknowledgment repair. [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §4.5] | Pending endpoint placement |
| C-TSC.26.20 — BAI consume-blocked event | C-BAI.16.6 — Live consume-blocked audit event | Changes | DESIGNED — C-TSC.26.20 — BAI consume-blocked event: supplies the genuine BAI event and its three canonical fields. [V10 §7E-TSC / 29. Integration Boundaries] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.17 — Personal-mode biometric opening boundary | Fed by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies the explicit opening request and its mode-operation bindings. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.17 — Personal-mode biometric opening boundary | Changes | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies one consumed opening proof, with activation still dependent on fresh SACL and explicit-action binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.17.2 — Mode proof validation before activation | Gated by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the explicit action and current mode-operation bindings must verify; C-SACL — Speaker Access-Control Layer (§25.4): a fresh check is required before activation commit. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.17.2 — Mode proof validation before activation | Gated by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the explicit action and current mode-operation bindings must verify; C-SACL — Speaker Access-Control Layer (§25.4): a fresh check is required before activation commit. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.17.3 — Consumed opening proof after crash | Changes | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): stays dry; the audit cannot restore its volatile session. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] | Pending endpoint placement |
| C-SACL.4.2 — Gate 1 top-security qualification | C-BAI.18 — Current top-security owner pair | Gated by | DESIGNED — C-SACL.4.2 — Gate 1 top-security qualification: its complete current decision must coexist compatibly with the live BAI lease. [V10 §25.4] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.18 — Current top-security owner pair | Changes | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): supplies a separate step-up owner truth without rewriting its underlying session. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-BAI.18.2 — Top-security ending and fallback | Gated by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): fallback requires a still-valid mode; C-SACL — Speaker Access-Control Layer (§25.4): current access remains a ceiling; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy permission remains binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.18.2 — Top-security ending and fallback | Gated by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): fallback requires a still-valid mode; C-SACL — Speaker Access-Control Layer (§25.4): current access remains a ceiling; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy permission remains binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-BAI.18.2 — Top-security ending and fallback | Gated by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): fallback requires a still-valid mode; C-SACL — Speaker Access-Control Layer (§25.4): current access remains a ceiling; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy permission remains binding. [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19 — Enrollment authorization producer | Fed by | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): requests authorization for the explicit begin operation and prospective session. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19 — Enrollment authorization producer | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the durable proof required before session opening, without becoming the session owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BAI.19.2 — Enrollment prerequisite revalidation | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current phone/recovery/QR/setup owner facts; C-SIA — Speaker Identity Assessment (§25.3): supplies acoustic-spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 disqualifier effect; C-7L — Person-Boxes (§7L): supplies confirmed Ness Person-Box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-BAI.19.2 — Enrollment prerequisite revalidation | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current phone/recovery/QR/setup owner facts; C-SIA — Speaker Identity Assessment (§25.3): supplies acoustic-spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 disqualifier effect; C-7L — Person-Boxes (§7L): supplies confirmed Ness Person-Box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.19.2 — Enrollment prerequisite revalidation | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current phone/recovery/QR/setup owner facts; C-SIA — Speaker Identity Assessment (§25.3): supplies acoustic-spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 disqualifier effect; C-7L — Person-Boxes (§7L): supplies confirmed Ness Person-Box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-BAI.19.2 — Enrollment prerequisite revalidation | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current phone/recovery/QR/setup owner facts; C-SIA — Speaker Identity Assessment (§25.3): supplies acoustic-spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 disqualifier effect; C-7L — Person-Boxes (§7L): supplies confirmed Ness Person-Box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.4 — Enrollment proof binding without new authority | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): receives the verifiable binding for its separately owned opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.5 — Enrollment consumed-proof crash boundary | Changes | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): stops rather than silently completing a missing opening or resuming capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Pending endpoint placement |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.6 — BAI-owned enrollment success observation | Gated by | DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the session-open commit must actually exist and reference the consumed proof; coordination affects timing only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.4 — Single enrollment biometric success observation | C-BAI.19.6 — BAI-owned enrollment success observation | Changes | ACCEPTED — C-BOP.15.4 — Single enrollment biometric success observation: receives the one stable BAI-sourced command fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-GOLD.1.6.4 — Conditional BAI artifact proof | C-BAI.20 — Conditional evaluation-judgment proof producer | Fed by | ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: supplies the already-defined conditional claim/receipt/commit sequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.11.17 — NHD-B16EEB-D16 authority-proof choice | C-BAI.20 — Conditional evaluation-judgment proof producer | Gated by | ACCEPTED — C-GOLD.1.11.17 — NHD-B16EEB-D16 authority-proof choice: an accepted choice of proof kind, purpose and scope must exist before any Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.6.4 — Conditional BAI artifact proof | C-BAI.20 — Conditional evaluation-judgment proof producer | Changes | ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: supplies BAI's actual conditional consumption fact and its durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.6.4.1 — BAI consume-time validity checks | C-BAI.20.1 — Judgment consume-time checks | Gated by | ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: all six canonical token conditions must hold now. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.6.4.3 — E9 durable receipt binding | C-BAI.20.2 — Judgment durable receipt | Changes | ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: supplies the receipt identity, integrity and exact claim binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.7 — Judgment-authorization claims and protected recovery | C-BAI.20.3 — Judgment no-receipt failure | Changes | ACCEPTED — C-GOLD.1.7 — Judgment-authorization claims and protected recovery: receives the no-receipt fact and applies its protected linked release rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-GOLD.1.7 — Judgment-authorization claims and protected recovery | C-BAI.20.4 — Judgment post-receipt recovery | Gated by | ACCEPTED — C-GOLD.1.7 — Judgment-authorization claims and protected recovery: retains the scope fence and forbids replacement of receipt-bearing ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16] | Pending endpoint placement |
| C-SACL.26 — Stage checkpoints preserve owner authority | C-BAI.21 — Owner proof across coordination boundaries | Changes | ACCEPTED — C-SACL.26 — Stage checkpoints preserve owner authority: exposes BAI-owned truth without transferring authority to output checkpoints. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BAI.4 — One-time authorization token | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): fresh SACL recognition holds at consume time. [V10 §25.6] | Reciprocal USED BY row added in CH09-d. |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-BAI — Biometric Authorization Interface (§25.6) | C-2.15.3.2 — Record identity boundary | 1 · DESIGNED | [MAP C-2] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-7B.10.8.4 — Identity and security condition | 2 · DESIGNED | [V10 §0B] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC — Temporary Session Cache (§7E-TSC) | 3 · DESIGNED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.15 — Inspection prohibition | 4 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16 — Session authorization | 5 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16.1 — Purpose-bound token condition | 6 · DESIGNED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16.5.3 — bai_token_id | 7 · ACCEPTED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16.7 — Durable consumption receipt | 8 · ACCEPTED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16.7.3 — Receipt token identity | 9 · ACCEPTED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.16.7.7 — Receipt consumption timestamp | 10 · ACCEPTED | [V10 §7E-TSC / 16. Fingerprint Authorization Through BAI and SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.26 — Security and operational records | 11 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.26.20 — BAI consume-blocked event | 12 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.26.20.1 — token_purpose | 13 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.26.20.2 — reason | 14 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.28.3 — Expired or revoked token | 15 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29 — Integration boundaries | 16 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29.1 — BAI consume boundary | 17 · DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29.1.1 — token_state | 18 · ACCEPTED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29.1.2 — purpose_binding | 19 · ACCEPTED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29.1.3 — validity | 20 · ACCEPTED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-TSC.29.1.5 — refusal_reason | 21 · ACCEPTED | [V10 §7E-TSC / 29. Integration Boundaries] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.3 — Linked protected-judgment protocol | 22 · ACCEPTED | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.4.1 — BAI consume-time validity checks | 23 · ACCEPTED | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.4.6 — BAI replay and reuse refusal | 24 · ACCEPTED | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt | 25 · ACCEPTED | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-7L.11.5 — Enrollment provisional link basis | 26 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-7P.2.6 — Strictest-rule and specialist authority boundary | 27 · ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-7Q.11.2 — Established identity and private-context boundary | 28 · ACCEPTED | [04/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md §4] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §13] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §5] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-7Q.11.8 — Outward exposure and no-signal boundary | 29 · ACCEPTED | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-BOP.15.3 — Biometric system-command and security-audit separation | 30 · ACCEPTED | [V10 §25.6 / BOP vs. Security Audit Separation] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-BOP.15.4 — Single enrollment biometric success observation | 31 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA — Speaker Identity Assessment (§25.3) | 32 · DESIGNED | [V10 §25.3] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.2.5 — Session biometric state | 33 · DESIGNED | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.4.1.1.3.7 — Device biometric state | 34 · DESIGNED | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.7.7 — Biometric-event trigger | 35 · DESIGNED | [V10 §25.3 / Assessment Update Cadence] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.11.5 — Ness training-session continuity | 36 · DESIGNED | [V10 §25.3 / Training Eligibility Rules] [V10 §25.3 / Settled Rules] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.13 — Protected raw voice and readings | 37 · DESIGNED | [V10 §25.3 / Raw Voice Data Protection] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SIA.15 — False lockout recovery | 38 · DESIGNED | [V10 §25.3 / False Lockout Recovery] [MAP C-SIA] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL — Speaker Access-Control Layer (§25.4) | 39 · DESIGNED | [V10 §25.4] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.4.2.1 — Verified biometric within timeout | 40 · DESIGNED | [V10 §25.4 / Fingerprint as One Independent Factor] [MAP C-SACL] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.5 — Independent biometric factor | 41 · DESIGNED | [V10 §25.4 / Fingerprint as One Independent Factor] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.18 — Proposed Output Delivery Coordinator | 42 · ACCEPTED | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.20.14 — Handoff required BAI lease | 43 · ACCEPTED | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.26 — Stage checkpoints preserve owner authority | 44 · ACCEPTED | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6E] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL.40 — Fresh TSC recognition-confirmation interface | 45 · ACCEPTED | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] | Existing TOGETHER relationship checked in earlier card |
| C-BAI — Biometric Authorization Interface (§25.6) | C-9 — Access/authentication model + voice I/O + phone modes (§9) | 46 · DESIGNED | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §14] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | 47 · DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-BAI — Biometric Authorization Interface (§25.6) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | 48 · DESIGNED | [V10 §25.6 / Purpose Binding] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-BAI — Biometric Authorization Interface (§25.6) | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | 49 · DESIGNED | [MAP CY-I] [V10 §25.6] | Existing TOGETHER relationship checked in earlier card |

## Source-to-card coverage added by CH09-e

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

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-BAI — Biometric Authorization Interface (§25.6) | USED BY row 73 / Takes in there |
| C-BAI — Biometric Authorization Interface (§25.6) | USED BY row 84 / Takes in there |
| C-BAI.1 — Narrow biometric-result boundary | Fails closed by |
| C-BAI.1 — Narrow biometric-result boundary | Fed by |
| C-BAI.1 — Narrow biometric-result boundary | Gated by |
| C-BAI.1 — Narrow biometric-result boundary | Changes |
| C-BAI.2 — OS biometric result | Gated by |
| C-BAI.2 — OS biometric result | Changes |
| C-BAI.2.1 — OS outcome | Gives out |
| C-BAI.2.1 — OS outcome | Fed by |
| C-BAI.2.1 — OS outcome | Gated by |
| C-BAI.2.1 — OS outcome | Changes |
| C-BAI.2.2 — OS audit error code | Gives out |
| C-BAI.2.2 — OS audit error code | Fails closed by |
| C-BAI.2.2 — OS audit error code | Fed by |
| C-BAI.2.2 — OS audit error code | Gated by |
| C-BAI.2.2 — OS audit error code | Changes |
| C-BAI.2.3 — OS lockout type | Does |
| C-BAI.2.3 — OS lockout type | Gives out |
| C-BAI.2.3 — OS lockout type | Must never |
| C-BAI.2.3 — OS lockout type | Fails closed by |
| C-BAI.2.3 — OS lockout type | Fed by |
| C-BAI.2.3 — OS lockout type | Gated by |
| C-BAI.2.3 — OS lockout type | Changes |
| C-BAI.3 — Pending authorization record | Gated by |
| C-BAI.3 — Pending authorization record | Changes |
| C-BAI.3.1 — Pending identity | Takes in |
| C-BAI.3.1 — Pending identity | Fails closed by |
| C-BAI.3.1 — Pending identity | Fed by |
| C-BAI.3.1 — Pending identity | Gated by |
| C-BAI.3.1 — Pending identity | Changes |
| C-BAI.3.2 — Pending challenge | Takes in |
| C-BAI.3.2 — Pending challenge | Gives out |
| C-BAI.3.2 — Pending challenge | Fails closed by |
| C-BAI.3.2 — Pending challenge | Fed by |
| C-BAI.3.2 — Pending challenge | Gated by |
| C-BAI.3.2 — Pending challenge | Changes |
| C-BAI.3.3 — Pending purpose | Gives out |
| C-BAI.3.3 — Pending purpose | Fed by |
| C-BAI.3.3 — Pending purpose | Gated by |
| C-BAI.3.3 — Pending purpose | Changes |
| C-BAI.3.4 — Pending requester | Gives out |
| C-BAI.3.4 — Pending requester | Fails closed by |
| C-BAI.3.4 — Pending requester | Fed by |
| C-BAI.3.4 — Pending requester | Gated by |
| C-BAI.3.4 — Pending requester | Changes |
| C-BAI.3.5 — Pending request time | Gives out |
| C-BAI.3.5 — Pending request time | Fails closed by |
| C-BAI.3.5 — Pending request time | Fed by |
| C-BAI.3.5 — Pending request time | Gated by |
| C-BAI.3.5 — Pending request time | Changes |
| C-BAI.3.6 — Pending expiry | Gives out |
| C-BAI.3.6 — Pending expiry | Fed by |
| C-BAI.3.6 — Pending expiry | Gated by |
| C-BAI.3.6 — Pending expiry | Changes |
| C-BAI.3.7 — Pending status | Gives out |
| C-BAI.3.7 — Pending status | Fed by |
| C-BAI.3.7 — Pending status | Gated by |
| C-BAI.3.7 — Pending status | Changes |
| C-BAI.3.8 — App-instance key reference | Gives out |
| C-BAI.3.8 — App-instance key reference | Fed by |
| C-BAI.3.8 — App-instance key reference | Gated by |
| C-BAI.3.8 — App-instance key reference | Changes |
| C-BAI.3.9 — Purpose vocabulary | Gated by |
| C-BAI.3.9 — Purpose vocabulary | Changes |
| C-BAI.3.9.1 — Top-security purpose | Takes in |
| C-BAI.3.9.1 — Top-security purpose | Gives out |
| C-BAI.3.9.1 — Top-security purpose | Fed by |
| C-BAI.3.9.1 — Top-security purpose | Gated by |
| C-BAI.3.9.1 — Top-security purpose | Changes |
| C-BAI.3.9.2 — Exact-session TSC purpose | Gives out |
| C-BAI.3.9.2 — Exact-session TSC purpose | Fed by |
| C-BAI.3.9.2 — Exact-session TSC purpose | Changes |
| C-BAI.3.9.3 — Ness enrollment purpose | Gives out |
| C-BAI.3.9.3 — Ness enrollment purpose | Changes |
| C-BAI.3.9.4 — Maintenance confirmation purpose | Gives out |
| C-BAI.3.9.4 — Maintenance confirmation purpose | Fails closed by |
| C-BAI.3.9.4 — Maintenance confirmation purpose | Gated by |
| C-BAI.3.9.4 — Maintenance confirmation purpose | Changes |
| C-BAI.3.9.5 — Extended purpose namespace | Gives out |
| C-BAI.3.9.5 — Extended purpose namespace | Fails closed by |
| C-BAI.3.9.5 — Extended purpose namespace | Fed by |
| C-BAI.3.9.5 — Extended purpose namespace | Gated by |
| C-BAI.3.9.5 — Extended purpose namespace | Changes |
| C-BAI.4 — One-time authorization token | Changes |
| C-BAI.4.1 — Token identity | Takes in |
| C-BAI.4.1 — Token identity | Gives out |
| C-BAI.4.1 — Token identity | Fails closed by |
| C-BAI.4.1 — Token identity | Fed by |
| C-BAI.4.1 — Token identity | Gated by |
| C-BAI.4.1 — Token identity | Changes |
| C-BAI.4.2 — Artifact authentication time | Gives out |
| C-BAI.4.2 — Artifact authentication time | Fed by |
| C-BAI.4.2 — Artifact authentication time | Gated by |
| C-BAI.4.2 — Artifact authentication time | Changes |
| C-BAI.4.3 — Artifact creation time | Gives out |
| C-BAI.4.3 — Artifact creation time | Fails closed by |
| C-BAI.4.3 — Artifact creation time | Fed by |
| C-BAI.4.3 — Artifact creation time | Gated by |
| C-BAI.4.3 — Artifact creation time | Changes |
| C-BAI.4.4 — Artifact expiry | Takes in |
| C-BAI.4.4 — Artifact expiry | Gives out |
| C-BAI.4.4 — Artifact expiry | Fed by |
| C-BAI.4.4 — Artifact expiry | Gated by |
| C-BAI.4.4 — Artifact expiry | Changes |
| C-BAI.4.5 — Token status | Gives out |
| C-BAI.4.5 — Token status | Fed by |
| C-BAI.4.5 — Token status | Gated by |
| C-BAI.4.5 — Token status | Changes |
| C-BAI.5 — One-time token lifecycle | Gated by |
| C-BAI.5 — One-time token lifecycle | Changes |
| C-BAI.5.1 — Valid token state | Gated by |
| C-BAI.5.1 — Valid token state | Changes |
| C-BAI.5.2 — Consumed token state | Gated by |
| C-BAI.5.2 — Consumed token state | Changes |
| C-BAI.5.3 — Expired token state | Gated by |
| C-BAI.5.3 — Expired token state | Changes |
| C-BAI.5.4 — Revoked token state | Gated by |
| C-BAI.5.4 — Revoked token state | Changes |
| C-BAI.6 — Top-security biometric lease | Gated by |
| C-BAI.6.1 — Lease identity | Takes in |
| C-BAI.6.1 — Lease identity | Gives out |
| C-BAI.6.1 — Lease identity | Must never |
| C-BAI.6.1 — Lease identity | Fails closed by |
| C-BAI.6.1 — Lease identity | Fed by |
| C-BAI.6.1 — Lease identity | Gated by |
| C-BAI.6.1 — Lease identity | Changes |
| C-BAI.6.2 — Lease status | Gives out |
| C-BAI.6.2 — Lease status | Fed by |
| C-BAI.6.2 — Lease status | Gated by |
| C-BAI.6.2 — Lease status | Changes |
| C-BAI.6.3 — Lease session identity | Takes in |
| C-BAI.6.3 — Lease session identity | Gives out |
| C-BAI.6.3 — Lease session identity | Fed by |
| C-BAI.6.3 — Lease session identity | Gated by |
| C-BAI.6.3 — Lease session identity | Changes |
| C-BAI.7 — Lease lifecycle | Gated by |
| C-BAI.7 — Lease lifecycle | Changes |
| C-BAI.7.1 — Active lease state | Gated by |
| C-BAI.7.1 — Active lease state | Changes |
| C-BAI.7.2 — Expired lease state | Gated by |
| C-BAI.7.2 — Expired lease state | Changes |
| C-BAI.7.3 — Revoked lease state | Gated by |
| C-BAI.7.3 — Revoked lease state | Changes |
| C-BAI.8 — Independent key purposes | Fails closed by |
| C-BAI.8 — Independent key purposes | Gated by |
| C-BAI.8 — Independent key purposes | Changes |
| C-BAI.8.1 — Manifest-signing key | Fails closed by |
| C-BAI.8.1 — Manifest-signing key | Fed by |
| C-BAI.8.1 — Manifest-signing key | Changes |
| C-BAI.8.2 — Rollback-sealing key | Fails closed by |
| C-BAI.8.2 — Rollback-sealing key | Fed by |
| C-BAI.8.2 — Rollback-sealing key | Gated by |
| C-BAI.8.2 — Rollback-sealing key | Changes |
| C-BAI.8.3 — Different keys per token purpose | Takes in |
| C-BAI.8.3 — Different keys per token purpose | Gives out |
| C-BAI.8.3 — Different keys per token purpose | Fails closed by |
| C-BAI.8.3 — Different keys per token purpose | Fed by |
| C-BAI.8.3 — Different keys per token purpose | Gated by |
| C-BAI.8.3 — Different keys per token purpose | Changes |
| C-BAI.9 — Biometric result handling | Gated by |
| C-BAI.9 — Biometric result handling | Changes |
| C-BAI.9.1 — Matched success | Changes |
| C-BAI.9.2 — Unmatched result | Gated by |
| C-BAI.9.2 — Unmatched result | Changes |
| C-BAI.9.3 — Authentication failure | Gated by |
| C-BAI.9.3 — Authentication failure | Changes |
| C-BAI.9.4 — Cancelled authentication | Gated by |
| C-BAI.9.4 — Cancelled authentication | Changes |
| C-BAI.9.5 — Authentication timeout | Gated by |
| C-BAI.9.5 — Authentication timeout | Changes |
| C-BAI.9.6 — Authentication lockout | Gated by |
| C-BAI.9.6 — Authentication lockout | Changes |
| C-BAI.9.7 — Authentication error | Gated by |
| C-BAI.9.7 — Authentication error | Changes |
| C-BAI.10 — Simultaneous TSC consume conditions | Changes |
| C-BAI.10.1 — TSC speaker-change invalidation | Gives out |
| C-BAI.10.1 — TSC speaker-change invalidation | Gated by |
| C-BAI.10.1 — TSC speaker-change invalidation | Changes |
| C-BAI.10.2 — TSC stale-assessment invalidation | Gives out |
| C-BAI.10.2 — TSC stale-assessment invalidation | Gated by |
| C-BAI.10.2 — TSC stale-assessment invalidation | Changes |
| C-BAI.10.3 — TSC spoofing invalidation | Gives out |
| C-BAI.10.3 — TSC spoofing invalidation | Gated by |
| C-BAI.10.3 — TSC spoofing invalidation | Changes |
| C-BAI.10.4 — TSC access-level invalidation | Gives out |
| C-BAI.10.4 — TSC access-level invalidation | Gated by |
| C-BAI.10.4 — TSC access-level invalidation | Changes |
| C-BAI.10.5 — TSC session-end invalidation | Gives out |
| C-BAI.10.5 — TSC session-end invalidation | Gated by |
| C-BAI.10.5 — TSC session-end invalidation | Changes |
| C-BAI.10.6 — TSC security-event invalidation | Gives out |
| C-BAI.10.6 — TSC security-event invalidation | Gated by |
| C-BAI.10.6 — TSC security-event invalidation | Changes |
| C-BAI.11 — Immediate lease revocation | Gated by |
| C-BAI.11.1 — Lease session-close trigger | Gated by |
| C-BAI.11.1 — Lease session-close trigger | Changes |
| C-BAI.11.2 — Lease certainty trigger | Gated by |
| C-BAI.11.2 — Lease certainty trigger | Changes |
| C-BAI.11.3 — Lease security-flag trigger | Gated by |
| C-BAI.11.3 — Lease security-flag trigger | Changes |
| C-BAI.11.4 — Lease anti-spoofing trigger | Gated by |
| C-BAI.11.4 — Lease anti-spoofing trigger | Changes |
| C-BAI.11.5 — Lease timeout trigger | Gated by |
| C-BAI.11.5 — Lease timeout trigger | Changes |
| C-BAI.11.6 — Lease session-break trigger | Gated by |
| C-BAI.11.6 — Lease session-break trigger | Changes |
| C-BAI.11.7 — Lease continuity trigger | Gated by |
| C-BAI.11.7 — Lease continuity trigger | Changes |
| C-BAI.11.8 — Lease explicit-relock trigger | Gated by |
| C-BAI.11.8 — Lease explicit-relock trigger | Changes |
| C-BAI.12 — Volatile BAI state | Gated by |
| C-BAI.12 — Volatile BAI state | Changes |
| C-BAI.12.1 — Current pending record | Gives out |
| C-BAI.12.1 — Current pending record | Gated by |
| C-BAI.12.1 — Current pending record | Changes |
| C-BAI.12.2 — Current active lease | Gives out |
| C-BAI.12.2 — Current active lease | Gated by |
| C-BAI.12.2 — Current active lease | Changes |
| C-BAI.12.3 — Active one-time token map | Gives out |
| C-BAI.12.3 — Active one-time token map | Gated by |
| C-BAI.12.3 — Active one-time token map | Changes |
| C-BAI.12.4 — Current lockout state | Takes in |
| C-BAI.12.4 — Current lockout state | Gives out |
| C-BAI.12.4 — Current lockout state | Fed by |
| C-BAI.12.4 — Current lockout state | Gated by |
| C-BAI.12.4 — Current lockout state | Changes |
| C-BAI.12.5 — Lockout start time | Gives out |
| C-BAI.12.5 — Lockout start time | Fed by |
| C-BAI.12.5 — Lockout start time | Gated by |
| C-BAI.12.5 — Lockout start time | Changes |
| C-BAI.12.6 — BAI session identity | Takes in |
| C-BAI.12.6 — BAI session identity | Gives out |
| C-BAI.12.6 — BAI session identity | Fed by |
| C-BAI.12.6 — BAI session identity | Gated by |
| C-BAI.12.6 — BAI session identity | Changes |
| C-BAI.12.7 — Last audit-event identity | Takes in |
| C-BAI.12.7 — Last audit-event identity | Gives out |
| C-BAI.12.7 — Last audit-event identity | Fed by |
| C-BAI.12.7 — Last audit-event identity | Gated by |
| C-BAI.12.7 — Last audit-event identity | Changes |
| C-BAI.13 — Physical-command and security-audit separation | Fed by |
| C-BAI.13 — Physical-command and security-audit separation | Gated by |
| C-BAI.14 — Restart and invalid-result failures | Gated by |
| C-BAI.14 — Restart and invalid-result failures | Changes |
| C-BAI.14.1 — Restart state clearing | Gated by |
| C-BAI.14.2 — Delayed-result rejection | Gated by |
| C-BAI.14.2 — Delayed-result rejection | Changes |
| C-BAI.14.3 — Duplicate-result rejection | Gated by |
| C-BAI.14.3 — Duplicate-result rejection | Changes |
| C-BAI.14.4 — Malformed-result rejection | Gated by |
| C-BAI.14.4 — Malformed-result rejection | Changes |
| C-BAI.15 — Protected-core biometric laws | Takes in |
| C-BAI.15 — Protected-core biometric laws | Gives out |
| C-BAI.15 — Protected-core biometric laws | Fails closed by |
| C-BAI.15 — Protected-core biometric laws | Fed by |
| C-BAI.15 — Protected-core biometric laws | Gated by |
| C-BAI.15 — Protected-core biometric laws | Changes |
| C-BAI.15.1 — No fingerprint-data handling | Takes in |
| C-BAI.15.1 — No fingerprint-data handling | Gives out |
| C-BAI.15.1 — No fingerprint-data handling | Fails closed by |
| C-BAI.15.1 — No fingerprint-data handling | Fed by |
| C-BAI.15.1 — No fingerprint-data handling | Gated by |
| C-BAI.15.1 — No fingerprint-data handling | Changes |
| C-BAI.15.2 — No cross-purpose authority | Gives out |
| C-BAI.15.2 — No cross-purpose authority | Gated by |
| C-BAI.15.2 — No cross-purpose authority | Changes |
| C-BAI.15.3 — No spent-token reuse | Gives out |
| C-BAI.15.3 — No spent-token reuse | Gated by |
| C-BAI.15.3 — No spent-token reuse | Changes |
| C-BAI.15.4 — One pending request | Gives out |
| C-BAI.15.4 — One pending request | Fed by |
| C-BAI.15.4 — One pending request | Gated by |
| C-BAI.15.4 — One pending request | Changes |
| C-BAI.15.5 — No protected-core override | Takes in |
| C-BAI.15.5 — No protected-core override | Gives out |
| C-BAI.15.5 — No protected-core override | Fails closed by |
| C-BAI.15.5 — No protected-core override | Fed by |
| C-BAI.15.5 — No protected-core override | Gated by |
| C-BAI.15.5 — No protected-core override | Changes |
| C-BAI.15.6 — No wellbeing query | Takes in |
| C-BAI.15.6 — No wellbeing query | Gives out |
| C-BAI.15.6 — No wellbeing query | Fails closed by |
| C-BAI.15.6 — No wellbeing query | Fed by |
| C-BAI.15.6 — No wellbeing query | Gated by |
| C-BAI.15.6 — No wellbeing query | Changes |
| C-BAI.16.1 — Winning-claim consumption boundary | Changes |
| C-BAI.16.2 — Live TSC validation | Changes |
| C-BAI.16.4 — Uncertain-consumption failure | Gated by |
| C-BAI.16.6 — Live consume-blocked audit event | Gated by |
| C-BAI.17.1 — Exact Personal-mode opening purpose | Gated by |
| C-BAI.17.1 — Exact Personal-mode opening purpose | Changes |
| C-BAI.17.2 — Mode proof validation before activation | Changes |
| C-BAI.17.3 — Consumed opening proof after crash | Gated by |
| C-BAI.18.1 — Step-up reference is not authority | Gated by |
| C-BAI.18.1 — Step-up reference is not authority | Changes |
| C-BAI.18.2 — Top-security ending and fallback | Changes |
| C-BAI.19.1 — Enrollment BAI request interface | Changes |
| C-BAI.19.2 — Enrollment prerequisite revalidation | Gated by |
| C-BAI.19.3 — Enrollment durable consumption proof | Changes |
| C-BAI.19.4 — Enrollment proof binding without new authority | Gated by |
| C-BAI.19.5 — Enrollment consumed-proof crash boundary | Gated by |
| C-BAI.19.7 — Biometric success identity limit | Fails closed by |
| C-BAI.19.7 — Biometric success identity limit | Gated by |
| C-BAI.19.7 — Biometric success identity limit | Changes |
| C-BAI.20.1 — Judgment consume-time checks | Changes |
| C-BAI.20.3 — Judgment no-receipt failure | Gated by |
| C-BAI.20.4 — Judgment post-receipt recovery | Changes |
| C-BAI.21 — Owner proof across coordination boundaries | Gated by |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. Each positive scan hit below is retained for its named reason.

| Card / line | Flag | Reason |
|---|---|---|
| C-BAI.1 — Narrow biometric-result boundary; line 135 | empty_together | Scope/boundary card, not an execution step. The source defines BAI's narrow role and prohibitions but no separate upstream component, gate or changed part for this boundary atom. |
| C-BAI.2.1 — OS outcome; line 181 | empty_together | OS result-value atom. The phone OS is not a Master-21 card. Non-success terminal handling and the no-auto-retry prohibition are populated; no separate gate on the outcome field is specified. |
| C-BAI.2.2 — OS audit error code; line 204 | empty_together | Audit-only string/null field, not a step. Its component-disclosure prohibition is populated; no independent field-level gate, failure procedure or changed component is sourced. |
| C-BAI.2.3 — OS lockout type; line 227 | empty_together | OS lockout-type enum atom. The source supplies temporary/permanent/null without a separate operation or component relationship. |
| C-BAI.3 — Pending authorization record; line 251 | prerequisite_review / Gated by | Pre-prompt purpose/identity binding is the record's own ordered construction, retained in Does and Must never; unmatched/expired/device-mismatch failure is populated. It is not recast as an invented external gate. |
| C-BAI.3.1 — Pending identity; line 275 | empty_together | Uuid4 pending-identity atom. Pre-prompt generation and its prohibition are explicit. OS prompting is not a separately named internal producer/gate card for this field. |
| C-BAI.3.1 — Pending identity; line 272 | prerequisite_review / Fails closed by | Uuid4 pending-identity atom. Pre-prompt generation and its prohibition are explicit. OS prompting is not a separately named internal producer/gate card for this field. |
| C-BAI.3.1 — Pending identity; line 276 | prerequisite_review / Gated by | Uuid4 pending-identity atom. Pre-prompt generation and its prohibition are explicit. OS prompting is not a separately named internal producer/gate card for this field. |
| C-BAI.3.2 — Pending challenge; line 300 | empty_together | Cryptographic nonce atom. BAI generation and BOP exclusion are populated; no separate source-defined gate or failure protocol for the nonce is invented. |
| C-BAI.3.3 — Pending purpose; line 324 | empty_together | Declared purpose-field atom. Cross-purpose prohibition and the sourced TSC failure outcome are filled; purpose matching defines token use, not an external gate on this field. |
| C-BAI.3.4 — Pending requester; line 349 | empty_together | Requester identity atom. Notification routing and security-audit/BOP separation are populated; the source names no independent field-level component gate. |
| C-BAI.3.5 — Pending request time; line 373 | empty_together | Trusted-local request timestamp atom; the clock is not a named Master-21 component. The ban on OS timestamp reliance is explicit. |
| C-BAI.3.6 — Pending expiry; line 396 | empty_together | Expiry-field atom. The formula and unmatched-result outcome are explicit; the source leaves numerical window and separate expiry-field wiring unspecified. |
| C-BAI.3.7 — Pending status; line 419 | empty_together | Pending-status field, with terminal enum unspecified by source. Terminal transition and duplicate rejection are explicit; no separate status-field gate is sourced. |
| C-BAI.3.8 — App-instance key reference; line 442 | empty_together | Hardware-backed app-key reference atom. Secure-keystore binding, OS-device-ID prohibition and mismatch refusal are populated; exact hardware implementation is not invented. |
| C-BAI.3.9.1 — Top-security purpose; line 491 | empty_together | Purpose-vocabulary atom for top-security. Lease expiry/revocation is its stated failure boundary; no independent producer/gate is assigned to the literal. |
| C-BAI.3.9.5 — Extended purpose namespace; line 586 | empty_together | Extension-purpose namespace atom, not a new authorization mechanism. Pre-prompt binding, consume matching and no cross-purpose reuse are explicit; no extra gate or purpose is derived. |
| C-BAI.4.1 — Token identity; line 636 | empty_together | Token-identity field atom. Map-key use and BOP exclusion are explicit. No primitive type or independent field-level gate is chosen. |
| C-BAI.4.2 — Artifact authentication time; line 660 | empty_together | Authentication-time field shared by both artifacts. Trusted local clock and immediate lease timeout consequence are explicit; the clock has no separate card. |
| C-BAI.4.3 — Artifact creation time; line 685 | empty_together | Artifact creation-time atom. Local-clock origin and OS timestamp prohibition are explicit; no extra creation-time gate is sourced. |
| C-BAI.4.4 — Artifact expiry; line 709 | empty_together | Artifact expiry field. Expired-token non-reuse and ended lease authority are populated. Numerical expiry settings and a separate field gate are not supplied. |
| C-BAI.4.5 — Token status; line 733 | empty_together | Token status enum atom. The requires-valid-token scan describes the consuming TSC gate, whose failure is filled; the enum field itself does not have that gate. No execution step is left without its rule link. |
| C-BAI.4.5 — Token status; line 734 | prerequisite_review / Gated by | Token status enum atom. The requires-valid-token scan describes the consuming TSC gate, whose failure is filled; the enum field itself does not have that gate. No execution step is left without its rule link. |
| C-BAI.6.1 — Lease identity; line 904 | empty_together | Lease identity atom. The source supplies only the field and artifact role, with no independent input/gate/failure wiring. |
| C-BAI.6.2 — Lease status; line 927 | empty_together | Lease status enum atom. Query-not-consume and inactive-on-expiry/revocation rules are explicit; no independent field-level gate is sourced. |
| C-BAI.6.3 — Lease session identity; line 950 | empty_together | Lease session-identity atom. Session-close revocation and the prohibition on keeping the associated lease active are filled; no invented session-identity field gate is added. |
| C-BAI.7.2 — Expired lease state; line 1022 | prerequisite_review / Gated by | The requires-valid-mode phrase belongs to fallback after expiry, not a precondition on becoming expired. Fails closed by states the fallback intersection; its actual owner gates are in C-BAI.18.2. |
| C-BAI.8.1 — Manifest-signing key; line 1093 | plain_together / Gated by | The plain gate is the source's own authorized-manifest prerequisite; the cited BAI section names no separate authorizing card for this key use. No additional signing enforcement mechanism is invented. |
| C-BAI.8.2 — Rollback-sealing key; line 1118 | empty_together | Key-role atom, not an execution step. The signing/sealing separation and non-export/logging prohibitions are populated; separate key-management mechanics are unspecified. |
| C-BAI.8.3 — Different keys per token purpose; line 1144 | empty_together | Restored separation law only. FR-0003 supplies different keys per purpose but no enforcement API, lifecycle or extra gate. Every DECIDED line retains the deciding record. |
| C-BAI.10.2 — TSC stale-assessment invalidation; line 1410 | prerequisite_review / Gated by | Freshness is the named rule card's consume condition; this child describes the stale-assessment invalidation and is linked to that rule. No-consumption/no-promotion failure is filled; no second gate is invented. |
| C-BAI.12.4 — Current lockout state; line 1832 | empty_together | Volatile lockout enum atom. Reauthentication is a restart consequence, already in Fails closed by, not an external prerequisite on storing the lockout label. |
| C-BAI.12.4 — Current lockout state; line 1833 | prerequisite_review / Gated by | Volatile lockout enum atom. Reauthentication is a restart consequence, already in Fails closed by, not an external prerequisite on storing the lockout label. |
| C-BAI.12.5 — Lockout start time; line 1855 | empty_together | Timestamp/null state atom. Volatility and local clock are explicit; no independent lockout-time operation or failure procedure is supplied. |
| C-BAI.12.6 — BAI session identity; line 1878 | empty_together | Volatile session-identity field atom. Its no-persistence prohibition is explicit; separate field-level gates and failure events are not stated. |
| C-BAI.12.7 — Last audit-event identity; line 1901 | empty_together | Volatile last-audit-reference atom. Source supplies the named field and no-persistence rule, not a separate authority or operational step. |
| C-BAI.14 — Restart and invalid-result failures; line 1997 | prerequisite_review / Gated by | Requires-reauthentication text is the result of restart, not a gate that could prevent safe state clearing. Does, Must never and Fails closed by all carry the source's failure outcomes. |
| C-BAI.14.1 — Restart state clearing; line 2023 | prerequisite_review / Gated by | New biometric authentication gates future authority, not execution of restart clearing. The card has its parent-rule link and the actual clear/re-authenticate outcome; no external gate on clearing is invented. |
| C-BAI.15 — Protected-core biometric laws; line 2114 | empty_together | Aggregate protected-law card, not a procedural step. All six prohibitions are explicit; concrete failure classes retain their source-defined owners and no generic enforcement mechanism is fabricated. |
| C-BAI.15.1 — No fingerprint-data handling; line 2137 | empty_together | Absolute data-boundary law. It states every prohibited fingerprint-data action; the source does not provide a separate runtime gate or failure event for this atom. |
| C-BAI.15.4 — One pending request; line 2206 | empty_together | Single-pending invariant. The actual enrollment concurrent-request refusal is filled; no separate arbitration component is invented. |
| C-BAI.15.5 — No protected-core override; line 2229 | empty_together | Interface prohibition, not a step. No override API exists in the source, so the card does not invent a gate or an override-failure mechanism. |
| C-BAI.15.6 — No wellbeing query; line 2252 | empty_together | Separation law forbidding wellbeing queries. There is no sourced wellbeing input edge to add and no independent execution step. |
| C-BAI.16.4 — Uncertain-consumption failure; line 2374 | prerequisite_review / Gated by | The new-flow requirement concerns a later attempt after no-receipt failure. Does/Gives out/Fails closed by preserve the original token's terminality, unchanged waiting session and required linked closure; no gate on failing closed is invented. |
| C-BAI.17.3 — Consumed opening proof after crash; line 2523 | prerequisite_review / Gated by | A new explicit action/token is required for a later opening attempt, not for stopping at dry after crash. The failure consequence is explicit and the card links to its opening rule and mode owner. |
| C-BAI.19.2 — Enrollment prerequisite revalidation; line 2692 | prerequisite_review / Gated by | All-six validation defines this gate card's own operation. Actual fact owners are named under Fed by and changed-prerequisite revoke/no-open is explicit. Those inner conditions are not duplicated as a gate on the gate. |
| C-BAI.21 — Owner proof across coordination boundaries; line 2969 | prerequisite_review / Gated by | Required-receipt/lease verification defines the dependent operation boundary, with explicit no-authority failure and named producer links. The source does not authorize a second coordinator gate or authority owner. |

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

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Complete §25.6; earlier V10 whole-read credit inherited, not repeated. Earlier consumer citations checked through the frozen cards and canonical source scopes. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Complete C-BAI entry and complete CY-I entry. No current whole-file credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Complete embedded §6 BAI, lines 1206–1396. No current whole-file credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Complete §4 including §§4.1–4.5; §7 introduction and full C1 interface. Earlier whole-read credit inherited; no claim to reread the complete package here. | `f722ac9599c8c88bb019220764266985aac2fe820068e20f5368dbcc9c229ef8` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole file reread for accepted scope and conditional formal closure. | `8fd19489e40f66105eb657fdbceeb320091493da2ff25c917964e11454dedf64` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Complete §5B, §6, §12 record 7, §14, §17 and §18. Other mode records remain CH09-i; no whole-file credit. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole file reread for acceptance and exact guarantees. | `663d0aa2b4cb8ee32eea1a4c70e863176c2b9fd40fb704f0c210c0190e269b0d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Complete §§4–6 including 6A–6D; complete §18; §19 introduction and I1–I10 in full; complete §§22–24; §17 identity table. Remaining enrollment sections belong to CH09-h; no whole-file credit. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole file reread, including all three frozen wording notes and conditional formal closure. | `df028286c89b7c0a4bea3bb1403d910b11f993bac010d03320f55eeec71d636a` |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Complete §§7.12 and 7.13; proposal-qualification headings and residual note checked. No new whole-file credit; canonical Gold ownership retained. | `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Complete §§5–6 for accepted architecture while decision choices remain open. No current whole-file credit. | `298de053269f4a9e93e97dfd994d33b0b879d71af636b169769264e7183d9d4c` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Lines 1–194, including complete §4 Group 11 and §5; exact §6 FR-0003 row. No whole-file credit from the partial appendix. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md` | Whole file read after authorized retrieval under FR-0003. Only §3D's restored key-separation text is eligible for behavior; remaining archive text excluded. | `e226fd243ca3a19f8e3c148925a954aad0006837e85cf427ce885da417888c31` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Earlier whole-file reading in CH09-d retained; §6E and §13 owner-lease boundaries reused, with topic hits in §11. No claim of whole-file rereading. | `4edaaadc57854b711e7f750ed897e6f4a6eaa0c0ae3734b4614167e6c58afe48` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Full individual owner rows §F.2 R31, §K.2 TSC and §T I8 inspected. Complete kernel reading remains CH10-b; no whole-file credit. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Complete Paths 3, 5, 6 and 7 and §§6–8. Other paths and full-file read remain pending. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Search-discovery scope only this piece; whole-file credit from CH09-d inherited without claiming a reread. | `d62ec6e4d61495147729241331733f81982792440148f624551fe64d9346fa44` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Complete §4.1–4.4; no whole-file credit. | `41e1f67d635a0e07a73ad572e8931bceaffd3cf6f44d88c3eaea9872818d339b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Acceptance-scope discovery hit only; no new whole-file credit. | `2fd9ba8e148533d03eb72a7fec69450717b243542ce0d44b0c5073ffa63458df` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Complete §9.1 specialist/base-authority classification; no current whole-file credit. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Complete §§13–14; §9 and other matches as source-discovery hits only. No current whole-file credit. | `46cf463389ea339bb3a908177dda8d1548095e21da6abebcd2efeb6a8a54c0ff` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Discovery hits in §§6–7; no current whole-file credit. | `3ef919f87c1dc7986a3fcaf30c8b365aa9b93e507648e679ab03825b9b534118` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Complete §15; no current whole-file credit. | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Complete §31; source-discovery match in §3. No current whole-file credit. | `1386091a0977ac79588f22a9f85213579203637e493dbb2d75be3d893326aa28` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Source-list discovery hit in §1 only; not a new BAI behavioral source. | `3deacafbd7fb840404d59f05b0f314199467889735dcb9f6243f7ef14078d6f5` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Dependency discovery hit in §7 only; no current whole-file credit. | `6179207c8d472ed81df208ceede832976f209e88e443ed7121a428d07a8b1a3d` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Navigation search hits only; no behavior taken from the index. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Older navigation search hit, excluded as a behavioral source. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Older navigation search hit, excluded as a behavioral source. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Older navigation search hit, excluded as a behavioral source. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Search-discovery hits only. No behavior used and no full or Stage-2 reading credit claimed in this piece; Appendix B retains sole ledger use. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |

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

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

50 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
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

§1.3 no history/actions/roles/workflow in this chapter: PASS — All 119 behavior cards and 277 USED BY rows checked; writer-workflow scan 0. Runtime explicit actions, operation names and proposed design names retain their source meanings. Delivery metadata remains outside the behavior boundary.

§1.4 every gap written as NOT DECIDED: PASS — All 307 empty field lines and 2 empty USED BY cells are registered, with no filled line left in the register and no mixed populated/NOT DECIDED field. Unchosen settings, unknown field encodings and the open NHD-B16EEB-D16 choice are not derived.

§1.5 conflicts marked, none resolved: PASS — The header and C-BAI.6 Does retain the differing lease-reuse wording while preserving V10's repeated-query/never-consume rule. Both B-INT-5 opening-purpose placeholder spellings remain visible. Distinct TSC, Personal-mode and enrollment recovery rules keep their own scopes.

§3 exactly one stamp per line: PASS — All 1,079 field lines and 277 individual use rows checked against source and target status. BUILT lines: 0. All 6 DECIDED-2026-09-25 lines cite the deciding buckets record; the authorized restored archive supplies only FR-0003.

§4 every behavior line cited in the exact format: PASS — All 97 unique citation headings resolve; source assertions were compared within their declared scopes. All 31 READ-record source files match the pinned Git blob identities and byte sizes as well as their listed full SHA-256 values. V10's unnumbered token/lease headings remain inside the logical numbered §25.6 scope.

§5.4 one name per thing: PASS — Official names checked against CH00, earlier canonical cards and the 119 current cards. No duplicate current ID; existing TSC, BOP and Gold field/protocol IDs remain canonical. Proposed record/operation names retain their qualifier; frozen official card names are not renamed.

§6 all template fields present, in order, for every part: PASS — 119 complete cards; 1,079 field lines. The complete misfiled-box review covered those fields and all 277 use rows, including 357 restriction/failure/gate slots represented by 359 lines. Each of the 47 positive review flags has a named disposition: 33 empty-TOGETHER atoms/laws, 13 prerequisite-language cases and 1 genuine plain prerequisite, across 43 cards. No unlinked execution-step exception is hidden among them.

§6.3 reciprocity within this chapter: PASS — All 127 internal relationships have matching current USED BY rows. The 60 outgoing relationships and 49 of the 150 external uses have 109 explicit continuations naming both endpoints; the other 101 external uses are answered by the using cards' own TOGETHER lines. All 47 incoming earlier fields across 45 distinct cards have current root use rows; the two same-place pairs are consolidated without grouping different places. Every use row names one part and at most one path; CY-I is a separate place row. Future endpoint placement remains explicit rather than editing frozen pieces.

§6.4 every decided detail written in, no citation used in place of content: PASS — The 32 source-placement rows account for the covered source scopes and named later owners; all 121 selected source-name literals are present. OS, pending, token, lease and BAI-state schemas are explicit, with shared field ownership identified. Lifecycles, outcomes, six TSC recognition invalidators, eight lease triggers, four restart/invalid-result classes, six core laws, key separation and consumer proof/recovery boundaries are written in. Full mode/enrollment records and full kernel mechanics remain expressly assigned to their later pieces.

§6.5 sub-parts recursed to the bottom: PASS — Record fields and lifecycle/result/trigger atoms have cards or their already-canonical shared field cards; no subpart list includes itself or another owner's card. The root lists its 21 own immediate subparts. Existing TSC receipt/C1 fields, BOP physical-event fields and Gold condition/claim atoms retain their earlier decomposition without duplicate ownership.

§9 coverage matrix rows added for every file used: PASS — Cumulative coverage contains 146 pinned file paths, including the newly authorized archive file; missing paths: 0. All 31 current READ fingerprints and all 50 preceding chapter fingerprints are listed and checked. Fifty inherited whole-file reading obligations remain explicitly open; search and bounded reads do not close them. The ledger contributes no behavior.

§10.11 no recommendation, no sentence addressed to Ness: PASS — The complete behavior body and use tables contain no recommendation or writer-to-user instruction. Formula, wording, workflow and structural/reciprocal errors: 0 each. The full header has all four labels and two trailing spaces on each label line.

Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` (reread); `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (reread); `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (reread); `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md` (new authorized archive whole read; only the restored FR-0003 text used). Other source scopes and their full fingerprints appear in READ RECORD. The cloned contract §§5–11 and lessons §§1–11 were reopened before this piece; contract §11.3 was reopened after writing for these checks.
