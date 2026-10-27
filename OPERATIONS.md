# Durable operations

These shared contracts do not select a database or implementation language.

## Records and recovery

- Each real operation has one parent history. Stages, attempts and recovery append children. Record actual outcomes, including rejection, omission, no change and evaluated-but-unused material.
- Logs stay protected and retrievable. They add no evidence weight or access and never recursively log their creation.
- Keep domain facts, operational logs, lifecycle events, authority proofs, and projections separate. A log cannot replace its owner's canonical record.
- General logs carry minimal structural references, not raw secrets, private payloads, full protected locators, or reconstructive descriptions.
- Freeze identity, schema version, provenance and governing inputs. Append corrections/status changes beside committed bodies.
- Commit each boundary completely or not at all. Acknowledge durable truth. Order cross-owner protocols without assuming a shared atomic transaction.
- Enforce structural uniqueness and stable canonical keys at effect boundaries. Before repeating work, recovery checks owner commitment. Similarity scans and random new IDs cannot prevent duplicates.
- Missing checkpoints, vanished workers, silence and interrupted calls prove neither effect nor absence. Reconcile unknown effects through their owner before retrying.
- Preserve failed, cancelled, partial, stale and unknown outcomes. Never relabel failed children as successful. A failed child need not terminate its parent unless its contract requires it.
- Retry policy, operation identity, reread trigger, hold release, authority, and effect ownership remain separate.
- Rebuildable indexes and views cannot determine commitment, replace originals, gate success retroactively, or grant permissions.
- Retain operational records. Append active/cold changes separately. Cooling needs an accepted rule; reactivation needs actual use or a valid governed new link, not similarity alone.

Record producer, operation, time, supplied inputs/sources, decisions/outputs, omissions/rejections/failures/unknowns with reasons, unchosen alternatives, uncertainty, connections and every actual use. Use events name record, consumer, purpose, contributing output/decision, outcome, unused alternatives/reasons and uncertainty. Append later use without rewriting earlier records.

Self-examination needs current context, a genuine system purpose, design rule, anomaly, Ness's question or another authorized trigger. Examine only what that purpose needs within work budgets. Record trigger, examined records, findings, result use, uncertainty and connections. Do not confuse this with recursively logging log creation.

## Background work budgets

Bound each background job's time, model calls or examined material using hardware/workload measurements. At budget exhaustion, preserve completed steps, remaining work and input references, then pause at a safe checkpoint. Before resuming, revalidate frozen inputs, permissions, retry rules and claim ownership. Never substitute changed inputs into the same attempt or repeat commitments/effects. Apply owner revision rules, including MEMORY.md's linked-operation rule for rereading.

A budget pause is not failure, crash replay or acceptance. Never weaken checks or silently enlarge budgets. Continue under allowed rules or Ness's required decision.

Live interaction normally outranks background interpretation. Yield after short safe commits. Priority grants no second queue worker or concurrent claim. Disclose unfinished dependencies; never deliver unvalidated conclusions.

## Reading queue

- Support one worker and one job at a time. Hold an exclusive OS job lock throughout processing. Expiry timestamps are not concurrency authority.
- After durable root append, enqueue once under `stable_hash(root_id + "reading_job_v1")` through the shared locked append/flush boundary. Release enqueue lock before reading work.
- Startup reconciles only the authorized eligible root set. Never silently enqueue all historical roots.
- Commit the immutable pass instruction before retrieval. Keep attempts and terminal lifecycle events separate.
- Use `stable_hash(enqueue_key + "reading_v1")` as the reading's idempotency key. Keep pass identity as provenance, not duplicate identity. Recovery finds an existing reading before writing.
- Preserve sequential retrieval, proposal, acceptance, quarantine write, clash/view processing, and job close. Check claim authority before protected writes.
- Commit explicit no-clash/no-update sentinels. Absence is not a negative result.
- Crash replay recovers incomplete crash work only. Completed/failed jobs and handled technical failures do not enter it. Budget continuation follows the rules above. Holds, privacy refusal, and indeterminate work block admission.
- Nightly activation durably records each trigger, admits one activation run, and processes only existing eligible jobs. Preserve separate request, configuration, run, and disposition records. No silent historical backfill.

## Promotion and evaluation

