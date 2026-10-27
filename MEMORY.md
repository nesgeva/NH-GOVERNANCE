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

`id` is UUID4. `subject` is an import-batch tag, never a semantic topic. `timestamp` is ISO 8601 record creation time. A root has `re_reads = []`. `source_title` is required and may be null where allowed by the existing schema. Carry `role` from the source. Do not retrofit new fields or mutate sealed `re_reads`.

The original sealed 5,521-root batch stays closed. Future writes use the shared B11 active-batch boundary, never direct file writes or fallback into a sealed batch. Serialize target selection, identity, ownership, append, sealing, and rotation. Prevent duplicate captures globally across epochs. Schema changes cannot manufacture another root for the same capture.

Batch identity is separate from location. A global capture claim permanently reserves one root ID, including after cancellation. Old sealed roots need verified ID coverage, not fabricated capture IDs. New admissions require the current active selection. A reservation admitted before cutoff may finish into its exact predecessor while sealing; unresolved reservations prevent sealing. Rotation prepares the successor, atomically selects it and cuts off the predecessor, then drains and seals. Equally valid selection forks stop writes; time and lexical order cannot choose a winner.

Cancellation and commit fencing compete atomically. A fenced claim needs exclusive recovery authority, proof the old writer cannot run, exact target lookup and conclusive non-commit before release. Commit the parent terminal log before acknowledgment. Index registration is repairable afterward; complete/partial/stale/missing/conflicting index coverage is separate from root commitment.

Future schema proposals preserve separate source Origins, source/import/record-creation times, thread identity, and append-only aliases and relationships. Keep mixed-media source items distinct and connected. Do not silently activate proposed fields on v1 roots.

The accepted next-schema design separates `thread_id` from `display_label`. Typed `source_times` distinguish created, captured, sent, recorded and occurred, with source provenance, reliability and timezone state. Zero reliable source times is valid; select at most one reliable main real-life date. Keep `imported_at` and `record_created_at` separate. Mixed-media relationships commit only after both exact Origins exist.

Aliases affect presentation and explicitly label-based filtering only. They never change thread membership. Compare-and-append one predecessor-bound alias chain; conflict or unverifiable history falls back to the sealed original. Live-conversation provenance asserts origin and source-known speakers, not meaning. Its designed structured label is `live_conversation/v1`, not the older illustrative string. Failed earlier-reference detection proceeds without reference context.

Keep original media type and provenance. Mechanical normalization records its method/version beside the untouched source. An optional hash over `reads`, `meaning`, `produced_by` and `schema_version` can check integrity or exact duplicates. It neither replaces operation identity nor adds a field to reading v1.

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
- Test writes go to `.nh_readings_quarantine.jsonl`. Production requires its separate marker, explicit proposed-change approval, valid promotion evidence, authorized writer, and current privacy/authority checks. Never create `.nh_readings_store.jsonl` or `.nh_readings_production_authorized` automatically.
- Bootstrap with raw roots and explicitly human-affirmed material. Prior machine readings are excluded by default or labeled low-trust auxiliary context. They never corroborate themselves.

## One reading pass

The webs work together in one pass. Segmentation and meaning classification happen together. Read against the widest usable accumulated context, and keep thin-context uncertainty explicit.

Thin-context readings default to low confidence and say so. Form and authorship stay separate: a character's despair inside a story is not automatically Ness's despair. More inferential readings must be easier to trace, challenge, suppress, and replace in the current view.

Peer webs examine intent, references such as "this" or "here", assumed common ground, implied meaning, attributed viewpoints, time/sequence, rereading, and mode/register. Their historical names are intent, deixis, common ground, implicature, theory of mind, time/sequence, rereading, and mode/register. Mode describes form rather than replacing intent. Whole-work form does not exempt individual sentences from other webs. Add a web only for a grounded dimension the existing set cannot express.

One declared pass produces one reading. Multiple angles require separate passes with their own inputs and provenance. Later synthesis adds a layer rather than rewriting earlier readings.

