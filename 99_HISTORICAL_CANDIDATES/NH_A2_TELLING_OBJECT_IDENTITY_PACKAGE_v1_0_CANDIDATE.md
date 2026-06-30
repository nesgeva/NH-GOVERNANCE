# NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_0_CANDIDATE

## Status block

- **Status:** `CANDIDATE`.
- **Not** adopted as an architectural authority. This package does not modify, supersede, or reinterpret `NH_MASTER-20_CORRECTED_v10.md`.
- **Standalone dependency package** for Register-A item **A2 — §7K Telling Object-Identity Seam**.
- Requires **independent ChatGPT audit** and **Ness's explicit acceptance** before package closure.
- **No implementation authorization.** Nothing in this file authorizes code, migration, store creation, seal lifting, or disk modification. This is implementation-neutral target architecture only.

**Authority order governing this package:**
1. `NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness June 29 2026; current immutable authoritative Master).
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`.
3. `cursorrules`.
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

`NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` is subordinate working material and never overrides Master V10. `NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` governs the design-completion process. Where this package and any source disagree, Master V10 governs and the disagreement is surfaced, never silently resolved.

---

# 1. NORMALIZED A2 DECISION RECORD

**Package ID:** A2 — §7K Telling Object-Identity Seam.

**Date of decision:** June 30, 2026.

**Ness's answer:** the **separate-card option** — a separate first-class immutable telling record, as opposed to a stable composite reference inside the parent reading. This is the first of the two options the Master left explicitly open at §7K "OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED" (Master V10 line 2200) and at the wiring map A2 entry (map line 602/604).