- Quarantine never silently becomes production input. B16 promotion resolves exact reading/evaluation identities and freezes complete evidence before reservation and commit fences.
- Evaluation distinguishes machine completeness, independent assessment, Ness's actual judgment, and authority proof. A model or annotator name cannot stand in for judgment authority.
- Lookup prior commitment, admit one reservation, verify current prerequisites, commit at most one eligibility record, and record the parent outcome before acknowledgment.
- Promotion machinery neither judges content nor creates/writes the production store. Production activation remains separately gated.
- Preserve sealed gold identities and trial provenance. Missing source cases, unresolved reviewer independence, unknown scoring rules, or unchosen judgment authorization cannot be fabricated into passing evidence.

Test reviewers on Ness-judged examples, including deliberate errors and valid readings. Measure missed errors and wrongful rejection before authorizing a defined automatic-acceptance scope. Separate models do not establish independence. Ness sets intended behavior and resolves substantive questions without manually grading every run.

Ness approved planning/testing, not activating automatic acceptance. Define candidates by task, sources, language and context, initially ordinary interpretation with clear attribution and available sources. Scope, reviewer, judgment authority, tolerances, qualification and activation still require evidence and separate decisions.

Reviewer authority and failure handling refine existing rules without appointing or authorizing models. Distinguish malformed output, fabrication, unsupported certainty, speaker confusion, mode violations and reviewer failure. Detailed handling remains open. Rewording cannot repair missing permission, stale sources or unknown effects. MEMORY.md owns correction/retry limits.

For complete-system tests, fix expected behavior before execution. Test full capture, interpretation, correction, persistence, recovery, retrieval, and authorized delivery cycles. Inspect records, permissions, duplicates, and operation outcomes as well as visible answers. Inject crashes during writes, connection loss after external effects, access changes during speech, and mid-answer corrections. Honest unfinished or unknown outcomes may pass where specified; apparent success cannot hide an unsafe effect.

Agree separate standards for permissions/record preservation, semantic quality, latency/interruption, and failure reporting. One aggregate score cannot excuse a forbidden disclosure or duplicate action. Repeat important scenarios and retain cases not used for tuning. Passing applies only to the tested version and scope, guarantees no universal correctness, and authorizes no production activation.

## Intent reliability research

The 2026-10-23 intent-reliability proposals remain unadopted, including candidate 12B/6B roles. PROVENANCE.md identifies full procedures and primary-source research. Neither more context, grammar/schema constraints nor model confidence guarantees meaning. Preserve Engine A/B contracts and existing acceptance, revision and delivery rules.

Use pinned disposable runtimes without production effects. Experimental briefs remain advisory, never canonical fields. Test baseline and proposed changes on frozen development/held-out scenario families without paraphrase leakage or answer feedback. Include English/Hebrew/mixed language, attribution, conditions, negation, confirmations, quotations, simulation, indirect requests, alternatives, corrections, stale work, clear requests and discussion versus execution. Separately measure unsupported commitments, meaning/attribution errors, ambiguity misses, needless questions, reviewer misses/rejections and fidelity, then latency, memory, interruption and speech. Ness sets tolerances. Code checks bindings/structure; independent review checks support and fidelity.