Code checks required fields, existing references, current inputs and permissions, and duplicate commitment. Shape checks neither certify meaning nor reject honest uncertainty. A separate AI reviewer checks grounding, invention, attribution, uncertainty, evidence consistency, channel separation, and declared-mode compliance against original evidence and permitted context. It checks whether omitted counterevidence changes the meaning, without treating grounded omission alone as failure under SYSTEM.md. Separate validation records name issues and supporting passages. Acceptance is a tested assessment, never certainty. Keep malformed/incomplete output, fabrication, unsupported certainty, channel confusion, and mode violations distinguishable.

- A rejected proposal is not a reading.
- After the permitted correction attempt under the retry rules below, unresolved disagreement leaves the proposal unaccepted. Never repeat reviews until one approves. Unrelated work continues. Routine readings need no individual approval within tested, authorized automatic-acceptance scopes. Consequential or unresolved cases follow the agreed review path. Ask Ness only when his judgment matters. See OPERATIONS.md for reviewer tests.
- Genuine `insufficient_context` is an honest, revisable reading when the source cannot support interpretation.
- Holding never forces a missing reading. An existing item or reading may also be held. Keep hold state outside the source and block new use, including derivatives, from its enforcement commit. Never park a rejected draft until it appears fresh.
- Unfillable webs name their gap without forcing Ness to answer or stopping unrelated work.
- A hold requires both a specific missing condition and a realistic way to obtain it. Otherwise write an honest insufficient-context reading when appropriate. Release requires verified bound evidence for every active hold reason.
- N.H tracks and checks holds automatically. Do not make them a manual backlog or invent an expiry. If a condition becomes known to be unobtainable, use the governed genuine-insufficiency path. Mechanical release does not reinterpret the item. Repeated rejection is not genuine insufficiency.
- Qualitative grounding labels are exactly `grounded_enough`, `partly_grounded`, `not_grounded_enough`, and `insufficient_context`. Governed assessment assigns them to exact revisions. No numeric companion, ranking score, producer self-review, or truth claim.
- `partly_grounded` cannot pass unchanged; repair or narrow it honestly. Grounding does not establish relevance, permission or quality. Missing validation is not a negative content judgment. Keep direct source evidence separate from prior interpretations, independently of positional/semantic retrieval. Ness's statement proves what he said or reported, not automatically the external event.
- Route a task-relevant unresolved meaning question to Ness with the supporting sources and exact question. Route missing sources to source recovery and technical failures to the existing retry path. Preserve unresolved rejection after the permitted correction; do not treat every failure as a question for Ness.

## Retrieval and relevance

Keep positional adjacency and semantic association separately labeled. Modes use neither, either or both as their triggers permit. Record search completion, coverage and index version. Verify results against current sources and corrections. Healthy empty retrieval permits target-only work. Failed or incomplete searches are not empty results. Use only predefined fallback paths. Never invent context or silently relax thresholds.

Versioned modes declare purpose, channel parameters, ceilings, uncertainty handling and audit rules. Enforce the lower of setting and ceiling independently at runtime. Retrieval values await empirical tests.

A usable declaration needs all eight contract fields, including its reason and uncertainty behavior. Bind exact declaration/configuration versions, source scope and ceilings. Reject over-ceiling configuration; runtime also records any defensive clamp. Audit admitted sources, exclusions, provenance, parameters and index/model/system versions. Keep positional and semantic prompt sections separate.

For ordinary answers, choose permitted relevant sources with enough conversation to interpret references and short replies. Follow important correction, replacement, clash and restriction links before relying on results. Similar wording alone is insufficient. Preserve statement time and circumstances. Newer statements do not automatically replace older ones about different situations. Historical Engine A/B input contracts remain unchanged.

Bound search. Check for evidence that could materially change the answer. Ask about gaps only when needed for the task. Otherwise answer from evidence and disclose limits. Search limits supply no certainty. Not finding a decision does not prove it never happened. Test old, differently worded and conflicting corrections.

