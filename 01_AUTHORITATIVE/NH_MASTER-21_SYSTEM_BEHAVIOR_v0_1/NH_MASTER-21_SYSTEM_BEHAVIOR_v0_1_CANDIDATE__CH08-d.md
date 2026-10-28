# Chapter 8-d — Group F: C-BOP

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece owns physical behavioral-observation capture: the full v1 event and payload contracts, stable identity/quality/recovery, the accepted bounded acoustic-note amendment, single Catalog entry, bounded imported-reaction linking, and BOP’s enrollment/biometric interfaces. OOP enforcement and outcome observation remain CH08-e; affirmation CH08-f; full adaptation CH08-g. Security and complete enrollment remain CH09, side-path assembly CH11 and registers CH12. Accepted A15 policy status does not activate a schema or select empirical values. Earlier historical pending wording is retained as such; proposed identifiers remain proposed.

[SOURCE CONFLICT] The Companion’s BOP Third-Party Flag paragraph applies pre-output review without the later purpose distinction. V10 §25.1 expressly assigns internal BOP retrieval/analysis/identity assessment to internal-use authorization, and visible surfacing/export/sharing/notifications to visible-output eligibility and pre-output review. V10 governs; the older unqualified wording is not used to make all internal processing a visible-output operation.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-BOP — Behavioral Observation Processing (§25.1/§26)
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The source-classification and capture-normalization responsibility that produces typed raw observation roots from directly measurable authorized-session events. [V10 §25.1]
- Takes in: DESIGNED — Available authorized voice, confirmed sent text, interface and session events, and explicitly authorized imported content. [V10 §25.1]
- Does: DESIGNED — Records what physically happened, under the enrichment boundary, and sends typed roots through the single Catalog path; interpretation belongs to the Meaning Engine. [V10 §25.1]
- Gives out: DESIGNED — Typed roots in shared memory and honest capture/failure records; no BOP-owned store or model. [V10 §25.1]
- Must never: DESIGNED — Interpret, conclude, classify meaning, maintain patterns or a model of Ness, observe unfinished typing or record unauthorized sources. [V10 §25.1]
- Fails closed by: DESIGNED — Records capture failures and crash gaps honestly without reconstructing missed observations. [V10 §25.1]

TOGETHER
- Fed by: DESIGNED — C-BOP.1 — Authorized physical-observation boundary: authorization; C-BOP.2 — BOP v1 controlled event vocabulary: event vocabulary; C-BOP.3 — Seven-field BOP root bindings: seven root bindings; C-BOP.4 — bop_payload: payload; C-BOP.5 — Corrected BOP capture_id: capture identity; C-BOP.6 — observation_quality: quality; C-BOP.7 — third_party_flag: third-party flags; C-BOP.8 — One observation root per simultaneous signal channel: simultaneous channels; C-BOP.9 — connection_anchors and later reconnection: reconnection; C-BOP.10 — Absolute DUMB and text non-inspection boundary: DUMB boundary; C-BOP.11 — Capture failure and idempotent recovery: failures; C-BOP.16 — Shared observation logging and protected access: logging. [V10 §25.1] [MAP C-BOP]
- Fed by: ACCEPTED — C-BOP.12 — Optional acoustic_condition_notes amendment: accepted optional acoustic notes; C-BOP.13 — Accepted single-path observation ingestion: single-path mechanics; C-BOP.14 — Bounded imported-voice reaction window: bounded imported-reaction link; C-BOP.15 — Enrollment and biometric observation interfaces: enrollment/capture-owner interface. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusions and exact-purpose internal/visible authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): capture/ingest gate and held-material boundary. [V10 §25.1] [V10 §7E]
- Changes: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): typed captures enter the existing Catalog; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): observations become evidence for separate interpretation. [V10 §25.1]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-LEARN — Personal Learning and Adaptation (§26, cross-cutting) | Raw behavioral observations in shared memory. | Uses their separate Meaning Engine readings in the continuous learning loop. | Capture itself creates no behavioral rule. | [V10 §26.4] |
| 2 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Authorized typed observation captures. | Routes them through its single Catalog entry and accepted writer. | No second root-writing path is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC) | References to observations already held in Catalog pre-ingest. | Links them without calling BOP. | Pending fingerprint authorization still blocks promotion. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 4 · DESIGNED | C-TSC.9 — BOP and SIA links | The existing preingest observation identity. | Maintains the structural event link. | No new capture or root copy is created. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 5 · DESIGNED | C-TSC.13.1 — Close observation | The actual session-close observation. | Preserves it with the close/seal facts. | Physical close remains distinct from content promotion. | [V10 §7E-TSC / 13. Normal Session Close and Sealing] |
| 6 · DESIGNED | C-SIA.10 — Natural voice variation | Readings from BOP roots across time, room, device position and state. | Supplies observation roots across varied conditions. | Nothing in this card. | [V10 §25.3 / Natural Voice Variation] |
| 7 · DESIGNED | C-SIA.1 — Identity-assessment scope | BOP roots. | Supplies the observation roots assessed here. | Nothing in this card. | [V10 §25.3 / What SIA Is and Is Not] |
| 8 · ACCEPTED | C-ENROLL.9 — Initial-corpus eligibility gate | Reading references, root provenance and actual owner facts for each immutable segment identity [proposed]. | Supplies completeness and physical provenance. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 9 · DESIGNED | C-SIA.11 — Ordinary voice-training eligibility | Session authorization. | Supplies what this place relies on: acoustic roots whose eligibility is assessed. | Nothing in this card. | [V10 §25.3 / Training Eligibility Rules] |
| 10 · DESIGNED | C-9.2 — Voice input and output pipeline | Microphone input and material intended for spoken output. | Takes this place's change: supplies actual authorized observations and actual interruption facts. | Supplies actual authorized observations and actual interruption facts. | [MAP C-9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 11 · DESIGNED | C-SIA.8 — Per-stream diarization | Detected voices, including overlapping and interrupted speech. | Supplies voice observation roots. | Nothing in this card. | [V10 §25.3 / What SIA Is and Is Not] |
| 12 · DESIGNED | C-SIA — Speaker Identity Assessment (§25.3) | BOP roots, Person-Box-linked profile readings and the current session's stream, conversational and biometric evidence. | Supplies physical observation roots. | Nothing in this card. | [V10 §25.3] [MAP C-SIA] |

SUB-PARTS: C-BOP.1 — Authorized physical-observation boundary; C-BOP.2 — BOP v1 controlled event vocabulary; C-BOP.3 — Seven-field BOP root bindings; C-BOP.4 — bop_payload; C-BOP.5 — Corrected BOP capture_id; C-BOP.6 — observation_quality; C-BOP.7 — third_party_flag; C-BOP.8 — One observation root per simultaneous signal channel; C-BOP.9 — connection_anchors and later reconnection; C-BOP.10 — Absolute DUMB and text non-inspection boundary; C-BOP.11 — Capture failure and idempotent recovery; C-BOP.12 — Optional acoustic_condition_notes amendment; C-BOP.13 — Accepted single-path observation ingestion; C-BOP.14 — Bounded imported-voice reaction window; C-BOP.15 — Enrollment and biometric observation interfaces; C-BOP.16 — Shared observation logging and protected access

### C-BOP.1 — Authorized physical-observation boundary
Stamp: DESIGNED    Source: [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: DESIGNED — The rule that an observation describes a directly physically measurable event in a session explicitly opened by Ness. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: DESIGNED — A permitted signal and its actual session/import authorization. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: DESIGNED — Uses the enrichment test: physical occurrence qualifies; an explanation of meaning does not. During an authorized session all available authorized signals may be recorded. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: DESIGNED — Authorized raw observations only. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: DESIGNED — Observe unfinished typing, observe an unauthorized source or turn permission to record into permission to interpret. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: DESIGNED — Unauthorized sources are refused and recorded. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-BOP.1.1 — Authorized-session all-signal rule: the accepted session authorization rule. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Fed by: DESIGNED — C-BOP.1.2 — Authorized live-voice signals: live voice; C-BOP.1.3 — Confirmed-sent-text source: confirmed sent text; C-BOP.1.4 — Authorized session-state source: session events; C-BOP.1.5 — Explicitly authorized imported source: authorized imports. [V10 §25.1]
- Gated by: DESIGNED — C-7E.1.1 — Raw-capture gate: actual raw-capture gate; C-7Q.4 — Two-layer capture exclusion: capture-exclusion owner. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The actual session/source authorization. | Captures physical events only. | No new capture source is created. | [V10 §25.1] |

SUB-PARTS: C-BOP.1.1 — Authorized-session all-signal rule; C-BOP.1.2 — Authorized live-voice signals; C-BOP.1.3 — Confirmed-sent-text source; C-BOP.1.4 — Authorized session-state source; C-BOP.1.5 — Explicitly authorized imported source

### C-BOP.1.1 — Authorized-session all-signal rule
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]

ALONE
- What it is: ACCEPTED — A session explicitly opened by Ness authorizes its available authorized behavioral signals. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Takes in: ACCEPTED — The opened session and otherwise permitted signals. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Does: ACCEPTED — Requires no separate prompt for each silence, interruption, timing pattern, voice measurement or other authorized signal; no extra signal-category exception is adopted. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Gives out: ACCEPTED — Session-bounded observation authority. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Must never: ACCEPTED — Capture outside the authorized session, bypass privacy, create meaning labels or invent a current per-signal exception. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Fails closed by: ACCEPTED — Signals outside the authorized scope remain unobserved. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy still governs capture and use. [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | The authorized opened session. | Applies the all-authorized-signal rule inside it. | A later special category exception would require a new decision. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] |
| 2 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The authorized-session observation basis. | Keeps reaction capture inside that authorization. | Linking does not authorize a new source. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-OOP.9 — Existing session and imported-reaction interfaces | The actual opened authorized session or exact imported item’s valid reaction window. | Supplies accepted A10 session rule. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-LEARN.6.1 — All authorized signals across the thirteen areas | An explicitly opened authorized Ness session and its available authorized behavioral signals. | Supplies canonical accepted session authorization rule. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-BOP.1.2 — Authorized live-voice signals
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Live voice during an active authorized session. [V10 §25.1]
- Takes in: DESIGNED — The available permitted live physical signal. [V10 §25.1]
- Does: DESIGNED — Admits raw physical observations for BOP capture. [V10 §25.1]
- Gives out: DESIGNED — Voice observation candidates. [V10 §25.1]
- Must never: DESIGNED — Admit unauthorized background audio. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | The authorized live-voice signal. | Checks it as a permitted source. | Only physical events enter capture. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.1.3 — Confirmed-sent-text source
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Confirmed sent text during an active authorized session. [V10 §25.1]
- Takes in: DESIGNED — The actually sent message and its raw timing/count facts. [V10 §25.1]
- Does: DESIGNED — Observes only after confirmed sending. [V10 §25.1]
- Gives out: DESIGNED — Sent-message observations. [V10 §25.1]
- Must never: DESIGNED — Inspect unfinished typing under any circumstances. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | The confirmed sent message. | Uses its raw observable facts. | Unsent composition is never observed. | [V10 §25.1] |
| 2 · DESIGNED | C-OOP.2.2 — Confirmed-sent-text outcomes | The actually sent response in the function’s observation context. | Supplies confirmed-sent-only observation boundary. | Nothing in this card. | [V10 §26.6] |

SUB-PARTS: NONE

### C-BOP.1.4 — Authorized session-state source
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Session-level state events from the authorized session. [V10 §25.1]
- Takes in: DESIGNED — Actual session/function state occurrences. [V10 §25.1]
- Does: DESIGNED — Records their physical occurrence under the controlled vocabulary. [V10 §25.1]
- Gives out: DESIGNED — Session-state observations. [V10 §25.1]
- Must never: DESIGNED — Infer a state event from meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | The actual session-state event. | Captures the observed transition. | No interpretation is added. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.1.5 — Explicitly authorized imported source
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Authorized content explicitly imported by Ness. [V10 §25.1]
- Takes in: DESIGNED — The actual authorized import and its physical signals. [V10 §25.1]
- Does: DESIGNED — Admits permitted import observations under source authorization. [V10 §25.1]
- Gives out: DESIGNED — Authorized imported observations. [V10 §25.1]
- Must never: DESIGNED — Treat an unrelated or unauthorized source as imported permission. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | The explicitly authorized imported content. | Keeps capture within that source. | Import permission creates no meaning claim. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2 — BOP v1 controlled event vocabulary
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical-only v1 event vocabulary, extended only through a registered extended type. [V10 §25.1]
- Takes in: DESIGNED — The directly measured event class. [V10 §25.1]
- Does: DESIGNED — Uses the exact voice, text, command, session, import or extended value. [V10 §25.1]
- Gives out: DESIGNED — A controlled event_type with only its permitted raw facts. [V10 §25.1]
- Must never: DESIGNED — Use a communicative-function label or interpret ordinary language as a system command. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.1 — voice_onset: voice_onset; C-BOP.2.2 — voice_offset: voice_offset; C-BOP.2.3 — silence_interval: silence_interval; C-BOP.2.4 — non_word_sound: non_word_sound; C-BOP.2.5 — voice_overlap: voice_overlap; C-BOP.2.6 — voice_interrupt_of_nh: voice_interrupt_of_nh; C-BOP.2.7 — pitch_measurement: pitch_measurement; C-BOP.2.8 — amplitude_measurement: amplitude_measurement; C-BOP.2.9 — text_message_sent: text_message_sent; C-BOP.2.10 — text_response_timing: text_response_timing; C-BOP.2.11 — no_response_session: no_response_session; C-BOP.2.12 — system_command: system_command; C-BOP.2.13 — session_opened: session_opened; C-BOP.2.14 — session_closed: session_closed; C-BOP.2.15 — session_interrupted: session_interrupted; C-BOP.2.16 — function_started: function_started; C-BOP.2.17 — function_completed: function_completed; C-BOP.2.18 — function_interrupted: function_interrupted; C-BOP.2.19 — capture_failure: capture_failure; C-BOP.2.20 — import_authorized: import_authorized; C-BOP.2.21 — import_processed: import_processed; C-BOP.2.22 — extended: extended. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The exact physical event type. | Classifies the capture without meaning. | Event vocabulary remains explicit. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.4.11 — signal_measurements | The exact physical event vocabulary and fields. | Uses the appropriate event type and raw structure. | No interpretation is added. | [V10 §25.1] |
| 3 · DESIGNED | C-BOP.4.2 — BOP event_type | The exact physical event vocabulary and fields. | Uses the appropriate event type and raw structure. | No interpretation is added. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.1 — voice_onset; C-BOP.2.2 — voice_offset; C-BOP.2.3 — silence_interval; C-BOP.2.4 — non_word_sound; C-BOP.2.5 — voice_overlap; C-BOP.2.6 — voice_interrupt_of_nh; C-BOP.2.7 — pitch_measurement; C-BOP.2.8 — amplitude_measurement; C-BOP.2.9 — text_message_sent; C-BOP.2.10 — text_response_timing; C-BOP.2.11 — no_response_session; C-BOP.2.12 — system_command; C-BOP.2.13 — session_opened; C-BOP.2.14 — session_closed; C-BOP.2.15 — session_interrupted; C-BOP.2.16 — function_started; C-BOP.2.17 — function_completed; C-BOP.2.18 — function_interrupted; C-BOP.2.19 — capture_failure; C-BOP.2.20 — import_authorized; C-BOP.2.21 — import_processed; C-BOP.2.22 — extended

### C-BOP.2.1 — voice_onset
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A vocalization began. [V10 §25.1]
- Takes in: DESIGNED — The physical voice onset. [V10 §25.1]
- Does: DESIGNED — Records the beginning; role identifies whose voice under its actual attribution standing. [V10 §25.1]
- Gives out: DESIGNED — voice_onset. [V10 §25.1]
- Must never: DESIGNED — Infer independently confirmed identity from a role declaration. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The vocalization beginning. | Uses voice_onset. | The boundary stays physical. | [V10 §25.1] |
| 2 · DESIGNED | C-OOP.2.1 — Post-output voice behavior | The actual authorized physical voice events. | Supplies `voice_onset`. | Nothing in this card. | [V10 §26.6] |
| 3 · DESIGNED | C-SIA.3.2 — Stream onset reference | The BOP root ID of the `voice_onset` that opened this stream. | Supplies the opening physical observation root ID. | Nothing in this card. | [V10 §25.3 / Voice Stream Record] |
| 4 · DESIGNED | C-SIA.7.1 — Voice-onset assessment trigger | A voice onset. | Supplies the physical onset event. | Nothing in this card. | [V10 §25.3 / Voice Stream Record] [V10 §25.3 / Assessment Update Cadence] |

SUB-PARTS: NONE

### C-BOP.2.2 — voice_offset
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A vocalization ended. [V10 §25.1]
- Takes in: DESIGNED — The physical voice ending. [V10 §25.1]
- Does: DESIGNED — Records that endpoint. [V10 §25.1]
- Gives out: DESIGNED — voice_offset. [V10 §25.1]
- Must never: DESIGNED — Infer why speech ended. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The vocalization ending. | Uses voice_offset. | No meaning attaches to the endpoint. | [V10 §25.1] |
| 2 · DESIGNED | C-OOP.2.1 — Post-output voice behavior | The actual authorized physical voice events. | Supplies `voice_offset`. | Nothing in this card. | [V10 §26.6] |

SUB-PARTS: NONE

### C-BOP.2.3 — silence_interval
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A silence interval measured by duration alone. [V10 §25.1]
- Takes in: DESIGNED — The observed silent duration. [V10 §25.1]
- Does: DESIGNED — Records duration without judgment. [V10 §25.1]
- Gives out: DESIGNED — silence_interval. [V10 §25.1]
- Must never: DESIGNED — Label silence expected, unexpected, emotional or communicative. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The raw silence duration. | Uses silence_interval. | Silence gains no judgment. | [V10 §25.1] |
| 2 · DESIGNED | C-OOP.2.1 — Post-output voice behavior | The actual authorized physical voice events. | Supplies raw silence interval. | Nothing in this card. | [V10 §26.6] |

SUB-PARTS: NONE

### C-BOP.2.4 — non_word_sound
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A non-language sound physically typed only as breath or non_breath_non_word. [V10 §25.1]
- Takes in: DESIGNED — The actual raw sound. [V10 §25.1]
- Does: DESIGNED — Uses one of the two physical descriptions. [V10 §25.1]
- Gives out: DESIGNED — A non_word_sound with physical type. [V10 §25.1]
- Must never: DESIGNED — Label a sound hesitation_sound, filler or any communicative function. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.4.1 — breath: breath; C-BOP.2.4.2 — non_breath_non_word: non_breath_non_word. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The physical non-language sound. | Records only its physical type. | No function is attributed. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.4.1 — breath; C-BOP.2.4.2 — non_breath_non_word

### C-BOP.2.4.1 — breath
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The breath physical subtype. [V10 §25.1]
- Takes in: DESIGNED — A physically identified breath sound. [V10 §25.1]
- Does: DESIGNED — Carries breath as the subtype. [V10 §25.1]
- Gives out: DESIGNED — breath. [V10 §25.1]
- Must never: DESIGNED — Infer hesitation or intent. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.4 — non_word_sound | The breath classification. | Preserves physical type only. | No communicative label is created. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.4.2 — non_breath_non_word
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The other non-word physical subtype. [V10 §25.1]
- Takes in: DESIGNED — A non-breath non-language sound. [V10 §25.1]
- Does: DESIGNED — Carries non_breath_non_word. [V10 §25.1]
- Gives out: DESIGNED — non_breath_non_word. [V10 §25.1]
- Must never: DESIGNED — Assign emotional or communicative meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.4 — non_word_sound | The non-breath sound classification. | Preserves physical type only. | Meaning remains outside BOP. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.5 — voice_overlap
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Two voice channels simultaneously active. [V10 §25.1]
- Takes in: DESIGNED — The simultaneous activity of both channels. [V10 §25.1]
- Does: DESIGNED — Records the overlap as physical timing. [V10 §25.1]
- Gives out: DESIGNED — voice_overlap. [V10 §25.1]
- Must never: DESIGNED — Conclude speaker identity or conversational intent. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The concurrent channel activity. | Uses voice_overlap. | Overlap is a raw event. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.6 — voice_interrupt_of_nh
Stamp: DESIGNED    Source: [V10 §25.1] [V10 §26.4] [MAP C-BOP]

ALONE
- What it is: DESIGNED — Ness’s voice began while N.H TTS was active. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Takes in: DESIGNED — The physical onset and the active output-stream position. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Does: DESIGNED — Records the event with timestamp and position in N.H’s output stream; OOP enforces immediate TTS stop during voice-mode execution. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Gives out: DESIGNED — A physical voice_interrupt_of_nh observation. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Must never: DESIGNED — Interpret the occurrence as correction, continuation request, stop signal or any reason for interrupting. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-OOP — Outcome Observation Processing (§26): the voice-priority occurrence during function execution; C-BOP.2.6.1 — Voice-interruption timestamp: timestamp; C-BOP.2.6.2 — Voice-interruption output-stream position: output position. [V10 §25.1] [V10 §26.4] [MAP C-BOP]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The physical TTS-interruption event. | Records it without interpretation. | Stop enforcement stays with OOP. | [V10 §25.1] |
| 2 · DESIGNED | C-OOP.2.1 — Post-output voice behavior | The actual authorized physical voice events. | Supplies physical TTS interruption. | Nothing in this card. | [V10 §26.6] |
| 3 · DESIGNED | C-9.2.7 — Voice-priority pipeline interruption | Ness beginning to speak during voice-mode execution. | Takes this place's change: supplies the actual interruption fact for physical recording. | Supplies the actual interruption fact for physical recording. | [MAP C-9] |
| 4 · DESIGNED | C-OOP.7 — Immediate voice-priority TTS stop | Ness beginning to speak while N.H TTS is active. | Supplies canonical physical event contract with timestamp and position. | Nothing in this card. | [V10 §26.4] [MAP C-OOP] |

SUB-PARTS: C-BOP.2.6.1 — Voice-interruption timestamp; C-BOP.2.6.2 — Voice-interruption output-stream position

### C-BOP.2.6.1 — Voice-interruption timestamp
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The timestamp of the physical interruption. [V10 §25.1]
- Takes in: DESIGNED — The actual event time. [V10 §25.1]
- Does: DESIGNED — Preserves when voice began during TTS. [V10 §25.1]
- Gives out: DESIGNED — An interruption timestamp. [V10 §25.1]
- Must never: DESIGNED — Substitute an inferred time. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.6 — voice_interrupt_of_nh | The physical event timestamp. | Records the timing. | The event remains locatable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.6.2 — Voice-interruption output-stream position
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The position in N.H’s output stream when the interruption occurred. [V10 §25.1]
- Takes in: DESIGNED — The actual current output position. [V10 §25.1]
- Does: DESIGNED — Preserves that position. [V10 §25.1]
- Gives out: DESIGNED — A physical output-stream position. [V10 §25.1]
- Must never: DESIGNED — Resolve what a later reference means merely from this recorded position. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.6 — voice_interrupt_of_nh | The stream position at interruption. | Records the physical position. | Interpretation remains separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.7 — pitch_measurement
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Raw pitch values for an interval. [V10 §25.1]
- Takes in: DESIGNED — Measured hz_min, hz_max and hz_mean with measurement_method and measurement_version. [V10 §25.1]
- Does: DESIGNED — Records those values and required measurement provenance without an emotional label. [V10 §25.1]
- Gives out: DESIGNED — A pitch_measurement with all five named fields. [V10 §25.1]
- Must never: DESIGNED — Emit a bare pitch label or an emotion. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.7.1 — hz_min: hz_min; C-BOP.2.7.2 — hz_max: hz_max; C-BOP.2.7.3 — hz_mean: hz_mean; C-BOP.2.7.4 — measurement_method: measurement_method; C-BOP.2.7.5 — measurement_version: measurement_version. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The interval’s raw pitch measurements. | Preserves values and provenance. | No emotion is inferred. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.7.1 — hz_min; C-BOP.2.7.2 — hz_max; C-BOP.2.7.3 — hz_mean; C-BOP.2.7.4 — measurement_method; C-BOP.2.7.5 — measurement_version

