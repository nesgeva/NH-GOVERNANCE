# Chapter 4-d — Group B: C-14

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-14 — Chat Front Door (§14), with all its sub-parts. It leaves C-9A to CH04-e, every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-14 — Chat Front Door (§14)
Stamp: DESIGNED    Source: [V10 §14] [MAP C-14]

ALONE
- What it is: DESIGNED — Live conversation as a first-class input front door. [V10 §14] [MAP C-14]
- Takes in: DESIGNED — Every live-chat message, including Ness's words and N.H's earlier output with its source-carried speaker. [V10 §14] [MAP C-14]
- Does: DESIGNED — Captures every message automatically through Catalog, without a manual save marker, and routes eligible material to the one Meaning Engine with creation-aware mode when applicable. [V10 §14] [MAP C-14]
- Gives out: DESIGNED — Captured turns and roots through Catalog; the governing visible point-back surface retains its explicit presentation conflict. [SOURCE CONFLICT: 04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5 specifies no visible clickable point-back] [V10 §14] [MAP C-14]
- Must never: DESIGNED — Guess the speaker, treat N.H's earlier output as fact merely because N.H said it, or narrate the mechanism in ordinary chat. [V10 §14] [MAP C-14]
- Fails closed by: DESIGNED — Uses Catalog's capture-error and holding boundaries; the live-reply relationship to asynchronous reading is not determined by capture completion. [V10 §14] [MAP C-14]

TOGETHER
- Fed by: DESIGNED — C-14.1 — Automatic live-turn capture: supplies automatic capture of each live message. [V10 §14] [MAP C-14]
- Fed by: ACCEPTED — C-14.2 — Live-conversation provenance meaning: supplies the provenance-only meaning of the recorded conversation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fed by: DESIGNED — C-14.3 — Creation-aware live routing: supplies the one-engine creation-aware route. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Fed by: DESIGNED — C-14.4 — Visible point-back: retains the governing point-back surface with the opposing accepted presentation recorded. [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-14.5 — Proposed structured live provenance label: supplies the proposed structured label within capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.6 — B18 earlier-reference detection: supplies reliable internal earlier-reference detection and context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fed by: DESIGNED — C-14.8 — Chat front-door event records: supplies records of actual front-door events. [MAP C-14]
- Fed by: DESIGNED — C-13 — Live Loop (§13): supplies the live-loop surface on which capture rides. [V10 §13] [MAP C-14]
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): applies independent acceptance and creation-aware mode where relevant (CY-B). [V10 §7G] [MAP C-7G]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): enqueues and processes without blocking the root-ingestion starter on the mouth (CY-B). [V10 §7G-A] [MAP C-13]
- Gated by: ACCEPTED — C-14.7 — Shared capture and reference-operation protections: requires its live capture/reference operations to retain the shared operation protections. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): requires standard Catalog capture, privacy, speaker, grouping and root-ingestion eligibility. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | A live turn and its source envelope. | Receives the capture for completeness, holding and eligible root promotion. | Live conversation enters through Catalog's ordinary capture lifecycle. | [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| 2 · DESIGNED | C-13 — Live Loop (§13) | A live turn from the chat front door. | Carries capture, silent context and fresh reply formation on the loop. | The conversation has governed loop behavior without a settled reply/read synchronization rule. | [MAP C-14] [V10 §13] |
| 3 · DESIGNED | C-13 — Live Loop (§13); CY-B | Each live turn with its source provenance. | Captures automatically through Catalog, preserves provisional status and uses only governed earlier-reference context. | The live turn enters the ordinary capture and reading path without settling reply/read synchronization. | [MAP CY-B] [MAP C-14] |

SUB-PARTS: C-14.1 — Automatic live-turn capture; C-14.2 — Live-conversation provenance meaning; C-14.3 — Creation-aware live routing; C-14.4 — Visible point-back; C-14.5 — Proposed structured live provenance label; C-14.6 — B18 earlier-reference detection; C-14.7 — Shared capture and reference-operation protections; C-14.8 — Chat front-door event records

### C-14.1 — Automatic live-turn capture
Stamp: DESIGNED    Source: [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — Capture of each live message as a source turn. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — Each message and its actual source metadata. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Captures automatically, then hands identifiable material to Catalog for completeness and resolution. Supplies stable unique `capture_id`, exact raw payload or immutable reference, capture timestamp, front-door/source type, media type, source metadata without reinterpretation and traceable capture provenance. Live Catalog may ask for necessary speaker or genuinely uncertain grouping clarification; unattended handling holds unresolved material and never asks. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — A Catalog intake with the common seven-element envelope. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Require a manual save marker; guess missing envelope values; silently drop malformed material; confuse raw capture with root eligibility. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Fails closed by: DESIGNED — Sends a malformed capture to the explicit capture-error path with available material preserved; unresolved catalog fields hold root ingestion. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: requires all seven minimum intake-envelope elements before pre-ingest acceptance. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Changes: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): supplies automatic live captures through the ordinary Catalog boundary. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14]
- Changes: DESIGNED — C-7E.3 — Capture-error path: sends malformed captures to the explicit preserved error path. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | A live message with source metadata. | Captures without a manual save marker. | Catalog receives an identifiable intake. | [V10 §14] [MAP C-14] |

SUB-PARTS: NONE

### C-14.2 — Live-conversation provenance meaning
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]

ALONE
- What it is: ACCEPTED — A provenance-only description of recorded live conversation between Ness and N.H. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Takes in: ACCEPTED — Live material and the two source-known speakers. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Does: ACCEPTED — Preserves the distinct speakers and their words, carries speaker identity from source, and leaves topic, meaning, truth and importance unasserted by the provenance label. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Gives out: ACCEPTED — Conversation provenance that does not substitute for a reading. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Must never: ACCEPTED — Guess speaker identity later, treat N.H output as fact through its source alone, or use the label as a semantic or truth judgment. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-14.2.1 — Two source-known speakers: preserves the two source-known speaker origins. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fed by: ACCEPTED — C-14.2.2 — Ness's words remain Ness's: preserves Ness's words as Ness's. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fed by: ACCEPTED — C-14.2.3 — N.H output remains model output: preserves prior N.H output without automatic truth authority. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fed by: ACCEPTED — C-14.2.4 — Speaker carried from source: supplies speaker identity carried from the source stream. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.2.5 — Provenance makes no semantic claim: limits the label to origin rather than semantic judgments. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.2.6 — Topical subject earned by reading: leaves the topical subject to later reading. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: DESIGNED — C-14.2.7 — Source speaker connection: preserves the speaker connection to its source fact. [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | Source-known Ness and N.H contributions. | Preserves the speakers and their distinct evidential status. | The label does not substitute for a reading. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] |
| 2 · ACCEPTED | C-14.5 — Proposed structured live provenance label | The proposed label and source fields. | Keeps structured provenance faithful to its accepted meaning. | The format cannot create semantic or truth claims. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: C-14.2.1 — Two source-known speakers; C-14.2.2 — Ness's words remain Ness's; C-14.2.3 — N.H output remains model output; C-14.2.4 — Speaker carried from source; C-14.2.5 — Provenance makes no semantic claim; C-14.2.6 — Topical subject earned by reading; C-14.2.7 — Source speaker connection

### C-14.2.1 — Two source-known speakers
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]

ALONE
- What it is: ACCEPTED — The two-speaker provenance of recorded Ness/N.H conversation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Takes in: ACCEPTED — Source evidence identifying Ness and N.H as the two speakers. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Does: ACCEPTED — Preserves that the conversation has two source-known speakers. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Gives out: ACCEPTED — Two distinct speaker origins retained in provenance. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Must never: ACCEPTED — Collapse the two speakers into one origin. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | The two speakers' source evidence. | Carries both origins distinctly. | Conversation provenance does not merge the speakers. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] |

SUB-PARTS: NONE

### C-14.2.2 — Ness's words remain Ness's
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]

ALONE
- What it is: ACCEPTED — Attribution of Ness's own words within the recording. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Takes in: ACCEPTED — Words carried from Ness's source stream. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Does: ACCEPTED — Preserves those words as Ness's words. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Gives out: ACCEPTED — Ness-attributed source content. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Must never: ACCEPTED — Reattribute Ness's words to N.H. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | Ness-origin words. | Retains their attribution. | Those words are not attributed to N.H. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] |

SUB-PARTS: NONE

### C-14.2.3 — N.H output remains model output
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]

ALONE
- What it is: ACCEPTED — Attribution and evidential limits of N.H's prior speech. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Takes in: ACCEPTED — N.H's earlier output as captured in the conversation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Does: ACCEPTED — Preserves it as N.H's earlier output without making it fact merely because N.H said it. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Gives out: ACCEPTED — Source-attributed prior N.H output with no automatic truth authority. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Must never: ACCEPTED — Promote prior N.H output to fact solely because it came from N.H. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | Captured prior N.H speech. | Keeps its source distinct from fact status. | Repetition of N.H speech cannot make it fact. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] |

