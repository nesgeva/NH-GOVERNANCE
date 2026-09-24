# DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY

**Authoritative source:** `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`  
**Source SHA-256:** `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152`

This file is a reader/working copy for focused use with Claude or ChatGPT.  
The complete source file remains authoritative. Section wording below is copied from the source and must not be edited independently. Any real change must be made in a new complete Master version, then the reader copies regenerated.

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed]

### 7A — THE UNIVERSAL FILTER (operating rules):
R0 reader/layer-er not judge; R0.5 never close the book; R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; R5.5 the affirmation surface is a per-person STORY-layer (six optional parts; absence read ONLY under the §0A guard; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE); R6 memory only ADDS (governs HISTORY; the COMPUTED VIEW decides current use); R7 the membrane; R8 associative bridging; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is.

### 7B — THE MEANING ENGINE (mechanism):
Part 0 THE PURE TAPE (verbatim, append-only, outside memory; capture-exclusions + audited redaction — §0A); Parts 1–2 the chain of webs; Part 2.5 THE STORY-LAYER WEB; Part 2.6 PERSON-BOXES; Part 3 webs combine; Part 4 nightly research (feeds MEMORY, not the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask); Part 6.5 THE WONDER/SIMULATION; Part 7 THE LOG; Part 7.5 THE NOTE/THE WHY.

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots + READING RECORD — ✅ COMPLETE (S14).** → **(2b) the detector — ✅ INVESTIGATED, recipe locked (S13); fallback, not deployed.** → **(2c) THE ENGINE — IN PROGRESS:** A ✅ BUILT (S14) → B ✅ BUILT (S16) → **C (story-layer) NEXT.** C needs story-bearing gold cases before it can be tested. **Build the LIVE path before the nightly deepening.**

**★ THE ENGINE LAYERS:**
- **A (BUILT, S14):** root → mouth ("say what the {role} is doing, don't describe/answer/invent") → 12-field reading → quarantine. Bare; no context, no story. ~5–6/8 on gold v1.
- **B (BUILT, S16):** + preceding turns context — `_get_preceding_turns(n=3)` pulls N roots immediately before the target in the same thread. BACKGROUND/END BACKGROUND prompt framing. Full content, no truncation. Tested dolphin 8B setup scored 6.5/7 on gold v2-B; the cause of the remaining miss has not been isolated — model capability, prompt framing, context format, and run variance remain possible contributors. **Future upgrade: full-thread reading with a larger model + larger context window — must be benchmarked, not assumed.**
- **C (NEXT):** + story-layer reading — fill `story_layer` (whose/firmness/theme). Needs story-bearing gold cases first.

---

## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT

WHY IT EXISTS. N.H currently models what something means, who said it, what story it belongs to, and what memories relate to it. That is a strong foundation. But a person is not only meanings and memories. At every moment a person also occupies a state — emotional, cognitive, bodily, practical — and moves through transitions between states across time, pressure, choices, and consequences. The Living State Web is the name for the future layer that would let N.H model that movement, rather than only interpreting individual messages.

WHAT DEPTH IT ADDS. The current engine reads a root and lays a reading beside it. The Living State Web would eventually allow N.H to understand not only what something means, but: what state may have shaped or accompanied it, what may have changed across relevant states, events, and readings over time, what is currently active and unresolved, what may be reachable from the present state, and what happened after action was taken. That is the difference between a meaning system and a partner that can model a living person moving through time.

CURRENT STATUS. PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT. S17 designed node and edge types, grounding rules, currency rules, action surfacing (§7N), the action-result return path (§7O), and relationships to Computed View, Story Layer, Person-Boxes, authority boundaries, and privacy boundaries. Several domains and all implementation details remain undesigned.

WHAT WAS DESIGNED IN S17 AT THE STRUCTURAL CONCEPT LEVEL.

Node and edge types: state nodes (time-bounded representations of experienced states), transition edges (possible connections between states with evidence), position nodes (simultaneous internal stances), open loop nodes (unresolved items consuming attention), relationship state edges (time-bounded connection states with people), causal hypothesis edges (proposed causal connections, always marked as hypotheses), counterfactual nodes (modeled possible worlds, always separated from actual states), value and constraint nodes (active values, fears, protected boundaries).

Grounding rule: every node carries (a) immediate source object IDs (readings, tellings, clashes, Ness response events, or other explicitly permitted derived objects) and (b) direct root IDs ultimately grounding it. Full derivation chain must remain inspectable. Circular support is forbidden — derived material cannot validate itself without root support. A node may not exist solely because another derived object asserted it. Weak or broken chains produce omission or an insufficiently-grounded marking, never invention.

Currency rule: state existence and currentness are two independent properties. Every state node records evidence time range, `last_supported_at`, currentness status, reason for that status, and rule/version used to assess currency. Six conceptual statuses: `current`, `possibly_current`, `stale`, `currentness_unknown`, `ended_by_evidence`, `superseded_by_evidence`. Time passing may move a node toward stale or currentness_unknown but may never alone mark a state ended. A state may be marked ended or superseded only through relevant new root evidence, a Ness response, or another explicitly authorized evidence-based rule. Different state types use different currency rules — a brief condition and a long-term constraint do not age at the same rate. Currentness is never a hidden decay score.

Action surfacing and return path: designed in full at §7N and §7O respectively. The Living State Web provides the state, open loop, value, and constraint evidence that action surfacing draws from.

RELATIONSHIPS NOW DESIGNED.

Computed View: the Living State Web is one source the Computed View draws from when assembling the current picture. The Computed View's seven-factor ordering and triggered snapshot rules apply when Living State Web material is surfaced.

Story Layer: story tellings are eligible source objects for Living State Web nodes. Tellings supply perspective and theme context. Story Layer rules on circular support and firmness apply when tellings are used as evidence.

Person-Boxes: relationship state edges in the Living State Web point to Person-Box identity anchors. Person-Box confirmation status and merge-proposal rules govern which identity anchor an edge may point to.

Permission and authority boundaries: action possibilities surfaced from the Living State Web pass through the authority system before any execution. §7P governs what may be done with surfaced possibilities.

Privacy boundaries: Living State Web nodes derived from third-party material follow the third-party data rules in §7Q. Pre-retrieval eligibility and pre-output review apply when Living State Web content is shown.

FUTURE DOMAINS — PARTIALLY DESIGNED AT THE STRUCTURAL CONCEPT LEVEL. The following had supporting structures designed in S17 (node types, edge types, currency, or retrieval rules), but their complete behavior, evidence requirements, interaction rules, and update mechanisms are not yet settled: transitions between states and what drives them; multiple simultaneous internal positions; relationship state and relational safety; possible causal chains; counterfactual paths; temporal identity across past, present, and possible future states; the loop act → observed result → reread (§7O); identity continuity across time and contexts (the currency rule supports temporal tracking but does not complete identity continuity design).

FUTURE DOMAINS — NOT YET DESIGNED AT ANY LEVEL: current emotional, cognitive, bodily, and practical state schema; needs, fears, protected boundaries, and active constraints schema; current capacity and cognitive/emotional load (open loop nodes may relate to capacity but are not the same — capacity/load representation is not yet designed); attention and relevance control; purpose-aware reading lenses; a world model beside the self model.