### C-BOP.2.7.1 — hz_min
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The interval’s minimum raw pitch value. [V10 §25.1]
- Takes in: DESIGNED — The measured minimum in hertz. [V10 §25.1]
- Does: DESIGNED — Records hz_min. [V10 §25.1]
- Gives out: DESIGNED — hz_min. [V10 §25.1]
- Must never: DESIGNED — Turn the value into an emotional label. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.7 — pitch_measurement | The minimum pitch value. | Preserves the raw minimum. | The measurement stays checkable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.7.2 — hz_max
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The interval’s maximum raw pitch value. [V10 §25.1]
- Takes in: DESIGNED — The measured maximum in hertz. [V10 §25.1]
- Does: DESIGNED — Records hz_max. [V10 §25.1]
- Gives out: DESIGNED — hz_max. [V10 §25.1]
- Must never: DESIGNED — Infer emotion from the field. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.7 — pitch_measurement | The maximum pitch value. | Preserves the raw maximum. | The measurement stays physical. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.7.3 — hz_mean
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The interval’s mean raw pitch value. [V10 §25.1]
- Takes in: DESIGNED — The measured mean in hertz. [V10 §25.1]
- Does: DESIGNED — Records hz_mean. [V10 §25.1]
- Gives out: DESIGNED — hz_mean. [V10 §25.1]
- Must never: DESIGNED — Replace the value with interpretation. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.7 — pitch_measurement | The mean pitch value. | Preserves the raw mean. | No meaning is added. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.7.4 — measurement_method
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The required method that produced the acoustic measurement. [V10 §25.1]
- Takes in: DESIGNED — The actual measurement method. [V10 §25.1]
- Does: DESIGNED — Records measurement_method. [V10 §25.1]
- Gives out: DESIGNED — Required method provenance. [V10 §25.1]
- Must never: DESIGNED — Emit the measurement without its method. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.7 — pitch_measurement | The actual measurement method. | Keeps pitch provenance explicit. | The value can be checked. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.2.8 — amplitude_measurement | The actual measurement_method. | Preserves required amplitude provenance. | No bare measurement is emitted. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.7.5 — measurement_version
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The required version of the acoustic measurement method. [V10 §25.1]
- Takes in: DESIGNED — The actual method version. [V10 §25.1]
- Does: DESIGNED — Records measurement_version. [V10 §25.1]
- Gives out: DESIGNED — Required version provenance. [V10 §25.1]
- Must never: DESIGNED — Emit the measurement without its version. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.7 — pitch_measurement | The actual measurement version. | Preserves version provenance. | Method changes remain traceable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.2.8 — amplitude_measurement | The actual measurement_version. | Preserves required amplitude provenance. | The measurement remains attributable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.8 — amplitude_measurement
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Raw amplitude or energy for an interval. [V10 §25.1]
- Takes in: DESIGNED — The actual physical amplitude/energy measurement. [V10 §25.1]
- Does: DESIGNED — Records the raw values with the same required method/version provenance as pitch. [V10 §25.1]
- Gives out: DESIGNED — amplitude_measurement with provenance. [V10 §25.1]
- Must never: DESIGNED — Infer an emotional or expressive label. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.7.4 — measurement_method: required measurement_method; C-BOP.2.7.5 — measurement_version: required measurement_version. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The raw amplitude/energy interval. | Preserves it as a measurement. | No interpreted label is produced. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.9 — text_message_sent
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A confirmed sent-message event without a duplicate copy of its content. [V10 §25.1]
- Takes in: DESIGNED — The sent conversational root and its raw counts. [V10 §25.1]
- Does: DESIGNED — Records character_count, word_count, sentence_count_approx and exact_text_reference. [V10 §25.1]
- Gives out: DESIGNED — text_message_sent with a reference to the conversational root carrying content. [V10 §25.1]
- Must never: DESIGNED — Copy message content into BOP or observe unfinished typing. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.9.1 — character_count: character_count; C-BOP.2.9.2 — word_count: word_count; C-BOP.2.9.3 — sentence_count_approx: sentence_count_approx; C-BOP.2.9.4 — exact_text_reference: exact_text_reference. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The confirmed sent-message facts. | Records counts and a reference. | The conversational root retains the content. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.9.1 — character_count; C-BOP.2.9.2 — word_count; C-BOP.2.9.3 — sentence_count_approx; C-BOP.2.9.4 — exact_text_reference

### C-BOP.2.9.1 — character_count
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The sent message’s character count. [V10 §25.1]
- Takes in: DESIGNED — The actual confirmed message. [V10 §25.1]
- Does: DESIGNED — Records its raw character_count. [V10 §25.1]
- Gives out: DESIGNED — character_count. [V10 §25.1]
- Must never: DESIGNED — Treat length as importance or meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.9 — text_message_sent | The character count. | Preserves the raw count. | No meaning is inferred. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.9.2 — word_count
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The sent message’s word count. [V10 §25.1]
- Takes in: DESIGNED — The confirmed sent text. [V10 §25.1]
- Does: DESIGNED — Records word_count. [V10 §25.1]
- Gives out: DESIGNED — word_count. [V10 §25.1]
- Must never: DESIGNED — Infer intent from count. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.9 — text_message_sent | The word count. | Preserves the raw count. | The event stays physical. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.9.3 — sentence_count_approx
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The approximate sentence count of the sent message. [V10 §25.1]
- Takes in: DESIGNED — The actual sent text. [V10 §25.1]
- Does: DESIGNED — Records sentence_count_approx with its approximate standing. [V10 §25.1]
- Gives out: DESIGNED — sentence_count_approx. [V10 §25.1]
- Must never: DESIGNED — Present an approximate count as a meaning conclusion. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.9 — text_message_sent | The approximate sentence count. | Preserves its scope. | No exact semantic segmentation is implied. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.9.4 — exact_text_reference
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The root ID of the conversational root carrying the message content. [V10 §25.1]
- Takes in: DESIGNED — The actual conversational root identity. [V10 §25.1]
- Does: DESIGNED — References that root without copying its content. [V10 §25.1]
- Gives out: DESIGNED — exact_text_reference. [V10 §25.1]
- Must never: DESIGNED — Duplicate the message inside BOP. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.9 — text_message_sent | The conversational root ID. | Keeps content in its proper root. | BOP retains a link only. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.10 — text_response_timing
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The raw millisecond delta from completion of N.H output to the sent message. [V10 §25.1]
- Takes in: DESIGNED — The actual output-completion event and message time. [V10 §25.1]
- Does: DESIGNED — Records the raw ms delta and a reference to that N.H output event. [V10 §25.1]
- Gives out: DESIGNED — text_response_timing with delta and output-event reference. [V10 §25.1]
- Must never: DESIGNED — Infer response meaning or approval from timing. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.10.1 — Text-response raw millisecond delta: millisecond delta; C-BOP.2.10.2 — Text-response N.H output-event reference: output-event reference. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual text response timing. | Preserves timing and output provenance. | Delay carries no interpretation. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.10.1 — Text-response raw millisecond delta; C-BOP.2.10.2 — Text-response N.H output-event reference

### C-BOP.2.10.1 — Text-response raw millisecond delta
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The raw milliseconds from N.H output completion to the message. [V10 §25.1]
- Takes in: DESIGNED — The two actual event times. [V10 §25.1]
- Does: DESIGNED — Preserves their raw timing difference. [V10 §25.1]
- Gives out: DESIGNED — A millisecond delta. [V10 §25.1]
- Must never: DESIGNED — Label the delay expected or meaningful. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.10 — text_response_timing | The raw delta. | Records response timing only. | No judgment is created. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.10.2 — Text-response N.H output-event reference
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The reference to the N.H output event used for timing. [V10 §25.1]
- Takes in: DESIGNED — The actual output event. [V10 §25.1]
- Does: DESIGNED — Preserves its identity. [V10 §25.1]
- Gives out: DESIGNED — An output-event reference. [V10 §25.1]
- Must never: DESIGNED — Guess which output a reply concerns from meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.10 — text_response_timing | The output-event reference. | Binds the measured delta. | The timing basis remains explicit. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.11 — no_response_session
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A session opened and closed with zero sent messages. [V10 §25.1]
- Takes in: DESIGNED — The session-open/close facts and sent-message count of zero. [V10 §25.1]
- Does: DESIGNED — Records no_response_session. [V10 §25.1]
- Gives out: DESIGNED — The raw zero-sent-message session fact. [V10 §25.1]
- Must never: DESIGNED — Treat no response as approval or a preference. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The zero-message closed session. | Records only the observed fact. | Absence gains no meaning. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.12 — system_command
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — A deterministic defined interface command. [V10 §25.1]
- Takes in: DESIGNED — The actual command_identifier from the interface command registry. [V10 §25.1]
- Does: DESIGNED — Records the defined command and its registered identifier. [V10 §25.1]
- Gives out: DESIGNED — system_command with command_identifier. [V10 §25.1]
- Must never: DESIGNED — Interpret ordinary spoken or typed language as a system-command event. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2.12.1 — command_identifier: command_identifier. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The deterministic interface event. | Uses the registered command identity. | Ordinary language remains separate. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The registered deterministic command identity. | Keeps biometric observations within that event boundary. | Ordinary language is never treated as a command. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: C-BOP.2.12.1 — command_identifier

### C-BOP.2.12.1 — command_identifier
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The stable identifier of the defined interface command. [V10 §25.1]
- Takes in: DESIGNED — An identifier from the interface command registry. [V10 §25.1]
- Does: DESIGNED — Preserves command_identifier. [V10 §25.1]
- Gives out: DESIGNED — The registered command identity. [V10 §25.1]
- Must never: DESIGNED — Invent a command by interpreting natural language. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.12 — system_command | The registry command identifier. | Binds the event to a defined command. | No language classifier is introduced. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.13 — session_opened
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical session-open event. [V10 §25.1]
- Takes in: DESIGNED — The actual session opening. [V10 §25.1]
- Does: DESIGNED — Records session_opened. [V10 §25.1]
- Gives out: DESIGNED — A session_opened observation. [V10 §25.1]
- Must never: DESIGNED — Infer opening from conversation meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The session opening. | Records the actual state event. | Session occurrence is traceable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.14 — session_closed
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical session-close event. [V10 §25.1]
- Takes in: DESIGNED — The actual session closing. [V10 §25.1]
- Does: DESIGNED — Records session_closed. [V10 §25.1]
- Gives out: DESIGNED — A session_closed observation. [V10 §25.1]
- Must never: DESIGNED — Invent a close event. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The session closing. | Records the actual close. | The event retains its true timing. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.15 — session_interrupted
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The session-interruption event, including a crash reported on restart. [V10 §25.1]
- Takes in: DESIGNED — The interruption or crash recovery fact. [V10 §25.1]
- Does: DESIGNED — Records session_interrupted honestly. [V10 §25.1]
- Gives out: DESIGNED — An interruption root. [V10 §25.1]
- Must never: DESIGNED — Reconstruct missed observations. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual session interruption. | Records the gap. | Missing capture remains missing. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.11.3 — Session-crash restart observation | The actual session_interrupted event. | Records the known interruption and gap. | Nothing uncaptured is reconstructed. | [V10 §25.1] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.6 — Reaction-window interruption closure | The actual session_interrupted event. | Records the known interruption and gap. | Nothing uncaptured is reconstructed. | [V10 §25.1] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-OOP.8.4 — Honest outcome crash and partial recovery | Committed captures, promotion checkpoints and unfinished items. | Supplies physical session_interrupted event. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.2.16 — function_started
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical function-start event. [V10 §25.1]
- Takes in: DESIGNED — Actual function start. [V10 §25.1]
- Does: DESIGNED — Records function_started. [V10 §25.1]
- Gives out: DESIGNED — A function_started observation. [V10 §25.1]
- Must never: DESIGNED — Infer function meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual function start. | Records the event. | No interpretation follows. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.17 — function_completed
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical function-completion event. [V10 §25.1]
- Takes in: DESIGNED — Actual function completion. [V10 §25.1]
- Does: DESIGNED — Records function_completed. [V10 §25.1]
- Gives out: DESIGNED — A function_completed observation. [V10 §25.1]
- Must never: DESIGNED — Treat completion as user approval. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual completion. | Records the event. | Completion is not acceptance. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.18 — function_interrupted
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical function-interruption event. [V10 §25.1]
- Takes in: DESIGNED — Actual function interruption. [V10 §25.1]
- Does: DESIGNED — Records function_interrupted. [V10 §25.1]
- Gives out: DESIGNED — A function_interrupted observation. [V10 §25.1]
- Must never: DESIGNED — Infer the reason for interruption. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual interruption. | Records the event. | Meaning remains unasserted. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.19 — capture_failure
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The physical capture-failure event. [V10 §25.1]
- Takes in: DESIGNED — The actual capture failure and gap. [V10 §25.1]
- Does: DESIGNED — Records capture_failure honestly. [V10 §25.1]
- Gives out: DESIGNED — A failure root. [V10 §25.1]
- Must never: DESIGNED — Invent uncaptured observations. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The failed capture. | Records its gap. | Failure remains explicit. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.11.1 — Capture failure observation | The actual capture_failure event. | Records the failed capture honestly. | The gap creates no inferred observation. | [V10 §25.1] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.6 — Reaction-window interruption closure | The actual capture_failure event. | Records the failed capture honestly. | The gap creates no inferred observation. | [V10 §25.1] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-OOP.8.4 — Honest outcome crash and partial recovery | Committed captures, promotion checkpoints and unfinished items. | Supplies physical capture_failure event. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.2.20 — import_authorized
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The authorized-import event. [V10 §25.1]
- Takes in: DESIGNED — The actual import authorization. [V10 §25.1]
- Does: DESIGNED — Records import_authorized. [V10 §25.1]
- Gives out: DESIGNED — An import_authorized observation. [V10 §25.1]
- Must never: DESIGNED — Widen authorization to unrelated content. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual import authorization. | Records the event. | Scope stays source-specific. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.21 — import_processed
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The import-processing event. [V10 §25.1]
- Takes in: DESIGNED — Actual completed import processing. [V10 §25.1]
- Does: DESIGNED — Records import_processed. [V10 §25.1]
- Gives out: DESIGNED — An import_processed observation. [V10 §25.1]
- Must never: DESIGNED — Infer meaning or truth from successful processing. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The actual processed import. | Records the event. | Processing is not interpretation. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.2.22 — extended
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The extension route for newly measurable authorized signals outside v1. [V10 §25.1]
- Takes in: DESIGNED — A registered extended_event_type_id and raw_payload. [V10 §25.1]
- Does: DESIGNED — Uses extended only after registration before first use. [V10 §25.1]
- Gives out: DESIGNED — An extended physical event with its registered identity and raw payload. [V10 §25.1]
- Must never: DESIGNED — Use an unregistered extended type or smuggle interpretation into raw_payload. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.3 — extended_event_type_id: registered extended identity; C-BOP.4.4 — extended_event_type_version: extension version; C-BOP.2.22.1 — Extended raw_payload: raw_payload. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2 — BOP v1 controlled event vocabulary | The registered new physical event. | Uses the controlled extension route. | New observation types create no meaning authority. | [V10 §25.1] |

SUB-PARTS: C-BOP.2.22.1 — Extended raw_payload

### C-BOP.2.22.1 — Extended raw_payload
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The raw payload of an extended measurable authorized event. [V10 §25.1]
- Takes in: DESIGNED — The physical measurements of the registered event. [V10 §25.1]
- Does: DESIGNED — Preserves raw_payload. [V10 §25.1]
- Gives out: DESIGNED — A raw extended payload. [V10 §25.1]
- Must never: DESIGNED — Place an interpreted meaning label in it. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.2.22 — extended | The registered event’s raw payload. | Carries physical data only. | The DUMB boundary still applies. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3 — Seven-field BOP root bindings
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The BOP-specific bindings inside the unchanged seven-field root schema. [V10 §25.1]
- Takes in: DESIGNED — The observation capture identity, time, payload and provenance. [V10 §25.1]
- Does: DESIGNED — Uses only id, subject, timestamp, content, re_reads, source_title and role. [V10 §25.1]
- Gives out: DESIGNED — A seven-field root with its payload serialized inside content. [V10 §25.1]
- Must never: DESIGNED — Add an eighth base-root field or repurpose subject as semantic content. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE.2 — Seven-field root schema v1: canonical unchanged seven-field root schema. [V10 §6A] [V10 §25.1]
- Fed by: DESIGNED — C-BOP.3.1 — BOP root id: id; C-BOP.3.2 — BOP root subject: subject; C-BOP.3.3 — BOP root timestamp: timestamp; C-BOP.3.4 — BOP root content: content; C-BOP.3.5 — BOP root re_reads: re_reads; C-BOP.3.6 — BOP root source_title: source_title; C-BOP.3.7 — BOP root role: role. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The seven BOP root bindings. | Preserves the base schema. | Observation fields remain within content. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The unchanged seven-field BOP bindings. | Keeps acoustic notes inside the payload. | No eighth root field is added. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: C-BOP.3.1 — BOP root id; C-BOP.3.2 — BOP root subject; C-BOP.3.3 — BOP root timestamp; C-BOP.3.4 — BOP root content; C-BOP.3.5 — BOP root re_reads; C-BOP.3.6 — BOP root source_title; C-BOP.3.7 — BOP root role

### C-BOP.3.1 — BOP root id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The root id bound to the corrected capture_id. [V10 §25.1]
- Takes in: DESIGNED — The corrected capture identity. [V10 §25.1]
- Does: DESIGNED — Uses it as id. [V10 §25.1]
- Gives out: DESIGNED — The stable BOP root identity. [V10 §25.1]
- Must never: DESIGNED — Mint a different id for a retry. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.5 — Corrected BOP capture_id: corrected capture_id. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The corrected capture_id. | Binds root id. | A retry retains identity. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.2 — BOP root subject
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The unchanged legacy source-class tag bop:v1. [V10 §25.1]
- Takes in: DESIGNED — The BOP root source classification. [V10 §25.1]
- Does: DESIGNED — Sets subject to "bop:v1". [V10 §25.1]
- Gives out: DESIGNED — subject = "bop:v1". [V10 §25.1]
- Must never: DESIGNED — Change the legacy tag or turn it into a semantic topic. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The BOP source-class tag. | Preserves subject. | The existing binding stays unchanged. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.3 — BOP root timestamp
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The BOP capture time, distinct from event time. [V10 §25.1]
- Takes in: DESIGNED — The actual capture time. [V10 §25.1]
- Does: DESIGNED — Stores it in timestamp. [V10 §25.1]
- Gives out: DESIGNED — The capture timestamp. [V10 §25.1]
- Must never: DESIGNED — Conflate capture time with event_occurred_at. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The actual capture time. | Records timestamp. | Event and capture times remain separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.4 — BOP root content
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The BOP payload serialized as a string in content. [V10 §25.1]
- Takes in: DESIGNED — The complete bop_payload. [V10 §25.1]
- Does: DESIGNED — Serializes the payload into the existing content field. [V10 §25.1]
- Gives out: DESIGNED — String content containing the BOP payload. [V10 §25.1]
- Must never: DESIGNED — Add payload fields outside the base schema. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4 — bop_payload: bop_payload. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The serialized BOP payload. | Uses the existing content field. | The base schema stays seven fields. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.5 — BOP root re_reads
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The empty list on the new raw observation root. [V10 §25.1]
- Takes in: DESIGNED — A new BOP root. [V10 §25.1]
- Does: DESIGNED — Sets re_reads to []. [V10 §25.1]
- Gives out: DESIGNED — re_reads = []. [V10 §25.1]
- Must never: DESIGNED — Attach an interpretation as a raw-root field. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The empty root reread list. | Preserves the raw-root binding. | Interpretations remain separate readings. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.6 — BOP root source_title
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The session grouping key under the existing source_title rules. [V10 §25.1]
- Takes in: DESIGNED — The actual authorized session grouping provenance. [V10 §25.1]
- Does: DESIGNED — Preserves that grouping key. [V10 §25.1]
- Gives out: DESIGNED — A source_title session grouping key. [V10 §25.1]
- Must never: DESIGNED — Infer a semantic topic as provenance. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The session grouping key. | Records source_title. | Source provenance stays structural. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.15.2 — Enrollment observation provenance | The enrollment session grouping key. | Uses enrollment:ness:<session_id>. | Source provenance does not confirm identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-BOP.3.7 — BOP root role
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The single role value of the observation root. [V10 §25.1]
- Takes in: DESIGNED — The actual source attribution with its declared or assessed standing. [V10 §25.1]
- Does: DESIGNED — Uses ness, nh, session or third_party_observed. [V10 §25.1]
- Gives out: DESIGNED — Exactly one permitted role. [V10 §25.1]
- Must never: DESIGNED — Merge simultaneous channels into multiple roles on one root or treat enrollment declaration as confirmed identity. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.3.7.1 — BOP role ness: ness; C-BOP.3.7.2 — BOP role nh: nh; C-BOP.3.7.3 — BOP role session: session; C-BOP.3.7.4 — BOP role third_party_observed: third_party_observed. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3 — Seven-field BOP root bindings | The actual role value. | Keeps one role per root. | Source attribution retains its standing. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.8 — One observation root per simultaneous signal channel | The single-role root constraint. | Creates a separate root per signal channel. | Simultaneous channels are linked, not merged. | [V10 §25.1] |

SUB-PARTS: C-BOP.3.7.1 — BOP role ness; C-BOP.3.7.2 — BOP role nh; C-BOP.3.7.3 — BOP role session; C-BOP.3.7.4 — BOP role third_party_observed

### C-BOP.3.7.1 — BOP role ness
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The ness role value. [V10 §25.1]
- Takes in: DESIGNED — The actual Ness attribution. [V10 §25.1]
- Does: DESIGNED — Carries ness with its actual provenance. [V10 §25.1]
- Gives out: DESIGNED — role = "ness". [V10 §25.1]
- Must never: DESIGNED — Treat enrollment-declared role as independently confirmed identity. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3.7 — BOP root role | The ness role value. | Preserves the attribution. | Its certainty is not upgraded. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.15.2 — Enrollment observation provenance | The declared ness role. | Preserves its enrollment-declared standing. | It is not an SIA conclusion. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-BOP.3.7.2 — BOP role nh
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The nh role value. [V10 §25.1]
- Takes in: DESIGNED — The N.H source attribution. [V10 §25.1]
- Does: DESIGNED — Carries nh. [V10 §25.1]
- Gives out: DESIGNED — role = "nh". [V10 §25.1]
- Must never: DESIGNED — Mix several roles on one root. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3.7 — BOP root role | The nh role value. | Preserves the source role. | The root remains single-role. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.7.3 — BOP role session
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The session role value. [V10 §25.1]
- Takes in: DESIGNED — The session-level event source. [V10 §25.1]
- Does: DESIGNED — Carries session. [V10 §25.1]
- Gives out: DESIGNED — role = "session". [V10 §25.1]
- Must never: DESIGNED — Turn a session event into speaker identity evidence. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3.7 — BOP root role | The session role value. | Preserves event provenance. | No speaker claim is added. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.3.7.4 — BOP role third_party_observed
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The third_party_observed role value. [V10 §25.1]
- Takes in: DESIGNED — The observed third-party source attribution. [V10 §25.1]
- Does: DESIGNED — Carries third_party_observed. [V10 §25.1]
- Gives out: DESIGNED — role = "third_party_observed". [V10 §25.1]
- Must never: DESIGNED — Infer a confirmed person identity. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.3.7 — BOP root role | The observed-third-party role. | Preserves the actual attribution. | No identity conclusion follows. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4 — bop_payload
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The typed physical-observation payload serialized in root content. [V10 §25.1]
- Takes in: DESIGNED — All source-decided schema, event, session, quality and provenance fields. [V10 §25.1]
- Does: DESIGNED — Carries the nineteen fields and their stated types/nullability without interpretation. [V10 §25.1]
- Gives out: DESIGNED — A bop_payload with complete honest source facts. [V10 §25.1]
- Must never: DESIGNED — Invent participant/anchor internals, add interpreted labels or conceal incompleteness. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.1 — bop_schema_version: schema version; C-BOP.4.2 — BOP event_type: event type; C-BOP.4.3 — extended_event_type_id: extended identity; C-BOP.4.4 — extended_event_type_version: extended version; C-BOP.4.5 — event_occurred_at: event time; C-BOP.4.6 — event_duration_ms: duration; C-BOP.4.7 — BOP session_id: session identity; C-BOP.4.8 — BOP session_mode: mode; C-BOP.4.9 — session_authorization: authorization; C-BOP.4.10 — BOP participants: participants; C-BOP.4.11 — signal_measurements: measurements; C-BOP.4.12 — simultaneous_bundle_id: bundle identity; C-BOP.4.13 — simultaneous_bundle_position: bundle position; C-BOP.6 — observation_quality: observation_quality; C-BOP.7 — third_party_flag: third_party_flag; C-BOP.9 — connection_anchors and later reconnection: connection_anchors; C-BOP.4.14 — bop_processor_version: processor version; C-BOP.4.15 — BOP capture_method: capture method; C-BOP.4.16 — capture_sequence_number: sequence number. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The complete physical payload. | Preserves its schema and provenance. | No BOP interpretation is created. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.3.4 — BOP root content | The complete bop_payload. | Serializes it as root content. | The seven-field root remains intact. | [V10 §25.1] |

SUB-PARTS: C-BOP.4.1 — bop_schema_version; C-BOP.4.2 — BOP event_type; C-BOP.4.3 — extended_event_type_id; C-BOP.4.4 — extended_event_type_version; C-BOP.4.5 — event_occurred_at; C-BOP.4.6 — event_duration_ms; C-BOP.4.7 — BOP session_id; C-BOP.4.8 — BOP session_mode; C-BOP.4.9 — session_authorization; C-BOP.4.10 — BOP participants; C-BOP.4.11 — signal_measurements; C-BOP.4.12 — simultaneous_bundle_id; C-BOP.4.13 — simultaneous_bundle_position; C-BOP.4.14 — bop_processor_version; C-BOP.4.15 — BOP capture_method; C-BOP.4.16 — capture_sequence_number

