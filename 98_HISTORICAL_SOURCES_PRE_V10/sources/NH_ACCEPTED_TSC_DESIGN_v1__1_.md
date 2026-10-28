# Temporary Session Cache (TSC) — Final Accepted Design

## Provenance

This file is the standalone project record of the complete accepted 31-section
Temporary Session Cache (TSC) detailed design for the N.H system. The design was
produced through iterative correction and explicit acceptance by Ness in the
Claude project chat (security/identity/BGMM/TSC design branch). All superseded
drafts and rejected wording have been removed. Only the final corrected accepted
text is preserved here.

This file is a **companion record**, not an authoritative source. It does not
replace, supersede, or modify the N.H Master (`NH_MASTER-19_CORRECTED_v6.md`),
the Decision Defaults (`NH_DECISION_DEFAULTS-S19_v1__1_.md`), or any
implementation file. The TSC design must be formally patched into the Master
through the accepted patch-only, no-loss protocol before it carries Master
authority.

Related companion file: `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
preserves the earlier accepted TSC foundation and the related security/identity
designs (BOP, SIA, SACL, BAI, BGMM, phone pairing, recovery, enrollment) that
the TSC depends on.

---

## Status

**ACCEPTED DESIGN — NOT YET BUILT**

No code written. No disk verification claimed. All 31 sections below are
accepted and complete.

---

## Contents

1. What TSC Is and Is Not
2. Relationship to §7E
3. Transactional Database Model
4. Session Record Schema
5. Contribution Record Schema
6. Participant and Speaker-Attribution Record Schema
7. Attribution Certainty and Unresolved-Speaker Handling
8. Conversation-Order and Branch-Link Schema
9. BOP and SIA Event-Link Handling
10. N.H Output Preservation
11. Blocker Schema and Blocker-Resolution History
12. Session Lifecycle and Item-Level Lifecycle
13. Normal Session Close and Sealing
14. Interrupted-Session Sealing and Linked Continuation Caches
15. Private Ness Inspection Without Promotion
16. Fingerprint Authorization Through BAI and SACL
17. Exact Promotion Sequence
18. Dependency Handling While Preserving Real Conversation Order
19. Partial Promotion and Idempotency
20. Automatic Retry Rules
21. Multi-Person Session Handling
22. Ness's Own Material Inside a Third-Party Session
23. Post-Promotion Retained Safety Archive
24. Protection Against Duplicate Use or Double Weighting
25. Privacy, Exclusion, Restriction, Deletion, and Third-Party Handling
26. Security Audit Events
27. Startup Recovery and Crash Recovery
28. Fail-Closed Behavior
29. Integration Boundaries
30. Explicit Prohibited Behaviors
31. Status

---

---

### 1. What TSC Is and Is Not

The Temporary Session Cache is a structured, transactional extension of §7E's
unified pre-ingest holding area. It is not a separate upstream system. It holds
session material in the §7E pre-ingest store, with TSC-specific organization
layered inside that same holding area, until Ness authorizes it to progress
through the standard §7E → sealed store path.

**TSC is:**
- An organized holding mode within §7E's unified pre-ingest store.
- A transactional local store for the TSC-specific structural records (session,
  contribution, participant, branch, blocker, and lifecycle tables) that support
  the richer session context §7E's flat per-item structure does not natively
  express.
- A complete faithful record of what happened in one real conversation session,
  held under §7E's rules.
- A provenance boundary that ensures third-party material undergoes the full
  §7E → §7G path before it can influence any N.H output.

**TSC is not:**
- A separate system that sits upstream of §7E and later submits into another
  waiting area.
- A second long-term memory system.
- A second Meaning Engine.
- A semantic interpretation store.
- A bypass around §7E, `append_root()`, or any other write boundary.
- A second independent route into readings, Person-Boxes, or Computed View.
- A place where third-party statements become facts about Ness.
- A system that performs identity fusion or merges speakers.

**The correct picture:** every TSC item exists in the §7E pre-ingest store from
the moment it is captured, carrying the `"pending_fingerprint_authorization"`
blocker. The TSC structural database holds the session-level organization —
conversation order, speaker attribution, branches, BOP event links, SIA event
links — that makes it possible to understand, navigate, and correctly promote
those §7E pre-ingest records. The TSC database and the §7E pre-ingest store are
two aspects of one holding system, not two stacked caches.

---

### 2. Relationship to §7E

The TSC is an extension of §7E's unified pre-ingest holding area. It adds one
new blocker type and one new organizational layer. It does not add a separate
upstream cache.

**The single blocker added:** `"pending_fingerprint_authorization"`. Every TSC
item enters the §7E pre-ingest store carrying this blocker alongside any other
applicable blockers (e.g., `"speaker_unresolved"`, `"thread_unresolved"`). The
blocker rules from §7E apply: held material is invisible to the Meaning Engine;
one blocked item never blocks unrelated ready items; silent deletion is never
permitted; material may remain held indefinitely.

**What the TSC structural database adds:** §7E's conceptual pre-ingest record
shape stores `capture_id`, raw payload, capture timestamp, front-door type,
source metadata, proposed catalog fields, blocker list, resolution history,
lifecycle state, and `root_id` if promoted. This is sufficient for the §7E
holding and promotion path. The TSC adds, alongside these per-item §7E records,
a set of relational tables that capture: session identity; conversation order
(`sequence_position`); participant and speaker-stream identity; attribution
assessments and certainty; branch and reply relationships; links to BOP
observation roots held in the same pre-ingest store; links to SIA assessment
events in the security audit log; N.H outputs; and per-item blocker and
lifecycle history. These tables exist only to organize the §7E pre-ingest
records as a coherent session — they do not replace, duplicate, or bypass those
records.

**All items in one place:** both conversation contributions and BOP observation
roots from the session sit in the §7E pre-ingest store, held under
`"pending_fingerprint_authorization"`. They do not enter the sealed long-term
root store while authorization is pending. The TSC structural database holds
the references and organizational context. It does not hold the raw payloads
— those are in the §7E pre-ingest records.

**Promotion from TSC to sealed store:** when the
`"pending_fingerprint_authorization"` blocker is lifted (after fingerprint
authorization), items with no remaining blockers progress through the normal
§7E lifecycle: `held` → `ready` → `promoting` → `promoted`, terminating in
`append_root()`. The TSC structural database tracks which items have been
promoted and records the resulting `root_id`. After promotion, the §7E
pre-ingest record remains as provenance per the settled §7E rule.

---

### 3. Transactional Database Model

The TSC uses a local transactional database for its structural organizational
records. The choice of specific technology (SQLite, embedded key-value store
with transaction support, or equivalent) is a build-time decision. The
architectural requirement is: ACID transactions, crash-safe writes, local-only
operation, and no network dependency.

This database stores session-level organization. It does not store raw payloads
— those remain in the §7E pre-ingest store. It does not perform semantic
interpretation. It does not produce readings.

**Database tables (logical schema):**
1. `sessions` — one row per TSC session
2. `contributions` — one row per conversation contribution
3. `participants` — one row per detected participant stream
4. `attribution_assessments` — one row per speaker attribution event
5. `branch_links` — one row per reply/branch relationship
6. `bop_preingest_links` — one row per BOP observation root in the §7E
   pre-ingest store, linked to the session or a specific contribution
7. `sia_event_links` — one row per SIA assessment event linked to a
   contribution moment
8. `nh_outputs` — one row per N.H response or output within the session
9. `blockers` — one row per active or resolved blocker per item
10. `blocker_history` — append-only resolution history for each blocker
11. `lifecycle_events` — append-only lifecycle state log for the session
12. `promotion_state` — one row per item tracking promotion progress
13. `security_audit_refs` — references to security audit log entries from
    TSC operations

---

### 4. Session Record Schema

```
sessions table
  session_id              uuid4
  session_mode            "voice" | "text" | "mixed"
  started_at              timestamp
  sealed_at               timestamp or null
  authorized_at           timestamp or null
  promotion_started_at    timestamp or null
  promotion_completed_at  timestamp or null
  lifecycle_status        "active" | "sealed" | "authorized" | "promoting" |
                          "promoted" | "promotion_failed" | "interrupted"
  continuation_of_session_id  uuid4 or null
  interruption_recorded   boolean
  bai_token_id            uuid4 or null
  sacl_recognized_ness_confirmed_at  timestamp or null
  tsc_schema_version      "tsc_v1"
  notes                   string or null