REMAINING UNRESOLVED: exact schema for all node and edge types; minimum evidence requirements and grounding-strength rules; currency time windows and state-type-specific aging rules; transition condition definitions; relevance triggers for condition-based action surfacing; mapping of specific action categories to the four risk levels and category-specific evidence/permission thresholds; detection rules for automatic result detection; confirmation workflow for result connections; attention and relevance control mechanism; purpose-aware reading lenses; world model beside the self model; build order position relative to other components.

HOW IT FITS N.H PHILOSOPHY. The Living State Web maps the state-space and possible movement. It never chooses the path. It never promotes its interpretation into settled truth. Ness remains the decider; the engine remains a helper. These are not new rules — they are the same soul rules that govern every existing layer.

---

## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO GATES. Raw capture and root ingestion are separate. A root cannot be written to the sealed store until all required catalog fields are resolved. Raw material is never destroyed merely because a field is unresolved.

MINIMUM INTAKE ENVELOPE. Every front door must produce the same minimum before the pre-ingest store accepts the capture: (1) one stable unique `capture_id`; (2) the exact raw payload or a stable immutable reference to it; (3) capture timestamp; (4) front-door / source type; (5) payload format or media type; (6) source-provided metadata, preserved without reinterpretation; (7) enough provenance to trace how and where the capture occurred. Front doors may additionally provide any reliable source-derived catalog fields they already know. They must not guess missing values to satisfy handoff.

DESIGN BOUNDARY. `front door = capture and normalize` / `pre-ingest catalog = evaluate completeness and manage resolution`. A front door cannot hand over an unidentifiable blob. A malformed capture that cannot meet the minimum envelope enters an explicit capture-error path with available material preserved. Never silent drop.

PRIVACY AND EXCLUSION PRECEDENCE. The catalog's preservation rules apply only to eligible, non-excluded material. The privacy rules in §7Q override catalog preservation for live credentials, non-negotiable secrets, Ness-configured exclusions, redaction, deletion, and mixed-content separation. When excluded material is present, N.H may preserve only the safe permitted remainder and non-reconstructive exclusion metadata; it must never preserve the excluded content merely to satisfy the catalog's no-silent-drop rule.

PRE-INGEST HOLDING AREA. One unified pre-ingest store. One item, one `capture_id`, one stable location, a list of blockers (e.g. `["speaker_unresolved"]`, `["thread_unresolved"]`, or both). Raw payload never rewritten. Material may remain in `held` indefinitely. Held material is invisible to the Meaning Engine unless an explicitly designed inspection mode says otherwise. One blocked item never blocks unrelated ready items. Silent deletion never permitted. Idempotent: repeated processing never creates duplicate roots. Promotion to the root store is atomic. After promotion, the pre-ingest record stays as provenance with the resulting `root_id` recorded.

LIFECYCLE STATES (conceptual): `held` → `ready` → `promoting` → `promoted`; plus `rejected`/`excluded` (intentional, with reason) and `error` (processing failed, material preserved).

CONCEPTUAL RECORD SHAPE includes at minimum: `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state, resulting `root_id` if promoted.

SPEAKER RESOLUTION RULE. `role` must come from source, not be guessed. Raw capture may happen without a known speaker; root ingestion cannot. Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`. A speaker detector may propose a candidate — that proposal is uncertain and remains a proposal until confirmed by Ness or supported by source evidence. Never silently promoted into the `role` field.

SOURCE TITLE RULE. `source_title` is a grouping key for Engine B's positional context retrieval. Rules: (1) Source provides a real thread identifier → carry it exactly. (2) Source missing but items provably belong together → one unique non-semantic placeholder per capture session: `untitled:paste:<capture-session-id>`, `untitled:voice:<capture-session-id>`. (3) Isolated item → unique singleton placeholder. (4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`. A machine-generated topic or summary must never become `source_title`. Future schema: separate `thread_id` (stable grouping key) from optional human-readable display label. Sealed roots are never rewritten; later clarification goes through an alias/correction layer (design deferred).

FOUR ENRICHMENT CATEGORIES.

**A. Source-carried facts — accepted as catalog facts.** Sender/speaker, source role, original timestamp, thread/conversation identifier, platform name, source title, message ordering, filename, attachment identifier, source media type. Provenance of each fact recorded.

**B. Deterministic mechanical derivations — allowed.** Content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index, normalized timestamp. Rules: preserve the original source value; store derived value separately; record method and version; never replace original with normalized form; derivation failure does not alter or destroy the capture.

**C. Machine-inferred classifications — proposals only.** Detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection, possible continuation. Stored only as proposals with: proposed value, producer/model/rule, evidence, confidence, timestamp, confirmation status. Never becomes a settled catalog fact without confirmation by source evidence, Ness, or an explicitly authorized resolution rule.

**D. Semantic interpretation — forbidden in the catalog.** Topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event, what a person "really meant." These belong to the Meaning Engine, reading layer, story layer, or later systems.

BOUNDARY TESTS. "Does this describe what the material physically/source-wise *is*, or does it explain what the material *means*?" And: "Could two reasonable readers disagree because they interpret the content differently?" If yes to the second, it belongs outside the catalog.

The raw captured payload is never rewritten. Enrichment metadata develops around it. Exact schemas, field names, and which derived values enter the future root schema remain undesigned.

---

## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO CHANNELS, ALWAYS SEPARATE. Positional context answers: "What was happening immediately before this root in the same thread?" Semantic context answers: "What other stored material may relate to this root?" These are different kinds of evidence. A semantically similar memory may come from a completely different time, person, event, or situation. Similarity is not proof of relevance.

Positional and semantic retrieval are separate channels. Every retrieved item carries retrieval provenance: retrieval type, why it was selected, source root ID, source thread/grouping, timestamp, retrieval score or position where relevant. When both are supplied, the prompt structure must show them in separate sections. The model must not be able to mistake a semantic match for a preceding turn. A conflict between positional and semantic context is surfaced, not silently resolved. Semantic retrieval never overrides or silently repairs positional context.

CHANNEL COMBINATIONS. The engine may receive: positional only, semantic only, both channels, or neither — depending on the explicitly designed reading mode.

FOUR CONCEPTUAL MODE CATEGORIES (not final names or settings): bare (no context), local-context (positional only), associative (semantic only), combined (both channels, still separated).

RETRIEVAL PARAMETERS ARE PER-MODE, NOT UNIVERSAL CONSTANTS. Every reading mode explicitly declares its own: positional-context limit, semantic-result limit, semantic threshold or ranking rule, eligible source scope, time range if any, token/size budget, and fallback behavior when insufficient context is found. Parameter values must be tested empirically against gold sets before defaults are locked. Testing must examine reading quality, whether relevant context was retrieved, whether irrelevant context was introduced, whether semantic matches were mistaken for direct context, reproducibility, latency, cost, and sensitivity to changing the limits.

All retrieval is bounded. No mode may request unlimited results. Hard safety ceilings exist above mode-level settings so a configuration error cannot retrieve unbounded material. Exact ceiling values remain undesigned.

Engine B's n=3 remains the configuration of the built Engine B experiment. It does not establish 3 as the universal future positional limit.

AUDIT TRAIL. Reading record must eventually preserve: reading mode, configured parameters, retrieval system/model/index version, exact roots supplied, scores or positions, exclusions or truncation caused by limits, execution timestamp.