### C-BOP.4.1 — bop_schema_version
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The BOP payload version marker. [V10 §25.1]
- Takes in: DESIGNED — The v1 payload. [V10 §25.1]
- Does: DESIGNED — Carries "bop_v1". [V10 §25.1]
- Gives out: DESIGNED — bop_schema_version = "bop_v1". [V10 §25.1]
- Must never: DESIGNED — Imply a different active schema. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The bop_v1 marker. | Identifies the payload schema. | Version remains explicit. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.2 — BOP event_type
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The controlled event type string. [V10 §25.1]
- Takes in: DESIGNED — The actual physical event class. [V10 §25.1]
- Does: DESIGNED — Uses the v1 controlled vocabulary or extended. [V10 §25.1]
- Gives out: DESIGNED — event_type string. [V10 §25.1]
- Must never: DESIGNED — Use an interpreted meaning as the event type. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2 — BOP v1 controlled event vocabulary: exact event vocabulary. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The exact event_type. | Preserves the physical class. | Classification is controlled. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The exact physical event_type. | Includes it in stable capture identity. | The captured event class remains bound. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.3 — extended_event_type_id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The registered extension identity, a string or null. [V10 §25.1]
- Takes in: DESIGNED — The registered extended type when applicable. [V10 §25.1]
- Does: DESIGNED — Carries extended_event_type_id; registration precedes first use. [V10 §25.1]
- Gives out: DESIGNED — A string or null. [V10 §25.1]
- Must never: DESIGNED — Use an unregistered extension. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The extension identity or null. | Preserves its registration. | The extension remains controlled. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.2.22 — extended | The registered type identity. | Binds the extended event. | No unregistered type is admitted. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.4 — extended_event_type_version
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The extension’s version string or null. [V10 §25.1]
- Takes in: DESIGNED — The actual extended type version when applicable. [V10 §25.1]
- Does: DESIGNED — Carries extended_event_type_version. [V10 §25.1]
- Gives out: DESIGNED — A string or null. [V10 §25.1]
- Must never: DESIGNED — Silently replace the version. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The extension version or null. | Preserves version provenance. | Extensions remain identifiable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.2.22 — extended | The actual extension version. | Preserves its version binding. | The event remains attributable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.5 — event_occurred_at
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The ISO 8601 time when the event happened. [V10 §25.1]
- Takes in: DESIGNED — The actual occurrence time. [V10 §25.1]
- Does: DESIGNED — Records event_occurred_at separately from capture time. [V10 §25.1]
- Gives out: DESIGNED — An ISO 8601 event time. [V10 §25.1]
- Must never: DESIGNED — Substitute the later capture time as occurrence. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The occurrence time. | Preserves event timing. | Delayed capture stays distinguishable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The actual event_occurred_at. | Includes occurrence time in identity. | Capture time cannot silently replace it. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.6 — event_duration_ms
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The event duration in milliseconds, integer or null. [V10 §25.1]
- Takes in: DESIGNED — The actual duration when available. [V10 §25.1]
- Does: DESIGNED — Carries event_duration_ms honestly. [V10 §25.1]
- Gives out: DESIGNED — An integer or null. [V10 §25.1]
- Must never: DESIGNED — Invent a missing duration. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The measured duration or null. | Preserves duration standing. | Missing measurement stays explicit. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The measured duration or literal null marker. | Includes it in stable capture identity. | Absence is represented explicitly. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.7 — BOP session_id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The stable identifier of the authorized session. [V10 §25.1]
- Takes in: DESIGNED — The actual session identity. [V10 §25.1]
- Does: DESIGNED — Carries session_id. [V10 §25.1]
- Gives out: DESIGNED — A stable session identifier. [V10 §25.1]
- Must never: DESIGNED — Bind the observation to another session. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The actual session identity. | Preserves session provenance. | Grouping remains stable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The actual stable session_id. | Includes it in capture identity. | The observation remains session-bound. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8 — BOP session_mode
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The observation session’s controlled mode. [V10 §25.1]
- Takes in: DESIGNED — The actual session mode. [V10 §25.1]
- Does: DESIGNED — Uses voice, text, imported_audio, imported_video, imported_text or mixed. [V10 §25.1]
- Gives out: DESIGNED — The exact session_mode value. [V10 §25.1]
- Must never: DESIGNED — Infer an authorization from mode alone. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.8.1 — BOP mode voice: voice; C-BOP.4.8.2 — BOP mode text: text; C-BOP.4.8.3 — BOP mode imported_audio: imported_audio; C-BOP.4.8.4 — BOP mode imported_video: imported_video; C-BOP.4.8.5 — BOP mode imported_text: imported_text; C-BOP.4.8.6 — BOP mode mixed: mixed. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The actual mode. | Preserves the controlled value. | Mode is provenance, not permission. | [V10 §25.1] |

SUB-PARTS: C-BOP.4.8.1 — BOP mode voice; C-BOP.4.8.2 — BOP mode text; C-BOP.4.8.3 — BOP mode imported_audio; C-BOP.4.8.4 — BOP mode imported_video; C-BOP.4.8.5 — BOP mode imported_text; C-BOP.4.8.6 — BOP mode mixed

### C-BOP.4.8.1 — BOP mode voice
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The voice session-mode value. [V10 §25.1]
- Takes in: DESIGNED — An actual voice session. [V10 §25.1]
- Does: DESIGNED — Carries voice. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "voice". [V10 §25.1]
- Must never: DESIGNED — Treat mode as independent capture permission. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The voice mode. | Records the actual mode. | Authorization stays separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8.2 — BOP mode text
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The text session-mode value. [V10 §25.1]
- Takes in: DESIGNED — An actual text session. [V10 §25.1]
- Does: DESIGNED — Carries text. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "text". [V10 §25.1]
- Must never: DESIGNED — Observe unsent typing. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The text mode. | Records the actual mode. | Only sent text is observable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8.3 — BOP mode imported_audio
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The imported_audio mode value. [V10 §25.1]
- Takes in: DESIGNED — Authorized imported audio. [V10 §25.1]
- Does: DESIGNED — Carries imported_audio. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "imported_audio". [V10 §25.1]
- Must never: DESIGNED — Create authorization from the mode label. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The imported-audio mode. | Preserves source-mode provenance. | Permission remains separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8.4 — BOP mode imported_video
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The imported_video mode value. [V10 §25.1]
- Takes in: DESIGNED — Authorized imported video. [V10 §25.1]
- Does: DESIGNED — Carries imported_video. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "imported_video". [V10 §25.1]
- Must never: DESIGNED — Widen authorization through a mode label. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The imported-video mode. | Preserves source-mode provenance. | No new capture path follows. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8.5 — BOP mode imported_text
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The imported_text mode value. [V10 §25.1]
- Takes in: DESIGNED — Authorized imported text. [V10 §25.1]
- Does: DESIGNED — Carries imported_text. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "imported_text". [V10 §25.1]
- Must never: DESIGNED — Treat unrelated text as authorized. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The imported-text mode. | Preserves source-mode provenance. | Scope stays with the import. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.8.6 — BOP mode mixed
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The mixed session-mode value. [V10 §25.1]
- Takes in: DESIGNED — An actual mixed-mode session. [V10 §25.1]
- Does: DESIGNED — Carries mixed. [V10 §25.1]
- Gives out: DESIGNED — session_mode = "mixed". [V10 §25.1]
- Must never: DESIGNED — Merge different roles into one root. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.8 — BOP session_mode | The mixed mode. | Preserves session mode. | Channel separation still applies. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.9 — session_authorization
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The session-authorization object with type and event reference. [V10 §25.1]
- Takes in: DESIGNED — The actual authorization kind and event root ID. [V10 §25.1]
- Does: DESIGNED — Preserves authorization_type and authorization_event_id. [V10 §25.1]
- Gives out: DESIGNED — A two-field session_authorization object. [V10 §25.1]
- Must never: DESIGNED — Infer confirmed identity merely from declared enrollment authorization. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.9.1 — BOP authorization_type: authorization_type; C-BOP.4.9.2 — authorization_event_id: authorization_event_id. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The actual authorization object. | Preserves its origin. | Capture provenance remains explicit. | [V10 §25.1] |

SUB-PARTS: C-BOP.4.9.1 — BOP authorization_type; C-BOP.4.9.2 — authorization_event_id

### C-BOP.4.9.1 — BOP authorization_type
Stamp: DESIGNED    Source: [V10 §25.1] [V10 §25.12]

