# NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_1_CANDIDATE

## Status block

- **Status:** `CANDIDATE`.
- **Not** adopted as an architectural authority. This package does not modify, supersede, or reinterpret `NH_MASTER-20_CORRECTED_v10.md`.
- **Standalone dependency package** for Register-A item **A2 — §7K Telling Object-Identity Seam**.
- **Corrected candidate.** This is the v1.1 correction of `NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_0_CANDIDATE.md`, addressing four verified issues raised in ChatGPT's audit. **v1.0 is preserved unchanged as historical candidate provenance.** This file does not overwrite, rename, delete, or modify v1.0 or any other file.
- Requires **independent ChatGPT audit** and **Ness's explicit acceptance** before package closure.
- **No implementation authorization.** Nothing here authorizes code, migration, store creation, seal lifting, or disk modification. Implementation-neutral target architecture only.

**Authority order governing this package:**
1. `NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness June 29 2026; current immutable authoritative Master).
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`.
3. `cursorrules`.
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

`NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` is subordinate working material and never overrides Master V10. `NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` governs the design-completion process. Where this package and any source disagree, Master V10 governs and the disagreement is surfaced, never silently resolved.

**Ness's accepted A2 decision is unchanged in v1.1:** every telling is its own separate first-class immutable card with its own permanent stable `telling_id`, linked to the immutable reading and supporting root evidence that produced it. The correction does not reopen, reinterpret, broaden, or weaken this decision; it only makes the unlocked mechanics correct.

## What changed from v1.0 (summary; full list in the delivery report)

- **§2** — operation-identity field naming corrected (canonical `telling_idempotency_key`; the wider operation key given a distinct name and scope); `storage_status` removed from the immutable core and replaced with a derived/event-based lifecycle model.
- **§3** — divergence handling corrected: a mismatched first-class card now fails closed and is barred from being the canonical link target, rather than merely being recorded as inspectable. A correspondence/integrity invariant is defined.
- **§4** — crash recovery corrected: a durable **prepared-telling manifest** is introduced so recovery never regenerates or reinterprets a telling; fail-closed handling defined for every commit/checkpoint boundary.
- **§4A (new)** — explicit field-by-field embedded-to-first-class **no-loss mapping contract**, and a fail-closed **legacy-materialization rule**.
- **§5** — quarantine/production separation re-expressed against the derived/event-based lifecycle (no mutable status field).
- **§5A (new)** — **telling-completion eligibility gate** governing all telling-level downstream fan-out.
- **§10, §11, §12** — logging, design-complete conditions, and self-audit updated for the connected consequences of the above.
- **§6, §7, §8, §9** — preserved from v1.0 unchanged in substance (the downstream identity interface, theme-link identity, reread rules, and privacy/authority boundaries were correct).

---

# 1. NORMALIZED A2 DECISION RECORD

**Package ID:** A2 — §7K Telling Object-Identity Seam.

**Date of decision:** June 30, 2026.

**Ness's answer:** the **separate-card option** — a separate first-class immutable telling record, as opposed to a stable composite reference inside the parent reading. The first of the two options the Master left open at §7K "OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED" (Master V10 line 2200) and at the wiring map A2 entry (map line 602/604).

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

**Authority and candidate status:** the decision is an accepted Ness decision carried through the exact ChatGPT-prepared task and correction instructions. The *package* remains a candidate; the *decision* is accepted. Acceptance of the decision is not adoption of this package.

**Affected components and registers:** §7K Story Layer (C-7K, owner); §7L Person-Boxes (C-7L); §7J Clash Handling (C-7J); §7M Computed View (C-7M); §7D Living State Web (C-7D); §7Q privacy/deletion/dependency discovery; C-ENGINE-C; B2 (clash-record schema, where applicable), B3 (theme + telling-link structure), B4 (Person-Box link schema), B5 (Computed-View snapshots, where applicable).

**Unlocked mechanics:** the permanent `telling_id` and first-class telling-record contract (§2); the durable prepared-telling manifest and exact-payload recovery (§4); the field-by-field no-loss mapping and fail-closed legacy-materialization rule (§4A); the correspondence/integrity invariant and divergence fail-closed (§3); the quarantine-subordination invariant via derived/event lifecycle (§5); the telling-completion eligibility gate (§5A); the downstream telling-ID identity interface (§6); the telling-to-theme link identity (§7); §0B component logging (§10).

**Still-blocked mechanics (named, not closed here):** exact firmness scale/labels/thresholds; theme schema/similarity/confirmation/retrieval-influence (B3 structure; A5-adjacent policy); A5 Person-Box evidence/merge; A9 clash downstream; A4 relevance mode; A6 Living State Web policy; A7 privacy/influence-removal; A31 "grounded enough" threshold; full B2/B3/B4/B5 beyond the telling-ID interface; Engine C construction/testing/implementation; production-store schema and any disk migration; bounded retry values (B9); reread operation-identity wiring (B10); the production-promotion procedure for tellings.