GENUINE NO-CONTEXT HANDLING. When retrieval returns nothing because no relevant context exists — first root in thread, or no semantic results above threshold — these are normal conditions, not failures. Engine proceeds with the target root only. Reading record must state: which channel returned nothing, why, that bare fallback was used, that the reading is context-limited and revisable. The system must not invent, lower thresholds silently, or substitute unrelated memories.

SYSTEM FAILURE SEPARATION. Index error, stale/incomplete index, timeout, unreachable service are system failures, distinct from genuine empty results. System must never claim retrieval succeeded when it failed. Exact fallback behavior for system failures remains undesigned.

Trigger conditions for semantic retrieval, exact retrieval limits, ranking methods, thresholds, and safety ceiling values remain undesigned.

---

## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

ONE READING PER PASS. One pass, one reading record, one target root. Multiple angles require multiple explicit passes. Every pass declares its reading mode, purpose, or angle. Multiple readings may point to the same root; each is separate with its own context inputs, engine version, configuration, and timestamp. A new reading never overwrites an older one. Conflicts between readings stay visible, never silently merged. Later synthesis is a separate layer and does not rewrite existing readings. The engine must not create hidden secondary interpretations outside the reading record.

ENGINE FLOW. Target root + optional positional context + optional semantic context + declared reading mode → mouth proposal → Reading Proposal Acceptance Check → reading record.

★ FIRST-CLASS PRINCIPLE — MODEL CONFIDENCE IS METADATA, NOT AUTHORITY. This principle applies to all present and future models used inside N.H, regardless of model size, architecture, or claimed capability.
1. Model confidence is metadata, not authority.
2. A confident response may still be wrong, unsupported, or invented.
3. Acceptance depends on grounding in the target root, supplied context, declared reading mode, and explicit evidence — not on what the model claims about itself.
4. Unsupported certainty must be rejected or downgraded by the acceptance layer.
5. Honest uncertainty is preferable to confident fabrication.
6. No reading is accepted solely because the mouth model labels itself confident.
7. The acceptance layer must record why a proposal passed or failed — not just the outcome, the reasoning.

READING PROPOSAL ACCEPTANCE CHECK. An explicit acceptance step runs between the mouth's proposal and the reading record. The mouth does not judge its own output alone.

The acceptance check verifies at minimum: required fields present and valid; meaning grounded in the target root or supplied context; no claims invented beyond available evidence; positional and semantic context not confused with each other; uncertainty expressed honestly; response does not contradict its own evidence; declared reading mode was followed.

A response fails acceptance when it: invents facts, overstates certainty, relies on context not supplied, confuses semantic similarity with direct context, violates the reading mode, is malformed or incomplete, or cannot support a meaningful interpretation from available evidence.

ON ACCEPTANCE FAILURE. The proposal is rejected and the specific failure reason is recorded separately. `insufficient_context` is used only when the available root/context cannot support a grounded interpretation. Fabrication, unsupported certainty, positional/semantic channel confusion, reading-mode violation, malformed output, and incomplete output are recorded as distinct proposal-rejection reasons rather than being mislabeled as context insufficiency. Under a future explicitly designed bounded fallback/retry rule, the engine may make a fresh proposal; if it still cannot produce a grounded reading, it writes the honest revisable `insufficient_context` reading required by the S14 engine-failure rule. The rejected proposal may be preserved in an audit log, but it must never silently become the accepted reading. The engine never invents.

Acceptance result, reasons, validator version, and relevant checks should eventually be recorded for reproducibility. Exact criteria, thresholds, retry behavior, and whether validation uses rules, another model, or both remain undesigned.

STORY-LAYER EVIDENCE RULES. The story-layer pass may retrieve both prior roots and prior readings, but they must remain in separate, clearly labeled context channels.

Two separate context channels for story-layer passes: (1) root evidence channel — original source material, higher evidential status; (2) prior reading context channel — previous interpretations, interpretive status only. Roots and readings must never be merged into one undifferentiated evidence block.

Grounding rule: every story telling must be grounded in supporting root IDs. Prior reading IDs may support continuity, comparison, or discovery, but a telling is never accepted solely because earlier readings stated it.

Circular support is forbidden: a reading cannot become true merely because later readings repeat it; derived material cannot endlessly validate other derived material without root support; an unfinished output from the current pass may not be used as its own evidence; only completed prior readings are eligible.

Conflict rule: conflicting readings remain visible and are not silently resolved. The story layer surfaces clash; it does not arbitrate it.

On weak evidence: if root support is insufficient, the telling is omitted or marked `insufficient_context`. Never invented.

Audit trail: every root ID and reading ID supplied to the story-layer pass must be preserved.

Exact retrieval scope, ranking, limits, and firmness criteria remain undesigned.

---

## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT]

A reread never happens without an explicit recorded reason. Three trigger types are allowed, each bounded.

MANUAL. Ness may request a reread at any time. No further justification required.

CONDITION-BASED. Triggered when materially relevant new information becomes available: new positional context, new root evidence, resolved speaker or thread information, corrected provenance, a newly available required context channel. Time passing alone is not a condition. Any new memory does not automatically trigger rereading everything. Relevance must be established under an explicitly designed rule.

SCHEDULED AUTOMATIC RETRY. Allowed only for temporary system conditions: model/service timeout, unavailable or stale index, interrupted processing, other explicitly retryable technical failures. Not for reinterpretation. Bounded, idempotent, protected against duplicate rereads and endless retry loops.

ON NESS REJECTING A READING. The rejection is recorded. The reading is marked and may become eligible for reread. Rejection does not prove the opposite interpretation is correct.

EVERY REREAD RECORDS. Trigger type, trigger reason, who or what initiated it, new evidence or changed condition, previous reading IDs, new configuration and timestamp.

A reread creates a new reading. It never overwrites, edits, or deletes the earlier reading. A revisable reading may remain unrevisited indefinitely if no trigger occurs.

Exact relevance rules, retry limits, scheduling, and orchestration remain undesigned.

---

## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO VIEWS. Simple by default, complete on demand. Ordering is presentation only — it never resolves conflict or grants authority.

CURRENT VIEW (default). In a simple per-root reading list, surfaces the newest usable reading first. Usable = passed acceptance, not marked rejected or `insufficient_context`. This does not mean it is true or final. Conflicts must be surfaced explicitly — for example: "A conflicting reading also exists." Revisable, rejected, and insufficient-context readings remain visible with clear labels. Whenever the interface claims to show the **current best-supported** reading or assembles a broader current picture, §7M's seven-factor ordering governs; recency is only a limited tie-breaker.

HISTORY VIEW (complete record). Every reading in strict chronological order. Ness may switch to it at any time. Always available, never hidden.

STANDING RULES. No reading is deleted, hidden permanently, or overwritten. Different reading modes may be grouped separately when helpful, but the original chronology remains available. Ordering is presentation only. Newest reading shown first does not make it authoritative, correct, or final. Simple by default, complete on demand.

Exact grouping rules, labels, interface layout, and definition of "current usable reading" remain undesigned.

---

## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT]

SIX CLASH TYPES.
1. **Direct contradiction** — two readings of the same root produce mutually exclusive meanings.
2. **Interpretive divergence** — same evidence, different conclusions, neither strictly excludes the other.
3. **Temporal change** — inconsistency between readings at different times that may reflect genuine change, not error.
4. **Perspectival difference** — different speakers' or observers' framings of the same event, each accurate within its own perspective.
5. **Evidence insufficiency** — conflict because neither reading had enough context to be reliable.
6. **Context mismatch** — apparent contradiction from different reading modes or retrieval configurations, not a real conflict in the material.

GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE. Core test: could both statements be simultaneously true under the same conditions, for the same person, at the same time, in the same context? If yes — contextual difference. If no — genuine contradiction. N.H records the distinction, never resolves it.

CLASH RECORD SHAPE (conceptual). Stable identifier, clash type, pointers to exact readings and roots involved, description of what specifically conflicts, retrieval configurations and reading modes of conflicting readings, detection mode, confidence of clash detection, lifecycle state, Ness response status, timestamp. Every clash record points to the exact supporting roots and readings. Original roots and readings remain unchanged.

TWO DETECTION MODES, SAME RECORD TYPE.

Triggered detection: runs when a new reading is written. Compares against readings of the same root, readings in the same thread, and other explicitly related readings.

Periodic or on-demand detection: scans wider scope — across roots, threads, people, time periods, story layers. Catches slow-developing and cross-thread contradictions.

Both modes produce the same conceptual clash-record type. Every clash record states its detection mode. The same clash must not produce two independent records — later detection appends a new detection-history event linked to the existing clash. Wider scans may append evidence or propose a refined classification through linked events, but they do not mutate the original clash, rewrite original readings, or spawn duplicate clashes. Detection mode does not affect authority. Neither mode may resolve, rank, or select a winner. Periodic scans are bounded and configurable.

NESS'S RESPONSE AS SEPARATE EVENT. Every response has its own stable event ID and points to the clash ID. It does not live inside the clash record. Every response event records: response type, Ness's exact statement or selection, timestamp, evidence or explanation supplied, any requested downstream action.

Response types include: one reading accepted over another, both valid in different contexts, genuine change over time, insufficient evidence to judge, detection artifact, deferred judgment, request for reread, or another explicitly defined type.

Ness may respond multiple times. Later responses do not erase earlier ones. Full response history always preserved. Current view may show the latest Ness response; full response history available on demand.

Downstream actions are separate linked records. A response event and the action it triggers are distinct records that point to each other. Ness choosing one reading does not delete the other — his judgment is recorded and may affect the computed view or presentation. It does not alter the underlying readings, roots, or clash record.

A clash is not automatically an error. N.H never silently resolves it. Exact schemas, detection methods, schedules, deduplication logic, and downstream effects remain undesigned.

---

## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Receiving tellings produced by engine passes and recording them without alteration. Organizing tellings by whose perspective they reflect, what theme they belong to, and when they were produced. Surfacing how a narrative thread has developed, shifted, or fractured across time. Preserving clash between tellings without resolving it. Making it possible to ask: what has been said about this person, theme, or period — and from whose perspective, with what firmness, supported by what roots. Distinguishing temporal change from contradiction. Keeping each person's story separate from every other person's.

MUST NEVER. Merge conflicting tellings into one synthesized narrative. Promote a repeated telling into established fact merely because it appears often. Assign a single authoritative story to a person, relationship, or event. Invent connective tissue between tellings that the roots do not support. Treat a gap in tellings as evidence of absence. Flatten temporal change into a single stable description. Allow one person's perspective to silently overwrite another's. Resolve whose telling is correct — that is Ness's judgment, off-board.

TELLING VS ONGOING STORY. A telling is one interpretation, produced in one engine pass, about one root, from one perspective, at one moment — local, bounded, specific. An ongoing story is the collection of tellings across time — with agreements, shifts, contradictions, silences — organized so that patterns can be seen without being hardened into conclusions. The story layer can surface the sequence; it cannot conclude from it.

CONNECTIONS ACROSS TIME. Tellings connect through explicit shared attributes: same `whose`, same theme, same thread or source, overlapping time period, or shared root IDs. These are navigational links, not logical merges. Always labeled with what they are based on, always pointing back to supporting roots and readings.

STRUCTURED PERSPECTIVE MODEL. Three minimum fields per telling:
- `root_speaker` — who produced the source root.
- `subject` — who or what the telling is about.
- `perspective_owner` — whose viewpoint, belief, feeling, or framing the telling claims to represent.
Optional: `attribution_path` — used when perspectives are nested (e.g. `friend → quoted by father → reported by Ness`). Populated only when the root supports the chain. Never invented.

These roles may refer to the same person or different people. The Story Layer never assumes the root speaker is automatically the subject or perspective owner. Evidence relationship must be recorded for every telling: direct self-report, direct quotation, reported speech, observation, or engine inference. Reported speech is not direct access to the reported person's internal state. The engine's interpretive lens stays separate from the human perspective represented in the telling. Unknown attribution stays explicitly unresolved. Existing flat `whose` field may remain for v1 compatibility; future schema should use the structured perspective fields.

OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED. In the built v1 reading schema, tellings are embedded entries inside the reading record's `story_layer` list; no separate first-class telling record is built. S17 treats a telling conceptually as something other components may link to, but it did not choose its future storage identity. Before Story Layer, Person-Box, clash, or deletion code relies on telling-level links, one identity method must be designed explicitly: either a separate immutable telling record or a stable composite reference within its immutable parent reading. This master does not choose between those options, and no implementation may assume standalone telling IDs until that seam is settled.

FIRMNESS RULE. Firmness and model confidence are separate dimensions. `firmness` = how strongly the perspective owner appears to hold the stance. `confidence` = how well-grounded the engine believes its reading to be. These are independent.

Firmness may be inferred from observable signals: explicit certainty words, hedging, repetition, emphasis, consistency within the root, direct statements of commitment or doubt. Every firmness value records its evidence basis. Firmness is always provisional and revisable. Direct self-report of certainty is stronger evidence than tone, wording style, or repetition alone. Reported speech or uncertain attribution lowers evidential strength. N.H must never present firmness as direct access to a person's internal state. Conflicting signals produce mixed firmness, uncertain firmness, or omission — never a forced resolution. If the root does not support a firmness judgment, the field is omitted. Exact scale, labels, thresholds, and scoring method remain undesigned.

HYBRID THEME SYSTEM. Engine proposes freely. Only Ness confirms. Confirmed themes are navigation categories, never facts.

Engine-proposed themes start as `proposed`, never as settled categories. May be generated from a single telling or patterns across multiple tellings. Every proposed theme records: supporting root IDs, supporting telling/reading IDs, who or what proposed it, why those items appear connected, timestamp, uncertainty.

Ness may: confirm, rename, merge, split, reject, or leave a proposed theme unresolved indefinitely. Unresolved proposed themes do not become confirmed by aging or repetition.

A telling may belong to no theme, one theme, or multiple themes. Membership is not exclusive. Circular support is forbidden — pattern-derived themes must retain root support. Repetition does not confirm. A theme cannot validate itself by being frequently proposed.

Proposed themes must not silently shape future readings. If a confirmed or proposed theme is used to retrieve context for a future engine pass, that influence must appear in the retrieval audit trail. Future readings may challenge, omit, or contradict an existing confirmed theme.

Ness-controlled vocabulary is open and extensible. Theme aliases may connect different labels across time without rewriting older tellings. Exact theme schema, similarity grouping, confirmation process, and retrieval influence remain undesigned.