```

---

### 5. Contribution Record Schema

One record per natural conversation contribution. The `sequence_position` and
all session-context fields are stored in the TSC structural database and in
the §7E pre-ingest record's `source_metadata` field. They are not added as new
fields to the sealed seven-field root schema.

```
contributions table
  contribution_id         uuid4
  session_id              foreign key
  sequence_position       integer — ordinal position within this session;
                          1-based; set at capture time; never changed
  occurred_at             timestamp
  duration_ms             integer or null
  contributor_stream_id   foreign key → participants.stream_id
  role                    "ness" | "participant" | "nh_output" | "unknown"
  content_type            "voice" | "text" | "nh_text" | "nh_voice" | "other"
  preingest_capture_id    uuid4 — the capture_id of this contribution's
                          §7E pre-ingest record; the link between the TSC
                          structural record and the §7E holding-area record
  word_count              integer or null
  character_count         integer or null
  reply_to_contribution_id uuid4 or null
  branch_level            integer
  item_lifecycle_status   "held" | "ready" | "promoting" | "promoted" |
                          "excluded" | "blocked"
  promoted_root_id        uuid4 or null
  exclusion_metadata      JSON or null — non-reconstructive metadata
                          describing the type of exclusion; no excluded
                          content
  content_hash            SHA-256 of raw_content at capture time
