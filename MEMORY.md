# Memory and meaning

See SYSTEM.md for scope and owners.

## Capture and roots

- One intake path serves text, chat, imports, images, audio, observations, research, and selected simulation material. Source type grants no bypass.
- Capture is not ingestion. Preserve the original payload and source metadata. Never guess a missing speaker or thread.
- The intake envelope carries stable capture identity, source type, immutable payload or reference, capture time, speaker/thread information when known, and source metadata. Keep reliable source values separate from mechanical normalization and proposed inferences.
- Live unresolved attribution may prompt Ness. Unattended unresolved attribution holds the item. Never write `role = "unknown"`.
- The investigated fallback speaker detector proposes only. Its recipe combines MiniLM embeddings, standardized `rel_length`, `no_uppercase`, `no_end_punct`, `starts_lowercase`, and `has_code`, then Logistic Regression with `C=0.1`. Its historical five-fold result is not deployment or identity authority.
- A real thread identifier stays unchanged. Use a nonsemantic session placeholder only for provably grouped untitled material, or a unique singleton placeholder. Never substitute a topic summary for grouping evidence.
- Held items may wait indefinitely. One blocked item does not block unrelated eligible items. Capture errors remain explicit rather than silently discarded.
- Held raw content cannot support ordinary readings, Person-Box interpretation, ranking, or output. Safe metadata references must not reconstruct the content. Sealed TSC inspection is prohibited.
- Catalog lifecycle states are `held`, `ready`, `promoting`, `promoted`, `rejected`, `excluded`, and `error`. These are distinct from TSC session/item states.

Root v1 has exactly seven fields:

`id`, `subject`, `timestamp`, `content`, `re_reads`, `source_title`, `role`.

`id` is UUID4. `subject` is an import-batch tag, never a semantic topic. `timestamp` is record creation time. A root has `re_reads = []`. `source_title` is required and may be null where allowed by the existing schema. Carry `role` from the source. Do not retrofit new fields or mutate sealed `re_reads`.

The original sealed 5,521-root batch stays closed. Future writes use the shared B11 active-batch boundary, never direct file writes or fallback into a sealed batch. Serialize target selection, identity, ownership, append, sealing, and rotation. Prevent duplicate captures globally across epochs. Schema changes cannot manufacture another root for the same capture.

Future schema proposals preserve separate source Origins, source/import/record-creation times, thread identity, and append-only aliases and relationships. Keep mixed-media source items distinct and connected. Do not silently activate proposed fields on v1 roots.

## Readings

Reading v1 has exactly twelve fields:

`id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`.

- `reads` references roots. `derived_from` references earlier readings. Do not copy root text into readings.
- `confidence` keeps `interpretation_confidence` and `source_reliability` separate. Both keys exist. Verify the permitted unavailable-source-reliability representation from the actual validator or adopted schema. Do not invent a sentinel.
- `story_layer` is a list, possibly empty. Omit unsupported optional fields instead of filling them with `"unknown"`.
- `mode` is open vocabulary with local `classification_confidence`, separate from reading confidence.
- `produced_by.origin` is `observed`, `imported`, `simulated`, `generated`, `reaction`, or `human_annotation`. Preserve model, engine, prompt, configuration, and version provenance.
- New records have `schema_version` and a stable `idempotency_key`. Repeated commitment returns or rejects the existing result rather than adding evidence.
- Show why through source pointers. Do not add a factual `why` or `reason` field to the reading. Separate acceptance and operation records may carry their own reasons.
- Shape validation checks fields and references. It does not certify meaning or reject honest uncertainty.
- Test writes go to `.nh_readings_quarantine.jsonl`. Production requires its separate marker, explicit proposed-change approval, valid promotion evidence, authorized writer, and current privacy/authority checks. Never create `.nh_readings_store.jsonl` or `.nh_readings_production_authorized` automatically.
- Bootstrap with raw roots and explicitly human-affirmed material. Prior machine readings are excluded by default or labeled low-trust auxiliary context. They never corroborate themselves.

## One reading pass

