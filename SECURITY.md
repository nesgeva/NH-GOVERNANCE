# Privacy, access, and action

Protection rules constrain every component and output channel.

## Privacy

- Ness's authorized private access is open by default. Sensitive, medical, emotional, or uncomfortable subject matter alone does not justify blocking or softening truthful understanding.
- External exposure and secondary use are restricted by default. Storage permission is not interpretation, disclosure, sharing, or action permission.
- Keep sensitivity levels separate from protected-handling tiers. Level-1 protected raw content and its physical paths stay outside ordinary components and logs. Use opaque references.
- Capture exclusion sends excluded raw material to separate sealed protected storage. Ordinary Catalog, TSC, memory, and archives retain only permitted remainder and non-reconstructive exclusion metadata. Protected preservation is not destruction.
- Non-negotiable live credentials and secrets require protected handling. Do not make all sensitive personal material automatically excluded.
- Keep exclusion, sealed isolation, hiding, restriction, redaction, and deletion from ordinary visibility distinct. Internal influence removal is separate. Hiding or deleting from view does not destroy originals or stop internal influence.
- Explicit influence removal names scope, affected components, and start time. Stop that use from the enforcement commit. Never infer broader scope from a topic pause.
- Understand natural instructions. A clear reopening needs no repeated confirmation. Do not silently restore a paused topic.
- Visible deletion includes direct and indirect traces and safely rebuilt derivatives. Verify every relevant surface before claiming completion. Preserve honest partial, failed, or unknown outcomes and a content-free record of what occurred.
- Master-21's visibility-removal outcomes are `protected_complete`, `protected_with_declared_limits`, `incomplete`, `blocked`, and `failed`. Do not reuse older destructive-deletion wording. Report remaining traces, unverified locations, limits, and possible further action where incomplete.
- During scoped hiding, verified surfaces retain their result; unverified surfaces withhold. History and expanded views cannot bypass privacy.
- Third-party speech stays attributed. Separate actual words/actions, Ness's interpretation, and N.H's interpretation. Do not infer private states as facts, build fixed psychological profiles, or treat closeness as disclosure permission.

## Modes and speaker access

Effective permission is the intersection of deliberate mode, privacy, current SACL ceiling, and applicable BAI authority. The strictest applicable rule wins.

- Dry Mode cannot reach Personal stores through code. UI appearance alone is insufficient separation.
- Personal Mode requires deliberate opening, a PIN or purpose-bound biometric proof, current owner checks, committed activation records, and release of the delivery fence before private retrieval.
- Recognition alone does not open Personal Mode. Opening does not grant top-security. Step-up remains a separate authority.
- Mode states are `dry`, `personal_opening`, `personal_active`, `personal_suspended`, `personal_closing`, and `personal_closed`.
- Bind access to runtime epoch and generation. At most one live/nonterminal session exists per boundary. Restart creates a new epoch and starts Dry. Never restore sessions, raw factors, prior recognition, tokens, leases, or dead-epoch output from history.
- On access reduction, stop new forbidden retrieval and discard affected output before delivery. Preserve independently authorized work and durable records. Resume surviving work only under current bindings.
- Closing immediately blocks private retrieval and delivery, releases transient buffers, and requests any separate authority ending through its actual owner. Indicators follow committed state and grant no authority.

SIA assesses each speaker stream independently. SACL decides access. BAI supplies purpose-bound biometric proof. None may diagnose wellbeing or borrow another's authority.

Access levels are `guest`, `known_person`, `recognized_ness`, and `top_security`.

- Guests get natural responses from permitted material without clues that hidden material exists.
- Known people receive only their current Person-Box permission categories and required Ness-presence conditions. One person's permission never transfers to another. Other people cannot change N.H memory, behavior, permissions, security, or authority.
- Keep each parent as a separate identity. Parent translation follows Ness's request. Private wording help does not authorize speaking to the parent or intervening in the conversation.
- Shared or observable output uses the minimum access of active streams. Use an individual's ceiling only on an owner-confirmed private, unobservable path. Personal Mode alone cannot make a shared channel private.
- SACL continuously recalculates access on speaker changes, uncertainty, stale assessments, and security events. Check categories and presence again at output time.
- Voice is a soft factor, not a hard lockout or sole identity proof. Identity uncertainty cannot increase access.
- Acoustic spoofing and behavioral `imitation_risk` are separate. Spoofing triggers the stream's guest/alert path and top-security relock. Behavioral divergence does not remove ordinary recognized-Ness access under Option A; it blocks top-security where specified.
- Wellbeing tiers, appointment anchors, emotional readings, and behavioral divergence are not identity or access evidence.