Apply categorical gates before named graded relevance dimensions. Preserve each dimension's producer and provenance. Never collapse dimensions into a hidden score.

- Use rules for reliable mechanical dimensions, embeddings for semantic proximity, and a specifically authorized model for necessary interpretation.
- Privacy and deletion eligibility are prerequisites, not relevance dimensions. A model-produced dimension cannot control a categorical gate.
- Evaluate on demand. Precompute only for an explicitly declared latency-sensitive context. No permanent global relevance state.
- Tier 1 belongs to relevance control. Tier 2 belongs to the consumer. Each validates its own contract.
- Ness can inspect gates, dimensions, their producers and both complete configuration tiers. An invalid requested change preserves his request and the existing configuration, identifies the exact conflict and helps translate his intent into a valid change. A consequence preview supplies information, not a veto over an otherwise valid choice.
- A mode change needs preview and confirmation. Per-judgment corrections and scoped overrides append directly without rewriting earlier judgments.
- Unknown purpose types halt evaluation and preserve the request. Offer an explicit mapping or versioned addition, never guess.
- Relevance events may prompt state review. They cannot establish state currentness, certainty, causation, permission, or truth.
- A consumer that uses model-produced dimensions owns a versioned unresolved-dimension rule. Tier 1 validates its reference; the consumer validates content. Changed rules require reference updates. Do not use the reviewed state's own currentness as proof of currentness.
- An uncertain connection may support quiet search preparation, but material effects, including withholding, retain its uncertainty. Old weak evidence supports only a gentle protective possibility. An active outward suggestion needs evidence of the current situation; thread/time proximity alone is insufficient.
- A correction pattern requires the same mode/version, target and correction direction. Show its exact basis as a possibility. Silence leaves it open; explicit dismissal closes it until new overrides or material change. This differs from SECURITY.md's general gentle-question rule.

Shared gates are `same_thread_or_group`, `precedes_target_in_same_thread`, `within_declared_time_range`, and `object_type_matches`. Shared dimensions are `semantic_similarity`, `temporal_distance`, `positional_distance`, `currentness_status`, `explicit_links`, `ness_response_links`, `proposal_acceptance_outcome`, `reading_context_status`, and `active_clash_links`.

Controlled purposes are `retrieval_context_selection`, `view_assembly`, `action_surfacing`, `reread_trigger_evaluation`, and `state_review_trigger_evaluation`. An explanatory label adds no behavior. The five accepted consumer declarations use on-demand evaluation, no precomputation, and no model-produced dimensions unless explicitly changed through the governed path.

## Rereading and retries

Rereading adds a new reading and preserves every earlier one. Triggers are manual, materially relevant changed conditions, or a bounded scheduled retry for temporary technical conditions. Time passing alone never warrants reinterpretation.

- Manual rereading needs no new evidence or justification. Do not manufacture a semantic reason or gate it on relevance.
- Semantic assignments are direct, wider-context, or both when their distinct relationships apply. They are not mutually exclusive and do not replace trigger evidence.
- Both assignments still produce one operation, context snapshot and at most one reading. They define the reason and checks, not a narrower context allowance. A manual reread with no new information uses one `manual_reread_compatibility_record`, kind `manual_no_new_information_compatibility`, basis `master_v10_7H_manual`, and no `assigned_modes` field. Neither an empty list nor a third "manual" mode substitutes. Recovery reuses the exact claim-bound record.
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

The source owner must permit unchanged-input continuation. Resuming a completed B26 retrieval requires a new linked operation and real change, whether the earlier operation succeeded or failed. Partial failed retrieval stays audit-only and is never merged into later results. Exhausted retrieval failure stops with saved state; no degraded continuation is authorized.

A held refusal consumes no attempt or clock; release alone starts no retry. A later episode's first attempt has no gap or deadline until its first durable failure. Gap class follows the latest outcome, while deadline class stays fixed. Real-change examples are not exhaustive, but every other change needs explanation and evidence. Technical exhaustion, an unstarted/failed careful retry or deadline expiry cannot open B24's insufficiency fallback.