The webs work together in one pass. Segmentation and meaning classification happen together. Read against the widest usable accumulated context, and keep thin-context uncertainty explicit.

Thin-context readings default to low confidence and say so. Form and authorship stay separate: a character's despair inside a story is not automatically Ness's despair. More inferential readings must be easier to trace, challenge, suppress, and replace in the current view.

Peer webs are intent, deixis, common ground, implicature, theory of mind, time/sequence, rereading, and mode/register. Mode describes form rather than replacing intent. Whole-work form does not exempt individual sentences from other webs. Add a web only for a grounded dimension the existing set cannot express.

One declared pass produces one reading. Multiple angles require separate passes with their own inputs and provenance. Later synthesis adds a layer rather than rewriting earlier readings.

Acceptance checks shape, grounding, invention, channel separation, uncertainty, evidence consistency, and declared-mode compliance. Keep malformed/incomplete output, fabrication, unsupported certainty, channel confusion, and mode violations distinguishable.

- A rejected proposal is not a reading.
- Genuine `insufficient_context` is an honest, revisable reading when the source cannot support interpretation.
- A hold produces no reading. Use it only for a legitimate missing condition that can be tracked and verified. Keep hold state outside the source record and block new use from its enforcement commit. Never park a rejected draft until it appears fresh.
- Unfillable webs name their gap without forcing Ness to answer or stopping unrelated work.
- A hold requires both a specific missing condition and a realistic way to obtain it. Otherwise write an honest insufficient-context reading when appropriate. Release requires verified bound evidence for every active hold reason.
- Qualitative grounding labels are exactly `grounded_enough`, `partly_grounded`, `not_grounded_enough`, and `insufficient_context`. Governed assessment assigns them to exact revisions. No numeric companion, ranking score, producer self-review, or truth claim.

## Retrieval and relevance

Keep positional adjacency and semantic association as separate labeled channels. A mode may use neither, either, or both where its trigger permits. Healthy empty retrieval permits target-only work. Retrieval failure stays a failure, never invented context or silently relaxed thresholds.

Each versioned mode declares purpose, channel parameters, ceilings, uncertainty handling, and audit rules. Apply the lower of setting and ceiling and enforce the ceiling independently at runtime. Empirical retrieval values remain open until tested.

Relevance first applies categorical gates, then named graded dimensions. Preserve producer and provenance for each dimension. Do not collapse them into a hidden score.

- Use rules for reliable mechanical dimensions, embeddings for semantic proximity, and a specifically authorized model for necessary interpretation.
- Privacy and deletion eligibility are prerequisites, not relevance dimensions. A model-produced dimension cannot control a categorical gate.
- Evaluate on demand. Precompute only for an explicitly declared latency-sensitive context. No permanent global relevance state.
- Tier 1 belongs to relevance control. Tier 2 belongs to the consumer. Each validates its own contract.
- A mode change needs preview and confirmation. Per-judgment corrections and scoped overrides append directly without rewriting earlier judgments.
- Unknown purpose types halt evaluation and preserve the request. Offer an explicit mapping or versioned addition, never guess.
- Relevance events may prompt state review. They cannot establish state currentness, certainty, causation, permission, or truth.

Shared gates are `same_thread_or_group`, `precedes_target_in_same_thread`, `within_declared_time_range`, and `object_type_matches`. Shared dimensions are `semantic_similarity`, `temporal_distance`, `positional_distance`, `currentness_status`, `explicit_links`, `ness_response_links`, `proposal_acceptance_outcome`, `reading_context_status`, and `active_clash_links`.

Controlled purposes are `retrieval_context_selection`, `view_assembly`, `action_surfacing`, `reread_trigger_evaluation`, and `state_review_trigger_evaluation`. An explanatory label adds no behavior. The five accepted consumer declarations use on-demand evaluation, no precomputation, and no model-produced dimensions unless explicitly changed through the governed path.

## Rereading and retries

Rereading adds a new reading and preserves every earlier one. Triggers are manual, materially relevant changed conditions, or a bounded scheduled retry for temporary technical conditions. Time passing alone never warrants reinterpretation.