ALONE
- What it is: DESIGNED — The controlled authorization kind. [V10 §25.1] [V10 §25.12]
- Takes in: DESIGNED — The actual live-session, manual-import or enrollment-declared authorization. [V10 §25.1] [V10 §25.12]
- Does: DESIGNED — Uses live_session, manual_import or enrollment_declared. [V10 §25.1] [V10 §25.12]
- Gives out: DESIGNED — The exact authorization_type value. [V10 §25.1] [V10 §25.12]
- Must never: DESIGNED — Convert enrollment declaration into SIA-confirmed identity. [V10 §25.1] [V10 §25.12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.9.1.1 — live_session: live_session; C-BOP.4.9.1.2 — manual_import: manual_import; C-BOP.4.9.1.3 — enrollment_declared: enrollment_declared. [V10 §25.1] [V10 §25.12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.9 — session_authorization | The authorization kind. | Preserves its precise meaning. | No identity authority is added. | [V10 §25.1] |

SUB-PARTS: C-BOP.4.9.1.1 — live_session; C-BOP.4.9.1.2 — manual_import; C-BOP.4.9.1.3 — enrollment_declared

### C-BOP.4.9.1.1 — live_session
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The live-session authorization value. [V10 §25.1]
- Takes in: DESIGNED — The actual live-session authorization. [V10 §25.1]
- Does: DESIGNED — Carries live_session. [V10 §25.1]
- Gives out: DESIGNED — authorization_type = "live_session". [V10 §25.1]
- Must never: DESIGNED — Authorize outside-session capture. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.9.1 — BOP authorization_type | The live_session value. | Records authorization provenance. | Session scope remains bounded. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.9.1.2 — manual_import
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The manual-import authorization value. [V10 §25.1]
- Takes in: DESIGNED — The actual explicitly authorized import. [V10 §25.1]
- Does: DESIGNED — Carries manual_import. [V10 §25.1]
- Gives out: DESIGNED — authorization_type = "manual_import". [V10 §25.1]
- Must never: DESIGNED — Expand to an unrelated source. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.9.1 — BOP authorization_type | The manual_import value. | Records import authorization. | Scope remains with the source. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.9.1.3 — enrollment_declared
Stamp: DESIGNED    Source: [V10 §25.12]

ALONE
- What it is: DESIGNED — The formally adopted value for role attribution declared by an authorized enrollment flow. [V10 §25.12]
- Takes in: DESIGNED — The actual authorized enrollment declaration. [V10 §25.12]
- Does: DESIGNED — Signals that speaker identity has not yet been independently confirmed by SIA; uses the existing extensible vocabulary without a schema version change. [V10 §25.12]
- Gives out: DESIGNED — authorization_type = "enrollment_declared". [V10 §25.12]
- Must never: DESIGNED — Treat the value or role ness as confirmed identity. [V10 §25.12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.9.1 — BOP authorization_type | The enrollment_declared value. | Preserves declared-attribution standing. | Identity remains for SIA to assess. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.15.2 — Enrollment observation provenance | The enrollment_declared value. | Preserves declared role provenance. | It grants no confirmed voice identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-ENROLL.9.5 — Declared authorization and durable-token check | `authorization_type="enrollment_declared"` and the segment's `session_id`. | Supplies canonical declared authorization meaning. | Nothing in this card. | [V10 §25.12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-BOP.4.9.2 — authorization_event_id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The reference to the authorization event’s root ID. [V10 §25.1]
- Takes in: DESIGNED — The actual authorization event. [V10 §25.1]
- Does: DESIGNED — Preserves its root reference. [V10 §25.1]
- Gives out: DESIGNED — authorization_event_id. [V10 §25.1]
- Must never: DESIGNED — Substitute an unrelated event as authority. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.9 — session_authorization | The authorization event reference. | Makes authorization provenance traceable. | The source of the declaration stays explicit. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.10 — BOP participants
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The list of participant_record objects. [V10 §25.1]
- Takes in: DESIGNED — The available participant records. [V10 §25.1]
- Does: DESIGNED — Carries the list with its actual standing. [V10 §25.1]
- Gives out: DESIGNED — participants as a list of participant_record objects. [V10 §25.1]
- Must never: DESIGNED — Invent source-unspecified participant fields or infer identities. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The participant-record list. | Preserves supplied participant data. | No new identity assessment is made. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.11 — signal_measurements
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The raw physical-measurement object, whose structure varies by event_type. [V10 §25.1]
- Takes in: DESIGNED — The actual physical measurements and provenance. [V10 §25.1]
- Does: DESIGNED — Carries only the event’s physical values. [V10 §25.1]
- Gives out: DESIGNED — A signal_measurements object without interpreted labels. [V10 §25.1]
- Must never: DESIGNED — Place emotion, meaning or identity conclusions inside measurements. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.2 — BOP v1 controlled event vocabulary: event-specific fields and physical types. [V10 §25.1]
- Fed by: ACCEPTED — C-BOP.12 — Optional acoustic_condition_notes amendment: accepted optional voice-channel acoustic_condition_notes at policy/design level. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The raw measurements. | Preserves the appropriate event structure. | No interpreted label enters the payload. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.12 — simultaneous_bundle_id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The simultaneous-moment bundle identifier, string or null. [V10 §25.1]
- Takes in: DESIGNED — The actual simultaneous bundle where applicable. [V10 §25.1]
- Does: DESIGNED — Carries its shared identifier. [V10 §25.1]
- Gives out: DESIGNED — simultaneous_bundle_id as string or null. [V10 §25.1]
- Must never: DESIGNED — Merge channel roots instead of linking them. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The bundle identity or null. | Preserves simultaneous grouping. | Separate roots remain reconstructible. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.8 — One observation root per simultaneous signal channel | The shared simultaneous_bundle_id. | Links roots from the same moment. | The bundle remains reconstructible. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.13 — simultaneous_bundle_position
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The bundle position, integer or null. [V10 §25.1]
- Takes in: DESIGNED — The actual position where applicable. [V10 §25.1]
- Does: DESIGNED — Carries simultaneous_bundle_position. [V10 §25.1]
- Gives out: DESIGNED — An integer or null. [V10 §25.1]
- Must never: DESIGNED — Invent unavailable ordering. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The bundle position or null. | Preserves recorded structure. | Missing position remains explicit. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.8 — One observation root per simultaneous signal channel | The recorded simultaneous_bundle_position. | Preserves bundle structure. | No unavailable order is invented. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.14 — bop_processor_version
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The processor-version string. [V10 §25.1]
- Takes in: DESIGNED — The BOP processor version that performed capture. [V10 §25.1]
- Does: DESIGNED — Records bop_processor_version. [V10 §25.1]
- Gives out: DESIGNED — A version string. [V10 §25.1]
- Must never: DESIGNED — Silently replace capture provenance. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The actual processor version. | Preserves capture provenance. | Identity construction remains attributable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The actual bop_processor_version. | Includes it in stable capture identity. | Capture provenance remains part of identity. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.15 — BOP capture_method
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The capture-method value. [V10 §25.1]
- Takes in: DESIGNED — The actual capture route. [V10 §25.1]
- Does: DESIGNED — Uses live_capture, import_processing or session_state_event. [V10 §25.1]
- Gives out: DESIGNED — The exact capture_method. [V10 §25.1]
- Must never: DESIGNED — Invent a new authorized route from a method label. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.15.1 — live_capture: live_capture; C-BOP.4.15.2 — import_processing: import_processing; C-BOP.4.15.3 — session_state_event: session_state_event. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The actual capture method. | Preserves route provenance. | Method is not authorization. | [V10 §25.1] |

SUB-PARTS: C-BOP.4.15.1 — live_capture; C-BOP.4.15.2 — import_processing; C-BOP.4.15.3 — session_state_event

### C-BOP.4.15.1 — live_capture
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The live_capture method value. [V10 §25.1]
- Takes in: DESIGNED — Actual live capture. [V10 §25.1]
- Does: DESIGNED — Carries live_capture. [V10 §25.1]
- Gives out: DESIGNED — capture_method = "live_capture". [V10 §25.1]
- Must never: DESIGNED — Capture an unauthorized source. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.15 — BOP capture_method | The live_capture value. | Records the actual method. | The source remains governed. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.15.2 — import_processing
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The import_processing method value. [V10 §25.1]
- Takes in: DESIGNED — Actual authorized import processing. [V10 §25.1]
- Does: DESIGNED — Carries import_processing. [V10 §25.1]
- Gives out: DESIGNED — capture_method = "import_processing". [V10 §25.1]
- Must never: DESIGNED — Treat import processing as meaning interpretation. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.15 — BOP capture_method | The import_processing value. | Records the actual method. | Physical capture remains distinct. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.15.3 — session_state_event
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The session_state_event method value. [V10 §25.1]
- Takes in: DESIGNED — An actual session-state observation. [V10 §25.1]
- Does: DESIGNED — Carries session_state_event. [V10 §25.1]
- Gives out: DESIGNED — capture_method = "session_state_event". [V10 §25.1]
- Must never: DESIGNED — Infer unobserved state from meaning. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4.15 — BOP capture_method | The session_state_event value. | Records the actual method. | The state event remains physical. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.4.16 — capture_sequence_number
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The monotonically increasing integer unique within the session. [V10 §25.1]
- Takes in: DESIGNED — The next actual capture sequence number. [V10 §25.1]
- Does: DESIGNED — Persists it in a local durable log before any write attempt and uses it in capture_id construction. [V10 §25.1]
- Gives out: DESIGNED — A durable session-unique sequence integer. [V10 §25.1]
- Must never: DESIGNED — Write first and persist the sequence afterward, or change the number on retry. [V10 §25.1]
- Fails closed by: DESIGNED — No write is attempted before the sequence is durably persisted. [V10 §25.1]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.4 — bop_payload | The persisted sequence number. | Carries durable ordering. | Capture identity survives retry. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.5 — Corrected BOP capture_id | The durable unique capture_sequence_number. | Includes it only after persistence before writes. | Retry retains the same capture. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.5 — Corrected BOP capture_id
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The stable hash of six capture facts. [V10 §25.1]
- Takes in: DESIGNED — session_id, event_type, event_occurred_at, event_duration_ms or the literal "null" when absent, capture_sequence_number, and bop_processor_version. [V10 §25.1]
- Does: DESIGNED — Computes capture_id = stable_hash(session_id, event_type, event_occurred_at, event_duration_ms or "null", capture_sequence_number, bop_processor_version). [V10 §25.1]
- Gives out: DESIGNED — One stable capture identity for the observation. [V10 §25.1]
- Must never: DESIGNED — Change identity across write retries or invent hash encoding/algorithm details. [V10 §25.1]
- Fails closed by: DESIGNED — The sequence is persisted before any write attempt. [V10 §25.1]

TOGETHER
- Fed by: DESIGNED — C-BOP.4.7 — BOP session_id: session identity; C-BOP.4.2 — BOP event_type: event type; C-BOP.4.5 — event_occurred_at: occurrence time; C-BOP.4.6 — event_duration_ms: duration/null; C-BOP.4.16 — capture_sequence_number: durable unique sequence; C-BOP.4.14 — bop_processor_version: processor version. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The six capture-identity facts. | Constructs stable identity. | Duplicate capture writes remain absorbable. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.3.1 — BOP root id | The stable corrected capture_id. | Uses it as root id. | The observation retains one identity. | [V10 §25.1] |
| 3 · DESIGNED | C-BOP.11.2 — Same-capture write retry | The stable capture_id and durable sequence basis. | Keeps retries attached to the original capture. | No duplicate observation is invented. | [V10 §25.1] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |
| 4 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The stable capture_id and durable sequence basis. | Keeps retries attached to the original capture. | No duplicate observation is invented. | [V10 §25.1] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-BOP.6 — observation_quality
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The honest measurement-quality and completeness object. [V10 §25.1]
- Takes in: DESIGNED — Signal quality, its note, per-field completeness and overall completeness. [V10 §25.1]
- Does: DESIGNED — Records incompleteness honestly; low quality alone does not erase a root and the Meaning Engine may return insufficient_context. [V10 §25.1]
- Gives out: DESIGNED — The four-field observation_quality object; even below_threshold roots follow the authorized normal root path. [V10 §25.1]
- Must never: DESIGNED — Invent missing data, reconstruct crash gaps or treat quality as capture/use authorization. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.6.1 — signal_quality: signal_quality; C-BOP.6.2 — signal_quality_note: signal_quality_note; C-BOP.6.3 — field_completeness: field_completeness; C-BOP.6.4 — overall_completeness: overall_completeness. [V10 §25.1]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and use still require applicable authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): held/ingestion gates still apply. [V10 §25.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The actual quality/completeness. | Preserves uncertainty without inventing data. | The reader sees honest limits. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.4 — bop_payload | The observation_quality object. | Carries quality within the payload. | Incomplete data remains marked. | [V10 §25.1] |
| 3 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The existing observation_quality contract. | Keeps honest incompleteness around acoustic notes. | The amendment does not hide quality limits. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: C-BOP.6.1 — signal_quality; C-BOP.6.2 — signal_quality_note; C-BOP.6.3 — field_completeness; C-BOP.6.4 — overall_completeness

### C-BOP.6.1 — signal_quality
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The controlled signal-quality value. [V10 §25.1]
- Takes in: DESIGNED — The actual signal-quality classification. [V10 §25.1]
- Does: DESIGNED — Uses clean, partial, degraded or reconstruction. [V10 §25.1]
- Gives out: DESIGNED — The exact signal_quality. [V10 §25.1]
- Must never: DESIGNED — Use a reconstruction label as permission to invent uncaptured observations. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.6.1.1 — Signal quality clean: clean; C-BOP.6.1.2 — Signal quality partial: partial; C-BOP.6.1.3 — Signal quality degraded: degraded; C-BOP.6.1.4 — Signal quality reconstruction: reconstruction. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6 — observation_quality | The actual signal_quality. | Preserves its stated standing. | Quality is not hidden. | [V10 §25.1] |

SUB-PARTS: C-BOP.6.1.1 — Signal quality clean; C-BOP.6.1.2 — Signal quality partial; C-BOP.6.1.3 — Signal quality degraded; C-BOP.6.1.4 — Signal quality reconstruction

### C-BOP.6.1.1 — Signal quality clean
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The clean quality value. [V10 §25.1]
- Takes in: DESIGNED — The actual clean classification. [V10 §25.1]
- Does: DESIGNED — Records clean. [V10 §25.1]
- Gives out: DESIGNED — signal_quality = "clean". [V10 §25.1]
- Must never: DESIGNED — Infer interpretive certainty from physical quality. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.1 — signal_quality | The clean value. | Carries the actual classification. | Meaning remains separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.1.2 — Signal quality partial
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The partial quality value. [V10 §25.1]
- Takes in: DESIGNED — The actual partial classification. [V10 §25.1]
- Does: DESIGNED — Records partial. [V10 §25.1]
- Gives out: DESIGNED — signal_quality = "partial". [V10 §25.1]
- Must never: DESIGNED — Conceal missing signal. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.1 — signal_quality | The partial value. | Preserves partial standing. | Missing signal stays visible. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.1.3 — Signal quality degraded
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The degraded quality value. [V10 §25.1]
- Takes in: DESIGNED — The actual degraded classification. [V10 §25.1]
- Does: DESIGNED — Records degraded. [V10 §25.1]
- Gives out: DESIGNED — signal_quality = "degraded". [V10 §25.1]
- Must never: DESIGNED — Present degraded signal as clean. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.1 — signal_quality | The degraded value. | Preserves its quality. | No upgrade is implied. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.1.4 — Signal quality reconstruction
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The reconstruction vocabulary value. [V10 §25.1]
- Takes in: DESIGNED — An observation carrying that actual quality standing. [V10 §25.1]
- Does: DESIGNED — Records reconstruction honestly without inferring a reconstruction procedure. [V10 §25.1]
- Gives out: DESIGNED — signal_quality = "reconstruction". [V10 §25.1]
- Must never: DESIGNED — Reconstruct observations missed before a crash. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.1 — signal_quality | The reconstruction value. | Preserves the source-defined label. | No new recovery mechanism is authorized. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.2 — signal_quality_note
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The signal-quality note, string or null. [V10 §25.1]
- Takes in: DESIGNED — The actual explanatory physical-quality note when present. [V10 §25.1]
- Does: DESIGNED — Preserves signal_quality_note. [V10 §25.1]
- Gives out: DESIGNED — A string or null. [V10 §25.1]
- Must never: DESIGNED — Add meaning or emotion to a physical-quality note. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6 — observation_quality | The quality note or null. | Carries the actual quality context. | No interpretation is smuggled in. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.3 — field_completeness
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The list of field_status records. [V10 §25.1]
- Takes in: DESIGNED — Each field’s actual completeness facts. [V10 §25.1]
- Does: DESIGNED — Carries field_name, status, status_note, fallback_value_used and fallback_basis for each entry. [V10 §25.1]
- Gives out: DESIGNED — A field_completeness list. [V10 §25.1]
- Must never: DESIGNED — Invent a status vocabulary or conceal fallback use. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.6.3.1 — Quality field_name: field_name; C-BOP.6.3.2 — Quality field status: status; C-BOP.6.3.3 — Quality status_note: status_note; C-BOP.6.3.4 — fallback_value_used: fallback_value_used; C-BOP.6.3.5 — fallback_basis: fallback_basis. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6 — observation_quality | The field_status list. | Preserves field-level completeness. | Fallbacks remain traceable. | [V10 §25.1] |

SUB-PARTS: C-BOP.6.3.1 — Quality field_name; C-BOP.6.3.2 — Quality field status; C-BOP.6.3.3 — Quality status_note; C-BOP.6.3.4 — fallback_value_used; C-BOP.6.3.5 — fallback_basis

### C-BOP.6.3.1 — Quality field_name
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The name of the field being described. [V10 §25.1]
- Takes in: DESIGNED — The actual payload field name. [V10 §25.1]
- Does: DESIGNED — Records field_name. [V10 §25.1]
- Gives out: DESIGNED — The named field. [V10 §25.1]
- Must never: DESIGNED — Attribute completeness to another field. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.3 — field_completeness | The actual field name. | Binds the completeness entry. | The affected field is explicit. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.3.2 — Quality field status
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The field’s recorded completeness status. [V10 §25.1]
- Takes in: DESIGNED — The actual status. [V10 §25.1]
- Does: DESIGNED — Carries status without inventing a vocabulary. [V10 §25.1]
- Gives out: DESIGNED — The field status. [V10 §25.1]
- Must never: DESIGNED — Guess missing status values. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.3 — field_completeness | The actual field status. | Preserves its standing. | No completion is fabricated. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.3.3 — Quality status_note
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The note accompanying field status. [V10 §25.1]
- Takes in: DESIGNED — The actual status explanation. [V10 §25.1]
- Does: DESIGNED — Carries status_note. [V10 §25.1]
- Gives out: DESIGNED — The recorded status note. [V10 §25.1]
- Must never: DESIGNED — Conceal a gap through an explanation. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.3 — field_completeness | The status note. | Preserves the completeness explanation. | The entry remains inspectable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.3.4 — fallback_value_used
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The entry describing the fallback value used. [V10 §25.1]
- Takes in: DESIGNED — The actual fallback use. [V10 §25.1]
- Does: DESIGNED — Carries fallback_value_used. [V10 §25.1]
- Gives out: DESIGNED — Recorded fallback use. [V10 §25.1]
- Must never: DESIGNED — Present a fallback as an original measurement. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.3 — field_completeness | The actual fallback value use. | Keeps fallback explicit. | Measurement provenance is not rewritten. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.3.5 — fallback_basis
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The basis recorded for the fallback. [V10 §25.1]
- Takes in: DESIGNED — The actual fallback basis. [V10 §25.1]
- Does: DESIGNED — Carries fallback_basis. [V10 §25.1]
- Gives out: DESIGNED — The fallback’s recorded basis. [V10 §25.1]
- Must never: DESIGNED — Invent a basis for missing data. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.3 — field_completeness | The fallback basis. | Preserves why the fallback exists. | The fallback remains distinguishable. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.4 — overall_completeness
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The overall payload completeness value. [V10 §25.1]
- Takes in: DESIGNED — The actual completeness standing. [V10 §25.1]
- Does: DESIGNED — Uses complete, partial, minimum_viable or below_threshold. [V10 §25.1]
- Gives out: DESIGNED — The exact overall_completeness. [V10 §25.1]
- Must never: DESIGNED — Treat below_threshold as permission to invent missing fields or bypass source protection. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.6.4.1 — Completeness complete: complete; C-BOP.6.4.2 — Completeness partial: partial; C-BOP.6.4.3 — Completeness minimum_viable: minimum_viable; C-BOP.6.4.4 — Completeness below_threshold: below_threshold. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6 — observation_quality | The overall completeness value. | Preserves honest limits. | Low quality alone does not erase a root. | [V10 §25.1] |
| 2 · ACCEPTED | C-ENROLL.9.4 — Allowed observation-completeness check | BOP's actual completeness field. | Supplies canonical field and actual value. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] |

SUB-PARTS: C-BOP.6.4.1 — Completeness complete; C-BOP.6.4.2 — Completeness partial; C-BOP.6.4.3 — Completeness minimum_viable; C-BOP.6.4.4 — Completeness below_threshold

### C-BOP.6.4.1 — Completeness complete
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The complete completeness value. [V10 §25.1]
- Takes in: DESIGNED — The actual complete classification. [V10 §25.1]
- Does: DESIGNED — Records complete. [V10 §25.1]
- Gives out: DESIGNED — overall_completeness = "complete". [V10 §25.1]
- Must never: DESIGNED — Infer interpretive truth from completeness. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.4 — overall_completeness | The complete value. | Preserves recorded completeness. | Meaning remains separately judged. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.4.2 — Completeness partial
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The partial completeness value. [V10 §25.1]
- Takes in: DESIGNED — The actual partial classification. [V10 §25.1]
- Does: DESIGNED — Records partial. [V10 §25.1]
- Gives out: DESIGNED — overall_completeness = "partial". [V10 §25.1]
- Must never: DESIGNED — Conceal missing fields. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.4 — overall_completeness | The partial value. | Preserves incompleteness. | Gaps remain visible. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.4.3 — Completeness minimum_viable
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The minimum_viable completeness value. [V10 §25.1]
- Takes in: DESIGNED — The actual minimum-viable classification. [V10 §25.1]
- Does: DESIGNED — Records minimum_viable. [V10 §25.1]
- Gives out: DESIGNED — overall_completeness = "minimum_viable". [V10 §25.1]
- Must never: DESIGNED — Invent numeric viability thresholds. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.4 — overall_completeness | The minimum_viable value. | Preserves its standing. | No empirical value is supplied. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.6.4.4 — Completeness below_threshold
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The below_threshold completeness value. [V10 §25.1]
- Takes in: DESIGNED — The actual below-threshold classification. [V10 §25.1]
- Does: DESIGNED — Records below_threshold honestly; the root still follows the authorized normal path and the reader may return insufficient_context. [V10 §25.1]
- Gives out: DESIGNED — overall_completeness = "below_threshold". [V10 §25.1]
- Must never: DESIGNED — Discard solely for low completeness, invent data or bypass privacy/ingest holds. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.6.4 — overall_completeness | The below_threshold value. | Preserves the limited observation. | The reader can acknowledge insufficient context. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7 — third_party_flag
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The four-field third-party presence/content/handling/privacy-version object. [V10 §25.1]
- Takes in: DESIGNED — Actual presence and content facts under the applicable privacy rule. [V10 §25.1]
- Does: DESIGNED — Records the booleans, handling value and privacy rule version. [V10 §25.1]
- Gives out: DESIGNED — A third_party_flag object. [V10 §25.1]
- Must never: DESIGNED — Turn mere presence into identity or permission to expose content. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.7.1 — third_party_present: third_party_present; C-BOP.7.2 — third_party_content_present: third_party_content_present; C-BOP.7.3 — third_party_handling: third_party_handling; C-BOP.7.4 — BOP privacy_rule_version: privacy_rule_version. [V10 §25.1]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal retrieval, analysis and identity assessment use internal-use authorization; visible surfacing/export/sharing/notifications use visible-output eligibility and pre-output review, with Level 1/TSC unchanged. [SOURCE CONFLICT: 01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md BOP / Third-Party Flag states unqualified pre-output review; V10 makes its application purpose-specific.] [V10 §25.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The actual third-party handling. | Preserves privacy and no-destruction boundaries. | Presence does not create disclosure authority. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.4 — bop_payload | The third_party_flag object. | Carries the actual handling facts. | Privacy version remains attached. | [V10 §25.1] |
| 3 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The existing third_party_flag and privacy boundary. | Preserves third-party handling unchanged. | Optional notes create no disclosure exception. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: C-BOP.7.1 — third_party_present; C-BOP.7.2 — third_party_content_present; C-BOP.7.3 — third_party_handling; C-BOP.7.4 — BOP privacy_rule_version

### C-BOP.7.1 — third_party_present
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Whether a third party is present, boolean. [V10 §25.1]
- Takes in: DESIGNED — The actual physical presence fact. [V10 §25.1]
- Does: DESIGNED — Records third_party_present. [V10 §25.1]
- Gives out: DESIGNED — A boolean. [V10 §25.1]
- Must never: DESIGNED — Infer person identity from presence. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7 — third_party_flag | The presence boolean. | Preserves the raw fact. | No identity claim follows. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7.2 — third_party_content_present
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — Whether third-party content is present, boolean. [V10 §25.1]
- Takes in: DESIGNED — The actual content-presence fact. [V10 §25.1]
- Does: DESIGNED — Records third_party_content_present. [V10 §25.1]
- Gives out: DESIGNED — A boolean. [V10 §25.1]
- Must never: DESIGNED — Treat presence as access permission. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7 — third_party_flag | The content-presence boolean. | Preserves the actual fact. | Authorization remains separate. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7.3 — third_party_handling
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The exact third-party handling value. [V10 §25.1]
- Takes in: DESIGNED — The actual permitted handling. [V10 §25.1]
- Does: DESIGNED — Uses ness_only, third_party_presence_noted or third_party_content_reference. [V10 §25.1]
- Gives out: DESIGNED — The controlled third_party_handling. [V10 §25.1]
- Must never: DESIGNED — Convert a content reference into a disclosure grant. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.7.3.1 — ness_only: ness_only; C-BOP.7.3.2 — third_party_presence_noted: third_party_presence_noted; C-BOP.7.3.3 — third_party_content_reference: third_party_content_reference. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7 — third_party_flag | The actual handling value. | Preserves how material is represented. | Privacy remains owner-governed. | [V10 §25.1] |

SUB-PARTS: C-BOP.7.3.1 — ness_only; C-BOP.7.3.2 — third_party_presence_noted; C-BOP.7.3.3 — third_party_content_reference

### C-BOP.7.3.1 — ness_only
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The ness_only handling value. [V10 §25.1]
- Takes in: DESIGNED — The actual Ness-only handling. [V10 §25.1]
- Does: DESIGNED — Carries ness_only. [V10 §25.1]
- Gives out: DESIGNED — third_party_handling = "ness_only". [V10 §25.1]
- Must never: DESIGNED — Infer additional identity authority. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7.3 — third_party_handling | The ness_only value. | Preserves actual handling. | No broader permission follows. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7.3.2 — third_party_presence_noted
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The third_party_presence_noted handling value. [V10 §25.1]
- Takes in: DESIGNED — The actual noted third-party presence. [V10 §25.1]
- Does: DESIGNED — Carries third_party_presence_noted. [V10 §25.1]
- Gives out: DESIGNED — The controlled presence-noted value. [V10 §25.1]
- Must never: DESIGNED — Convert noted presence into content disclosure. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7.3 — third_party_handling | The presence-noted value. | Preserves the limited fact. | Content is not inferred. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7.3.3 — third_party_content_reference
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The third_party_content_reference handling value. [V10 §25.1]
- Takes in: DESIGNED — The actual permitted third-party content reference. [V10 §25.1]
- Does: DESIGNED — Carries third_party_content_reference. [V10 §25.1]
- Gives out: DESIGNED — The controlled content-reference value. [V10 §25.1]
- Must never: DESIGNED — Turn reference existence into permission to reveal it. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7.3 — third_party_handling | The content-reference value. | Preserves reference standing. | No access exception is created. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.7.4 — BOP privacy_rule_version
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The privacy-rule-version string applied to the handling. [V10 §25.1]
- Takes in: DESIGNED — The actual applicable rule version. [V10 §25.1]
- Does: DESIGNED — Records privacy_rule_version. [V10 §25.1]
- Gives out: DESIGNED — A string. [V10 §25.1]
- Must never: DESIGNED — Apply or imply an unrelated version. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.7 — third_party_flag | The applicable privacy-rule version. | Keeps handling attributable. | The policy basis is explicit. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.8 — One observation root per simultaneous signal channel
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The reconstructible simultaneous bundle with one root for each signal channel. [V10 §25.1]
- Takes in: DESIGNED — Signals from the same simultaneous moment. [V10 §25.1]
- Does: DESIGNED — Gives each channel its own root; all share simultaneous_bundle_id and carry the recorded bundle position. [V10 §25.1]
- Gives out: DESIGNED — A reconstructible group of single-role roots. [V10 §25.1]
- Must never: DESIGNED — Merge channels into one multi-role root. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.4.12 — simultaneous_bundle_id: shared bundle identity; C-BOP.4.13 — simultaneous_bundle_position: recorded position; C-BOP.3.7 — BOP root role: single-role values. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The simultaneous physical channels. | Captures each separately. | The bundle remains reconstructible without schema change. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The one-root-per-channel simultaneous bundle. | Preserves channel separation. | Acoustic notes add no multi-role root. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-BOP.9 — connection_anchors and later reconnection
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The list of optional anchor_record retrieval aids, which may be empty. [V10 §25.1]
- Takes in: DESIGNED — Any available structural connection anchors. [V10 §25.1]
- Does: DESIGNED — Preserves the list; any root remains reconnectable through condition-based rereads and semantic retrieval even without preregistered anchors. [V10 §25.1]
- Gives out: DESIGNED — Optional connection_anchors and ordinary later reconnection. [V10 §25.1]
- Must never: DESIGNED — Require anchors as a condition of later retrieval or invent their unspecified internal schema. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7H — Reread Lifecycle (§7H): condition-based rereads; C-7F — Context Retrieval (§7F): semantic retrieval. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The optional anchors and later retrieval route. | Keeps every root reconnectable. | Absence of anchors is not a dead end. | [V10 §25.1] |
| 2 · DESIGNED | C-BOP.4 — bop_payload | The optional anchor list. | Carries it even when empty. | No new base-root field is needed. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.10 — Absolute DUMB and text non-inspection boundary
Stamp: DESIGNED    Source: [V10 §25.1] [V10 §26.4]

ALONE
- What it is: DESIGNED — The prohibition on capture-time interpretation. [V10 §25.1] [V10 §26.4]
- Takes in: DESIGNED — A proposed observation field or event classification. [V10 §25.1] [V10 §26.4]
- Does: DESIGNED — Keeps only physically measurable description; interpretation belongs to the Meaning Engine or SIA under their own roles. [V10 §25.1] [V10 §26.4]
- Gives out: DESIGNED — Typed raw evidence without conclusions. [V10 §25.1] [V10 §26.4]
- Must never: DESIGNED — Produce emotional labels, identity conclusions, speaker-change detections, spoofing assessments, meaning attributions, patterns, importance judgments or reasons why; use correction, continuation_request, stop_signal, hesitation_sound, filler or expected/unexpected silence labels; observe unfinished typing. [V10 §25.1] [V10 §26.4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): the enrichment boundary excludes meaning from capture. [V10 §25.1] [V10 §26.4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The physical-versus-meaning boundary. | Rejects interpretive capture content. | All meaning remains separate. | [V10 §25.1] |
| 2 · DESIGNED | C-LEARN.9.2 — Observation and query data remain within their roles | BOP observations, OOP outcomes and LMAC calls. | Supplies full DUMB observation boundary. | Nothing in this card. | [V10 §26.12] |

SUB-PARTS: NONE

### C-BOP.11 — Capture failure and idempotent recovery
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The capture failure, write retry and crash-gap contract. [V10 §25.1]
- Takes in: DESIGNED — Actual capture/write failure or a mid-session crash. [V10 §25.1]
- Does: DESIGNED — Writes honest failure/interruption roots, retries an existing write with the same identity and never reconstructs uncaptured observations. [V10 §25.1]
- Gives out: DESIGNED — Preserved captured truth and explicit gaps. [V10 §25.1]
- Must never: DESIGNED — Invent observations or count a retry as new evidence. [V10 §25.1]
- Fails closed by: DESIGNED — Uncaptured observations stay missing. [V10 §25.1]

TOGETHER
- Fed by: DESIGNED — C-BOP.11.1 — Capture failure observation: capture failure; C-BOP.11.2 — Same-capture write retry: write failure; C-BOP.11.3 — Session-crash restart observation: crash restart. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The actual failure or interruption. | Preserves identity and honest gaps. | No recovery fiction enters memory. | [V10 §25.1] |
| 2 · ACCEPTED | C-BOP.12.4 — Acoustic amendment preserves existing capture rules | The existing capture failure and recovery rules. | Preserves honest gaps and same-ID retry. | The amendment creates no recovery exception. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: C-BOP.11.1 — Capture failure observation; C-BOP.11.2 — Same-capture write retry; C-BOP.11.3 — Session-crash restart observation

### C-BOP.11.1 — Capture failure observation
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The outcome when capture itself fails. [V10 §25.1]
- Takes in: DESIGNED — The actual failure and known gap. [V10 §25.1]
- Does: DESIGNED — Writes capture_failure and records the gap honestly. [V10 §25.1]
- Gives out: DESIGNED — A capture_failure root. [V10 §25.1]
- Must never: DESIGNED — Reconstruct what was not captured. [V10 §25.1]
- Fails closed by: DESIGNED — No missing signal is invented. [V10 §25.1]

TOGETHER
- Fed by: DESIGNED — C-BOP.2.19 — capture_failure: capture_failure event. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.11 — Capture failure and idempotent recovery | The capture failure. | Preserves the honest gap. | Failure becomes recorded truth. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.11.2 — Same-capture write retry
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The retry after capture_id has been computed and writing fails. [V10 §25.1]
- Takes in: DESIGNED — The actual captured observation and its unchanged capture_id. [V10 §25.1]
- Does: DESIGNED — Retries through append_root() using the same identity so duplicate writes are absorbed. [V10 §25.1]
- Gives out: DESIGNED — One root for the capture. [V10 §25.1]
- Must never: DESIGNED — Change the capture ID or bypass the Catalog/writer on retry. [V10 §25.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.5 — Corrected BOP capture_id: stable capture_id; C-7E — Catalog Front Door + pre-ingest holding (§7E): the single entry route. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.11 — Capture failure and idempotent recovery | The failed write and stable capture. | Retries without duplicating identity. | The observation remains one root. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.11.3 — Session-crash restart observation
Stamp: DESIGNED    Source: [V10 §25.1]

ALONE
- What it is: DESIGNED — The restart after a crash during the session. [V10 §25.1]
- Takes in: DESIGNED — The known crash and committed observations. [V10 §25.1]
- Does: DESIGNED — Writes session_interrupted on restart and preserves captured truth. [V10 §25.1]
- Gives out: DESIGNED — An interruption root and an honest uncaptured gap. [V10 §25.1]
- Must never: DESIGNED — Reconstruct observations missed before the crash. [V10 §25.1]
- Fails closed by: DESIGNED — Nothing uncaptured is restored. [V10 §25.1]

TOGETHER
- Fed by: DESIGNED — C-BOP.2.15 — session_interrupted: session_interrupted event. [V10 §25.1]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP.11 — Capture failure and idempotent recovery | The crashed session. | Records interruption on restart. | The gap remains honest. | [V10 §25.1] |

SUB-PARTS: NONE

### C-BOP.12 — Optional acoustic_condition_notes amendment
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted policy/design allowance for an optional list inside voice-channel signal_measurements; no active schema or capture path is created merely by acceptance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — Deterministic measurable recording conditions with complete measurement provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Allows exactly six fields and five controlled condition names; absence of the optional list is normal and means nothing. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Physical recording-condition notes, never conclusions about the person. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Add fields or names, select empirical thresholds/algorithms, widen capture authorization, silently activate a schema, or treat a note as sufficient identity/meaning evidence. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.12.1 — Acoustic condition record: six-field record; C-BOP.12.2 — Five acoustic condition names: five-name vocabulary; C-BOP.12.3 — Bounded acoustic-note downstream context: bounded downstream use; C-BOP.12.4 — Acoustic amendment preserves existing capture rules: preserved capture structure. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The optional physical acoustic notes. | Keeps them within the accepted bounded amendment. | No implementation or capture widening is inferred. | [V10 §25.1] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §2] |
| 2 · DESIGNED | C-BOP.4.11 — signal_measurements | The optional voice-channel note list. | Carries it within measurements. | Base-root structure remains unchanged. | [V10 §25.1] |
| 3 · ACCEPTED | C-ENROLL.5.6 — Enrollment physical-observation consumption | BOP-owned committed observations with stable `capture_id`, durable ordering, observation-quality fields and failure observations. | Supplies the existing six-field record and five controlled physical-condition names. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-SIA.10.1 — Bounded acoustic-condition context | Records with `condition_name`, `detection_method`, `detection_version`, `threshold_value`, `measured_value` and `certainty`. | Supplies the optional physical records. | Nothing in this card. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |

SUB-PARTS: C-BOP.12.1 — Acoustic condition record; C-BOP.12.2 — Five acoustic condition names; C-BOP.12.3 — Bounded acoustic-note downstream context; C-BOP.12.4 — Acoustic amendment preserves existing capture rules

### C-BOP.12.1 — Acoustic condition record
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The exact six-field reproducible condition record. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual condition, method/version, threshold, measured value and physical-classification certainty. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Carries all six fields with no bare labels. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — A checkable deterministic physical classification. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Drop provenance or broaden certainty to identity, speaker, emotion, truth or evidence authority. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.12.1.1 — Acoustic condition_name: condition_name; C-BOP.12.1.2 — Acoustic detection_method: detection_method; C-BOP.12.1.3 — Acoustic detection_version: detection_version; C-BOP.12.1.4 — Acoustic threshold_value: threshold_value; C-BOP.12.1.5 — Acoustic measured_value: measured_value; C-BOP.12.1.6 — Acoustic certainty: certainty. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12 — Optional acoustic_condition_notes amendment | The complete six-field note. | Preserves reproducibility. | A bare label is never sufficient. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: C-BOP.12.1.1 — Acoustic condition_name; C-BOP.12.1.2 — Acoustic detection_method; C-BOP.12.1.3 — Acoustic detection_version; C-BOP.12.1.4 — Acoustic threshold_value; C-BOP.12.1.5 — Acoustic measured_value; C-BOP.12.1.6 — Acoustic certainty

### C-BOP.12.1.1 — Acoustic condition_name
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Which of the five controlled measurable recording conditions the note describes. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual controlled physical condition. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Preserves condition_name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — One accepted condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Add a sixth name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.12.2 — Five acoustic condition names: closed condition vocabulary. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The controlled condition_name. | Identifies the physical condition. | The vocabulary remains closed. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.1.2 — Acoustic detection_method
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The named deterministic method that produced the classification. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual measuring method. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records detection_method. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — The method name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Emit a bare condition without method. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The actual method. | Preserves measurement provenance. | The classification is checkable. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.1.3 — Acoustic detection_version
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The version of the detection method that ran. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual method version. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records detection_version. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — The exact version. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Silently substitute another method version. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The actual detection version. | Preserves reproducibility. | The same tool version remains identifiable. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.1.4 — Acoustic threshold_value
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The line against which the measurement was compared. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual threshold used by the eventual governed method. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records threshold_value without choosing a numeric value here. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — The applied threshold. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Invent a numeric threshold or omit the applied line. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The applied threshold value. | Makes classification reproducible. | No empirical parameter is silently chosen. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.1.5 — Acoustic measured_value
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — What was actually measured on this signal. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual measurement. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records measured_value with the threshold. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — The physical measured value. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Substitute an interpretation for measurement. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The actual measured value. | Preserves the classification basis. | The physical comparison remains checkable. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.1.6 — Acoustic certainty
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Confidence only that the physical condition classification is correct. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The measurement’s actual classification confidence. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records certainty within that physical scope. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — Physical-classification certainty. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Use it as identity, speaker, emotional or truth confidence, or evidence authority. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.1 — Acoustic condition record | The scoped certainty. | Preserves confidence about the measurement alone. | No downstream conclusion is certified. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.12.2 — Five acoustic condition names
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The closed list of five deterministic physical recording-condition names. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — The actual measured recording condition. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Uses only high_ambient_noise, close_microphone, far_microphone, room_reverb_present or signal_compression_heavy. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — One of five accepted condition_name values. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Add names or attach personal/interpretive meaning. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.12.2.1 — high_ambient_noise: high_ambient_noise; C-BOP.12.2.2 — close_microphone: close_microphone; C-BOP.12.2.3 — far_microphone: far_microphone; C-BOP.12.2.4 — room_reverb_present: room_reverb_present; C-BOP.12.2.5 — signal_compression_heavy: signal_compression_heavy. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12 — Optional acoustic_condition_notes amendment | The closed physical vocabulary. | Keeps the note bounded. | No sixth classification is introduced. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-BOP.12.1.1 — Acoustic condition_name | The allowed condition name. | Validates vocabulary membership. | The name remains physical. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: C-BOP.12.2.1 — high_ambient_noise; C-BOP.12.2.2 — close_microphone; C-BOP.12.2.3 — far_microphone; C-BOP.12.2.4 — room_reverb_present; C-BOP.12.2.5 — signal_compression_heavy

### C-BOP.12.2.1 — high_ambient_noise
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The high_ambient_noise recording-condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Its deterministic threshold-and-measurement basis. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Carries high_ambient_noise with complete provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — A physical noise-condition note. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Conclude who spoke or how anyone felt. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.2 — Five acoustic condition names | The high_ambient_noise name. | Preserves physical recording context. | It supplies no identity conclusion. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-BOP.12.2.2 — close_microphone
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The close_microphone recording-condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Its deterministic measurement basis. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Carries close_microphone with complete provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — A physical microphone-condition note. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Infer intent or importance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.2 — Five acoustic condition names | The close_microphone name. | Preserves recording context. | No personal conclusion follows. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-BOP.12.2.3 — far_microphone
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The far_microphone recording-condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Its deterministic measurement basis. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Carries far_microphone with complete provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — A physical microphone-condition note. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Infer speaker identity or meaning. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.2 — Five acoustic condition names | The far_microphone name. | Preserves recording context. | The note remains physical. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-BOP.12.2.4 — room_reverb_present
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The room_reverb_present recording-condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Its deterministic measurement basis. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Carries room_reverb_present with complete provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — A physical reverberation note. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Infer emotion or motive. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.2 — Five acoustic condition names | The room_reverb_present name. | Preserves room-condition evidence. | Meaning remains separate. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-BOP.12.2.5 — signal_compression_heavy
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The signal_compression_heavy recording-condition name. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Its deterministic measurement basis. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Carries signal_compression_heavy with complete provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — A physical compression-condition note. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Treat recording quality as truth or identity authority. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12.2 — Five acoustic condition names | The signal_compression_heavy name. | Preserves signal-condition evidence. | No conclusion is certified. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-BOP.12.3 — Bounded acoustic-note downstream context
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The permitted use of acoustic notes as physical context under each receiver’s own authority, evidence, uncertainty and validation rules. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — The original measurement, method/version, threshold, measured value, certainty scope and source provenance. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Preserves all provenance in every use; Meaning Engine or SIA may weigh the physical context with other evidence while any interpretation remains labeled, uncertain and rejectable. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Bounded physical evidence that remains DUMB even when a SMART or identity component considers it. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Let the note itself assert or suffice alone for identity, speaker change, spoofing, imitation risk, emotion, intent, meaning, importance, patterns or reasons why; silently convert it to interpretation or fact. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): owns meaning under its rules; C-SIA — Speaker Identity Assessment (§25.3): owns identity judgments under its rules. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12 — Optional acoustic_condition_notes amendment | The physical note and full provenance. | Preserves lawful bounded contextual use. | The note never becomes a conclusion by itself. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-SIA.10.1 — Bounded acoustic-condition context | Records with `condition_name`, `detection_method`, `detection_version`, `threshold_value`, `measured_value` and `certainty`. | Supplies the provenance-preserving use boundary. | Nothing in this card. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-BOP.12.4 — Acoustic amendment preserves existing capture rules
Stamp: ACCEPTED    Source: [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The unchanged authorization, root/channel, identity, failure and privacy rules around optional acoustic notes. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The actual authorized BOP capture. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps the seven-field root, one channel per root, simultaneous bundles, durable sequence, same-ID retry, honest failure/crash gaps, quality and third-party handling. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — An optional note within the existing protected capture. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Create a source, capture permission, new root schema or reconstruction path. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.3 — Seven-field BOP root bindings: base bindings; C-BOP.5 — Corrected BOP capture_id: capture identity; C-BOP.6 — observation_quality: quality; C-BOP.7 — third_party_flag: third-party handling; C-BOP.8 — One observation root per simultaneous signal channel: channels; C-BOP.11 — Capture failure and idempotent recovery: failure/recovery. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): unchanged capture/use privacy. [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.12 — Optional acoustic_condition_notes amendment | The unchanged capture protections. | Keeps the amendment bounded. | Optional measurement does not widen authority. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-BOP.13 — Accepted single-path observation ingestion
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The accepted B-INT-3 path for BOP roots into the one shared store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Authorized typed captures with the unchanged legacy subject and stable capture identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Uses exactly Catalog envelope → append_root() in the B11 active batch → standard Meaning Engine readings; no parallel entry or root store exists. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — One committed root per capture and the existing reading path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Write directly to memory, append to the sealed 5,521-root batch, duplicate ingestion paths or guess raw-signal meaning. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Unauthorized sources are refused and recorded; uncertainty does not authorize an append. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: writer/commit protections; C-BOP.13.2 — BOP shared retry and committed-state recovery: bounded retry/recovery; C-BOP.13.3 — Held TSC observation-reference boundary: held TSC observations; C-BOP.13.4 — Observation operation and canonical child links: shared operation record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): the one catalog envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture authorization and prior exact-purpose use authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Changes: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): each committed root enters the existing reading queue. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The authorized observation capture. | Uses the only root-entry path. | No second store or interpretation path is introduced. | [V10 §25.1] |
| 2 · DESIGNED | C-LEARN.3.1 — Learning receives DUMB observation inputs | Authorized BOP events and OOP outcome_observation roots. | Supplies canonical single-writer capture identity/commit/recovery contract. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §26.3] [V10 §26.4] [V10 §26.6] |

SUB-PARTS: C-BOP.13.1 — BOP consumption of B11 writer protections; C-BOP.13.2 — BOP shared retry and committed-state recovery; C-BOP.13.3 — Held TSC observation-reference boundary; C-BOP.13.4 — Observation operation and canonical child links

### C-BOP.13.1 — BOP consumption of B11 writer protections
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The existing B11 contract consumed unchanged for every observation-root append. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — The stable capture, catalog envelope and actual active-batch authority. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Uses canonical selection, one global claim, WB1 ownership generation/reservation/root-ID binding, WB2 append fence, WB3 parent/child identity, coverage-before-writes and existing recovery/refusals. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — The actual committed root outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Reopen the sealed original batch, bypass ownership/fence/coverage or create second parent truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Existing B11 fail-closed refusals stop an unproved or ineligible append. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: full canonical B11 mechanisms and recovery; C-STORE.4.7.2.7 — Append commit fence (WB2 [proposed] entry): append commit fence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | The actual B11 admission and commit result. | Preserves canonical writer authority. | Observation capture cannot bypass the store owner. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-BOP.15.5 — Frozen enrollment capture set and normal entry | The accepted B11 writer protections. | Uses them for each frozen enrollment observation. | No second root path appears. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-ENROLL.15 — Enrollment crash recovery | The real interruption point and authoritative committed owner facts. | Supplies root commitments. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 4 · ACCEPTED | C-ENROLL.8 — Closed-session root and reading handoff | Committed observations and a committed session-close or interruption fact. | Supplies global claim, ownership and fence. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 5 · ACCEPTED | C-ENROLL.6.16 — Roots partially committed state | B11/append truth that some frozen observations have roots and some do not. | Supplies actual append/fence outcomes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 6 · ACCEPTED | C-ENROLL.6.17 — Roots committed state | A verified `root_id` for every frozen observation. | Supplies verified append outcomes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 7 · ACCEPTED | C-ENROLL.8.3 — B11 append interface | `capture_id`-derived identity, validated root fields and B11-owned `ingest_operation_id`. | Supplies the complete existing writer mechanism. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.13.2 — BOP shared retry and committed-state recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The accepted operation spine for observation capture and promotion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Actual technical failure, committed checkpoints and per-item completion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Uses stable identity, atomic state/record commits, structural duplicate prevention and existing B9 classification/values; recovery scans committed state only and records each recovery operation. Completed items stand; unfinished promotion resumes from durable checkpoints. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Bounded retry and honest partial completion without reconstructing observations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Repeat completed effects, invent a lost capture or bypass retry bounds through new identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Terminal failures halt honestly; uncertainty claims no completion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7H.9 — B9 retry-state architecture: B9 failure classes; C-7H.10 — Accepted B9 retry values and episodes: exact counts/waits/deadlines. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | The actual failure and durable state. | Reuses accepted retry/recovery rules. | No empirical retry value is reopened. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-BOP.13.3 — Held TSC observation-reference boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]

ALONE
- What it is: ACCEPTED — The existing TSC connection to BOP captures already held in Catalog pre-ingest. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Takes in: ACCEPTED — The actual preingest_capture_id and TSC lifecycle/blocker state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Does: ACCEPTED — Keeps observations held under pending_fingerprint_authorization; TSC references them without calling BOP. After authorization and promotion they proceed in real event order, with timing links through existing identifiers/metadata rather than added base-root fields. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Gives out: ACCEPTED — Held references or authorized promoted roots through the existing path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Must never: ACCEPTED — Treat authorized observation capture as permission for immediate sealed-store entry or ordinary use, or promote SIA security-audit events as roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Fails closed by: ACCEPTED — Pending fingerprint authorization and other active blockers retain the hold. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]

