# NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md

## Provenance

This file consolidates the complete final accepted designs produced during the
security, identity, speaker access, and Biometric-Gated Maintenance Mode design
branch in the Claude project chat. All designs were reached through iterative
correction and explicit acceptance by Ness.

This file is a **companion record**, not an authoritative source. It does not
replace, supersede, or modify the N.H Master (`NH_MASTER-19_CORRECTED_v6.md`),
the Decision Defaults (`NH_DECISION_DEFAULTS-S19_v1__1_.md`), or any
implementation file. These designs must be formally patched into the Master
through the accepted patch-only, no-loss protocol before they carry Master
authority.

Every superseded draft and every rejected wording from earlier iterations has
been removed. Only final corrected accepted text is preserved here.

---

## Contents

1. BOP — Behavioral Observation Processing (detailed design)
2. Other-Speaker / Guest / Known-Person Architecture (high-level, final)
3. SIA — Speaker Identity Assessment (detailed design)
4. SACL — Speaker Access-Control Layer (detailed design)
5. Wellbeing / Identity / Security Separation Rules
6. BAI — Biometric Authorization Interface (detailed design)
7. Initial Owner-Phone Pairing
8. Recovery-Code Lifecycle (creation, verification, local test, activation, rotation)
9. Future-Phone Replacement Flow
10. Atomic Emergency Recovery Flow
11. Initial Ness Voice-Profile Enrollment Bootstrap
12. Formally Adopted Vocabulary Additions
13. BGMM — Biometric-Gated Maintenance Mode (detailed design)

---

## Status Label

Every component in this file carries the status:

**ACCEPTED DESIGN — NOT YET BUILT**

No component described here has been implemented in code, verified on disk, or
patched into the Master.

---

## Build-Time Implementation Settings (not unresolved concept decisions)

The following two items are confirmed build-time settings, not open concept
decisions requiring Ness:

- **Maintenance timeout duration:** set empirically after observing actual
  maintenance operation durations in deployment. The architecture supports any
  value; the value itself is a calibration decision.