SUB-PARTS: NONE

### C-14.2.4 — Speaker carried from source
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The source-carried speaker identity accompanying the live label. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — `speaker_of_record` from the source stream. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the speaker from that stream without later guessing or re-derivation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Source-grounded attribution. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Guess a speaker later or replace a source fact with a model inference. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | `speaker_of_record` from the stream. | Preserves the actual source identity. | No later guessing replaces attribution. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.2.5 — Provenance makes no semantic claim
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The limit on what the conversation label asserts. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The provenance label and the recorded conversation's origin. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Asserts only recorded live-conversation origin; asserts no topic, meaning, truth or importance. Leaves the legacy `subject` field untouched. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Origin information without semantic classification. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Reuse the legacy `subject` field as the conversation's inferred topic or make semantic claims through the provenance label. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | The conversation's provenance. | Leaves topic, meaning, truth and importance unasserted. | Legacy `subject` remains untouched. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.2.6 — Topical subject earned by reading
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The separation between known provenance and a later topical reading. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The conversation content with its source provenance. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Leaves the real topical subject to the Meaning Engine's later reading. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Provenance that does not predetermine the topical subject. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat a front-door provenance label as an earned semantic topic. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | Source-labeled conversation content. | Separates provenance from the engine's earned subject. | Capture does not preselect a topic. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.2.7 — Source speaker connection
Stamp: DESIGNED    Source: [V10 §14]

ALONE
- What it is: DESIGNED — The speaker connection back to the source fact. [V10 §14]
- Takes in: DESIGNED — The source location where the speaker fact already lives. [V10 §14]
- Does: DESIGNED — Points back to that fact through the speaker connection instead of guessing or making a fresh assertion. [V10 §14]
- Gives out: DESIGNED — A pointer to the existing source fact. [V10 §14]
- Must never: DESIGNED — Guess the speaker or replace the pointer with a copied assertion of the fact. [V10 §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.2 — Live-conversation provenance meaning | The source location of the speaker fact. | Points back to that source. | Attribution is connected rather than guessed or reasserted. | [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] |

SUB-PARTS: NONE

### C-14.3 — Creation-aware live routing
Stamp: DESIGNED    Source: [V10 §14] [V10 §7G / CREATION-AWARE MODE]

ALONE
- What it is: DESIGNED — Routing of live-created `design`, `idea`, `rule`, `name` and `decision` material through a mode of the one Meaning Engine. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Takes in: DESIGNED — Material Ness produces during live conversation. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Does: DESIGNED — Uses creation-aware mode inside the Meaning Engine, creates provisional records automatically and permits confirmation only through explicit Ness confirmation or later words/actions clearly demonstrating adoption. Ambiguity stays provisional. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Gives out: DESIGNED — Provisional creation material, with confirmation available only through the two settled routes. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Must never: DESIGNED — Add a separate Creation Filter stage; let time alone confirm a creation; silently treat ambiguity as adoption. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Fails closed by: DESIGNED — Leaves ambiguous or unconfirmed material provisional. [V10 §14] [V10 §7G / CREATION-AWARE MODE]

TOGETHER
- Fed by: ACCEPTED — C-14.3.1 — Broad provisional capture: supplies broad provisional capture of partial creation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fed by: ACCEPTED — C-14.3.4 — Provisional availability and influence: supplies status-preserving and traceable provisional influence. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gated by: DESIGNED — C-14.3.2 — Explicit confirmation route: permits explicit confirmation as one of the two alternative confirmation routes. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Gated by: DESIGNED — C-14.3.3 — Clear demonstrated-adoption route: permits later words or actions only when they clearly demonstrate adoption, as the other alternative route. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Changes: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): supplies live-created material for the engine's creation-aware mode. [V10 §7G / CREATION-AWARE MODE] [V10 §14]
- Changes: DESIGNED — C-CREATE — Unified Creation Store (§14, §7G creation-aware mode): supplies provisional creation material with only the two confirmation routes. [V10 §7G / CREATION-AWARE MODE] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | Material Ness produces during live conversation. | Routes it as creation-aware reading and provisional creation. | Confirmation remains limited to two routes. | [V10 §14] [V10 §7G / CREATION-AWARE MODE] |
| 2 · ACCEPTED | C-14.3.1 — Broad provisional capture | Partial created material. | Captures without treating breadth as adoption. | Fragmentary material remains provisional. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [V10 §7G / CREATION-AWARE MODE] |
| 3 · DESIGNED | C-14.3.2 — Explicit confirmation route | Ness's explicit confirmation of a provisional creation. | Applies that permitted confirmation route. | The creation can become confirmed through explicit assent. | [V10 §7G / CREATION-AWARE MODE] |
| 4 · DESIGNED | C-14.3.3 — Clear demonstrated-adoption route | Ness's later words or actions. | Requires clear demonstrated adoption. | Ambiguous evidence leaves the creation provisional. | [V10 §7G / CREATION-AWARE MODE] |
| 5 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Provisional material from the Meaning Engine's creation-aware mode, source provenance and actual confirmation evidence. | Receives material from the settled live-chat creation route. | Nothing in this card. | [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE] |
| 6 · DESIGNED | C-7G.7 — Creation-aware reading mode | Live-session designs, ideas, rules, names and decisions produced by Ness. | Receives live material through creation-aware routing. | Nothing in this card. | [V10 §7G / CREATION-AWARE MODE] |

SUB-PARTS: C-14.3.1 — Broad provisional capture; C-14.3.2 — Explicit confirmation route; C-14.3.3 — Clear demonstrated-adoption route; C-14.3.4 — Provisional availability and influence

