# Durable operations

These shared contracts select no universal database or implementation language. SECURITY.md preserves the specific accepted SQLite choice for TSC.

## Build plan draft

This repository-only draft grants no implementation, model adoption, migration or activation authority. It is not an adopted build plan. DECISIONS.md owns unresolved choices; domain documents own behavior.

### 1. First-version scope

Proposed first milestone: one isolated text-memory cycle using nonpersonal fixtures, authorized capture, durable root commitment, one contextual reading proposal, independent assessment, quarantine, retrieval and permitted presentation. Demonstrate both accepted and withheld outcomes. A fixture cannot qualify a reviewer or authorize automatic acceptance. Live conversation use still depends on the unresolved TSC boundary in DECISIONS.md.

Later proposed milestones add conversation, speech, research/actions, phone and World/Wonder. Ness has not approved this release order or scope. Future intentions need adoption; legacy retirement needs authorization.

### 2. Existing-code baseline

The tracked project contains design documents and a document checker, not an N.H runtime. This draft makes no finding about external code. Before implementation, inspect the actual supplied runtime checkout, its instructions, protections, dependencies, stores and tests. Record verified reusable components and gaps; choose reuse or replacement from evidence, not filenames or historical claims. PROVENANCE.md locates historical contracts/evidence, not a verified current implementation.

### 3. Component connections

| Handoff | Existing contract and remaining detail |
|---|---|
| Capture to Catalog | MEMORY.md owns source identity, payload, attribution and blockers. Resolve exact adapters without inventing missing attribution. |
| Catalog to root writer to queue | Use authorized batches, existing root schema and durable enqueue rules. Specify actual calls, receipts and recovery from owner contracts. |
| Retrieval to Meaning Engine | Commit pass instructions, retrieve permitted context, produce one proposal under MEMORY.md. Select models only after evidence and adoption. |
| Proposal to reviewer to quarantine | Separate structural checks, semantic assessment and accepted commitment. Recover original schemas before coding validators; preserve rejection and holds. |
| Reading to stories, state and views | MEMORY.md owns references and update rules. Complete required telling sets and dependent updates without duplicate effects. |
| Current result to presentation | SYSTEM.md owns request revisions and messenger fidelity; SECURITY.md owns delivery. Revalidate exact versions and permissions before effects. |

Before coding these logical handoffs, resolve concrete inputs/outputs, writers, commitment, duplicate keys, revisions, cancellation and unknown-result recovery in owner contracts. These are not finalized APIs; invent no fields or universal success flags.

### 4. Build order and completion evidence

| Proposed stage | Reviewable result and completion check |
|---|---|
| Establish baseline | Inspect supplied code and original contracts; resolve milestone-dependent gaps and propose stack, dependencies and exact change scope. No runtime edits yet. |
| Isolated storage and queue | Fixture capture commits once, survives interruption and respects exclusions, holds, batch sealing and single-worker ownership. |
| Reading and assessment | Preserve source, attribution, uncertainty and provenance; distinguish structural success from semantic acceptance. Check incorrect and valid proposals under the evaluation rules below. |
| Retrieval and presentation | Recover committed results; honor corrections/restrictions; distinguish empty retrieval from failure; withhold stale or unauthorized output. |
| Conversation and extensions | After their prerequisites are resolved, test revisions, late cancellation, speech interruption, private channels, sync loss and each authorized extension's full cycle. |
| Release review | Collect version-bound behavior, security, recovery and resource evidence. Obtain separate required model, migration, retirement and activation decisions. |

Agree outcomes before tests. Required records/checks determine completion, not demos or document counts. Test partial-write restart, duplicate capture, mid-output access changes and missing sources. Semantic acceptance needs external judgment, not model confidence.

### 5. Installation and execution

Only the documentation checker currently has a repository-defined executable command; README.md documents it and the optional bundle export. `tools/requirements.txt` pins its tokenizer dependency, not runtime requirements. No N.H installation, launch or runtime-test command is established here.