- **Hardware-backed key implementation:** the specific mechanism for the
  manifest-signing key and the rollback-sealing key (TPM sealed keys, HSM,
  OS secure key store, or equivalent on Ness's motherbase hardware) is chosen
  at build time based on available hardware. The architecture requires
  hardware-backed separation; which specific mechanism is used is a build
  decision.

---

---

# 1. BOP — Behavioral Observation Processing

**ACCEPTED DESIGN — NOT YET BUILT**

## What BOP Is and Is Not

BOP is the set of rules that decide when something that happened during an
authorized session should be recorded as a behavioral observation root, what
fields it carries, and how it enters the shared store through §7E. BOP produces
only typed raw roots. It does not interpret. It does not conclude. It holds no
data of its own. It is a source-classification and capture-normalization
processing responsibility.

BOP is not a store, not a model of Ness, not a pattern system, not an analysis
layer, and not a classifier of meaning. All interpretation belongs to §7G.

## What Counts as a Behavioral Observation

A behavioral observation is any event that occurred during an authorized session
that is directly and physically measurable without interpretation. The test is
§7E's enrichment boundary test: does this describe what physically happened, or
does it explain what it means? If it explains meaning, it is not a BOP
observation.

**Authorized session definition:** any session explicitly opened by Ness with
N.H is authorized for behavioral observation. During an authorized session, N.H
may automatically record all available authorized signals as observations.

**Authorized signal sources:** live voice mode during an active session;
confirmed sent text during an active session; session-level state events;
imported authorized content when explicitly imported by Ness. Unfinished typing
is never observed. Signals from unauthorized sources are never observed.

## V1 Controlled Event Type Vocabulary

All event types carry physical descriptions only. The vocabulary is extensible
via the `extended` event type using a registered `extended_event_type_id`.

**Voice events** (live voice mode or authorized imported recordings):
- `voice_onset` — a vocalization began; role field identifies whose voice
- `voice_offset` — a vocalization ended
- `silence_interval` — a silence interval; duration only; no judgment
- `non_word_sound` — a non-language sound; physically typed as `breath` or
  `non_breath_non_word` only
- `voice_overlap` — two voice channels simultaneously active
- `voice_interrupt_of_nh` — Ness's voice began while N.H's TTS was active;
  carries timestamp and position in N.H output stream
- `pitch_measurement` — raw pitch values [hz_min, hz_max, hz_mean] for an
  interval; measurement_method and measurement_version required; no emotional label
- `amplitude_measurement` — raw amplitude/energy for an interval; same
  provenance requirements

**Text events** (confirmed sent messages only):
- `text_message_sent` — confirmed sent; carries character_count, word_count,
  sentence_count_approx, exact_text_reference (root id of the conversational
  root carrying content; BOP does not copy message content)
- `text_response_timing` — raw ms delta between N.H output completing and this
  message; reference to the N.H output event
- `no_response_session` — session opened and closed with zero sent messages

**Interface and system command events** (deterministic interface events only):
- `system_command` — a defined interface command; carries command_identifier
  from the interface command registry; no interpretation of ordinary language

**Session state events:**
- `session_opened`, `session_closed`, `session_interrupted`, `function_started`,
  `function_completed`, `function_interrupted`, `capture_failure`

**Import events:**
- `import_authorized`, `import_processed`

**Extended event type:**
- `extended` — for newly measurable authorized signals not in v1; carries
  `extended_event_type_id` (registered before first use) and `raw_payload`

## Observation Root Schema

Base 7 fields (existing sealed schema, unchanged):

```
id:            corrected capture_id (see below)
subject:       "bop:v1"
timestamp:     BOP capture time (distinct from event_occurred_at in payload)
content:       BOP payload serialized as string
re_reads:      []
source_title:  session grouping key using existing source_title rules
role:          "ness" | "nh" | "session" | "third_party_observed"
```

BOP payload inside `content`:

```
bop_payload
  bop_schema_version:      "bop_v1"
  event_type:              string from controlled vocabulary or "extended"
  extended_event_type_id:  string or null
  extended_event_type_version: string or null
  event_occurred_at:       ISO 8601 — when the event happened
  event_duration_ms:       integer or null
  session_id:              stable identifier for the authorized session
  session_mode:            "voice" | "text" | "imported_audio" |
                           "imported_video" | "imported_text" | "mixed"
  session_authorization:
    authorization_type:    "live_session" | "manual_import" |
                           "enrollment_declared"
                           [enrollment_declared: formally adopted vocabulary
                           addition — see section 12]
    authorization_event_id: reference to the authorization event root id
  participants:            list of participant_record objects
  signal_measurements:     object containing raw physical measurements;
                           structure varies by event_type; no interpreted label
  simultaneous_bundle_id:  string or null
  simultaneous_bundle_position: integer or null
  observation_quality:     object (see below)
  third_party_flag:        object (see below)
  connection_anchors:      list of anchor_record objects (may be empty)
  bop_processor_version:   string
  capture_method:          "live_capture" | "import_processing" |
                           "session_state_event"
  capture_sequence_number: integer — monotonically increasing within session;
                           used in capture_id construction
```

## Corrected Capture ID

```
capture_id = stable_hash(
  session_id,
  event_type,
  event_occurred_at,
  event_duration_ms,         (or "null" if absent)
  capture_sequence_number,   (unique within session)
  bop_processor_version
)
```

`capture_sequence_number` must be persisted in a local durable log before any
write is attempted, ensuring idempotency across retries.

## Observation Quality

```
observation_quality
  signal_quality:          "clean" | "partial" | "degraded" | "reconstruction"
  signal_quality_note:     string or null
  field_completeness:      list of field_status records:
    field_name, status, status_note, fallback_value_used, fallback_basis
  overall_completeness:    "complete" | "partial" | "minimum_viable" |
                           "below_threshold"
```

All roots including below-threshold enter the sealed root store. Incompleteness
is recorded honestly; the Meaning Engine may return insufficient_context.

## Third-Party Flag

```
third_party_flag
  third_party_present:           boolean
  third_party_content_present:   boolean
  third_party_handling:          "ness_only" | "third_party_presence_noted" |
                                 "third_party_content_reference"
  privacy_rule_version:          string
```

§7Q's sensitivity levels, deletion framework, and pre-output review apply to
BOP roots identically to any other root.

## Multiple Simultaneous Signals

One observation root per signal channel. All roots from the same simultaneous
moment share the same `simultaneous_bundle_id`. The bundle is reconstructible.
Separate roots per channel preserves the sealed root schema's single-role
constraint.

## Later Reconnection

Connection anchors are optional retrieval aids. Any root is reconnectable
through §7H condition-based rereads and §7F semantic retrieval regardless of
whether anchors were pre-registered. Anchors may be empty.

## DUMB Boundary — What BOP Must Never Produce

BOP must never produce: emotional labels, identity conclusions, speaker-change
detections, spoofing assessments, meaning attributions, pattern conclusions,
importance judgments, or any field that requires reasoning about why something
happened. All of these belong to §7G or SIA.

## Failure, Recovery, Idempotency

On capture failure: `capture_failure` event root written; gap recorded honestly.
On write failure after capture_id computed: retry uses same capture_id;
`append_root()` absorbs duplicate. On crash mid-session: `session_interrupted`
event root written on restart; observations not captured before crash are not
reconstructed.

## Proposed BOP Schema Amendment (Pending Separate Review)

`acoustic_condition_notes` field for voice channel `signal_measurements`: a
list of named physical condition records, each carrying condition_name,
detection_method, detection_version, threshold_value, measured_value,
certainty. Condition names are deterministic physical classifications only
(`high_ambient_noise`, `close_microphone`, `far_microphone`,
`room_reverb_present`, `signal_compression_heavy`). Each carries the numeric
threshold and measured value so the classification is reproducible. This
amendment requires separate consistency review before adoption.

---

---

# 2. Other-Speaker / Guest / Known-Person Architecture

**ACCEPTED DESIGN — NOT YET BUILT**

## Core Principle

The whole N.H mechanism remains active at every access level. Speaker access
control gates what may be surfaced to the current speaker — not what the
mechanism holds or processes internally. Internal understanding and external
disclosure are permanently separate.

## Protected Rules (Unconditional)

- Guest speakers cannot access private Ness memory.
- Uncertainty reduces access; it never expands it.
- Voice alone cannot unlock top-security information.
- Top-security always requires both fingerprint verification and independently
  sufficient active-speaker SIA confidence with no disqualifying suspicion.
- Hidden information must not be indirectly acknowledged.
- One person's permissions must not transfer to another.
- N.H may use information internally only within privacy and authority rules.
- Internal understanding does not equal permission to reveal.
- Other people cannot change permissions, memories, security rules, system
  authority, or N.H's behavior.
- Ness also cannot override the protected architectural core, immutable roots,
  provenance, or non-negotiable safeguards.
- N.H is not a Truth Engine. Claims remain attributed to their speakers.

## Access Levels

Four levels, determined by SACL from SIA's output. The whole mechanism is
active at all levels; only permitted disclosure changes.

- **top_security:** biometric verified + Ness recognized at high certainty + no
  spoofing suspicion
- **recognized_ness:** Ness recognized at threshold certainty + no disqualifying
  suspicion; no biometric required
- **known_person:** confirmed non-Ness Person-Box recognized at threshold + valid
  active PBR
- **guest:** all other conditions

## Guest Mode

Uses general conversational capabilities. No material from the shared store
containing Ness-personal content is accessible. N.H does not say "I cannot tell
you" or signal hidden material exists. It responds naturally from available
content.

## Known-Person Permissions

Permission Boundary Records (PBRs) are maintained by the mechanism under
protected authority rules, informed by Ness's expressed boundaries and learned
evidence. No other person has authority over PBRs. Ness may express boundaries
directly; the mechanism learns and adapts these under §7P authority rules.
Neither Ness nor anyone else may override the protected core.

Permission categories (open-ended vocabulary, initial list): `family_information`,
`health_information`, `nh_project_information`, `creative_projects`,
`current_plans`, `shared_memories`, `practical_information`.

## Separate Parent Identities

Each parent has a fully separate Person-Box, voice profile, behavioral pattern
readings, PBR, relationship context in §7D, and translation behavior history.
N.H never treats parents as one combined person.

## Parent Translation

Entirely request-driven. N.H never autonomously joins, intervenes in, or
redirects a family conversation. Translation is requested by Ness:

- "What did [parent] mean?" → Meaning Engine reading of parent's statement,
  delivered to Ness only, labeled as N.H's interpretation with uncertainty.
- "How should I say X to [parent]?" → candidate wordings delivered privately to
  Ness; N.H does not speak to the parent.
- Ness asks N.H to speak to a parent → N.H delivers the requested content with
  automatic tone/wording adaptation within the request scope.

Translation output is a reading in the shared store, revisable through §7H.
N.H may use private Ness context internally for translation understanding;
disclosure to the parent is bounded by the parent's PBR categories.

## Statements About Ness

A third party's statement about Ness remains attributed to that speaker throughout
the entire path — in the TSC, in the promoted root, in the Meaning Engine reading.
It never silently becomes a fact about Ness. Later evidence may trigger §7H
rereads. The original root and reading are never altered.

## Person-Box Visibility

Another person may not inspect their full Person-Box, hidden readings, private
observations, internal relationship models, or stored security information.
N.H answers only from what their current access level permits. N.H must never
reveal how much it has stored or how recognition works.

## Temporary Session Cache

Third-party session material enters a Temporary Session Cache (TSC) rather than
the long-term shared store. The TSC uses §7E's pre-ingest holding area with a
new blocker: `pending_fingerprint_authorization`. Held material is invisible to
the Meaning Engine while held. The cache preserves complete session context
including Ness's words when they give meaning to another person's statements.

TSC lifecycle: `active` → `sealed` (on session close) → `authorized` (after
fingerprint) → `promoting` → `promoted` or `promotion_failed`.

## Fingerprint-Authorized Batch Promotion

Ness provides a thumbprint in a later session. This authorizes the complete
pending TSC from the relevant completed session. Ness does not select individual
people, memories, or items. The relevant session's cache is the authorization
unit. Unrelated sealed caches from other sessions are not automatically promoted.

After authorization: all items in the cache with no remaining blockers proceed
through §7E → sealed store → §7G → readings → §7J → §7M → §7L proposals. No
additional manual Ness approval is required after the fingerprint authorization.
The mechanism processes the material under its settled evidence rules.

## Continuous Speaker Security

SIA assesses identity continuously throughout a session. SACL applies the
fail-closed rule: uncertainty reduces access, never expands it. Speaker changes
trigger immediate access recalculation. Spoofing suspicion at medium or higher
drops access to guest immediately and queues a private Ness alert. No routine
live voice challenges are issued.

---

---

# 3. SIA — Speaker Identity Assessment

**ACCEPTED DESIGN — NOT YET BUILT**

## What SIA Is and Is Not

SIA assesses who is probably speaking and whether incoming audio shows
characteristics of replayed, synthetic, converted, or non-live audio. It does
not make access decisions (SACL does). It does not interpret meaning (§7G does).
It does not store content. It reads BOP roots and produces identity assessments
and security audit events.

## Speaker Session State (SSS)

In-memory, maintained throughout the active phone session. On restart, SSS is
lost and all streams default to unknown/guest assessment.

```
speaker_session_state
  session_id
  session_mode:             "voice" | "text" | "mixed"
  active_voice_stream_set:  list of voice_stream_record
  primary_addressed_stream: stream_id of stream N.H is responding to
  biometric_state:          "verified" | "not_verified" | "expired"
  biometric_verified_at:    timestamp or null
  assessment_history:       append-only list within the session
```

## Voice Stream Record

```
voice_stream_record
  stream_id
  onset_event_id:           BOP root id of the voice_onset that opened this stream
  speaker_assessment:       speaker_assessment object
  anti_spoofing:            anti_spoofing_assessment object
  stream_status:            "active" | "paused" | "ended"
  last_assessment_at:       timestamp
  last_assessment_trigger:  named trigger
```

## Speaker Assessment Object

```
speaker_assessment
  identity_candidates:      ranked list — all Person-Box candidates above
                            minimum reporting threshold; none silently discarded:
    candidate_record:
      person_box_id
      match_score:          [0.0, 1.0]
      evidence_dimension_scores:
        voice_acoustic_match
        behavioral_pattern_match
        branch_continuity_score
        session_continuity_score
        timing_rhythm_score
        wording_pattern_score
        device_biometric_state: "verified" | "not_verified" | "expired"
      uncertainty_flags:    list of named flags for this candidate
      profile_status:       "enrollment_provisional" | "enrollment_active" |
                            "calibrated" | "stale" | "absent"

  assessed_person_box_id:   leading candidate id, or null when:
                            (a) no candidate reaches minimum certainty, or
                            (b) leading candidate lacks sufficient score
                                separation from competing candidates
  assessed_certainty:       [0.0, 1.0] or null when assessed_person_box_id null
  active_flags:             union of flags active across leading and near-competing
                            candidates; vocabulary:
                            "speaker_change_possible"
                            "spoofing_suspected"
                            "imitation_risk"
                            "profile_provisional"
                            "profile_stale"
                            "low_evidence"
                            "degraded_signal_conditions"
  profile_status:           status of leading candidate's profile or null
```

`assessed_person_box_id` is null whenever two candidates are within the minimum
separation threshold. SACL treats null as unknown and applies guest.

## Anti-Spoofing Assessment Object

Contains only evidence that audio may be replayed, synthetic, converted, or
non-live. Conversational divergence does not appear here.

```
anti_spoofing_assessment
  suspicion_level:          "none" | "low" | "medium" | "high"
  suspicion_basis:          list — acoustic spoofing signals only:
                            "playback_artifact_detected"
                            "compression_artifact_detected"
                            "synthetic_speech_trace"
                            "microphone_room_inconsistency"
                            "pattern_too_uniform"
  suspicion_source:         reading ids that produced these assessments
  assessment_certainty:     [0.0, 1.0]
```

`branch_discontinuity`, timing changes, wording differences, and conversational
divergence are NOT in anti_spoofing_assessment. They appear in
`evidence_dimension_scores` within `identity_candidates` or in a separate
imitation-risk assessment.

## SIA Output Interface

SIA produces one output per assessment cycle. Contains no access decisions.

```
SIA_output
  speaker_session_state:      full SSS object
  assessment_event_id:        stable id for this assessment cycle
  assessment_confidence_note: "normal" | "degraded_conditions" |
                              "provisional_profile" | "low_evidence"
                              — audit label only; not used as decision input
```

## Assessment Update Cadence

Assessment runs continuously across bounded audio windows while speech is
active, and on each named trigger:

- `voice_onset`
- `acoustic_window` — periodic update while stream is active; window size is
  empirical implementation decision
- `meaningful_acoustic_change` — significant shift in acoustic measurements
- `overlap_detected`
- `speaker_transition`
- `confirmed_text_sent`
- `biometric_event`
- `session_state_change`

## Diarization

SIA maintains a `voice_stream_record` per detected voice stream. Multiple
parallel streams exist during overlap or interruption. Each is assessed
independently. If two profiles produce similar scores, both are reported;
`assessed_person_box_id` may be null rather than silently resolved.

## Voice Profile Architecture

Profiles are sets of readings in the shared store linked to a Person-Box through
§7L. All profiles use a common technical embedding space for comparison. What is
protected is the separation of identity authority: no merged profiles, no shared
identity authority, no silent reassignment. Each comparison is independent.

## Natural Voice Variation

Voice profiles represent a range, not a fixed point. Readings from BOP roots
across varied conditions (time, room, device position, state) build the range.
When voice acoustic match drops but other dimensions remain strong, combined
certainty may remain above threshold. Physical acoustic conditions (from the
proposed `acoustic_condition_notes` BOP amendment) contextualize low match
scores.

## Training Eligibility Rules

A BOP acoustic root may contribute to a voice profile only if all of these hold:

1. Produced during an authorized session.
2. SIA certainty for this stream at capture time ≥ training_eligibility_threshold.
3. Anti-spoofing suspicion_level = "none" at capture time.
4. Not flagged in the security audit log with spoofing-related events.
5. For Ness's profile: session was biometric-verified or recognized_ness level
   continuously throughout, with no identity uncertainty flags.
6. Root has completed §7E → §7G reading path before contributing.

Psychiatric or medical appointment records are not voice-identity training
evidence.

## The 6–10 Month Learning Period

During calibration: certainty thresholds set conservatively; recognized_ness is
the maximum achievable level for a provisional profile; behavioral, branch, and
contextual dimensions carry proportionally more weight than voice acoustic match.
Conservativeness reduces gradually as evidence accumulates.

## Raw Voice Data Protection

Raw acoustic roots are in the sealed root store (Layer 3 Full Protected). Voice
profile readings are in the readings store under the same protection rules. No
voice profile reading, acoustic root, or anti-spoofing reading is accessible at
access levels below recognized_ness. Never transmitted outside the local device
except through the Full Mode tunnel under biometric-verified conditions.

## Identity Uncertain vs. Spoofing Suspected

These are distinct events with distinct responses:

- **Identity uncertain:** certainty below threshold; may be natural variation,
  unknown speaker, noise. No private Ness alert. SIA continues assessing; may
  recover naturally.
- **Spoofing suspected (low):** acoustic evidence present. Access drops to guest.
  No alert yet. SIA monitors closely.
- **Spoofing suspected (medium or high):** access drops to guest immediately.
  Top-security relocks. Private Ness alert queued. No routine voice challenge.

## False Lockout Recovery

Primary: thumbprint verification. Biometric success satisfies the biometric
factor. Top-security requires biometric AND independently sufficient speaker
recognition AND no spoofing flag — fingerprint alone does not restore top-security
if speaker assessment remains uncertain or suspicious.

No routine voice challenges are issued. System monitors and updates naturally, or
Ness uses the thumbprint.

## Multi-Speaker State

`active_voice_stream_set` holds one `voice_stream_record` per detected stream.
`primary_addressed_stream` identifies who N.H is responding to.

SACL uses SIA's multi-stream output to calculate per-stream access levels and
the shared-output level (minimum of all active streams for content visible to
all). SACL owns those calculations; SIA provides the evidence.

## Minimum Evidence for Person-Box Linking

Before an unknown speaker may be linked to a Person-Box:
1. Minimum quantity of attributed voice material across authorized sessions.
2. Attribution certainty above minimum at time of capture.
3. No spoofing flags on attributed material.
4. Material promoted from TSC through fingerprint-authorized path and processed by §7G.
5. §7G readings support the connection above minimum reading confidence.
6. §7L proposal-based creation rules satisfied; no silent merge.

## Compact Profile Representation

Derived from authoritative readings; non-authoritative; locally protected;
versioned; rebuildable from source readings; never replaces original evidence;
invalidated when source readings change or become stale. Not a second profile
store. Used at inference time only.

## Settled Rules

- Routine live voice challenges are prohibited.
- Medium-or-higher spoofing suspicion: access drops to guest silently; private
  Ness alert queued; no in-conversation indication.
- SIA assesses identity and suspicion only. SACL decides access.

---

---

# 4. SACL — Speaker Access-Control Layer

**ACCEPTED DESIGN — NOT YET BUILT**

## What SACL Is and Is Not

SACL receives SIA's assessments and decides what the current speaker is permitted
to receive or do. It owns all authorization decisions. It does not assess identity,
perform acoustic analysis, interpret meaning, retrieve content, or generate output.

The whole N.H mechanism remains active at every access level. SACL controls what
may be surfaced — it does not create a reduced version of N.H.

## SACL-Owned State

```
SACL_session_state
  session_id
  last_sia_event_id
  last_sia_received_at
  stream_authorization_set:  list of stream_authorization_record
  primary_addressed_stream
  shared_output_level:       minimum access level across all active streams
  shared_output_level_since
  in_progress_operations:    list of in_progress_operation_record
  last_audit_event_id
```

```
stream_authorization_record
  stream_id
  person_box_id:             or null
  stream_access_level:       "top_security" | "recognized_ness" |
                             "known_person" | "guest"
  stream_access_level_since
  pbr_version:               or null
  ness_presence_satisfied:   boolean
  active_disqualifiers:      list of named conditions preventing level from rising
```

## Access Level Calculation

Calculated per-stream on every SIA assessment event. `shared_output_level` is
the minimum across all active streams.

**Gate 0 — Disqualifier check (acoustic spoofing only):**

Triggers on:
- `anti_spoofing.suspicion_level = "medium"` or `"high"`
- `active_flags` contains `"spoofing_suspected"`

Result: `stream_access_level = "guest"`. Medium-or-higher suspicion additionally
queues private Ness alert. STOP.

The `"imitation_risk"` flag does NOT trigger Gate 0.

**Gate 1 — top_security:** requires ALL of:
- `biometric_state = "verified"` within timeout
- `assessed_person_box_id` = Ness's Person-Box
- `assessed_certainty` ≥ top_security_certainty_threshold
- Leading candidate has sufficient score separation
- `anti_spoofing.suspicion_level = "none"`
- No active disqualifiers
- `active_flags` does NOT contain `"imitation_risk"`

**Gate 2 — recognized_ness:** requires ALL of:
- `assessed_person_box_id` = Ness's Person-Box
- `assessed_certainty` ≥ recognized_ness_certainty_threshold
- Leading candidate has sufficient score separation
- No disqualifying spoofing or imitation-risk flags
- No active disqualifiers

The `"imitation_risk"` flag blocks Gate 1 only. It does not reduce Ness to guest.
Natural behavioral divergence from stress, illness, or emotion produces
imitation_risk without triggering Gate 0.

**Gate 3 — known_person:** requires ALL of:
- `assessed_person_box_id` = confirmed non-Ness Person-Box
- `assessed_certainty` ≥ known_person_certainty_threshold
- Sufficient score separation
- Valid active non-revoked PBR exists
- Ness-presence requirement satisfied if PBR requires it
- No active disqualifiers

**Else:** `stream_access_level = "guest"`

All thresholds are empirically calibrated configuration values.

## Fingerprint as One Independent Factor

`biometric_state = "verified"` satisfies the biometric factor only. Gate 1
requires this plus independently sufficient speaker recognition. If the active
speaker remains uncertain or suspicious after fingerprint success, top-security
remains locked. Fingerprint alone does not restore top-security.

## Imitation Risk Policy (Ness's Decision — Option A)

Conversational or behavioral imitation risk blocks top-security only. It does
not reduce Ness to guest and does not remove recognized_ness access. Natural
causes of behavioral divergence — stress, tiredness, illness, emotion, overload —
may produce the imitation_risk flag without any attack occurring.

## Three Mechanisms Kept Separate

- **SIA:** who is probably speaking; does audio show non-live characteristics?
- **§22 Wellbeing Baseline:** is Ness showing sustained divergence across
  multiple sessions? Its tiered actions affect REALITY growth only. It does not
  erase identity, convert Ness to guest, or suppress SIA recognition.
- **SACL:** based on identity and security evidence, what may be revealed?

SACL does not read wellbeing tier state. One unusual session is not a wellbeing
security event. Behavioral divergence follows the imitation-risk path; acoustic
spoofing follows Gate 0. These paths never merge.

## Multi-Speaker Sessions

`shared_output_level` = minimum across all active streams.
Per-stream private output (e.g. translation to Ness only) may use the individual
stream's access level if the output path is private and unobservable by others.

Ness-presence requirement: when a known person's PBR has `ness_presence_required
= true`, elevated access applies only while a Ness stream is active at
recognized_ness or above. If Ness's stream drops below that level, the known
person's stream drops to guest simultaneously.

## Permission Boundary Enforcement

SACL reads PBRs via LMAC → §7L at Gate 3. Per-output permission category check
runs at output time against `permission_categories` in the active PBR. No content
outside permitted categories is surfaced to the known-person speaker. SACL holds
a cached copy of each recently-used PBR; refreshed when PBR version changes.

## Access Changes During In-Progress Operations

On any access reduction: SACL compares new level against each in-progress
operation's `material_sensitivity`. If the new level is below material_sensitivity,
the operation is flagged for immediate discard. The output-generation component
receives a discard signal before any output channel is written. No partial output
from a higher-sensitivity operation is delivered.

## Avoiding Indirect Disclosure

SACL specifies the permitted access level and permission categories to LMAC
when initiating context retrieval for any function. LMAC queries the shared
mechanism only for material within those boundaries. The content-generation
component never sees content above its permitted level and cannot reveal its
existence — not through direct statement, not through structural gaps, not through
implied omission.

## Output Gate (Two Factors, Sequential)

1. §7Q privacy gate — must pass.
2. SACL access gate — content must fall within current access level and (for
   known_person) permitted PBR categories.

If either gate fails: content withheld. Response generated from permitted content
only. No signal that more exists.

## Internal Context vs. External Disclosure

SACL controls what may be revealed or done for the current speaker. It does not
make the whole mechanism blind to protected context when internal processing is
permitted. The complete shared mechanism remains active internally. Only permitted
information and actions may reach the current speaker through the output gate.

## Background Functions

Background functions operate according to their own purpose, authority, privacy,
and function rules. They do not become guest-level merely because no active
speaker stream is present. A background function authorized during a Ness session
continues under those rules unless a specific security event revokes that
authorization.

## Failure, Stale Assessments, Fail-Closed

On SACL restart: all streams → guest; all in-progress operations discarded.
On stale SIA assessment: all streams above guest downgraded; disqualifier
`"assessment_stale"` added; SACL continues at guest until fresh SIA output arrives.
On SIA component failure: all streams → guest; audit event written immediately.
On PBR query failure: Gate 3 fails closed; stream → guest.

## Protected-Core Rules (Unconditional)

- Voice alone never unlocks top-security.
- Unknown or uncertain speakers receive guest unconditionally.
- Medium-or-higher spoofing: guest + Ness alert, unconditionally.
- No routine live voice challenges.
- Other people cannot change permissions or security levels through SACL.
- Ness cannot override protected architectural safeguards through SACL.
- Hidden information is never indirectly acknowledged.

---

---

# 5. Wellbeing / Identity / Security Separation Rules

**ACCEPTED DESIGN — NOT YET BUILT**

These three mechanisms are kept strictly separate:

**SIA:** who is probably speaking; does audio show non-live characteristics?
SIA never diagnoses wellbeing. SIA never produces conclusions about Ness's mental
or physical state.

**§22 Wellbeing and Behavioral Baseline System:** is Ness showing sustained
divergence from his own demonstrated long-term baseline across multiple sessions
and types of interaction? One unusual session is treated as possible noise. Tiered
actions: silent flag → mirror signal → REALITY promotion throttling → REALITY
promotion freeze. These affect REALITY growth and integrity only. They do not
erase Ness's identity, remove SIA's recognition, convert Ness to guest, or
suppress recognized_ness access. Dry mode, research, and normal thinking-partner
operation remain available.

**SACL:** based on current identity and security evidence from SIA, what may be
revealed or done for the current speaker? SACL does not diagnose wellbeing. SACL
does not read wellbeing tier state. SACL does not treat behavioral divergence
captured in SIA's identity dimensions as acoustic spoofing evidence.

**Psychiatric and medical appointment records:** wellbeing calibration anchors
and the REALITY-freeze unlock mechanism only. Not voice-identity training
evidence. Not identity proof. Not access-control evidence.

**Temporary off-baseline behavior:** tiredness, stress, illness, or emotion may
produce SIA's `"imitation_risk"` flag. SACL applies Option A: top_security
blocked; recognized_ness remains. The wellbeing system observes the session as
one data point. No automatic guest downgrade. Ness retains recognized_ness
access and full thinking-partner capability.

**Acoustic spoofing:** SIA produces `suspicion_level = "medium"` or `"high"` in
`anti_spoofing_assessment`. SACL Gate 0 fires: stream → guest, top-security
relocks, private Ness alert queued. This is a security event. The wellbeing
system is uninvolved.

The two paths — behavioral divergence (imitation-risk) and acoustic spoofing
(Gate 0) — never merge. SACL never conflates them.

---

---

# 6. BAI — Biometric Authorization Interface

**ACCEPTED DESIGN — NOT YET BUILT**

## What BAI Is and Is Not

BAI is the narrowest possible interface between the phone's native biometric
hardware and N.H. It receives OS authentication results. It produces
purpose-bound, one-time-use authorization tokens (or a revocable top-security
lease) containing no biometric data. It owns no fingerprint data at any stage.

BAI is not an authentication system, not an access-control system, and not a
session manager. It receives, binds purposes, creates local proofs, and audits.

## What BAI Receives From the OS

```
os_biometric_result
  outcome:          "success" | "failure" | "cancelled" | "timeout" |
                    "lockout" | "error"
  os_error_code:    string or null — audit only; never exposed to components
  os_lockout_type:  "temporary" | "permanent" | null
```

No OS-provided timestamps or device-id fields are relied upon. BAI uses only
its own trusted local clock.

## Purpose Binding

Purposes are declared and recorded before the OS prompt is shown. One pending
record exists at a time.

```
pending_authorization_record
  pending_id:           uuid4 — generated by BAI before OS prompt
  challenge:            cryptographically random nonce — generated by BAI
  purpose:              declared purpose identifier
  requester:            named component
  requested_at:         N.H trusted local clock
  expires_at:           requested_at + pending_expiry_window
  status:               "pending" | [terminal states]
  app_session_key_ref:  reference to hardware-backed key for this app instance
```

Device and app trust is bound through a hardware-backed key in the phone's
secure keystore, not through OS-provided device-id fields.

**Purpose vocabulary:**
- `"top_security_access"`
- `"tsc_promotion:<session_id>"`
- `"voice_enrollment_ness"`
- `"bgmm_confirmation:<session_id>:<purpose>"`
- `"extended:<purpose_id>"`

## Two Distinct Artifacts

### One-Time Authorization Token

For TSC promotion and voice enrollment:

```
one_time_authorization_token
  token_id, pending_id, challenge, purpose, authenticated_at, created_at,
  expires_at, status: "valid" | "consumed" | "expired" | "revoked"
```

Lifecycle: created on OS success → delivered to requester → consumed before the
protected action begins → permanently unusable. Single-use. Purpose verified
on every consume call.

### Top-Security Biometric Lease

For ongoing top-security access:

```
top_security_lease
  lease_id, pending_id, purpose: "top_security_access",
  authenticated_at, created_at, expires_at,
  status: "active" | "expired" | "revoked",
  session_id
```

Lifecycle: created on OS success → remains active until expiry or revocation →
queried repeatedly by SACL → never consumed; queried, not spent.

## Key Separation

**Manifest-signing key:** signs authorized manifest versions only.  
**Rollback sealing key:** encrypts and integrity-protects rollback packages only.

Neither key is derivable from the other. Neither private key is exportable or
written to any log. Compromise of one does not compromise the other. Specific
hardware implementation is a build-time decision.

## Result Handling

Success with matched pending record within expiry → create appropriate artifact
(lease or one-time token) → write audit events → deliver to requester.

No matching pending record (expired, absent, or device mismatch) → reject;
write `bai_unmatched_result`; no artifact created.

All non-success outcomes (failure, cancelled, timeout, lockout, error) → pending
record terminal status set → requester notified → audit events written. BAI does
not retry automatically.

## TSC Promotion Authorization

Requires:
1. Valid unconsumed `one_time_authorization_token` with purpose
   `"tsc_promotion:<session_id>"`.
2. At consume time: SACL reports that the current session holds a fresh
   non-stale recognized_ness assessment for the Ness stream.

If either condition is not met, token is not consumed; promotion does not proceed.

Conditions that invalidate condition 2: speaker change detected; SIA assessment
stale; medium-or-higher spoofing suspicion; SACL access for Ness stream below
recognized_ness; session end; relevant security event.

## Lease Revocation Triggers

Any one fires immediately:

- Session close
- `assessed_certainty` drops below recognized_ness_threshold
- Any active spoofing, speaker-change, or imitation-risk flag at security level
- Anti-spoofing suspicion_level rises to medium or above
- Timeout since `authenticated_at`
- Major session break
- Branch continuity below threshold
- Explicit relock from SACL

## BAI-Owned State

In-memory only. Nothing persists across restarts.

```
BAI_state
  pending_record:           single pending record or null
  active_lease:             top_security_lease or null
  active_one_time_tokens:   map of token_id → one_time_authorization_token
  lockout_state:            "none" | "temporary" | "permanent"
  lockout_since:            timestamp or null
  app_session_key_ref
  session_id
  last_audit_event_id
```

On restart: all state cleared; biometric_state → not_verified; Ness
re-authenticates. Fail-closed.

## BOP vs. Security Audit Separation

**BOP system_command roots record only:** prompt_opened; result:success;
result:failure; result:cancelled; result:timeout; result:lockout; result:error.
Each carries only session_id and N.H local clock timestamp. No token_id, no
challenge, no purpose, no authorization conclusions.

**Security audit log records:** all purpose binding, challenge creation, token
and lease creation, consumption, revocation, purpose mismatch, requester
identity, and security-policy consequences.

## Crash, Duplicates, Delayed Events, Malformed Results

On restart: BAI_state cleared; `bai_restart_state_cleared` written.
On delayed result: no matching pending record; rejected as `bai_delayed_result_rejected`.
On duplicate result: pending record already resolved; rejected as `bai_duplicate_result_rejected`.
On malformed result: rejected without logging potentially biometric fields; `bai_malformed_result_rejected`.

## Protected-Core Rules

- BAI never receives, stores, inspects, reconstructs, or processes fingerprint
  data.
- A token created for one purpose cannot satisfy another.
- Consumed tokens cannot be reused. Expired tokens cannot be reused.
- One pending record at a time.
- BAI exposes no interface allowing override of immutable roots or protected
  safeguards.
- Wellbeing system not involved in BAI; BAI never queries §22.

---

---

# 7. Initial Owner-Phone Pairing

**ACCEPTED DESIGN — NOT YET BUILT**

## Four States

**State 1 — `qr_available`:**
Desktop has generated the signed QR. Scannable for 90 seconds. No phone paired.

**State 2 — `phone_provisionally_paired_qr_destroyed`:**
First phone pairs successfully. At this exact moment: signed QR and temporary
pairing secret are permanently destroyed. Cannot be scanned, reused, or
regenerated. Desktop binds permanently to phone's hardware-backed cryptographic
identity. Phone holds provisional trusted status only.
Audit event: `bai_qr_destroyed_phone_provisionally_paired`.

**State 3 — `recovery_setup_in_progress`:**
Recovery-code setup begins on the already-paired provisional phone. QR secret
was destroyed at state 2. If setup fails or times out, the phone remains in
state 3, provisionally paired. Ness may retry recovery-code setup on the same
phone. Retrying does not generate or reopen another QR.

**State 4 — `owner_setup_finalized_qr_path_permanently_closed`:**
Reached only after the first recovery code completes all four steps: saved in
Bitwarden, verified through 4-character check, successfully tested through
automatic local acceptance test, and activated. At this moment: phone receives
final permanent trusted-owner status; permanent closure audit event written;
initial QR path closed forever.

**What is destroyed when:**

| Artifact | Destroyed at |
|---|---|
| Signed QR | State 2 — immediately on successful pairing |
| Temporary pairing secret | State 2 — immediately on successful pairing |
| Provisional phone status | Upgraded to permanent at state 4 |
| Recovery code local copy | Immediately after activation at state 4 |

---

---

# 8. Recovery-Code Lifecycle

**ACCEPTED DESIGN — NOT YET BUILT**

## First Recovery Code Creation

Created immediately after the first phone pairs successfully. Never appears on
the desktop or clipboard. Desktop encrypts it using the paired phone's
hardware-backed public key. Only that phone may decrypt it, after biometric
approval.

Code appears on the trusted phone only. Visible until Ness confirms or until
automatic timeout of 10 minutes 30 seconds. On confirmation or timeout, phone
hides code and clears clipboard. If timeout occurs before confirmation, old code
remains valid; new code is not activated.

## Save Verification

After Ness presses "Saved in Bitwarden":
- N.H asks for exactly 4 unique random character positions.
- Ness enters the characters at those positions in exact requested order.
- Matching is exact, including letter case.
- 3 attempts total; each failed attempt uses a new set of 4 positions.
- Verification runs locally.
- Entered characters, requested positions, and comparison results are not stored.
- If all 3 attempts fail: new code destroyed; old code remains valid; rotation
  must restart.

## Activation Handover

After 4-character verification succeeds:
1. Phone performs automatic local test proving new code would be accepted.
2. Test must not change settings, create a recovery event, pair another device,
   or expose the code.
3. Only after local test succeeds does new recovery code become active.
4. Only then does old recovery code become permanently invalid.
5. Phone immediately erases its local copy.
6. Bitwarden is the only intended long-term storage location.

## Recovery Code Rotation

After every successful phone pairing or re-pairing, the normal recovery code
is rotated following the same save-verification-activation sequence. The old
recovery code remains valid until the new one has been saved, verified, locally
tested, and activated.

---

---

# 9. Future-Phone Replacement Flow

**ACCEPTED DESIGN — NOT YET BUILT**

Requires both factors; neither alone is sufficient:
1. Current Bitwarden normal recovery code.
2. Ness's thumbprint through Maintenance Mode on the N.H desktop.

A new phone is a replacement by default. Once fully paired and verified, the
previously trusted phone is automatically revoked. A revoked phone may become
trusted again only through the complete recovery-code + thumbprint pairing flow.

After every successful replacement, rotate the normal recovery code per the
accepted lifecycle.

---

---

# 10. Atomic Emergency Recovery Flow

**ACCEPTED DESIGN — NOT YET BUILT**

## Required Factors

All required simultaneously:
- Physical access to the N.H desktop (motherbase).
- Separate emergency code stored outside Bitwarden.
- Printed recovery sheet stored in a physically secure place.
- Ness's thumbprint on the motherbase through BGMM.

Remote emergency recovery is prohibited unconditionally.

## Intermediate State (Provisional Only)

During the intermediate state:
- New phone is only provisionally paired; no permanent trusted status yet.
- All previously trusted phones remain valid.
- Old normal recovery code remains valid.
- Old emergency code remains valid.
- Old printed recovery sheet remains valid.
- No partial revocation occurs.

## Required Steps Before Final Commit

All of the following must complete successfully:
1. New normal recovery code: saved, 4-character verified, local test passed.
2. New emergency code: saved and verified.
3. New printed recovery sheet: confirmed saved and verified.

## Atomic Final Commit

Only after every required step succeeds, N.H performs one atomic commit:
- New phone becomes sole permanently trusted phone.
- All previously trusted phones permanently revoked.
- Old normal recovery code permanently invalid.
- Old emergency code permanently invalid.
- Old printed recovery sheet permanently invalid.
- All new recovery materials become active simultaneously.
- `bai_emergency_reset_finalized` written.

## If Any Step Fails Before Final Commit

- Emergency reset aborted safely.
- All provisional new material destroyed.
- New phone's provisional pairing cancelled.
- All previously valid trust and recovery material remains valid.
- No partial revocation has occurred.
- `bai_emergency_reset_aborted` written with failed step and reason.

---

---

# 11. Initial Ness Voice-Profile Enrollment Bootstrap

**ACCEPTED DESIGN — NOT YET BUILT**

## Prerequisites (All Six Must Be True)

1. Phone holds final permanent trusted-owner status (BAI state 4).
2. First normal recovery code saved, verified, locally tested, and activated.
3. Original QR and temporary pairing secret destroyed at pairing.
4. Original owner setup finalized; QR path permanently closed.
5. No active medium-or-higher acoustic spoofing suspicion in current session.
6. Ness's Person-Box confirmed in §7L.

## Enrollment Session Opening

Accessible only through the dedicated Owner Setup / Voice Enrollment flow on
the permanently trusted phone. Ness must explicitly choose to begin. On Ness's
choice:

1. Enrollment flow calls BAI request interface with purpose `"voice_enrollment_ness"`.
2. BAI creates pending record; triggers OS biometric prompt.
3. On success: BAI creates `one_time_authorization_token` with purpose
   `"voice_enrollment_ness"`. Single-use, short-lived.
4. Enrollment flow verifies all six prerequisites against current system state
   before consuming.
5. If all satisfied: token consumed. Enrollment session opens.
6. If any prerequisite changed since prompt shown: token revoked without
   consumption; enrollment does not begin.

**What biometric success proves:** an enrolled device biometric on the
permanently trusted phone was accepted. It does not identify Ness by name. The
trusted-phone binding is the outer bootstrap authority. The purpose-bound token
is the inner approval.

## BOP Integration

BOP records only raw voice observations during the enrollment session. Standard
BOP rules apply without exception.

Each root carries:
- `role = "ness"` — the enrollment flow's declared attribution, not a confirmed
  identity assessment.
- `source_title = "enrollment:ness:<session_id>"` — states material came from
  an authorized enrollment session.
- `session_authorization.authorization_type = "enrollment_declared"` — formally
  adopted vocabulary addition (see section 12). Signals to §7G that role
  attribution is a declaration by the enrollment flow, not a confirmed SIA
  assessment.

One BOP `system_command` root from BAI at session open: `command_identifier =
"biometric:result:success"`, carrying session_id and N.H local clock timestamp
only. No purpose, no token_id, no authorization conclusions.

## §7G Integration

Enrollment roots enter the shared store through §7E's standard catalog path after
the enrollment session ends. §7G reads them through the standard reading queue.
Readings go to quarantine. §7G reads `authorization_type = "enrollment_declared"`
and treats `role = "ness"` as the enrollment flow's declared attribution — not
confirmed identity.

Readings reflect honest provisional confidence. They become the initial voice
profile reading set.

## Initial-Corpus Eligibility Rules

Before an enrollment segment's roots may contribute to the provisional profile,
all of the following must hold:

1. One consistent live speaker stream during the segment.
2. No medium-or-higher acoustic spoofing suspicion during the segment.
3. No unresolved overlapping speaker contamination.
4. Sufficient signal quality (overall_completeness = "complete" or "partial").
5. Complete enrollment provenance (authorization_type = "enrollment_declared"
   present; session_id links to confirmed bai_token_consumed audit event).
6. **Stream integrity:** diarization confidence remains above bootstrap
   stream-stability threshold for the full segment duration; no unresolved
   speaker-transition event; no material stream split or merge; no uncertainty
   that a second speaker entered; no medium-or-higher spoofing evidence.
   (Check 6 assesses whether the segment came from one consistent live speaker.
   It does not require SIA to have identified who that speaker is — the profile
   does not yet exist.)

Rejected segments are preserved in the shared store as observation roots. They
do not train the provisional profile. Exclusion is recorded in the enrollment
component's audit log.

## §7L Integration

After sufficient readings are produced, a Person-Box link is proposed:

```
Link type: "enrollment_material_provisional"  [formally adopted — see section 12]
What it means: this material was collected during Ness's authorized owner-enrollment
  flow. It does NOT mean the captured voice has been confirmed as Ness's voice.
Certainty: "enrollment_provisional"
Basis: bai_token_consumed: voice_enrollment_ness + owner_phone_trust:
  bai_initial_setup_finalized + authorization_type: enrollment_declared
```

The link strengthens only through: later SIA evidence, repeated authorized
sessions, anti-spoofing-clean material, candidate separation, and accepted
profile-integrity rules.

## SIA Integration

Once the provisional profile reading set is linked to Ness's Person-Box, SIA
may use those readings as one input. At this stage:
- `profile_status = "enrollment_provisional"`
- Conservative confidence ceiling: recognized_ness is the maximum achievable
  level regardless of voice acoustic match score.
- SIA weights behavioral, branch, session continuity, timing, and wording
  dimensions more heavily than voice acoustic match until profile reaches
  `enrollment_active`.

All subsequent evidence follows standard SIA training eligibility rules without
exception. No shortcut for enrollment roots.

## Audit Event Ownership

BAI-owned: `bai_token_consumed`, `bai_token_revoked` (for this flow).

Enrollment-component-owned:
- `enrollment_prerequisites_verified`
- `enrollment_session_opened`
- `enrollment_session_closed`
- `enrollment_segment_accepted`
- `enrollment_segment_rejected`
- `enrollment_prerequisite_failed`
- `enrollment_token_revoked_prereq_changed`
- `enrollment_provisional_link_proposed`
- `enrollment_provisional_profile_created`

## What Enrollment Does Not Establish

The authorized enrollment provenance permits N.H to create a provisional profile
candidate associated with Ness's enrollment process. It does not establish that
the captured voice belongs to Ness. The association strengthens gradually through
later SIA evidence, repeated authorized sessions, anti-spoofing-clean material,
candidate separation, and accepted profile-integrity rules. No enrollment session
alone establishes that association.

---

---

# 12. Formally Adopted Vocabulary Additions

**ACCEPTED — FORMALLY ADOPTED**

Both vocabulary additions were examined against their parent schemas and formally
adopted within existing open-ended vocabularies. No schema version changes and
no further consistency reviews are required.

## Addition 1: BOP `authorization_type = "enrollment_declared"`

**Location:** `session_authorization.authorization_type` field in the BOP
payload's `session_authorization` object.

**Existing values before adoption:** `"live_session"` | `"manual_import"`

**New value:** `"enrollment_declared"`

**Meaning:** the role attribution in this root was declared by an authorized
enrollment flow; the speaker identity has not yet been independently confirmed
by SIA.

**Fit:** the `authorization_type` field is a controlled vocabulary in an
extensible payload object. This addition follows the established BOP vocabulary
extension mechanism. No structural schema change is required.

## Addition 2: §7L `link_type = "enrollment_material_provisional"`

**Location:** the `link_type` field in §7L Person-Box link records.

**Meaning:** this material was collected during Ness's authorized owner-enrollment
flow. It does not mean the voice in that material has been confirmed as Ness's
voice. The link represents enrollment provenance, not confirmed voice identity.

**Fit:** §7L's link-type field is open-ended by design in the current Master
text. This addition is a new named value within that open-ended vocabulary. No
schema version change and no structural alteration to §7L is required.

---

---

# 13. BGMM — Biometric-Gated Maintenance Mode

**ACCEPTED DESIGN — NOT YET BUILT**

## What BGMM Is and Is Not

BGMM is the only authorized path through which protected N.H material may be
changed. Outside BGMM, protected files are read-only by architectural
enforcement. BGMM does not make N.H more powerful; it makes unauthorized change
structurally harder and always detectable.

BGMM is not a general administrator mode. It does not grant broader access than
the declared purpose requires. It cannot be entered remotely. It cannot be
entered through ordinary terminal, editor, script, or installer access regardless
of OS privilege level. It cannot override immutable roots, provenance, privacy
rules, or protected architectural safeguards.

## Protected Material Boundary

**Writable only through BGMM:**
- `code_change` — Python source, executable code, .cursorrules, engine config
- `configuration_change` — non-code behavior configuration files
- `security_policy_change` — SACL thresholds, anti-spoofing policy, audit
  retention rules
- `device_trust_change` — trusted-phone binding records, pairing credentials,
  recovery-code authority records
- `emergency_recovery` — device-trust reset per accepted BAI emergency flow only

**Permanently unchangeable even inside BGMM:**
- Immutable roots in the sealed root store
- Reading records and their provenance
- Clash records, Person-Box links and their provenance
- Security audit log entries (append-only; BGMM may not delete or alter)
- Gold set records
- Recovery code values (never stored in N.H)

Existing records are append-only and immutable. New readings, rereads, links,
revisions, and superseding interpretations may still be appended through their
normal architectural mechanisms. BGMM cannot directly create, rewrite, delete,
or "correct" those records. A later record may supersede an earlier interpretation
without altering the earlier record.

## Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)

**Layer 1 — ACLs and service isolation:** ordinary user sessions, terminals,
editors, scripts, and installers are blocked by ACLs and `nh_system` account
isolation.

**Layer 2 — Administrator-level resistance:** a person with full Windows
administrator privileges or offline disk access may be able to take file
ownership or modify files through OS recovery mechanisms. ACLs alone cannot
prevent this. Additional resistance: Secure Boot; TPM-backed trust anchoring
the boot chain; full-disk encryption; signed application-control policy
(Windows Defender Application Control or equivalent); protected service
configuration. These layers raise the cost and detectability of administrator-level
tampering substantially but do not make it physically impossible.

**Layer 3 — Code signing:** all executable N.H code is signed. Runtime verifies
signatures before loading. Unsigned or invalidly-signed modules are rejected.

**Layer 4 — Signed manifest integrity:** all protected files are registered in
a signed manifest. Startup verifies the manifest signature. Any file modified
outside BGMM produces a hash mismatch against the signed manifest.

**Layer 5 — Change-log provenance:** every BGMM change is recorded in the
append-only change log before the change is applied.

The net guarantee: ordinary user paths are blocked. Administrator-level
tampering is substantially resisted and always detected before N.H runs.
Physical attackers with sufficient hardware access may bypass some layers, but
N.H fails closed on any integrity failure.

## Signed-Manifest Trust Anchor

The manifest contains expected hashes and versions of all protected files. After
every authorized change, BGMM signs a new manifest version with the
**manifest-signing private key** (hardware-backed, accessible only within an
authorized BGMM session). The prior signed manifest is appended to an append-only
manifest provenance history — never deleted.

Startup verification: verifier reads the current signed manifest; verifies the
signature against a pinned public key anchored in the TPM or equivalent
hardware-backed trust store (public key does not change when manifest changes);
verifies each protected file's hash against its manifest entry.

If any signature or hash fails: N.H does not start; integrity failure written
to audit log; BGMM is the only authorized repair path.

Rollback: prior file content restored; prior signed manifest version restored
from provenance history after re-verifying its signature.

## Encrypted Full-Content Rollback Packages

Before any protected file is changed, BGMM creates a protected rollback package:

```
rollback_package
  session_id
  change_description:   declared change, for audit linkage
  file_entries:         one per in-scope file:
    file_path
    prior_content:      exact byte-for-byte prior file content
    prior_hash:         SHA-256 of prior content (verification evidence)
    prior_signature:    prior code signature if applicable
    prior_manifest_version
    file_metadata:      permissions, timestamps, attributes for exact restoration
  created_at:           before any write occurs
```

**Rollback sealing key:** separate from the manifest-signing key. Hardware-backed.
Not derivable from the manifest-signing key. Neither private key is exportable
or written to any log. Used only to encrypt rollback packages.

The package is: encrypted using the rollback sealing key; integrity-protected
with a MAC or signature verifiable by BGMM; inaccessible to ordinary users,
applications, terminals, and the normal N.H runtime; persisted before the first
write; deleted only after successful final verification or successful rollback.

## Protected Startup Recovery Worker

After a crash or unexpected restart, a minimal protected BGMM recovery worker
may access the rollback package automatically during verified startup recovery.

Its authority is strictly bounded:
- May decrypt and verify the rollback package under the expected secure and
  measured boot state.
- May restore exactly the files, metadata, prior signatures, and prior signed
  manifest named in that package — nothing else.
- Cannot edit arbitrary files, create a new change, expand scope, export package
  contents, or open a general Maintenance Mode session.
- Access conditional on boot state matching expected measured-boot record and
  package passing full integrity verification before any restoration begins.

After verified rollback succeeds: package securely deleted; `bgmm_rollback_completed`
written.

If decryption, integrity verification, or restoration fails: recovery worker
halts; package not deleted; N.H remains stopped; fails closed until Ness enters
BGMM through the full normal authorization path.

## Entering Maintenance Mode

**Step 1 — Purpose declaration:** Ness declares the exact purpose (one of the
five controlled values) and the specific change in plain language. Recorded
before any authorization step.

**Step 2 — Motherbase thumbprint:** Ness provides thumbprint; BGMM receives
only `"success"` or `"failure"` from the native OS framework.

**Step 3 — Trusted phone confirmation (for code, configuration, security-policy
changes):** motherbase sends purpose-bound confirmation request to the trusted
paired phone. Phone displays declared purpose and change description. Ness
explicitly confirms. Phone requires its own BAI `one_time_authorization_token`
with purpose `"bgmm_confirmation:<session_id>:<purpose>"` before sending
confirmation.

**Step 4 — Recovery code (for device_trust_change):** current Bitwarden normal
recovery code verified locally. Phone confirmation is not required for
device_trust_change — the old trusted phone may be unavailable.

**Step 5 — Emergency factors (for emergency_recovery):** emergency code and
printed-recovery-sheet verification. No trusted-phone confirmation required.

**Step 6 — Maintenance window opens:** scope enforced to exactly declared files
and purpose. `nh_system` write token granted for in-scope files only.

## Purpose-Specific Authorization

| Purpose | Required factors |
|---|---|
| code_change | Motherbase thumbprint + phone confirmation |
| configuration_change | Motherbase thumbprint + phone confirmation |
| security_policy_change | Motherbase thumbprint + phone confirmation |
| device_trust_change | Motherbase thumbprint + Bitwarden recovery code (no phone confirmation required) |
| emergency_recovery | Physical motherbase access + thumbprint + emergency code + printed recovery sheet (no phone confirmation required) |

Emergency_recovery scope is device-trust records only. No code or configuration
files are writable, regardless of what the session declares. The scope-enforcement
guard enforces this unconditionally.

## File Scope Enforcement

The `nh_system` write token is scoped to the exact file list derived from the
declared purpose and declared change. Any write attempt outside this scope is
blocked by the scope-enforcement guard and immediately written to the security
audit log as `bgmm_out_of_scope_write_attempt`.

## Change Application

Before any file is touched:
1. Change-log entry written and flushed.
2. Rollback package created and persisted.
3. Change applied.
4. hash_after computed and recorded.
5. Manifest updated and re-signed with manifest-signing key.
6. Modified executable files re-signed with code-signing key.
7. `bgmm_change_applied` written to security audit log immediately.

If any step fails after the file is touched: rollback triggered immediately.

## Automatic Relocking

Maintenance window closes immediately on:
- Completion (change applied, verified, logged)
- Timeout (expires_at reached)
- Restart or crash
- Security alert from SACL (medium-or-higher spoofing, session-level alert)
- Phone disconnection during an open session
- Explicit Ness abort
- Biometric verification expiry

On any relock: write token revoked immediately; `bgmm_write_token_revoked` written;
rollback triggered if change was partially applied.

## Rollback

Rollback uses the encrypted full-content rollback package. For each file entry:
decrypt package; verify prior_hash against prior_content; restore prior_content;
restore prior_signature and prior_metadata; update signed manifest to prior
signed version from provenance history. Rollback is idempotent — if a file
already matches prior_content, no write occurs.

## BGMM-Owned State

In-memory only across active session. Nothing persists except: the rollback
package (encrypted, deleted after successful completion or rollback); the
change log (append-only, permanent provenance record); the signed manifest and
its provenance history.

```
BGMM_session_state
  session_id, declared_purpose, declared_change, scope,
  authorization_factors, session_status, opened_at, expires_at,
  write_token_active, applied_changes (append-only list),
  rollback_checkpoint (file list and hash_before values — verification reference
  pointing to the encrypted package; hashes alone are not backups)
```

## Privacy During Maintenance

BGMM may not expose protected content merely because Maintenance Mode is open:
- Change descriptions shown to Ness and sent to the phone must not contain
  private content.
- Rollback packages must not expose private content in metadata or audit fields.
- Change log records file paths, operations, and hashes — not file content.
- Security audit events record structural facts only — not content from protected
  files.
- Secrets, private memory, health records, and sensitive content must not appear
  in any maintenance description, log entry, or phone-confirmation payload.

## Immediate Security Audit Events

All events written and flushed before the function that produced them returns.
Key events include: `bgmm_session_initiated`, `bgmm_session_opened`,
`bgmm_write_token_granted`, `bgmm_change_log_entry`, `bgmm_change_applied`,
`bgmm_hash_registry_updated`, `bgmm_out_of_scope_write_attempt`,
`bgmm_session_completed`, `bgmm_write_token_revoked`, `bgmm_rollback_triggered`,
`bgmm_rollback_completed`, `bgmm_rollback_failed`, `bgmm_session_timed_out`,
`bgmm_session_aborted`, `bgmm_integrity_check_failed`, `bgmm_integrity_check_passed`,
`bgmm_immutable_write_blocked`.

## Crash, Restart, Offline Behavior

On crash during open session: state lost; write token revoked by OS process exit;
startup-recovery worker runs rollback from rollback package; `bgmm_rollback_completed`
written before N.H starts.

On crash during rollback: idempotent; restart triggers rollback again from
whatever state files are in.

On integrity check failure at startup: N.H does not start; BGMM entry is the
only authorized repair path.

BGMM operates fully offline. No network required.

## Protected-Core Rules (Unconditional)

- Immutable roots, readings, provenance, audit log: scope enforcement blocks
  all writes; `bgmm_immutable_write_blocked` written if attempted.
- Normal PC access cannot modify protected material: Layer 1 and nh_system token
  enforce this for ordinary users; administrator-level tampering is resisted and
  always detected.
- Maintenance authorization is temporary and purpose-bound.
- Emergency_recovery does not grant code-edit authority.
- Recovery code values are never stored in N.H.

---

*End of NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md*
