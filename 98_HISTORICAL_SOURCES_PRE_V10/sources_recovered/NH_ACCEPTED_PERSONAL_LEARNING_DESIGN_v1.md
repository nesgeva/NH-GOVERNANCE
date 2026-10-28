# N.H — Personal Learning and Adaptation System
## Complete Accepted Design — v1

**Status: ACCEPTED DESIGN — NOT YET BUILT**

**Provenance:** This design was produced and accepted across the design-completeness
audit session (June 26–27 2026). It covers the high-level architecture, corrected
final architecture, and all component designs for how N.H learns, adapts, and
personalizes its behavior specifically for Ness. No code has been written. No
disk verification is claimed. This design must be formally patched into the Master
through the accepted patch-only, no-loss protocol before it carries Master authority.

**Relationship to other accepted designs:** This design connects to BOP
(Behavioral Observation Processing), which is documented in full in
`NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`. BOP is the raw capture
layer; LMAC and OOP in this design are the coordination and outcome-observation
layers that complete the loop. The 13 personalization areas described here are
views into the shared mechanism, not separate modules.

---

## Contents

1. What the Personal Learning System Is and Is Not
2. The Central Concept — No Isolated Model of Ness
3. The Three Processing Responsibilities
4. BOP — Behavioral Observation Processing (summary reference)
5. LMAC — Live Mechanism Access Coordinator
6. OOP — Outcome Observation Processing
7. Response Behavior — Recalculated Per Moment, Not Stored Configuration
8. The 13 Personalization Areas as Views, Not Modules
9. Self-Improvement Rules
10. Architecture Map
11. The Learning Period (First 6–10 Months)
12. What the System Explicitly Must Not Do

---

---

## 1. What the Personal Learning System Is and Is Not

The personal learning and adaptation system is not a separate subsystem sitting
beside N.H. It is a set of processing responsibilities that run inside the same
shared mechanism, producing typed roots and readings that enter the shared store
through the existing catalog and engine path.

**It is:**
- A set of observation and coordination responsibilities within the shared
  accretive architecture.
- The mechanism by which N.H gets better at understanding Ness's behavioral
  patterns, communication preferences, and interaction needs over time.
- A continuous process that operates during authorized sessions and feeds
  evidence into the shared store.
- Fully governed by the same DUMB/SMART boundary, privacy rules, authority
  hierarchy, and evidence discipline as everything else in N.H.

**It is not:**
- A separate module or subsystem with its own stores.
- A parallel model of Ness maintained alongside the main one.
- A configuration system that applies fixed rules learned from the past.
- An interpretation layer — all interpretation belongs to §7G.
- A system that silently promotes observations into facts about Ness.
- A system that creates a reduced or simplified version of Ness for any function.

---

---

## 2. The Central Concept — No Isolated Model of Ness

The central architectural requirement governing this entire design:

**Every N.H function must remain connected to the entire shared living N.H
mechanism before, during, and after execution. No function may operate from
an isolated, reduced, or independently maintained version of Ness.**

Relevance may control attention, retrieval order, processing depth, immediate
weighting, and computational priority. It must not create an architectural
boundary that makes the rest of N.H unavailable to the function.

The shared mechanism is not a database that functions query for a result and
then operate independently. It is a live structure that every function remains
connected to while it operates. Every function has access to the entire structure
at every moment through the existing component interfaces:

- §7F — Context Retrieval
- §7R — Attention and Relevance Control
- §7D — Living State Web
- §7L — Person-Boxes
- §7K — Story Layer
- §7J — Clash Handling
- §7Q — Privacy
- §7P — Permission and Authority Boundaries
- §22 — Wellbeing Baseline

None of these deliver a package and disconnect. They are callable at any moment
during a function's execution. If mid-execution the function detects that a
branch changed, a new root arrived, a clash was recorded, or a Living State Web
node became stale, it may query the relevant component again immediately.