- Manual rereading needs no new evidence or justification. Do not manufacture a semantic reason or gate it on relevance.
- Semantic assignments are direct, wider-context, or both when their distinct relationships apply. They are not mutually exclusive and do not replace trigger evidence.
- B10 gives each root/trigger one canonical claim and at most one new quarantine reading. Use separate caller, child, and attempt identities. Do not reuse new-root enqueue keys.
- Commit trigger, claim, inputs, reading, telling completion where required, and final outcome before acknowledging completion. Recover from committed sources, never rebuilt indexes alone.
- Retry completes the same operation. It never reinterprets a completed reading, bypasses a hold, renews authority, or repeats an uncertain outside effect.

Accepted technical budgets:

| Context | Total attempts | Minimum gaps | Episode deadline |
|---|---:|---|---|
| Live | 3 | 10 seconds, then 30 seconds | 7 minutes |
| Background | 3 | 1 minute, then 3 minutes | 15 minutes |

The original execution counts as attempt one. Deadlines start at the episode's first durable failure. Both time and attempt gates apply. Do not cancel an in-flight attempt merely because its retry-admission deadline passes.

Substantive rejection permits one careful retry within the same deadline, without a scheduled gap. Another rejection is terminal for that episode. Eligible B24 insufficiency assessment opens only after that retry is consumed and rejected, never from authorization failure, holds, staleness, or indeterminate effects.

A later episode needs recorded real change and one-time consumption of that change evidence. Permanent attempt numbers never reset. Episode ordinals restart within the same canonical operation only when inputs remain unchanged. Changed inputs require a new linked operation. Time and repetition alone are not real change.

## Story, people, and clashes

Tellings stay local, source-grounded, and perspective-specific. Separate root producer, subject, viewpoint owner, direct self-report, quotation, reported speech, observation, and inference. Retain supported nested attribution; leave unsupported attribution unresolved.

Optional telling elements are whose, stance, firmness, telling, theme, and when. Read absence only where the information was expected, could have been observed, and its absence matters to the question. Any interpretation of absence stays weak and revisable.

The Story Layer owns immutable telling cards. Consumers reference them. Persist the preparation before the reading, the reading before its cards, and valid set completion before semantic telling use. Partial cards and recovery material are not canonical evidence.

Firmness describes supported stance, never truth or inner access. Labels are `high_firmness`, `moderate_firmness`, `low_firmness`, `mixed_firmness`, and `uncertain_firmness`. `omitted_no_support` means omit the unsupported field. Use qualitative evidence, never hidden arithmetic. Firmness does not trigger or release holds.

Themes combine stable organization and provisional engine proposals. A telling may belong to several themes or none. Proposals can remain unconfirmed indefinitely and cannot silently influence later readings as adopted themes.

Person-Boxes gather references. They are not profiles, diagnoses, summaries, scores, or fixed identities.

- Search before proposing. Link clear mentions automatically and join definitely identical records. Keep uncertain anchors and joins pending. Name similarity alone is insufficient.
- Ness has a confirmed Person-Box. Clear authored and source-resolved first-person material links automatically. First-person text inside a pasted third-party source does not.
- Preserve link basis, certainty, authority, time, batch, and correction history. Never merge source contents across batches.
- Holding links Ness's understanding, original evidence, other perspectives, and revisable readings as separate objects. It creates no second profile or memory store.
- Keep each person's permissions separate. A link grants no disclosure right. Generic connections cannot establish identity or merge people.

The seven Person-Box sections are roots, readings, story tellings, clashes, Ness responses, themes, and unresolved identity. Filters may combine time, perspective/role, theme, source/thread, and lifecycle/confirmation. Clearing filters restores the default; full chronology remains one switch away.

Clash types are direct contradiction, interpretive divergence, temporal change, perspectival difference, evidence insufficiency, and context mismatch. Compare the same person, conditions, time, and context. Record whether both statements could be true without selecting a winner.

Deduplicate clashes by identity. Later detections and Ness responses append linked events. Keep active conflict beside affected items in retrieval, views, state support, and suggestions. A response or new reading does not erase the original clash. Do not provide a misleading resolve action.