**Must-nevers (carried from Master §7K and the no-loss list, binding):** never merge conflicting tellings; never promote a repeated telling to fact; never assign a single authoritative story; never invent connective tissue the roots do not support; never treat a gap as absence; never flatten temporal change; never let one perspective silently overwrite another; never resolve whose telling is correct (Ness's judgment, off-board); never rewrite/edit/delete a root or reading to install telling identity; never let a link copy or silently rewrite the original telling; never let telling identity make a telling factual, authoritative, a profile, or a diagnosis.

**Integration status:** NOT integrated into Master V10, the Design and Wiring Map, Decision Defaults, `cursorrules`, the Companion, or the workflow. This package stands alone.

---

# 2. TARGET FIRST-CLASS TELLING-RECORD CONTRACT

This section defines the **required semantics** of a first-class telling record. It chooses no file format, serialization, storage engine, or threshold. Each field is described by what it must mean and preserve.

**Identity**
- `telling_id` — permanent, stable, system-generated, unique. Allocated once at creation, never reused, never reassigned, never derived from mutable content. It is the durable link target every downstream component points to. It is **not** the parent reading id plus a list index. **The same `telling_id` remains unchanged across every later lifecycle state of the telling** (quarantine, promotion, rejection, retention, visibility change); lifecycle change never mints a new id and never retires the id (§5). **`telling_id` is unambiguous across the lifecycle and cannot collide merely because quarantine and production are separate storage locations** — identity is the `telling_id` value itself, not the location of the record; the same telling in quarantine and (if ever promoted) in production is one identity, never two (§5).

**Required provenance links (mandatory; a telling with a broken or absent chain is not a valid telling)**
- `parent_reading_id` — the id of the immutable reading whose engine pass produced this telling. Required, single-valued. The telling is always traceable back to exactly one parent reading.
- `supporting_root_ids` — the root id(s) that ground this telling, consistent with the parent reading's `reads`. A telling is grounded in supporting roots; never accepted solely because an earlier reading stated it (Master §7K grounding rule, line 1702). Points to roots by id; never copies root text.
- `derivation_provenance` — how this telling came to exist: which engine pass, in which lifecycle (fresh reading vs reread), and — when materialized from a pre-existing embedded `story_layer` entry rather than freshly emitted — an explicit record that it is a materialization and of which embedded entry (§3, §4A).
- `embedded_entry_correspondence` — the exact, deterministic identifier of the embedded `story_layer` entry this card corresponds to: the `parent_reading_id` plus the stable per-telling discriminator (the embedded entry's ordinal index within its reading's `story_layer` list as emitted by the producing pass). This is the correspondence anchor used by the §3 integrity invariant. The discriminator is a correspondence/creation device only; it is **never** the telling's identity (that is `telling_id`).

**Structured perspective (Master §7K STRUCTURED PERSPECTIVE MODEL, lines 2192–2198 — roles kept separate, never collapsed)**
- `root_speaker` — who produced the source root.
- `subject` — who or what the telling is about.
- `perspective_owner` — whose viewpoint, belief, feeling, or framing the telling claims to represent.
- `attribution_path` — optional; used only when perspectives are nested (e.g. `friend → quoted by father → reported by Ness`). Populated only when the root supports the chain. Never invented. Absent when not supported — honest non-presence, never a filled placeholder.

These roles may refer to the same person or to different people. The record never assumes the root speaker is automatically the subject or the perspective owner.

**Evidence relationship (mandatory for every valid first-class telling — Master §7K line 2198)**
- `evidence_relationship` — one of: direct self-report, direct quotation, reported speech, observation, or engine inference. Required on every valid first-class telling. Reported speech is not direct access to the reported person's internal state. The engine's interpretive lens stays separate from the human perspective represented in the telling. *(This package preserves the five named categories exactly; it invents no scale, weighting, or threshold over them — that is A-policy where evidential weight is judged.)*

**Telling content**
- `telling` — the interpretive content of this telling, recorded unaltered as the producing pass emitted it. Immutable once written.
- `stance` — preserved as its own value when the producing pass emitted a `stance`; **not** assumed to be derivable from the general `telling` text (§4A). Present only when emitted; omitted when not, never `"unknown"`.

**Firmness (present only when supported — Master §7K FIRMNESS RULE, line 2204)**
- `firmness` — how strongly the perspective owner appears to hold the stance. Present only when the root supports a firmness judgment; **omitted** when it does not (never `"unknown"`, never forced).
- `firmness_evidence_basis` — when `firmness` is present, the observable signals it rests on. Firmness is always provisional and revisable. Separate dimension from model confidence; never presented as direct access to a person's internal state. **The firmness scale, labels, thresholds, and scoring method are not invented here — open dependency (Master §7K).** *(See §4A for how a legacy embedded `firmness` that lacks a recorded basis is handled.)*

**Time (three distinct time concepts, never conflated — see §4A)**
- `created_at` — record creation time: the moment this first-class telling record was written. ISO 8601, consistent with the reading-schema timestamp convention.
- `embedded_when` — the original embedded `when` value carried forward exactly, when the embedded entry had one. Distinct from `created_at`. Omitted when the embedded entry had no `when`.
- `source_event_time` — the time of the source event the telling is about, when the root/source supports it. Distinct from both `created_at` and `embedded_when`. Omitted when unsupported; never invented.

**Producer and schema provenance**
- `produced_by` — reproducibility-grade provenance consistent with the reading schema's `produced_by` model (Master §6B line 543): `origin` from `{observed, imported, simulated, generated, reaction, human_annotation}`, plus, for engine-produced tellings, model/digest/engine_version/prompt_version/config provenance. A telling's `produced_by` must be consistent with — not contradict — its parent reading's `produced_by`.
- `schema_version` — present on every new telling record; un-retrofittable. (No literal version string assigned here — a mechanical/adoption detail for the implementing change.)

**Operation identity (canonical naming — corrects v1.0 Issue, "Operation identity clarification")**
- `telling_idempotency_key` — **the one canonical record-level idempotency identity of a telling card.** Present and unique per store. The writer rejects an already-committed `telling_idempotency_key`. This is the field name used everywhere a telling card's idempotency identity is meant.
- The **wider operation key** is a separate, distinctly-named device: `telling_creation_operation_key` (defined in §4) scopes the *creation operation for one telling within one reading-pass*, from which the record-level `telling_idempotency_key` is **deterministically derived**. They are not interchangeable: the operation key identifies the *operation*; the idempotency key identifies the *record*. Their scopes and deterministic relationship are specified in §4. (v1.0 wrote these as the interchangeable pair `operation_key / idempotency_key`; that ambiguity is removed.)

**Lifecycle (no mutable status in the immutable core — corrects v1.0 Issue 3)**
- The immutable telling core carries **no editable `storage_status` field.** (v1.0's `storage_status` is removed.)
- A telling's **effective lifecycle eligibility** (quarantine, production, visibility, rejection, retention) is **derived** from its parent reading's valid append-only lifecycle state and/or represented through **separate append-only lifecycle events** that point to the `telling_id` — never by mutating the telling card. Full model in §5.

**What this contract must never include:** no `reason`-as-asserted-fact field (the "why" is shown by pointers, never stored as asserted fact — wiring map Part 7.5); no field that copies root text or another telling's content; no field that records a winner, resolution, or merge of conflicting tellings; no field that turns the telling into a profile, diagnosis, or settled fact; **no mutable status field of any kind in the immutable core.**

**Explicitly not decided here (open, named):** firmness scale/labels/thresholds; evidence-relationship weighting; any identity threshold for deciding two perspective references are the same person (Person-Box / A5 territory, not telling identity); theme-confirmation policy. This contract defines *identity and shape*, not *evidential or interpretive policy*.

---

# 3. RELATIONSHIP TO THE EXISTING BUILT READING CONTRACT — WITH CORRESPONDENCE/INTEGRITY INVARIANT

**The fact base (Master §6B line 541, lines 535–545; Decision Defaults lines 58–62):**
- The built, verified v1 reading record has 12 fields: `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`.
- `story_layer` is a **LIST** of tellings; an empty list is legal.
- Each existing embedded telling entry carries optional `whose · stance · firmness · telling · theme · when`; unknown sub-values are omitted, never `"unknown"`.
- Existing reading records are **immutable**. Existing embedded telling content must not be rewritten or deleted.

**The single relationship this package defines:** the first-class telling record is the **permanent telling-level link target**. The embedded `story_layer` entry inside the immutable reading remains exactly as written — preserved, never rewritten, never deleted. The first-class record does not replace the embedded entry; it is the addressable, linkable object that carries the embedded entry's content forward under a stable identity, plus the required provenance and structured-perspective fields the flat embedded form did not have.

Governing rules:
1. **The embedded entry is the original record of what the engine pass produced.** It stays inside its immutable parent reading as the provenance anchor. Never edited to match the first-class record.
2. **The first-class telling record is the canonical link target — only when it is integrity-valid (rule 5).** Every downstream component that needs to point at "a telling" points at the `telling_id`, never at "reading X, list position N."
3. **Content correspondence is one-directional and append-only.** A first-class record corresponds to exactly one embedded entry, identified by `embedded_entry_correspondence` (§2). The embedded entry inside the immutable reading is the historical truth of what the pass emitted.
4. **There are never two editable authorities.** Both the embedded entry and the first-class record are immutable once written. Neither is a mutable cache of the other. A later interpretation does not edit either; it creates a *new* telling record (new `telling_id`) beside them.
5. **Correspondence/integrity invariant (corrects v1.0 Issue 4).** A three-way correspondence must hold and be verifiable across:
   - the durable **prepared-telling manifest** entry (§4);
   - the **embedded reading entry** it was derived from;
   - the committed **first-class telling card**.
   Verification is by **stable identity** (`telling_id` + `embedded_entry_correspondence`), **deterministic correspondence** (the card's carried-forward embedded values equal the embedded entry's values, field by field per §4A), and an **integrity digest** (or equivalent implementation-neutral mechanism) computed over the prepared payload and re-checkable against the committed card. **Any unexplained mismatch is an integrity failure.**
6. **Divergence fails closed (corrects v1.0 — v1.0 only recorded divergence as inspectable).** A first-class card that fails the integrity invariant **must fail closed: it must not be available as a canonical downstream link target.** The failure is recorded (§10) without rewriting either immutable source — neither the embedded entry nor any committed record is altered. N.H **never silently reconciles, normalizes, or chooses the divergent card over the original embedded output.** The embedded entry remains the historical truth; the divergent card is quarantined from canonical use until the discrepancy is resolved through an authorized path (not invented here).

**Forward path (Engine C emits fresh):** when Engine C produces a reading whose `story_layer` carries one or more tellings, each telling is (a) written as an embedded entry inside the reading (preserving the built schema), (b) captured in the durable prepared-telling manifest with its complete first-class payload before the system reaches a state from which recovery would otherwise need to regenerate it (§4), and (c) committed as a first-class telling card. The integrity invariant (rule 5) binds all three.

**Materialization path (first-class records from pre-existing embedded entries):** any future materialization must be append-only (writes new cards; never edits/deletes embedded entries or parent readings), auditable (records that it was materialized and from which embedded entry), deterministic/idempotent (re-running over the same embedded entry creates no second card — §4), never a rewrite of the parent reading (the immutable reading is read, never written), and **subject to the fail-closed legacy-materialization rule of §4A** (an incomplete legacy entry never becomes a valid card by invention).

**This package performs no migration, no backfill, and no disk modification.** Materialization is target architecture only; whether/when/under what authorization it runs is a later separately authorized act.

---

# 4. CREATION, PERSISTENCE, AND EXACT-PAYLOAD CRASH RECOVERY (implementation-neutral)

All design, not code. No pseudocode that could be mistaken for patch-ready code.

## 4.1 The durable prepared-telling manifest (corrects v1.0 Issue 1)

**Why it exists.** v1.0 committed the parent reading first, then created first-class cards, and said recovery could reconstruct missing cards from the immutable parent reading. That is insufficient: the embedded `story_layer` entry holds only `whose · stance · firmness · telling · theme · when`, while the first-class contract additionally requires structured perspective roles, `evidence_relationship`, `firmness_evidence_basis`, exact provenance, and the three time concepts — information that **may not be recoverable from the embedded entry after a crash.** Reconstructing it would require rerunning the model or reinterpreting the root, which could yield a *semantically different* telling. That is prohibited.

**What it is.** An implementation-neutral, durable, operation-scoped **prepared-telling manifest** for one reading-pass. Before the system reaches any state from which recovery would otherwise need to regenerate or reinterpret a telling, the manifest durably preserves, **for every expected telling of that reading**, the **exact complete immutable first-class payload**. Each manifest entry contains, at minimum:
- the **stable per-telling discriminator** (`embedded_entry_correspondence`, §2);
- the **complete first-class card payload** (every §2 field the card will carry: identity, provenance links, structured perspective, `evidence_relationship`, content/`stance`, firmness + basis when present, the three time fields, producer/schema provenance);
- the **parent-reading operation identity** (the reading's `idempotency_key` / the pass's operation identity) tying the manifest to its reading-pass;
- the **exact embedded-entry correspondence** (which embedded entry each payload derives from);
- the **required provenance** (`parent_reading_id`, `supporting_root_ids`, `derivation_provenance`);
- an **integrity digest** over the payload (§3 rule 5).

**Recovery uses this manifest, never the model.** Recovery reads the durable manifest and commits the missing first-class cards directly from the preserved exact payloads. **Recovery must never rerun the model, reinterpret the root, infer missing fields again, or create a semantically different telling.** The immutable parent reading is read for correspondence checking only and **is never rewritten.**

**A prepared payload is not a valid telling card.** A manifest entry is preparation, not a committed first-class telling. It **must not be available to downstream semantic consumers** (C-7K/7L/7J/7M/7D, §7Q traversal, B2–B5). Only a committed, integrity-valid first-class card is a usable link target. The manifest is recovery material, not memory.

## 4.2 Allocation and connection

**When `telling_id` is allocated.** At the moment a telling is first committed as a first-class card — either during the Engine C pass that emits it (after the reading's own commit boundary and after the manifest is durable) or during an authorized materialization pass. Allocation is a write-time event, never read-time or display-time. Never allocated speculatively for a telling not being committed. (The manifest entry may carry the intended `telling_id` as part of the exact payload so that recovery commits the *same* id deterministically rather than minting a new one.)

**How a telling is connected to its producing pass.** Every card is written with `parent_reading_id` = the committed reading's `id` and `supporting_root_ids` consistent with that reading's `reads`. A card is only ever written **after** its parent reading is durably committed **and** its manifest entry is durable — so a telling can never point to a reading that does not exist, and recovery always has the exact payload. This ordering is the structural guarantee against orphan tellings.

## 4.3 Transaction and commit boundaries

Ordered commit with explicit checkpoints, consistent with the existing post-root async checkpoint model (Master/map C-7GA, RC-1…RC-8):
1. The parent reading is written and durably committed first (existing built behavior; unchanged).
2. The **prepared-telling manifest** for that reading is written and made durable (every expected telling's exact payload + integrity digest).
3. A telling-creation checkpoint is opened for that reading, keyed by the parent reading's operation identity.
4. Each telling is committed as a first-class card, each carrying its own `telling_creation_operation_key` and derived `telling_idempotency_key`, and each integrity-checked against its manifest entry (§3 rule 5) before it is treated as canonical.
5. A telling-creation-completed checkpoint is appended once all expected cards for that reading are durably committed and integrity-valid.

The parent reading's commit is never deferred or made dependent on telling creation; root ingestion and reading commit never block on telling creation. If telling creation fails after the reading commits, the reading stands and telling creation is recoverable from the manifest.

## 4.4 Zero, one, or several tellings

- **Zero tellings** (empty `story_layer`, legal): no cards and no manifest payloads are created; the checkpoint records a **zero-telling sentinel** — an explicit positive completion fact, not silence — distinguishing "legitimately no tellings" from "creation never ran." The zero-telling sentinel satisfies the §5A eligibility gate.
- **One telling:** one manifest payload, one committed card, one completion checkpoint.
- **Several tellings:** one manifest payload per telling; each card committed under its own operation/idempotency identity; the single completion checkpoint appended only after **all** are durably committed and integrity-valid. Conflicting tellings within the same reading remain separate cards — never merged at creation.

## 4.5 Operation identity / idempotency (canonical naming)

- `telling_creation_operation_key` — scopes **one telling-creation operation within one reading-pass**. Derived deterministically from stable inputs that uniquely identify *that telling of that reading*: at minimum the `parent_reading_id`, the stable per-telling discriminator (`embedded_entry_correspondence`), and a telling-operation version tag. This mirrors the existing operation-keyed pattern in the post-root path (e.g. `reading_idempotency_key = hash(enqueue_key + "reading_v1")`, and operation-keyed clash/Computed-View sentinels).
- `telling_idempotency_key` — the **record-level** idempotency identity stored on the card, **deterministically derived from** `telling_creation_operation_key` (e.g. a further keyed derivation tagged `telling_v1`). Unique per store; the writer rejects an already-committed key.
- **Relationship and scope:** the operation key identifies the *operation* (and is what recovery re-derives to find or commit the right card); the idempotency key identifies the *record* (and is what the writer's duplicate check rejects). One operation key yields exactly one idempotency key. `telling_id` is a third, separate thing: the **permanent identity**, allocated once and preserved across all lifecycle states.

## 4.6 Duplicate prevention

Before committing a card, the writer checks whether a card with that `telling_idempotency_key` already exists. If it does, the existing card stands and no second card is written — idempotent. The same rule governs materialization: a second materialization of the same embedded entry derives the same operation/idempotency identity and creates no duplicate.

## 4.7 Partial-completion detection

A reading that is committed but whose telling-creation-completed checkpoint is absent is a partial completion: cards may be all, some, or none committed. Detection relies on the per-reading checkpoint and the manifest's record of expected tellings, not on counting cards blindly.

## 4.8 Fail-closed handling at every commit/checkpoint boundary (corrects v1.0 Issue 1)

Each case below closes in the safe direction; the immutable parent reading is never rewritten in any case:

- **Prepared manifest exists but parent reading does not.** Fail closed: do **not** commit any card (a card requires a durably committed parent reading). Record the integrity/ordering anomaly (§10). The manifest entry is preparation only; with no parent reading it can never become a valid card. No orphan card is ever produced.
- **Parent reading exists but no telling cards exist.** Use the manifest to commit the missing cards from their exact payloads (idempotently); integrity-check each against its manifest entry; append the completion checkpoint once all expected cards are durably committed and valid. If the manifest itself is absent (e.g. crash before step 2 completed), no exact payload exists; the engine **must not** regenerate or reinterpret — the telling-creation operation for that reading is left explicitly incomplete and recoverable only through a re-run of the producing pass under its own idempotency (a *new* pass that re-derives the same identities), never through invention. The parent reading stands; telling-level fan-out stays blocked (§5A).
- **Only some telling cards exist.** Commit the remaining cards from their manifest payloads (idempotently — present keys skipped); integrity-check each; append the completion checkpoint only once the **complete** expected set is durably committed and valid.
- **All telling cards exist but the completion checkpoint is absent.** Confirm via idempotency keys and integrity checks that every expected card is durably present and valid; if so, append the missing completion checkpoint **without writing any new card**. If any expected card is missing or integrity-failed, fall to the cases above; the checkpoint is never appended while any expected card is absent or invalid.
- **Prepared payload or committed card fails integrity validation.** Fail closed: the affected card is **not** treated as canonical and **must not** be available as a downstream link target (§3 rule 6, §5A). Record the integrity failure (§10) without rewriting either immutable source. No silent reconciliation, normalization, or selection of the divergent card.

**General fail-closed rule.** On any system failure during telling creation: the parent reading stands (already committed); no partial, malformed, or integrity-failed card is left as if valid or canonical; no completion checkpoint is appended; the partial state is left explicitly recoverable from the manifest; the system never reports telling creation complete on failure; a half-written or divergent card is never exposed as a usable link target.

## 4.9 Retryable vs terminal failures

A transient technical failure during telling creation (I/O error, lock contention, process interruption) is **retryable**: re-attempted under the same operation/idempotency identities, with idempotency and the manifest guaranteeing no duplication and no reinterpretation. A failure that is not transient — a payload that cannot satisfy the required-field contract (missing `parent_reading_id`, missing `evidence_relationship`, broken provenance), or an integrity-invariant failure — is **terminal for that card**: the card is not committed as canonical, the failure is recorded as a distinct reason (§10), and the engine never silently substitutes a degraded or regenerated telling. Bounded retry **values** (attempts, timing, backoff) are inherited from the open system-wide retry policy (B9) and are **not chosen here**; until adopted, a substantively rejected card is terminal.

## 4.10 Orphan and duplicate prevention (restated)

- **No orphan tellings:** a card is only ever committed after its parent reading is durably committed and its manifest entry is durable; every card carries a required `parent_reading_id`. A card can never reference a non-existent reading.
- **No duplicate cards after crash/retry:** the deterministic `telling_creation_operation_key` → `telling_idempotency_key` derivation plus the pre-write duplicate check guarantees any re-run finds the existing card and writes no second one; recovery commits from the manifest under the same identities.

---

# 4A. EMBEDDED-FIELD NO-LOSS MAPPING AND LEGACY-MATERIALIZATION RULE (corrects v1.0 Issue 2)

## 4A.1 Field-by-field mapping contract

Every existing embedded field (`whose · stance · firmness · telling · theme · when`) maps to the first-class architecture as follows. **Every original populated value is preserved exactly; no populated value is silently reinterpreted; omitted values are preserved as honestly absent (never invented, never `"unknown"` where omission is required).**

- **`whose` →** carried forward as a **preserved legacy value** (`legacy_whose`, retained exactly as emitted). It is **not** silently mapped into `root_speaker`, `subject`, or `perspective_owner` unless the source explicitly supports that mapping. Where the source does not disambiguate which structured role the flat `whose` denotes, the structured roles that cannot be grounded are **omitted** (honest absence), and `legacy_whose` preserves the original value for inspection. (The Master itself states the flat `whose` field may remain for v1 compatibility while future schema uses the structured fields — §7K line 2198; this mapping honors that without inventing role assignments.)
- **`stance` →** preserved as its own `stance` value **explicitly**, exactly as emitted. It is **never** assumed to be derivable from, or already contained in, the general `telling` text. Omitted when the embedded entry had no `stance`.
- **`firmness` →** carried forward as `firmness` exactly when present. If the legacy embedded `firmness` has **no recorded evidence basis** (the embedded schema carried no `firmness_evidence_basis`), see §4A.2 — a basis is **never invented** to satisfy the new contract.
- **`telling` →** carried forward as `telling`, unaltered.
- **`theme` →** carried forward as a **preserved legacy theme value with its provenance** (`legacy_theme`), retained exactly. It is **not** automatically treated as a confirmed theme. Under the hybrid theme system (Master §7K lines 2206–2216) only Ness confirms themes; a legacy `theme` value is preserved as-emitted with whatever provenance it carried, and remains unconfirmed unless and until Ness confirms it through the theme process (not invented here). A `legacy_theme` is never silently promoted to a confirmed theme link.
- **`when` →** carried forward as `embedded_when` exactly (§2), kept **distinct** from `created_at` (record creation time) and from `source_event_time` (source/event time when the source supports it). Omitted when the embedded entry had no `when`.

**Three time concepts kept distinct (required by the instruction):** `created_at` (record creation time) ≠ `embedded_when` (original embedded `when`) ≠ `source_event_time` (source/event time when available). None is collapsed into another; each is omitted rather than guessed when unavailable.

**Parent-reading confidence and other uncertainty remain inspectable through `parent_reading_id`, never copied into a competing authority.** The reading's two-slot `confidence` object (`{interpretation_confidence, source_reliability}` — Master §6B line 539) and any other reading-level uncertainty are **not** copied onto the telling card. They remain on the immutable parent reading and are reached by following `parent_reading_id`. This keeps one authority for reading-level confidence (the reading) and one for telling-level firmness (the card), with no second competing copy. Firmness on the card stays separate from the reading's model-confidence object (Master §7K line 2202).

## 4A.2 Fail-closed legacy-materialization rule

Existing embedded entries may lack fields the first-class contract makes mandatory — structured perspective roles, `evidence_relationship`, `firmness_evidence_basis`. For materialization of such entries:

- **Missing mandatory information is never invented.** No default, no inferred role, no fabricated evidence relationship, no manufactured firmness basis, no `"unknown"` placeholder where the contract requires real content.
- **An incomplete legacy entry must not become a valid first-class telling card merely to satisfy migration.** Validity requires the mandatory fields to be genuinely present; an entry that cannot supply them is **blocked**, not force-fitted.
- **The blocked materialization operation is recorded with its exact missing requirements** (§10): which embedded entry, which mandatory fields are absent, why it cannot become a valid card.
- **The original embedded entry is preserved unchanged.** It stays inside its immutable parent reading exactly as emitted.
- **It remains unavailable as a valid first-class telling-level link target** until a separately valid future process — a reread that produces a new complete reading and new complete telling, a supported human annotation, or another authorized process — creates a **new complete telling** (with a new `telling_id`). The blocked legacy entry is never retroactively completed in place.
- **No new evidential or annotation policy is chosen here.** What counts as a valid future reread, a supported annotation, or an authorized completion process is open (A-policy / B-mechanics as applicable); this rule fixes only that incompleteness fails closed and is never resolved by invention.

---

# 5. QUARANTINE AND PRODUCTION SEPARATION — DERIVED/EVENT LIFECYCLE (corrects v1.0 Issue 3)

**The boundary being preserved (Master/map: Engine C writes to quarantine, never directly to production; production readings store absent by design — Decision Defaults line 81, Master §6B "PRODUCTION READINGS AUTHORIZATION" lines 454–461):**

- Engine C writes readings to **quarantine**, never directly to production. Unchanged.
- **The immutable telling core is never edited when the parent reading changes state.** (Corrects v1.0, which placed a `storage_status` inside the immutable card while requiring it to follow the parent reading's later state — a contradiction.) A telling card, once written, is immutable; lifecycle change never mutates it.
- **Effective lifecycle eligibility is derived or event-based, never a mutable field:**
  - **Derived:** a telling's effective quarantine / production / visibility / rejection / retention eligibility is **derived from its parent reading's valid append-only lifecycle state.** The reading's state is the source of truth; the telling inherits it by reference through `parent_reading_id`.
  - **And/or event-based:** where a telling-specific lifecycle fact must be represented, it is recorded as a **separate append-only lifecycle event** that points to the `telling_id` (never edited into the card). Such events are append-only and never rewrite history.
- **A telling can never become more eligible or more promoted than its parent reading.** This invariant holds structurally because eligibility derives from the parent reading; there is no independent telling promotion state that could outrun the reading.
- **The same permanent `telling_id` is unchanged across all later lifecycle states.** Promotion, rejection, retention, or visibility change never mints a new id and never retires it.
- **`telling_id` cannot collide merely because quarantine and production are separate locations.** Identity is the `telling_id` value, not the storage location. A telling in quarantine and (if ever promoted) the same telling in production are **one identity**, not two records competing for canonical status. (How a promotion is physically represented — same record referenced from a production index, or an append-only promotion event, or another mechanism — is part of the still-open production-promotion procedure and is **not chosen here**; the invariant fixed here is one-identity-across-locations.)
- **No production store is created here**, and **no new promotion policy is invented.** The existing production-readings authorization (Ness's deliberate `.nh_readings_production_authorized` marker plus Cursor's approved dry-run) is unchanged and untriggered by this package. Any promotion-policy detail not already settled remains **explicitly open**.

**Open here, named:** the exact telling-promotion procedure (how a telling's effective eligibility is updated/represented when its parent reading is promoted, and the operation identity of that event) follows whatever production-promotion design is later authorized. This package fixes only the invariants — immutable core, derived/event eligibility, never-more-promoted-than-parent, one identity across locations.

---

# 5A. TELLING-COMPLETION ELIGIBILITY GATE (corrects v1.0 Issue 4)

No telling-level downstream operation may proceed until the telling set for a reading is complete and valid.

**The gate.** Until **either** the **zero-telling sentinel** (§4.4) **or** the **complete valid set of expected first-class telling cards plus the telling-creation-completed checkpoint** (§4.3–§4.8) exists for a reading, **no telling-level downstream operation that depends on that reading's tellings may proceed.**

**What must wait (and must never substitute).** C-7K, C-7L, C-7J telling-level links, C-7M, C-7D, §7Q derivative traversal, B2, B3, B4, and B5 **must not use**:
- an **embedded telling as a substitute** for its missing first-class card;
- a **partial telling-card set** (some cards present, completion checkpoint absent);
- an **integrity-failed telling card** (§3 rule 6, §4.8).

**The parent reading may remain durably committed.** Only the **telling-specific fan-out** waits. Reading-level downstream work that does not depend on telling-level cards is not blocked by this gate; root ingestion and reading commit are never blocked (§4.3).

**Idempotent resume.** Once recovery completes the valid card set and appends the completion checkpoint (or the zero-telling sentinel is present), telling-level fan-out **resumes idempotently** — consumers proceed exactly once against the now-complete set, with their own duplicate-prevention intact; the wait-then-resume produces no double work and no double evidence.

**Logging.** Every **block** (a telling-level operation refused because the gate is not satisfied), every **recovery** step, every **no-op** (an idempotent skip), and every **resumed fan-out** is recorded under §0B one-operation/one-log, with no-double-evidence (§10). A block is an inspectable event; a resume is an inspectable event; neither adds certainty to any telling's correctness.

---

# 6. CROSS-COMPONENT TELLING-ID CONTRACTS

*(Preserved from v1.0 unchanged in substance. A2 unlocks exactly one thing for downstream components: a stable `telling_id` they may point at — and, per §5A, only once the telling set is complete and valid. This section defines only that identity interface; it does not complete any consumer's own schema, which remain B2/B3/B4/B5 and the respective A-policies.)*

**Universal rule for every consumer below:** a downstream reference points to the stable `telling_id` and, through it, preserves access to the parent reading and the supporting roots. **Links are never copies.** A link never copies or silently rewrites the original telling; the telling stays where it is and the consumer holds a reference plus its own link metadata (what it connects, why-by-pointer, who established it, certainty, timestamp — per Master §7L line 2226 where applicable). **No consumer may point at a telling that has not passed the §5A gate.**

- **C-7K Story Layer (owner).** Holds the first-class telling cards. Organizes tellings by perspective/theme/time using `telling_id` as the stable handle. Connections across time are explicit navigational links keyed on shared attributes (same `perspective_owner`/`whose`, same theme, same thread/source, overlapping time, shared root ids) — navigational links, not logical merges, always labeled with their basis and always pointing back to supporting roots and readings (Master §7K line 2190).
- **C-7L Person-Boxes.** Links story tellings in which a person appears in any perspective role, by `telling_id`. The link record preserves what/why/who-established/certainty/timestamp. Linking a telling never copies it and never promotes it to a fact about the person. *(Person-Box evidence/merge policy remains A5; link-schema mechanics remain B4.)*
- **C-7J Clash Handling (where telling-level links are used).** A clash record points to the exact readings and roots involved (Master §7J line 2160); where a clash is between *tellings* specifically, it may additionally point to the `telling_id`s involved. The same clash never produces two records (later detection appends a detection-history event). Clashes are surfaced, never resolved; pointing at conflicting tellings never selects a winner. *(Clash-record schema specifics remain B2; clash-response downstream policy remains A9.)*
- **C-7M Computed View.** Lists tellings among its source-object types (Master §7M line 2262), referenced by `telling_id`, linked never copied. Seven-factor ordering and internal-only rules unchanged; telling identity gives a stable handle, nothing more. *(Snapshot-schema structure remains B5; relevance mode remains A4.)*
- **C-7D Living State Web.** Story tellings are eligible source objects for state nodes (Master §7D lines 645, 655), referenced by `telling_id`. The grounding rule still requires immediate source-object ids plus direct root ids and a fully inspectable chain; circular support remains forbidden; Story-Layer firmness rules apply when tellings are used as evidence. Telling identity supplies the stable source-object id; it supplies no evidential weight. *(Living State Web evidence/currentness/domain policy remains A6.)*
- **§7Q deletion / dependency discovery.** Dependency discovery must locate telling records and their links (Master §7Q line 2442 lists "story tellings"). A stable `telling_id` plus required parent-reading and supporting-root provenance is what makes a telling discoverable and its derivatives traceable. No telling may bypass privacy, restriction, sealed-isolation, or visibility handling through a secondary index or link (§9). *(Privacy/influence-removal policy remains A7; deletion remains non-destructive visibility removal under the settled current rules.)*
- **C-ENGINE-C.** Emits tellings into `story_layer` and, under §3–§4A, into first-class cards via the manifest. May rely on `telling_id` now that A2 is settled — but Engine C construction/testing/implementation remains blocked (A1 gold first; design completion; Ness authorization). This package authorizes the *identity Engine C will emit*, not Engine C's construction.
- **B3 theme and telling-link structure.** May use `telling_id` as the telling end of a telling-to-theme link (§7). Theme schema, similarity grouping, confirmation thresholds remain open (B3 structure; A5-adjacent policy).
- **B4 Person-Box link schema.** May use `telling_id` as a linkable target type. Schema mechanics remain B4.
- **B2 clash-record schema (where applicable).** May include `telling_id`s where a clash is telling-level. Schema specifics remain B2.
- **B5 Computed-View snapshots (where applicable).** May reference `telling_id`s in immutable snapshots. Snapshot schema remains B5.

---

# 7. THEME-LINK BEHAVIOR UNLOCKED BY A2

*(Preserved from v1.0 unchanged in substance. A2 unlocks only the mechanical telling-to-theme link identity — that a theme link's telling end is a stable `telling_id`. It does not choose theme policy.)*

**Link identity (what A2 settles):** a telling-to-theme link connects a `telling_id` (telling end) to a theme (theme end), recording the link as a first-class connection with its own provenance (what it connects, who/what proposed it, why-by-pointer, timestamp, uncertainty), never as a copy of the telling and never as an assertion that the theme is a fact.

**Preserved (Master §7K HYBRID THEME SYSTEM, lines 2206–2216 — binding):**
- Themes are navigation categories, never facts.
- Engine-proposed themes remain `proposed`; only Ness confirms.
- One telling may have zero, one, or several theme links; membership is not exclusive.
- Repetition does not confirm a theme; a theme cannot validate itself by being frequently proposed.
- Circular support is prohibited — pattern-derived themes must retain root support; a telling-to-theme link must not become a path by which a theme validates itself without root grounding.
- Theme use in later retrieval remains auditable — if a confirmed or proposed theme is used to retrieve context for a future engine pass, that influence must appear in the retrieval audit trail (Master §7K line 2214).
- *(Connected consequence of §4A:)* a `legacy_theme` value carried forward from an embedded entry is preserved with its provenance and is **not** a confirmed theme; it becomes a confirmed theme link only through Ness's confirmation, never automatically.

**Not chosen here (open):** theme-confirmation thresholds, theme similarity policy, theme schema structure, any A5-adjacent evidence policy. B3 carries the theme/telling-link *structure* after A2 fixes the seam; thresholds are A-policy. This package fixes only that the telling end of a theme link is the stable `telling_id`.

---

# 8. CORRECTIONS AND REREADING

*(Preserved from v1.0 unchanged in substance.)*

**Preserved (Master §7K, §7H reread lifecycle, and the no-loss list — binding):**
- A reread creates a **new reading** beside the old; it never overwrites (Master §6B "a re-read is a NEW reading beside the old," line 535).
- New tellings from that reread receive **new `telling_id`s** — new first-class records, not edits of earlier tellings.
- Earlier tellings remain intact, immutable, fully inspectable.
- No "current telling" operation exists that could rewrite history. No mutable "latest" telling supersedes earlier ones in place.
- Connections across time are **explicit navigational links**, not logical merges — they point, they do not combine, and they always carry their basis.
- Temporal change and contradiction remain **distinguishable**: link metadata records whether two tellings represent a change over time or a contradiction; neither is collapsed into the other (Master §7K line 2184).
- No automatic supersession and no truth winner may be invented. A later telling does not automatically defeat an earlier one; only Ness, off-board, judges — and even then his judgment is recorded as a separate event and never rewrites the readings, roots, or tellings (Master §7J lines 2170–2176).

**Mechanical consequence for telling identity:** each reread yields new readings and therefore new tellings with new ids under fresh operation/idempotency identities (and their own manifest entries); the idempotency and duplicate-prevention rules of §4 apply unchanged; a reread never collides with or overwrites an earlier telling's id. *(The reread mode-assignment rule remains A25; reread operation-identity wiring remains B10 — not closed here.)*

---

# 9. PRIVACY, DELETION, RELEVANCE, AND AUTHORITY BOUNDARIES

*(Preserved from v1.0 unchanged in substance.)*

**Preserved (Master §7Q, §7R, §0B, §7P — binding):**
- **§7Q governs eligibility and handling.** A telling is subject to §7Q as any derived object. Telling identity creates no new access path around §7Q.
- **Deletion remains non-destructive visibility removal** under the settled current rules (Master §7Q lines 2440–2457): removes from ordinary visible output while content remains preserved internally; stopping internal influence is a separate explicit Ness instruction with its own scope and record; a history record (not a content-free tombstone) documents what was removed, when, and by what authority.
- **Dependency discovery must locate telling records and their links** (Master §7Q line 2442). The stable `telling_id` plus required provenance is what makes a telling and its derivatives findable in a deletion case — a reason the first-class record must carry those links, not an optional convenience.
- **No telling may bypass privacy, restriction, sealed-isolation, or visibility handling through a secondary index or link.** A telling-level link is not a back door: following a `telling_id` is still subject to the same §7Q visibility-vs-internal-use distinction and the same Level-1/Level-2 protections (Master §0B "ACCESS AND AUTHORIZATION BOUNDARY," line 257). A link's existence never grants visibility the underlying telling would not have.
- **§7R relevance never determines truth, authority, or permission** (Master §7R; Decision Defaults). A telling being relevant never makes it true, grants permission to act, or resolves a clash. §7Q runs before §7R on derived operations.
- **Ness remains the sole decider.** Telling identity makes a telling *addressable*; never *authoritative*. The engine never closes; only Ness affirms, off-board.
- **Telling identity does not make the telling factual or authoritative.** A first-class telling record is still a weightless, dated, evidence-tagged, rejectable interpretation (Decision Defaults SMART-machinery law, line 46) — being a first-class object changes addressability, never epistemic status.

**Not decided here (open):** any open A7 privacy policy and any influence-removal policy remain reserved to Ness. This package introduces no privacy, restriction, or deletion *policy* — only the identity that §7Q's existing dependency-discovery requirement already presupposes.

---

# 10. §0B LIVING-RECORD LOGGING

Per §0B (Master lines 233–259): every real operation creates one append-only living-record log; **one operation, one log**; a log proves an operation occurred and **never becomes double evidence** that the underlying telling is true; no silent operation. Logs are subject to §7Q access/authorization and §25 identity/security authorization where applicable. Component-specific logging:

- **Telling-record creation** — one log per card committed (`telling_id`, `telling_idempotency_key`, that a first-class card was created). Creating the log does not itself create a second log.
- **Prepared-manifest creation** *(new in v1.1)* — one log when a reading's prepared-telling manifest is made durable (which reading, how many expected tellings, integrity digests recorded), so recovery material's existence is itself inspectable.
- **Parent-reading and root linkage** — recorded with creation: `parent_reading_id` and `supporting_root_ids`, so the grounding chain is inspectable.
- **Materialization from an embedded entry** — one log per materialized card, recording that it was materialized (not freshly emitted) and from which embedded entry.
- **Blocked legacy-materialization** *(new in v1.1)* — one log per blocked legacy entry, recording the exact missing mandatory requirements and that the original embedded entry is preserved unchanged (§4A.2).
- **Duplicate-prevention result** — recorded when a write is skipped because the `telling_idempotency_key` already exists, so the idempotent no-op is visible once.
- **Integrity-check result** *(new in v1.1)* — recorded for each card's correspondence/integrity check (§3 rule 5): pass, or an integrity failure with what mismatched, without rewriting either immutable source.
- **Partial-completion recovery** — recorded when recovery detects a missing completion checkpoint or missing/invalid cards and what it did (which keys it committed from the manifest, which it skipped, when it appended the completion checkpoint or zero-telling sentinel).
- **Eligibility-gate block / resume** *(new in v1.1)* — recorded for each telling-level downstream operation **blocked** by the §5A gate, and for each **resumed** fan-out after the set becomes complete; each is an inspectable event that adds no certainty to any telling's correctness.
- **Retry or terminal failure** — distinct reason types per the §4.9 taxonomy: a retryable technical failure logged as such; a terminal validation or integrity failure logged as a distinct terminal reason, never silently relabeled.
- **Telling-level link creation** — one log per downstream link established to a `telling_id` (Person-Box link, theme link, clash telling-pointer, Living-State-Web source reference, Computed-View reference): what was linked, by which component, its provenance pointer.
- **Rejected or blocked downstream use** — recorded when a link or use is blocked (a quarantined telling refused as production material; a §7Q visibility block; a §5A gate block; an integrity-failed card refused as canonical), so the block is inspectable.
- **Schema/version provenance** — every card and every telling-level link carries the `schema_version` / producer-version provenance tracing it to the exact producing logic and model.

**No-double-evidence reminder, binding on all of the above:** repeated logs about a telling — its creation, manifest, integrity check, use, linking, blocking, resuming — never add certainty that the telling is *correct*. One underlying telling must not become several independent votes for itself (Master §0B line 243). Logging records that operations happened; it never strengthens the interpretation.

---

# 11. DESIGN-COMPLETE CONDITIONS FOR THIS PACKAGE

**What A2 closes (and only this):** the telling **object-identity choice** — separate first-class immutable telling record with a permanent stable `telling_id` — and the **directly unlocked mechanical identity/reference design**: the first-class telling-record contract (§2), the one non-contradictory relationship to the existing immutable embedded `story_layer` entry **plus the correspondence/integrity invariant and divergence fail-closed** (§3), the creation/persistence/**exact-payload-recovery**/idempotency/fail-closed mechanics with the **durable prepared-telling manifest** (§4), the **field-by-field no-loss mapping and fail-closed legacy-materialization rule** (§4A), the quarantine-subordination invariant via **derived/event lifecycle with no mutable status field** (§5), the **telling-completion eligibility gate** (§5A), the downstream telling-ID identity interface (§6), the telling-to-theme link identity (§7), the reread "new id per new telling" rule (§8), the §7Q discoverability and no-bypass invariants (§9), and the §0B component logging (§10).

**What A2 does not close (explicitly open, owners named):**
- Firmness scale, labels, evidential thresholds, scoring method — open (Master §7K; A-policy where evidential weight is judged).
- Theme schema, similarity grouping, confirmation thresholds, retrieval-influence policy — open (B3 structure; A5-adjacent policy).
- Person-Box evidence/merge policy (A5); Person-Box link-schema mechanics (B4).
- Clash-response downstream policy (A9); clash-record schema specifics (B2) beyond the telling-pointer interface.
- Relevance-mode policy (A4); Computed-View snapshot schema (B5) beyond the telling-reference interface.
- Living State Web evidence/currentness/domain policy (A6); node/edge schema (B6).
- Privacy / influence-removal policy (A7).
- Substantive "grounded enough" threshold (A31).
- A1 story-bearing gold cases — the separate Register-A item; **not reopened, not reconstructed here**. This package neither confirms nor questions the A1 substantive decision.
- Engine C construction, testing, implementation — blocked.
- Production-store schema; any disk migration; any materialization run — blocked / separately authorized.
- Bounded retry *values* for telling-creation failures (B9); reread operation-identity wiring (B10); the production-promotion procedure for tellings, including how a promotion is physically represented across quarantine/production locations (follows later authorized production design).
- What counts as a valid future reread, supported annotation, or authorized completion process that could complete a blocked legacy entry (§4A.2) — open (A-policy / B-mechanics as applicable).

**The package is design-complete for A2 when:** the telling object-identity is fixed as a separate first-class immutable record with a permanent `telling_id` unchanged across all lifecycle states and locations (§1–§2); a single non-contradictory relationship to the existing immutable reading/`story_layer` is specified with no second editable authority, a verifiable correspondence/integrity invariant, and divergence failing closed (§3); allocation, transaction boundaries, the zero/one/several cases, deterministic operation/idempotency identity, duplicate prevention, partial-completion detection, **exact-payload recovery via a durable manifest that never regenerates or reinterprets a telling**, fail-closed handling at every commit/checkpoint boundary, retryable-vs-terminal handling, and orphan/duplicate prevention are all specified implementation-neutrally (§4); the field-by-field embedded mapping preserves every value and conflates no time concept, and incomplete legacy entries fail closed without invention (§4A); the quarantine-subordination invariant is expressed with no mutable status field, derived/event eligibility, never-more-promoted-than-parent, and one identity across locations (§5); telling-level fan-out is gated until the set is complete and valid, resuming idempotently (§5A); the downstream identity interface, theme-link identity, reread rules, §7Q boundaries, and §0B logging are specified (§6–§10) — **with every dependency above left explicitly open and owner-named, and no concept, threshold, or policy invented.** These conditions are met by this candidate, subject to ChatGPT's independent audit and Ness's acceptance.

---

# 12. PACKAGE SELF-AUDIT (internal; full delivery audit accompanies the file)

- **Authority:** Master V10 treated as adopted/authoritative; subordinate sources not promoted; candidate status explicit; no authority inversion. **PASS.**
- **Preservation vs v1.0:** all correct v1.0 material retained; §6/§7/§8/§9 preserved in substance; §2/§3/§4/§5/§10/§11/§12 corrected; §4A/§5A added; v1.0 itself untouched on disk. **PASS.**
- **Concept fidelity:** the separate-card decision is unchanged and remains the basis of every mechanic; the rejected address-style identity is still excluded. **PASS.**
- **Issue 1 (exact-payload recovery):** durable prepared-telling manifest defined; recovery uses exact payloads and never reruns the model or reinterprets the root; fail-closed handling at every boundary; immutable parent reading never rewritten. **PASS.**
- **Issue 2 (field-by-field no-loss mapping):** every embedded field mapped with exact preservation, no silent `whose`→role mapping, explicit `stance`, three distinct time concepts, legacy `theme` not auto-confirmed, parent confidence inspectable via `parent_reading_id` not copied, omissions honest; fail-closed legacy-materialization rule with no invention. **PASS.**
- **Issue 3 (immutable record vs mutable status):** `storage_status` removed from the immutable core; eligibility derived/event-based; `telling_id` constant across lifecycle and locations; never-more-promoted-than-parent preserved. **PASS.**
- **Issue 4 (divergence & partial-completion eligibility):** correspondence/integrity invariant defined; divergent card fails closed and is barred from canonical use without reconciliation; telling-completion eligibility gate blocks all telling-level fan-out until complete-and-valid, resuming idempotently. **PASS.**
- **Operation identity:** one canonical record-level `telling_idempotency_key`; the wider `telling_creation_operation_key` given distinct scope and a deterministic derivation relationship; `telling_id` separate from both. **PASS.**
- **Logging:** §0B one-operation-one-log, no double evidence, new manifest/integrity/blocked-materialization/gate events specified, §7Q/§25 access noted. **PASS.**
- **Wiring / DUMB-SMART / root-reading / quarantine-production / Layer-2-Layer-3:** telling identity is SMART-side and weightless; roots/readings immutable; tellings subordinate to the parent reading's state; no Layer mixing introduced. **PASS.**
- **No implementation:** no code, no patch-ready pseudocode, no migration, no store creation, no seal lifting, no disk modification. **PASS.**

---

*End of `NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_1_CANDIDATE` — CANDIDATE, unaudited, awaiting ChatGPT independent audit and Ness's explicit acceptance. v1.0 and every authority/source file remain unchanged; no implementation was performed.*