This is the architectural principle that replaces any one-time context-package
model. A function does not carry a copy of what it was given at the start. It
remains connected to the live structure throughout.

---

---

## 3. The Three Processing Responsibilities

The personal learning system introduces three new processing responsibilities.
These are not new stores and not parallel models of Ness. They are new types of
work that run inside the shared accretive architecture, producing typed roots and
readings that enter the shared store through the existing catalog and engine path.

The three responsibilities:

1. **BOP — Behavioral Observation Processing**
   Captures raw behavioral observation events as typed roots. Strictly DUMB —
   produces no interpretations. All outputs enter the sealed root store via §7E
   and append_root(). Full detailed design in NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md.

2. **LMAC — Live Mechanism Access Coordinator**
   Provides every running function with a live interface to the complete shared
   mechanism throughout execution. Stateless between calls. No cache. No copy.

3. **OOP — Outcome Observation Processing**
   Observes what happens after a function acts and produces typed outcome
   observation roots. Strictly DUMB — produces no interpretations. All outputs
   enter the sealed root store via §7E and append_root().

---

---

## 4. BOP — Behavioral Observation Processing (Summary Reference)

**Full design:** `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` Section 1.

BOP is a processing responsibility, not a store. It captures raw physical
observations during authorized sessions and produces typed observation roots.

**Owns data:** No. All outputs are roots entered through §7E and readings
produced by §7G. BOP owns no data separately.

**How it stays connected to the complete mechanism:** BOP is a catalog input
processor. Everything it produces enters the shared accretive store immediately
via §7E → §7G. BOP has no private store, no private model, no interpretation
authority.

**Key behavioral observation event types (v1 vocabulary):**

Voice events (live voice mode or authorized imported recordings):
- `voice_onset`, `voice_offset` — vocalization boundaries
- `silence_interval` — silence between or within turns; duration only, no judgment
- `non_word_sound` — physically typed as `"breath"` | `"non_breath_non_word"` only;
  no communicative function label
- `voice_overlap` — two voice channels simultaneously active
- `voice_interrupt_of_nh` — Ness's voice began while N.H TTS was active
- `pitch_measurement`, `amplitude_measurement` — raw acoustic measurements only;
  no emotional or expressive label

Text events (confirmed sent messages only — unfinished typing never observed):
- `text_message_sent` — character count, word count, sentence count approx,
  exact_text_reference pointing to the conversational root ID
- `text_response_timing` — raw millisecond delta from N.H output to Ness reply
- `no_response_session` — session opened and closed with zero sent messages

Interface and system command events:
- `system_command` — only deterministic interface commands with stable command
  identifiers; ordinary spoken/typed language never produces this event type

Session state events:
- `session_opened`, `session_closed`, `session_interrupted`, `function_started`,
  `function_completed`, `function_interrupted`, `capture_failure`

**What BOP must never produce:**
- Emotional labels (e.g., "frustrated", "engaged")
- Identity conclusions
- Speaker-change detections
- Spoofing assessments
- Meaning attributions
- Pattern conclusions
- Importance judgments
- Any field that requires reasoning about why something happened
- Labels implying communicative function: not "correction", "continuation_request",
  "stop_signal", "hesitation_sound", "filler", "expected/unexpected silence"

All interpretation of what BOP observations mean belongs entirely to §7G.

**Voice priority rule:** When Ness speaks, N.H TTS stops immediately. This is
enforced by OOP during voice-mode function execution and recorded as an event
root if it occurs.

**Text-mode non-inspection rule:** Confirmed sent messages only. Unfinished
typing is never observed under any circumstances.

---

---

## 5. LMAC — Live Mechanism Access Coordinator

**Status: PROPOSED COMPONENT — ACCEPTED DESIGN, NOT YET BUILT**

### What LMAC Is and Is Not

LMAC is the coordination layer that gives every running function a single
interface through which it can query any part of the shared mechanism at any
moment, including mid-execution.