## Views and state

- Always retain current and historical views. Ordering is presentation, never a truth verdict.
- Person-Box sections open as compact lists with evidential status and expandable chains. Keep unusable items labeled, clashes adjacent, and original chronology reachable. No synthesized personality strip or per-person score.
- Computed View derives an inspectable current picture with disclosed ordering. It neither writes new interpretations nor supplies upstream evidence. Use it quietly for responses; show the internal picture when Ness asks.
- Its fixed factor order is current Ness judgment, direct root evidence, reading acceptance/grounding, purpose relevance, context quality/provenance, clashes/uncertainty, then recency as a tie-breaker. Preserve separate factor outcomes and explain priorities. No aggregate truth score.
- Refresh only on applicable triggers. Commit immutable snapshots and separate refresh-status events. Failed, incomplete, and no-change refreshes do not create falsely fresh snapshots. Never mark an old snapshot in place.
- Living State has no reader of its own. It consumes permitted evidence and readings. Keep state existence separate from present currentness.
- Preserve brief or weak signs as evidence. Full-node creation requires materiality. Each time-bounded episode has its own identity. Later recurrence creates a new episode.
- Separate experienced states, causes, positions, open loops, relationships, values, constraints, capacity dimensions, transitions, causal hypotheses, and counterfactuals.
- Multiple positions may coexist. Do not average them into a false middle or label complexity a disorder.
- Currentness changes append dated evidence-linked events. Time alone does not end a state. Relevance can initiate review, never decide its result.
- Ground every causal-chain link. Timing, similarity, coherent storytelling, and a confirmed result connection do not prove causation.
- Internal counterfactuals may support comparison automatically. Visible or immersive simulations require their separate permission. Imagined scenes are not observed reality.
- Keep the world model's active core separate from wider general knowledge. Preserve attribution, uncertainty, world membership, and currentness. Visual manipulation cannot rewrite evidence.

Currentness labels are `current`, `possibly_current`, `stale`, `currentness_unknown`, `ended_by_evidence`, and `superseded_by_evidence`. Capacity keeps thinking, emotional, bodily, practical, and decision-making dimensions separate; an optional supported summary identifies its contributing dimensions.

Read-only memory-health checks look for missing sources, excessive older-reading dependence, one lineage masquerading as independent repetition, thin Person-Box support, confidence without independent roots, and hidden contradictions. Checks never repair or rewrite inspected records themselves.

## Connections and creations

Connections require a direct recorded relationship, Ness's explicit statement/confirmation, or a narrow authorized rule. Similarity, timing, shared themes, interpretation, and co-retrieval cannot create accepted relationships by themselves.

- Keep endpoints, relationship type/direction, certainty, decision status, authority, and history separate.
- Pending connections may guide investigation silently. They cannot support claims, recommendations, identity effects, or actions. They never age into acceptance.
- Acceptance atomically commits the connection and its authority evidence after duplicate checking. Competing routes converge on one relationship.
- Before each use, resolve exact accepted version, later correction/dispute/supersession, integrity, authority, current-use state, certainty, privacy, and influence restrictions. An old accepted record is insufficient.
- Rejection suppresses repeat surfacing. Genuine new evidence permits a new linked proposal, not reversal of the earlier decision.

The Unified Creation Store holds root-referencing records for `design`, `idea`, `rule`, `name`, and `decision`. A record may have several types. Projects and categories are views, not separate databases.

- Detect source-grounded fragments broadly and provisionally. Each immutable base starts `provisional` with identity, type set, provenance, schema version, and detector reference where applicable.
- Later confirmation, correction, supersession, and grouping are append-only events. Do not change the original status field.
- Confirmation requires explicit Ness confirmation or later clear words/actions demonstrating adoption. Ambiguity, time, retrieval, repetition, and model confidence never confirm.
- Wider provisional use must retain status and a trace. Larger works reference every original fragment rather than fusing them.
- Affirmation records an actual response to specific readings. It does not alter their truth, confidence, evidence, or firmness. Rejection does not prove the opposite. Silence changes nothing.