---

## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Maintaining a stable identity anchor for a person. Linking roots where this person appears, is mentioned, is quoted, or is the subject of a telling. Linking readings and tellings that involve this person in any perspective role. Linking clashes that involve this person. Linking Ness's responses where relevant. Recording how each link was established and how certain it is. Tracking proposed identity connections without silently merging them. Surfacing what has changed over time about how this person appears across the store.

MUST NEVER. Synthesize linked material into a summary description or personality profile. Promote a frequently appearing interpretation into a settled fact about the person. Treat a report about someone as equivalent to that person's own perspective. Merge two uncertain identity references without explicit resolution. Treat absence of information as evidence of anything. Resolve contradictions between tellings. Allow one perspective owner's framing to silently become the authoritative view of the subject. Invent connections not explicitly supported. Become a diagnosis, personality model, fixed character description, or closed identity. Claim to represent what a person is like — only what N.H has observed or been told, from whom, with what certainty, at what time.

LINKABLE OBJECT TYPES. Roots, readings, story tellings, themes (with confirmation status), clash records, Ness response events, other Person-Boxes (where identity connection proposed or confirmed), and **metadata-only** references to pre-ingest records where the person appears. Held pre-ingest raw content remains invisible to Person-Box semantic analysis unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be linked. Every link records: what it connects, why, who or what established the connection, certainty, and timestamp. Links are never copies — the original object stays where it is.

UNCERTAIN IDENTITY. Uncertain identity is the normal state. A reference anchor records: the label or name used, where it appeared, when, what evidence connects it to a specific person, and current certainty level. Multiple anchors may exist for what might be the same person. They remain separate until a resolution rule — Ness confirmation, strong source evidence, or another explicitly authorized rule — merges them.

PROPOSAL-BASED CREATION. N.H may detect a new person reference and create a proposed identity anchor, but it must not silently create a confirmed Person-Box or decide that two references are the same person.

Every Person-Box has a stable system-generated ID. Human-readable names, labels, and roles attach separately and may change. A new unrecognized reference may generate a proposed anchor when encountered through a front door, root, reading, story telling, or other authorized source. A proposed anchor is not a confirmed Person-Box.

Before proposing a new anchor, N.H must search: confirmed Person-Boxes, unresolved identity anchors, aliases, and previous merge proposals. Similar names or labels alone are not sufficient to merge. Possible duplicates produce a separate merge proposal, never a silent merge.

Ness may: confirm, reject, rename, keep unresolved, link to an existing Person-Box, or propose a merge. Strong source evidence may confirm identity only under an explicitly authorized resolution rule.

Confirmed merge: links identity anchors under one stable identity view. Does not rewrite roots, readings, tellings, or historical links. If a merge is later found wrong, correction is recorded through new events or links. History is never rewritten.

Unresolved references may remain separate indefinitely. Exact matching rules, evidence thresholds, confirmation workflow, and merge mechanics remain undesigned.

DEFAULT VIEW. Seven separate sections: roots, readings, story tellings, clashes, Ness response events, themes, unresolved identity anchors and merge proposals. Every section states what it contains and its evidential status. These are never visually flattened into equivalent claims. Section order is navigation only — not authority, reliability, importance, or truth. Frequency and recency do not silently determine reliability.

Ness may filter or reorganize by: time, perspective role, theme, source/thread, lifecycle or confirmation status. Full chronological view always available. Conflicts, unresolved identity questions, and uncertain links surfaced clearly. Simple by default, complete on demand.

Exact layout, section order, filters, and labels remain undesigned.

---

## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The present-facing surface of N.H. Its job is to take all accumulated material and produce a navigable, useful picture of what N.H currently has reason to show, without altering any underlying objects or pretending that one interpretation has won.

RESPONSIBILITIES. Assembling the most useful current picture using explicit derivation rules. Surfacing the current best-supported reading for a root, story thread, person, or theme while preserving access to alternatives and history. Reflecting Ness's explicit responses without treating them as rewrites of history. Distinguishing evidence, engine interpretation, Ness's explicit judgment, and unresolved material. Updating automatically when triggered. Preserving a record of what the view showed at previous points in time.

MUST NEVER. Rewrite, alter, merge, or delete any root, reading, telling, clash, or response event. Silently select one reading as authoritative. Treat most recent or most frequent interpretation as more reliable without explicit justification. Present engine inference as settled fact. Present Ness's response as a rewrite of history. Suppress conflicts. Store new interpretations. Decide what is true.

OBJECT TYPES USED. Roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, and **metadata-only** pre-ingest references. Held pre-ingest raw content must not influence Computed View ranking, interpretation, or output unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be surfaced. All objects are linked, never copied.

SEVEN-FACTOR PRIORITY ORDER (explicit, no hidden truth score):
1. Ness's explicit current judgment, when relevant.
2. Strength and directness of supporting root evidence.
3. Acceptance status and grounding quality of readings.
4. Relevance to the current question or view purpose.
5. Context quality and retrieval provenance.
6. Active clashes, unresolved uncertainty, and contrary evidence — surfaced beside the item, not suppressed.
7. Recency as a limited tie-breaker only. Never as authority.

Every surfaced item must state why it was prioritized. No single hidden score may collapse evidence, interpretation, judgment, and uncertainty into one number. Direct root support outranks repetition, frequency, or model confidence. A highly supported item with an active clash must display the clash beside it. The view must be able to say "no clear current view" when support is too conflicted or weak.

DECLARED ORDERING PROFILES. Different view purposes may use different profiles — current situation, person-focused, project-focused, historical review, or others. Each profile discloses its ordering rules. Alternatives and full provenance remain accessible from any profile.

UPDATE TIMING. Triggered updates, not continuous recomputation. Three update triggers: (1) Ness opens the view; (2) Ness manually requests a refresh; (3) a materially relevant event occurs — new accepted reading, new or changed active clash, Ness response event, confirmed theme or identity resolution, or another event explicitly defined as relevant to that view profile. Unrelated new material does not force every Computed View to recalculate.

Every completed update creates a new immutable snapshot. Previous snapshots remain accessible and never overwritten. Every snapshot records: update trigger, view profile, source objects used, derivation-rule version, timestamp, what changed from the previous snapshot, and why it changed. Normal interface shows the newest valid snapshot. If an update fails, the last valid snapshot remains visible, clearly marked as possibly stale. Failure is never silently treated as a successful refresh. The view may state that nothing materially changed — a null update is a valid outcome.

Exact relevance rules, significance thresholds, refresh scheduling, and snapshot schema remain undesigned.

---

## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT]

PERMISSION-CONTROLLED HYBRID. N.H surfaces possible actions when asked or when an explicitly authorized relevance rule applies. Never instructions. Never decisions. Ness remains sole decision-maker.

TWO SURFACING MODES. (1) On explicit request from Ness — always permitted. (2) Proactive — permitted only when an explicitly authorized relevance rule says the possibility is useful enough to show. Controllable by Ness's settings. May be disabled entirely.

Every surfaced possibility is labeled as derived, not instructed. Required language: "one possible option," "this may be reachable," "you could consider." Prohibited language: "you should," "you need to," "you must."

Every possibility records: the state, open loop, value, constraint, or evidence it was derived from; why it may be reachable now; important assumptions; uncertainty; possible limitations or risks.