**LMAC is:**
- A live query interface that remains active for the full duration of a
  function's execution.
- A routing layer that connects function calls to the correct shared mechanism
  components.
- An enforcer of §7Q (Privacy) and §7P (Permission and Authority Boundaries)
  on every query.

**LMAC is not:**
- A context assembler that packages material and delivers it once at the start.
- A gatekeeper that decides what a function may reach.
- A cache between queries.
- A component with its own data store.
- A component that makes relevance judgments — relevance belongs to §7R.
- A component that applies privacy filtering — privacy belongs to §7Q.

### Owns Data

No. LMAC owns nothing. It holds no copy of any component's output. It holds
no accumulated view of Ness. Each query returns the current live state of
the queried component at that moment. LMAC is stateless between queries.

### How It Stays Connected to the Complete Mechanism

LMAC provides query interfaces to the live shared mechanism components and
routes those queries correctly. Every call from a running function to any shared
mechanism component passes through LMAC's routing layer.

LMAC does not cache results between calls. If the Living State Web's currency
status changed since the function's last query, the next query returns the
updated state.

### What LMAC Coordinates

When a function begins execution, LMAC provides an initial relevance-guided
working view using §7R with the function's declared purpose type. This is the
first query, not the only query. The function remains free to query any component
at any subsequent moment throughout its execution.

LMAC coordinates queries to:
- **§7F** — Context Retrieval
- **§7R** — Attention and Relevance Control (relevance, not LMAC itself, makes
  relevance judgments)
- **§7D** — Living State Web (current state, relationship edges, currency status)
- **§7L** — Person-Boxes (identity links, permission boundary records)
- **§7K** — Story Layer
- **§7J** — Clash Handling
- **§7Q** — Privacy eligibility pre-check (LMAC enforces §7Q, does not replace it)
- **§7P** — Permission boundary enforcement
- **§22** — Wellbeing Baseline current tier
- **Behavioral observation roots** — the most recent BOP-produced roots in the
  shared store (not a separate LMAC copy)
- **Response pattern readings** — the most recent readings of behavioral pattern
  material from the shared store (not a separate LMAC copy; not a stored
  configuration)

### How It Receives Updates During an Active Function

LMAC does not receive updates — it routes queries. Updates to the shared
mechanism happen in the shared store through their normal paths. When a function
queries LMAC for the current state of any component, it receives whatever the
current state is at that exact moment, including changes that occurred since the
function started.

### How It Avoids Creating a Reduced Model of Ness

LMAC is stateless between queries. It holds no accumulated view of Ness. It
does not filter which components a function may query — every component is
reachable through LMAC by any function that has permission to query it. §7Q
and §7P govern what a function may access; LMAC enforces those boundaries but
adds none of its own.

### What LMAC Explicitly Must Not Do

- Cache results between queries
- Filter which components a function may reach
- Make relevance judgments (it routes to §7R; it does not apply relevance logic)
- Override §7Q or §7P (it enforces them, not bypasses them)
- Produce a summarized or reduced version of any component's output
- Decide what a function should do with the context it receives

---

---

## 6. OOP — Outcome Observation Processing

**Status: PROPOSED COMPONENT — ACCEPTED DESIGN, NOT YET BUILT**

### What OOP Is and Is Not

OOP is the set of rules and processors that recognize when something that
happened after a function acted should be recorded as an outcome observation
root and route it through the existing path.

**OOP is:**
- A processing responsibility — not a store, not a feedback database.
- A source of new behavioral evidence for the shared store.
- The mechanism that closes the learning loop: action → outcome → evidence.

**OOP is not:**
- A store.
- A separate model of Ness.
- An interpretation layer.
- A component that decides whether N.H's behavior was good or bad.
- A component that directly changes N.H's behavior.

### Owns Data

No. All outputs are roots entered through §7E and readings produced by §7G.
OOP owns no data separately.

### What OOP Observes