## Story, people, and clashes

Tellings stay local, source-grounded, and perspective-specific. Separate root producer, subject, viewpoint owner, direct self-report, quotation, reported speech, observation, and inference. Retain supported nested attribution; leave unsupported attribution unresolved.

Optional telling elements are whose, stance, firmness, telling, theme, and when. Read absence only where the information was expected, could have been observed, and its absence matters to the question. Any interpretation of absence stays weak and revisable.

The Story Layer owns immutable telling cards. Consumers reference them. Persist the preparation before the reading, the reading before its cards, and valid set completion before semantic telling use. Partial cards and recovery material are not canonical evidence.

Resolve pass-local source handles mechanically and assign stable IDs before hashing preparation. Prepared IDs remain spent after abandonment. Models cannot invent persisted IDs or enrich semantics after approval. `created_at` is logical creation during preparation; `prepared_at` records manifest validity; `committed_at` records card commitment. Recovery uses exact prepared payloads, never a new model interpretation. Abandoned preparation without a committed reading needs a new linked pass.

Preserve embedded `whose`, `stance`, `firmness`, `telling`, `theme` and `when` exactly. Do not guess structured roles from `whose`, turn a legacy theme into a confirmed theme, copy parent confidence as card certainty or fill missing required legacy fields. Keep embedded time, source-event time and record time separate. A card and its commit event must exist before use. Eligibility never exceeds the parent reading. The complete expected set gates semantic use, while privacy, safety and recovery discovery remain available. A zero-telling sentinel requires a validated zero-telling result, never removal of rejected tellings.

Firmness describes supported stance, never truth or inner access. Labels are `high_firmness`, `moderate_firmness`, `low_firmness`, `mixed_firmness`, and `uncertain_firmness`. `omitted_no_support` means omit the unsupported field. Use qualitative evidence, never hidden arithmetic. Firmness does not trigger or release holds.

Direct statements of certainty/doubt outweigh tone, style or repetition alone. Reported speech and uncertain attribution weaken the basis. `mixed_firmness` requires conflicting comparable signals; `uncertain_firmness` means signals exist but support no level. Repetition within one root may be a signal; repeated records add no strength.

Themes combine stable organization and provisional engine proposals. A telling may belong to several themes or none. Proposals can remain unconfirmed indefinitely and cannot silently influence later readings as adopted themes.

Keep each theme's identity stable across renaming. Append name changes and links as separate events. Provisional links remain provisional until the applicable acceptance path completes. Theme merging changes organization, never source contents or existing tellings.

Theme actions may confirm, reject, rename, merge, split or remain unresolved. Only Ness confirms. Every retrieval use retains a trace so later evidence can challenge theme influence. A clash key binds the conflicting item set and specific disputed aspect. Dismissal can stop resurfacing until a valid trigger; it removes neither evidence nor confidence.

Grounded Keeper of Origins displays and resolves source references through existing owners. It shows sources, versions, and documented derivation links. It has no authority to determine meaning, identity, or permission.

Person-Boxes gather references. They are not profiles, diagnoses, summaries, scores, or fixed identities.

- Search before proposing. Link clear mentions automatically and join definitely identical records. Keep uncertain anchors and joins pending. Name similarity alone is insufficient.
- Ness has a confirmed Person-Box. Clear authored and source-resolved first-person material links automatically. First-person text inside a pasted third-party source does not.
- Preserve link basis, certainty, authority, time, batch, and correction history. Never merge source contents across batches.
- Holding presents linked existing objects for Ness's understanding, original evidence, other perspectives, and revisable readings, with each role explicit. Corrections append events and update the presentation while preserving earlier objects. It creates no second profile or memory store.
- Keep each person's permissions separate. A link grants no disclosure right. Generic connections cannot establish identity or merge people.