```

**On session-context metadata and the seven-field root schema:** the
`sequence_position`, `occurred_at`, `contributor_stream_id`, branch
relationship, and session identity are stored in the TSC structural database
and in the §7E pre-ingest record's `source_metadata` field. They flow through
to the sealed root via the `source_metadata` provenance fields that §7E already
carries in its conceptual record shape. They are not added as new fields to the
sealed root's seven-field schema (id, subject, timestamp, content, re_reads,
source_title, role). If a future schema version is needed to carry additional
session provenance directly in the root, that is a future schema dependency —
it is not silently applied here. The current seven-field schema is unchanged.

**Ness's own contributions:** `role = "ness"`, preserved in the TSC and the
§7E pre-ingest store with the same `"pending_fingerprint_authorization"` blocker
as other items. They are not excluded from the session context. They proceed
through the same promotion path.

---

### 6. Participant and Speaker-Attribution Record Schema

```
participants table
  stream_id               uuid4
  session_id              foreign key
  first_seen_at           timestamp
  last_seen_at            timestamp
  declared_role           "ness" | "third_party" | "unknown"
  assessed_person_box_id  uuid4 or null
  assessed_certainty      float [0.0, 1.0] or null
  identity_status         "confirmed_known" | "assessed_probable" |
                          "unresolved" | "below_threshold" | "unknown"
  permission_boundary_record_version  integer or null
  sia_stream_id_ref       uuid4 or null
```

---

### 7. Attribution Certainty and Unresolved-Speaker Handling

Attribution certainty is recorded at the moment of capture and never upgraded
retrospectively within the TSC.

```
attribution_assessments table
  assessment_id           uuid4
  session_id              foreign key
  stream_id               foreign key
  contribution_id         foreign key or null
  assessed_at             timestamp
  assessed_person_box_id  uuid4 or null
  assessed_certainty      float [0.0, 1.0]
  certainty_dimensions    JSON object
  uncertainty_flags       JSON array
  anti_spoofing_suspicion_level  "none" | "low" | "medium" | "high"
  sia_assessment_event_id uuid4
```

**Unresolved-speaker handling:** a contribution whose speaker cannot be
confirmed from source carries `item_lifecycle_status = "blocked"` and two
blockers: `"pending_fingerprint_authorization"` and `"speaker_unresolved"`.
The `"pending_fingerprint_authorization"` blocker is lifted by the
authorization event. The `"speaker_unresolved"` blocker remains and must be
resolved through the §7E speaker-resolution rule before the item can proceed
to `append_root()`. This resolution does not require a new fingerprint — the
authorization covers the session. It does not require manual Ness selection of
an identity — the §7E rule governs resolution. No item with `"speaker_unresolved"`
outstanding is ever promoted. No root is ever written with `role = "unknown"`.

---

### 8. Conversation-Order and Branch-Link Schema

```
branch_links table
  link_id                 uuid4
  session_id              foreign key
  child_contribution_id   foreign key
  parent_contribution_id  foreign key or null
  link_type               "direct_reply" | "continuation" | "interruption" |
                          "branch_open" | "branch_close" | "context_reference"
  confidence              "certain" | "inferred" | "uncertain"
  confidence_basis        string
```

`sequence_position` establishes total chronological order. Branch links express
reply structure without changing the chronological record. The parent-before-child
promotion dependency is enforced: a parent's `promoted_root_id` must be set
before its child is submitted to §7E. Branch and reply context is preserved in
the §7E pre-ingest record's `source_metadata` — not as new fields in the sealed
root schema.

---

### 9. BOP and SIA Event-Link Handling

BOP observation roots generated during a TSC session are held in the §7E
pre-ingest store under `"pending_fingerprint_authorization"` alongside the
conversation contributions. They do not enter the sealed long-term root store
while authorization is pending. The TSC structural database links to them by
their `preingest_capture_id` — the same identifier that exists in the §7E
pre-ingest record.

```
bop_preingest_links table
  link_id                 uuid4
  session_id              foreign key
  bop_preingest_capture_id uuid4 — the capture_id of the BOP observation
                          root's §7E pre-ingest record; this root is HELD
                          in §7E pre-ingest, not yet in the sealed store
  linked_contribution_id  uuid4 or null
  occurred_at             timestamp
  event_type              string — the BOP event_type for reference
  relationship_type       "concurrent" | "precedes_contribution" |
                          "follows_contribution" | "session_level"