**Plain-language meaning (Ness's words):** each telling should have its own separate permanent card rather than only an address such as "Reading 5, Telling 2."

**Normalized accepted rule:**
- Every Story-Layer telling is a separate first-class immutable record.
- Every telling receives its own permanent stable system-generated `telling_id`.
- A telling is not identified only by its parent reading plus its list position.
- Every telling retains a required provenance link back to the parent reading that produced it and to its supporting root or roots.
- A telling record is append-only and must never be edited, overwritten, silently merged, or replaced.
- A later interpretation or rereading creates a new telling record rather than changing an earlier telling.
- Conflicting tellings remain separate.
- Repetition does not promote a telling into fact.
- The parent reading, supporting roots, perspective, evidence relationship, time, firmness, and uncertainty remain inspectable.
- The current immutable reading and root records must never be rewritten to install this decision.

**Authority and candidate status:** this decision is recorded here as an accepted Ness decision carried into the package through the exact ChatGPT-prepared task instruction. The *package* remains a candidate; the *decision* is accepted. Acceptance of the decision is not adoption of this package.

**Affected components and registers:**
- §7K Story Layer (C-7K) — the owning component of the telling record.
- §7L Person-Boxes (C-7L) — links story tellings.
- §7J Contradiction and Clash Handling (C-7J) — clash records point to readings/roots and, where telling-level links are used, to tellings.
- §7M Computed View (C-7M) — lists tellings as a source-object type.
- §7D Living State Web (C-7D) — tellings are eligible source objects for nodes.
- §7Q Privacy / deletion / dependency discovery — must locate telling records and their links.
- C-ENGINE-C — the engine that emits tellings into `story_layer`.
- B2 (clash-record schema, where applicable), B3 (theme + telling-link structure), B4 (Person-Box link schema), B5 (Computed-View snapshots, where applicable) — the mechanical schema followers that consume the telling identity.

**Unlocked mechanics (what A2 makes designable now):**
- The permanent `telling_id` and the first-class telling-record contract (§2 below).
- One non-contradictory content/provenance relationship between the existing embedded `story_layer` entry and the first-class telling record (§3).
- Creation/persistence/recovery mechanics for allocating and committing telling records beside their parent reading (§4).
- The telling-level link *identity interface* for downstream components — what they point to and what access that pointer must preserve (§6).
- The mechanical telling-to-theme link *identity* (§7).

**Still-blocked mechanics (named, not closed here):**
- Exact firmness scale, labels, evidential thresholds — open (Master §7K "FIRMNESS RULE"; A-policy where evidential weight is judged).
- Exact theme schema, similarity grouping, confirmation thresholds, retrieval-influence policy — open (B3 for structure; A5-adjacent policy for thresholds).
- Person-Box evidence/merge policy — A5.
- Clash-response downstream-effect policy — A9.
- Relevance-mode policy — A4.
- Living State Web evidence/currentness/domain policy — A6.
- Privacy / influence-removal policy — A7.
- Substantive "grounded enough" threshold — A31.
- Full B2/B3/B4/B5 completion beyond the telling-ID interface — open.
- Engine C construction, testing, implementation — blocked (A1 gold + design completion + Ness authorization).
- Any production-store schema or disk migration — blocked.

**Must-nevers (carried from Master §7K and the no-loss list, binding on this package):**
- Never merge conflicting tellings into one synthesized narrative.
- Never promote a repeated telling into established fact because it appears often.
- Never assign a single authoritative story to a person, relationship, or event.
- Never invent connective tissue between tellings the roots do not support.
- Never treat a gap in tellings as evidence of absence.
- Never flatten temporal change into a single stable description.
- Never allow one person's perspective to silently overwrite another's.
- Never resolve whose telling is correct — that is Ness's judgment, off-board.
- Never rewrite, edit, or delete a root or a reading to install telling identity.
- Never let a telling-level link copy or silently rewrite the original telling.
- Never let telling identity make a telling factual, authoritative, a profile, or a diagnosis.

**Integration status:** NOT integrated into Master V10, the Design and Wiring Map, Decision Defaults, `cursorrules`, the Companion, or the workflow. Integration, if any, is a separate later act requiring its own authorization. This package stands alone.

---

# 2. TARGET FIRST-CLASS TELLING-RECORD CONTRACT

This section defines the **required semantics** of a first-class telling record. It does not choose a file format, a serialization, a storage engine, or any threshold. Every field below is described by what it must mean and what it must preserve, not by an implementation.

A telling record carries, at minimum:

**Identity**
- `telling_id` — permanent, stable, system-generated, unique within its store. Allocated once at creation and never reused, never reassigned, never derived from mutable content. It is the durable link target every downstream component points to. It is **not** the parent reading id plus a list index; the address-style reference the decision rejected must never be the identity.

**Required provenance links (mandatory; a telling with a broken or absent chain is not a valid telling)**
- `parent_reading_id` — the id of the immutable reading whose engine pass produced this telling. Required, single-valued. The telling is always traceable back to exactly one parent reading.
- `supporting_root_ids` — the root id or ids that ground this telling, carried through from / consistent with the parent reading's `reads`. A telling is grounded in supporting roots; it is never accepted solely because an earlier reading stated it (Master §7K grounding rule, line 1702). The telling points to roots by id; it never copies root text.
- `derivation_provenance` — how this telling came to exist: which engine pass, in which lifecycle (fresh reading vs reread), and — when the telling was materialized from a pre-existing embedded `story_layer` entry rather than freshly emitted — an explicit record that it is a materialization and of which embedded entry (see §3). This makes the production path inspectable.

**Structured perspective (Master §7K STRUCTURED PERSPECTIVE MODEL, lines 2192–2198 — roles kept separate, never collapsed)**
- `root_speaker` — who produced the source root.
- `subject` — who or what the telling is about.
- `perspective_owner` — whose viewpoint, belief, feeling, or framing the telling claims to represent.
- `attribution_path` — optional; used only when perspectives are nested (e.g. `friend → quoted by father → reported by Ness`). Populated only when the root supports the chain. Never invented. Absent when not supported — absence here is honest non-presence, never a gap filled with a placeholder.

These roles may refer to the same person or to different people. The record must never assume the root speaker is automatically the subject or the perspective owner.

**Evidence relationship (mandatory for every telling — Master §7K line 2198)**
- `evidence_relationship` — one of: direct self-report, direct quotation, reported speech, observation, or engine inference. This field is required on every telling. Reported speech is not direct access to the reported person's internal state. The engine's interpretive lens stays separate from the human perspective represented in the telling. *(This package preserves the five named categories exactly as the Master states them; it does not invent a scale, weighting, or threshold over them — that is A-policy where evidential weight is judged.)*

**Telling content**
- `telling` — the interpretive content of this telling: what is being said, about whom, from whose perspective. Recorded unaltered as the engine pass produced it. Immutable once written.

**Firmness (present only when supported — Master §7K FIRMNESS RULE, line 2204)**
- `firmness` — how strongly the perspective owner appears to hold the stance. Present only when the root supports a firmness judgment; **omitted** when it does not (never `"unknown"`, never a forced value).
- `firmness_evidence_basis` — when `firmness` is present, the observable signals it rests on (explicit certainty words, hedging, repetition, emphasis, consistency, direct statements of commitment or doubt). Firmness is always provisional and revisable.
- Firmness is a separate dimension from model confidence and must never be presented as direct access to a person's internal state. **This package does not invent the firmness scale, labels, thresholds, or scoring method — those remain undesigned (Master §7K) and are an open dependency.**

**Time and producer provenance**
- `created_at` — creation timestamp (the moment this telling record was written), ISO 8601, consistent with the reading-schema timestamp convention.
- `produced_by` — reproducibility-grade provenance consistent with the reading schema's `produced_by` model (Master §6B line 543): `origin` from the controlled vocabulary `{observed, imported, simulated, generated, reaction, human_annotation}`, plus, for engine-produced tellings, the model/digest/engine_version/prompt_version/config provenance that lets any telling be traced to the exact model that produced it. A telling's `produced_by` must be consistent with — not contradict — its parent reading's `produced_by`.
- `schema_version` — present on every new telling record; un-retrofittable; the first telling-record schema version is its own declared value (this package does not assign a literal version string — that is a mechanical/adoption detail for the implementing change).

**Operation identity and lifecycle**
- `operation_key` / `idempotency_key` — a deterministic operation identity (see §4) that makes telling creation idempotent and prevents duplicate cards after a crash or retry. Present and unique per store.
- `storage_status` — the telling's lifecycle/quarantine status, kept consistent with and subordinate to the parent reading's status (see §5). A telling does not carry an independent promotion state; it inherits eligibility from its parent reading.

**What this contract must never include:**
- No `reason`-as-asserted-fact field. The "why" behind a connection is shown by pointers, never stored as an asserted fact (wiring map Part 7.5). 
- No field that copies root text or copies another telling's content.
- No field that records a winner, a resolution, or a merge of conflicting tellings.
- No field that turns the telling into a profile, diagnosis, or settled fact.

**Explicitly not decided here (open dependencies, named so they cannot be silently closed):** firmness scale/labels/thresholds; evidence-relationship weighting; any identity threshold for deciding two perspective references are the same person (that is Person-Box / A5 territory, not telling identity); theme-confirmation policy. This contract defines *identity and shape*, not *evidential or interpretive policy*.

---

# 3. RELATIONSHIP TO THE EXISTING BUILT READING CONTRACT

**The fact base (Master §6B line 541, §6B lines 535–545, Decision Defaults lines 58–62):**
- The built, verified v1 reading record has 12 fields: `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`.
- `story_layer` is a **LIST** of tellings; an empty list is legal.
- Each existing embedded telling entry carries optional `whose · stance · firmness · telling · theme · when`; unknown sub-values are omitted, never `"unknown"`.
- Existing reading records are **immutable**. Existing embedded telling content must not be rewritten or deleted.

**The relationship this package defines (exactly one, non-contradictory):**

The first-class telling record is the **permanent telling-level link target**. The embedded `story_layer` entry inside the immutable reading remains exactly as written — it is preserved, never rewritten, never deleted. The first-class telling record does not replace the embedded entry; it is the addressable, linkable object that carries the embedded entry's content forward under a stable identity, plus the required provenance and structured-perspective fields the flat embedded form did not have.

To keep one authority and avoid two silently divergent versions of the same telling, the relationship is governed by these rules:

1. **The embedded entry is the original record of what the engine pass produced.** It stays inside its immutable parent reading as the provenance anchor. It is never edited to match the first-class record.
2. **The first-class telling record is the canonical link target.** Every downstream component that needs to point at "a telling" points at the `telling_id`, never at "reading X, list position N." The first-class record is where structured perspective, evidence relationship, firmness-with-basis, and provenance links live in full.
3. **Content correspondence is one-directional and append-only.** A first-class telling record's `telling` content corresponds to its source embedded entry; the first-class record records which embedded entry it corresponds to (in `derivation_provenance`). If the two ever appear to diverge, the embedded entry inside the immutable reading is the historical truth of what the pass emitted, and the first-class record's divergence is itself a recorded, inspectable fact — never silently reconciled by rewriting either side.
4. **There are never two editable authorities.** Both the embedded entry and the first-class record are immutable once written. Neither is a mutable cache of the other. A later interpretation does not edit either; it creates a *new* telling record (with a new `telling_id`) beside them.

**For tellings emitted fresh by Engine C (the forward path):** when Engine C produces a reading whose `story_layer` carries one or more tellings, each telling is written both as an embedded entry inside the reading (preserving the built schema) and as a first-class telling record carrying that entry's content plus the required identity/provenance/perspective fields. The two are created in one bounded operation (see §4) so a telling never exists in one form without the other being accounted for.

**For tellings that already exist only as embedded entries (the materialization path):** any future materialization of first-class telling records from existing embedded entries must be:
- **append-only** — it writes new first-class telling records; it never edits or deletes the embedded entries or their parent readings;
- **auditable** — each materialized record records that it was materialized and from which embedded entry;
- **deterministic or otherwise idempotent** — re-running materialization over the same embedded entry must not create a second first-class record for it (see §4 idempotency);
- **never a rewrite of the parent reading** — the immutable reading is read, never written, during materialization.

**This package performs no migration, no backfill, and no disk modification.** The materialization path is specified as target architecture only. Whether, when, and under what authorization materialization runs is a later separately authorized act.

---

# 4. CREATION AND PERSISTENCE MECHANICS (implementation-neutral)

All of the following is design, not code. No pseudocode that could be mistaken for patch-ready code appears here.

**When a telling identity is allocated.** A `telling_id` is allocated at the moment a telling is first written as a first-class record — either (a) during the Engine C reading pass that emits it, immediately after the reading's own commit boundary is reached, or (b) during an authorized materialization pass, when a first-class record is created from a pre-existing embedded entry. Allocation is a write-time event, never a read-time or display-time event. An id is never allocated speculatively for a telling that is not being committed.

**How a telling is connected to the reading pass that produced it.** Every telling record is written with its `parent_reading_id` set to the committed reading's `id` and its `supporting_root_ids` consistent with that reading's `reads`. A telling is only ever written *after* its parent reading is durably committed, so a telling can never point to a reading that does not exist. This ordering is the structural guarantee against orphan tellings (a telling with no real parent).

**Transaction and commit boundaries between the reading and the telling records.** The reading and its telling records are committed in a defined order with explicit checkpoints, consistent with the existing post-root async path's checkpoint model (Master/map C-7GA, RC-1…RC-8):
1. The parent reading is written and durably committed first (this is the existing built behavior; unchanged).
2. A telling-creation checkpoint is opened for that reading, keyed by the parent reading's operation identity.
3. Each telling for that reading is written as a first-class record, each carrying its own deterministic operation key.
4. A telling-creation-completed checkpoint is appended once all tellings for that reading are durably written.

The parent reading's commit is never deferred or made dependent on telling creation; root ingestion and reading commit never block on telling creation. If telling creation fails after the reading commits, the reading stands and telling creation is recoverable (see partial-completion recovery below) — the system is never left believing telling creation finished when it did not.

**Behavior when a reading contains zero, one, or several tellings.**
- **Zero tellings** (empty `story_layer`, which is legal): no telling records are created; the telling-creation checkpoint records "zero tellings for this reading" as an explicit, positive completion fact (a sentinel), not as silence. This distinguishes "this reading legitimately had no tellings" from "telling creation never ran."
- **One telling:** exactly one first-class record is created and one completion checkpoint is appended.
- **Several tellings:** each telling is written as its own first-class record with its own operation key; the single completion checkpoint for the reading is appended only after all of them are durably written. Conflicting tellings within the same reading remain separate records — they are never merged at creation.

**Deterministic operation identity / idempotency-key structure.** Each telling's operation key is derived deterministically from stable inputs that uniquely identify *that telling of that reading* — at minimum the parent reading's id, a stable per-telling discriminator within that reading (for example the telling's ordinal position *within the producing pass*, used only as a creation-time discriminator and never as the telling's identity), and a telling-operation version tag. This mirrors the existing operation-keyed pattern in the post-root path (e.g. `reading_idempotency_key = hash(enqueue_key + "reading_v1")`, and operation-keyed clash/Computed-View sentinels). The operation key is what makes re-running a pass safe; the `telling_id` remains a separate permanent identity allocated once.

**Duplicate prevention.** Before writing a telling record, the writer checks whether a telling with that operation key has already been committed. If it has, the existing record stands and no second record is written — the operation is idempotent. This prevents duplicate telling cards after a crash or retry. The same rule governs materialization: a second materialization of the same embedded entry finds the existing operation key and does not create a duplicate.

**Partial-completion detection.** A reading that has been committed but whose telling-creation-completed checkpoint is absent is detected as a partial completion: tellings may be all, some, or none written. Detection relies on the per-reading telling-creation checkpoint, not on counting records blindly.

**Recovery when the reading exists but one or more telling records are missing.** The recovery pass re-derives the operation key for each expected telling of that reading and, for each key with no committed record, writes the missing telling record (idempotently — keys already present are skipped). Because the parent reading is immutable and still present, recovery reads it to re-derive what tellings it should yield; recovery never rewrites the reading. Once all expected tellings are present, the completion checkpoint is appended. This is the analogue of RC-5 ("reading exists but checkpoints missing → restore the lifecycle/checkpoint records without rewriting the reading").

**Recovery when telling records exist but a completion checkpoint is missing.** The recovery pass confirms, via operation keys, that every expected telling for the reading is durably present; if so, it appends the missing completion checkpoint without writing any new telling record. If some are still missing, it falls to the missing-records case above. A completion checkpoint is never appended while any expected telling is absent.

**Retryable versus terminal failures.** A transient technical failure during telling creation (I/O error, lock contention, process interruption) is **retryable**: the operation is re-attempted under the same operation keys, and idempotency guarantees no duplication. A failure that is not a transient technical condition — for example a telling that cannot be validated against the required-field contract (missing `parent_reading_id`, missing `evidence_relationship`, broken provenance chain) — is **terminal for that telling**: the telling is not written, the failure is recorded as a distinct logged reason, and the engine does not silently substitute a degraded telling. The bounded retry *policy values* (how many attempts, timing, backoff) are inherited from the open system-wide retry policy (B9) and are **not chosen here**; until that policy is adopted, a substantively rejected telling is terminal.

**Fail-closed behavior.** On any system failure during telling creation, the operation closes in the safe direction: the parent reading stands (already committed), no partial or malformed telling record is left as if valid, no completion checkpoint is appended, and the partial state is left explicitly recoverable. The system never reports telling creation as complete on failure, and never exposes a half-written telling as a usable link target.

**Prevention of orphan tellings.** Guaranteed structurally by the ordering rule: a telling is only ever written after its parent reading is durably committed, and every telling carries a required `parent_reading_id`. A telling can never reference a non-existent reading.

**Prevention of duplicate telling cards after a crash or retry.** Guaranteed by the deterministic operation key plus the pre-write duplicate check: any re-run produces the same key, finds the existing record, and does not write a second one.

---

# 5. QUARANTINE AND PRODUCTION SEPARATION

**The boundary being preserved (Master/map: Engine C writes to quarantine, never directly to production; production readings store is absent by design — Decision Defaults line 81, Master §6B "PRODUCTION READINGS AUTHORIZATION" lines 454–461):**

- Engine C writes readings to **quarantine**, never directly to production. This package does not change that.
- A telling is a derived child of a reading. **A telling derived from a quarantined reading must not bypass the reading's quarantine state.** The telling's `storage_status` is subordinate to and consistent with its parent reading's status; a telling cannot be "more promoted" than its parent reading.
- **Telling-level links must not expose an unapproved quarantined telling as production material.** A downstream component following a `telling_id` into a quarantined telling sees it under the parent reading's quarantine state, not as production-grade material.
- **Promotion, rejection, and retention behavior remain connected to the parent reading's valid state.** A telling is promoted, rejected, or retained as a consequence of what happens to its parent reading — it has no independent promotion lifecycle that could diverge from the reading's.
- **No production store is created here**, and **no new promotion policy is invented.** The existing production-readings authorization (Ness's deliberate `.nh_readings_production_authorized` marker plus Cursor's approved dry-run) is unchanged and is not triggered by anything in this package. Any promotion policy detail not already settled remains **explicitly open**.

**Open here, named:** the exact promotion mechanics for tellings (how a telling's status is updated when its parent reading is promoted, and the operation identity of that update) follow whatever production-promotion design is later authorized; this package fixes only the *invariant* — a telling never escapes its parent reading's state — not the promotion procedure.

---

# 6. CROSS-COMPONENT TELLING-ID CONTRACTS

A2 unlocks exactly one thing for downstream components: a stable `telling_id` they may point at. This section defines only that **identity interface** — what each consumer points to and what the pointer must preserve. It does **not** complete any consumer's own schema (those remain B2/B3/B4/B5 and the respective A-policies).

**Universal rule for every consumer below:** a downstream reference points to the stable `telling_id` and, through it, preserves access to the parent reading and the supporting roots. **Links are never copies.** A link never copies or silently rewrites the original telling; the telling stays where it is and the consumer holds a reference plus its own link metadata (what it connects, why-by-pointer, who established it, certainty, timestamp — per Master §7L line 2226 link-record rules where applicable).

- **C-7K Story Layer (owner).** Holds the first-class telling records. Organizes tellings by perspective/theme/time using `telling_id` as the stable handle. Connections across time between tellings are explicit navigational links keyed on shared attributes (same `perspective_owner`/`whose`, same theme, same thread/source, overlapping time, shared root ids) — navigational links, not logical merges, always labeled with their basis and always pointing back to supporting roots and readings (Master §7K line 2190).
- **C-7L Person-Boxes.** Links story tellings in which a person appears in any perspective role, by `telling_id`. The Person-Box link record preserves what/why/who-established/certainty/timestamp. Linking a telling never copies it and never promotes it to a fact about the person. *(Person-Box evidence/merge policy remains A5; link-schema mechanics remain B4 — not closed here.)*
- **C-7J Clash Handling (where telling-level links are used).** A clash record points to the exact readings and roots involved (Master §7J line 2160); where a clash is between *tellings* specifically, it may additionally point to the `telling_id`s involved. The same clash never produces two records (later detection appends a detection-history event to the existing clash). Clashes are surfaced, never resolved; pointing at conflicting tellings never selects a winner. *(Clash-record schema specifics remain B2 where applicable; clash-response downstream policy remains A9.)*
- **C-7M Computed View.** Lists tellings among its source-object types (Master §7M line 2262), referenced by `telling_id`, linked never copied. The Computed View's seven-factor ordering and internal-only rules are unchanged; telling identity gives it a stable handle, nothing more. *(Snapshot-schema structure remains B5 where applicable; relevance mode remains A4.)*
- **C-7D Living State Web.** Story tellings are eligible source objects for state nodes (Master §7D line 645, line 655), referenced by `telling_id`. A node's grounding rule still requires immediate source-object ids plus direct root ids and a fully inspectable chain; circular support remains forbidden; Story-Layer firmness rules apply when tellings are used as evidence. Telling identity supplies the stable source-object id; it supplies no evidential weight. *(Living State Web evidence/currentness/domain policy remains A6.)*
- **§7Q deletion / dependency discovery.** Dependency discovery must be able to locate telling records and their links (Master §7Q line 2442 lists "story tellings" among what a deletion case must find). A stable `telling_id` plus the required parent-reading and supporting-root provenance links is exactly what makes a telling discoverable and its derivatives traceable. No telling may bypass privacy, restriction, sealed-isolation, or visibility handling through a secondary index or link (§9 below). *(Privacy/influence-removal policy remains A7; deletion remains non-destructive visibility removal under the settled current rules.)*
- **C-ENGINE-C.** Emits tellings into `story_layer` and, under §3–§4, into first-class telling records. Engine C may rely on `telling_id` now that A2 is settled — but Engine C construction/testing/implementation remains blocked (A1 gold cases first; design completion; Ness authorization). This package authorizes the *identity Engine C will emit*, not Engine C's construction.
- **B3 theme and telling-link structure.** May use `telling_id` as the telling end of a telling-to-theme link (see §7). Theme schema, similarity grouping, and confirmation thresholds remain open (B3 structure; A5-adjacent policy).
- **B4 Person-Box link schema.** May use `telling_id` as a linkable target type. Schema mechanics remain B4.
- **B2 clash-record schema (where applicable).** May include `telling_id`s where a clash is telling-level. Schema specifics remain B2.
- **B5 Computed-View snapshots (where applicable).** May reference `telling_id`s in immutable snapshots. Snapshot schema remains B5.

---

# 7. THEME-LINK BEHAVIOR UNLOCKED BY A2

A2 unlocks only the **mechanical telling-to-theme link identity** — i.e. that a theme link's telling end is a stable `telling_id`. It does not choose theme policy.

**Link identity (what A2 settles):** a telling-to-theme link connects a `telling_id` (the telling end) to a theme (the theme end), recording the link as a first-class connection with its own provenance (what it connects, who/what proposed it, why-by-pointer, timestamp, uncertainty), never as a copy of the telling and never as an assertion that the theme is a fact.

**Preserved (Master §7K HYBRID THEME SYSTEM, lines 2206–2216 — binding):**
- Themes are navigation categories, never facts.
- Engine-proposed themes remain `proposed`; only Ness confirms.
- One telling may have zero, one, or several theme links; membership is not exclusive.
- Repetition does not confirm a theme; a theme cannot validate itself by being frequently proposed.
- Circular support is prohibited — pattern-derived themes must retain root support; a telling-to-theme link must not become a path by which a theme validates itself without root grounding.
- Theme use in later retrieval remains auditable — if a confirmed or proposed theme is used to retrieve context for a future engine pass, that influence must appear in the retrieval audit trail (Master §7K line 2214).

**Not chosen here (open):** theme-confirmation thresholds, theme similarity policy, theme schema structure, and any A5-adjacent evidence policy. B3 carries the theme/telling-link *structure* after A2 fixes the seam; the thresholds are A-policy. This package fixes only that the telling end of a theme link is the stable `telling_id`.

---

# 8. CORRECTIONS AND REREADING

**Preserved (Master §7K, §7H reread lifecycle, and the no-loss list — binding):**
- A reread creates a **new reading** beside the old; it never overwrites (Master §6B "a re-read is a NEW reading beside the old," line 535).
- New tellings produced by that reread receive **new `telling_id`s** — they are new first-class records, not edits of earlier tellings.
- Earlier tellings remain intact, immutable, fully inspectable.
- No "current telling" operation exists that could rewrite history. There is no mutable "latest" telling that supersedes earlier ones in place.
- Connections across time between an earlier telling and a later one are **explicit navigational links**, not logical merges — they point, they do not combine, and they always carry their basis.
- Temporal change and contradiction remain **distinguishable**: the link metadata records whether two tellings represent a change over time or a contradiction; neither is collapsed into the other (Master §7K "Distinguishing temporal change from contradiction," line 2184).
- No automatic supersession and no truth winner may be invented. A later telling does not automatically defeat an earlier one; only Ness, off-board, judges — and even then his judgment is recorded as a separate event and never rewrites the readings, roots, or tellings (Master §7J lines 2170–2176).

**Mechanical consequence for telling identity:** because each reread yields new readings and therefore new tellings with new ids under fresh operation keys, the idempotency and duplicate-prevention rules of §4 apply unchanged to reread-produced tellings; a reread never collides with or overwrites an earlier telling's id. *(The reread mode-assignment rule itself remains A25, and reread operation-identity wiring remains B10 — not closed here; this package only fixes that reread tellings are new first-class records.)*

---

# 9. PRIVACY, DELETION, RELEVANCE, AND AUTHORITY BOUNDARIES

**Preserved (Master §7Q, §7R, §0B, §7P — binding):**
- **§7Q governs eligibility and handling.** A telling is subject to §7Q the same as any derived object. Telling identity does not create a new access path around §7Q.
- **Deletion remains non-destructive visibility removal** under the settled current rules (Master §7Q lines 2440–2457): deletion removes material from ordinary visible output while content remains preserved internally; stopping internal influence is a separate explicit Ness instruction with its own scope and record; a history record (not a content-free tombstone) documents what was removed, when, and by what authority.
- **Dependency discovery must be capable of locating telling records and their links** (Master §7Q line 2442). The stable `telling_id` plus required provenance links is what makes a telling and its derivatives findable in a deletion case; this is a reason the first-class record must carry those links, not an optional convenience.
- **No telling may bypass privacy, restriction, sealed-isolation, or visibility handling through a secondary index or link.** A telling-level link is not a back door: following a `telling_id` is still subject to the same §7Q visibility-vs-internal-use distinction and the same Level-1/Level-2 protections (Master §0B "ACCESS AND AUTHORIZATION BOUNDARY," line 257). A link's existence never grants visibility the underlying telling would not have.
- **§7R relevance never determines truth, authority, or permission** (Master §7R; Decision Defaults). A telling being relevant to a purpose never makes it true, never grants permission to act, and never resolves a clash. §7Q runs before §7R on derived operations.
- **Ness remains the sole decider.** Telling identity makes a telling *addressable*; it never makes it *authoritative*. The engine never closes; only Ness affirms, off-board.
- **Telling identity does not make the telling factual or authoritative.** A first-class telling record is still a weightless, dated, evidence-tagged, rejectable interpretation (Decision Defaults SMART-machinery law, line 46) — being a first-class object changes its addressability, never its epistemic status.

**Not decided here (open):** any open A7 privacy policy, and any influence-removal policy, remain reserved to Ness. This package introduces no privacy, restriction, or deletion *policy* — only the identity that §7Q's existing dependency-discovery requirement already presupposes.

---

# 10. §0B LIVING-RECORD LOGGING

Per §0B (Master lines 233–259): every real operation creates one append-only living-record log; **one operation, one log**; a log proves an operation occurred and **never becomes double evidence** that the underlying telling is true; no silent operation. Logs are subject to §7Q access/authorization and §25 identity/security authorization where applicable. This component therefore specifies the following component-specific logging:

- **Telling-record creation** — one log per telling written, recording the `telling_id`, the operation key, and that a first-class telling record was created. Creating the log does not itself create a second log.
- **Parent-reading and root linkage** — recorded as part of the creation log (or a linked record): the `parent_reading_id` and `supporting_root_ids` the telling was written with, so the grounding chain is inspectable.
- **Materialization from an embedded telling** — one log per materialized record, recording that it was materialized (not freshly emitted) and from which embedded entry, distinguishing the materialization path from the forward path.
- **Duplicate-prevention result** — recorded when a write is skipped because the operation key already exists, so the idempotent no-op is itself visible (an operation occurred — a duplicate check ran — and its outcome is logged once).
- **Partial-completion recovery** — recorded when a recovery pass detects a missing completion checkpoint or missing telling records and what it did (which keys it wrote, which it skipped, when it appended the completion checkpoint).
- **Retry or terminal failure** — recorded as a distinct reason type per the §4 failure taxonomy: a retryable technical failure is logged as such; a terminal validation failure (broken provenance, missing required field) is logged as a distinct terminal reason and never silently relabeled.
- **Telling-level link creation** — one log per downstream link established to a `telling_id` (Person-Box link, theme link, clash telling-pointer, Living-State-Web source reference, Computed-View reference), recording what was linked, by which component, and its provenance pointer.
- **Rejected or blocked downstream use** — recorded when a link or use is blocked (e.g. a quarantined telling refused as production material, or a §7Q visibility block on following a link), so the block is an inspectable event.
- **Schema/version provenance** — every telling record and every telling-level link carries the `schema_version` / producer-version provenance that lets it be traced to the exact producing logic and model.

**No-double-evidence reminder, binding on all of the above:** repeated logs about a telling — its creation, its use, its linking — never add certainty that the telling is *correct*. One underlying telling must not become several independent votes for itself (Master §0B line 243). Logging records that operations happened; it never strengthens the interpretation.

---

# 11. DESIGN-COMPLETE CONDITIONS FOR THIS PACKAGE

**What A2 closes (and only this):** the telling **object-identity choice** — separate first-class immutable telling record with a permanent stable `telling_id` — and the **directly unlocked mechanical identity/reference design**: the first-class telling-record contract (§2), the one non-contradictory relationship to the existing immutable embedded `story_layer` entry (§3), the creation/persistence/recovery/idempotency/fail-closed mechanics for allocating and committing telling records beside their parent readings (§4), the quarantine-subordination invariant (§5), the downstream telling-ID *identity interface* (§6), the telling-to-theme link *identity* (§7), the reread "new id per new telling" rule (§8), the §7Q discoverability and no-bypass invariants (§9), and the §0B component logging (§10).

**What A2 does not close (explicitly open, owners named):**
- Firmness scale, labels, evidential thresholds, scoring method — open (Master §7K; A-policy where evidential weight is judged).
- Theme schema, similarity grouping, confirmation thresholds, retrieval-influence policy — open (B3 structure; A5-adjacent policy).
- Person-Box evidence/merge policy (A5); Person-Box link-schema mechanics (B4).
- Clash-response downstream policy (A9); clash-record schema specifics (B2) beyond the telling-pointer interface.
- Relevance-mode policy (A4); Computed-View snapshot schema (B5) beyond the telling-reference interface.
- Living State Web evidence/currentness/domain policy (A6); node/edge schema (B6).
- Privacy / influence-removal policy (A7).
- Substantive "grounded enough" threshold (A31).
- A1 story-bearing gold cases — the separate Register-A item; **not reopened, not reconstructed here**. Its standalone artifact status is whatever the project record says; this package neither confirms nor questions the A1 substantive decision.
- Engine C construction, testing, implementation — blocked.
- Production-store schema; any disk migration; any materialization run — blocked / separately authorized.
- Bounded retry *values* for telling-creation failures (B9); the production-promotion procedure for tellings (follows later authorized production design).

**The package is design-complete for A2 when:** the telling object-identity is fixed as a separate first-class immutable record with a permanent `telling_id` (§1–§2); a single non-contradictory relationship to the existing immutable reading/`story_layer` is specified with no second editable authority (§3); allocation, transaction boundaries, the zero/one/several cases, deterministic operation identity, duplicate prevention, partial-completion detection, both recovery directions, retryable-vs-terminal failure handling, fail-closed behavior, and orphan/duplicate prevention are all specified implementation-neutrally (§4); the quarantine-subordination invariant is stated (§5); the downstream identity interface for every named consumer is specified as point-to-`telling_id`-never-copy with provenance preserved (§6); the telling-to-theme link identity is fixed without choosing theme policy (§7); the reread/correction rules are preserved with new ids per new telling (§8); the §7Q discoverability and no-bypass invariants and §7R/authority boundaries are preserved (§9); and the §0B one-operation-one-log component logging with no-double-evidence is specified (§10) — **with every dependency above left explicitly open and owner-named, and no concept, threshold, or policy invented.** All of these conditions are met by this candidate, subject to ChatGPT's independent audit and Ness's acceptance.

---

# 12. PACKAGE SELF-AUDIT (internal; full delivery audit accompanies the file)

- **Authority:** Master V10 treated as adopted/authoritative; subordinate sources not promoted; candidate status explicit; no authority inversion. **PASS.**
- **Scope:** only the A2-unlocked identity/reference mechanics designed; no unrelated component completed; no concept invented. **PASS.**
- **Concept fidelity:** the separate-card decision is recorded verbatim-normalized and is the basis of every mechanic; the rejected address-style identity is explicitly excluded. **PASS.**
- **No-loss:** every relevant settled §7K/§7L/§7J/§7M/§7D/§7Q/§7R/§0B rule and every item on the instruction's no-loss list is preserved and cited. **PASS.**
- **Identifiers / references / lifecycle / operation identity / transactions / idempotency / duplicate prevention / crash recovery / retry / partial completion / fail-closed:** all specified in §4, consistent with the existing operation-keyed post-root model. **PASS.**
- **Logging:** §0B one-operation-one-log, no double evidence, §7Q/§25 access noted. **PASS.**
- **Wiring / DUMB-SMART / root-reading / quarantine-production / Layer-2-Layer-3:** telling identity is SMART-side and weightless; roots/readings stay immutable; tellings stay subordinate to the parent reading's quarantine state; no Layer-2/Layer-3 mixing introduced. **PASS.**
- **No implementation:** no code, no patch-ready pseudocode, no migration, no store creation, no seal lifting, no disk modification. **PASS.**

---

*End of `NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_0_CANDIDATE` — CANDIDATE, unaudited, awaiting ChatGPT independent audit and Ness's explicit acceptance. No source file was changed; no implementation was performed.*