After baseline/stack decisions, document verified prerequisites, versions, isolated installation, configuration locations without secrets, startup, shutdown, tests and recovery commands in README.md. Report missing commands; invent no installation procedure or historical-launcher use.

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
- Every log starts active. Cooling requires both sufficient age under its component-owned versioned rule and no genuine use or valid new link. Exact authorized use reactivates without a new general permission. Cooling changes presentation/retrieval priority only. Failed evaluation preserves status. Rule changes need observed frequency/usefulness, examples and Ness's approval, not invented universal values. Find cold records through known links first, with semantic search as fallback.

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
- `thread_membership_v1` permits bare/local-context for manual work. Live bare requires a recorded nonempty reason. Nightly, reread and unknown triggers cannot borrow that live/manual rule. Confirmed real or provably untitled groups with preceding turns use local context; otherwise use the applicable bare rule. Unknown membership warns. This version never adds associative/combined retrieval; rereading has its own later owner.
- Use derived `source_title_type` and thread facts, never raw title text, for this policy. An invalid associative/combined path falls back to bare input and records an implementation error. This narrow policy does not override B26's retrieval-failure rules.
- Enqueue and job locks have separate roles. Reuse the existing OS lock rather than replacing its file to gain ownership. Check the current claim before each durable write. Preserve exact existing lock/claim contracts before implementation.
- Use `stable_hash(enqueue_key + "reading_v1")` as the reading's idempotency key. Keep pass identity as provenance, not duplicate identity. Recovery finds an existing reading before writing.
- If a committed instruction lacks its lifecycle result, look up the job-key reading first and recover any existing result. Only confirmed absence permits appending abandonment, creating a new linked pass and restarting from retrieval. Failed lookup is not absence. Never silently resume half of an interpretation.
- Preserve sequential retrieval, proposal, acceptance, quarantine write, clash/view processing, and job close. Check claim authority before protected writes.
- Commit explicit no-clash/no-update sentinels. Absence is not a negative result.
- Crash replay recovers incomplete crash work only. Completed/failed jobs and handled technical failures do not enter it. Budget continuation follows the rules above. Holds, privacy refusal, and indeterminate work block admission.
- Nightly activation durably records each trigger, admits one activation run, and processes only existing eligible jobs. Preserve separate request, configuration, run, and disposition records. No silent historical backfill.
- The one-time `.nh_queue_activation.json` boundary is immutable, not a nightly switch. Scheduled requests bind schedule version/window; manual requests bind their own durable identity. A distinct request during a run is not a duplicate. Coalesce only proven exact work coverage; otherwise durably hold or explicitly refuse it. Recheck held requests after completion or crash. A crashed run closes with committed progress; the next window may proceed while job recovery follows its own rules.
- Commit per-reading clash and per-profile view outcomes, including zero-result sentinels. Aggregate completion requires every expected child. Zero profiles may be valid. Recover missing checkpoints from actual owner results, not by rerunning effects.

## Promotion and evaluation