OOP observes authorized signals from the post-action window during and
immediately after a function's execution. These signals are:

- **Voice behavior** (in voice mode): voice_onset, voice_offset, interruptions,
  silence patterns following N.H output
- **Text responses** (confirmed sent messages only; unfinished typing never
  observed)
- **Interruptions** — Ness's voice or text interrupting N.H output
- **Corrections** — messages that correct N.H's immediately preceding output
  (captured as the physical fact of a correction; content enters as a separate
  conversational root; OOP produces the timing and relationship metadata as an
  observation root)
- **Follow-up requests** — a new message arriving that continues or extends the
  prior topic
- **Session endings** — how the session closed relative to N.H's last output
- **Silence** — specifically only when the system expected a signal and conditions
  for observing it were satisfied

### The Absence-Is-Not-Confirmation Discipline

**Silence is evidence only when the system expected a signal and conditions for
observing it were satisfied.**

Absence of correction must be carefully distinguished from confirmed acceptance.
The absence of a response after N.H speaks is not evidence that Ness was
satisfied. It may mean he didn't notice, was doing something else, or the session
ended. OOP records the absence honestly as an absence, not as positive evidence
of any outcome.

This discipline follows §0A's DUMB/SMART boundary: everything OOP produces is
DUMB input — it records what happened, never what it means.

### How It Stays Connected to the Complete Mechanism

OOP produces roots that enter the shared store through §7E. Those roots are read
by §7G. The resulting readings are available to every other component through
the live shared mechanism — including to LMAC for future function queries, to
§7H for reread triggers, to §7J for clash detection, and to §7D for Living State
Web currency reviews.

### How It Routes

OOP routes outcome observation roots to:
- **§7E** (catalog front door) — entering them as a new root source type
  (`outcome_observation`)
- **§7H** (Reread Lifecycle) — when an outcome reading contradicts an existing
  reading, §7H's condition-based reread mechanism fires; the original reading
  is preserved; a new reading is placed beside it
- **§7J** (Clash Handling) — when a new outcome reading directly contradicts
  a prior reading
- **§22** (Wellbeing Baseline) — outcome observations from wellbeing-relevant
  sessions are tagged for baseline consideration

OOP does not route directly to response configuration, behavioral rules, or any
N.H output path. All changes to N.H's behavior emerge from §7G readings of
OOP-produced roots, not from OOP directly.

### How It Avoids Creating a Reduced Model of Ness

OOP produces only typed observation roots. It does not interpret outcomes. It
does not conclude that a configuration should change. It does not promote an
observation into a pattern. The Meaning Engine reads outcome observation roots
and produces readings. Pattern proposals surface through the normal evidence-stage
path.

### Self-Improvement Through OOP

N.H may observe its own outcomes and propose improvements to its own behavior
automatically through the OOP path.

**Rules for self-improvement:**
- N.H may propose improvements automatically — these proposals enter the shared
  store as readings and surface through the normal Computed View and authority path.
- N.H may not silently rewrite settled architecture, authority boundaries, or
  core rules.
- Any self-improvement proposal must enter the shared store as a reading before
  any behavioral change takes effect.
- Every automatic change must be: logged, explainable, traceable to evidence,
  and reversible.
- A small protected core — safety, ownership, authority, architectural integrity
  rules — is outside automatic self-rewriting and requires explicit Ness approval.

### What OOP Explicitly Must Not Do

- Treat absence of correction as confirmation
- Write interpretations — only raw typed roots
- Propose configuration changes directly — those must go through §7G
- Observe unauthorized sources
- Cross the DUMB/SMART boundary — everything OOP produces is DUMB input

---

---

## 7. Response Behavior — Recalculated Per Moment, Not Stored Configuration

**This is a critical settled rule.**

Response behavior is not a stored configuration that is applied. It is
recalculated at the moment of response from the whole mechanism.

When a function is about to respond, it queries LMAC for the current state of
the mechanism relevant to response behavior. That query returns:

- Readings of behavioral pattern material from the shared store (produced by §7G
  from BOP-produced observation roots)
- The current Living State Web picture (active states, open loops,
  capacity-relevant nodes)
- The current Wellbeing Baseline tier (from §22)
- The active permission and authority boundaries (from §7P)
- The active privacy boundaries (from §7Q)
- The current voice or text mode state

From these, the function calculates response behavior for this specific moment —
this person, this situation, this time, this state, this context. It does not
apply a fixed stored configuration. It uses pattern readings as evidence, weighted
by their confidence and firmness. Different patterns may point in different
directions; the function uses the whole picture to navigate.

This means response behavior may differ between two situations that appear similar
— because the whole mechanism is available to differentiate them, not just a
stored pattern label.

**No stored response configuration is ever promoted to a behavioral rule without
going through the Meaning Engine and surfacing through the Computed View to Ness.**

This design explicitly replaces the earlier RBCS (Response Behavior Configuration
Store) proposal, which was rejected. RBCS was rejected because it would have
created a stored configuration that gets applied as a fixed rule — which violates
the central architectural principle. There is no RBCS.

---

---

## 8. The 13 Personalization Areas as Views, Not Modules

The 13 personalization areas are not 13 components, not 13 stores, and not 13
separate models of Ness. They are **13 named views into the same shared material**,
distinguished by the source classification of BOP-produced behavioral observation
roots and the purpose types declared in LMAC queries to §7R.

All 13 areas access the same shared roots and readings through the same shared
components. No area has its own store, its own model, or its own version of Ness.

When a function is operating in one personalization domain (e.g., response
timing), it queries LMAC with a purpose type reflecting that domain. §7R weights
relevant material. But the rest of the mechanism remains reachable — a query for
relationship context or decision priorities can be made at any moment if
mid-execution evidence suggests they are relevant.