The seven Person-Box sections are roots, readings, story tellings, clashes, Ness responses, themes, and unresolved identity. Filters may combine time, perspective/role, theme, source/thread, and lifecycle/confirmation. Clearing filters restores the default; full chronology remains one switch away.

Clash types are direct contradiction, interpretive divergence, temporal change, perspectival difference, evidence insufficiency, and context mismatch. Compare the same person, conditions, time, and context. Record whether both statements could be true without selecting a winner.

Deduplicate clashes by identity. Later detections and Ness responses append linked events. Keep active conflict beside affected items in retrieval, views, state support, and suggestions. A response or new reading does not erase the original clash. Do not provide a misleading resolve action.

## Views and state

- Always retain current and historical views. Ordering is presentation, never a truth verdict.
- Simple reading presentation starts with the newest usable accepted reading, excluding rejected and insufficient-context readings. It is not automatically the best or true reading. Computed View's evidence ordering remains a separate presentation; original chronology stays reachable.
- Person-Box sections open as compact lists with evidential status and expandable chains. Keep unusable items labeled, clashes adjacent, and original chronology reachable. No synthesized personality strip or per-person score.
- Computed View derives an inspectable current picture with disclosed ordering. It neither writes new interpretations nor supplies upstream evidence. Use it quietly for responses; show the internal picture when Ness asks.
- Its fixed factor order is current Ness judgment, direct root evidence, reading acceptance/grounding, purpose relevance, context quality/provenance, clashes/uncertainty, then recency as a tie-breaker. Preserve separate factor outcomes and explain priorities. No aggregate truth score.
- Refresh only on applicable triggers. Commit immutable snapshots and separate refresh-status events. Failed, incomplete, and no-change refreshes do not create falsely fresh snapshots. Never mark an old snapshot in place.
- Living State has no reader of its own. It consumes permitted evidence and readings. Keep state existence separate from present currentness.
- Use a small common state record with source references, viewpoint, event period, and update history. Add only details needed for that state type, such as a constraint, capacity, or causal hypothesis.
- Preserve brief or weak signs as evidence. Full-node creation requires materiality. Each time-bounded episode has its own identity. Later recurrence creates a new episode.
- Separate experienced states, causes, positions, open loops, relationships, values, constraints, capacity dimensions, transitions, causal hypotheses, and counterfactuals.
- Multiple positions may coexist. Do not average them into a false middle or label complexity a disorder.
- Currentness changes append dated evidence-linked events. Time alone does not end a state. Relevance can initiate review, never decide its result.
- Ground every causal-chain link. Timing, similarity, coherent storytelling, and a confirmed result connection do not prove causation.
- Internal counterfactuals may support comparison automatically. Visible or immersive simulations require their separate permission. Imagined scenes are not observed reality.
- Keep the world model's active core separate from wider general knowledge. Preserve attribution, uncertainty, world membership, and currentness. Keep world membership, links to simulated situations, and relevance to the current request separate. Attention selects what to inspect or present; it cannot establish truth, identity, accepted relationships, or permission. Display changes cannot change source type or rewrite evidence.

Currentness labels are `current`, `possibly_current`, `stale`, `currentness_unknown`, `ended_by_evidence`, and `superseded_by_evidence`. Capacity keeps thinking, emotional, bodily, practical, and decision-making dimensions separate; an optional supported summary identifies its contributing dimensions.

Direct self-report may establish current state immediately. Inference requires several meaningfully independent grounded messages/signals and starts `possibly_current`; repeated copies count once. Routine updates need no per-item approval. Only newer grounded evidence ends or supersedes a state; time alone gives stale or unknown. A protected personal boundary needs direct wording or repeated clear choices, refusals, stopping or withdrawal. Causes require direct statements or several connected grounded signs, with alternatives and uncertainty. Exact counts/windows remain open.

Give records derived from one underlying evidence event a shared evidence-family identifier. Readings, restatements, derivative links and logs retain their individual records but count as one family when assessing independent support. Do not confuse repeated representations with independent observations.