- Quarantine never silently becomes production input. B16 promotion resolves exact reading/evaluation identities and freezes complete evidence before reservation and commit fences.
- Evaluation distinguishes machine completeness, independent assessment, Ness's actual judgment, and authority proof. A model or annotator name cannot stand in for judgment authority.
- Lookup prior commitment, admit one reservation, verify current prerequisites, commit at most one eligibility record, and record the parent outcome before acknowledgment.
- Promotion machinery neither judges content nor creates/writes the production store. Production activation remains separately gated.
- Promotion derives eligibility for the unchanged quarantined reading, not a physical copy/move. Its permanent claim binds an immutable evidence snapshot. Gold, held-out results, manual inspection, Ness's bound promotion decision, deliberate marker, approved dry run, privacy and hold status remain separate prerequisites. Orphan eligibility grants nothing. Ordinary reasoning cannot consume promotion logs as content. Reservation release and commit fencing obey the same strict non-commit recovery proofs as the root writer.
- Preserve sealed gold identities and trial provenance. Missing source cases, unresolved reviewer independence, unknown scoring rules, or unchosen judgment authorization cannot be fabricated into passing evidence.
- The accepted A1 replacement contains actual separate story-bearing cases; it does not recover the missing original set or prove pinning/ingestion. Pin exact source and acceptance identities before tests. Fix scoring/format before parallel gold annotation and structural validator work. Structural fixtures use the format, not the answers. Full semantic evaluation requires the sealed case set.
- The eight replacement cases R01 through R08 all have `high_firmness`, a coverage limitation. Preserve exact target/context boundaries, separate primary/thematic grading and exclude later conversation leakage. Do not reconstruct those fixtures from summaries.
- B16 evidence epochs freeze policies, case lists and trial counts before runs. Exploratory runs stay permanently ineligible. Commit every completed output before judging it, including failures. A failed human grade is not a retryable execution. Do not use the ordinary careful-retry allowance to erase measured outputs. No new attempt starts after run closure.
- Gold, held-out quality and B24 system eligibility are distinct. Ness judges gold and B24 semantic cases; machine graders judge declared mechanical rules only. Judgment forks are indeterminate, not newest-wins. D16 identity proof remains unselected, so canonical formal Ness judgments are blocked; informal feedback is allowed.
- Later discovery of a committed output may establish effective completion; proven absence after closure leaves a run incomplete. New relevant evidence invalidates prior results for new checks, not absorbing committed promotions. Judgment authority is checked at commit time; later normal session expiry does not erase it. Conditional token designs require claim, durable BAI receipt, then exact judgment commitment. A head breach blocks replacement until an accepted repair policy exists.

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
- Distinguish unavailable inspection from verified absence or contradiction. Retry exhaustion never turns unfinished work into artifact refusal.
- Recovery preserves partial observations and resumes only admissible missing steps. It never releases provisional, inherited, or assumed authority.
- AIC family identity contains artifact class/scope only. Concurrent callers share a durable pre-generation establishment anchor, not clocks/nonces, while retaining separate caller attachments. One claim precedes enumeration. Enumerate the entire governing/status-evidence set, revalidate it, then atomically seal; only sealing creates a generation.
- Freeze the verification basis and commit one outcome before parent terminal/release. A family lookup key owns no generation outcome lock. Reuse requires identical current membership, bytes, rules and verified absences, including a complete refusal basis. Cached summaries, elapsed time and remembered hashes prove no freshness. A changed-input cause admits fresh shared establishment, never a pre-generated outcome. Technical inspection failure is neither absence nor refusal.
- Route committed snapshot, retryable technical failure, deterministic refusal, indeterminate recovery, live dependency hold and privacy refusal separately to B9. Deterministic refusal has no substantive-retry authorization; do not retry refusal into approval. Indeterminate is run evidence, not a third authority result.
- Before sealing, retry admissible AIC-1/2 establishment work. After sealing, preserve unchanged input confirmation and the AIC-3/4/5 execution boundary. The explicit v1.5 correction retained through v1.10 controls stale generic restart wording; never reopen AIC-0/1/2 on an established-generation retry.

## Coordination

UDOK coordinates typed references to owner records. It does not own meaning, policy, effect execution, privacy, retry admission, hold release, or authority.