```

After fingerprint authorization and promotion, BOP roots proceed through §7E
to the sealed store alongside the conversation contributions, in the real event
order. Their timing relationship to conversation moments is preserved in the
§7E pre-ingest record's `source_metadata`, which flows into the sealed root as
provenance. This is not carried as new fields in the sealed seven-field root
schema.

```
sia_event_links table
  link_id                 uuid4
  session_id              foreign key
  sia_assessment_event_id uuid4 — in the security audit log; not held
                          in §7E; SIA assessment events are not promoted
                          as roots
  linked_contribution_id  uuid4 or null
  assessed_at             timestamp
  relationship_type       "assessment_at_contribution" | "session_level" |
                          "between_contributions"
```

SIA assessment events remain in the security audit log throughout. They are
not promoted as roots. Their timing relationship to contributions is preserved
through the `sia_event_links` table and through the `source_metadata` provenance
on relevant promoted roots.

---

### 10. N.H Output Preservation

```
nh_outputs table
  output_id               uuid4
  session_id              foreign key
  sequence_position       integer — interleaved with contributions in the
                          full session order
  produced_at             timestamp
  output_type             "text_response" | "voice_response" | "action_result" |
                          "translation_output" | "system_message"
  addressed_to_stream_id  uuid4 or null
  access_level_at_output  "top_security" | "recognized_ness" |
                          "known_person" | "guest"
  preingest_capture_id    uuid4 — the capture_id of this output's §7E
                          pre-ingest record; held under
                          "pending_fingerprint_authorization"
  item_lifecycle_status   "held" | "ready" | "promoting" | "promoted" |
                          "excluded"
  promoted_root_id        uuid4 or null
```

N.H outputs are promoted as roots with `role = "nh"`. Their session context is
preserved in the §7E pre-ingest record's `source_metadata`. No new fields are
added to the sealed seven-field root schema.

---

### 11. Blocker Schema and Blocker-Resolution History

```
blockers table
  blocker_id              uuid4
  session_id              foreign key
  item_id                 uuid4
  item_type               "contribution" | "nh_output" | "bop_root" | "session"
  blocker_type            "pending_fingerprint_authorization" |
                          "speaker_unresolved" | "content_under_review" |
                          "technical_hold"
  added_at                timestamp
  status                  "active" | "resolved" | "waived_by_exclusion"
  resolved_at             timestamp or null
  resolution_method       string or null
  resolution_event_ref    uuid4 or null
```

```
blocker_history table
  history_id              uuid4
  blocker_id              foreign key
  event_type              "blocker_added" | "blocker_resolved" |
                          "resolution_attempt_failed" | "blocker_waived"
  event_at                timestamp
  event_detail            string
  event_ref               uuid4 or null