TOGETHER
- Fed by: DESIGNED — C-TSC.9 — BOP and SIA links: canonical BOP/SIA event-link structures; C-TSC — Temporary Session Cache (§7E-TSC): lifecycle and promotion authority. [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | The held observation and its identifiers. | Preserves the existing TSC boundary. | Capture does not bypass promotion authorization. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |

SUB-PARTS: NONE

### C-BOP.13.4 — Observation operation and canonical child links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — One operational record per capture, promotion or capture failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — The real operation and any link committed as part of capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Commits state and its append-only record atomically; a capture-time link is a canonical child event/field inside that capture transaction, and the parent has exactly one terminal operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — One parent truth with its own child details. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Create a second independent parent log for the same capture or log recursively; a genuinely later relationship operation needs a distinct identity and cannot silently duplicate the capture-time link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7B.10.5.1 — One real operation one log: one real operation one log. [V10 §0B] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fed by: ACCEPTED — C-BOP.14.11 — Capture-time reaction-link transaction: capture-transaction link commit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | The capture’s actual record and child details. | Preserves one logical operation. | Linking adds no duplicate parent truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14 — Bounded imported-voice reaction window
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]

ALONE
- What it is: ACCEPTED — The accepted operation linking raw observations during listening and immediately afterward to the exact imported voice item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Takes in: ACCEPTED — The item’s recorded playback-start during an authorized session and valid finite governed bounds. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Does: ACCEPTED — Keeps two eligible segment types inside one window: active playback and bounded post-playback. Links only actual observations inside a valid eligible segment, with at most one item/segment per observation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Gives out: ACCEPTED — Separate observation roots with an exact structural imported-Origin reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Must never: ACCEPTED — Merge observations with the imported Origin, link paused or post-bound observations, or infer emotion, motive, agreement, causality or meaning. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Fails closed by: ACCEPTED — Linking stays disabled until every required bound and window fact is present, valid and verifiable; ordinary authorized capture continues without a link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.1 — Reaction-window start event: start; C-BOP.14.2 — First-ending-event window closure: first ending event; C-BOP.14.3 — Active playback segment: active segment; C-BOP.14.4 — Paused interval and governed same-item resume: paused interval/resume; C-BOP.14.5 — Bounded post-playback reaction segment: post-playback segment; C-BOP.14.6 — Reaction-window interruption closure: interruption; C-BOP.14.7 — Structural reaction-window overlap prevention: structural overlap prevention; C-BOP.14.8 — Proposed reaction_window_id [proposed]: proposed reaction_window_id; C-BOP.14.9 — Committed-window crash recovery: recovery; C-BOP.14.10 — linked_imported_origin_ref: exact reference; C-BOP.14.11 — Capture-time reaction-link transaction: atomic capture child; C-BOP.14.12 — Reaction-link fail-closed conditions: no-guessed-link failure; C-BOP.14.13 — Imported-reaction raw facts only: permitted raw facts. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12]
- Gated by: ACCEPTED — C-BOP.1.1 — Authorized-session all-signal rule: authorized-session capture remains required. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The bounded exact-item reaction operation. | Links raw observations without interpreting them. | The item and observations remain separate Origins. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-AFFIRM.9 — Raw reaction does not create reading affirmation | Raw voice/text/timing/silence observations, including a permitted linked_imported_origin_ref, and any separate actual reading response. | Supplies full two-segment bounded imported-reaction operation and capture-child link contract. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-OOP.9 — Existing session and imported-reaction interfaces | The actual opened authorized session or exact imported item’s valid reaction window. | Supplies complete canonical A12 reaction operation and child-link transaction. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: C-BOP.14.1 — Reaction-window start event; C-BOP.14.2 — First-ending-event window closure; C-BOP.14.3 — Active playback segment; C-BOP.14.4 — Paused interval and governed same-item resume; C-BOP.14.5 — Bounded post-playback reaction segment; C-BOP.14.6 — Reaction-window interruption closure; C-BOP.14.7 — Structural reaction-window overlap prevention; C-BOP.14.8 — Proposed reaction_window_id [proposed]; C-BOP.14.9 — Committed-window crash recovery; C-BOP.14.10 — linked_imported_origin_ref; C-BOP.14.11 — Capture-time reaction-link transaction; C-BOP.14.12 — Reaction-link fail-closed conditions; C-BOP.14.13 — Imported-reaction raw facts only

### C-BOP.14.1 — Reaction-window start event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The recorded playback-start of the exact imported item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — That event and the imported Origin/capture_id. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Binds the exact item into the window identity when opening. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — One item-bound window and active playback segment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Open from guessed playback or a missing start record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Missing start-event record permits no reaction link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.8 — Proposed reaction_window_id [proposed]: deterministic proposed reaction_window_id. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The committed playback-start identity. | Opens the exact item’s window. | Replay cannot create another window. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.3 — Active playback segment | The actual playback-start event. | Opens the active segment. | No start is guessed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.2 — First-ending-event window closure
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The four ending events, of which the earliest closes the window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — A post-playback expiry, different-item start, session end or explicit close. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes on whichever occurs first. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A bounded closed window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Leave an unbounded immediately-afterward interval or overlap windows for different items. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.2.1 — Finite post-playback-bound expiry: post-playback expiry; C-BOP.14.2.2 — Different-item playback start closes prior window: item switch; C-BOP.14.2.3 — Session-end reaction closure: session end; C-BOP.14.2.4 — Explicit reaction-window close: explicit close. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The earliest end event. | Closes the window immediately. | Later observations cannot be attributed to it. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.3 — Active playback segment | The first applicable ending event. | Closes the eligible segment. | No later observation is linked. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.5 — Bounded post-playback reaction segment | The first applicable ending event. | Closes the eligible segment. | No later observation is linked. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: C-BOP.14.2.1 — Finite post-playback-bound expiry; C-BOP.14.2.2 — Different-item playback start closes prior window; C-BOP.14.2.3 — Session-end reaction closure; C-BOP.14.2.4 — Explicit reaction-window close

### C-BOP.14.2.1 — Finite post-playback-bound expiry
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The finite governed duration after the final recorded playback-end. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The required valid finite post-playback setting and actual final playback end. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes the window when the bound elapses. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — An expired closed window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Use a missing/non-finite value, choose an empirical duration here or link observations after expiry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Missing, invalid or non-finite bound disables linking. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14.2 — First-ending-event window closure | The post-playback expiry. | Closes at the finite bound. | Nothing after the bound is linked. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.5 — Bounded post-playback reaction segment | The valid finite post-playback bound. | Limits the post-playback segment. | No unbounded aftermath is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.2.2 — Different-item playback start closes prior window
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The recorded start of another imported item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The new item’s actual playback-start. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes the old window at that instant before a new item’s window may open. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A nonoverlapping item switch. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Attribute one observation to two imported items. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14.2 — First-ending-event window closure | The different-item start. | Closes the previous window first. | Windows cannot overlap. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.2.3 — Session-end reaction closure
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The actual session-end event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The recorded session ending. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes the reaction window at that event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A closed session-bounded window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Continue linking after session end. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14.2 — First-ending-event window closure | The actual session end. | Closes the window. | No later session signal is linked. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.2.4 — Explicit reaction-window close
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The explicit window-close event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The actual close event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes the window immediately. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — An explicitly closed window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Continue linking after explicit close. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14.2 — First-ending-event window closure | The explicit close. | Ends the window. | Closure is honored. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.3 — Active playback segment
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The eligible segment while the exact item is actively playing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Recorded playback-start or a valid same-item resume. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Opens at start/resume; immediately suspends linking on pause and closes the segment on pause, playback end, item switch, session end, explicit close or interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Only observations physically inside active playback are eligible for an item link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Link paused observations or infer meaning from being temporally adjacent. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.1 — Reaction-window start event: actual start; C-BOP.14.4 — Paused interval and governed same-item resume: bounded same-item resume; C-BOP.14.2 — First-ending-event window closure: ending events; C-BOP.14.6 — Reaction-window interruption closure: interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The actual active playback interval. | Admits observations only inside that eligible segment. | Playback timing never implies causality. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.10 — linked_imported_origin_ref | The valid active playback segment. | Allows its observations to carry the exact item reference. | Paused time remains ineligible. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.4 — Paused interval and governed same-item resume
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The suspension of linking during pause and the finite rule for a later same-item resume. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Actual pause/resume events and a valid finite maximum-pause setting. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Captures authorized paused observations normally without linked_imported_origin_ref. A valid same-item resume may open a new active segment under the same operation only within the finite governed pause rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Unlinked paused observations or a new eligible active segment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Retroactively link paused observations or resume under a missing/invalid/expired pause bound. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Missing, invalid or expired pause bound closes the window fail-closed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The actual pause or bounded resume. | Keeps paused time ineligible. | Only a valid resume reopens an active segment. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.3 — Active playback segment | The valid finite same-item resume. | Opens a new active segment only within that rule. | A missing or expired bound closes the window. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.5 — Bounded post-playback reaction segment
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The second eligible segment immediately after final committed playback end. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The final committed playback-end and valid finite configured bound. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Opens at that event and remains eligible only until expiry; closes immediately on different-item start, session end, explicit close, interruption or expiry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A bounded post-playback interval in which raw observations may link to the exact item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Omit this accepted second segment, allow an unbounded interval or create it without a valid finite setting. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — No valid finite bound means no post-playback segment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.2.1 — Finite post-playback-bound expiry: finite post-playback bound; C-BOP.14.2 — First-ending-event window closure: first ending event; C-BOP.14.6 — Reaction-window interruption closure: interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The valid post-playback segment. | Allows only observations inside its finite interval. | Immediately afterward remains bounded. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.10 — linked_imported_origin_ref | The valid bounded post-playback segment. | Allows observations only until its actual bound. | Nothing after expiry is attributed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.6 — Reaction-window interruption closure
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The closure on crash or capture interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The last committed observation and actual interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Closes the window honestly at that observation and records session_interrupted or capture_failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A closed interrupted window with committed links preserved. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Back-attribute anything after the gap or reconstruct missed observations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Nothing after the interruption gap is linked to the old window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: DESIGNED — C-BOP.2.15 — session_interrupted: session_interrupted; C-BOP.2.19 — capture_failure: capture_failure. [V10 §25.1] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The actual interruption and last committed observation. | Closes without guessing later capture. | The gap remains honest. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.3 — Active playback segment | The actual interruption at the last committed observation. | Closes the segment honestly. | No post-gap observation is back-attributed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.5 — Bounded post-playback reaction segment | The actual interruption at the last committed observation. | Closes the segment honestly. | No post-gap observation is back-attributed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.7 — Structural reaction-window overlap prevention
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — At most one open reaction window per session, one eligible segment and one imported item per observation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The existing window identity and proposed link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Enforces uniqueness structurally; a switch closes the old window before opening the next. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — At most one linked_imported_origin_ref on an observation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Overlap different-item windows or assign an observation twice. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.8 — Proposed reaction_window_id [proposed]: unique window identity; C-BOP.14.10 — linked_imported_origin_ref: one exact imported reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The candidate observation and current window. | Prevents overlap and multiple attribution structurally. | Temporal links remain unambiguous. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.8 — Proposed reaction_window_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The proposed deterministic window identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Session ID, exact imported Origin reference and recorded playback-start event ID. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Uses proposed reaction_window_id = session id + imported origin ref + recorded playback-start event id; recognizes and records a duplicate open instead of opening another window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — One unique window identity per playback. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Mint a second identity for a replay or guess a missing start event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Unverifiable identity/window state permits no link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The deterministic proposed reaction_window_id. | Keeps window operations idempotent. | Replay cannot create another window. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.1 — Reaction-window start event | The deterministic proposed reaction_window_id. | Keeps one window per recorded playback. | Duplicate opens are absorbed and recorded. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.7 — Structural reaction-window overlap prevention | The deterministic proposed reaction_window_id. | Keeps one window per recorded playback. | Duplicate opens are absorbed and recorded. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.9 — Committed-window crash recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The restart rule for recorded reaction windows and observations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Committed window records and committed observation/link records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Trusts only those records; closes any open window as interrupted and leaves already committed links intact. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Preserved committed truth and no resumed old window. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Re-attribute observations, recreate a missed window or infer uncommitted state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Open-at-restart windows close interrupted; no link is guessed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The committed state on restart. | Closes interrupted work without re-attribution. | Existing links stand and gaps remain gaps. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.10 — linked_imported_origin_ref
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The explicit structural relationship to the exact imported item’s root/capture_id. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — An observation captured inside one valid active or bounded post-playback segment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Carries linked_imported_origin_ref only for that exact eligible item, at most once; imported item and reaction root remain separate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A structural observed-while-listening link, including the accepted bounded post-playback scope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Merge Origins, link paused/post-bound signals, or infer emotion, motive, agreement, causality or meaning. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — No valid eligible segment means no reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.3 — Active playback segment: active segment; C-BOP.14.5 — Bounded post-playback reaction segment: post-playback segment; C-BOP.14.12 — Reaction-link fail-closed conditions: no guessed links. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The eligible observation and exact item reference. | Links without merging. | Later interpretation remains separate evidence-bound work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.11 — Capture-time reaction-link transaction | The one eligible exact-item reference. | Preserves it as a unique structural capture link. | No second item or duplicate parent truth is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-BOP.14.7 — Structural reaction-window overlap prevention | The one eligible exact-item reference. | Preserves it as a unique structural capture link. | No second item or duplicate parent truth is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.11 — Capture-time reaction-link transaction
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The atomic link commit inside the observation-capture transaction. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The eligible linked_imported_origin_ref established at capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Records it as an append-only canonical child event or field inside the same capture operation; keeps exactly one terminal parent operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — A captured observation with its own canonical child link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Create a second independent parent log for the same capture; silently duplicate this link through a later relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.14.10 — linked_imported_origin_ref: the actual eligible relationship reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The capture-time imported-item link. | Commits it within the capture transaction. | Linking does not multiply parent truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.13.4 — Observation operation and canonical child links | The canonical capture child link. | Keeps it inside the one parent record. | No independent duplicate operation appears. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.12 — Reaction-link fail-closed conditions
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The no-link outcome when a required window fact or bound is not valid. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Missing/invalid/non-finite post-playback bound, missing start-event record, unverifiable window state, or invalid/missing/expired pause bound. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps linking disabled until every required bound is present and valid; otherwise permitted A10 observations still capture normally without linked_imported_origin_ref. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Ordinary authorized observations with no guessed link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Guess the link, use unbounded afterward, or stop honest ordinary capture merely because the reaction link is unavailable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — No valid bounded window means no reaction reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The invalid or missing bound/window fact. | Refuses only the unproved link. | Ordinary authorized observation stays intact. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-BOP.14.10 — linked_imported_origin_ref | The required valid bounded window. | Refuses an unproved link. | Ordinary authorized capture continues unlinked. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.14.13 — Imported-reaction raw facts only
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The permitted raw reaction facts: timing, silence, interruption, stopping, resuming, speaking immediately afterward and permitted voice measurements. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Those actual physical observations during eligible windows. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Preserves raw facts connected to the item; later meaning is separate Meaning Engine evidence-bound work. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Separate roots and structural relationships. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Conclude upset, agreement, relief, motive or causality from raw temporal association. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.14 — Bounded imported-voice reaction window | The permitted physical reaction facts. | Preserves them without interpretation. | The linked item is not declared a cause. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-BOP.15 — Enrollment and biometric observation interfaces
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The accepted BOP side of enrollment and BAI observation exchange. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The authorized physical stream from B29 and BAI’s own permitted command facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Owns only DUMB records, capture identity, durable ordering, quality, failures and idempotent observation truth; the enrollment coordinator owns neither these facts nor the microphone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Committed observation references for the frozen enrollment set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Own microphone activation/cleanup/transport, decide identity/spoofing/profile membership, or copy raw voice into coordinator records or ordinary logs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Unsafe or excluded capture does not proceed; absence of an observation alone never proves capture did not start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: capture owner split; C-BOP.15.2 — Enrollment observation provenance: enrollment provenance; C-BOP.15.3 — Biometric system-command and security-audit separation: biometric command boundary; C-BOP.15.4 — Single enrollment biometric success observation: one enrollment success command; C-BOP.15.5 — Frozen enrollment capture set and normal entry: frozen-set/normal root entry; C-BOP.15.6 — Protected raw-voice boundary: protected raw voice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion before capture and protected handling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The authorized enrollment stream and BAI facts. | Preserves the BOP owner boundary. | Observation does not become security authority. | [V10 §25.1] |

SUB-PARTS: C-BOP.15.1 — B29 capture and BOP observation ownership; C-BOP.15.2 — Enrollment observation provenance; C-BOP.15.3 — Biometric system-command and security-audit separation; C-BOP.15.4 — Single enrollment biometric success observation; C-BOP.15.5 — Frozen enrollment capture set and normal entry; C-BOP.15.6 — Protected raw-voice boundary