Ness may: accept, reject, modify, postpone, ignore, or ask for alternatives. All responses are valid. Ignoring or rejecting a suggestion is never treated as failure, resistance, or evidence against Ness. No repeated surfacing of the same suggestion without a new request, materially changed evidence, or another explicitly authorized trigger.

Weak, conflicted, stale, or insufficient evidence: N.H either withholds the suggestion or labels it clearly as uncertain. Higher-impact actions require stronger permission and review rules than small reversible actions. The four risk levels are defined in §7P; what remains undesigned is the mapping of specific action categories to those levels, category-specific evidence and permission thresholds, and interface wording.

A surfaced possibility is not an action record until Ness chooses or performs something. The suggestion and any later real action remain separate linked objects.

NESS-RESPONSE STATES FOR SURFACED POSSIBILITIES (before or instead of execution):

- **Accepted and acted on** — Ness confirms and performs or authorizes the action. A new action record is created. The possibility and action record are linked but remain separate objects.
- **Rejected** — recorded as a rejection event pointing to the possibility. Not treated as failure, resistance, or evidence against Ness. The possibility is not resurfaced without a new trigger.
- **Modified** — Ness changes the scope, target, or form of the suggestion before acting. The modification is recorded. The modified version becomes the basis for the action record, not the original suggestion.
- **Postponed** — recorded with a reason if given. The possibility remains eligible for resurfacing only when a new trigger or request occurs. Time alone does not resurface it.
- **Ignored** — no response event required. The possibility is not resurfaced without a new trigger.
- **Alternative requested** — Ness asks for different options. A new surfacing pass is initiated. Prior suggestions remain in record but are not repeated in the new pass.

Exact relevance triggers, mapping of specific action categories to the four risk levels, category-specific evidence and permission thresholds, and interface wording remain undesigned.

---

## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO RESULT TYPES, KEPT SEPARATE. Neither grants direct system access to reality.

EXPLICIT REPORTED RESULT. Ness directly reports what happened through a normal front door. Enters catalog and ingestion as normal — becomes a root only after standard checks. Labeled as Ness's report of the result. Not direct system observation of reality.

DETECTED POSSIBLE RESULT. N.H notices incoming material that may relate to an earlier action. Creates a proposal linking new material to the action. Never silently declares the material is the action's result.

Every possible-result proposal records: action ID, new root or capture ID, why they may be connected, timing, uncertainty, alternative explanations, who or what detected the connection.

Ness may: confirm, reject, modify, or leave the proposed connection unresolved indefinitely.

CAUSATION RULES. Timing alone does not prove causation. Similarity alone does not prove an observed event resulted from the action. Confirmation of a result connection does not automatically confirm why it happened.

THREE SEPARATE LINKED OBJECTS. Action record, result root, connection between them. Never merged.

N.H must distinguish: (1) the observed or reported event; (2) the claim that it resulted from the action; (3) interpretations of what that result means.

A confirmed result connection may trigger: reread, state update, open-loop update, or another explicitly designed process. Automatic detection may be disabled or restricted by Ness.

SIX RESULT STATES:

- **Success** — the action may have produced the expected or intended effect. Success may be recorded as confirmed when Ness confirms it. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with the intended effect, but this remains a revisable interpretation and does not establish causation. The observed event, the inferred relationship to the action, and Ness's confirmation or judgment remain separately represented.
- **Partial success** — may be recorded as confirmed when Ness confirms that some but not all intended effects occurred. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with partial success, but this remains a revisable interpretation and does not establish causation. The record describes what appears achieved and what appears unmet while keeping the observed outcome, the proposed relationship to the action, and Ness's judgment separately represented. Does not automatically trigger a retry.
- **Failure** — may be recorded as confirmed when Ness judges that the intended effect did not occur or that the result was negative. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with failure, but this remains a revisable interpretation and does not establish causation. The observed outcome, the proposed relationship to the action, and Ness's judgment remain separately represented. Does not automatically trigger a retry or a new surfaced suggestion. Ness decides what to do next.
- **Cancellation** — the action was authorized but stopped before completion, either by Ness, by a pre-authorized emergency stop, or by a system condition. The cancellation is recorded with its trigger, reason, and the state of the action at the point of cancellation. Partially completed effects are recorded separately from intended effects.
- **No result or unknown result** — the action was taken but no observable result has arrived or can be confirmed. Recorded as result-unknown. Any open loop or state node remains active and marked with uncertainty. The system does not assume success or failure. Time passing alone does not resolve this.
- **Incorrect or disputed result linkage** — a proposed connection between a result and an action is found to be wrong, contested by Ness, or contradicted by later evidence. The incorrect linkage is recorded as a rejected connection event. The action record and result root remain as separate objects. A corrected linkage may be proposed. The original action record is never rewritten to remove the disputed connection — the dispute is recorded alongside it.

Exact detection rules, confirmation workflow, classification criteria and subcategories within the six result states, and downstream triggers remain undesigned.

---

## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The formal boundary between N.H as a helper and N.H as an actor in the world. Defines what N.H may do on its own, what it must prepare and show before doing, what it must ask Ness before doing, and what it may never do regardless of any instruction.

MUST NEVER ALLOW. N.H acting on the world without recorded authorization. Silence, absence, or non-response interpreted as consent to act. A permission granted for one action being silently extended to a different action. Past permission automatically remaining valid for future similar actions. N.H proceeding when its authority level is unclear. Preview being skipped for actions requiring approval. An irreversible action taken on the basis of reversible-action authorization. Cascading permissions. N.H deciding what counts as a successful result of an action it took.

THREE ACTION STATES WITH DISTINCT AUTHORITY REQUIREMENTS.

**Suggesting** — N.H surfaces a possibility for Ness to consider. No external effect, external write, or execution occurs. Authorized Level 1 internal read-only retrieval may occur to derive the possibility, but no message is sent, no external account or system is changed, and no executable action is staged. Lowest authority level; always permitted within action-surfacing rules.

**Preparing** — N.H assembles something ready to act but not yet acted. A draft exists but has not been sent. A change is staged but not saved. The prepared object is real and inspectable but no external effect has occurred. Ness reviews before anything is committed. Requires higher authority than suggesting. Must be shown to Ness before execution.

**Executing** — N.H takes an action with real-world effect. Something irreversible may have occurred. Requires the highest authority level, explicit prior approval for the specific action, and a complete record of what was done. The boundary between preparing and executing is: has anything outside N.H changed? If yes, execution has occurred.

FOUR RISK LEVELS.

**Level 1 — Internal read-only.** N.H accesses its own stores, indexes, and records. No external effect. No change to any object. Autonomous within normal operating parameters.

**Level 2 — Internal write.** N.H writes a new reading, appends a new state node, state-version, or currentness event, creates a clash record, or produces another derived object inside its own stores. Existing state nodes and other historical records are not modified in place. Append-only operations at this level are lower risk than modifying existing objects. Autonomous within established schema and validation rules for normal append operations; flagged for any exceptional operation that would alter an existing record.

**Level 3 — Prepared external action.** N.H drafts, stages, or assembles something intended to have external effect. The prepared object is shown to Ness before anything is committed. Ness must explicitly approve before execution. Silence is not approval.

**Level 4 — Executed external action.** N.H takes an action with real-world effect. Requires explicit prior approval for the specific action, a pre-execution preview, and a post-execution record. Irreversible actions require additional confirmation. Actions in heightened-risk categories require their own special boundary rules regardless of whether they appear small or reversible.