```

`"speaker_unresolved"` is an additive blocker for contributions where speaker
cannot be confirmed. It does not resolve through TSC logic — it resolves through
§7E's speaker-resolution rule.

---

### 12. Session Lifecycle and Item-Level Lifecycle

**Session-level lifecycle:**
`active` → `sealed` or `interrupted` → `authorized` → `promoting` → `promoted`
or `promotion_failed`

**Item-level lifecycle:**
`held` → `ready` → `promoting` → `promoted` or `excluded` or `blocked`

No item proceeds from `blocked` to `promoting` while `"speaker_unresolved"` is
active. No item ever reaches `promoted` with an unresolved speaker.

---

### 13. Normal Session Close and Sealing

On normal session close: BOP `session_closed` pre-ingest record created and
linked; TSC session `lifecycle_status` → `"sealed"`, `sealed_at` = now; all
items confirmed `"held"` or `"blocked"`; `cache_sealed` security audit event
written immediately; TSC database transaction commits; session is immutable from
this moment.

The sealed TSC waits indefinitely. No auto-expiry. No auto-deletion.
No auto-promotion.

---

### 14. Interrupted-Session Sealing and Linked Continuation Caches

On crash: restart detects `"active"` session; `lifecycle_status` →
`"interrupted"`; `sealed_at` = restart timestamp; all material successfully
written before crash preserved exactly; nothing reconstructed; `cache_sealed`
written with `"interrupted_crash"` reason; session is sealed.

Continuation: new TSC with new `session_id`;
`continuation_of_session_id` = interrupted session's `session_id`; two sessions
remain separate immutable units; continuation relationship preserved; both
authorized and promoted separately.

---

### 15. Private Ness Inspection Without Promotion

**Settled decision:** private read-only inspection of a sealed TSC requires
fingerprint authorization through BAI, using a separate purpose-bound inspection
authorization. Inspection authorization is entirely independent of promotion
authorization — consuming an inspection token does not affect, consume, or create
any promotion token, and holding a promotion token does not provide inspection
access.

**Inspection authorization mechanism:**

Inspection uses a dedicated BAI `one_time_authorization_token` with purpose
`"tsc_inspection:<session_id>"`. This purpose is formally adopted into the BAI
purpose vocabulary following the same extension mechanism as other BAI purposes.
It follows all BAI token lifecycle rules: single-use, short-lived, purpose-bound,
delivered only to the requesting component, audited immediately.

The `"tsc_inspection:<session_id>"` token and the `"tsc_promotion:<session_id>"`
token are entirely separate artifacts. One cannot substitute for the other. They
may coexist without either affecting the other.

**What inspection shows:** the complete conversation as preserved in the TSC
structural database — all contributions in sequence order, participant attribution
with certainty scores, N.H outputs, BOP pre-ingest link references with timing,
SIA event link references, and blocker status. Inspection is read-only. It does
not pass through the Meaning Engine.

**What inspection explicitly does not do:**
- Consume or affect the promotion token.
- Change the session's `lifecycle_status`.
- Lift the `"pending_fingerprint_authorization"` blocker on any item.
- Begin or imply promotion.
- Expose material to §7G, §7J, §7M, §7L, or any downstream operational
  component.
- Count as Ness's approval of content.
- Make held material available to LMAC, §7F, or the reading queue.

**SACL condition:** inspection requires the current session to hold a
recognized-Ness assessment at the moment the inspection token is consumed,
following the same two-condition pattern as promotion authorization (BAI token
+ SACL recognized-Ness confirmation). This ensures a non-Ness speaker cannot
trigger inspection during a session where Ness's identity is not confirmed. The
SACL check for inspection is independent of any SACL check for promotion.

---

### 16. Fingerprint Authorization Through BAI and SACL

Promotion requires both conditions simultaneously at token consumption:

**Condition 1 — BAI `one_time_authorization_token`** with purpose
`"tsc_promotion:<session_id>"`.

**Condition 2 — SACL recognized-Ness session** confirmed fresh and non-stale
at consume time.

If either condition is not met: token not consumed; `bai_token_consume_blocked`
written; session remains `"sealed"`.

After successful authorization: token consumed; `bai_token_consumed` written;
session `lifecycle_status` → `"authorized"`; `authorized_at` = now;
`sacl_recognized_ness_confirmed_at` = SACL confirmation timestamp;
`cache_authorization_received` written; promotion begins automatically. No
additional manual Ness action is required after this point.

---

### 17. Exact Promotion Sequence

**Phase 1 — Pre-promotion check:**
1. Verify TSC session `lifecycle_status = "authorized"`.
2. Verify BAI and SACL conditions remain valid (not stale).
3. Apply §7Q privacy and exclusion rules to each item (see section 25).
4. Items that fall under §7Q exclusions: `item_lifecycle_status` →
   `"excluded"`; non-reconstructive exclusion metadata recorded; raw content
   replaced with exclusion metadata; item's §7E pre-ingest record updated;
   item will not proceed to `append_root()`.
5. Items that pass: `item_lifecycle_status` → `"ready"` (if
   `"pending_fingerprint_authorization"` was their only blocker).
6. Items with `"speaker_unresolved"` or other non-fingerprint blockers remain
   `"blocked"`.
7. Session `lifecycle_status` → `"promoting"`; `promotion_started_at` = now;
   `cache_promotion_started` written.

**Phase 2 — Ordered promotion loop (ascending `sequence_position`):**

For each item:

If `"excluded"`: skip; already recorded.

If `"blocked"` (non-fingerprint blocker remains, e.g. `"speaker_unresolved"`):
skip this pass; record in `promotion_state` as pending-blocked; continue. No
second fingerprint required.

If `"ready"`:

1. Idempotency check: if `promoted_root_id` already set → this item was
   promoted in a prior attempt; mark `"promoted"`; continue.
2. Lift the `"pending_fingerprint_authorization"` blocker on the §7E pre-ingest
   record. Write `sequence_position`, `occurred_at`, `contributor_stream_id`,
   `session_id`, branch relationship from the TSC structural database into the
   §7E pre-ingest record's `source_metadata`. These are not added as new fields
   to the sealed root schema.
3. §7E processes the now-unblocked pre-ingest record: validates intake envelope;
   if `"speaker_unresolved"` still active → item stays held, not promoted. If
   all fields resolved → item proceeds to `append_root()`.
4. On `append_root()` success: `promoted_root_id` recorded;
   `item_lifecycle_status` → `"promoted"`; transaction commits.
5. BOP roots held in §7E for this session proceed through the same path in
   their event-order position, interleaved by `occurred_at`.

**Phase 3 — Post-promotion:**

All items are `"promoted"`, `"excluded"`, `"blocked"`, or `"promotion_failed"`.
If none `"promotion_failed"`: session → `"promoted"`; `promotion_completed_at`
= now; `cache_promotion_completed` written; retained safety archive created.
Blocked items remain in `promotion_state` as pending, resuming automatically
when their blockers clear through normal §7E rules — no new fingerprint required.

---

### 18. Dependency Handling While Preserving Real Conversation Order

The promotion sequence follows ascending `sequence_position` as its primary
ordering. One dependency rule overlays this: if a contribution has a
`reply_to_contribution_id`, the parent's `promoted_root_id` must be set before
the child is submitted to §7E. If the parent is blocked, the child's promotion
is deferred to the next retry pass, not skipped permanently. BOP roots promote
interleaved by `occurred_at`. This is the only ordering dependency beyond
chronological sequence.

---

### 19. Partial Promotion and Idempotency

`preingest_capture_id` (stable per item) derives the §7E `capture_id` used as
input to `append_root()`. Any item already in the sealed store is silently
absorbed. No duplication. If promotion is interrupted, the loop picks up from
the first item not yet `"promoted"`, `"excluded"`, or `"blocked"`. Already-
promoted items are skipped via the idempotency check.

---

### 20. Automatic Retry Rules

**A — Automatic continuation of already-authorized interrupted promotion:** if
promotion was interrupted after authorization was already granted, the TSC
process resumes automatically on restart. No new fingerprint required. No new
SACL confirmation required from Ness. Security conditions are checked
automatically before resuming: if SACL no longer reports a recognized-Ness
session, promotion pauses until conditions recover naturally — this is an
automatic check, not a new Ness action.

**B — New promotion authorization:** required only when the session was never
authorized, or when the original BAI token was revoked before promotion began.

**C — Retry of temporary technical failure:** retries specific failed items
automatically after a backoff interval, within a bounded maximum attempt count.
No new authorization required. Security conditions checked automatically before
each retry.

**Ness notification on failure:** a private notice stating that promotion of a
specific session could not complete, with an indication that Ness may authorize
a new attempt when ready. No content is exposed. This is a notification, not a
request for clerk work.

---

### 21. Multi-Person Session Handling

One TSC session per real conversation. Participants are structurally separated
by `stream_id`. Each person has their own `participants` record,
`attribution_assessments`, and `permission_boundary_record_version`. No identity,
certainty, or permission transfers between streams. Full conversation order
preserved in `sequence_position`. The conversation is not split into per-person
sub-caches.

---

### 22. Ness's Own Material Inside a Third-Party Session

Ness's contributions held under `"pending_fingerprint_authorization"` alongside
other items. `role = "ness"`. Same promotion path. Not excluded from session
context. Idempotency prevents duplication if Ness's material was also captured
through the normal live-session path.

---

### 23. Post-Promotion Retained Safety Archive

After all items resolve and `cache_promotion_completed` is written, a frozen
encrypted read-only snapshot of the TSC structural database is created. It
contains structural records and references — not raw content excluded under
§7Q. Excluded items appear only as exclusion metadata.

**What it is for:** integrity checking, verifying what was promoted, recovery
if promoted material is damaged or missing, and explicitly authorized deletion
or audit processes.

**What it is not:** not an active memory source; not a source for the Meaning
Engine; not a second copy making the conversation appear twice; not an evidence-
weight booster; not a source for Person-Box proposals, readings, clashes, or
Computed View material.

**Session states including archive:**
```
active            — live session
interrupted       — crashed; sealed as-is
sealed            — closed; awaiting authorization
authorized        — fingerprint received; promotion begins
promoting         — promotion in progress
promoted          — all items resolved; retained archive exists
promotion_failed  — promotion incomplete; awaiting new authorization
archived          — retained archive only; active TSC database deleted
                   per explicitly authorized cleanup