**The 13 areas (working vocabulary — subject to Ness's naming decisions):**

1. Response timing and pacing
2. Tone and register calibration
3. Language and vocabulary alignment
4. Processing depth preferences (how much N.H expands vs. stays concise)
5. Branch and topic navigation patterns
6. Decision-support preferences
7. Question-handling patterns
8. Silence and non-response interpretation
9. Emotional register recognition
10. Personal correction and feedback integration
11. Project and context continuity
12. Energy and capacity state awareness
13. Communication pattern adaptation over time

These names are working vocabulary. The underlying design (shared roots, shared
readings, LMAC purpose types, §7R weighting) is fixed. The naming of each area
is open to Ness's meaning-layer decisions.

**How the 13 areas connect to BOP, LMAC, and OOP:**

- BOP captures the raw observations relevant to each area (voice events, timing,
  text patterns, session state).
- §7G produces readings from those roots — readings that carry the area's
  conceptual content.
- LMAC provides running functions with live access to those readings by
  routing queries with the appropriate purpose type.
- OOP captures what happened after the function acted, feeding new evidence
  back into the same shared store.
- The cycle is continuous and cumulative. It does not restart. It does not
  produce a summary that replaces earlier evidence.

---

---

## 9. Self-Improvement Rules

These rules govern the full arc from first use through long-term operation.

**During any authorized session:**
N.H may automatically record all available authorized signals as behavioral
observations. No per-signal authorization is required within an already-authorized
session. This covers all 13 personalization areas simultaneously.

**Small response adaptations** (tone, timing, pacing, answer length) may happen
automatically. These are low-stakes, reversible adjustments. They do not require
Ness's explicit approval for each one.

**First 6–10 months — the learning period:**
During the first months of active use, N.H learns carefully and requests approval
before making major self-changes. The system is building its evidence base.
Pattern readings from this period carry lower confidence than readings from later
calibrated periods. The system flags its own uncertainty explicitly.

**After the learning period:**
N.H may make larger behavioral changes automatically when the evidence is strong
enough. "Strong enough" means: readings from multiple independent sessions, across
varied conditions, with consistent direction, without contradiction from recent
evidence, and at a confidence level that passes the current threshold for automatic
action.

**Every automatic change must be:**
- Logged (in the shared store via the OOP → §7E → §7G path)
- Explainable (the reading that produced the change must be traceable)
- Traceable to evidence (not inferred from a pattern summary; grounded in
  specific roots)
- Reversible (Ness can request reversion; the prior state is preserved)

**The protected core:**
Safety, ownership, authority boundaries, and architectural integrity rules are
outside automatic self-rewriting. These may only be changed through the explicit
Ness approval path, regardless of how strong the evidence is.

**Later evidence reconnection:**
Evidence from hours, days, weeks, or longer after an event must be able to connect
to an earlier observation and change the current interpretation without erasing
the original evidence or reading. The §7H condition-based reread mechanism is
the path for this. The original root and original reading are never altered. A
new reading is placed beside them. The full chain is preserved and auditable.

---

---

## 10. Architecture Map

```
SHARED MECHANISM — always live, always complete
─────────────────────────────────────────────────────────────────────
 Roots store (sealed)     Readings store (quarantine/production)
       ↑                              ↑
 §7E Catalog        →      §7G Meaning Engine      →    §7H Reread
 (front door)              (reads all root types)        Lifecycle
       ↑                              ↓
 BOP [designed]       →    §7K Story Layer
 (produces behavioral        §7D Living State Web
  observation roots)         §7L Person-Boxes
       ↑                     §7J Clash Handling
 OOP [designed]              §7R Attention/Relevance
 (produces outcome           §7Q Privacy
  observation roots)         §7P Permissions
       ↑                     §22 Wellbeing Baseline
  Function execution               │
       │                           ↓
       └──────────── LMAC [designed] ─────────────────┐
                    (live query interface;             │
                     stateless between calls;         │
                     routes to any component;         │
                     enforces §7Q + §7P;              │
                     no cache, no copy of Ness)       │
                           ↑                          │
              All N.H functions — connected           │
              to whole mechanism throughout           │
              their execution:                        │
              conversation / voice / research /       │
              simulation / memory / projects /        │
              decisions / reminders / file analysis / │
              music / every later function            │
                           │                          │
                     (function acts)                  │
                           ↓                          │
                  OOP observes outcomes ─────────────►┘
                  → new outcome_observation roots
                  → into §7E → §7G → shared store
                  → available immediately to next
                    LMAC query from same function
─────────────────────────────────────────────────────────────────────
```

**Key properties of this map:**

- The shared mechanism is always complete. No function sees a reduced version.
- BOP, LMAC, and OOP are processing responsibilities inside the shared
  architecture — not separate subsystems outside it.
- LMAC has no vertical boundary. It is a query interface to the whole, not a
  filter over part of it.
- OOP's outputs re-enter the mechanism at the bottom of the map, not at a
  separate configuration layer. The loop is through §7E → §7G, not through
  any behavioral rule store.
- The 13 personalization areas are invisible in this map because they are not
  structural components. They are purpose types declared in LMAC queries to §7R.

---

---

## 11. The Learning Period — First 6–10 Months

The learning period is a design-settled concept with specific behavioral effects.

**During the learning period:**

- Certainty thresholds for pattern readings are set conservatively. A reading
  that would pass a threshold after 12 months of evidence may not pass it at
  month 2.
- N.H requests approval before major self-changes. Small adaptations (tone,
  pacing, timing, answer length) remain automatic.
- The system explicitly flags its own provisional state. Pattern readings
  produced during the learning period carry explicit confidence markers
  showing they are from the calibration phase.
- Psychiatric appointment records (§22 calibration anchors) serve as anchor
  points for behavioral baseline calibration. They do not serve as identity
  proof, voice-identity training evidence, or access-control evidence.

**Transition out of the learning period:**

There is no fixed date at which the learning period ends. The transition happens
when the system's evidence base reaches a threshold of reliability across the
13 personalization areas — enough independent sessions, enough varied conditions,
enough consistent patterns, enough rereads that have survived without contradiction.

The 6–10 month estimate is a calibration target, not a commitment. The actual
transition may happen earlier or later depending on how frequently N.H is used
and how varied the evidence is.

**After the learning period:**

Larger automatic behavioral changes become available when evidence meets the
higher confidence threshold. The protected core remains unchanged regardless of
when the transition happens. Later evidence can always trigger rereads of earlier
patterns — the transition out of the learning period does not freeze earlier
conclusions.

---

---

## 12. What the System Explicitly Must Not Do

These prohibitions are settled rules, not guidelines.

**Architecture:**
- Must not create a separate behavioral observation store outside the shared
  accretive architecture.
- Must not create a private LMAC store or cache.
- Must not create a stored response configuration (no RBCS or equivalent).
- Must not create a parallel model of Ness alongside the shared mechanism.
- Must not split the 13 personalization areas into 13 separate subsystems.

**Data:**
- BOP must not produce emotional labels, identity conclusions, communicative
  function labels, or any interpretation of meaning.
- BOP must not observe unfinished typing.
- BOP must not record voice signals from unauthorized sources.
- OOP must not treat absence of correction as confirmation.
- OOP must not propose configuration changes directly.
- LMAC must not cache results between queries.
- LMAC must not hold an accumulated view of Ness between sessions.

**Behavior:**
- N.H must not silently rewrite settled architecture, authority boundaries,
  or core rules through the self-improvement path.
- N.H must not apply a stored pattern as a fixed behavioral rule without going
  through §7G.
- N.H must not make a major self-change during the learning period without
  requesting approval.
- N.H must not treat the wellbeing system's outputs as identity evidence or
  access-control inputs.
- N.H must not surface the computed view of what it knows about Ness
  unprompted. The Computed View is internal only.

**Evidence:**
- The system must not treat repeated observations as confirmation. Repetition
  does not confirm a pattern — §7K's firmness rules apply.
- The system must not erase original roots or readings when new evidence
  arrives. All changes are new readings beside the original.
- The system must not promote an observation into a settled behavioral fact
  without going through the full evidence-stage path.

---

---

## Open Items (Not Yet Decided)

The following questions were identified during the design process as requiring
Ness's concept-level decision. They were recorded as open rather than filled in
by the design work.

**D1 — Authorization boundary for behavioral observation.**
BOP records indirect reactions automatically within authorized sessions. The
open question is whether any specific category of behavioral signal requires
explicit per-signal authorization before BOP may record it — for example,
signals derived from silence, or signals from interactions Ness did not initiate
with N.H. The current rule is: any session explicitly opened by Ness with N.H
is authorized for behavioral observation; no additional per-signal authorization
is required within that session. Whether this applies to all signals or whether
Ness wants some categories to require additional authorization is not yet closed.

**D2 — The 13 personalization area names.**
The current names (listed in Section 8) are working vocabulary from the design
session. These are Ness's concept-layer decisions — the correct names should
emerge from Ness's meaning-first naming process (the same process used for all
N.H naming decisions). The underlying design structure is fixed; the names
are not.

**D3 — Voice mode observation scope during imported content.**
When an imported voice message is processed, what is OOP's observation scope?
May it observe Ness's live reaction to the imported content (his voice tone while
listening, his response immediately after), or only the imported content itself?
This is a privacy and authorization boundary question that has not been closed.

---

---

*End of NH_ACCEPTED_PERSONAL_LEARNING_DESIGN_v1.md*

*This file was created June 29 2026 as a standalone accepted design record.*
*It does not modify the Master, Decision Defaults, .cursorrules, or any*
*implementation file. It must be formally patched into the Master through*
*the accepted patch-only, no-loss protocol before it carries Master authority.*