### C-BOP.15.1 — B29 capture and BOP observation ownership
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — The interface from the voice-pipeline owner to BOP. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Only the authorized physical observation stream. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — B29 owns microphone activation/deactivation, device interaction, cleanup/transport and physical start/stop results; BOP returns committed physical observations with stable capture_id. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Idempotent committed observations, not an independent capture-control result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Infer never-started from absent observations, fabricate B29 truth or automatically reopen the microphone after restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Unknown physical start remains unknown; committed observations stand and gaps are recorded honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the voice pipeline’s actual authorized stream and physical start/stop facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The authorized stream from B29. | Creates observation truth under its own scope. | Control and observation facts remain distinct. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.7.8 — Application or machine restart safety change | Committed opening, intent/start records and actual BOP commits. | Supplies actual committed observations. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 3 · ACCEPTED | C-ENROLL.15 — Enrollment crash recovery | The real interruption point and authoritative committed owner facts. | Supplies real observation commits. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 4 · ACCEPTED | C-ENROLL.5.6 — Enrollment physical-observation consumption | BOP-owned committed observations with stable `capture_id`, durable ordering, observation-quality fields and failure observations. | Supplies committed stream truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-ENROLL.15.10 — Recovery after observations before close | The actual committed observation set. | Supplies committed observations. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 6 · DESIGNED | C-9.2.1 — Microphone capture stage | Physical microphone input. | Takes this place's change: supplies the stream and actual physical start/stop result without moving observation ownership. | Supplies the stream and actual physical start/stop result without moving observation ownership. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [V10 §9] |
| 7 · ACCEPTED | C-ENROLL.5 — Capture-control and observation boundary | Current open truth, privacy permission, trusted-phone/security validity and no cancellation/stop condition. | Supplies actual observed truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 8 · ACCEPTED | C-9.2.8 — B29 enrollment capture interface | Only enrollment_operation_ref [proposed], enrollment_session_ref [proposed], current committed session-open reference, current privacy/capture-eligibility reference, enrollment provenance references (role/source_title/authorization_type), destination BOP context and current cancellation/stop references. | Takes this place's change: hands over the authorized stream while preserving observation ownership. | Hands over the authorized stream while preserving observation ownership. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 9 · ACCEPTED | C-ENROLL.15.9 — Recovery during confirmed capture | Whatever BOP actually committed. | Supplies actual durable observations and failure truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 10 · ACCEPTED | C-ENROLL.8.1 — Frozen enrollment capture-set record | Committed BOP observations under I6 and committed closure/interruption. | Supplies committed physical truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 11 · ACCEPTED | C-ENROLL.5.3.6 — Capture destination observation context | The authorized observation destination by reference. | Supplies the actual observation receiver. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.15.2 — Enrollment observation provenance
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The three fixed enrollment bindings with declared-attribution standing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The actual authorized enrollment session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries role="ness", source_title="enrollment:ness:<session_id>" and session_authorization.authorization_type="enrollment_declared". [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Enrollment provenance that signals declaration, not SIA confirmation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Conclude the speaker is Ness from the role, source title, biometric event or declaration alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BOP.3.7.1 — BOP role ness: role ness with declared standing; C-BOP.3.6 — BOP root source_title: source_title session grouping; C-BOP.4.9.1.3 — enrollment_declared: enrollment_declared meaning. [V10 §25.11 / BOP Integration] [V10 §25.12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The three enrollment provenance bindings. | Preserves declaration without upgrading identity. | SIA keeps identity authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-ENROLL.5.3.5 — Capture declared-provenance references | `role="ness"`, `source_title="enrollment:ness:<session_id>"` and `session_authorization.authorization_type="enrollment_declared"`. | Supplies canonical provenance bindings and field owners. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-ENROLL.5.6 — Enrollment physical-observation consumption | BOP-owned committed observations with stable `capture_id`, durable ordering, observation-quality fields and failure observations. | Supplies declared attribution. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-ENROLL.8.2 — Catalog submission interface | `{ frozen capture_ids, provenance }` after committed close/interruption. | Supplies canonical declared provenance fields. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.15.3 — Biometric system-command and security-audit separation
Stamp: ACCEPTED    Source: [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The narrow BOP biometric-command observation, separate from BAI’s security audit. [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Only prompt_opened, result:success, result:failure, result:cancelled, result:timeout, result:lockout or result:error as defined interface facts. [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Records the physical command with session_id and N.H local-clock timestamp only; purpose/challenge/token/lease/requester and security consequences remain in security audit. [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A minimal system_command root. [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Carry token_id, challenge, purpose, biometric data, authorization conclusions or a claim of identified Ness. [V10 §25.6 / BOP vs. Security Audit Separation] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): its own actual command facts; C-BOP.2.12 — system_command: deterministic system-command event.; C-BOP.15.3.3 — Biometric prompt_opened observation: prompt_opened; C-BOP.15.3.4 — Biometric result:success observation: result:success; C-BOP.15.3.5 — Biometric result:failure observation: result:failure; C-BOP.15.3.6 — Biometric result:cancelled observation: result:cancelled; C-BOP.15.3.7 — Biometric result:timeout observation: result:timeout; C-BOP.15.3.8 — Biometric result:lockout observation: result:lockout; C-BOP.15.3.9 — Biometric result:error observation: result:error. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fed by: ACCEPTED — C-BOP.15.3.1 — Biometric command session ID: safe session field; C-BOP.15.3.2 — Biometric command trusted-local timestamp: safe local timestamp. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The permitted BAI physical command. | Records only safe minimal facts. | Security authority stays outside the BOP root. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [V10 §25.6 / BOP vs. Security Audit Separation] |
| 2 · DESIGNED | C-BAI — Biometric Authorization Interface (§25.6) | An OS result and the single locally prepared pending record with a declared purpose and requester. | Takes this place's change: receives only physical prompt/result facts with session identity and trusted local time. | Receives only physical prompt/result facts with session identity and trusted local time. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · DESIGNED | C-BAI.13 — Physical-command and security-audit separation | Biometric prompt/results and local security operations. | Takes this place's change: receives only the permitted physical-command fact. | Receives only the permitted physical-command fact. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · DESIGNED | C-BAI.13.1 — Permitted biometric physical facts | The actual prompt/result fact, `session_id` and N.H local-clock timestamp. | Takes this place's change: records the physical command without security conclusions. | Records the physical command without security conclusions. | [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: C-BOP.15.3.1 — Biometric command session ID; C-BOP.15.3.2 — Biometric command trusted-local timestamp; C-BOP.15.3.3 — Biometric prompt_opened observation; C-BOP.15.3.4 — Biometric result:success observation; C-BOP.15.3.5 — Biometric result:failure observation; C-BOP.15.3.6 — Biometric result:cancelled observation; C-BOP.15.3.7 — Biometric result:timeout observation; C-BOP.15.3.8 — Biometric result:lockout observation; C-BOP.15.3.9 — Biometric result:error observation

### C-BOP.15.3.1 — Biometric command session ID
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The session ID in the safe biometric command payload. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual command’s session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Preserves that identity only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — The session ID field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Copy a token identity or purpose into it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual session ID. | Keeps command provenance minimal. | No security-secret field is introduced. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-BOP.15.4 — Single enrollment biometric success observation | The actual session ID. | Carries the safe command field. | No token identity is added. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.15.3.2 — Biometric command trusted-local timestamp
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The N.H trusted-local timestamp in the safe command payload. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual local-clock event time. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Preserves that timestamp. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — The local timestamp field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Infer identity or authorization conclusions from the time. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual trusted-local timestamp. | Preserves event timing. | The payload remains a physical record. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-BOP.15.4 — Single enrollment biometric success observation | The trusted-local event timestamp. | Carries the safe timing field. | The command remains a physical fact. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.15.3.3 — Biometric prompt_opened observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical prompt_opened interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI prompt opening. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records prompt_opened with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A prompt-opened observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Assert authorization or identity. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual prompt_opened fact. | Records the physical command only. | No security consequence enters the root. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.4 — Biometric result:success observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:success interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI success result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:success with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A success-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Conclude that Ness was identified or an action authorized. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual success-result fact. | Records the physical command only. | Authorization remains in security audit. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.5 — Biometric result:failure observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:failure interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI failure result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:failure with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A failure-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Copy biometric data or security-policy conclusions. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual failure-result fact. | Records the physical command only. | The safe boundary remains intact. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.6 — Biometric result:cancelled observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:cancelled interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI cancellation result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:cancelled with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A cancelled-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Infer the reason for cancellation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual cancelled-result fact. | Records the physical command only. | No motive is inferred. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.7 — Biometric result:timeout observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:timeout interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI timeout result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:timeout with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A timeout-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Infer identity or intent from timeout. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual timeout-result fact. | Records the physical command only. | Security decisions remain separate. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.8 — Biometric result:lockout observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:lockout interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI lockout result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:lockout with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — A lockout-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Copy lockout authority or policy consequences into the root. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual lockout-result fact. | Records the physical command only. | The root does not become security state. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.3.9 — Biometric result:error observation
Stamp: DESIGNED    Source: [V10 §25.6 / BOP vs. Security Audit Separation]

ALONE
- What it is: DESIGNED — The physical result:error interface fact. [V10 §25.6 / BOP vs. Security Audit Separation]
- Takes in: DESIGNED — The actual BAI error result. [V10 §25.6 / BOP vs. Security Audit Separation]
- Does: DESIGNED — Records result:error with the safe minimal payload. [V10 §25.6 / BOP vs. Security Audit Separation]
- Gives out: DESIGNED — An error-result observation. [V10 §25.6 / BOP vs. Security Audit Separation]
- Must never: DESIGNED — Log potentially biometric fields or invent the error’s meaning. [V10 §25.6 / BOP vs. Security Audit Separation]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15.3 — Biometric system-command and security-audit separation | The actual error-result fact. | Records the physical command only. | Protected details stay outside the root. | [V10 §25.6 / BOP vs. Security Audit Separation] |

SUB-PARTS: NONE

### C-BOP.15.4 — Single enrollment biometric success observation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The one BAI-sourced system_command at committed enrollment-session opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The session-open truth referencing BAI’s durable consumed-token proof and the command identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Stages exactly one command_identifier="biometric:result:success" with session ID and trusted-local timestamp; deterministic capture identity derives from session id, command identifier and the single session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — One idempotent BAI physical fact passed to BOP. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Let the enrollment coordinator fabricate or become the source, carry purpose/token/biometric fields, claim identified Ness or duplicate the command during recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Without the actual committed opening/BAI fact, no success observation is fabricated. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.3.1 — Biometric command session ID: safe session field; C-BOP.15.3.2 — Biometric command trusted-local timestamp: safe timestamp. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): actual source and durable consumed-token proof; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): actual committed session-open truth, timing coordination only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The actual BAI command at committed opening. | Records it once under stable capture identity. | Coordination never becomes biometric evidence. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.4.4 — Proof-bound session-open commit | A flushed `bai_token_consumed` bound to this operation and prospective session. | Takes this place's change: permits timing coordination after actual opening, with BAI as sole source. | Permits timing coordination after actual opening, with BAI as sole source. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.5.7 — Enrollment biometric-observation timing | The committed session opening referencing durable consumed-token proof. | Supplies idempotent physical receiver. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-BAI.19.6 — BAI-owned enrollment success observation | The actual session-open truth and command identity. | Takes this place's change: receives the one stable BAI-sourced command fact. | Receives the one stable BAI-sourced command fact. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-ENROLL.15.7 — Recovery before the biometric system-command observation | Actual `enrollment_session_opened` truth referencing durable BAI proof. | Supplies deterministic receiver identity. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-BOP.15.5 — Frozen enrollment capture set and normal entry
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The immutable set of actually captured observation references after the enrollment session ends. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Takes in: ACCEPTED — Committed observations and the close/interruption fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Does: ACCEPTED — After capture stops and close/interruption commits, the coordinator freezes the reference set; nothing is added afterward. Each observation then follows Catalog→B11 append→verified root_id→standard reading queue→quarantine, preserving capture_id end to end. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gives out: ACCEPTED — Preserved roots and quarantined readings; no extra staging/root/profile store or reading queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Submit enrollment roots before session end, append to the old sealed batch, or destroy an observation because its segment is rejected from profile training. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Capture exclusion still has its own privacy effect; profile rejection alone is not deletion, hiding or destruction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: full existing B11 writer protections. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): owns close/freeze and later profile eligibility; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy exclusion remains distinct. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Changes: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed roots enter its standard queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Changes: ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: readings remain in the quarantine/promote boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The frozen committed observation references. | Preserves all valid captured truth through normal entry. | Rejected training segments remain observations. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-ENROLL.8 — Closed-session root and reading handoff | Committed observations and a committed session-close or interruption fact. | Supplies actual observation references and standard path. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-BOP.15.6 — Protected raw-voice boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The minimum necessary protected B29/BOP interface for raw voice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Takes in: ACCEPTED — Privacy-permitted raw voice inside its proper capture boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Does: ACCEPTED — Checks capture exclusion before capture; keeps raw voice inside the protected boundary and carries only references/structural facts into coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Gives out: ACCEPTED — Protected observations without raw voice in coordinator records, ordinary logs or failure notices. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Must never: ACCEPTED — Expose reconstructive descriptions, hand sensitive content to ordinary components merely to reject it, or indirectly reveal hidden/protected material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Excluded or protected material follows the actual privacy owner’s handling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture-first exclusion and protected handling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-BOP.15 — Enrollment and biometric observation interfaces | The privacy-governed raw-voice stream. | Keeps crossing minimal and protected. | Observation creates no content exposure. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-ENROLL.5.6 — Enrollment physical-observation consumption | BOP-owned committed observations with stable `capture_id`, durable ordering, observation-quality fields and failure observations. | Gates this place: minimum necessary protected interface and no raw voice in coordination. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| 3 · ACCEPTED | C-ENROLL.12 — Enrollment authority and privacy limits | Enrollment provenance, references, provisional profile evidence and status/failure output. | Gates this place: protected interface and no raw voice in coordination. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-9.2.9 — Protected voice boundary | Authorized raw voice inside the capture boundary. | Supplies what this place relies on: canonical observation-side protection remains unchanged. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-BOP.16 — Shared observation logging and protected access
Stamp: DESIGNED    Source: [MAP C-BOP] [V10 §0B]

ALONE
- What it is: DESIGNED — The shared operational trace of observation capture and failures. [MAP C-BOP] [V10 §0B]
- Takes in: DESIGNED — Each captured observation, capture_failure and session_interrupted with known gaps. [MAP C-BOP] [V10 §0B]
- Does: DESIGNED — Records actual events honestly in shared memory; one real operation has one log and logging does not recursively log itself. [MAP C-BOP] [V10 §0B]
- Gives out: DESIGNED — Protected append-only observation/failure history. [MAP C-BOP] [V10 §0B]
- Must never: DESIGNED — Create a private BOP store, reconstruct gaps, use logs as truth for their own subject or add evidence weight through repetition. [MAP C-BOP] [V10 §0B]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7B.10.5.1 — One real operation one log: canonical one-operation/one-log law. [MAP C-BOP] [V10 §0B]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record access and purpose-specific authorization; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization. [MAP C-BOP] [V10 §0B]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | The actual observation operation and failure gaps. | Preserves one honest protected trace. | Logging adds no meaning authority. | [V10 §25.1] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-BOP — Behavioral Observation Processing (§25.1/§26) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusions and exact-purpose internal/visible authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): capture/ingest gate and held-material boundary. | [V10 §25.1] [V10 §7E] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | Gated by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusions and exact-purpose internal/visible authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): capture/ingest gate and held-material boundary. | [V10 §25.1] [V10 §7E] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | Changes | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): typed captures enter the existing Catalog; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): observations become evidence for separate interpretation. | [V10 §25.1] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | Changes | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): typed captures enter the existing Catalog; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): observations become evidence for separate interpretation. | [V10 §25.1] |
| C-BOP.1 — Authorized physical-observation boundary | Gated by | C-7E.1.1 — Raw-capture gate | DESIGNED | C-7E.1.1 — Raw-capture gate: actual raw-capture gate; C-7Q.4 — Two-layer capture exclusion: capture-exclusion owner. | [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.1 — Authorized physical-observation boundary | Gated by | C-7Q.4 — Two-layer capture exclusion | DESIGNED | C-7E.1.1 — Raw-capture gate: actual raw-capture gate; C-7Q.4 — Two-layer capture exclusion: capture-exclusion owner. | [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.1.1 — Authorized-session all-signal rule | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy still governs capture and use. | [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] |
| C-BOP.2.6 — voice_interrupt_of_nh | Fed by | C-OOP — Outcome Observation Processing (§26) | DESIGNED | C-OOP — Outcome Observation Processing (§26): the voice-priority occurrence during function execution; C-BOP.2.6.1 — Voice-interruption timestamp: timestamp; C-BOP.2.6.2 — Voice-interruption output-stream position: output position. | [V10 §25.1] [V10 §26.4] [MAP C-BOP] |
| C-BOP.3 — Seven-field BOP root bindings | Fed by | C-STORE.2 — Seven-field root schema v1 | BUILT | C-STORE.2 — Seven-field root schema v1: canonical unchanged seven-field root schema. | [V10 §6A] [V10 §25.1] |
| C-BOP.6 — observation_quality | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and use still require applicable authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): held/ingestion gates still apply. | [V10 §25.1] |
| C-BOP.6 — observation_quality | Gated by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and use still require applicable authorization; C-7E — Catalog Front Door + pre-ingest holding (§7E): held/ingestion gates still apply. | [V10 §25.1] |
| C-BOP.7 — third_party_flag | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal retrieval, analysis and identity assessment use internal-use authorization; visible surfacing/export/sharing/notifications use visible-output eligibility and pre-output review, with Level 1/TSC unchanged. [SOURCE CONFLICT: 01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md BOP / Third-Party Flag states unqualified pre-output review; V10 makes its application purpose-specific.] | [V10 §25.1] |
| C-BOP.9 — connection_anchors and later reconnection | Fed by | C-7H — Reread Lifecycle (§7H) | DESIGNED | C-7H — Reread Lifecycle (§7H): condition-based rereads; C-7F — Context Retrieval (§7F): semantic retrieval. | [V10 §25.1] |
| C-BOP.9 — connection_anchors and later reconnection | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7H — Reread Lifecycle (§7H): condition-based rereads; C-7F — Context Retrieval (§7F): semantic retrieval. | [V10 §25.1] |
| C-BOP.10 — Absolute DUMB and text non-inspection boundary | Gated by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): the enrichment boundary excludes meaning from capture. | [V10 §25.1] [V10 §26.4] |
| C-BOP.11.2 — Same-capture write retry | Fed by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-BOP.5 — Corrected BOP capture_id: stable capture_id; C-7E — Catalog Front Door + pre-ingest holding (§7E): the single entry route. | [V10 §25.1] |
| C-BOP.12.3 — Bounded acoustic-note downstream context | Gated by | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): owns meaning under its rules; C-SIA — Speaker Identity Assessment (§25.3): owns identity judgments under its rules. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |
| C-BOP.12.3 — Bounded acoustic-note downstream context | Gated by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): owns meaning under its rules; C-SIA — Speaker Identity Assessment (§25.3): owns identity judgments under its rules. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §5] |
| C-BOP.12.4 — Acoustic amendment preserves existing capture rules | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): unchanged capture/use privacy. | [04/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md §4] |
| C-BOP.13 — Accepted single-path observation ingestion | Gated by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): the one catalog envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture authorization and prior exact-purpose use authorization. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.13 — Accepted single-path observation ingestion | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): the one catalog envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture authorization and prior exact-purpose use authorization. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.13 — Accepted single-path observation ingestion | Changes | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): each committed root enters the existing reading queue. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| C-BOP.13.1 — BOP consumption of B11 writer protections | Fed by | C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture | ACCEPTED | C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: full canonical B11 mechanisms and recovery; C-STORE.4.7.2.7 — Append commit fence (WB2 [proposed] entry): append commit fence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-BOP.13.1 — BOP consumption of B11 writer protections | Fed by | C-STORE.4.7.2.7 — Append commit fence (WB2 [proposed] entry) | ACCEPTED | C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: full canonical B11 mechanisms and recovery; C-STORE.4.7.2.7 — Append commit fence (WB2 [proposed] entry): append commit fence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-BOP.13.2 — BOP shared retry and committed-state recovery | Fed by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7H.9 — B9 retry-state architecture: B9 failure classes; C-7H.10 — Accepted B9 retry values and episodes: exact counts/waits/deadlines. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.13.2 — BOP shared retry and committed-state recovery | Fed by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7H.9 — B9 retry-state architecture: B9 failure classes; C-7H.10 — Accepted B9 retry values and episodes: exact counts/waits/deadlines. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.13.3 — Held TSC observation-reference boundary | Fed by | C-TSC.9 — BOP and SIA links | DESIGNED | C-TSC.9 — BOP and SIA links: canonical BOP/SIA event-link structures; C-TSC — Temporary Session Cache (§7E-TSC): lifecycle and promotion authority. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| C-BOP.13.3 — Held TSC observation-reference boundary | Fed by | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED | C-TSC.9 — BOP and SIA links: canonical BOP/SIA event-link structures; C-TSC — Temporary Session Cache (§7E-TSC): lifecycle and promotion authority. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| C-BOP.13.4 — Observation operation and canonical child links | Fed by | C-7B.10.5.1 — One real operation one log | DESIGNED | C-7B.10.5.1 — One real operation one log: one real operation one log. | [V10 §0B] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP.15 — Enrollment and biometric observation interfaces | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion before capture and protected handling. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| C-BOP.15.1 — B29 capture and BOP observation ownership | Fed by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9): the voice pipeline’s actual authorized stream and physical start/stop facts. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-BOP.15.3 — Biometric system-command and security-audit separation | Fed by | C-BAI — Biometric Authorization Interface (§25.6) | DESIGNED | C-BAI — Biometric Authorization Interface (§25.6): its own actual command facts; C-BOP.2.12 — system_command: deterministic system-command event.; C-BOP.15.3.3 — Biometric prompt_opened observation: prompt_opened; C-BOP.15.3.4 — Biometric result:success observation: result:success; C-BOP.15.3.5 — Biometric result:failure observation: result:failure; C-BOP.15.3.6 — Biometric result:cancelled observation: result:cancelled; C-BOP.15.3.7 — Biometric result:timeout observation: result:timeout; C-BOP.15.3.8 — Biometric result:lockout observation: result:lockout; C-BOP.15.3.9 — Biometric result:error observation: result:error. | [V10 §25.6 / BOP vs. Security Audit Separation] |
| C-BOP.15.4 — Single enrollment biometric success observation | Gated by | C-BAI — Biometric Authorization Interface (§25.6) | DESIGNED | C-BAI — Biometric Authorization Interface (§25.6): actual source and durable consumed-token proof; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): actual committed session-open truth, timing coordination only. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-BOP.15.4 — Single enrollment biometric success observation | Gated by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-BAI — Biometric Authorization Interface (§25.6): actual source and durable consumed-token proof; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): actual committed session-open truth, timing coordination only. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-BOP.15.5 — Frozen enrollment capture set and normal entry | Gated by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): owns close/freeze and later profile eligibility; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy exclusion remains distinct. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| C-BOP.15.5 — Frozen enrollment capture set and normal entry | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): owns close/freeze and later profile eligibility; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy exclusion remains distinct. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| C-BOP.15.5 — Frozen enrollment capture set and normal entry | Changes | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed roots enter its standard queue. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| C-BOP.15.5 — Frozen enrollment capture set and normal entry | Changes | C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam: readings remain in the quarantine/promote boundary. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| C-BOP.15.6 — Protected raw-voice boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture-first exclusion and protected handling. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] |
| C-BOP.16 — Shared observation logging and protected access | Fed by | C-7B.10.5.1 — One real operation one log | DESIGNED | C-7B.10.5.1 — One real operation one log: canonical one-operation/one-log law. | [MAP C-BOP] [V10 §0B] |
| C-BOP.16 — Shared observation logging and protected access | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record access and purpose-specific authorization; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization. | [MAP C-BOP] [V10 §0B] |
| C-BOP.16 — Shared observation logging and protected access | Gated by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record access and purpose-specific authorization; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization. | [MAP C-BOP] [V10 §0B] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-LEARN — Personal Learning and Adaptation (§26, cross-cutting) | Raw behavioral observations in shared memory. | Uses their separate Meaning Engine readings in the continuous learning loop. | Capture itself creates no behavioral rule. | DESIGNED | [V10 §26.4] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Authorized typed observation captures. | Routes them through its single Catalog entry and accepted writer. | No second root-writing path is created. | DESIGNED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-TSC — Temporary Session Cache (§7E-TSC) | References to observations already held in Catalog pre-ingest. | Links them without calling BOP. | Pending fingerprint authorization still blocks promotion. | DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-TSC.9 — BOP and SIA links | The existing preingest observation identity. | Maintains the structural event link. | No new capture or root copy is created. | DESIGNED | [V10 §7E-TSC / 29. Integration Boundaries] |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-TSC.13.1 — Close observation | The actual session-close observation. | Preserves it with the close/seal facts. | Physical close remains distinct from content promotion. | DESIGNED | [V10 §7E-TSC / 13. Normal Session Close and Sealing] |

## Scope, paths and source dispositions

BOP owns physical capture/classification only. Complete V10 §25.1 and §26.4 are placed in source order: authorization, event vocabulary, seven-field root bindings, full payload, corrected capture identity, quality, third-party handling, simultaneous channels, optional reconnection, DUMB boundary and failures. All twenty-two event values retain their decided payload details. Voice interruption carries both timestamp and N.H output position; OOP owns the immediate TTS stop. The command registry applies only to deterministic interface events, never interpretation of ordinary language. Confirmed sent text is the only live text source; unfinished typing is never observed.

The nineteen BOP payload fields retain their types/nullability and exact controlled values. Nested authorization distinguishes live_session, manual_import and formally adopted enrollment_declared; the latter is role declaration, not SIA-confirmed identity, with no schema version change. The root’s seven fields remain unchanged and the bop:v1 legacy subject remains intact. Capture time and event time stay separate. Corrected capture_id includes all six specified inputs, with literal null for absent duration and the monotonically increasing session-unique sequence durably persisted before any write. No hashing algorithm or encoding is invented.

Quality retains all four fields, four signal-quality values, five field_status fields and four completeness values. The reconstruction label grants no authority to reconstruct uncaptured crash data. Below-threshold quality does not erase an otherwise eligible root or authorize a privacy/hold bypass. Participant/anchor object internals and the field_status types/vocabulary are not supplied by these sources and remain open. Third-party booleans, three handling values and privacy-rule version are explicit; the Companion’s unqualified pre-output wording is marked against V10’s exact internal/visible-purpose distinction. Level 1, TSC and no-destruction protections remain intact.

A15’s whole corrected source and receipt establish accepted policy/design scope: optional voice-channel acoustic_condition_notes, exactly six fields and five controlled physical names, no bare labels, certainty about the physical classification only. Every downstream use preserves measurement/method/version/threshold/value/certainty scope/source provenance. The notes may inform bounded owner-governed context but never independently assert or suffice for identity, spoofing, emotion, motive, meaning or causation. This distinction preserves v1.1’s correction to the overbroad older ban. Existing root/channel/quality/third-party/identity/failure rules are unchanged. The receipt expressly identifies V10/Map pending wording as historical status awaiting versioned integration. No active schema, empirical number, algorithm, capture source or implementation authority is inferred. Its own formal closure/audit condition is retained separately from accepted policy status.

B-INT-3 uses exactly Catalog→append_root/B11 active batch→standard readings. Canonical B11 selection/claim/ownership/fence/coverage/recovery and B9 failure/value trees are reused, with no new tuning or second mechanism. Old sealed roots are never reopened. TSC-held BOP observations keep their existing pre-ingest identifiers, timing links and authorization hold; TSC does not call BOP. SIA security events remain separate audit records and are not promoted as roots. Capture failure and session interruption preserve honest gaps and stable retry identity.

The complete imported-reaction operation is placed: exact playback start; first of post-bound expiry, different-item start, session end or explicit close; active and bounded post-playback eligible segments; immediate pause suspension; finite valid same-item resume; interruption at last committed observation; no overlap and at most one segment/item per observation; proposed reaction_window_id from session/item/start; duplicate-open recognition; committed-state-only restart with open windows closed interrupted; and no guessed reference when bounds/start/state are invalid. Paused and post-bound observations remain unlinked while ordinary authorized capture continues. Raw timing/silence/interruption/stop/resume/afterward-speech/measurements remain connected, never merged and never causal or emotional claims. The capture-time link is a canonical child inside the same atomic capture transaction, with exactly one parent terminal record; a truly later relationship operation must have a distinct identity.

Enrollment interfaces preserve B29 microphone/control ownership and BOP observation truth. Absent BOP observation is not proof that capture never started. Enrollment roots carry exactly the declared role/source-title/authorization provenance. The BAI observation boundary preserves all seven permitted physical result forms and the safe session/local-timestamp payload. The one enrollment success command is BAI-sourced and deterministic from session/command/open commit; the coordinator may time it but never fabricate it. Capture stops before the frozen reference set is created; roots enter through the normal writer only after session end, capture_id remains end-to-end, and readings go to quarantine. Rejected training segments remain preserved observations. Raw voice never enters coordinator records, ordinary logs or reconstructive failure descriptions. Full enrollment lifecycles and security owners remain CH09.

All four prior incoming places are reciprocated individually. CH04-a’s Catalog root stamps C-BOP ACCEPTED in Fed by; the root is DESIGNED under contract §3, while accepted mechanical subparts have their own stamps. That earlier status defect is carried for the fix round without altering bytes. The imported-reaction/observation obligation carried from Writing 1 is now placed here; the independent affirmation obligation remains CH08-f. OOP and full adaptation remain CH08-e/g, full side paths CH11 and regenerated registers CH12. Decision-index rows are navigation only; inactive Voice/Delivery Director is intent only; no historical source was newly opened.