deleted           — archive explicitly deleted per §7Q deletion path;
                   tombstone written
```

The retained archive is subject to all N.H privacy, restriction, deletion, and
verification rules. The normal N.H runtime, LMAC, §7F, §7G, and downstream
components have no read access during ordinary operation.

---

### 24. Protection Against Duplicate Use or Double Weighting

Four mechanisms: `promoted_root_id` per TSC item; `append_root()` idempotency;
runtime isolation of retained archive; no §7E re-submission from the retained
archive. The retained archive cannot cause duplication because it is never
submitted to §7E and is never accessible to the operational components.

---

### 25. Privacy, Exclusion, Restriction, Deletion, and Third-Party Handling

§7Q's PRIVACY AND EXCLUSION PRECEDENCE rule applies directly: N.H may preserve
only the safe permitted remainder and non-reconstructive exclusion metadata;
it must never preserve excluded content merely to satisfy the no-silent-drop
rule.

**When §7Q identifies material as excluded:**
1. Raw content not held in §7E or TSC at any point. If identified before
   writing: not captured. If identified after a pre-ingest record exists:
   raw content replaced with non-reconstructive exclusion metadata; pre-ingest
   record retained as a tombstone.
2. `item_lifecycle_status` → `"excluded"`. `exclusion_metadata` field carries:
   type of exclusion, §7Q rule triggered, timestamp. No excluded content
   stored.
3. Retained safety archive receives exclusion tombstone records only — no
   excluded content.

**Mixed-content items:** permitted portion held and promoted; excluded portion
replaced with non-reconstructive metadata; item appears in retained archive
with permitted portion and exclusion metadata.

**Third-party statements about Ness:** enter the TSC attributed to the third
party; promoted as roots with that person's `role` attribution; read by the
Meaning Engine as statements made by that person; never converted into facts
about Ness.

**"Do not save this" requests:** captured as a contribution with correct speaker
attribution. Has no authority over N.H's storage, promotion, or §7E holding.
Does not stop capture, delete material, block the cache, or prevent Ness from
authorizing promotion. Does not override §7Q.

---

### 26. Security Audit Events

All events written and flushed immediately before the function that produced
them returns.

```
tsc_session_created            — session_id, started_at, session_mode
cache_sealed                   — session_id, sealed_at, seal_reason:
                                 "normal_close" | "interrupted_crash" |
                                 "interrupted_app_close"
