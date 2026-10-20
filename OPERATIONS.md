# Durable operations

These shared contracts do not select a database or implementation language.

## Records and recovery

- One real operation has one parent history. Stages, attempts, and recovery append linked child events. Log actual outcomes, including rejection, omission, no change, and evaluated-but-unused material.
- Logs are living, protected, retrievable records. They add no evidence weight, grant no access, and never recursively log their own creation.
- Keep domain facts, operational logs, lifecycle events, authority proofs, and projections separate. A log cannot replace its owner's canonical record.
- General logs carry minimal structural references, not raw secrets, private payloads, full protected locators, or reconstructive descriptions.
- Freeze record identity, schema version, provenance, and governing inputs. Corrections and status changes append beside committed bodies.
- Commit each defined boundary completely or not at all. Acknowledgment follows durable truth. Keep cross-owner protocols ordered rather than pretending separate stores share one atomic transaction.
- Use structural uniqueness and stable canonical keys at the actual effect boundary. Lookup-first recovery checks owner commitment before repeating work. Similarity scans and random new IDs are not duplicate defenses.
- Missing checkpoints, vanished workers, silence, and interrupted calls do not prove an effect did or did not happen. Reconcile unknown effects through the owner; do not retry blindly.
- Preserve failed, cancelled, partial, stale, and unknown outcomes. Never mutate a failed child into success. A failed child need not terminate its parent unless the parent contract says so.
- Retry policy, operation identity, reread trigger, hold release, authority, and effect ownership remain separate.
- Rebuildable indexes and views cannot determine commitment, replace originals, gate success retroactively, or grant permissions.
- Keep each operational record. Active/cold status changes append separately. Cooling needs an accepted rule; reactivation requires actual use or a valid governed new link, not similarity alone.

Record producer, operation, time, supplied inputs/sources, decision/output, omissions/rejections/failures/unknowns and reasons, unchosen alternatives, remaining uncertainty, record connections, and every actual use. A use event identifies the record, consumer, purpose, contributing output/decision, outcome, unused alternatives/reasons, and uncertainty. Do not rewrite an earlier record to add later use.

Recursive self-examination runs when current context, a genuine system purpose, a design rule, an anomaly, Ness's question, or another authorized trigger requires it. Go only as deep as that purpose needs, without a fixed maximum. Record trigger, examined records, findings, result use, uncertainty, and connections. This is distinct from automatically logging the act of logging.

## Reading queue

- Support one worker and one job at a time. Hold an exclusive OS job lock throughout processing. Expiry timestamps are not concurrency authority.
- After durable root append, enqueue once under `stable_hash(root_id + "reading_job_v1")` through the shared locked append/flush boundary. Release enqueue lock before reading work.
- Startup reconciles only the authorized eligible root set. Never silently enqueue all historical roots.
- Commit the immutable pass instruction before retrieval. Keep attempts and terminal lifecycle events separate.
- Use `stable_hash(enqueue_key + "reading_v1")` as the reading's idempotency key. Keep pass identity as provenance, not duplicate identity. Recovery finds an existing reading before writing.
- Preserve sequential retrieval, proposal, acceptance, quarantine write, clash/view processing, and job close. Check claim authority before protected writes.
- Commit explicit no-clash/no-update sentinels. Absence is not a negative result.
- Recover incomplete crash work only. Completed/failed jobs and handled technical failures do not enter automatic crash replay. Holds, privacy refusal, and indeterminate work block admission.
- Nightly activation durably records each trigger, admits one activation run, and processes only existing eligible jobs. Preserve separate request, configuration, run, and disposition records. No silent historical backfill.

## Promotion and evaluation

- Quarantine never silently becomes production input. B16 promotion resolves exact reading/evaluation identities and freezes complete evidence before reservation and commit fences.
- Evaluation distinguishes machine completeness, independent assessment, Ness's actual judgment, and authority proof. A model or annotator name cannot stand in for judgment authority.
- Lookup prior commitment, admit one reservation, verify current prerequisites, commit at most one eligibility record, and record the parent outcome before acknowledgment.
- Promotion machinery neither judges content nor creates/writes the production store. Production activation remains separately gated.
- Preserve sealed gold identities and trial provenance. Missing source cases, unresolved reviewer independence, unknown scoring rules, or unchosen judgment authorization cannot be fabricated into passing evidence.

## Authority verification

AIC verifies artifact identity and recorded authority. It does not create authority, repair artifacts, choose a winner between contradictory governing records, or replace runtime access checks.

- Derive status from explicit adoption/acceptance evidence, not filename, placement, date, or an embedded historical header.
- Establish shared work, enumerate the governing set, recompute member identities and status evidence, revalidate authority order/rules, then seal a content-bound verification generation.
- Commit one outcome per fully sealed generation before its terminal. A family lookup key does not own a generation's outcome lock.
- Reuse requires checking the complete current input basis again. Cached summaries, elapsed time, and remembered hashes are not freshness proof.
- Distinguish inability to inspect from determinate absence or contradiction. Unfinished work does not become an artifact refusal merely because retries ran out.
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
- Separate fetch, text-only synthesis, and create-space/review contexts. Synthesis cannot call tools, read files, or make network requests. Treat fetched instructions as untrusted source data.
- No research stage writes directly to roots, readings, creations, or production. All accepted intake uses the normal shared path and permissions.
- Preserve relevant plain text and an inert full-page PNG with provenance, time, reference, and integrity hash. Isolate page rendering separately. Store no active HTML, scripts, cookies, or sessions.
- The screenshot supports human review, not reasoning or embeddings. If unavailable, retain verified text/metadata and failure reason. Do not discard or lower textual confidence solely for a missing screenshot.
- Auto-reject flagged material but never silently delete it. The rejected-bin view uses escaped text, inactive URLs, stripped spoofing characters, no previews/network fetches, and disabled copy/select. Those UI restrictions are not a security boundary.
- Implement a query counter and daily spending cap. Automatic currency checks need Ness's approved schedule. Historical 3 AM / 150-cycle / three-search values grant no schedule authority.
- Extract only facts present in at least two of the three raw result sets and add nothing absent from raw data. This is not a vote among models. Source/run identities and content duplicate identities remain separate.
- Commit fetched, preserved, synthesized, gated, and queued/rejected checkpoints. Resume committed progress without fabricating failed stages.
- Image intake preserves metadata, proposes a plain description, proposes contextual meaning, obtains Ness's confirmation, then uses Catalog. Neither machine proposal is a source fact or a substitute for the original image.
- The selected plain-description direction uses detection/segmentation labels, boxes, and confidence rather than a narrating vision-language model. Its trained vocabulary limits coverage. YOLO, Segment-Anything, osam, PaddleOCR-VL, SmolVLM, and Ollama routes are candidates, not installed selections. Keep imported observations and later reactions separate.
- Deferred WhatsApp ingestion stays disabled until its protected mechanics are accepted/integrated and Ness authorizes use. A design record alone cannot authorize decryption or ingestion.