TWO AUTHORITY LAYERS.

**Layer 1 — Standing permissions.** General abilities Ness enables or disables. May authorize: Level 1 internal read-only, normal validated Level 2 append-only internal actions, Level 3 preparation within clearly defined boundaries. Cannot silently authorize broad categories of external execution.

**Layer 2 — Moment-level approval.** Permission for one specific action at one specific moment. Required for Level 4 external execution after Ness sees the exact action preview. Preparing something does not authorize executing it.

RECURRING EXECUTION AUTHORIZATION. Ness may create a narrowly scoped recurring authorization, but it must explicitly define: exact action type, destination or recipient, frequency or trigger, content or value limits, permitted tools, start and expiry conditions, audit and notification requirements, and how it can be paused or revoked. It is its own recorded authority object — not inferred from general settings or past approvals. Actions outside its exact scope require new approval.

ABSOLUTE BOUNDARY — ALWAYS REQUIRES SPECIFIC PER-INSTANCE CONFIRMATION REGARDLESS OF STANDING PERMISSIONS. Medical, legal, financial, privacy-sensitive, relationship-affecting, destructive, or irreversible actions.

STOP CONDITIONS. Changed conditions, ambiguity, expired permission, or unexpected output require N.H to stop and seek reconfirmation before proceeding. Silence is never approval. In any layer, at any level.

AUTHORITY VIOLATION AND CORRECTION RULE.

Stop-and-surface is the default. On detecting a violation or unexpected result, N.H must immediately: stop all related autonomous action; prevent any further steps in the same action chain; record the full event (what was intended, what actually happened, the authority N.H believed it had, where the boundary was crossed, what unexpected result occurred, what is known/unknown/still changing, which tools and external systems were involved); surface the event clearly to Ness without minimizing, hiding, or reframing it; present possible corrective actions separately as proposals.

Ness's approval required before: reversal, compensation, follow-up communication, deletion, restoration, or any other real-world corrective action.

Corrective action is a new action with its own risk level, preview, permission requirement, execution record, and possible consequences. It is never automatically authorized by the fact that it is corrective.

N.H must never assume that reversal restores the original state completely. N.H must never mark the incident resolved merely because a reversal attempt succeeded technically.

FIVE SEPARATE LINKED OBJECTS. Original action, violation record, corrective proposal, approved correction, observed result. Never merged.

NARROW PRE-AUTHORIZED EMERGENCY STOP EXCEPTION. Permitted only when all five conditions are met simultaneously: (1) the original action is still actively in progress; (2) stopping prevents additional effects rather than undoing completed effects; (3) the stop mechanism is mechanically bounded and previously authorized; (4) stopping cannot reasonably create a larger consequence than continuing; (5) the emergency stop and its authority basis are immediately recorded and surfaced to Ness.

This exception explicitly does not permit: recalling or deleting a completed message, restoring or modifying external data, sending an apology or explanation, making a compensating payment, contacting another person, or any other completed-world reversal without Ness's approval.

Exact permission categories, authorization object schema, and interface remain undesigned.

---

## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT GOVERNS. What N.H may capture, how it classifies and protects sensitive material, who and what may access it under what conditions, what appears in views and chat, and what happens to material when Ness removes, restricts, or deletes it. Operates at every stage: before capture, during storage, during retrieval and display, and during deletion.

MUST NEVER ALLOW. Capturing material that was explicitly excluded at the front door. Storing credentials or secrets in plain recoverable form anywhere. Surfacing sensitive material merely because it is relevant. Retaining deleted material through any indirect path. Allowing derived objects to preserve the content of deleted roots after deletion is confirmed. Treating a deletion marker as equivalent to actual deletion. Displaying another person's sensitive information without an explicitly designed rule authorizing it. Permission to store being silently extended to permission to analyze, simulate, display, or share. Partial deletion claimed as complete. N.H confirming deletion when it cannot verify that deletion was carried out in all relevant locations.

FIVE OPERATIONS — DISTINCT, NOT INTERCHANGEABLE.

**Exclusion** — material never enters N.H at all. Filtered at the front door before capture. Cleanest boundary because there is nothing to manage afterward.

**Hiding** — material exists in the store but is not displayed in normal views or surfaced in retrieval. A presentation rule, not a data operation. Reversible without data recovery.

**Restriction** — material exists and may be physically present, but access is limited by explicit rules. More granular than hiding, more targeted than deletion.

**Redaction** — specific content within a root or derived object is removed or obscured while the containing record remains. The sensitive portion is removed and replaced with a tombstone or placeholder. Must propagate to derived objects that contained the redacted content.

**Deletion** — the root and all material derived from it are removed from every location. A tombstone record may remain to preserve that something was deleted, when, and by what authority — without preserving the deleted content. Deletion is the strongest operation and the hardest to verify as complete.

FOUR SENSITIVITY LEVELS.

**Level 1 — General personal.** Everyday conversation, preferences, projects, general life events. Standard N.H privacy rules apply.

**Level 2 — Sensitive personal.** Health information, financial details, relationship difficulties, emotional material, and things Ness has explicitly marked as private. For Ness's authenticated private use, this material is eligible by default unless Ness explicitly restricted or hid it, it was excluded/redacted/deleted, an unresolved deletion case applies, it contains non-negotiably excluded secrets, or another explicit compartment rule applies. External exposure, shared screens, exports, tool use, notifications, and secondary uses require explicit authorization under the two-stage access-control rules below.

**Level 3 — Third-party and relationship data.** Information about other people. Requires separate rules from Ness's own data because other people did not consent to being in N.H.

**Level 4 — Credentials, secrets, and high-harm material.** Authentication material, passwords, keys, financial credentials. Must never enter normal stores. If encountered at capture, must be excluded or immediately isolated.

DELETION AS BLOCKING, VERIFICATION-BASED OPERATION. N.H may confirm complete deletion only when every known location has been removed or verified clean.

A deletion request creates a deletion case with a complete dependency and location search. N.H must identify and check: the original root, direct readings, story tellings, state nodes, clash records, Computed View snapshots, Person-Box links, indexes, embeddings, caches, temporary processing files, exports, backups, model-context records, and any other known derivative or storage location. Indirect traces must also be searched: quotations, paraphrases, summaries, semantic representations, inferred states grounded partly in the root, copied text without a preserved source link.

Every identified derivative must be deleted, redacted, rebuilt without the deleted source, or explicitly marked unresolved if safe removal cannot yet be verified. Multi-root derived objects may be recomputed without the deleted root only if the deleted content is no longer recoverable from them, their meaning is re-evaluated without that evidence, and their provenance records that they were rebuilt. Embeddings and indexes derived from deleted content must be removed and rebuilt where necessary. Backups follow an explicit deletion or expiry process.

FIVE DELETION OUTCOMES.
- `verified_complete` — every known location and derivative removed or safely rebuilt and verified. The only outcome that may be described as complete deletion.
- `completed_with_declared_limits` — removed from all controllable locations; one or more locations cannot be fully verified.
- `incomplete` — one or more identified traces remain.
- `blocked` — deletion cannot safely proceed yet.
- `failed` — an attempted deletion operation failed.