Try retrieval/prompts/tests before [QLoRA](https://arxiv.org/abs/2305.14314). Training needs separate approval, excludes personal memories/identity, and requires untouched reevaluation before adoption. Adapter feasibility proves neither accuracy nor hardware fit. Never weaken acceptance for a failing model.

## Local conversation and speech findings

PROVENANCE.md locates the 2026-10-24 experiments and full historical measurements. EXPERIENCE.md owns acceptance. Gemma4 12B, E4B and Qwen3 4B Thinking remained unadopted; trials included needless clarifications, wrong-topic advice, delayed correction acknowledgments and withheld stale results. No training or answer keys occurred.

Q8 VoxCPM and RAM-buffered playback passed measured preparation, driver-progress and simulated revocation/Stop checks. Acoustic/click latency, actual N.H grants, microphone interruption and message-feed integration remain unproved. Targets remain preparation during arrival within 20 to 30 seconds and playback within two seconds of Read; retest with pronunciation connected.

RenikudPlus int8 preserved characters and passed substitution/span checks, but meaning and a suspect verb remain unresolved. Automatic vowel marks degraded VoxCPM, style instructions became speech, native GPU trials failed before rendering, and manual vowel fixes failed the general requirement.

BlueTTS ONNX v2's UTF-8 phoneme demonstration succeeded after encoding failure with the unchanged full reference. Whole-context predictions through section rendering remain unverified. ASR only screens; human listening judges. No gain, filtering, added silence or selected retakes hid failures. No engine replacement or N.H activation occurred.

Next test fresh sentences, meaning, reference fidelity, tone, authorization, revisions, cancellation and interruption. Preserve first takes and failures without weaker privacy/acceptance, training or answer leakage.

## Authority verification

AIC verifies artifact identity and recorded authority. It does not create authority, repair artifacts, choose a winner between contradictory governing records, or replace runtime access checks.

- Derive status from explicit adoption or acceptance evidence, never filenames, placement, dates or historical headers.
- Establish shared work, enumerate the governing set, recompute member identities and status evidence, revalidate authority order/rules, then seal a content-bound verification generation.
- Commit one outcome per fully sealed generation before terminal. A family lookup key owns no generation outcome lock.
- Reuse requires rechecking all current inputs. Cached summaries, elapsed time and remembered hashes prove no freshness.
- Distinguish unavailable inspection from verified absence or contradiction. Retry exhaustion never turns unfinished work into artifact refusal.
- Recovery preserves partial observations and resumes only admissible missing steps. It never releases provisional, inherited, or assumed authority.

## Coordination

UDOK coordinates typed references to owner records. It does not own meaning, policy, effect execution, privacy, retry admission, hold release, or authority.

- Keep operation, generation, caller, child, claim, evidence, authority, attempt, checkpoint, and delivery identities distinct. A kernel ID cannot replace an owner's duplicate key.
- Commit coordination boundaries separately. Carry references rather than copies of usable owner truth, summaries, or booleans.
- Resolve pre-coordination prerequisites before admission. Resolve owner-created claims and per-use permissions only at the owner's exact effect boundary, after the owner can create them. Recheck at commitment.
- Register children before work. Close unchanged membership before terminal completeness. Do not trim requirements after failure or declare two of three required children complete.
- Bind results to exact current generation and owner references. Fence stale results before consumption, effect, release, and delivery. Do not rebind old results or escape unresolved obligations by changing generation.
- Cancellation requests, receipt acknowledgments, and actual owner cancellation are different facts. The coordinator cannot cancel a child or revoke authority on its owner's behalf.
- Keep waiting, holds, unknown delivery, and failure distinct. A checkpoint grants no permission and refreshes no authority.
- Recover establishment, generation, current owner prerequisites, claims/effects, and child terminals before appending missing coordination events. Never replay an effect to recover an acknowledgment.

## Research and imports

- Brave supplies raw research. Academic sources are Semantic Scholar and OpenAlex under the later recorded design. Google Scholar and Tavily are excluded directions.
- Separate fetch, text-only synthesis, and create-space/review contexts. SECURITY.md owns enforced isolation and untrusted-input handling.
- No research stage writes directly to roots, readings, creations, or production. All accepted intake uses the normal shared path and permissions.
- Preserve relevant plain text and an inert full-page PNG with provenance, time, reference, and integrity hash. Isolate page rendering separately. Store no active HTML, scripts, cookies, or sessions.
- The screenshot supports human review, not reasoning or embeddings. If unavailable, retain verified text/metadata and failure reason. Do not discard or lower textual confidence solely for a missing screenshot.
- Auto-reject flagged material but never silently delete it. The rejected-bin view uses escaped text, inactive URLs, stripped spoofing characters, no previews/network fetches, and disabled copy/select. Those UI restrictions are not a security boundary.
- Implement a query counter and daily spending cap. Automatic currency checks need Ness's approved schedule. Historical 3 AM / 150-cycle / three-search values grant no schedule authority.
- Check claims against whole supporting passages, not two-of-three result-set votes. Retain each source, date and passage; trace copied or shared origins. Repeated pages add no independent support. Preserve conflicts and missing evidence. One direct source supports narrow attributed claims, not broader untested performance. Add nothing unsupported. Keep source and run identities separate from content duplicate identities.
- Commit fetched, preserved, synthesized, gated, and queued/rejected checkpoints. Resume committed progress without fabricating failed stages.
- Image intake preserves metadata, proposes a plain description, proposes contextual meaning, obtains Ness's confirmation, then uses Catalog. Neither machine proposal is a source fact or a substitute for the original image.
- Use text recognition for writing, detection/segmentation for labels and locations, and local vision-language models for proposed descriptions. Keep tool outputs separate with uncertainty. Never infer identity, emotion or intent from appearance alone or invent unreadable details. Qwen3-VL, YOLO, Segment-Anything, osam, PaddleOCR-VL, SmolVLM and Ollama remain candidates needing image and hardware tests; this design selects and installs none. Imported observations and later reactions stay separate.
- Deferred WhatsApp ingestion stays disabled until its protected mechanics are accepted/integrated and Ness authorizes use. A design record alone cannot authorize decryption or ingestion.