### C-14.3.1 — Broad provisional capture
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Provisional capture of small or incomplete creation material. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Small fragments, partial thoughts, short phrases, unfinished sections and pieces that may later form a larger idea. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Captures creation as broadly as reasonably possible so fragmentary thinking is not lost. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Provisional creation fragments available for later development. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Treat broad capture as automatic confirmation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Keeps capture provisional without one of the two confirmation routes. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.3 — Creation-aware live routing: leaves broad capture provisional until a permitted confirmation route applies. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [V10 §7G / CREATION-AWARE MODE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.3 — Creation-aware live routing | Small fragments and unfinished thoughts. | Keeps them available without automatic confirmation. | Fragmentary creation is not lost for being incomplete. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-14.3.2 — Explicit confirmation route
Stamp: DESIGNED    Source: [V10 §14] [V10 §7G / CREATION-AWARE MODE]

ALONE
- What it is: DESIGNED — One of the two permitted routes from provisional to confirmed creation. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Takes in: DESIGNED — A provisional creation and Ness's explicit confirmation. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Does: DESIGNED — Confirms the creation on that explicit confirmation. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Gives out: DESIGNED — A creation confirmed through Ness's express act. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Must never: DESIGNED — Substitute elapsed time for the explicit confirmation. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Fails closed by: DESIGNED — Leaves the record provisional when this route lacks confirmation and the other permitted route does not apply. [V10 §14] [V10 §7G / CREATION-AWARE MODE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.3 — Creation-aware live routing: requires Ness’s explicit confirmation before this alternative route can confirm the record. [V10 §7G / CREATION-AWARE MODE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.3 — Creation-aware live routing | A provisional creation and Ness's explicit confirmation. | Uses that act as a permitted route. | The record may become confirmed through express confirmation. | [V10 §14] [V10 §7G / CREATION-AWARE MODE] |
| 2 · ACCEPTED | C-CREATE.5.1 — Explicit-confirmation commit | The words that explicitly confirm the creation, referenced rather than replaced by a model assertion. | Gates this place: consumes the existing explicit-confirmation route. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-14.3.3 — Clear demonstrated-adoption route
Stamp: DESIGNED    Source: [V10 §14] [V10 §7G / CREATION-AWARE MODE]

ALONE
- What it is: DESIGNED — Confirmation through later words or actions that clearly demonstrate adoption. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Takes in: DESIGNED — A provisional creation and Ness's later relevant words or actions. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Does: DESIGNED — Confirms only when those words or actions clearly demonstrate adoption; retains provisional status when ambiguous. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Gives out: DESIGNED — Confirmed creation when clear adoption is demonstrated. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Must never: DESIGNED — Treat ambiguous later behavior or time passing as clear adoption. [V10 §14] [V10 §7G / CREATION-AWARE MODE]
- Fails closed by: DESIGNED — Keeps ambiguity provisional. [V10 §14] [V10 §7G / CREATION-AWARE MODE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.3 — Creation-aware live routing: requires later words or actions to demonstrate adoption clearly before this alternative route can confirm the record. [V10 §7G / CREATION-AWARE MODE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.3 — Creation-aware live routing | A provisional creation and later adoption evidence. | Requires clear demonstrated adoption. | Ambiguity remains provisional. | [V10 §14] [V10 §7G / CREATION-AWARE MODE] |
| 2 · ACCEPTED | C-CREATE.5.2 — Later-adoption proposal evaluation | A confirmation proposal with exact later roots/recorded actions and exact original creation-fragment references. | Gates this place: consumes the existing clear-demonstrated-adoption route. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-14.3.4 — Provisional availability and influence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

ALONE
- What it is: ACCEPTED — Continued availability and permitted wider use of provisional creation material. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Takes in: ACCEPTED — A provisional creation and a relevant retrieval, reasoning, answer or Computed View operation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Does: ACCEPTED — Keeps the material in a clear ideas-in-progress/provisional area and allows relevant wider use only with provisional status carried in the output context and traceable in the operation record through `provisional_material_used`, identifying the record and status at use time. Relationships among fragments may be recorded or proposed while the original fragments and their provenance remain traceable. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gives out: ACCEPTED — Relevant provisional influence that remains visible as provisional and traceable. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Must never: ACCEPTED — Present a fragment as confirmed fact, adopted rule, final decision or settled creation; confirm through time, repetition, retrieval frequency, system use, repeated model output or confidence; silently fuse fragments into an adopted creation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Fails closed by: ACCEPTED — Retains provisional status unless explicit confirmation or clear later demonstrated adoption supplies a permitted route. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-CREATE — Unified Creation Store (§14, §7G creation-aware mode): requires provisional status and record/status-at-use provenance on every wider use. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.3 — Creation-aware live routing | Relevant provisional material proposed for wider use. | Carries its status and operation-record trace. | Wider use does not confirm or silently fuse the creation. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)] |

SUB-PARTS: NONE

### C-14.4 — Visible point-back
Stamp: DESIGNED    Source: [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]

ALONE
- What it is: DESIGNED — The visible point-back surface for earlier referenced material. [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Takes in: DESIGNED — A current turn referring to earlier material. [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Does: DESIGNED — Presents one clickable point-back to the earlier piece and back to now. [SOURCE CONFLICT: 04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5 supersedes the visible link in its separately accepted scope] [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Gives out: DESIGNED — A clickable route to the earlier piece and back to the current conversation. [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Must never: DESIGNED — Narrate the reference plumbing in ordinary chat. [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-14.4.1 — Accepted silent earlier-context use: records the accepted no-link target and reliable silent context use. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | A reference to earlier material. | Preserves the V10 surface and its explicit conflict. | No source integration is silently inferred. | [V10 §13] [V10 §14] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-14.4.1 — Accepted silent earlier-context use

### C-14.4.1 — Accepted silent earlier-context use
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The accepted target presentation for reliable named earlier context. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — References to an earlier topic, project rule, document, specification, message or idea. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Uses reliably identified earlier context naturally and silently; the accepted target has no visible clickable point-back link and no visible topic-type tag. [SOURCE CONFLICT: V10 §13 and §14 retain the visible clickable point-back] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Earlier-context use with no link, tag or navigation UI in the accepted target presentation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Fabricate uncertain references or expose the accepted internal-reference mechanism as a visible link or topic-type tag. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Does not use an unresolved reference as a resolved one. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: requires reliable resolution before earlier named context is used. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.4 — Visible point-back | A reliable earlier named reference. | Uses its context naturally in the accepted target presentation. | The target has no visible link or topic-type tag. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.5 — Proposed structured live provenance label
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — B17's proposed structured typed `provenance_label`, carried on the pre-ingest record and into root provenance metadata. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Recorded live-conversation origin, source-carried `speaker_of_record` and the flag marking prior N.H output as N.H output. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Uses the proposed structure `{ label_type: "live_conversation", label_version [proposed]: "v1" }` alongside those source fields. Assigns it inside the same capture transaction, with the same capture idempotency and one capture record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — A proposed typed provenance label in capture and root provenance, verified by the Catalog envelope check. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Adopt `live:ness_nh_conversation` as the final label string; overload the label with meaning; create a separate label-assignment operation or log; change legacy `subject`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A live capture missing the label fails the envelope and follows the capture-error path; it never enters silently. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-14.5.1 — provenance_label — proposed typed object: supplies the proposed `provenance_label` object. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.5.2 — Source speaker beside the label: supplies the accompanying source-carried speaker. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.5.3 — Prior N.H output flag: supplies the flag identifying prior N.H output. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.5.4 — Label inside the capture transaction: assigns the label inside the existing capture transaction. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-14.5.5 — Live-label envelope condition: requires the live label to be present at envelope checking. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-14.2 — Live-conversation provenance meaning: permits the label to assert origin only, with all speaker and non-fact protections. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A33] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | Live-conversation origin and source attribution. | Places the typed label in the capture transaction. | Root provenance can retain the same origin label. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-14.5.5 — Live-label envelope condition | The live capture's provenance label. | Checks it within the envelope. | Normal admission includes the label. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: C-14.5.1 — provenance_label — proposed typed object; C-14.5.2 — Source speaker beside the label; C-14.5.3 — Prior N.H output flag; C-14.5.4 — Label inside the capture transaction; C-14.5.5 — Live-label envelope condition

### C-14.5.1 — provenance_label — proposed typed object
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed required live-capture provenance object. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Origin in recorded live conversation between Ness and N.H. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the two proposed structured members `label_type` and `label_version` in capture and root provenance metadata. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — The proposed object `{ label_type: "live_conversation", label_version [proposed]: "v1" }`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Replace the structure with the unadopted illustrative string or use it to assert topic, meaning, truth or importance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing label causes the live capture's envelope check to fail and enter the capture-error path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-14.5.1.1 — label_type [proposed] — proposed member: supplies proposed `label_type` with value `"live_conversation"`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-14.5.1.2 — label_version [proposed] — proposed member: supplies proposed `label_version` with value `"v1"`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-14.5.5 — Live-label envelope condition: requires the label for live-capture envelope acceptance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5 — Proposed structured live provenance label | Recorded live-conversation origin. | Carries the proposed type and version members. | Provenance remains structured and origin-only. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: C-14.5.1.1 — label_type [proposed] — proposed member; C-14.5.1.2 — label_version [proposed] — proposed member

### C-14.5.1.1 — label_type [proposed] — proposed member
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed type member of the live provenance label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Recorded live-conversation origin. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the exact string `"live_conversation"` as `label_type` [proposed]. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — A proposed label identifying that source kind. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat the type string as a semantic topic or truth judgment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5.1 — provenance_label — proposed typed object | The source kind. | Retains the declared type value. | The proposed label identifies live-conversation origin. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.5.1.2 — label_version [proposed] — proposed member
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed version member of the structured label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The proposed live label format. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Carries `label_version` [proposed] with the exact string `"v1"`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — An explicit version in the proposed label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Supply another version value as this proposed v1 label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5.1 — provenance_label — proposed typed object | The label format. | Retains its declared version. | The proposed object is explicitly versioned. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.5.2 — Source speaker beside the label
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The source-carried `speaker_of_record` accompanying the structured label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Speaker identity from the source stream. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Carries that known identity beside the label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Source-attributed live material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Guess `speaker_of_record` after capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5 — Proposed structured live provenance label | `speaker_of_record` from the stream. | Preserves source attribution beside the label. | Speaker identity is not guessed later. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.5.3 — Prior N.H output flag
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The source flag distinguishing N.H's own prior output. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Captured prior N.H output. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Marks that content as N.H output alongside the provenance label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Prior output identified without becoming fact through its origin. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat flagged N.H output as fact solely because N.H produced it. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5 — Proposed structured live provenance label | N.H's captured prior output. | Retains that source distinction. | N.H output does not gain fact status from origin. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.5.4 — Label inside the capture transaction
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Assignment of the label as part of the existing Catalog capture operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The capture, proposed typed label and source attribution fields. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Commits label assignment inside the capture transaction, idempotent with that capture and included in its one operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — One capture containing its provenance label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Create a second operation or second log solely for label assignment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing label prevents normal envelope acceptance and sends the capture to the error path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-14.5.5 — Live-label envelope condition: requires label presence inside the capture being committed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Changes: DESIGNED — C-7E.13.1 — Capture record: includes assignment in the existing capture record, never a separate label log. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5 — Proposed structured live provenance label | The capture and structured label. | Commits the label with the capture. | No second operation or log is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.5.5 — Live-label envelope condition
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The label-presence requirement in the live-front-door envelope check. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — A live capture and its provenance label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Verifies the label as part of the Catalog envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — A label-bearing capture eligible to continue under the remaining Catalog rules. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Admit a live capture silently without its label. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Fails the envelope and follows the capture-error path when the label is missing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-14.5 — Proposed structured live provenance label: defines the required live typed-label shape and origin boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: includes the live label in the shared envelope verification. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Changes: DESIGNED — C-7E.3 — Capture-error path: supplies missing-label failures to the capture-error path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.5 — Proposed structured live provenance label | A live capture and its label. | Checks the label before normal admission. | A missing label goes to capture-error. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-14.5.1 — provenance_label — proposed typed object | The live capture and proposed label object. | Supplies it to the envelope check. | Missing label prevents silent entry. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-14.5.4 — Label inside the capture transaction | Capture contents and the structured label. | Keeps the label within the checked capture transaction. | A missing-label capture goes to the error path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-14.6 — B18 earlier-reference detection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Internal detection and governed use of references to earlier context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Each live turn and candidate earlier roots, threads, creations or specifications. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Runs `re_reads` silently per turn; proposes reference records; uses candidates only under the consuming mode's declared reliability condition through normal context channels. Commits one detection record per evaluation, including unused candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — A committed reference evaluation and, when reliable, provenance-bearing context for retrieval. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Fabricate a reference, use an unresolved candidate as resolved, surface it as a claim, or add the visible link/tag/navigation UI prohibited in the accepted target. [SOURCE CONFLICT: V10 §13 and §14 retain visible point-back behavior] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — On detector failure, lets the turn proceed without earlier-reference context; never supplies guessed context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-14.6.1 — Reference record: supplies the proposed reference record and its evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.3 — Reliable reference into retrieval: supplies the reliable-context handoff. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.6 — Detector-failure continuation: supplies continuation without earlier context on detector failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: requires the consuming mode's declared reliability condition before context use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-14.6.4 — One detection evaluation record: requires one committed record for each evaluation, including used and unused candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-14.6.5 — Detection idempotency and recovery: recognizes the turn-capture-id and detector-version identity and preserves committed evaluations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-14.7 — Shared capture and reference-operation protections: requires stable identity, durable recording, bounded retry and privacy-before-relevance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | A live turn and earlier candidate objects. | Evaluates references under declared reliability and operation rules. | The turn receives reliable context or proceeds without it on detector failure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-14.6.4 — One detection evaluation record | The evaluation's candidate outcomes. | Commits its detection record. | Used and unused results remain traceable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-14.6.5 — Detection idempotency and recovery | Turn identity, detector version and prior committed records. | Recognizes duplicates and recovers missing evaluations. | A replay does not duplicate work already committed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: C-14.6.1 — Reference record; C-14.6.2 — Declared reference reliability; C-14.6.3 — Reliable reference into retrieval; C-14.6.4 — One detection evaluation record; C-14.6.5 — Detection idempotency and recovery; C-14.6.6 — Detector-failure continuation

### C-14.6.1 — Reference record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The proposed internal reference record emitted by turn evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — The source turn/capture, candidate referenced objects and detector evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves proposed `reference_id`, source turn/capture reference, candidate object(s) of root/thread/creation/spec kind, each candidate's confidence representation and stated basis, and detector version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — A traceable proposed reference record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat a candidate reference as resolved merely because a record exists. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Unresolved candidates remain recorded as unresolved and do not supply resolved context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-14.6.1.1 — reference_id [proposed] — proposed identifier: supplies proposed `reference_id`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.1.2 — Source turn or capture reference: supplies the source turn/capture reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.1.3 — Candidate referenced objects: supplies candidate root/thread/creation/spec targets. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.1.4 — Detector version: supplies the detector version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: prohibits treating a record's unresolved candidates as resolved references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | Turn provenance and candidate targets. | Preserves identity, candidates, confidence, basis and detector version. | Earlier-reference proposals stay traceable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: C-14.6.1.1 — reference_id [proposed] — proposed identifier; C-14.6.1.2 — Source turn or capture reference; C-14.6.1.3 — Candidate referenced objects; C-14.6.1.4 — Detector version

### C-14.6.1.1 — reference_id [proposed] — proposed identifier
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The proposed identifier of a reference record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — A proposed reference record from turn evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Identifies that record using proposed `reference_id`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — A reference record carrying its proposed identity field. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1 — Reference record | A reference proposal. | Identifies the proposed record. | The record has its own reference identity. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.1.2 — Source turn or capture reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Provenance linking a reference record to its source turn/capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — The turn or capture being evaluated. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Retains its source reference in the proposed record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — A reference proposal traceable to the evaluated input. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1 — Reference record | The evaluated input. | Anchors the proposal to that input. | Reference provenance remains inspectable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.1.3 — Candidate referenced objects
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — One or more proposed earlier objects to which the turn may refer. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — Candidate root, thread, creation or specification objects. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Retains the candidate object(s), each with its own confidence representation and stated basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Candidate targets distinguished from resolved references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent a target to satisfy the current turn. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Keeps unresolved candidates out of resolved-context use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-14.6.1.3.1 — Candidate confidence representation: supplies each candidate's confidence representation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.1.3.2 — Candidate stated basis: supplies the stated basis for each candidate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: admits a candidate target only under the declared consuming condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1 — Reference record | Proposed earlier objects. | Keeps candidate identity separate from resolution. | A proposed target is not automatically usable context. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: C-14.6.1.3.1 — Candidate confidence representation; C-14.6.1.3.2 — Candidate stated basis

### C-14.6.1.3.1 — Candidate confidence representation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The confidence representation attached to each candidate reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — The detector's candidate assessment under the consuming mode declarations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Carries confidence for that candidate; reliability representation is governed by Tier-1/Tier-2 declarations rather than a numeric threshold selected here. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Confidence represented with the candidate for reliability evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat confidence alone as resolution outside the consuming mode's declared reliability condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — A candidate that does not meet that condition cannot be used as resolved earlier context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: requires the declared reliability condition, not confidence alone. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1.3 — Candidate referenced objects | The detector's candidate assessment. | Carries confidence under the declared mode. | Reliability can be checked without inventing a threshold. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.1.3.2 — Candidate stated basis
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The stated basis for proposing a particular earlier reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — Support for the candidate, such as a name match, quoted fragment or structural link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the basis with the candidate and its confidence representation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable basis for the proposed reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Fabricate a basis to make an uncertain reference appear resolved. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1.3 — Candidate referenced objects | A name match, quoted fragment or structural link. | Preserves the support for the proposal. | The proposed connection can be inspected. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.1.4 — Detector version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The version of the detector that evaluated the turn. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — The detector used for that evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves its version in the reference record and uses it with turn capture identity in the evaluation's idempotency key. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Versioned evaluation provenance and the detector-version portion of duplicate identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Drop the detector version from the declared detection identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.1 — Reference record | The evaluation's detector. | Retains its version in provenance and duplicate identity. | Replays remain tied to the declared evaluation identity. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.2 — Declared reference reliability
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The consuming mode's condition for admitting earlier-reference context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — A candidate object, confidence representation and stated basis under the declared Tier-1/Tier-2 mode. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Allows earlier-context use only when the candidate meets that declared reliability condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Candidates eligible for natural earlier-context use under the mode. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently invent a threshold or treat an unresolved candidate as reliable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Records unresolved candidates as unresolved and does not use or surface them as resolved claims. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): requires the consuming mode’s declared Tier-1/Tier-2 reliability condition before earlier context may be used. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | A proposed reference with confidence and basis. | Admits only candidates satisfying that condition. | Unresolved references remain unused as resolved context. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-14.6.1 — Reference record | Candidate references and their reliability outcome. | Keeps record existence distinct from reliability. | Unresolved candidates remain non-authoritative context proposals. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-14.6.1.3 — Candidate referenced objects | Candidate object, confidence and stated basis. | Preserves unresolved status until the condition is met. | Proposed targets do not silently become resolved. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-14.6.1.3.1 — Candidate confidence representation | The candidate's confidence representation. | Evaluates it within the consuming mode. | An unsupported certainty claim supplies no resolved context. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-14.6.3 — Reliable reference into retrieval | A proposed earlier reference. | Admits only reliable context. | Unresolved candidates stay out of the retrieval handoff. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-14.4.1 — Accepted silent earlier-context use | A candidate earlier reference. | Applies the consuming reliability condition. | An unresolved reference is not fabricated or used as resolved. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A32] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.3 — Reliable reference into retrieval
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The handoff of a reliably resolved earlier reference to context retrieval. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — A reference meeting the consuming mode's reliability condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Feeds provenance-bearing earlier context into normal Context Retrieval channels for natural silent use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — Earlier-reference context that retains retrieval provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Surface the accepted target mechanism as a link, topic-type tag or navigation UI. [SOURCE CONFLICT: V10 §13 and §14 retain a visible link] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Excludes unresolved reference candidates from this handoff. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-14.6.2 — Declared reference reliability: requires the reference to meet the mode's reliability condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Changes: DESIGNED — C-7F — Context Retrieval (§7F): supplies reliable provenance-bearing context through normal retrieval channels. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | A reference meeting the consuming condition. | Feeds normal retrieval with provenance-bearing earlier context. | Natural context use remains silent in the accepted target. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.6.4 — One detection evaluation record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The durable operation record for each live-turn reference evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — The evaluated turn and all used or evaluated-but-unused candidates with their reliability outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Commits one detection record per turn evaluation, including unused candidates and outcomes; keeps one real evaluation to one operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — One committed evaluation record containing both used and unused candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Omit evaluated-but-unused candidates, duplicate the operational log, let logging recursively log itself or use the log as evidence weight for its own subject. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — On detector failure, records the failed evaluation under the shared operation boundary and supplies no earlier-reference context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-14.6 — B18 earlier-reference detection: requires the record of every turn evaluation, including unused candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-14.7 — Shared capture and reference-operation protections: requires the evaluation change and its one operational record to commit atomically. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | The turn evaluation and all candidate outcomes. | Commits its complete operation record. | An evaluation cannot disappear from the record or acquire duplicate logs. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-14.6.5 — Detection idempotency and recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Duplicate prevention and crash recovery for per-turn reference evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Turn capture identity, detector version and existing committed detection records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Uses the declared idempotency key of turn capture id + detector version, recognizes duplicates structurally and re-evaluates after a crash only turns lacking committed detection records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — A preserved committed evaluation or evaluation of an uncommitted turn. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Re-evaluate a committed turn as missing work, manufacture committed state or create duplicate evaluation effects. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Recovers from committed state only; detector failure yields no earlier-reference context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-14.6 — B18 earlier-reference detection: defines the per-turn evaluation and committed-record recovery boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-14.6.5.1 — Committed evaluation recognized: supplies recognition of an already committed evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-14.6.5.2 — Missing evaluation re-evaluated: supplies recovery of a turn without committed detection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-14.7 — Shared capture and reference-operation protections: requires structural duplicate identity and recovery from committed state only. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | The evaluation key and committed state. | Prevents duplicate effects and recovers only missing evaluations. | A crash does not erase committed detection work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: C-14.6.5.1 — Committed evaluation recognized; C-14.6.5.2 — Missing evaluation re-evaluated

### C-14.6.5.1 — Committed evaluation recognized
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Recovery and replay where the detection evaluation already has a committed record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — The turn capture id, detector version and matching committed evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Recognizes the duplicate structurally, skips repeated effects and records duplicate prevention under the shared operation contract. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — The committed evaluation preserved without a second evaluation effect. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Re-evaluate committed work as if its record were missing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Uses committed evidence; an uncertain state does not authorize invented or duplicate effects. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.5 — Detection idempotency and recovery | The evaluation key and matching durable record. | Recognizes replay and skips duplicate effects. | Committed detection work remains intact. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-14.6.5.2 — Missing evaluation re-evaluated
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Crash recovery for a turn lacking a committed detection record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — A live turn with no committed detection evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Re-evaluates only that missing work and records the recovery operation under the shared contract. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — A recovered evaluation for the previously uncommitted turn, or the detector-failure continuation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Reconstruct a fictitious committed record or guess earlier context on failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Detector failure leaves the turn without earlier-reference context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6.5 — Detection idempotency and recovery | The turn lacking its committed evaluation. | Re-evaluates the missing work only. | Recovery does not redo committed evaluations. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-14.6.6 — Detector-failure continuation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The live-turn outcome when earlier-reference detection fails. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — Detector failure during evaluation of a live turn. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Continues the turn without earlier-reference context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — A live turn without guessed earlier context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent a reference or guessed context to conceal detector failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Omits earlier-reference context and lets the turn proceed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-14.6 — B18 earlier-reference detection | A failed detector evaluation. | Lets the turn proceed without guessed context. | Detector failure does not manufacture an earlier reference. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-14.7 — Shared capture and reference-operation protections
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The accepted shared operation contract consumed by live capture and reference evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — A real operation, stable operation identity, deterministic duplicate key, committed state and its applicable authority. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Retains one stable operation id per real operation. Commits each state change atomically with its append-only record; recognizes replay structurally, skips repeated effects and records duplicate prevention. Recovers from committed checkpoints only and records each recovery action as one operation. Partial completion uses per-item commits: completed items stand and unfinished items resume. Technical failure has 3 total attempts with minimum live gaps of 10 then 30 seconds and a 7-minute live maximum. Background work has 1 then 3 minute gaps and a 15-minute maximum. A bad/unsafe/unsupported proposal has exactly 1 careful retry after durable rejection. The attempt or elapsed gate that closes first stops retry; early stopping is allowed when unsafe or useless, and further continuation requires a recorded real change. Every root-producing operation uses the B11 active writable batch. WB1 binds ownership generation, reservation and root-ID commit atomically; WB2 verifies the durable `commit_fenced` generation and matching root-ownership entry immediately before commit; WB3 records exactly one terminal parent operation, with child logs never counted as additional parent logs. Historical coverage must verify before writes under §8.2B. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — Committed outcomes with exactly one operational record per real operation; root-write parent records remain distinct from child logs. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Treat repetition as real change; recursively log logging; turn a log into evidence for its own subject; bypass Catalog or append to the sealed 5,521-root batch; allow privacy to follow relevance; read held/sealed content outside its governing boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Halts terminal failures honestly; on uncertainty permits no entry, activation or completion claim. Every root write still requires the accepted B11 global claim, ownership binding, append fence, historical-coverage gate and recorded terminal-parent outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-STORE.5.2 — Bundle 6 operation protections: supplies the accepted shared operation contract without changing its values or boundaries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7E.12 — Accepted root-write handoff: requires root-producing work to use the accepted B11 Catalog handoff. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | Operation identity, committed state and authority. | Preserves atomicity, structural idempotency, retry limits and one-operation logging. | Uncertain or unauthorized effects do not enter memory or claim completion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-14.6 — B18 earlier-reference detection | The live-turn evaluation and its committed state. | Applies the shared operation protections. | Reference use does not bypass the operation contract. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-14.6.4 — One detection evaluation record | The evaluation and its full candidate outcomes. | Preserves the one-operation/one-record boundary. | An incomplete record cannot be claimed as a completed evaluation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 4 · ACCEPTED | C-14.6.5 — Detection idempotency and recovery | The evaluation key and durable records. | Recognizes replay and resumes only missing work. | No guessed state or duplicate effects are admitted. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-14.8 — Chat front-door event records
Stamp: DESIGNED    Source: [MAP C-14]

ALONE
- What it is: DESIGNED — Records of captured turns, surfaced point-backs and provisional creation production. [MAP C-14]
- Takes in: DESIGNED — Each occurrence of the three front-door event classes. [MAP C-14]
- Does: DESIGNED — Records each captured turn, each surfaced point-back and each provisional creation record produced; keeps records under privacy access and applicable identity/security authorization. [SOURCE CONFLICT: 04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5 removes the visible point-back in its accepted target] [MAP C-14]
- Gives out: DESIGNED — Governed records of actual front-door occurrences. [MAP C-14]
- Must never: DESIGNED — Invent a surfaced-link event where no link was surfaced or treat an event record as unrestricted visible content. [MAP C-14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-14.8.1 — Captured-turn event: supplies the captured-turn event. [MAP C-14]
- Fed by: DESIGNED — C-14.8.2 — Surfaced-point-back event: supplies an event only for a point-back actually surfaced. [MAP C-14]
- Fed by: DESIGNED — C-14.8.3 — Provisional-creation production event: supplies the provisional-production event. [MAP C-14]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): requires privacy authorization for use or access to front-door records. [MAP C-14]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): requires applicable identity/security authorization before front-door records are surfaced. [MAP C-14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14 — Chat Front Door (§14) | Captured turns, surfaced point-backs and provisional creation production. | Records each actual occurrence under access controls. | Front-door activity remains traceable. | [MAP C-14] |
| 2 · DESIGNED | C-14.8.1 — Captured-turn event | A recorded capture and proposed access. | Preserves the front-door logging/access rule. | Recording does not authorize unrestricted disclosure. | [MAP C-14] |
| 3 · DESIGNED | C-14.8.2 — Surfaced-point-back event | A surfaced point-back and its record. | Records only the real occurrence under access rules. | No absent link is reported as surfaced. | [MAP C-14] |
| 4 · DESIGNED | C-14.8.3 — Provisional-creation production event | Provisional creation production. | Records the real provisional event. | The record neither confirms creation nor grants open access. | [MAP C-14] |

SUB-PARTS: C-14.8.1 — Captured-turn event; C-14.8.2 — Surfaced-point-back event; C-14.8.3 — Provisional-creation production event

### C-14.8.1 — Captured-turn event
Stamp: DESIGNED    Source: [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: DESIGNED — The record of a captured live turn. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: DESIGNED — The actual capture occurrence. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: DESIGNED — Records that captured turn using the capture operation’s existing record and governing access boundary. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: DESIGNED — A captured-turn event record. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: DESIGNED — Expose the record without applicable privacy and access authorization. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: DESIGNED — The capture state and record commit together; under uncertainty no entry is made and no completion is claimed. [MAP C-14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.8 — Chat front-door event records: requires the captured-turn record to retain the governing access boundary. [MAP C-14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.8 — Chat front-door event records | A real turn capture. | Records the capture. | The event is preserved under its access boundary. | [MAP C-14] |

SUB-PARTS: NONE

### C-14.8.2 — Surfaced-point-back event
Stamp: DESIGNED    Source: [MAP C-14]

ALONE
- What it is: DESIGNED — The record of a point-back actually surfaced under the governing visible-link design. [MAP C-14]
- Takes in: DESIGNED — An actual surfaced point-back. [MAP C-14]
- Does: DESIGNED — Records that occurrence under the applicable record-access rules. [SOURCE CONFLICT: 04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §5 specifies a target with no visible link] [MAP C-14]
- Gives out: DESIGNED — A governed event record when the surface event occurs. [MAP C-14]
- Must never: DESIGNED — Manufacture a surfaced-link occurrence or expose its record without applicable authorization. [MAP C-14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.8 — Chat front-door event records: requires an actual surfaced-link occurrence and governed record access. [MAP C-14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.8 — Chat front-door event records | An actual visible-link occurrence. | Records that occurrence. | No event is invented for an absent link. | [MAP C-14] |

SUB-PARTS: NONE

### C-14.8.3 — Provisional-creation production event
Stamp: DESIGNED    Source: [MAP C-14]

ALONE
- What it is: DESIGNED — The event recording production of a provisional creation. [MAP C-14]
- Takes in: DESIGNED — An actual provisional creation record produced from live material. [MAP C-14]
- Does: DESIGNED — Records that production while preserving provisional status and applicable access restrictions. [MAP C-14]
- Gives out: DESIGNED — A governed event record of provisional production. [MAP C-14]
- Must never: DESIGNED — Treat production as confirmation or expose the record without applicable authorization. [MAP C-14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.8 — Chat front-door event records: requires provisional-production records to retain their status and access restrictions. [MAP C-14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.8 — Chat front-door event records | A new provisional creation record. | Records its production as provisional. | Production is not confused with confirmation. | [MAP C-14] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-7E.2 — Minimum intake envelope | DESIGNED — C-14.1 — Automatic live-turn capture | The message and its capture envelope. | Preserves source data and checks the common minimum. | An unidentifiable capture cannot enter silently. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — C-14.1 — Automatic live-turn capture | Each live message and its source envelope. | Hands it to Catalog for completeness, holding and promotion. | The front door has no independent root-writing route. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14] |
| C-7E.3 — Capture-error path | DESIGNED — C-14.1 — Automatic live-turn capture | A capture unable to satisfy the minimum envelope. | Preserves available material through capture-error handling. | Failed capture is neither silently dropped nor accepted as an unidentified blob. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-13 — Live Loop (§13) | DESIGNED — C-14 — Chat Front Door (§14) | Live conversation on the loop. | Captures each turn through the front door. | Capture participates in the loop without fixing reply/read synchronization. | [V10 §13] [MAP C-14] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — C-14 — Chat Front Door (§14) | A live turn and its actual capture state. | Uses the shared capture lifecycle. | Only eligible material becomes a root. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED — C-14.3 — Creation-aware live routing | Ness-produced live material. | Routes it through the one engine's applicable mode. | Creation is read without a separate filtering stage. | [V10 §7G / CREATION-AWARE MODE] [V10 §14] |
| C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | DESIGNED — C-14.3 — Creation-aware live routing | Live creation and any actual confirmation evidence. | Preserves provisional or confirmed status under its proper route. | Captured fragments do not become settled merely through use. | [V10 §7G / CREATION-AWARE MODE] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | ACCEPTED — C-14.3.4 — Provisional availability and influence | Relevant provisional creation material. | Carries its status and traces its influence. | Retrieval and answers do not silently confirm it. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)] |
| C-7E.13.1 — Capture record | ACCEPTED — C-14.5.4 — Label inside the capture transaction | The labeled live capture. | Uses the capture's one operation record. | Label provenance does not multiply operational logs. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| C-7E.2 — Minimum intake envelope | ACCEPTED — C-14.5.5 — Live-label envelope condition | The live capture and source envelope. | Checks label-bearing intake at the Catalog boundary. | Incomplete capture cannot enter the normal path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-7E.3 — Capture-error path | ACCEPTED — C-14.5.5 — Live-label envelope condition | A live capture lacking its label. | Fails normal acceptance and preserves the error case. | The malformed live capture does not enter silently. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-14.6.2 — Declared reference reliability | The candidate and declared consuming mode. | Uses the declared reliability condition. | No ad hoc numeric threshold is invented. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| C-7F — Context Retrieval (§7F) | ACCEPTED — C-14.6.3 — Reliable reference into retrieval | A reliable earlier reference. | Hands its context to ordinary retrieval. | Retrieval can use earlier context without a visible link in the accepted target. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| C-STORE.5.2 — Bundle 6 operation protections | ACCEPTED — C-14.7 — Shared capture and reference-operation protections | A live capture or reference operation. | Consumes the accepted identity, atomicity, retry, recovery and logging rules. | The live front door inherits the established protections. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7E.12 — Accepted root-write handoff | ACCEPTED — C-14.7 — Shared capture and reference-operation protections | An eligible capture ready to become a root. | Uses the active writable batch and its claim, ownership, commit and coverage boundaries. | No sealed historical batch is reopened or appended to. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-14.8 — Chat front-door event records | Proposed access to event records. | Retains the applicable privacy boundary. | Recorded events do not become unrestricted visible content. | [MAP C-14] |
| C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — C-14.8 — Chat front-door event records | A proposed visible use of a record. | Applies current speaker-access restrictions. | Unauthorized disclosure is blocked. | [MAP C-14] |

## Scope and path placement

C-14 and its owned sub-parts participate in CY-B. The shared envelope and operation-protection cards retain their earlier exact identities. Full CY-B synchronization, reply latency, reading-not-ready fallback and connected-cycle crash behavior remain with CH11. Automatic capture is not a claim that a reply waits for the asynchronous post-root worker. P-MAIN contains Catalog's capture/root-entry steps, not a separate C-14 step; no new main-path step is inserted.

B17's structured names remain proposed inside an accepted mechanical package. Acceptance of that design is not schema activation. The illustrative `live:ness_nh_conversation` string is not adopted, and the legacy `subject` field is not repurposed. The root schema, Catalog envelope, B11 state/record atomization and shared operation protections are reused through their existing cards; no earlier card is redefined.

The accepted Bundle 6 policy and mechanical receipts establish their named package scopes. The final closeout receipt records acceptance of the v1.2 closeout, while its own formal receipt-audit gate remains stated as pending. This piece uses the recorded accepted source scope and does not claim a later receipt audit or implementation.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | Fed by | C-14 — Chat Front Door (§14) | DESIGNED — supplies automatic live-chat captures through the common intake boundary. | [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-13 — Live Loop (§13) | Fed by | C-14 — Chat Front Door (§14) | DESIGNED — supplies each captured live-chat turn to the loop. | [MAP C-14] [V10 §13] |



## Source conflicts and explicit source-scope differences

| Kind | Affected cards | Source difference and preserved boundary |
|---|---|---|
| [SOURCE CONFLICT] | C-14.4, C-14.4.1, C-14.6, C-14.6.3, C-14.8 and C-14.8.2 | V10 §13 and §14 and the Map retain a visible clickable point-back to the earlier piece and back to now. Accepted Bundle 6 policy §4 A32 and §5 expressly record a no-visible-link supersession candidate; accepted mechanical §8 B18 supplies internal silent reference use with no link, tag or navigation UI. The accepted sources explicitly say V10/Map integration has not occurred. Under the build contract V10 remains governing; the opposing accepted behavior is written and marked, without silently integrating or erasing either source. |
| Scope distinction | C-14.3 and C-14.5–6 | V10 and the Map retain open A13/A33/B14/B17/B18 design slots. The accepted packages provide later standalone design within those owners. An old open placeholder is not used to discard the later accepted detail. No build or runtime integration is inferred. |
| Scope distinction | C-14.5.4 and C-14.8.1 | B17 label assignment is inside the capture transaction and its single operation record. The front-door captured-turn event does not require an additional label-assignment log. |
| Scope distinction | C-14.6.6 and C-14.7 | B18 explicitly lets the turn continue without earlier context on detector failure. The shared operation contract also supplies bounded retry values. No new wait-for-retry policy or latency promise is inferred; complete live-response timing remains with CY-B. |

## Explicit remaining scope

| Owner piece | Content retained by that owner |
|---|---|
| CH03-a and CH04-a, existing identities | Root schemas, B11 batch registry/global claim/ownership/commit fence/coverage gate, complete Catalog lifecycle and seven envelope field cards. C-14 supplies and consumes these interfaces; it does not redefine their records. |
| CH04-c, unchanged | Full live-loop surface, output gates and optional dual-model concept. Its delivered source review omitted accepted A32/B18; the manifest records that source-completeness finding. Its gap treating broader A32 adoption as wholly undecided requires a later whole-piece audit correction. |
| CH05-a — C-7G | Complete engine interior, acceptance and creation-aware reading. The front door does not judge its own semantic output. |
| CH05-b — C-7GA | Full post-root queue, worker, checkpoints and RC-1–RC-8 recovery, independent of the still-open connected chat-response cycle. |
| CH05-c — C-7F | Complete normal retrieval channels, per-mode parameters and retrieval-failure behavior; B18 supplies only its reliable provenance-bearing earlier-context handoff. |
| CH05-e — C-CREATE | B14 base records, append-only events, confirmation-event canonical truth, detector identity and full provisional-influence records. The live boundary here carries all A13 status protections and the `provisional_material_used` record-id/status-at-use requirement. |
| CH08-a/b/c and CH09-d | Complete privacy, relevance-mode declarations, LMAC coordination and SACL access internals. The consumed privacy-before-relevance and authorized-record-access boundaries remain explicit here. |
| CH10-e — C-19 | A13.3's future non-blocking conversation about promising fragments. It is not silently promoted into settled front-door behavior. |
| CH11 — CY-B / B-CYCLE-1 and creation cycle | Full connected identity, transaction, synchronization, latency, fallback, retry timing and partial-completion behavior across capture and reply. B17/B18's settled local identities and recovery do not close that broader cycle. |
| CH12 | Regeneration of gap, conflict and coverage appendices after the audit, with earlier findings carried from the manifest. |

## Additional undecided implementation slots

| Slot | Owner | Value | Source |
|---|---|---|---|
| Exact final adopted live-label schema/activation, beyond the accepted proposed structured format | C-14.5; root/schema activation owners | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| Flat serialization, if ever needed, derived from structured fields | C-14.5 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| Exact prior-N.H-output flag field name and encoding | C-14.5.3 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| Individual label-member failure outcomes beyond missing-label envelope failure | C-14.5.1.1–2 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |
| Proposed reference_id encoding and complete serialized reference-record field types | C-14.6.1 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| Concrete consuming-mode reliability representation and numeric thresholds | C-14.6.2; C-7R / C-7F | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| Concrete encoding of turn-capture-id plus detector-version idempotency key | C-14.6.5 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| Full capture/reply synchronization, latency, reading-not-ready fallback and crash mid-turn | C-14; CH11 CY-B / B-CYCLE-1 | NOT DECIDED | [MAP CY-B] [MAP C-14] |
| Conversation about promising provisional fragments, A13.3 | C-14.3; CH10-e | NOT DECIDED | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| Complete connected live-creation cycle, B-CYCLE-7 | C-14.3; CH11 | NOT DECIDED | [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md §7] |
| Exact Map-only captured-turn, surfaced-link and provisional-production event names/encodings | C-14.8 | NOT DECIDED | [MAP C-14] |

## Review of plain gates and empty boxes

The two creation-confirmation routes are alternatives, not a requirement to satisfy both. Label assignment is one capture step, not a second operation. Actual reliability and committed-record conditions gate the corresponding reference steps. Privacy/access restrictions on event records are separate from event-writing failure machinery, which the Map does not define. Record-field cards without a specified independent failure action retain empty failure boxes; no detector schema or identifier encoding is invented.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-14 | Changes | NOT DECIDED |
| C-14.1 | Fed by | NOT DECIDED |
| C-14.2 | Fails closed by | NOT DECIDED |
| C-14.2 | Gated by | NOT DECIDED |
| C-14.2 | Changes | NOT DECIDED |
| C-14.2.1 | Fails closed by | NOT DECIDED |
| C-14.2.1 | Fed by | NOT DECIDED |
| C-14.2.1 | Gated by | NOT DECIDED |
| C-14.2.1 | Changes | NOT DECIDED |
| C-14.2.2 | Fails closed by | NOT DECIDED |
| C-14.2.2 | Fed by | NOT DECIDED |
| C-14.2.2 | Gated by | NOT DECIDED |
| C-14.2.2 | Changes | NOT DECIDED |
| C-14.2.3 | Fails closed by | NOT DECIDED |
| C-14.2.3 | Fed by | NOT DECIDED |
| C-14.2.3 | Gated by | NOT DECIDED |
| C-14.2.3 | Changes | NOT DECIDED |
| C-14.2.4 | Fails closed by | NOT DECIDED |
| C-14.2.4 | Fed by | NOT DECIDED |
| C-14.2.4 | Gated by | NOT DECIDED |
| C-14.2.4 | Changes | NOT DECIDED |
| C-14.2.5 | Fails closed by | NOT DECIDED |
| C-14.2.5 | Fed by | NOT DECIDED |
| C-14.2.5 | Gated by | NOT DECIDED |
| C-14.2.5 | Changes | NOT DECIDED |
| C-14.2.6 | Fails closed by | NOT DECIDED |
| C-14.2.6 | Fed by | NOT DECIDED |
| C-14.2.6 | Gated by | NOT DECIDED |
| C-14.2.6 | Changes | NOT DECIDED |
| C-14.2.7 | Fails closed by | NOT DECIDED |
| C-14.2.7 | Fed by | NOT DECIDED |
| C-14.2.7 | Gated by | NOT DECIDED |
| C-14.2.7 | Changes | NOT DECIDED |
| C-14.3.1 | Fed by | NOT DECIDED |
| C-14.3.1 | Changes | NOT DECIDED |
| C-14.3.2 | Fed by | NOT DECIDED |
| C-14.3.2 | Changes | NOT DECIDED |
| C-14.3.3 | Fed by | NOT DECIDED |
| C-14.3.3 | Changes | NOT DECIDED |
| C-14.3.4 | Fed by | NOT DECIDED |
| C-14.3.4 | Changes | NOT DECIDED |
| C-14.4 | Fails closed by | NOT DECIDED |
| C-14.4 | Gated by | NOT DECIDED |
| C-14.4 | Changes | NOT DECIDED |
| C-14.4.1 | Fed by | NOT DECIDED |
| C-14.4.1 | Changes | NOT DECIDED |
| C-14.5 | Changes | NOT DECIDED |
| C-14.5.1 | Changes | NOT DECIDED |
| C-14.5.1.1 | Fails closed by | NOT DECIDED |
| C-14.5.1.1 | Fed by | NOT DECIDED |
| C-14.5.1.1 | Gated by | NOT DECIDED |
| C-14.5.1.1 | Changes | NOT DECIDED |
| C-14.5.1.2 | Fails closed by | NOT DECIDED |
| C-14.5.1.2 | Fed by | NOT DECIDED |
| C-14.5.1.2 | Gated by | NOT DECIDED |
| C-14.5.1.2 | Changes | NOT DECIDED |
| C-14.5.2 | Fails closed by | NOT DECIDED |
| C-14.5.2 | Fed by | NOT DECIDED |
| C-14.5.2 | Gated by | NOT DECIDED |
| C-14.5.2 | Changes | NOT DECIDED |
| C-14.5.3 | Fails closed by | NOT DECIDED |
| C-14.5.3 | Fed by | NOT DECIDED |
| C-14.5.3 | Gated by | NOT DECIDED |
| C-14.5.3 | Changes | NOT DECIDED |
| C-14.5.4 | Fed by | NOT DECIDED |
| C-14.6 | Changes | NOT DECIDED |
| C-14.6.1 | Changes | NOT DECIDED |
| C-14.6.1.1 | Must never | NOT DECIDED |
| C-14.6.1.1 | Fails closed by | NOT DECIDED |
| C-14.6.1.1 | Fed by | NOT DECIDED |
| C-14.6.1.1 | Gated by | NOT DECIDED |
| C-14.6.1.1 | Changes | NOT DECIDED |
| C-14.6.1.2 | Must never | NOT DECIDED |
| C-14.6.1.2 | Fails closed by | NOT DECIDED |
| C-14.6.1.2 | Fed by | NOT DECIDED |
| C-14.6.1.2 | Gated by | NOT DECIDED |
| C-14.6.1.2 | Changes | NOT DECIDED |
| C-14.6.1.3 | Changes | NOT DECIDED |
| C-14.6.1.3.1 | Fed by | NOT DECIDED |
| C-14.6.1.3.1 | Changes | NOT DECIDED |
| C-14.6.1.3.2 | Fails closed by | NOT DECIDED |
| C-14.6.1.3.2 | Fed by | NOT DECIDED |
| C-14.6.1.3.2 | Gated by | NOT DECIDED |
| C-14.6.1.3.2 | Changes | NOT DECIDED |
| C-14.6.1.4 | Fails closed by | NOT DECIDED |
| C-14.6.1.4 | Fed by | NOT DECIDED |
| C-14.6.1.4 | Gated by | NOT DECIDED |
| C-14.6.1.4 | Changes | NOT DECIDED |
| C-14.6.2 | Fed by | NOT DECIDED |
| C-14.6.2 | Changes | NOT DECIDED |
| C-14.6.3 | Fed by | NOT DECIDED |
| C-14.6.4 | Changes | NOT DECIDED |
| C-14.6.5 | Changes | NOT DECIDED |
| C-14.6.5.1 | Fed by | NOT DECIDED |
| C-14.6.5.1 | Changes | NOT DECIDED |
| C-14.6.5.1 | Gated by | NOT DECIDED |
| C-14.6.5.2 | Fed by | NOT DECIDED |
| C-14.6.5.2 | Changes | NOT DECIDED |
| C-14.6.5.2 | Gated by | NOT DECIDED |
| C-14.6.6 | Fed by | NOT DECIDED |
| C-14.6.6 | Changes | NOT DECIDED |
| C-14.6.6 | Gated by | NOT DECIDED |
| C-14.7 | Fed by | NOT DECIDED |
| C-14.7 | Changes | NOT DECIDED |
| C-14.8 | Fails closed by | NOT DECIDED |
| C-14.8 | Changes | NOT DECIDED |
| C-14.8.1 | Fed by | NOT DECIDED |
| C-14.8.1 | Changes | NOT DECIDED |
| C-14.8.2 | Fails closed by | NOT DECIDED |
| C-14.8.2 | Fed by | NOT DECIDED |
| C-14.8.2 | Changes | NOT DECIDED |
| C-14.8.3 | Fails closed by | NOT DECIDED |
| C-14.8.3 | Fed by | NOT DECIDED |
| C-14.8.3 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card; no plain gate remains.

## Source coverage added by CH04-d

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §13 and §14 whole; §7G CREATION-AWARE MODE whole; full Catalog §7E body before the detailed TSC subsection; §6B root/provenance boundary. | C-14.1–4 and C-14.8; source-carried speaker and confirmation routes; shared Catalog cards reused. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: C-13 and C-14; complete CY-B, with live capture/response boundary here and remaining cycle details assigned to named later owners. | C-14 top, C-14.8 and CY-B local path placement. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: §4 A13, A32 and A33 in full; §5 in full; receipt establishes accepted policy scope. | C-14.2, C-14.3.1/4 and C-14.4; no-link disagreement explicitly preserved. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §3 shared mechanical spine, §7 B17 and §8 B18 in full; reuse C-STORE.5.2 and Catalog contracts. | C-14.5 B17 record/fields/transaction; C-14.6 B18 record/reliability/recovery; C-14.7 consumed shared contract. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: §6 relevant policy summary; §7 mechanical summary; §8 live-conversation row 1; §9(b),(e),(f),(g), with (g) provisional_material_used entry. | C-14.3.4 and capture/held-boundary check; wider store machinery left with named owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | Accepted design identity/status evidence; no behavior added by receipt and no implementation asserted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | Accepted design identity/status evidence; no behavior added by receipt and no implementation asserted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | Accepted design identity/status evidence; no behavior added by receipt and no implementation asserted. |

## Coverage matrix — cumulative carried inventory




The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
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
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
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
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
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
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners. |
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
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §13 and §14 whole; §7G CREATION-AWARE MODE whole; full Catalog §7E body before the detailed TSC subsection; §6B root/provenance boundary. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: C-13 and C-14; complete CY-B, with live capture/response boundary here and remaining cycle details assigned to named later owners. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: §4 A13, A32 and A33 in full; §5 in full; receipt establishes accepted policy scope. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §3 shared mechanical spine, §7 B17 and §8 B18 in full; reuse C-STORE.5.2 and Catalog contracts. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: §6 relevant policy summary; §7 mechanical summary; §8 live-conversation row 1; §9(b),(e),(f),(g), with (g) provisional_material_used entry. | `5797a2ac51328985e479d2bc101f310b96d2d75976acfaf5f066c529b31d309b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole: Receipt status and accepted-source identity evidence only; project workflow excluded. | `e397a787911d72533fa0d6245f6331d8d176ea07a21a306d1296b41593dae9c4` |

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

### READ-folder files not yet read whole

84 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 45 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 114 empty fields/cells exactly match the register; 11 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 1 explicit conflict-register rows. The V10 visible point-back and the accepted A32/B18 no-link target remain separately stated; no hidden integration or new precedence is invented.
§3 exactly one stamp per line: PASS — 45 headers, 331 populated fields and 71 USED BY rows checked; 0 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 25 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 45 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 45 templates and 445 field lines checked.
§6.3 reciprocity within this chapter: PASS — 64 internal lines cover 64 reciprocal pairs; 17 external-use continuations and 2 incoming continuations name both endpoints; 2 further outgoing lines are answered directly by the named cards' own USED BY rows.
§6.4 every decided detail written in, no citation used in place of content: PASS — Automatic turn capture, the seven-element envelope, source-speaker/provenance protections, creation-aware routing and both confirmation alternatives, broad provisional capture and traceable influence, proposed B17 object/members and source fields, one capture transaction/log, missing-label error, B18 record/field contents, confidence and stated basis, declared reliability, unresolved refusal, used/unused evaluation record, exact duplicate key, committed-versus-missing recovery, detector-failure continuation, all consumed shared operation/retry values and three front-door event classes are present. Full shared and later-owner schemas are explicitly assigned.
§6.5 sub-parts recursed to the bottom: PASS — 44 declared child/shared references and 45 owned cards checked; 15 explicit steps have 0 empty TOGETHER cases. The proposed label and reference records recurse to their decided members; recovery cases and confirmation alternatives have separate cards. The existing envelope, B11 handoff and shared operation-protection atoms are reused by exact identity; undecided encodings are not manufactured.
§9 coverage matrix rows added for every file used: PASS — 8 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 45 |
| field_lines | 445 |
| populated_fields | 331 |
| not_decided_boxes | 114 |
| not_decided_fields_and_cells | 114 |
| used_by_rows | 71 |
| relationships | 83 |
| internal_relationships | 64 |
| external_relationships | 19 |
| internal_use_pairs | 64 |
| external_use_pairs | 19 |
| used_by_continuation_rows | 17 |
| incoming_continuation_rows | 2 |
| plain_gates | 0 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 15 |
| unique_citations | 25 |
| resolved_citations | 25 |
| named_source_paths_checked | 145 |
| source_identities | 8 |
| whole_read_files | 3 |
| earlier_identities | 22 |
| pending_source_paths | 84 |
| built_field_lines | 0 |
| misfiled_scan_fields | 445 |
| misfiled_scan_used_by_cells | 213 |
| empty_restriction_failure_gate_boxes | 42 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 1 |
| path_covered_cards | 45 |
| subpart_references_checked | 44 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 16 |
| errors | 0 |
| additional_undecided_slots | 11 |
| explicit_source_conflict_records | 1 |

The complete-card review covered every field and USED BY cell. It placed actual confirmation, reliability, detector-failure and committed-state conditions in Gated by, and retained owning-rule links on each step. Intrinsic field-carrying behavior was not turned into an invented gate. Event record-access authorization is explicit; separate event-write failure machinery remains empty where the source does not decide it. Every populated TOGETHER line names its card. Exact source names and all proposed-name qualifiers were checked against B17/B18 and the shared spine.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension, and V10 heading 15 contains the literal dot-prefixed cursorrules name. No actionable wording flags remain.

All 22 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