For every outcome other than `verified_complete`, Ness must be told plainly: what was removed, what remains, what could not be checked, why, whether the remaining trace is accessible or usable, and what further action may be possible. N.H must never confirm deletion merely because the root record is gone. N.H must never hide uncertainty behind the phrase "best effort."

A content-free tombstone may remain containing only: deleted object identifier, deletion time, deletion authority, deletion outcome, verification record. No deleted content, no reconstructive metadata.

While a deletion case remains unresolved: affected material must be immediately prevented from retrieval, display, analysis, simulation, or use in new derivations.

CAPTURE EXCLUSION — TWO-LAYER SYSTEM.

**Layer A — Non-negotiable core.** Narrow by design. Covers material that could directly grant access or cause immediate serious harm if stored: passwords, private cryptographic keys, authentication tokens, recovery codes, one-time security codes, payment-card security codes, and equivalent live access credentials. Must never enter root stores, readings, indexes, embeddings, caches, logs, model context retained by N.H, or normal backups. Cannot be disabled by Ness for normal N.H memory stores. A dedicated secrets vault, if ever built, is a separate system with separate authority, encryption, access, and deletion rules.

**Layer B — Ness-configured exclusions.** Rules Ness controls and can extend, narrow, pause, or remove. May be based on: content category, person, source, date range, front door, project, sensitivity, or intended use. May specify that material should be fully excluded, held for review, entered only after confirmation, entered with specified parts redacted, or entered under immediate restriction. Sensitive but context-dependent material — medical details, childhood memories, third-party information, relationship material, emotional disclosures — must not be placed in the non-negotiable core merely because it is sensitive. These require explicit handling rules but are not automatically excluded in every context.

Mixed-content capture: when one input contains both permitted and excluded material, N.H must isolate and remove the excluded portion, preserve the permitted portion when safe, record that exclusion occurred without recording the excluded content, and tell Ness what category of material was removed. If safe separation is not possible, the entire capture is held before ingestion and Ness is asked what to do. Ambiguous suspected secrets enter a protected pre-ingest hold, not normal memory, until classified. Exclusion happens as early as technically possible at every front door. Exclusion event records may retain only non-reconstructive metadata: time, front door, exclusion category, rule used, outcome. Never the excluded content itself.

THIRD-PARTY DATA RULES.

Universal minimum baseline — applies to every person other than Ness without exception: preserves source and speaker of third-party material; distinguishes the person's actual words or actions from Ness's interpretation and N.H's interpretation; does not present inferred feelings, intentions, diagnoses, motives, or private states as facts; does not share third-party material externally without Ness's specific authorization; does not use third-party material merely because it is relevant; does not silently expand one piece of information into a fixed profile of the person.

Context-sensitive rules above the baseline may vary based on: relationship to Ness, amount and frequency of data, sensitivity, source and front door, whether the person spoke directly or was described by someone else, whether content was private/public/forwarded/recorded/inferred, age or vulnerability, and intended use. Relationship closeness does not reduce protection automatically. A close family member appearing frequently may require stronger safeguards because more material exists.

Ness may configure person-specific or group-specific rules covering permitted storage, retrieval, display, analysis, simulation, retention, redaction, restriction, or exclusion. Configuration may make protections stricter. It may not remove the universal baseline.

Four separate operations with increasingly stronger privacy requirements: (1) understanding Ness's experience of another person; (2) recording what that person actually said or did; (3) interpreting what the person may have meant; (4) constructing a model of the person. N.H may normally perform the first. Each subsequent operation requires stronger authorization.

Third-party simulations must never be presented as the real person. Always labeled as bounded hypothetical models derived from limited material, with uncertainty and missing information visible. Minors and highly vulnerable people receive stronger default restriction. Large-volume imported third-party data does not become fully usable merely because it was imported. Public availability does not automatically authorize unrestricted storage, combination, profiling, or simulation.

TWO-STAGE OUTPUT ACCESS CONTROL.

★ CENTRAL RULE. Private access for Ness is open by default unless Ness explicitly restricts it. External exposure and secondary uses are restricted by default.

★ N.H may use material when the current purpose is authorized by Ness. It blocks material from unauthorized uses, not from Ness's own understanding by default.

**Layer 1 — Pre-retrieval eligibility control.** Before material becomes a retrieval candidate, N.H checks whether it is eligible for the current operation and purpose. For Ness's authenticated private use, material is eligible by default. N.H does not remove material from Ness's private self-understanding merely because it is sensitive, emotional, medical, traumatic, sexual, relationship-related, controversial, or uncomfortable. Third-party involvement does not automatically block Ness from understanding his own experiences. "Sensitive" alone is never a sufficient reason to withhold information from Ness. Material is blocked from Ness's private use only when: Ness explicitly restricted or hid it; it was excluded, redacted, or deleted; a deletion case remains unresolved; it contains live credentials or non-negotiably excluded secrets; a specific compartment rule applies; or another explicit rule chosen by Ness applies. For other purposes — external sharing, tool use, exports, secondary analysis, notifications, shared screens — eligibility is restricted by default and requires explicit authorization. Ineligible material must not be ranked, semantically compared, selected, passed to the mouth, used for simulation, or allowed to influence the response indirectly. Privacy filtering happens before semantic ranking so restricted material cannot influence selection even indirectly.

**Layer 2 — Pre-output privacy review.** After authorized material is retrieved and a response, view, suggestion, or derived output is formed, N.H reviews the final result before showing it. The output review is not a general content-safety or emotional-sanitization filter. It checks specifically for: accidental exposure outside the authorized private context; deleted or restricted content appearing in output; live secrets or non-negotiably excluded material; unauthorized secondary uses; unintended third-party profiling beyond the current authorized purpose; external sharing, notifications, tool outputs, or exports carrying private material; disclosure through shared screens or other unintended channels; several permitted pieces combining into a disclosure that exceeds the authorized purpose; generated language revealing more than the authorized sources themselves support. N.H must not soften, omit, or replace truthful relevant material merely because it may be upsetting to Ness.

MODEL-PROVIDER LIMITATIONS ARE RECORDED SEPARATELY. Any refusal or limitation from the mouth model — such as a Claude refusal — is recorded as a mouth limitation. It is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false. The material remains in the store under its existing rules. The limitation is attributed to the borrowed mouth, not to N.H's privacy system.

When permissions are ambiguous, outdated, unavailable, or conflicting for a non-private-Ness purpose — access defaults to withheld.

On output failure: withhold affected content for the unauthorized purpose, produce a safer version when possible, state plainly that material was withheld and why. Components receive only the minimum material needed for their authorized task. A component must not receive sensitive content merely so it can later decide not to display it.

Privacy checks apply to: chat, Computed View, Story Layer, Person-Boxes, Living State Web, memory browsing, search results, simulations, proactive suggestions, notifications, exports, tool use, and external sharing.

Every privacy decision records: operation requested, purpose, material considered, applicable privacy rule, authorization basis, eligibility decision, output-review result, and any withholding or transformation performed.

Remaining undesigned: exact eligibility rules, purpose categories, privacy-policy evaluation order, safe-transformation rules, interface behavior, core exclusion detection methods, mixed-content separation process, backup deletion/expiry mechanics, derivative-discovery methods, cryptographic erasure mechanisms, verification procedures, person-specific control interface, minor-data specific rules, volume thresholds for large imports, simulation permission specifics.

---