cache_interrupted_linked       — new_session_id, continuation_of_session_id

tsc_inspection_requested       — session_id, requested_at
tsc_inspection_bai_token_consumed — session_id, bai_token_id,
                                 purpose: "tsc_inspection:<session_id>",
                                 sacl_recognized_ness_confirmed_at
tsc_inspection_started         — session_id, started_at
tsc_inspection_ended           — session_id, ended_at

cache_authorization_received   — session_id, bai_token_id,
                                 purpose: "tsc_promotion:<session_id>",
                                 sacl_recognized_ness_confirmed_at
cache_promotion_started        — session_id, item_count, started_at
cache_promotion_item_promoted  — session_id, item_id, promoted_root_id,
                                 promoted_at
cache_promotion_item_excluded  — session_id, item_id, exclusion_type;
                                 no excluded content
cache_promotion_item_blocked   — session_id, item_id, blocker_type
cache_promotion_item_failed    — session_id, item_id, failure_reason
cache_promotion_completed      — session_id, promoted_count, excluded_count,
                                 blocked_count, completed_at
cache_promotion_failed         — session_id, failed_item_count, reason,
                                 failed_at
tsc_retry_started              — session_id, retry_type:
                                 "continuation" | "technical_retry",
                                 attempt_number
tsc_retry_security_paused      — session_id, reason, paused_at
tsc_retry_security_resumed     — session_id, resumed_at
tsc_retained_archive_created   — session_id, archive_location_ref,
                                 created_at
tsc_archive_access_authorized  — session_id, purpose, authorized_at
tsc_archive_deletion_authorized — session_id, authorized_at, authorized_by
tsc_archive_deleted            — session_id, deleted_at,
                                 tombstone_written: true
tsc_duplicate_promotion_prevented — session_id, item_id, existing_root_id
tsc_privacy_exclusion_applied  — session_id, item_id, exclusion_rule,
                                 excluded_at