Only a definite same-episode match adds support to an existing node. Later recurrence, separate concurrent positions, changed interpretation and uncertain matches stay distinct. Search existing vocabulary and nodes first. Ground each causal link and preserve the weakest link's visibility. Internal counterfactuals remain hypothetical and assumption-linked, never plans.

World-model active membership needs a qualifying life, relationship, project, commitment, decision, environment, resource, rule, purpose or materially connected event. Preserve every separate basis. End membership only after all bases end on evidence; failed evaluation preserves prior membership. It is not the visual World or a store of all knowledge.

Computed View needs a valid current authorized ordering profile, with separate factor, tie, omission, surfacing and refresh rules. A null update creates only a status event. Failed refresh leaves the prior valid snapshot possibly stale. Recover a missing status event for a committed snapshot without rebuilding it. Source families include roots and safe pre-ingest metadata, never held raw content.

During quarantine and periodically afterward, read-only memory-health checks look for missing sources, excessive older-reading dependence, one lineage masquerading as independent repetition, thin Person-Box support, confidence without independent roots, and hidden contradictions. Checks never repair or rewrite inspected records themselves.

## Connections and creations

Connections require a direct recorded relationship, Ness's explicit statement/confirmation, or a narrow authorized rule. Similarity, timing, shared themes, interpretation, and co-retrieval cannot create a connection proposal or accepted relationship by themselves.

- Keep endpoints, relationship type/direction, certainty, decision status, authority, and history separate.
- Pending connections may guide investigation silently. They cannot support claims, recommendations, identity effects, or actions. They never age into acceptance.
- Acceptance atomically commits the connection and its authority evidence after duplicate checking. Competing routes converge on one relationship.
- Candidate reports, proposals, Ness's durable decision input, final decisions and accepted records remain distinct. Forward completion requires the same current proposal/version, shown certainty and decision display, valid authority/integrity/privacy and no intervening competing decision or correction. Never rebind approval. Commit the accepted record, authority proof, duplicate key and final decision together. Symmetric keys normalize endpoint order; directional keys preserve it. Changed endpoints/type/direction/type version require a new key. Failed source verification is evaluated and set aside, not confused with unavailable verification.
- Before each use, resolve exact accepted version, later correction/dispute/supersession, integrity, authority, current-use state, certainty, privacy, and influence restrictions. An old accepted record is insufficient.
- Rejection suppresses repeat surfacing. Genuine new evidence permits a new linked proposal, not reversal of the earlier decision.

The Unified Creation Store holds root-referencing records for `design`, `idea`, `rule`, `name`, and `decision`. A record may have several types. Projects and categories are views, not separate databases. Creation origination is currently live-chat-only. Adding intake paths or types beyond these five requires Ness's explicit decision and a versioned change.

- Detect source-grounded fragments broadly and provisionally. Each immutable base starts `provisional` with identity, type set, provenance, schema version, and detector reference where applicable.
- Later confirmation, correction, supersession, and grouping are append-only events. Do not change the original status field.
- Confirmation requires explicit Ness confirmation or later clear words/actions demonstrating adoption. Ambiguity, time, retrieval, repetition, and model confidence never confirm.
- Wider provisional use must retain status and a trace. Larger works reference every original fragment rather than fusing them.
- The root and exact fragment identify a creation independently of detector version. Changed segmentation is a linked proposal, never silent fusion. The confirmation event is the single status authority. Demonstrated adoption requires a grounded B24-checked proposal linking the original fragment and later words/actions. Every wider use records `provisional_material_used` with status at use time and shows its provisional status in the output context.
- Selected Wonder material retains its origin on every presentation. An explicit retrieval request is enough reason to surface it within permissions. Later real-world evidence has a separate source identity even if it matches the imagined event.
- Affirmation records an actual response to specific readings. It does not alter their truth, confidence, evidence, or firmness. Rejection does not prove the opposite. Dismissing a specific reading can stop its resurfacing until a valid new trigger, without deleting it. Silence changes nothing.