- Keep operation, generation, caller, child, claim, evidence, authority, attempt, checkpoint, and delivery identities distinct. A kernel ID cannot replace an owner's duplicate key.
- Commit coordination boundaries separately. Carry references rather than copies of usable owner truth, summaries, or booleans.
- Resolve pre-coordination prerequisites before admission. Resolve owner-created claims and per-use permissions only at the owner's exact effect boundary, after the owner can create them. Recheck at commitment.
- Bind results to exact current generation and owner references. Fence stale results before consumption, effect, release, and delivery. Do not rebind old results or escape unresolved obligations by changing generation.
- Cancellation requests, receipt acknowledgments, and actual owner cancellation are different facts. The coordinator cannot cancel a child or revoke authority on its owner's behalf.
- Keep waiting, holds, unknown delivery, and failure distinct. A checkpoint grants no permission and refreshes no authority.
- Recover establishment, generation, current owner prerequisites, claims/effects, and child terminals before appending missing coordination events. Never replay an effect to recover an acknowledgment.
- Register each child against the exact current open parent/generation/owner before work. Registration and closure compete on one head. Close unchanged membership before terminal completeness. Fixed rules determine the exact required set; failure cannot shrink it. Two of three required children are not complete.
- Commit predecessor closure separately before admitting a successor, then recheck the head. Resolve unknown owner obligations or prove effect-free supersession. Fresh admission and required AIC release precede work. Terminal parent state ends its generations; later work needs a new operation.
- Reconcile unregistered work found while the generation is open from owner records without replaying effects. Discovery after closure is a contradiction requiring owner resolution. Before terminal it blocks terminal/acknowledgment; after terminal but before acknowledgment it preserves terminal and blocks acknowledgment; after acknowledgment it preserves both and blocks further reliance. Never claim late discovery prevented an already completed effect.

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
- Source-content identity excludes fetch time and run ID. Candidate identity binds source content and normalized candidate payload, not synthesis version. Identical results add an event to the existing candidate; materially changed content creates a linked version. Preserve separate dated snapshots. Screenshot failure records `SOURCE PRESERVATION INCOMPLETE` when text/integrity/provenance remain valid. Rejected material may be deliberately inspected in its restricted view but cannot influence ordinary reasoning or memory.
- Image intake preserves metadata, proposes a plain description, proposes contextual meaning, obtains Ness's confirmation, then uses Catalog. Neither machine proposal is a source fact or a substitute for the original image.
- Use text recognition for writing, detection/segmentation for labels and locations, and local vision-language models for proposed descriptions. Keep tool outputs separate with uncertainty. Never infer identity, emotion or intent from appearance alone or invent unreadable details. Qwen3-VL, YOLO, Segment-Anything, osam, PaddleOCR-VL, SmolVLM and Ollama remain candidates needing image and hardware tests; this design selects and installs none. Imported observations and later reactions stay separate.
- Deferred WhatsApp ingestion stays disabled until its protected mechanics are accepted/integrated and Ness authorizes use. A design record alone cannot authorize decryption or ingestion.
- The accepted intake design names `wa-crypt-tools`, read-only SQLite message intake, image intake when needed, privacy and Catalog. Historical `_iter_whatsapp_messages()` and batch tag `seed:whatsapp_a13` remain proposed implementation identifiers, not active v1 fields. Preserve source sender and chat/contact title.
- Check authority at each stage before plaintext staging. Keep keys in Level-1 protection, register every temporary derivative and seal staging after a crash. Message, media and attachment relationship are independent durable work items. Recover all incomplete items. A terminal media failure preserves its valid message without inventing an attachment link. Commit links only after both exact endpoints exist. Directional duplicate keys preserve endpoint order; symmetric ones normalize it.


## Decision triage and deferred hardening

Recover existing decisions before asking new questions. A mandatory derivation must follow from accepted rules, not merely be compatible. A mechanical choice must preserve behavior, failure/recovery, resources and effects on people. Real alternatives and reserved policy decisions remain Ness's. Evidence waiting retains its owner, producer and return trigger.

A proposed bulk derivation/equivalence batch needs blind independent ChatGPT and Claude reviews of the same questions and sources before comparison. Without both, disclose unchecked status. Ness may still decide individual alternatives. Bind the exact batch version, support partial approval and recheck dependencies after rejection. This method does not require a new approval for the present explicitly authorized source-restoration task.

Deferred hardening includes hash-chained audit with missing-entry detection and a declared writer; dependency locks, model hashes, environment export, restore instructions and upgrade compatibility checks; measured queue/storage limits and explicit deferral; and tested joint restoration of roots, readings, manifests, indexes, seals, hashes and keys without duplicates. These are not retroactive prerequisites for the historical minimal engine.

Keep private-content-free rates for reading failure, insufficient context, malformed output, retrieval misses, duplicate readings, resurfaced rejections, missing roots and model latency. Owners, values and schedules remain open. Root unavailability, malformed stores, missing indexes, offline models, missing keys and inconsistent manifests need their predefined read-only/evidence-only responses. Unsupported-version handling remains open; invent no universal fallback.

The historical Claude Code kit is a source reference, not a verified installed sandbox. Its Stage 0 report covers the listed Windows/PowerShell checks, not Bash or every indirect script. Any future external runtime handoff uses a deliberate engine-file allowlist in an isolated copy. Git history and non-prefixed exports can contain private material; removing visible `.nh_` files alone is insufficient.