## Source-to-card coverage added by CH08-d

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

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-BOP.4.10 — BOP participants | participant_record internal fields/types beyond the stated list | NOT DECIDED |
| C-BOP.9 — connection_anchors and later reconnection | anchor_record internal fields/types beyond optional retrieval-aid list | NOT DECIDED |
| C-BOP.6.3 — field_completeness | field_status field types and permitted status vocabulary beyond the five named fields | NOT DECIDED |
| C-BOP.5 — Corrected BOP capture_id | Exact stable_hash algorithm and canonical input encoding | NOT DECIDED |
| C-BOP.2.8 — amplitude_measurement | Exact amplitude/energy payload field names and units beyond raw measurement and required method/version | NOT DECIDED |
| C-BOP.12 — Optional acoustic_condition_notes amendment | Acoustic numeric thresholds, detection algorithms, calibration data, device/hardware tuning, false-positive handling, performance limits and implementation mechanics | NOT DECIDED |
| C-BOP.14 — Bounded imported-voice reaction window | Finite governed post-playback duration and maximum-pause value; linking remains disabled until required valid settings exist | NOT DECIDED |
| C-BOP.2.22 — extended | Registration mechanics and extended-event schemas beyond registered-before-first-use identity/version/raw payload | NOT DECIDED |
| C-BOP.15 — Enrollment and biometric observation interfaces | Complete enrollment/security coordination belongs to CH09; the decided BOP interfaces are retained here | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-BOP.1 — Authorized physical-observation boundary | Changes | 1 | NOT DECIDED |
| C-BOP.1.1 — Authorized-session all-signal rule | Fed by | 1 | NOT DECIDED |
| C-BOP.1.1 — Authorized-session all-signal rule | Changes | 1 | NOT DECIDED |
| C-BOP.1.2 — Authorized live-voice signals | Fails closed by | 1 | NOT DECIDED |
| C-BOP.1.2 — Authorized live-voice signals | Fed by | 1 | NOT DECIDED |
| C-BOP.1.2 — Authorized live-voice signals | Gated by | 1 | NOT DECIDED |
| C-BOP.1.2 — Authorized live-voice signals | Changes | 1 | NOT DECIDED |
| C-BOP.1.3 — Confirmed-sent-text source | Fails closed by | 1 | NOT DECIDED |
| C-BOP.1.3 — Confirmed-sent-text source | Fed by | 1 | NOT DECIDED |
| C-BOP.1.3 — Confirmed-sent-text source | Gated by | 1 | NOT DECIDED |
| C-BOP.1.3 — Confirmed-sent-text source | Changes | 1 | NOT DECIDED |
| C-BOP.1.4 — Authorized session-state source | Fails closed by | 1 | NOT DECIDED |
| C-BOP.1.4 — Authorized session-state source | Fed by | 1 | NOT DECIDED |
| C-BOP.1.4 — Authorized session-state source | Gated by | 1 | NOT DECIDED |
| C-BOP.1.4 — Authorized session-state source | Changes | 1 | NOT DECIDED |
| C-BOP.1.5 — Explicitly authorized imported source | Fails closed by | 1 | NOT DECIDED |
| C-BOP.1.5 — Explicitly authorized imported source | Fed by | 1 | NOT DECIDED |
| C-BOP.1.5 — Explicitly authorized imported source | Gated by | 1 | NOT DECIDED |
| C-BOP.1.5 — Explicitly authorized imported source | Changes | 1 | NOT DECIDED |
| C-BOP.2 — BOP v1 controlled event vocabulary | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2 — BOP v1 controlled event vocabulary | Gated by | 1 | NOT DECIDED |
| C-BOP.2 — BOP v1 controlled event vocabulary | Changes | 1 | NOT DECIDED |
| C-BOP.2.1 — voice_onset | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.1 — voice_onset | Fed by | 1 | NOT DECIDED |
| C-BOP.2.1 — voice_onset | Gated by | 1 | NOT DECIDED |
| C-BOP.2.1 — voice_onset | Changes | 1 | NOT DECIDED |
| C-BOP.2.2 — voice_offset | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.2 — voice_offset | Fed by | 1 | NOT DECIDED |
| C-BOP.2.2 — voice_offset | Gated by | 1 | NOT DECIDED |
| C-BOP.2.2 — voice_offset | Changes | 1 | NOT DECIDED |
| C-BOP.2.3 — silence_interval | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.3 — silence_interval | Fed by | 1 | NOT DECIDED |
| C-BOP.2.3 — silence_interval | Gated by | 1 | NOT DECIDED |
| C-BOP.2.3 — silence_interval | Changes | 1 | NOT DECIDED |
| C-BOP.2.4 — non_word_sound | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.4 — non_word_sound | Gated by | 1 | NOT DECIDED |
| C-BOP.2.4 — non_word_sound | Changes | 1 | NOT DECIDED |
| C-BOP.2.4.1 — breath | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.4.1 — breath | Fed by | 1 | NOT DECIDED |
| C-BOP.2.4.1 — breath | Gated by | 1 | NOT DECIDED |
| C-BOP.2.4.1 — breath | Changes | 1 | NOT DECIDED |
| C-BOP.2.4.2 — non_breath_non_word | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.4.2 — non_breath_non_word | Fed by | 1 | NOT DECIDED |
| C-BOP.2.4.2 — non_breath_non_word | Gated by | 1 | NOT DECIDED |
| C-BOP.2.4.2 — non_breath_non_word | Changes | 1 | NOT DECIDED |
| C-BOP.2.5 — voice_overlap | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.5 — voice_overlap | Fed by | 1 | NOT DECIDED |
| C-BOP.2.5 — voice_overlap | Gated by | 1 | NOT DECIDED |
| C-BOP.2.5 — voice_overlap | Changes | 1 | NOT DECIDED |
| C-BOP.2.6 — voice_interrupt_of_nh | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.6 — voice_interrupt_of_nh | Gated by | 1 | NOT DECIDED |
| C-BOP.2.6 — voice_interrupt_of_nh | Changes | 1 | NOT DECIDED |
| C-BOP.2.6.1 — Voice-interruption timestamp | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.6.1 — Voice-interruption timestamp | Fed by | 1 | NOT DECIDED |
| C-BOP.2.6.1 — Voice-interruption timestamp | Gated by | 1 | NOT DECIDED |
| C-BOP.2.6.1 — Voice-interruption timestamp | Changes | 1 | NOT DECIDED |
| C-BOP.2.6.2 — Voice-interruption output-stream position | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.6.2 — Voice-interruption output-stream position | Fed by | 1 | NOT DECIDED |
| C-BOP.2.6.2 — Voice-interruption output-stream position | Gated by | 1 | NOT DECIDED |
| C-BOP.2.6.2 — Voice-interruption output-stream position | Changes | 1 | NOT DECIDED |
| C-BOP.2.7 — pitch_measurement | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7 — pitch_measurement | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7 — pitch_measurement | Changes | 1 | NOT DECIDED |
| C-BOP.2.7.1 — hz_min | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7.1 — hz_min | Fed by | 1 | NOT DECIDED |
| C-BOP.2.7.1 — hz_min | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7.1 — hz_min | Changes | 1 | NOT DECIDED |
| C-BOP.2.7.2 — hz_max | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7.2 — hz_max | Fed by | 1 | NOT DECIDED |
| C-BOP.2.7.2 — hz_max | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7.2 — hz_max | Changes | 1 | NOT DECIDED |
| C-BOP.2.7.3 — hz_mean | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7.3 — hz_mean | Fed by | 1 | NOT DECIDED |
| C-BOP.2.7.3 — hz_mean | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7.3 — hz_mean | Changes | 1 | NOT DECIDED |
| C-BOP.2.7.4 — measurement_method | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7.4 — measurement_method | Fed by | 1 | NOT DECIDED |
| C-BOP.2.7.4 — measurement_method | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7.4 — measurement_method | Changes | 1 | NOT DECIDED |
| C-BOP.2.7.5 — measurement_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.7.5 — measurement_version | Fed by | 1 | NOT DECIDED |
| C-BOP.2.7.5 — measurement_version | Gated by | 1 | NOT DECIDED |
| C-BOP.2.7.5 — measurement_version | Changes | 1 | NOT DECIDED |
| C-BOP.2.8 — amplitude_measurement | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.8 — amplitude_measurement | Gated by | 1 | NOT DECIDED |
| C-BOP.2.8 — amplitude_measurement | Changes | 1 | NOT DECIDED |
| C-BOP.2.9 — text_message_sent | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.9 — text_message_sent | Gated by | 1 | NOT DECIDED |
| C-BOP.2.9 — text_message_sent | Changes | 1 | NOT DECIDED |
| C-BOP.2.9.1 — character_count | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.9.1 — character_count | Fed by | 1 | NOT DECIDED |
| C-BOP.2.9.1 — character_count | Gated by | 1 | NOT DECIDED |
| C-BOP.2.9.1 — character_count | Changes | 1 | NOT DECIDED |
| C-BOP.2.9.2 — word_count | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.9.2 — word_count | Fed by | 1 | NOT DECIDED |
| C-BOP.2.9.2 — word_count | Gated by | 1 | NOT DECIDED |
| C-BOP.2.9.2 — word_count | Changes | 1 | NOT DECIDED |
| C-BOP.2.9.3 — sentence_count_approx | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.9.3 — sentence_count_approx | Fed by | 1 | NOT DECIDED |
| C-BOP.2.9.3 — sentence_count_approx | Gated by | 1 | NOT DECIDED |
| C-BOP.2.9.3 — sentence_count_approx | Changes | 1 | NOT DECIDED |
| C-BOP.2.9.4 — exact_text_reference | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.9.4 — exact_text_reference | Fed by | 1 | NOT DECIDED |
| C-BOP.2.9.4 — exact_text_reference | Gated by | 1 | NOT DECIDED |
| C-BOP.2.9.4 — exact_text_reference | Changes | 1 | NOT DECIDED |
| C-BOP.2.10 — text_response_timing | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.10 — text_response_timing | Gated by | 1 | NOT DECIDED |
| C-BOP.2.10 — text_response_timing | Changes | 1 | NOT DECIDED |
| C-BOP.2.10.1 — Text-response raw millisecond delta | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.10.1 — Text-response raw millisecond delta | Fed by | 1 | NOT DECIDED |
| C-BOP.2.10.1 — Text-response raw millisecond delta | Gated by | 1 | NOT DECIDED |
| C-BOP.2.10.1 — Text-response raw millisecond delta | Changes | 1 | NOT DECIDED |
| C-BOP.2.10.2 — Text-response N.H output-event reference | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.10.2 — Text-response N.H output-event reference | Fed by | 1 | NOT DECIDED |
| C-BOP.2.10.2 — Text-response N.H output-event reference | Gated by | 1 | NOT DECIDED |
| C-BOP.2.10.2 — Text-response N.H output-event reference | Changes | 1 | NOT DECIDED |
| C-BOP.2.11 — no_response_session | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.11 — no_response_session | Fed by | 1 | NOT DECIDED |
| C-BOP.2.11 — no_response_session | Gated by | 1 | NOT DECIDED |
| C-BOP.2.11 — no_response_session | Changes | 1 | NOT DECIDED |
| C-BOP.2.12 — system_command | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.12 — system_command | Gated by | 1 | NOT DECIDED |
| C-BOP.2.12 — system_command | Changes | 1 | NOT DECIDED |
| C-BOP.2.12.1 — command_identifier | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.12.1 — command_identifier | Fed by | 1 | NOT DECIDED |
| C-BOP.2.12.1 — command_identifier | Gated by | 1 | NOT DECIDED |
| C-BOP.2.12.1 — command_identifier | Changes | 1 | NOT DECIDED |
| C-BOP.2.13 — session_opened | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.13 — session_opened | Fed by | 1 | NOT DECIDED |
| C-BOP.2.13 — session_opened | Gated by | 1 | NOT DECIDED |
| C-BOP.2.13 — session_opened | Changes | 1 | NOT DECIDED |
| C-BOP.2.14 — session_closed | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.14 — session_closed | Fed by | 1 | NOT DECIDED |
| C-BOP.2.14 — session_closed | Gated by | 1 | NOT DECIDED |
| C-BOP.2.14 — session_closed | Changes | 1 | NOT DECIDED |
| C-BOP.2.15 — session_interrupted | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.15 — session_interrupted | Fed by | 1 | NOT DECIDED |
| C-BOP.2.15 — session_interrupted | Gated by | 1 | NOT DECIDED |
| C-BOP.2.15 — session_interrupted | Changes | 1 | NOT DECIDED |
| C-BOP.2.16 — function_started | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.16 — function_started | Fed by | 1 | NOT DECIDED |
| C-BOP.2.16 — function_started | Gated by | 1 | NOT DECIDED |
| C-BOP.2.16 — function_started | Changes | 1 | NOT DECIDED |
| C-BOP.2.17 — function_completed | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.17 — function_completed | Fed by | 1 | NOT DECIDED |
| C-BOP.2.17 — function_completed | Gated by | 1 | NOT DECIDED |
| C-BOP.2.17 — function_completed | Changes | 1 | NOT DECIDED |
| C-BOP.2.18 — function_interrupted | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.18 — function_interrupted | Fed by | 1 | NOT DECIDED |
| C-BOP.2.18 — function_interrupted | Gated by | 1 | NOT DECIDED |
| C-BOP.2.18 — function_interrupted | Changes | 1 | NOT DECIDED |
| C-BOP.2.19 — capture_failure | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.19 — capture_failure | Fed by | 1 | NOT DECIDED |
| C-BOP.2.19 — capture_failure | Gated by | 1 | NOT DECIDED |
| C-BOP.2.19 — capture_failure | Changes | 1 | NOT DECIDED |
| C-BOP.2.20 — import_authorized | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.20 — import_authorized | Fed by | 1 | NOT DECIDED |
| C-BOP.2.20 — import_authorized | Gated by | 1 | NOT DECIDED |
| C-BOP.2.20 — import_authorized | Changes | 1 | NOT DECIDED |
| C-BOP.2.21 — import_processed | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.21 — import_processed | Fed by | 1 | NOT DECIDED |
| C-BOP.2.21 — import_processed | Gated by | 1 | NOT DECIDED |
| C-BOP.2.21 — import_processed | Changes | 1 | NOT DECIDED |
| C-BOP.2.22 — extended | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.22 — extended | Gated by | 1 | NOT DECIDED |
| C-BOP.2.22 — extended | Changes | 1 | NOT DECIDED |
| C-BOP.2.22.1 — Extended raw_payload | Fails closed by | 1 | NOT DECIDED |
| C-BOP.2.22.1 — Extended raw_payload | Fed by | 1 | NOT DECIDED |
| C-BOP.2.22.1 — Extended raw_payload | Gated by | 1 | NOT DECIDED |
| C-BOP.2.22.1 — Extended raw_payload | Changes | 1 | NOT DECIDED |
| C-BOP.3 — Seven-field BOP root bindings | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3 — Seven-field BOP root bindings | Gated by | 1 | NOT DECIDED |
| C-BOP.3 — Seven-field BOP root bindings | Changes | 1 | NOT DECIDED |
| C-BOP.3.1 — BOP root id | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.1 — BOP root id | Gated by | 1 | NOT DECIDED |
| C-BOP.3.1 — BOP root id | Changes | 1 | NOT DECIDED |
| C-BOP.3.2 — BOP root subject | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.2 — BOP root subject | Fed by | 1 | NOT DECIDED |
| C-BOP.3.2 — BOP root subject | Gated by | 1 | NOT DECIDED |
| C-BOP.3.2 — BOP root subject | Changes | 1 | NOT DECIDED |
| C-BOP.3.3 — BOP root timestamp | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.3 — BOP root timestamp | Fed by | 1 | NOT DECIDED |
| C-BOP.3.3 — BOP root timestamp | Gated by | 1 | NOT DECIDED |
| C-BOP.3.3 — BOP root timestamp | Changes | 1 | NOT DECIDED |
| C-BOP.3.4 — BOP root content | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.4 — BOP root content | Gated by | 1 | NOT DECIDED |
| C-BOP.3.4 — BOP root content | Changes | 1 | NOT DECIDED |
| C-BOP.3.5 — BOP root re_reads | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.5 — BOP root re_reads | Fed by | 1 | NOT DECIDED |
| C-BOP.3.5 — BOP root re_reads | Gated by | 1 | NOT DECIDED |
| C-BOP.3.5 — BOP root re_reads | Changes | 1 | NOT DECIDED |
| C-BOP.3.6 — BOP root source_title | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.6 — BOP root source_title | Fed by | 1 | NOT DECIDED |
| C-BOP.3.6 — BOP root source_title | Gated by | 1 | NOT DECIDED |
| C-BOP.3.6 — BOP root source_title | Changes | 1 | NOT DECIDED |
| C-BOP.3.7 — BOP root role | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.7 — BOP root role | Gated by | 1 | NOT DECIDED |
| C-BOP.3.7 — BOP root role | Changes | 1 | NOT DECIDED |
| C-BOP.3.7.1 — BOP role ness | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.7.1 — BOP role ness | Fed by | 1 | NOT DECIDED |
| C-BOP.3.7.1 — BOP role ness | Gated by | 1 | NOT DECIDED |
| C-BOP.3.7.1 — BOP role ness | Changes | 1 | NOT DECIDED |
| C-BOP.3.7.2 — BOP role nh | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.7.2 — BOP role nh | Fed by | 1 | NOT DECIDED |
| C-BOP.3.7.2 — BOP role nh | Gated by | 1 | NOT DECIDED |
| C-BOP.3.7.2 — BOP role nh | Changes | 1 | NOT DECIDED |
| C-BOP.3.7.3 — BOP role session | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.7.3 — BOP role session | Fed by | 1 | NOT DECIDED |
| C-BOP.3.7.3 — BOP role session | Gated by | 1 | NOT DECIDED |
| C-BOP.3.7.3 — BOP role session | Changes | 1 | NOT DECIDED |
| C-BOP.3.7.4 — BOP role third_party_observed | Fails closed by | 1 | NOT DECIDED |
| C-BOP.3.7.4 — BOP role third_party_observed | Fed by | 1 | NOT DECIDED |
| C-BOP.3.7.4 — BOP role third_party_observed | Gated by | 1 | NOT DECIDED |
| C-BOP.3.7.4 — BOP role third_party_observed | Changes | 1 | NOT DECIDED |
| C-BOP.4 — bop_payload | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4 — bop_payload | Gated by | 1 | NOT DECIDED |
| C-BOP.4 — bop_payload | Changes | 1 | NOT DECIDED |
| C-BOP.4.1 — bop_schema_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.1 — bop_schema_version | Fed by | 1 | NOT DECIDED |
| C-BOP.4.1 — bop_schema_version | Gated by | 1 | NOT DECIDED |
| C-BOP.4.1 — bop_schema_version | Changes | 1 | NOT DECIDED |
| C-BOP.4.2 — BOP event_type | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.2 — BOP event_type | Gated by | 1 | NOT DECIDED |
| C-BOP.4.2 — BOP event_type | Changes | 1 | NOT DECIDED |
| C-BOP.4.3 — extended_event_type_id | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.3 — extended_event_type_id | Fed by | 1 | NOT DECIDED |
| C-BOP.4.3 — extended_event_type_id | Gated by | 1 | NOT DECIDED |
| C-BOP.4.3 — extended_event_type_id | Changes | 1 | NOT DECIDED |
| C-BOP.4.4 — extended_event_type_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.4 — extended_event_type_version | Fed by | 1 | NOT DECIDED |
| C-BOP.4.4 — extended_event_type_version | Gated by | 1 | NOT DECIDED |
| C-BOP.4.4 — extended_event_type_version | Changes | 1 | NOT DECIDED |
| C-BOP.4.5 — event_occurred_at | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.5 — event_occurred_at | Fed by | 1 | NOT DECIDED |
| C-BOP.4.5 — event_occurred_at | Gated by | 1 | NOT DECIDED |
| C-BOP.4.5 — event_occurred_at | Changes | 1 | NOT DECIDED |
| C-BOP.4.6 — event_duration_ms | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.6 — event_duration_ms | Fed by | 1 | NOT DECIDED |
| C-BOP.4.6 — event_duration_ms | Gated by | 1 | NOT DECIDED |
| C-BOP.4.6 — event_duration_ms | Changes | 1 | NOT DECIDED |
| C-BOP.4.7 — BOP session_id | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.7 — BOP session_id | Fed by | 1 | NOT DECIDED |
| C-BOP.4.7 — BOP session_id | Gated by | 1 | NOT DECIDED |
| C-BOP.4.7 — BOP session_id | Changes | 1 | NOT DECIDED |
| C-BOP.4.8 — BOP session_mode | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8 — BOP session_mode | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8 — BOP session_mode | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.1 — BOP mode voice | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.1 — BOP mode voice | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.1 — BOP mode voice | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.1 — BOP mode voice | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.2 — BOP mode text | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.2 — BOP mode text | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.2 — BOP mode text | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.2 — BOP mode text | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.3 — BOP mode imported_audio | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.3 — BOP mode imported_audio | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.3 — BOP mode imported_audio | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.3 — BOP mode imported_audio | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.4 — BOP mode imported_video | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.4 — BOP mode imported_video | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.4 — BOP mode imported_video | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.4 — BOP mode imported_video | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.5 — BOP mode imported_text | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.5 — BOP mode imported_text | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.5 — BOP mode imported_text | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.5 — BOP mode imported_text | Changes | 1 | NOT DECIDED |
| C-BOP.4.8.6 — BOP mode mixed | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.8.6 — BOP mode mixed | Fed by | 1 | NOT DECIDED |
| C-BOP.4.8.6 — BOP mode mixed | Gated by | 1 | NOT DECIDED |
| C-BOP.4.8.6 — BOP mode mixed | Changes | 1 | NOT DECIDED |
| C-BOP.4.9 — session_authorization | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9 — session_authorization | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9 — session_authorization | Changes | 1 | NOT DECIDED |
| C-BOP.4.9.1 — BOP authorization_type | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9.1 — BOP authorization_type | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9.1 — BOP authorization_type | Changes | 1 | NOT DECIDED |
| C-BOP.4.9.1.1 — live_session | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.1 — live_session | Fed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.1 — live_session | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9.1.1 — live_session | Changes | 1 | NOT DECIDED |
| C-BOP.4.9.1.2 — manual_import | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.2 — manual_import | Fed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.2 — manual_import | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9.1.2 — manual_import | Changes | 1 | NOT DECIDED |
| C-BOP.4.9.1.3 — enrollment_declared | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.3 — enrollment_declared | Fed by | 1 | NOT DECIDED |
| C-BOP.4.9.1.3 — enrollment_declared | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9.1.3 — enrollment_declared | Changes | 1 | NOT DECIDED |
| C-BOP.4.9.2 — authorization_event_id | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.9.2 — authorization_event_id | Fed by | 1 | NOT DECIDED |
| C-BOP.4.9.2 — authorization_event_id | Gated by | 1 | NOT DECIDED |
| C-BOP.4.9.2 — authorization_event_id | Changes | 1 | NOT DECIDED |
| C-BOP.4.10 — BOP participants | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.10 — BOP participants | Fed by | 1 | NOT DECIDED |
| C-BOP.4.10 — BOP participants | Gated by | 1 | NOT DECIDED |
| C-BOP.4.10 — BOP participants | Changes | 1 | NOT DECIDED |
| C-BOP.4.11 — signal_measurements | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.11 — signal_measurements | Gated by | 1 | NOT DECIDED |
| C-BOP.4.11 — signal_measurements | Changes | 1 | NOT DECIDED |
| C-BOP.4.12 — simultaneous_bundle_id | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.12 — simultaneous_bundle_id | Fed by | 1 | NOT DECIDED |
| C-BOP.4.12 — simultaneous_bundle_id | Gated by | 1 | NOT DECIDED |
| C-BOP.4.12 — simultaneous_bundle_id | Changes | 1 | NOT DECIDED |
| C-BOP.4.13 — simultaneous_bundle_position | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.13 — simultaneous_bundle_position | Fed by | 1 | NOT DECIDED |
| C-BOP.4.13 — simultaneous_bundle_position | Gated by | 1 | NOT DECIDED |
| C-BOP.4.13 — simultaneous_bundle_position | Changes | 1 | NOT DECIDED |
| C-BOP.4.14 — bop_processor_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.14 — bop_processor_version | Fed by | 1 | NOT DECIDED |
| C-BOP.4.14 — bop_processor_version | Gated by | 1 | NOT DECIDED |
| C-BOP.4.14 — bop_processor_version | Changes | 1 | NOT DECIDED |
| C-BOP.4.15 — BOP capture_method | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.15 — BOP capture_method | Gated by | 1 | NOT DECIDED |
| C-BOP.4.15 — BOP capture_method | Changes | 1 | NOT DECIDED |
| C-BOP.4.15.1 — live_capture | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.15.1 — live_capture | Fed by | 1 | NOT DECIDED |
| C-BOP.4.15.1 — live_capture | Gated by | 1 | NOT DECIDED |
| C-BOP.4.15.1 — live_capture | Changes | 1 | NOT DECIDED |
| C-BOP.4.15.2 — import_processing | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.15.2 — import_processing | Fed by | 1 | NOT DECIDED |
| C-BOP.4.15.2 — import_processing | Gated by | 1 | NOT DECIDED |
| C-BOP.4.15.2 — import_processing | Changes | 1 | NOT DECIDED |
| C-BOP.4.15.3 — session_state_event | Fails closed by | 1 | NOT DECIDED |
| C-BOP.4.15.3 — session_state_event | Fed by | 1 | NOT DECIDED |
| C-BOP.4.15.3 — session_state_event | Gated by | 1 | NOT DECIDED |
| C-BOP.4.15.3 — session_state_event | Changes | 1 | NOT DECIDED |
| C-BOP.4.16 — capture_sequence_number | Fed by | 1 | NOT DECIDED |
| C-BOP.4.16 — capture_sequence_number | Gated by | 1 | NOT DECIDED |
| C-BOP.4.16 — capture_sequence_number | Changes | 1 | NOT DECIDED |
| C-BOP.5 — Corrected BOP capture_id | Gated by | 1 | NOT DECIDED |
| C-BOP.5 — Corrected BOP capture_id | Changes | 1 | NOT DECIDED |
| C-BOP.6 — observation_quality | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6 — observation_quality | Changes | 1 | NOT DECIDED |
| C-BOP.6.1 — signal_quality | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.1 — signal_quality | Gated by | 1 | NOT DECIDED |
| C-BOP.6.1 — signal_quality | Changes | 1 | NOT DECIDED |
| C-BOP.6.1.1 — Signal quality clean | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.1.1 — Signal quality clean | Fed by | 1 | NOT DECIDED |
| C-BOP.6.1.1 — Signal quality clean | Gated by | 1 | NOT DECIDED |
| C-BOP.6.1.1 — Signal quality clean | Changes | 1 | NOT DECIDED |
| C-BOP.6.1.2 — Signal quality partial | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.1.2 — Signal quality partial | Fed by | 1 | NOT DECIDED |
| C-BOP.6.1.2 — Signal quality partial | Gated by | 1 | NOT DECIDED |
| C-BOP.6.1.2 — Signal quality partial | Changes | 1 | NOT DECIDED |
| C-BOP.6.1.3 — Signal quality degraded | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.1.3 — Signal quality degraded | Fed by | 1 | NOT DECIDED |
| C-BOP.6.1.3 — Signal quality degraded | Gated by | 1 | NOT DECIDED |
| C-BOP.6.1.3 — Signal quality degraded | Changes | 1 | NOT DECIDED |
| C-BOP.6.1.4 — Signal quality reconstruction | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.1.4 — Signal quality reconstruction | Fed by | 1 | NOT DECIDED |
| C-BOP.6.1.4 — Signal quality reconstruction | Gated by | 1 | NOT DECIDED |
| C-BOP.6.1.4 — Signal quality reconstruction | Changes | 1 | NOT DECIDED |
| C-BOP.6.2 — signal_quality_note | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.2 — signal_quality_note | Fed by | 1 | NOT DECIDED |
| C-BOP.6.2 — signal_quality_note | Gated by | 1 | NOT DECIDED |
| C-BOP.6.2 — signal_quality_note | Changes | 1 | NOT DECIDED |
| C-BOP.6.3 — field_completeness | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3 — field_completeness | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3 — field_completeness | Changes | 1 | NOT DECIDED |
| C-BOP.6.3.1 — Quality field_name | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3.1 — Quality field_name | Fed by | 1 | NOT DECIDED |
| C-BOP.6.3.1 — Quality field_name | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3.1 — Quality field_name | Changes | 1 | NOT DECIDED |
| C-BOP.6.3.2 — Quality field status | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3.2 — Quality field status | Fed by | 1 | NOT DECIDED |
| C-BOP.6.3.2 — Quality field status | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3.2 — Quality field status | Changes | 1 | NOT DECIDED |
| C-BOP.6.3.3 — Quality status_note | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3.3 — Quality status_note | Fed by | 1 | NOT DECIDED |
| C-BOP.6.3.3 — Quality status_note | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3.3 — Quality status_note | Changes | 1 | NOT DECIDED |
| C-BOP.6.3.4 — fallback_value_used | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3.4 — fallback_value_used | Fed by | 1 | NOT DECIDED |
| C-BOP.6.3.4 — fallback_value_used | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3.4 — fallback_value_used | Changes | 1 | NOT DECIDED |
| C-BOP.6.3.5 — fallback_basis | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.3.5 — fallback_basis | Fed by | 1 | NOT DECIDED |
| C-BOP.6.3.5 — fallback_basis | Gated by | 1 | NOT DECIDED |
| C-BOP.6.3.5 — fallback_basis | Changes | 1 | NOT DECIDED |
| C-BOP.6.4 — overall_completeness | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.4 — overall_completeness | Gated by | 1 | NOT DECIDED |
| C-BOP.6.4 — overall_completeness | Changes | 1 | NOT DECIDED |
| C-BOP.6.4.1 — Completeness complete | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.4.1 — Completeness complete | Fed by | 1 | NOT DECIDED |
| C-BOP.6.4.1 — Completeness complete | Gated by | 1 | NOT DECIDED |
| C-BOP.6.4.1 — Completeness complete | Changes | 1 | NOT DECIDED |
| C-BOP.6.4.2 — Completeness partial | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.4.2 — Completeness partial | Fed by | 1 | NOT DECIDED |
| C-BOP.6.4.2 — Completeness partial | Gated by | 1 | NOT DECIDED |
| C-BOP.6.4.2 — Completeness partial | Changes | 1 | NOT DECIDED |
| C-BOP.6.4.3 — Completeness minimum_viable | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.4.3 — Completeness minimum_viable | Fed by | 1 | NOT DECIDED |
| C-BOP.6.4.3 — Completeness minimum_viable | Gated by | 1 | NOT DECIDED |
| C-BOP.6.4.3 — Completeness minimum_viable | Changes | 1 | NOT DECIDED |
| C-BOP.6.4.4 — Completeness below_threshold | Fails closed by | 1 | NOT DECIDED |
| C-BOP.6.4.4 — Completeness below_threshold | Fed by | 1 | NOT DECIDED |
| C-BOP.6.4.4 — Completeness below_threshold | Gated by | 1 | NOT DECIDED |
| C-BOP.6.4.4 — Completeness below_threshold | Changes | 1 | NOT DECIDED |
| C-BOP.7 — third_party_flag | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7 — third_party_flag | Changes | 1 | NOT DECIDED |
| C-BOP.7.1 — third_party_present | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.1 — third_party_present | Fed by | 1 | NOT DECIDED |
| C-BOP.7.1 — third_party_present | Gated by | 1 | NOT DECIDED |
| C-BOP.7.1 — third_party_present | Changes | 1 | NOT DECIDED |
| C-BOP.7.2 — third_party_content_present | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.2 — third_party_content_present | Fed by | 1 | NOT DECIDED |
| C-BOP.7.2 — third_party_content_present | Gated by | 1 | NOT DECIDED |
| C-BOP.7.2 — third_party_content_present | Changes | 1 | NOT DECIDED |
| C-BOP.7.3 — third_party_handling | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.3 — third_party_handling | Gated by | 1 | NOT DECIDED |
| C-BOP.7.3 — third_party_handling | Changes | 1 | NOT DECIDED |
| C-BOP.7.3.1 — ness_only | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.3.1 — ness_only | Fed by | 1 | NOT DECIDED |
| C-BOP.7.3.1 — ness_only | Gated by | 1 | NOT DECIDED |
| C-BOP.7.3.1 — ness_only | Changes | 1 | NOT DECIDED |
| C-BOP.7.3.2 — third_party_presence_noted | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.3.2 — third_party_presence_noted | Fed by | 1 | NOT DECIDED |
| C-BOP.7.3.2 — third_party_presence_noted | Gated by | 1 | NOT DECIDED |
| C-BOP.7.3.2 — third_party_presence_noted | Changes | 1 | NOT DECIDED |
| C-BOP.7.3.3 — third_party_content_reference | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.3.3 — third_party_content_reference | Fed by | 1 | NOT DECIDED |
| C-BOP.7.3.3 — third_party_content_reference | Gated by | 1 | NOT DECIDED |
| C-BOP.7.3.3 — third_party_content_reference | Changes | 1 | NOT DECIDED |
| C-BOP.7.4 — BOP privacy_rule_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.7.4 — BOP privacy_rule_version | Fed by | 1 | NOT DECIDED |
| C-BOP.7.4 — BOP privacy_rule_version | Gated by | 1 | NOT DECIDED |
| C-BOP.7.4 — BOP privacy_rule_version | Changes | 1 | NOT DECIDED |
| C-BOP.8 — One observation root per simultaneous signal channel | Fails closed by | 1 | NOT DECIDED |
| C-BOP.8 — One observation root per simultaneous signal channel | Gated by | 1 | NOT DECIDED |
| C-BOP.8 — One observation root per simultaneous signal channel | Changes | 1 | NOT DECIDED |
| C-BOP.9 — connection_anchors and later reconnection | Fails closed by | 1 | NOT DECIDED |
| C-BOP.9 — connection_anchors and later reconnection | Gated by | 1 | NOT DECIDED |
| C-BOP.9 — connection_anchors and later reconnection | Changes | 1 | NOT DECIDED |
| C-BOP.10 — Absolute DUMB and text non-inspection boundary | Fails closed by | 1 | NOT DECIDED |
| C-BOP.10 — Absolute DUMB and text non-inspection boundary | Fed by | 1 | NOT DECIDED |
| C-BOP.10 — Absolute DUMB and text non-inspection boundary | Changes | 1 | NOT DECIDED |
| C-BOP.11 — Capture failure and idempotent recovery | Gated by | 1 | NOT DECIDED |
| C-BOP.11 — Capture failure and idempotent recovery | Changes | 1 | NOT DECIDED |
| C-BOP.11.1 — Capture failure observation | Gated by | 1 | NOT DECIDED |
| C-BOP.11.1 — Capture failure observation | Changes | 1 | NOT DECIDED |
| C-BOP.11.2 — Same-capture write retry | Fails closed by | 1 | NOT DECIDED |
| C-BOP.11.2 — Same-capture write retry | Gated by | 1 | NOT DECIDED |
| C-BOP.11.2 — Same-capture write retry | Changes | 1 | NOT DECIDED |
| C-BOP.11.3 — Session-crash restart observation | Gated by | 1 | NOT DECIDED |
| C-BOP.11.3 — Session-crash restart observation | Changes | 1 | NOT DECIDED |
| C-BOP.12 — Optional acoustic_condition_notes amendment | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12 — Optional acoustic_condition_notes amendment | Gated by | 1 | NOT DECIDED |
| C-BOP.12 — Optional acoustic_condition_notes amendment | Changes | 1 | NOT DECIDED |
| C-BOP.12.1 — Acoustic condition record | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1 — Acoustic condition record | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1 — Acoustic condition record | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.1 — Acoustic condition_name | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.1 — Acoustic condition_name | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.1 — Acoustic condition_name | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.2 — Acoustic detection_method | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.2 — Acoustic detection_method | Fed by | 1 | NOT DECIDED |
| C-BOP.12.1.2 — Acoustic detection_method | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.2 — Acoustic detection_method | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.3 — Acoustic detection_version | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.3 — Acoustic detection_version | Fed by | 1 | NOT DECIDED |
| C-BOP.12.1.3 — Acoustic detection_version | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.3 — Acoustic detection_version | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.4 — Acoustic threshold_value | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.4 — Acoustic threshold_value | Fed by | 1 | NOT DECIDED |
| C-BOP.12.1.4 — Acoustic threshold_value | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.4 — Acoustic threshold_value | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.5 — Acoustic measured_value | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.5 — Acoustic measured_value | Fed by | 1 | NOT DECIDED |
| C-BOP.12.1.5 — Acoustic measured_value | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.5 — Acoustic measured_value | Changes | 1 | NOT DECIDED |
| C-BOP.12.1.6 — Acoustic certainty | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.1.6 — Acoustic certainty | Fed by | 1 | NOT DECIDED |
| C-BOP.12.1.6 — Acoustic certainty | Gated by | 1 | NOT DECIDED |
| C-BOP.12.1.6 — Acoustic certainty | Changes | 1 | NOT DECIDED |
| C-BOP.12.2 — Five acoustic condition names | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2 — Five acoustic condition names | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2 — Five acoustic condition names | Changes | 1 | NOT DECIDED |
| C-BOP.12.2.1 — high_ambient_noise | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2.1 — high_ambient_noise | Fed by | 1 | NOT DECIDED |
| C-BOP.12.2.1 — high_ambient_noise | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2.1 — high_ambient_noise | Changes | 1 | NOT DECIDED |
| C-BOP.12.2.2 — close_microphone | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2.2 — close_microphone | Fed by | 1 | NOT DECIDED |
| C-BOP.12.2.2 — close_microphone | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2.2 — close_microphone | Changes | 1 | NOT DECIDED |
| C-BOP.12.2.3 — far_microphone | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2.3 — far_microphone | Fed by | 1 | NOT DECIDED |
| C-BOP.12.2.3 — far_microphone | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2.3 — far_microphone | Changes | 1 | NOT DECIDED |
| C-BOP.12.2.4 — room_reverb_present | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2.4 — room_reverb_present | Fed by | 1 | NOT DECIDED |
| C-BOP.12.2.4 — room_reverb_present | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2.4 — room_reverb_present | Changes | 1 | NOT DECIDED |
| C-BOP.12.2.5 — signal_compression_heavy | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.2.5 — signal_compression_heavy | Fed by | 1 | NOT DECIDED |
| C-BOP.12.2.5 — signal_compression_heavy | Gated by | 1 | NOT DECIDED |
| C-BOP.12.2.5 — signal_compression_heavy | Changes | 1 | NOT DECIDED |
| C-BOP.12.3 — Bounded acoustic-note downstream context | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.3 — Bounded acoustic-note downstream context | Fed by | 1 | NOT DECIDED |
| C-BOP.12.3 — Bounded acoustic-note downstream context | Changes | 1 | NOT DECIDED |
| C-BOP.12.4 — Acoustic amendment preserves existing capture rules | Fails closed by | 1 | NOT DECIDED |
| C-BOP.12.4 — Acoustic amendment preserves existing capture rules | Changes | 1 | NOT DECIDED |
| C-BOP.13.1 — BOP consumption of B11 writer protections | Gated by | 1 | NOT DECIDED |
| C-BOP.13.1 — BOP consumption of B11 writer protections | Changes | 1 | NOT DECIDED |
| C-BOP.13.2 — BOP shared retry and committed-state recovery | Gated by | 1 | NOT DECIDED |
| C-BOP.13.2 — BOP shared retry and committed-state recovery | Changes | 1 | NOT DECIDED |
| C-BOP.13.3 — Held TSC observation-reference boundary | Gated by | 1 | NOT DECIDED |
| C-BOP.13.3 — Held TSC observation-reference boundary | Changes | 1 | NOT DECIDED |
| C-BOP.13.4 — Observation operation and canonical child links | Fails closed by | 1 | NOT DECIDED |
| C-BOP.13.4 — Observation operation and canonical child links | Gated by | 1 | NOT DECIDED |
| C-BOP.13.4 — Observation operation and canonical child links | Changes | 1 | NOT DECIDED |
| C-BOP.14 — Bounded imported-voice reaction window | Changes | 1 | NOT DECIDED |
| C-BOP.14.1 — Reaction-window start event | Gated by | 1 | NOT DECIDED |
| C-BOP.14.1 — Reaction-window start event | Changes | 1 | NOT DECIDED |
| C-BOP.14.2 — First-ending-event window closure | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.2 — First-ending-event window closure | Gated by | 1 | NOT DECIDED |
| C-BOP.14.2 — First-ending-event window closure | Changes | 1 | NOT DECIDED |
| C-BOP.14.2.1 — Finite post-playback-bound expiry | Fed by | 1 | NOT DECIDED |
| C-BOP.14.2.1 — Finite post-playback-bound expiry | Gated by | 1 | NOT DECIDED |
| C-BOP.14.2.1 — Finite post-playback-bound expiry | Changes | 1 | NOT DECIDED |
| C-BOP.14.2.2 — Different-item playback start closes prior window | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.2.2 — Different-item playback start closes prior window | Fed by | 1 | NOT DECIDED |
| C-BOP.14.2.2 — Different-item playback start closes prior window | Gated by | 1 | NOT DECIDED |
| C-BOP.14.2.2 — Different-item playback start closes prior window | Changes | 1 | NOT DECIDED |
| C-BOP.14.2.3 — Session-end reaction closure | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.2.3 — Session-end reaction closure | Fed by | 1 | NOT DECIDED |
| C-BOP.14.2.3 — Session-end reaction closure | Gated by | 1 | NOT DECIDED |
| C-BOP.14.2.3 — Session-end reaction closure | Changes | 1 | NOT DECIDED |
| C-BOP.14.2.4 — Explicit reaction-window close | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.2.4 — Explicit reaction-window close | Fed by | 1 | NOT DECIDED |
| C-BOP.14.2.4 — Explicit reaction-window close | Gated by | 1 | NOT DECIDED |
| C-BOP.14.2.4 — Explicit reaction-window close | Changes | 1 | NOT DECIDED |
| C-BOP.14.3 — Active playback segment | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.3 — Active playback segment | Gated by | 1 | NOT DECIDED |
| C-BOP.14.3 — Active playback segment | Changes | 1 | NOT DECIDED |
| C-BOP.14.4 — Paused interval and governed same-item resume | Fed by | 1 | NOT DECIDED |
| C-BOP.14.4 — Paused interval and governed same-item resume | Gated by | 1 | NOT DECIDED |
| C-BOP.14.4 — Paused interval and governed same-item resume | Changes | 1 | NOT DECIDED |
| C-BOP.14.5 — Bounded post-playback reaction segment | Gated by | 1 | NOT DECIDED |
| C-BOP.14.5 — Bounded post-playback reaction segment | Changes | 1 | NOT DECIDED |
| C-BOP.14.6 — Reaction-window interruption closure | Gated by | 1 | NOT DECIDED |
| C-BOP.14.6 — Reaction-window interruption closure | Changes | 1 | NOT DECIDED |
| C-BOP.14.7 — Structural reaction-window overlap prevention | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.7 — Structural reaction-window overlap prevention | Gated by | 1 | NOT DECIDED |
| C-BOP.14.7 — Structural reaction-window overlap prevention | Changes | 1 | NOT DECIDED |
| C-BOP.14.8 — Proposed reaction_window_id [proposed] | Fed by | 1 | NOT DECIDED |
| C-BOP.14.8 — Proposed reaction_window_id [proposed] | Gated by | 1 | NOT DECIDED |
| C-BOP.14.8 — Proposed reaction_window_id [proposed] | Changes | 1 | NOT DECIDED |
| C-BOP.14.9 — Committed-window crash recovery | Fed by | 1 | NOT DECIDED |
| C-BOP.14.9 — Committed-window crash recovery | Gated by | 1 | NOT DECIDED |
| C-BOP.14.9 — Committed-window crash recovery | Changes | 1 | NOT DECIDED |
| C-BOP.14.10 — linked_imported_origin_ref | Gated by | 1 | NOT DECIDED |
| C-BOP.14.10 — linked_imported_origin_ref | Changes | 1 | NOT DECIDED |
| C-BOP.14.11 — Capture-time reaction-link transaction | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.11 — Capture-time reaction-link transaction | Gated by | 1 | NOT DECIDED |
| C-BOP.14.11 — Capture-time reaction-link transaction | Changes | 1 | NOT DECIDED |
| C-BOP.14.12 — Reaction-link fail-closed conditions | Fed by | 1 | NOT DECIDED |
| C-BOP.14.12 — Reaction-link fail-closed conditions | Gated by | 1 | NOT DECIDED |
| C-BOP.14.12 — Reaction-link fail-closed conditions | Changes | 1 | NOT DECIDED |
| C-BOP.14.13 — Imported-reaction raw facts only | Fails closed by | 1 | NOT DECIDED |
| C-BOP.14.13 — Imported-reaction raw facts only | Fed by | 1 | NOT DECIDED |
| C-BOP.14.13 — Imported-reaction raw facts only | Gated by | 1 | NOT DECIDED |
| C-BOP.14.13 — Imported-reaction raw facts only | Changes | 1 | NOT DECIDED |
| C-BOP.15 — Enrollment and biometric observation interfaces | Changes | 1 | NOT DECIDED |
| C-BOP.15.1 — B29 capture and BOP observation ownership | Gated by | 1 | NOT DECIDED |
| C-BOP.15.1 — B29 capture and BOP observation ownership | Changes | 1 | NOT DECIDED |
| C-BOP.15.2 — Enrollment observation provenance | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.2 — Enrollment observation provenance | Gated by | 1 | NOT DECIDED |
| C-BOP.15.2 — Enrollment observation provenance | Changes | 1 | NOT DECIDED |
| C-BOP.15.3 — Biometric system-command and security-audit separation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3 — Biometric system-command and security-audit separation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3 — Biometric system-command and security-audit separation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.1 — Biometric command session ID | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.1 — Biometric command session ID | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.1 — Biometric command session ID | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.1 — Biometric command session ID | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.2 — Biometric command trusted-local timestamp | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.2 — Biometric command trusted-local timestamp | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.2 — Biometric command trusted-local timestamp | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.2 — Biometric command trusted-local timestamp | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.3 — Biometric prompt_opened observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.3 — Biometric prompt_opened observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.3 — Biometric prompt_opened observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.3 — Biometric prompt_opened observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.4 — Biometric result:success observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.4 — Biometric result:success observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.4 — Biometric result:success observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.4 — Biometric result:success observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.5 — Biometric result:failure observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.5 — Biometric result:failure observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.5 — Biometric result:failure observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.5 — Biometric result:failure observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.6 — Biometric result:cancelled observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.6 — Biometric result:cancelled observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.6 — Biometric result:cancelled observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.6 — Biometric result:cancelled observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.7 — Biometric result:timeout observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.7 — Biometric result:timeout observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.7 — Biometric result:timeout observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.7 — Biometric result:timeout observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.8 — Biometric result:lockout observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.8 — Biometric result:lockout observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.8 — Biometric result:lockout observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.8 — Biometric result:lockout observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.3.9 — Biometric result:error observation | Fails closed by | 1 | NOT DECIDED |
| C-BOP.15.3.9 — Biometric result:error observation | Fed by | 1 | NOT DECIDED |
| C-BOP.15.3.9 — Biometric result:error observation | Gated by | 1 | NOT DECIDED |
| C-BOP.15.3.9 — Biometric result:error observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.4 — Single enrollment biometric success observation | Changes | 1 | NOT DECIDED |
| C-BOP.15.6 — Protected raw-voice boundary | Fed by | 1 | NOT DECIDED |
| C-BOP.15.6 — Protected raw-voice boundary | Changes | 1 | NOT DECIDED |
| C-BOP.16 — Shared observation logging and protected access | Fails closed by | 1 | NOT DECIDED |
| C-BOP.16 — Shared observation logging and protected access | Changes | 1 | NOT DECIDED |