## Biometrics and owner recovery

- The OS owns raw biometrics. BAI receives results, never fingerprint images/templates. Bind purpose and requester before prompting. Keep one pending request with a random challenge and trusted local expiry.
- On matched success, issue either an exact one-time token or a revocable top-security lease. Tokens are consumed once before the protected effect. Leases support repeated checks until revoked or expired.
- Reject expired, mismatched, malformed, delayed, duplicated, or already resolved results. Do not retry a failed biometric prompt automatically. Clear volatile authority on restart.
- Top-security needs both current SACL Gate 1 and a live compatible BAI lease. Voice alone, biometric success alone, or old recorded proof is insufficient.
- Separate keys by token purpose. Keep hardware-backed manifest-signing and rollback-sealing keys independent and nonexportable.
- BOP records only the physical prompt/result event. Tokens, purposes, challenges, consumption, and security consequences belong to security audit.

Initial pairing progresses through QR available, provisional pairing with the QR permanently inert, recovery setup, and finalized owner setup. Never regenerate the used QR or treat scanning as final trust.

Normal recovery codes appear only on the paired phone. Verify the Bitwarden save and local acceptance before activating a new code; then invalidate the old code and seal the local copy. Do not expose code values on the desktop or clipboard, or retain save-check inputs/results.

Replacement requires the normal recovery code and local thumbprint. Fully verify the new phone before revoking the old one, then rotate recovery material. Emergency recovery is local, provisional until its required preparation completes, and atomic across new trust, old revocations, old-material invalidation, and new-material activation. It grants no code or configuration editing authority.

## Voice enrollment

- Enrollment starts through explicit Ness action. Reserve one operation/session and recheck all six owner prerequisites before prompting and immediately before consuming `voice_enrollment_ness` authorization.
- Prerequisites are final owner-phone trust, completed first-code setup, permanently inert initial pairing material, finalized setup, clean current spoofing status, and Ness's confirmed Person-Box.
- Flush and verify consumption proof before opening the session. Open durably before microphone capture. B29 owns capture; BOP owns actual observations.
- Stop capture before logging a protective stop. Preserve committed observations without reconstructing gaps or automatically reopening the microphone.
- Close capture before sending observations through Catalog, B11, the standard queue, and quarantine. Failed profile eligibility does not erase roots.
- Profile eligibility requires a consistent live stream, no medium-or-higher spoofing, no unresolved overlap, allowed completeness, valid authorization, and full-segment integrity. Count each eligible reading once.
- Propose the provisional Person-Box link before SIA profile creation. Person-Boxes commit their own link; acknowledgment is not commitment. SIA owns profile creation.
- Authorized enrollment provenance does not identify the voice as Ness, grant recognized-Ness/top-security, open Personal Mode, or authorize actions.

## Session caches

TSC organizes Catalog pre-ingest material, not a second memory. Hold every contribution, N.H output, and BOP capture under `pending_fingerprint_authorization`. Keep raw payloads out of the structural database.

- One owning process writes each session. Use transactions, uniqueness, foreign keys, and one monotonic contribution/output ordering allocator.
- Keep participant streams, capture-time attribution, certainty, branch links, source references, and content hashes. Later assessments append beside capture-time facts; they do not upgrade them retrospectively.
- Normal closure seals the session. A crash preserves committed material and marks it interrupted. A continuation is a new linked session, never a reopened or merged capture.
- Sealed sessions wait indefinitely. No expiry, deletion, automatic promotion, or human inspection. The old inspection-token design is superseded.
- One session-specific `tsc_promotion:<session_id>` token plus current recognized-Ness SACL confirmation authorizes the whole session. Serialize claim, consumption, and durable receipt before the atomic authorization transition. A claim alone grants nothing.
- After authorization, promotion proceeds automatically through Catalog/B11. Other blockers remain independent. Resolving a speaker blocker does not require another fingerprint.
- Preserve real chronology, submit children only after parent roots exist, and interleave BOP observations by event time. Absorb already-promoted captures by stable identity.
- Do not claim complete promotion or archive while any item remains blocked. Pause on lost security; resume valid authorized work only after fresh checks. Recover proof from durable receipts, not vanished BAI state.
- Excluded raw content goes to separate protected storage, never ordinary TSC or its archive. Another speaker's request does not override Ness's capture authority or the governing privacy rules.
- Verify an encrypted safety snapshot, commit archive state, and freeze the database/snapshot. Later permanent sealing needs separate authorization and external append-only control history.
- Archives support bounded machine integrity and recovery only. No ordinary LMAC, Meaning Engine, Person-Box, retrieval, human inspection, or resubmission path. They add no evidence weight.