tsc_ness_private_notice_sent   — session_id, notice_type, sent_at
bai_token_consume_blocked      — session_id, token_purpose, reason
```

Two distinct audit event clusters exist for the two distinct BAI purposes: the
`tsc_inspection_*` cluster for inspection tokens and the
`cache_authorization_received` / `cache_promotion_*` cluster for promotion
tokens. Neither cluster's events affect or imply the other.

---

### 27. Startup Recovery and Crash Recovery

On startup, TSC examines all session databases:

- `lifecycle_status = "active"`: crash during live session. Seal as interrupted.
  Write `cache_sealed` with `"interrupted_crash"`.
- `lifecycle_status = "promoting"`: crash during promotion. Resume automatically
  (section 20, case A). Check security conditions automatically first.
- `lifecycle_status = "authorized"`: crash between authorization and promotion
  start. Begin promotion automatically.
- `lifecycle_status = "sealed"` or `"interrupted"`: no action. Session waits
  for Ness's fingerprint.
- `lifecycle_status = "promoted"` and retained archive exists: normal terminal
  state. No action.
- `lifecycle_status = "promotion_failed"`: Ness has been notified. Awaits new
  authorization attempt.

Transactional database: any uncommitted write is absent; items with
`promoted_root_id` set are safely in the sealed store; promotion loop picks up
from the first item not yet `"promoted"`, `"excluded"`, or `"blocked"`;
idempotency prevents duplication.

---

### 28. Fail-Closed Behavior

- Security condition failure during promotion: promotion pauses; already-promoted
  items remain promoted; retry resumes automatically when conditions recover —
  no new Ness action unless a genuinely new authorization is required (case B
  in section 20).
- Missing or stale SACL at promotion time: promotion does not begin.
- BAI token expired or revoked before consumption: new authorization required.
- TSC database integrity failure: N.H does not proceed; error logged.
- Unknown session state on startup: sealed as interrupted.
- Retained archive access outside authorized purpose: denied unconditionally.

---

### 29. Integration Boundaries

**BAI:** TSC calls BAI consume interface with `"tsc_promotion:<session_id>"` for
promotion and with `"tsc_inspection:<session_id>"` for inspection. These are
separate BAI token requests, each following all BAI token lifecycle rules. BAI
writes its own audit events. TSC does not call BAI for any other purpose.

**SACL:** queried at token consumption time for both promotion and inspection
authorization. Also checked automatically during promotion retries. TSC does
not receive SACL push events directly.

**SIA:** not called by TSC. SIA assessment events linked by reference in
`sia_event_links`. Authoritative records remain in the security audit log.

**BOP:** not called by TSC. BOP observation roots are in the §7E pre-ingest
store (held), linked by `bop_preingest_capture_id` in `bop_preingest_links`.
They are not in the sealed root store while authorization is pending.

**§7E:** TSC lifts the `"pending_fingerprint_authorization"` blocker on a §7E
pre-ingest record and writes `source_metadata` from the TSC structural database
into that record before §7E processes it. §7E then handles the now-unblocked
record through its own path to `append_root()`. TSC never calls `append_root()`
directly.

**§7G:** not called by TSC. Reads promoted roots through the standard reading
queue only after they are in the sealed store. Retained archive is never
accessible to §7G.

**§7J, §7M, §7L:** not called by TSC. All run through their normal paths after
promotion.

**`append_root()`:** called by §7E's internal path only. TSC never calls it
directly. Idempotency key prevents duplication.

**Security audit log:** all events in section 26 written immediately and flushed
before the function that produced them returns.

---

### 30. Explicit Prohibited Behaviors

- TSC must not describe itself as upstream of §7E submitting into another
  waiting area. It is an extension of §7E.
- TSC must not write BOP observation roots to the sealed store while the session
  is pending authorization.
- TSC must not promote any item with `"speaker_unresolved"` outstanding. No root
  is written with `role = "unknown"`.
- TSC must not add new fields to the sealed seven-field root schema.
  Session-context metadata is carried in §7E source_metadata and TSC structural
  records.
- TSC must not retain excluded content in the active database, the §7E
  pre-ingest record, or the retained safety archive. Only non-reconstructive
  exclusion metadata may be preserved.
- TSC must not require a new fingerprint for automatic retry of already-
  authorized promotion.
- TSC must not become a second long-term memory system.
- TSC must not perform semantic interpretation or produce readings.
- TSC must not call `append_root()` directly.
- TSC must not bypass §7E.
- TSC must not auto-expire or auto-delete sealed caches.
- TSC must not promote without both fingerprint authorization and SACL
  recognized-Ness confirmation at token consumption time.
- TSC must not require a new fingerprint for items whose non-fingerprint
  blockers clear after the session was already authorized.
- TSC must not convert a third party's statement into a fact about Ness.
- TSC must not merge speaker streams or Person-Box candidates.
- TSC must not treat the retained safety archive as active memory.
- TSC must not allow the retained archive to be queried by LMAC, §7F, §7G, or
  any normal operational component.
- TSC must not split one real conversation into per-person sub-caches.
- TSC must not grant another participant's "do not save" request authority over
  N.H's storage.
- TSC must not apply §7Q rules itself — it records §7Q decisions and exclusion
  metadata but does not make them.
- TSC must not duplicate promoted roots in the sealed store.
- TSC must not re-enter material from the retained archive into the §7E path.
- TSC must not invent or reconstruct material not captured before a crash.
- TSC must not reopen or modify a sealed session.
- TSC must not silently reuse expired authorization state during retries.
- An inspection token must not substitute for a promotion token, and a promotion
  token must not provide inspection access. The two purposes are independent and
  non-interchangeable.
- TSC must not begin promotion as a consequence of inspection.
- TSC must not lift `"pending_fingerprint_authorization"` on any item as a
  consequence of inspection.

---

### 31. Status

**ACCEPTED DESIGN — NOT YET BUILT**

All seven corrections from the ChatGPT review applied. The inspection
authorization mechanism settled: a dedicated BAI `one_time_authorization_token`
with purpose `"tsc_inspection:<session_id>"`, entirely separate from the
promotion token, requiring SACL recognized-Ness confirmation at consumption
time, following all BAI token lifecycle rules.

No remaining concept questions. No files patched. No implementation claimed.
The TSC design is complete and ready for Master patch proposal when Ness directs.