## Plain-gate and empty-box review

All nine fields and each one-place USED BY row were reviewed against the source-first outline. Actual capture, privacy, writer, hold and downstream interpretation boundaries use existing owners. Pure fields/vocabulary have empty TOGETHER slots where no distinct operational owner is decided; their parents consume them. No field-presence statement is invented as an independent gate. One existing built root schema is consumed under its BUILT stamp; no BOP behavior is BUILT. The two eligible reaction segments and every exact event/field/value are retained. Existing B11/B9/TSC/reading/quarantine atoms keep their IDs.

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

## READ RECORD

Pinned sources unchanged. Contract §§5–11 reopened before drafting and §11.3 after writing. Two A15 files were read whole; all other entries are scoped or retained prior readings. No truncated discovery output is credited as a whole read. The original and earlier delivered fingerprints are preserved.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §§25.1/26.4/25.12; complete BOP integration paragraph §25.11, BOP/security-audit separation §25.6 and §7E-TSC event-link handling. Prior general root/capture/log boundaries retained. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete accepted BOP §1, including full event/payload/recovery/amendment paragraphs; unqualified privacy wording compared with V10. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-BOP/C-OOP entries and B-INT-3/A15 navigation; no whole-file credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Whole: all 324 lines, including the precise v1.1 downstream-context correction, all fields/names/open items. | `9010e9e7b66118436acaa90bb0bf3e681b5aef229b06dbbc792563b85c859a6c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: all 204 lines; acceptance/PASS/source SHA and separate receipt-closure condition retained. | `3db1015eabf7f157fff4c48a81ed4e1e70c992b4eb6eecc95ae35f5059c32e15` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: complete A10/A12, A11 adjacent text and §7 B-INT-3 handoff; prior acceptance/source reading retained. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: complete §§3/13, relevant status/version notes and §16 dependency status; prior §§14/15 retained. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Prior whole read retained from CH08-c; no new whole-file credit. | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: §8 BOP row and §7/§9 preserved boundary readings retained; old A15 pending wording not current policy status. | `5797a2ac51328985e479d2bc101f310b96d2d75976acfaf5f066c529b31d309b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped: complete A15 owner paragraph §4 and exact inventory rows for accepted source/receipt; BOP/enrollment boundary rows discovered only. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Scoped: complete §§7/8/10/16; exact I5A/I5B/I5C/I6/I10 rows in §19; capture restart rows in §21. Full security/enrollment lifecycle remains CH09. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Prior full writer/claim/ownership/fence/recovery owner reading retained through C-STORE.4; consumed unchanged under B6 §3. | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Prior accepted exact retry-value reading retained at C-7H.10; B6 §3 reopens the complete counts/waits/deadlines. | `e8f4c3debe65d258519f07a71b221802297596e2f9ef86148d2ad1a5800b0814` |
| `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Scoped: voice-priority/BOP reference paragraph and ownership references only; INTENT, no behavior imported. | `bf57f2fc1a1dd44e3935e46f50fc4144acfaa43d11228f8779e0f468a5b5b5d2` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped: full NHD-M25/M25-BOP-VI/A15/BU6P/BU6M rows where present; navigation only. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped: full NHD-M25/M25-BOP-VI/A15/BU6P/BU6M rows where present; navigation only. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped: full NHD-M25/M25-BOP-VI/A15/BU6P/BU6M rows where present; navigation only. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped: full NHD-M25/M25-BOP-VI/A15/BU6P/BU6M rows where present; navigation only. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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
| CH08-b | `6bb46d5f30d1e67d7a27f252d656118a89b86f3a46a820542010f8599b169fa0` |
| CH08-c | `30824515b3c0d90a694118848113c4695434b1203ff1c8d5267e4dee5d456bbf` |

### READ-folder files not yet read whole

58 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 180 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 614 empty fields match 614 register rows; 9 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — the Companion’s unqualified BOP pre-output wording is marked in the header and C-BOP.7; V10’s purpose-specific authorization governs. A15’s receipt explicitly establishes later policy acceptance while preserving historical pending wording and no active-schema implication.
§3 exactly one stamp per line: PASS — 180 headers, 1013 populated fields and 298 USED BY rows checked. 1 BUILT field lines name only existing built reading/store sources; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 44 distinct citations; 44 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 180 unique current IDs without prior collisions; 1107 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 180 templates and 1627 field lines checked.
§6.3 reciprocity within this chapter: PASS — 235 internal relationship occurrences checked; 42 outgoing and 5 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 12 source-to-card rows reviewed; 101 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — twenty-two event values and their decided fields, seven root bindings, nineteen payload fields, six capture-hash inputs, all quality/third-party fields and values, six acoustic-note fields/five names, complete two-segment reaction start/pause/resume/end/failure/recovery/transaction rules, seven biometric result forms and enrollment interfaces are explicit. 115 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 18 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 180 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 180 |
| field_lines | 1627 |
| used_by_rows | 298 |
| empty_fields | 614 |
| internal_relationships | 235 |
| external_relationships | 42 |
| distinct_citations | 44 |
| resolved_citations | 44 |
| empty_together_cards | 115 |
| plain_together_lines | 0 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 1107 |
| misfiled_box_fields_scanned | 1627 |
| restriction_failure_gate_slots_reviewed | 540 |
| registered_empty_fields | 614 |
| cross_piece_continuations_checked | 42 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 18 |
| source_names_checked | 101 |
| source_names_missing | 0 |
| built_field_lines | 1 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 0 |
| outgoing_continuations | 42 |
| incoming_continuations | 5 |
| registered_fields | 614 |
| additional_gaps | 9 |
| pending_source_paths | 58 |
| source_map_rows | 12 |
| read_record_rows | 18 |

The delivery recount compares these metrics with the finished file.