## Visible delivery

1. Before retrieval and generation, restrict inputs to the authorized intersection for the actual purpose and audience.
2. Review the exact immutable output under privacy rules.
3. Check SACL/PBR access on that same version.
4. Recheck current owners, mode epoch/generation, authority, and delivery fence immediately before effect commitment.
5. Deliver at most once and record the actual outcome.

Any changed binding invalidates the old pass. Access reduction discards affected undelivered output. Do not reveal hidden existence through refusals, gaps, logs, or error wording.

An unknown delivery is unresolved, never proof of withholding or success. Resolve the owner's actual outcome before any retry. Do not blindly resend, replay a withheld draft, or bypass the chain through voice, diagnostics, debugging, or another channel.

## Actions

Keep suggestion, preparation, approval, attempt, outside effect, observed result, interpretation, and correction as separate linked records. Approval is not execution or proof that the reasoning is true.

- Track current stage/current level separately from prospective risk and remaining requirements. The four authority levels and heightened categories remain distinct.
- Levels are internal read-only, internal append-only write, prepared external action, and executed external action. Heightened categories include medical, legal, financial, privacy-sensitive, relationship-affecting, destructive, and irreversible actions.
- Suggestions may use derived-possibility language. Do not tell Ness what he must do. A gentle question may be asked once; rejection, ignoring, or no reply closes that topic until Ness personally reopens it.
- Response states are `accepted and acted on`, `rejected`, `modified`, `postponed`, `ignored`, and `alternative requested`. None is resistance or failure by Ness.
- Strong evidence never grants permission. Permission never supplies evidence. Higher-impact possibilities need stronger review.
- Execution needs exact recorded approval or an explicitly bounded recurring grant. Similar past actions, broad settings, silence, and preparation cannot substitute.
- Heightened categories require per-instance confirmation even under standing authority and even when reversible.
- Preview actual effects, boundaries, uncertainty, and required approval. Stop on unclear, stale, changed, or revoked authority.
- If authority is violated, stop related autonomous work and further chain steps, record honestly, and show the incident. A corrective world action needs its own preview and approval.
- A preauthorized emergency stop may prevent additional effects. It does not authorize recalling messages, changing external data, contacting people, or reversing completed effects.
- Never retry an uncertain external effect to repair a missing acknowledgment.

Result inputs distinguish Ness-reported outcomes from automatically detected possible links. Keep action, result event, and proposed connection separate. Ness may confirm, reject, modify, dispute, or leave a link unresolved. A confirmed link is not causal proof.

Result states are success, partial success, failure, cancellation, no/unknown result, and incorrect/disputed linkage. A result may trigger another owner's designed review, never automatic action repetition. Ness may disable or restrict automatic detection.

## Protected maintenance

BGMM opens a local, purpose-bound, exact-file maintenance window with its required factors. Ordinary editors, scripts, installers, terminal privilege, or remote entry do not grant protected access. It resists tampering; do not promise physical impossibility.

- Persist the structural change log and encrypted full-content rollback package before touching a file.
- Apply only the declared change, record hashes, update/sign the manifest, sign changed executables, and record completion.
- Keep signing and rollback keys separate. Preserve earlier manifests and encrypted rollback packages.
- Relock/revoke immediately on any required trigger. Roll back a partial change from verified exact bytes and metadata.
- Startup verifies secure/measured boot, signatures, and hashes. A bounded worker restores only listed prior files and manifest before N.H starts. Recovery is idempotent and works offline.
- Never use maintenance to rewrite immutable memory, reveal protected content, preserve active authority across restart, or expand emergency recovery into code editing.
