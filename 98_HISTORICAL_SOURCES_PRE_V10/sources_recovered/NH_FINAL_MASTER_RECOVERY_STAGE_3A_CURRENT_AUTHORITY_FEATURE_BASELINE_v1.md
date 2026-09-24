# N.H — FINAL-MASTER RECOVERY — STAGE 3A: CURRENT-AUTHORITY FEATURE BASELINE v1

**What this is.** The first real feature-recovery pass (Stage 1 v1.3 §9.1 step 3, scoped to the current
authority set only). It reads the complete bodies of the four current-authority files and the two
accepted companion bodies, and recovers every present feature, mechanism, subsystem, safeguard,
workflow, storage structure, interface behavior, and unresolved design area in them. It then compares
the two accepted companions against the **current Master only** to establish integration status.

**Sources read (full bodies):** SRC-044 `NH_MASTER-19_CORRECTED_v7_1.md`; SRC-015
`NH_DECISION_DEFAULTS-S19_v2_2.md`; SRC-076 Cursor Rules v3.2; SRC-087 governance/archive companion
(which embeds the two accepted companions verbatim in Parts II and III, a wellbeing design-source
snapshot in Part IV, and a superseded MASTER-19_FULL in Part V); SRC-001 accepted security/identity
designs; SRC-002 accepted TSC design. Exact line ranges are in §6.

**What this is NOT.** No comparison of historical Master versions; no judging which conflicting design
is better; no resolving architecture questions; no decisions for Ness; no integration or patching; no
authority-file change; no final-Master organization; no canonical drafting; no Stage 3B.

---

## 0. READING CONVENTIONS AND STATUS-LABEL MAPPING (read first)

**This audit is document-based.** It read the authority and companion bodies. It performed **no fresh
disk inspection** of Ness's machine. Therefore, wherever the Master documents something as built and
verified on disk, this audit records it as **documented**, never as freshly re-verified. The label
`BUILT AND DOCUMENTED AS VERIFIED` below means exactly that: the authority documents disk verification
(S12–S16); this audit did not re-run the check. Where the Master itself flags a built item as not
re-verified, the label `BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT` is used.

**Mapping the Master's own design tags to the required status labels:**
- `[BUILT & VERIFIED]` → **BUILT AND DOCUMENTED AS VERIFIED** (subject to the no-fresh-verification note above).
- `[CONCEPTUALLY DESIGNED, NOT BUILT]` / `[CORE CONCEPTUALLY DESIGNED, NOT BUILT]` → **FULLY DESIGNED — NOT BUILT** at the conceptual/structural level. Each such section names implementation details that "remain undesigned"; those are listed per-feature in field 10 and consolidated in §5. "Fully designed" here means the conceptual design is complete, **not** that implementation is specified.
- `[PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]` → **PARTIALLY DESIGNED**.
- `[DESIGNED]` (full spec, not built) → **FULLY DESIGNED — NOT BUILT**.
- `[DESIGNED-IN-PROGRESS]` / `[IN-PROGRESS DESIGN]` → **PARTIALLY DESIGNED**.
- Companion `ACCEPTED DESIGN — NOT YET BUILT`, judged against the Master → **ACCEPTED — NOT YET INTEGRATED** or **ACCEPTED — PARTLY INTEGRATED** (see §4).

**Strict distinctions enforced throughout:** designed ≠ built; accepted ≠ integrated; mentioned ≠ fully
specified; a Master "previously verified" claim ≠ fresh disk verification; an external companion may
remain authoritative within its own scope even when not integrated into the Master.

Each feature entry uses the 10 required fields: **(1) name · (2) purpose · (3) runtime behavior ·
(4) inputs · (5) outputs/records · (6) info it stores/reads/changes/seals/restricts/exposes ·
(7) dependencies · (8) authority source + line range · (9) status · (10) limits / safety / open
questions.**

---

# 1. PRESENT-FEATURE INVENTORY (grouped by subsystem)

## A. Foundational premise and frame

**A1 — The Premise (never decide facts / never close the book).**
(1) The floor rule under every other rule. (2) Stops reasoning from hardening into a closed, settled
fact; the AI may reason, connect, lean, wonder — never close the book or promote a conclusion to
"real." (3) Every conclusion stays a non-decisive, accreting layer; Ness decides off-board in real
life, never as an engine step; recording *that* he reacted is allowed, the truth-verdict is not.
(4) Any engine conclusion. (5) Behavioral constraint, not a record. (6) Restricts what any component
may assert as fact. (7) Governs every subsystem. (8) Master §0 (L174–190). (9) FULLY DESIGNED — NOT
BUILT (a principle, enforced where components are built). (10) "Hold firmly" ≠ "close"; the DUMB
machinery may establish directly-verifiable machine-state/provenance facts, the SMART machinery never
silently promotes interpretation to fact.

**A2 — The Two Machineries (DUMB vs SMART / psychologics) + the membrane.**
(1) Top-level architectural frame splitting the system into data-moving vs person-reading halves.
(2) DUMB moves/holds data and is safe because it cannot interpret; SMART reads the person and is safe
because it cannot close; the membrane is the boundary. (3) DUMB: append/point/carry/sort/gather only.
SMART: everything weightless, dated, confidence-tagged, rejectable. (4)/(5) Framing, not I/O.
(6) Defines which components may assert facts. (7) Underlies the store, two-file split, person-box
gather (DUMB) and the meaning webs, story layer, clash, wonder, NOTE (SMART). (8) Master §0A (L193–204);
DD §2 (L42–50). (9) FULLY DESIGNED — NOT BUILT (frame; §0A placement still open — see A-note).
(10) Open pins (§11 item 17 / DD §5): whether the name is "SMART" or "psychologics"; where the NOTE and
clash sit within the frame. Pure-tape redaction path and "absence-is-read" guard are flagged needs.

**A3 — What N.H is / two destinations / two purposes.**
(1) Defines the system: sovereign local memory+meaning helper; "Jarvis is the memory + soul + gathering
+ mouth wired together," not the model. (2) Every eligible accepted input goes to TWO places — a sealed
raw root and a reading beside it (why there are two files); runs INWARD (mirror of Ness's own thinking)
and OUTWARD (translate new data through his lens) at once. (3) New input is read by the webs and lands
as a reading; growth lands in memory, never the frozen mouth. (4) Any eligible input. (5) Root +
reading. (6) Reads inputs; writes roots/readings. (7) Accretive store, filter/engine, mouth.
(8) Master §1 (L208–223), §1A (L227–231); DD §1 (L32–38). (9) FULLY DESIGNED — NOT BUILT as a whole
(its built parts are inventoried in C/D). (10) הכל יחסי — meaning is never final, always relative and
relative-to-whom.

## B. The machine and codebase

**B1 — The machine (hardware + launch).**
(1) The physical host. (2) Local, offline-by-default desktop; only research connectors and the mobile
Full-Mode tunnel touch the network. (3) Launched by `run_app.pyw` → pywebview at localhost:8080.
(4)/(5) n/a. (6) n/a. (7) All components run here. (8) Master §4 (L283–290). (9) BUILT AND DOCUMENTED AS
VERIFIED (host inspected S14). (10) RTX 2060 6GB runs 3B models ~35–50 tok/s, 7–8B slow (~7–9 tok/s),
limited context; settled upgrade direction RTX 3090 24GB (purchase-time verification required — a
hardware decision, carried for the audit not as chronology).

**B2 — Codebase map / three physical store sets.**
(1) Inventory of code modules and on-disk stores. (2) Tells each layer which files/stores it owns.
(3) Protected core modules (old gate stack) still run harmlessly; Layer-3 accretive files are the active
build target. (4)/(5) n/a. (6) Lists the sealed roots, seal marker, quarantine, gold files, Chroma
collections, models, source JSONs. (7) cursorrules protection. (8) Master §5 (L294–325). (9) BUILT AND
DOCUMENTED AS VERIFIED (store inventory S14/S16). (10) "Verify on disk; the doc's remembered state has
been wrong repeatedly."

## C. Built storage substrate

**C1 — The accretive store (append-only roots-of-record).**
(1) The DUMB-machinery heart. (2) Append-only store of raw root records; schema-validated before every
append; roots file sealed. (3) `append_root()` refuses while `.nh_roots.sealed` exists; no direct file
writes permitted. (4) Eligible captured material (currently only the seed ingest). (5) Root records in
`.nh_accretive_store.jsonl`. (6) Stores/seals 5,521 clean roots; reads via `read_all`/`read_by_subject`.
(7) `nh_accretive_store.py` is the sole write boundary. (8) Master §6B (L470–495), §5 (L300–301); DD §3C
(L77–84). (9) BUILT AND DOCUMENTED AS VERIFIED (S12–S16). (10) Production readings path gated (see C4);
seed-only; multi-box architecture undesigned (must precede any second batch).

**C2 — 7-field root schema (v1, sealed).**
(1) The immutable shape of a root. (2) Fixed fields so roots are stable and never reinterpreted.
(3) All seven required on every root; immutable once written; only change is audited destruction (§7Q).
(4) Source-carried fields. (5) `id·subject·timestamp·content·re_reads·source_title·role`. (6) `subject`
is a provenance batch tag in v1 (values `seed:conversations_000/001/002`), **not** semantic; `source_title`
may be `None`; `role` required on new writes. (7) Accretive store; ingest pipeline. (8) Master §6A
schema constraints (L389–391), §6B (L474–476); DD §3B (L70–75). (9) BUILT AND DOCUMENTED AS VERIFIED.
(10) Do not reinterpret `subject`; schema change needs a new `schema_version` and Ness's adoption; a
future rename (`source_batch`) is an open item.

**C3 — 12-field reading record (validator + writer).**
(1) The interpretive layer that points at roots. (2) Hold a reading beside a root without copying its
text. (3) `_validate_reading()` gates SHAPE only (rejects malformed, never uncertain); writer verifies
each `reads` root id exists in the sealed store, checks idempotency, routes to quarantine/production.
(4) Target root id(s) + engine output. (5) Reading records (currently to quarantine). (6) Fields:
`id·reads·meaning·confidence·role·story_layer·mode·timestamp·produced_by·schema_version·derived_from·idempotency_key`;
`confidence` is a TWO-SLOT object `{interpretation_confidence, source_reliability}`, never blended;
`story_layer` a list; `mode` an open word + local confidence; `produced_by.origin` from a controlled
vocabulary. (7) Accretive store, mouth/engines. (8) Master §6B (L478–494), §6A (L393–395); DD §3A
(L56–68). (9) BUILT AND DOCUMENTED AS VERIFIED (S14). (10) `source_reliability` not-yet-knowable value
form is **unverified from live code** — must be confirmed from the live validator before v3.2 fully
adopted; no `reason`/`why` field by design.

**C4 — Roots seal + production-readings authorization (dual gate).**
(1) Two protections guarding new writes. (2) Prevent accidental root appends and premature production
readings. (3) `.nh_roots.sealed` blocks `append_root`; production readings require both a Ness-created
`.nh_readings_production_authorized` marker AND an approved dry-run. (4) Ness's deliberate filesystem
acts. (5) Seal marker; (absent) production store. (6) Seals roots; restricts production writes; quarantine
holds test readings. (7) Accretive store; Cursor behavioral rule. (8) Master §6A (L385, L399–407), §5
(L301–303); DD §3C (L82). (9) PARTIALLY BUILT — seal + quarantine BUILT AND DOCUMENTED AS VERIFIED; the
marker-check inside `append_reading()` is DECIDED but NOT YET IMPLEMENTED (enforced today only as a
Cursor behavioral rule). (10) Whether `append_reading()` currently contains any production-path check is
unverified from live code.

**C5 — Quarantine readings store.**
(1) Test sink for engine output. (2) Keep all engine readings out of production. (3) Both engines write
here, never production. (4) Engine A/B output. (5) `.nh_readings_quarantine.jsonl`. (6) Holds gold-run
output (test-only). (7) Reading writer. (8) Master §5 (L303), §6B (L492). (9) BUILT AND DOCUMENTED AS
VERIFIED (S14). (10) Production store absent by design.

**C6 — Gold sets v1 and v2-B (sealed outside exam).**
(1) Sealed answer keys for grading engine readings. (2) An outside exam only Ness grades; engine output
may fail but may never alter a case. (3) Engine runs against the cases; Ness scores by semantic match by
hand. (4) Root cases. (5) `NH_GOLD_SET_v1.md` (8 clean-bare cases) + `NH_GOLD_SET_v2_B.md` (7
context-requiring cases) + seal markers. (6) Sealed; never modified. (7) Engines A/B. (8) Master §6
(L333–334), §6B (L304–307); DD §3D (L85–92), gold-scoring six rules (L90). (9) BUILT AND DOCUMENTED AS
VERIFIED (S14/S16). (10) `story_layer` not graded in v1/v2-B; a correction is a new versioned gold; a
context gold set v1 was drafted/approved but not yet placed or sealed.

## D. Built engines and tooling

**D1 — Engine A (`nh_engine_minimal.py`).**
(1) Bare reader. (2) Read one root with no context and lay a 12-field reading beside it. (3)
`read_root(root_id)` → mouth ("say what the {role} is doing; don't describe/answer/invent") → reading →
quarantine; `run_on_gold()` runs the 8 v1 cases. (4) A root id. (5) A quarantine reading. (6) Reads a
root; writes a reading. (7) Accretive store, mouth model. (8) Master §6 (L335), §5 (L317), §7C (L570).
(9) BUILT AND DOCUMENTED AS VERIFIED (S14); scored ~5–6/8 on gold v1. (10) `MOUTH_MODEL` is a test
candidate only; benchmark-protected.

**D2 — Engine B (`nh_engine_b.py`).**
(1) Context reader. (2) Read a root in the context of the preceding turns in the same thread. (3)
`read_root_b` → `_get_preceding_turns(n=3)` (position-based, same `source_title`, full content, no
truncation) → BACKGROUND/END BACKGROUND framing → mouth → reading → quarantine; `run_on_gold()` runs 7
v2-B cases. (4) A root id + preceding roots. (5) A quarantine reading. (6) Reads roots; writes a reading.
(7) Accretive store, mouth, `source_title` grouping. (8) Master §6 (L336), §5 (L318), §7C (L571); DD §3E
(L94–100). (9) BUILT AND DOCUMENTED AS VERIFIED (S16); scored 6.5/7 on the tested dolphin-8B setup.
(10) Cause of the remaining miss NOT isolated (model capability, prompt framing, context format, run
variance all possible); n=3 is the experiment's setting, not a universal future limit.

**D3 — Chroma `nh_roots_v1` + `nh_rebuild_chroma.py`.**
(1) Semantic index of clean roots. (2) Retrieve roots by meaning-distance. (3) Rebuild script has a
`--dry-run` (10-root test + retrieval check); full run = 5,521 roots in ~187.59s; never touches old
collections. (4) Clean roots. (5) `nh_roots_v1` collection (5,521, `all-MiniLM-L6-v2`). (6) Builds/reads
the index; old `nh_reality_core` (116,391) kept until proven. (7) Accretive store, embedding model.
(8) Master §6 (L337–338), §5 (L309, L319). (9) BUILT AND DOCUMENTED AS VERIFIED (S16). (10) Old
collections must not be modified/dropped.

**D4 — Ingest pipeline (`nh_ingest_chatgpt.py`).**
(1) Clean ChatGPT-export parser. (2) Turn JSON exports into clean roots. (3) Tree-walk ordering, clean
fields, junk-skip; ran on three JSON sources → 5,521 roots. (4) `conversations-000/001/002.json`.
(5) Roots. (6) Defines `SUBJECT_TAG` as the provenance batch tag. (7) Accretive store, seal.
(8) Master §5 (L311, L321), §6B (L476); DD §3C. (9) BUILT AND DOCUMENTED AS VERIFIED (S12). (10) Existing
dry-run/test-path mechanism not confirmed; `gpt_purified` and `cleaned_history` deliberately not ingested.

**D5 — Speaker-detector recipe (`nh_embed_confirm_speaker.py` reference).**
(1) Fallback for role-less sources. (2) Propose a speaker when source lacks `role`. (3) Investigated
ten methods; embed+shape (LogReg C=0.1, 5-fold) reached ~94.89%; recipe locked, NOT deployed (read-only
probes). (4) Root content. (5) A proposal (not deployed). (6) Reads content; proposes a candidate.
(7) Embedding model. (8) Master §6 (L340), §6A (L422), §7C (L567). (9) PARTIALLY BUILT — investigated and
recipe-locked (S13), not deployed. (10) A proposal stays a proposal until confirmed by Ness or source
evidence; never silently written to `role`.

## E. Code governance — Cursor Rules v3.2 (operational authority)

**E1 — Three-layer architecture + permanent prohibitions.**
(1) The operative ruleset Cursor obeys. (2) Keep three coexisting code layers separate and protect both
the legacy gate and the accretive store. (3) Layer 1 legacy read-only; Layer 2 still-running gate; Layer
3 active build target; "Cursor proposes, Ness approves, Cursor implements"; never touch `.env`,
PIN hash, vault, tokens; never write test/mock data into production; never build a parallel gate.
(4) Proposed code changes. (5) Approvals/blocks. (6) Restricts writes by layer. (7) All build work.
(8) Cursor Rules v3.2 (SRC-076) IDENTITY+§1 (L51–181), §6 three-layer map (L413–462); Master §6A
(L357–376); DD §3M (L195–202). (9) BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT — v3.2 is the
in-force adopted text; whether the disk `.cursorrules` carries v3.2 is not freshly verified (Master notes
the disk file was not overwritten in prior sessions; the disk file governs in any conflict). (10) Stale
"188 seed records" docstring in `_validate_record` pending cleanup.

**E2 — Protected files/stores + dry-run protocol + five protection decisions.**
(1) Change-control gate for sensitive files. (2) No edit to a protected file without "CONFIRMED: modify
[file]" + a full PROPOSED CHANGE dry-run and "APPROVED." (3) Lists Layer-2 and Layer-3 protected files;
five settled decisions (engine benchmark protection; ingest protection; rebuild no-touch-old-collections;
production-readings dual-authorization; `nh_baseline_engine.py` creation gate). (4) Proposed change.
(5) PROPOSED CHANGE block + approval. (6) Restricts edits; protects stores/markers/gold. (7) All Layer-3
work. (8) Cursor Rules §7–§8 (L463–573); Master §6A (L410–457); DD §3M (L201). (9) BUILT, BUT NOT FRESHLY
DISK-VERIFIED IN THIS AUDIT (rules in force). (10) `nh_baseline_engine.py` creation gate carries six §22
prerequisites.

**E3 — Pull Sovereignty + "before adding any feature that touches memory."**
(1) Behavioral guardrails. (2) No unsolicited autonomous tasks; watch for unexpected agent file
spawns; check before extending memory. (3) Stop-and-look if a tool call queues more files than asked.
(4) Agent activity. (5) Stops. (6) Restricts autonomous action. (7) Cursor. (8) Cursor Rules §10–§11
(L597–633). (9) BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT. (10) —

## F. Legacy gate (still running)

**F1 — REALITY/SIMULATION gate stack (Layer 2).**
(1) The old sovereignty mechanism. (2) Gate unverified content into REALITY only through one authorized
path. (3) `promote_to_memory()` in `nh_context_router.py` is the one gate; `ContextRouter.write()` is
NOT a gate (the exact June-19 bypass); `NH_PROMOTE_TOKEN` active; status labels INFERRED/GENERATED/
VERIFIED/REPORTED_SPEECH apply here. (4) Chat/HUD/research content. (5) REALITY/SIMULATION store records.
(6) Reads/writes Layer-2 stores. (7) Governs running chat, HUD, research pipeline. (8) Master §5 (L297),
§6A (L371–373, L381); Cursor Rules §2A (L183–221); DD §3M (L199). (9) BUILT, BUT NOT FRESHLY
DISK-VERIFIED IN THIS AUDIT — runs, but the Master documents Layer-2 store write-activity "as of June 19
2026, current disk behavior not re-verified." (10) Still-active legacy (not inactive); to be reconciled
only when the new filter is complete and Ness declares the new model active; do not rip out early.

## G. Universal Filter + Meaning Engine (design)

**G1 — Universal Filter (R0–R12) + the Keystone.**
(1) The operating rules of the one continuous reader. (2) One filter, not two stages: finding a
meaning-boundary and naming its type are one act; meaning comes from wide context; classification never
locks; memory only adds. (3) Words flow in → the reader tracks meaning → when the type shifts it closes a
statement, tags it, opens the next; a later context re-colors an old statement by adding a layer, never
editing. (4) Input pieces. (5) Readings/layers. (6) Reads; never closes "real." (7) Meaning engine,
accretive store. (8) Master §7A (L500–516); DD §2/§6. (9) FULLY DESIGNED — NOT BUILT (engines A+B are the
built first slices). (10) Ness steers/affirms off-board; the membrane is the boundary.

**G2 — The Meaning Engine seven webs + parts.**
(1) The reading mechanism. (2) A piece's meaning is how dimensions relate across webs, not one flat tag.
(3) The piece runs through INTENT, DEIXIS, COMMON-GROUND, IMPLICATURE, THEORY-OF-MIND, TIME/SEQUENCE,
RE-READING together in one pass; the parts include the Pure Tape (Part 0), nightly research (Part 4,
feeds memory not the mouth), inform-don't-ask (Part 6), wonder/simulation (Part 6.5), the LOG (Part 7),
the NOTE/why (Part 7.5). (4) A piece + accumulated context. (5) A reading; a LOG surface; a NOTE.
(6) Reads; the NOTE is write-only toward memory and never closes into fact. (7) Mouth, store, webs.
(8) Master §7B (L517–565). (9) FULLY DESIGNED — NOT BUILT (web list deliberately open). (10) Wonder/
simulation mechanism is concept-only; "register/mode" placement was an early open thread.

**G3 — The Forced Build Order + engine layers A→B→C.**
(1) The never-re-fought build sequence. (2) 2a (reading record) → 2b (detector) → 2c (engine A→B→C);
build the live path before nightly deepening. (3) A ✅ built, B ✅ built, C (story-layer) next, needs
story-bearing gold cases. (4)/(5) n/a. (6) Orders the build. (7) Store, engines, gold. (8) Master §7C
(L566–573); DD §3E/§4. (9) PARTIALLY BUILT (A,B built; C not). (10) Engine C blocked on story-bearing
gold cases.

## H. Catalog Front Door + Temporary Session Cache

**H1 — Catalog Front Door (two gates / minimum intake envelope / four enrichment categories).**
(1) The capture-and-normalize entry stage. (2) Separate raw capture from root ingestion; a root cannot
be sealed until required catalog fields resolve; raw material never destroyed for an unresolved field.
(3) Each front door produces a minimum intake envelope (capture_id, raw payload/ref, timestamp,
source-type, format, source metadata, provenance); a unified pre-ingest holding area carries items with
a blocker list through `held→ready→promoting→promoted` (+ rejected/excluded/error); promotion to the
sealed store is atomic and idempotent. (4) Raw captures. (5) Pre-ingest records; eventually roots.
(6) Holds raw material invisibly to the engine; records proposals; preserves raw payload unchanged.
(7) §7Q precedence; speaker/thread rules; accretive store. (8) Master §7E (L616–648). (9) FULLY DESIGNED
— NOT BUILT. (10) Four enrichment categories (source facts / mechanical derivations / machine
proposals / forbidden semantic interpretation); exact schemas/field names undesigned; `role` and
`source_title` resolution rules; never silent drop.

**H2 — Temporary Session Cache (TSC) — §7E integration summary.**
(1) Organized holding mode within §7E for sessions involving people other than Ness. (2) Hold an entire
third-party session under a fingerprint-authorization blocker until Ness authorizes promotion. (3) Every
item enters §7E carrying `"pending_fingerprint_authorization"`; a transactional structural DB organizes
order/attribution/branches/BOP+SIA links/N.H outputs/lifecycle; on close the cache seals immutably and
waits indefinitely; the blocker lifts only via a purpose-bound BAI token `"tsc_promotion:<session_id>"`
consumed with a confirmed recognized-Ness SACL session; then items promote through the normal §7E
lifecycle preserving order. (4) Session contributions, BOP roots, N.H outputs, metadata. (5) Pre-ingest
records + structural DB + a retained encrypted read-only safety archive. (6) Holds/seals session
material; records §7Q decisions; never writes `role="unknown"`; never interprets. (7) §7E, §7Q, BAI,
SACL, BOP, SIA, `append_root()`. (8) Master §7E-TSC (L650–675); DD §3N (L204–218). (9) FULLY DESIGNED —
NOT BUILT as the §7E integration summary; the full design is the accepted companion SRC-002 (see §4).
(10) Inspection uses a separate `"tsc_inspection:<session_id>"` token; the full 31-section spec is the
authoritative specification and is external.

## I. Context Retrieval (§7F)

**I1 — Two-channel context retrieval (positional vs semantic).**
(1) Supplies context to a reading pass. (2) Keep "what came immediately before in this thread"
(positional) strictly separate from "what else may relate" (semantic). (3) Each retrieved item carries
retrieval provenance; both channels shown in separate prompt sections; a conflict is surfaced, not
silently resolved; per-mode parameters; genuine no-context is a normal condition, distinct from system
failure. (4) A target root + reading mode. (5) Retrieved context + audit trail. (6) Reads roots/index;
exposes retrieval provenance. (7) Engine, Chroma, `source_title`. (8) Master §7F (L678–701); DD §3G
(L119). (9) FULLY DESIGNED — NOT BUILT. (10) Trigger conditions, exact limits, ranking, thresholds, and
safety-ceiling values undesigned; each mode must declare its §7R relevance config later.

## J. Meaning Engine Interior + Acceptance Check (§7G)

**J1 — One-reading-per-pass + Reading Proposal Acceptance Check.**
(1) The interior reading flow and its gate. (2) One pass = one reading record for one target root; the
mouth does not judge its own output. (3) Flow: target root + optional context + declared mode → mouth
proposal → acceptance check → reading record; acceptance verifies grounding, no invention, channels not
confused, honest uncertainty, mode followed; failures recorded as distinct reasons. (4) Root + context +
mode. (5) A reading or a recorded rejection reason. (6) Reads roots/context; writes readings/audit.
(7) Mouth, context retrieval, store. (8) Master §7G (L704–743); DD §3G (L120). (9) FULLY DESIGNED — NOT
BUILT. (10) FIRST-CLASS: model confidence is metadata, not authority; story-layer evidence kept in two
labeled channels; circular support forbidden; exact criteria/thresholds/retry undesigned.

## K. Reread Lifecycle (§7H)

**K1 — Reread triggers (manual / condition-based / scheduled retry).**
(1) Controls when an old reading is re-read. (2) A reread never happens without an explicit recorded
reason. (3) Three trigger types only; time passing alone is never a condition; a reread creates a NEW
reading, never overwrites; rejection is recorded and may make a reading eligible. (4) A trigger event.
(5) A new reading + reread record. (6) Reads prior readings; writes new ones. (7) Meaning engine, §7R.
(8) Master §7H (L747–763); DD §3G (L121). (9) FULLY DESIGNED — NOT BUILT. (10) Exact relevance rules,
retry limits, scheduling undesigned.

## L. View Layer + Computed View (§7I, §7M)

**L1 — View Layer (current + history).**
(1) Per-root presentation of readings. (2) Simple by default, complete on demand; ordering is
presentation only, never authority. (3) Current view surfaces the newest usable reading and surfaces
conflicts explicitly; history view shows strict chronology; nothing deleted/hidden/overwritten.
(4) Readings. (5) A view. (6) Reads readings; exposes them with labels. (7) Computed View seven-factor
ordering when claiming "current best." (8) Master §7I (L767–777). (9) FULLY DESIGNED — NOT BUILT.
(10) Exact grouping/labels/layout undesigned.

**L2 — Computed View (seven-factor ordering, immutable snapshots).**
(1) The present-facing surface. (2) Assemble the most useful current picture without altering objects or
declaring a winner. (3) Seven explicit factors (Ness's judgment → root-evidence strength → grounding →
relevance → context quality → clashes-surfaced → recency tie-break) with no hidden score; triggered
updates only; each update writes a new immutable snapshot. (4) Roots, readings, tellings, clashes,
response events, person-box links, themes, metadata-only pre-ingest refs. (5) A snapshot. (6) Links
(never copies) objects; preserves prior snapshots; never rewrites/merges/deletes. (7) Most other
subsystems; §7R for factor 4. (8) Master §7M (L885–912); DD §3G (L126). (9) FULLY DESIGNED — NOT BUILT.
(10) Must be able to say "no clear current view"; exact relevance rules/thresholds/snapshot schema
undesigned.

## M. Clash Handling (§7J)

**M1 — Contradiction/clash records (six types, two detection modes).**
(1) Records conflicts without resolving them. (2) Distinguish genuine contradiction from contextual
difference; never resolve. (3) Six clash types; triggered + periodic detection produce the same record
type; the same clash never spawns duplicates (later detection appends an event); Ness's response is a
separate linked event; downstream actions are separate linked records. (4) Readings of the same/related
roots. (5) Clash records + response events. (6) Points to exact readings/roots; never mutates them.
(7) Meaning engine, view/computed view, person-boxes. (8) Master §7J (L781–811); DD §3G (L123).
(9) FULLY DESIGNED — NOT BUILT. (10) A clash is not automatically an error; exact schemas/detection/
dedup undesigned.

## N. Story Layer (§7K)

**N1 — Story Layer (tellings, structured perspective, firmness, hybrid themes).**
(1) Holds per-person tellings across time. (2) Record tellings unaltered; keep each person's story
separate; preserve clash; never merge into one narrative. (3) Tellings connect by explicit shared
attributes (navigational links, not merges); structured perspective model (`root_speaker`, `subject`,
`perspective_owner`, optional `attribution_path`); firmness inferred from observable signals and kept
separate from model confidence; themes are engine-proposed, Ness-confirmed navigation categories.
(4) Engine-pass tellings + roots/prior readings (two labeled channels). (5) Tellings, proposed themes.
(6) Reads roots/readings; records tellings/themes; never closes. (7) Meaning engine, person-boxes,
clash. (8) Master §7K (L815–850); DD §3G (L124). (9) FULLY DESIGNED — NOT BUILT. (10) **Object-identity
seam UNRESOLVED** — tellings are embedded in `story_layer`; no standalone telling record/ID exists;
must be designed before story/person-box/clash/deletion code relies on telling-level links; firmness
scale and theme schema undesigned.

## O. Person-Boxes (§7L)

**O1 — Person-Boxes (gather, proposal-based anchors, merges).**
(1) Stable identity anchor per person. (2) Gather everything linked to a person without synthesizing a
profile. (3) Links roots/readings/tellings/themes/clashes/responses/other boxes (links never copies);
uncertain identity is normal; proposed anchors never silently become confirmed boxes; merges require
explicit resolution and never rewrite history. (4) References to a person across the store. (5) Anchors,
merge proposals, links. (6) Reads/links; never profiles, diagnoses, or closes. (7) Story layer, clash,
computed view. (8) Master §7L (L853–875); DD §3G (L125). (9) FULLY DESIGNED — NOT BUILT. (10) SETTLED
FACT: Ness has a Person-Box (June 25) — its creation/anchoring/maintenance not yet designed; matching/
merge mechanics undesigned.

## P. Living State Web (§7D)

**P1 — Living State Web (state/transition modeling).**
(1) Future layer to model a person moving through states over time. (2) Beyond meaning/memory: model
state, transitions, open loops, relationships, causal hypotheses, counterfactuals, values/constraints.
(3) S17 designed node/edge types, a grounding rule (every node carries source + root ids; circular
support forbidden), and a currency rule (existence vs currentness are independent; six currency
statuses; time alone never marks a state ended). (4) Readings, tellings, clashes, response events,
roots. (5) State nodes, transition/relationship/causal edges, open-loop nodes. (6) Reads derived
objects; never chooses the path or promotes to truth. (7) Computed View, Story Layer, Person-Boxes,
§7P, §7Q, §7R. (8) Master §7D (L576–612); DD §3G (L131). (9) PARTIALLY DESIGNED. (10) Many domains and
all implementation details undesigned (schema, evidence thresholds, aging windows, transition
conditions, world model, purpose-aware lenses, build-order position, currency-review-trigger
authorization).

## Q. Action lifecycle (§7N, §7O)

**Q1 — Action Surfacing (permission-controlled hybrid).**
(1) Surfaces possible actions. (2) Show possibilities (never instructions/decisions); Ness is sole
decider. (3) Two modes (on request always; proactive only under an authorized relevance rule); every
possibility labeled "one possible option," records what it derived from + uncertainty; six Ness-response
states; rejection is never treated as failure; no repeat surfacing without a new trigger. (4) State/
open-loop/value/constraint/evidence. (5) Surfaced possibilities + response events. (6) Reads derived
material; records possibilities/responses. (7) Living State Web, §7P, §7R. (8) Master §7N (L916–941);
DD §3G (L127). (9) FULLY DESIGNED — NOT BUILT. (10) Action-category→risk-level mapping, evidence/
permission thresholds, interface wording undesigned.

**Q2 — Action-Result Return Path (two result types, six result states).**
(1) Handles what happened after an action. (2) Never let the system declare an action's result on its
own. (3) Explicit reported result (Ness reports, enters as a normal root) vs detected possible result (a
proposal linking material to an action, never a silent declaration); causation never inferred from
timing/similarity; three separate linked objects (action, result root, connection); six result states.
(4) Reported/observed material + action records. (5) Result roots, connection proposals. (6) Records
results/connections; never merges. (7) §7N, §7P, reread, Living State Web. (8) Master §7O (L945–974);
DD §3G (L128). (9) FULLY DESIGNED — NOT BUILT. (10) Detection rules, confirmation workflow, subcategories
undesigned.

## R. Permission and Authority Boundaries (§7P)

**R1 — Permission/Authority Boundaries (three action states, four risk levels, two authority layers).**
(1) The boundary between helper and actor. (2) Define what N.H may do alone, must preview, must ask, or
may never do. (3) Suggesting/Preparing/Executing; four risk levels (internal read-only → internal write
→ prepared external → executed external); standing vs moment-level authority; silence is never approval;
absolute boundary requires per-instance confirmation for medical/legal/financial/privacy/relationship/
destructive/irreversible actions; on violation, stop-and-surface is default; five separate linked
objects; a narrow emergency-stop exception cannot reverse a completed world. (4) Action requests.
(5) Authorization objects, violation records, corrective proposals. (6) Restricts/records actions; never
self-extends a permission. (7) Action surfacing/result, all external action. (8) Master §7P (L978–1031);
DD §3G (L129). (9) FULLY DESIGNED — NOT BUILT. (10) Exact permission categories, authorization-object
schema, and interface undesigned.

## S. Privacy, Deletion, Sensitive-Data (§7Q)

**S1 — Privacy/deletion/sensitive-data handling (five operations, four levels, two-stage access).**
(1) Governs capture, classification, access, display, and deletion of sensitive material. (2) Protect
secrets and third-party data; keep Ness's own access open while restricting external exposure.
(3) Five distinct operations (exclusion/hiding/restriction/redaction/deletion); four sensitivity levels;
deletion is blocking and verification-based with five outcomes (`verified_complete` the only "complete")
and a content-free tombstone; two-layer capture exclusion (non-negotiable core vs Ness-configured);
third-party baseline; two-stage output access control (pre-retrieval eligibility + pre-output review);
model-provider refusals recorded as mouth limitations. (4) Captures, retrieval requests, deletion
requests. (5) Eligibility decisions, tombstones, exclusion metadata, privacy-decision records.
(6) Excludes/redacts/restricts/deletes; exposes only authorized material. (7) Catalog, computed view,
story, person-boxes, Living State Web, §7R prerequisite. (8) Master §7Q (L1034–1121); DD §3G (L130).
(9) PARTIALLY DESIGNED. (10) CENTRAL RULE: private access for Ness open by default. Many mechanics
undesigned (exact eligibility rules, exclusion detection, cryptographic erasure, derivative discovery,
backup deletion, minor-data rules, verification procedures).

## T. Attention and Relevance Control (§7R)

**T1 — Attention and Relevance Control (two-layer judgment, fourteen decisions).**
(1) Decides what is worth showing/retrieving/acting on, by explicit auditable rule. (2) Provide a shared
relevance definition every surfacing component uses. (3) Output = a context boolean gate + graded named
dimensions each with provenance (no hidden score); three producer types per dimension (deterministic
rules, embedding model, mouth-for-declared-interpretive-only); on-demand by default (no global relevance
state); two-tier mode contract; Ness inspects/overrides per-judgment and changes modes via consequence
preview; mouth-dimension validation; disagreement and relevance-event records; pattern-observation rule;
halt on unrecognized purpose type. (4) Candidates + a declared mode config. (5) Relevance judgments,
relevance-event records, disagreement records. (6) Reads eligible candidates; records judgments; never
determines truth/authority/causation, never writes the Living State Web. (7) §7Q prerequisite; consumed
by Context Retrieval, Computed View, Action Surfacing, Reread, Living State Web. (8) Master §7R
(L1125–1404); DD §3H (L133–142). (9) FULLY DESIGNED — NOT BUILT (core; fourteen decisions settled S18).
(10) RELEVANCE IS NOT TRUTH/EVIDENCE/AUTHORITY/PERMANENT; per-component mode declarations, Tier-2
handling, thresholds, storage formats remain open.

## U. Research / Knowledge Catcher pipeline (§8)

**U1 — Research pipeline (Brave → synthesis → gate; source preservation).**
(1) Brings outside info into the review queue and re-checks stored info against sources. (2) Gather raw
web data and check stored claims, landing findings in MEMORY as readings, never the mouth. (3) Brave
(raw JSON) → one auditable OpenRouter/llama synthesis (text-in/text-out only, no tools/file/network) →
create-space → gate; auto-reject never auto-delete; rejected-bin "look don't touch" display; source
preservation saves a plain-text excerpt + a frozen full-page screenshot (inert) with provenance/hash;
fallback marks SOURCE PRESERVATION INCOMPLETE. (4) Queries; web results. (5) Research readings + frozen
source captures + rejected-bin entries. (6) Writes readings to memory; preserves inert source evidence.
(7) Legacy gate, mouth/synthesis model, store. (8) Master §8 (L1406–1431); DD §5 (L264–265). (9) FULLY
DESIGNED — NOT BUILT (Brave not wired). (10) Brave has NO spending cap — a query counter/daily cap MUST
be coded; live full-page capture needs an isolated environment (undesigned); academic source open
(Semantic Scholar vs OpenAlex vs both); screenshot-as-inert-image proposal not yet decided; re-check
schedule only with Ness's explicit approval.

## V. Model layer (§16)

**V1 — The borrowed frozen mouth + embedding/search model + synthesis model.**
(1) The swappable language layer. (2) The model is a commodity mouth; everything that makes N.H its own
lives outside it; search first, word last; growth lands in memory not the mouth; uncensored by design.
(3) `dolphin-llama3` (8B) is the CURRENT TEST MODEL on disk (not the adopted final Interactive
Translator); `all-MiniLM-L6-v2` is the tiny search model; an OpenRouter synthesis model serves research.
(4) Meaning + context. (5) Sentences (mouth); meaning-distance (embeddings). (6) Reads; produces wording.
(7) Engines, retrieval, research. (8) Master §16 (L1542–1567), §4; DD §3F (L102–113). (9) Models on disk:
BUILT AND DOCUMENTED AS VERIFIED; local-first wiring: FULLY DESIGNED — NOT BUILT. (10) Final mouth
UNDECIDED; Dolphin 3.0 R1 Mistral 24B is the first post-upgrade candidate (untested); a new mouth must
pass BOTH sealed gold sets before replacing the current one; Hebrew quality weak-but-workable, gated on
bigger model/VRAM; model-provider limits are mouth limits.

## W. Live path: Live Loop + Chat Front Door (§13, §14)

**W1 — The Live Loop.**
(1) The fire-and-let-go concurrency design. (2) Deep work never blocks the chat; the deep side announces
itself back; parallel topics become mechanically possible. (3) The chat speaks fresh from a silent
memory pull; the loop carries N.H's own output toward memory only as an append-only proposal, never a
closing/REALITY write. (4) Live interaction. (5) Async readings/proposals. (6) Reads memory; guarded
write toward memory. (7) Store, membrane. (8) Master §13 (L1504–1517). (9) FULLY DESIGNED — NOT BUILT.
(10) THE GUARD: the fast loop must never become a closing/REALITY-write path.

**W2 — The Chat Front Door.**
(1) The live chat as a first-class input. (2) Treat Ness↔N.H chat as recorded input (speaker carried,
connect-not-claim, point-back shown, mechanism never narrated). (3) Two-filter path riding the live
loop; the point-back is the one clickable thing shown. (4) Live chat turns. (5) Roots/readings.
(6) Records the chat; surfaces point-backs. (7) Live loop, store, membrane. (8) Master §14 (L1519–1536);
DD §5 (L276). (9) PARTIALLY DESIGNED (in-progress, not confirmed, not built). (10) Two open questions:
creation-filter as a distinct mechanism vs a mode; always-capture vs deliberate-capture.

## X. Image ingest front door (§9A)

**X1 — Image ingest (first worked front-door example).**
(1) A worked example of a new front door. (2) Show how a non-text input becomes engine-readable pieces.
(3) Metadata → plain description → context meaning → Ness confirms. (4) An image. (5) Catalog pieces.
(6) Extracts/normalizes; defers semantics to the engine. (7) Catalog front door, engine. (8) Master §9A
(L1436–1437). (9) FULLY DESIGNED — NOT BUILT. (10) Precondition for WhatsApp media ingest (deferred).

## Y. Interface, World, and Interaction (§19)

**Y1 — Interface/world/interaction system.**
(1) The future interactive environment ("Ness's World"). (2) A navigable space for architecture and
solving. (3) Settled: world manipulation is presentation/navigation/explicitly-labeled-simulation only
by default (does not mutate records). (4) Ness's interaction. (5) Views/world state. (6) Presents;
does not mutate underlying records. (7) §7P (authority), §7Q (camera/VR front doors), simulation.
(8) Master §19 (L1613–1699). (9) PARTIALLY DESIGNED (in-progress, paused). (10) Simulation interior,
gesture vocabulary, VR, camera, accessibility, visual language largely undesigned; three open
cross-component dependencies (approval-explicitness vs unobtrusiveness; camera/VR as new front doors;
external actions from within the world).

## Z. Wellbeing and Behavioral Baseline System (§22)

**Z1 — Wellbeing/behavioral baseline (Ness vs Ness).**
(1) A self-monitoring layer protecting both data integrity and Ness's wellbeing. (2) Detect when Ness's
judgment is off-baseline (since REALITY rests on his judgment). (3) Builds the baseline passively from
demonstrated behavior (promotion/rejection patterns, conversation/decision patterns); a monthly surface
Ness can refine but not override; four tiers (silent flag → mirror signal → queue throttling → REALITY
freeze); unlock via a psychiatric/medical appointment record used as a calibration anchor. (4) Decision
history, simulation rejections, conversation/session metadata. (5) Tier actions; CALIBRATION_ANCHOR
records. (6) Reads patterns; throttles/freezes REALITY promotion. (7) Legacy gate; `nh_baseline_engine.py`
(uncreated). (8) Master §22 (L1759–1817); DD §3K (L178–185). (9) FULLY DESIGNED — NOT BUILT. (10) Build-
order gate (AFTER the search pipeline is stable and the queue has been healthy ≥1 month); six creation
prerequisites; the one honest limitation — it validates internal consistency, not health; appointment
anchors not optional; advisory only.

## AA. Mobile App — Three-Mode Companion (§23)

**AA1 — Mobile three-mode companion.**
(1) A phone companion in three modes. (2) Nothing connects to the real N.H automatically, ever.
(3) Mode 1 Full (deliberate fingerprint/Face-ID/PIN tunnel that Ness opens and closes; not passive);
Modes 2/3 an independent local AI (online learns; offline runs on what it knows) with its own memory;
Manual Sync sends local memory to the desktop through the same SIMULATION review gate, no shortcuts.
(4) Phone input; explicit Ness triggers. (5) Local memory; synced records (to SIMULATION). (6) Stores
local memory (encrypted at rest); bridges only on deliberate action. (7) `nh_auth.py`, legacy gate.
(8) Master §23 (L1821–1858); DD §3L (L187–193). (9) FULLY DESIGNED — NOT BUILT. (10) Security
requirements non-negotiable (auth-gated tunnel; no raw OS command execution; remove `nh_pc_agent.py`
`run:`; encryption at rest; SIMULATION-first); open: on-device model choice, local memory format, iOS/
Android background feasibility, Full-Mode tunnel wiring, Manual-Sync content scope.

## AB. Connection Capability (§24)

**AB1 — Connection capability (lasting connections + pending proposals).**
(1) Connects pieces that belong to the same situation without merging originals. (2) From Ness's side,
one ability; the split is internal. (3) Part one = a lasting connection record (type, decision status,
certainty kept separate from decision, confirmer, evidence, correction history); part two = Context
Retrieval (gathers, creates no lasting connection); a waiting area holds pending proposals (accepted/
rejected/undecided); connections may come only from three approved bases (direct recorded relationship;
Ness's confirmation; a narrow authorized rule); certainty controls use; a one-way rule. (4) Material +
proposed/confirmed relationships. (5) Lasting connection records; pending proposals. (6) Records
connections; never invents from similarity/timing/theme/co-retrieval. (7) Context Retrieval, §7G.
(8) Master §24 (L1862–1896); DD §3J (L174–176). (9) FULLY DESIGNED — NOT BUILT (conceptually designed
S19; not integrated through an audited build). (10) ACCEPTED ≠ CERTAIN; pending connections may guide
investigation silently but never support a claim/judgment/recommendation/action; five source types kept
separate.

## AC. Concept-only / not-designed areas (named in the authority)

**AC1 — Wonder/Simulation mechanism.** Concept in §7B (the create-space, wonders kept and shown);
mechanism not designed. Status: PARTIALLY DESIGNED (concept settled). (Master §7B; DD §5 L271.)
**AC2 — World model beside the self model.** Named in the Living State Web domain list; not designed.
Status: OPEN / UNRESOLVED. (Master §7D L608; DD §5 L272.)
**AC3 — End-to-end cycle.** The complete connected flow from new input through all components to Computed
View/chat is identified but not designed as one sequence. Status: OPEN / UNRESOLVED. (DD §4 L252, §5 L273.)

## AD. Intentionally absent / historical (named in the authority)

**AD1 — `cleaned_history (1).txt` ingest.** Deliberately not ingested (damaged). Status: INTENTIONALLY
ABSENT. (Master §5 L311.)
**AD2 — `gpt_purified` ingest.** Skipped (0 unique, redundant/scrambled). Status: INTENTIONALLY ABSENT.
(Master §5 L311.)
**AD3 — Hetzner sovereignty sync.** Explicitly superseded by Ness (June 25); no longer an active task.
Status: HISTORICAL / INACTIVE. (Master §11 L1458, §25 L1906.)
**AD4 — `nh_peek.py`.** Throwaway viewer, not on disk (superseded by `nh_log.py`); harmless phantom.
Status: HISTORICAL / INACTIVE. (Master §6 context.)

---

# 2. PLAIN-LANGUAGE BEHAVIOR MAP (how the present features work together)

What actually runs today is a small, sealed foundation; almost everything else is design sitting above
it. The map below distinguishes the two.

**The built floor (today).** Three JSON exports were parsed by the ingest pipeline (D4) into **5,521
clean root records** in the append-only **accretive store** (C1), each carrying who-spoke from source
(C2). The roots file is **sealed** (C4), so nothing more is appended without Ness lifting the seal.
Beside the roots sits the built **reading record** (C3): a 12-field validator and writer that lets an
engine lay an interpretation next to a root by pointing at it (never copying), gating shape but never
certainty, holding confidence as two honest slots. Two **engines** read: **Engine A** (D1) reads a root
bare; **Engine B** (D2) reads it with the three preceding turns in the same thread. Both write only to a
**quarantine** file (C5); the production readings file does not exist yet, and a second protection (a
Ness-made marker) is still only a behavioral rule (C4). Both engines are graded against two **sealed
gold sets** (C6) that only Ness scores. A **Chroma index** (D3) lets roots be found by meaning. All of
this is governed by **Cursor Rules v3.2** (E1–E3), which protects these files and keeps three code
layers separate — including the still-running **legacy REALITY/SIMULATION gate** (F1), which the new
architecture has not yet replaced.

**The designed system above it.** The intended live path is: an input arrives at a **Catalog Front
Door** (H1) that captures and normalizes it but interprets nothing, holding it in a pre-ingest area
until required fields resolve; sessions with other people are held in the **TSC** (H2) until a fingerprint
authorizes promotion. Eligible material becomes a sealed root; then the **Meaning Engine Interior** (J1)
reads it — pulling **two separate channels of context** (I1), proposing a reading through the mouth (V1),
and passing it through an **Acceptance Check** that treats model confidence as metadata, not authority.
Readings accrete; the **Story Layer** (N1) holds per-person tellings without merging them; **Person-Boxes**
(O1) gather everything about a person without profiling; **Clash Handling** (M1) records contradictions
without resolving them; the **Reread Lifecycle** (K1) re-reads only on an explicit recorded trigger.
The **Computed View** (L2) and **View Layer** (L1) assemble what N.H currently has reason to show, using
an explicit seven-factor order with no hidden truth score, and **Attention and Relevance Control** (T1)
supplies the shared definition of "relevant" each of these uses. The **Living State Web** (P1) would model
Ness moving through states over time. Around all of this, **Permission and Authority Boundaries** (R1)
and **Privacy/Deletion** (S1) gate every action and every disclosure, the **Research pipeline** (U1)
brings outside evidence into memory (never the mouth), and the **Action lifecycle** (Q1–Q2) keeps every
suggestion and every result a separate, Ness-decided object. The **Live Loop** (W1) and **Chat Front
Door** (W2) are the intended live interface; the **Mobile** companion (AA1), **Wellbeing baseline** (Z1),
**Connection capability** (AB1), and **Interface/World** (Y1) sit further out. The whole thing rests on
the **premise** (A1) and the **two-machineries frame** (A2): the DUMB half moves and seals data, the
SMART half reads the person, and the membrane between them is the one place creation must never close
into fact.

**The accepted security spine (external).** Layered under the third-party path is an accepted but
un-built security/identity spine: **BOP** captures physical observations, **SIA** assesses who is
speaking, **SACL** decides what the current speaker may receive, **BAI** mints purpose-bound biometric
tokens, **BGMM** is the only path to change protected files, and a pairing/recovery/emergency/enrollment
set anchors device trust. The Master reaches into this spine only at the TSC seam (BAI tokens + a
recognized-Ness SACL session); the full designs live outside the Master (see §4).

---

# 3. BUILT vs DESIGNED vs ACCEPTED — STATUS TABLE

| Feature | §/source | Status (this audit) |
|---|---|---|
| Accretive store (C1) | Master §6B / DD §3C | BUILT AND DOCUMENTED AS VERIFIED |
| 7-field root schema (C2) | Master §6A/§6B | BUILT AND DOCUMENTED AS VERIFIED |
| 12-field reading record + validator/writer (C3) | Master §6B | BUILT AND DOCUMENTED AS VERIFIED |
| Roots seal (C4) | Master §6A/§5 | BUILT AND DOCUMENTED AS VERIFIED |
| Production-readings authorization (C4) | Master §6A | PARTIALLY BUILT (marker-check decided, not implemented) |
| Quarantine readings store (C5) | Master §6B | BUILT AND DOCUMENTED AS VERIFIED |
| Gold sets v1 + v2-B (C6) | Master §6 | BUILT AND DOCUMENTED AS VERIFIED |
| Engine A (D1) | Master §6 | BUILT AND DOCUMENTED AS VERIFIED |
| Engine B (D2) | Master §6 | BUILT AND DOCUMENTED AS VERIFIED |
| Chroma `nh_roots_v1` + rebuild (D3) | Master §6 | BUILT AND DOCUMENTED AS VERIFIED |
| Ingest pipeline (D4) | Master §5 | BUILT AND DOCUMENTED AS VERIFIED |
| Speaker-detector recipe (D5) | Master §6/§7C | PARTIALLY BUILT (recipe locked, not deployed) |
| Cursor Rules v3.2 governance (E1–E3) | SRC-076 / Master §6A | BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT |
| Legacy REALITY/SIMULATION gate (F1) | Master §5/§6A | BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT |
| Universal Filter + Meaning Engine webs (G1–G2) | Master §7A/§7B | FULLY DESIGNED — NOT BUILT |
| Forced build order A→B→C (G3) | Master §7C | PARTIALLY BUILT (A,B built; C not) |
| Catalog Front Door (H1) | Master §7E | FULLY DESIGNED — NOT BUILT |
| TSC §7E integration summary (H2) | Master §7E-TSC | FULLY DESIGNED — NOT BUILT (full design = SRC-002) |
| Context Retrieval (I1) | Master §7F | FULLY DESIGNED — NOT BUILT |
| Meaning Engine Interior + Acceptance Check (J1) | Master §7G | FULLY DESIGNED — NOT BUILT |
| Reread Lifecycle (K1) | Master §7H | FULLY DESIGNED — NOT BUILT |
| View Layer (L1) | Master §7I | FULLY DESIGNED — NOT BUILT |
| Computed View (L2) | Master §7M | FULLY DESIGNED — NOT BUILT |
| Clash Handling (M1) | Master §7J | FULLY DESIGNED — NOT BUILT |
| Story Layer (N1) | Master §7K | FULLY DESIGNED — NOT BUILT |
| Person-Boxes (O1) | Master §7L | FULLY DESIGNED — NOT BUILT |
| Living State Web (P1) | Master §7D | PARTIALLY DESIGNED |
| Action Surfacing (Q1) | Master §7N | FULLY DESIGNED — NOT BUILT |
| Action-Result Return Path (Q2) | Master §7O | FULLY DESIGNED — NOT BUILT |
| Permission/Authority Boundaries (R1) | Master §7P | FULLY DESIGNED — NOT BUILT |
| Privacy/Deletion/Sensitive-data (S1) | Master §7Q | PARTIALLY DESIGNED |
| Attention and Relevance Control (T1) | Master §7R | FULLY DESIGNED — NOT BUILT |
| Research / Knowledge Catcher pipeline (U1) | Master §8 | FULLY DESIGNED — NOT BUILT |
| Model layer — models on disk (V1) | Master §16 | BUILT AND DOCUMENTED AS VERIFIED |
| Model layer — local-first wiring (V1) | Master §16 | FULLY DESIGNED — NOT BUILT |
| Live Loop (W1) | Master §13 | FULLY DESIGNED — NOT BUILT |
| Chat Front Door (W2) | Master §14 | PARTIALLY DESIGNED |
| Image ingest front door (X1) | Master §9A | FULLY DESIGNED — NOT BUILT |
| Interface/World/Interaction (Y1) | Master §19 | PARTIALLY DESIGNED |
| Wellbeing baseline (Z1) | Master §22 | FULLY DESIGNED — NOT BUILT |
| Mobile three-mode (AA1) | Master §23 | FULLY DESIGNED — NOT BUILT |
| Connection capability (AB1) | Master §24 | FULLY DESIGNED — NOT BUILT |
| Wonder/Simulation mechanism (AC1) | Master §7B | PARTIALLY DESIGNED |
| World model (AC2) | Master §7D | OPEN / UNRESOLVED |
| End-to-end cycle (AC3) | Master §4/DD §4 | OPEN / UNRESOLVED |
| cleaned_history / gpt_purified ingest (AD1–AD2) | Master §5 | INTENTIONALLY ABSENT |
| Hetzner sync / nh_peek (AD3–AD4) | Master §11/§25 | HISTORICAL / INACTIVE |
| Accepted security/identity designs (§4) | SRC-001 | ACCEPTED — NOT YET INTEGRATED |
| Accepted TSC full design (§4) | SRC-002 | ACCEPTED — PARTLY INTEGRATED |

---

# 4. ACCEPTED-COMPANION INTEGRATION MATRIX (SRC-001, SRC-002 vs the current Master only)

**Method.** Each accepted mechanism is compared against `NH_MASTER-19_CORRECTED_v7_1.md` only (not the
historical spine). "Integrated" means the Master carries the design itself; "referenced" means the Master
names or depends on it without containing it; "external" means the full design lives only in the companion.
Both companions carry their own status `ACCEPTED DESIGN — NOT YET BUILT` and state they "must be formally
patched into the Master… before they carry Master authority." Each remains authoritative within its own
scope even while un-integrated.

| Accepted mechanism | Companion source + line range | Present in Master v7_1? | Integration status |
|---|---|---|---|
| BOP — Behavioral Observation Processing | SRC-001 §1 (gov L378–588) | Referenced only (BOP roots named in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Other-Speaker / Guest / Known-Person architecture | SRC-001 §2 (gov L589–719) | Not present (access levels, guest mode, PBR) | ACCEPTED — NOT YET INTEGRATED |
| SIA — Speaker Identity Assessment | SRC-001 §3 (gov L720–964) | Referenced only (SIA links named in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| SACL — Speaker Access-Control Layer | SRC-001 §4 (gov L965–1159) | Referenced only (recognized-Ness SACL session in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Wellbeing/Identity/Security separation rules | SRC-001 §5 (gov L1160–1205) | Not present | ACCEPTED — NOT YET INTEGRATED |
| BAI — Biometric Authorization Interface | SRC-001 §6 (gov L1206–1390) | Referenced only (purpose-bound BAI tokens in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Initial Owner-Phone Pairing (four states) | SRC-001 §7 (gov L1391–1432) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Recovery-Code Lifecycle | SRC-001 §8 (gov L1433–1482) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Future-Phone Replacement Flow | SRC-001 §9 (gov L1483–1501) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Atomic Emergency Recovery Flow | SRC-001 §10 (gov L1502–1556) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Initial Ness Voice-Profile Enrollment Bootstrap | SRC-001 §11 (gov L1557–1702) | Not present (references §7G/§7L integration internally) | ACCEPTED — NOT YET INTEGRATED |
| Formally Adopted Vocabulary Additions | SRC-001 §12 (gov L1703–1743) | Not present in §6B schema sections | ACCEPTED — NOT YET INTEGRATED |
| BGMM — Biometric-Gated Maintenance Mode | SRC-001 §13 (gov L1744–2037) | Not present | ACCEPTED — NOT YET INTEGRATED |
| TSC — full 31-section detailed design | SRC-002 (gov L2038–3003) | Master §7E-TSC carries a substantial integration summary and explicitly defers to the external full spec as "the authoritative specification" | ACCEPTED — PARTLY INTEGRATED |

**Notes.** (a) The Master's only structural contact with the security spine is at the TSC seam: §7E-TSC
depends on a BAI `"tsc_promotion:<session_id>"`/`"tsc_inspection:<session_id>"` token and a recognized-Ness
SACL session, and references BOP/SIA links. These are dependencies named in the Master, **not** the
designs themselves. (b) The TSC is the one case where the Master contains a real, detailed integration
summary (blocker, authorization, sealing, promotion, inspection, retained archive, boundaries) — hence
"ACCEPTED — PARTLY INTEGRATED" — while the full 31-section behavior remains external and authoritative-in-
scope. (c) None of these mechanisms reaches `INTEGRATED INTO CURRENT AUTHORITY`. (d) Both companions were
written against `MASTER-19_CORRECTED_v6` + `DD-S19_v1` (their stated patch targets); the current authority
pair is v7_1 + DD-S19_v2_2 — re-confirming the patch target is part of any future integration, but is a
Ness decision and is not made here.

---

# 5. CURRENT UNRESOLVED-FEATURE REGISTER (within the current authority set)

**A. Built layer — unresolved/unverified-by-code:**
1. `source_reliability` not-yet-knowable value form — unverified from live code (Master §6B, §6A; DD §5).
2. Production-readings marker check in `append_reading()` — DECIDED, not implemented (Master §6A; DD §5).
3. Whether `append_reading()` holds any production-path check today — unverified from live code (Master §25).
4. `nh_ingest_chatgpt.py` dry-run/test-path mechanism — not confirmed (Master §6A; DD §5).
5. `nh_research_engine.py` import sites; `nh_timeline.json`/`nh_nightly.py` disk presence; Layer-2 store
   write-activity — documented June 19 2026, not re-verified (Master §25; DD §5).
6. Stale "188 seed records" docstring in `_validate_record` — pending cleanup (Master §6A; DD §3M).
7. Disk `.cursorrules` v3.2 sync status — Master notes the disk file was not overwritten in prior sessions.

**B. Engine/build next steps:**
8. Engine C (story-layer) — blocked on story-bearing gold cases (Master §7C; DD §5).
9. Object-identity seam (telling record vs composite reference) — must be settled before story/person-box/
   clash/deletion code relies on telling-level links (Master §7K).
10. Multi-box (sealed-batch) architecture — undesigned; required before a second batch (Master §11; DD §5).
11. Context gold set v1 — drafted/approved, not placed or sealed (Master §6B).

**C. Conceptual designs with named open implementation (per §7 closing lines):** exact schemas, thresholds,
ranking, limits, interface wording, and retrieval safety ceilings for §7E/§7F/§7G/§7H/§7I/§7J/§7K/§7L/§7M/
§7N/§7O/§7P; §7D Living State Web (schema, evidence thresholds, aging, transition conditions, world model,
purpose-aware lenses, build order, currency-review-trigger authorization); §7Q (eligibility rules,
exclusion detection, cryptographic erasure, derivative discovery, backup deletion, minor-data rules); §7R
per-component mode declarations, Tier-2 handling, thresholds, storage formats.

**D. Pipeline / model / interface opens:** academic source (Semantic Scholar vs OpenAlex vs both);
live-retrieval isolated capture environment (undesigned); screenshot-as-inert-image proposal (not decided);
Brave spending-cap counter (must be coded); final Interactive Translator mouth UNDECIDED (Dolphin 3.0 R1
Mistral 24B untested); Hebrew quality gated on bigger model/VRAM; Chat Front Door two questions; §0A
DUMB/SMART placement (name + NOTE/clash location); Mobile open questions; Interface/World undesigned areas;
TSC inspection-authorization mechanism (resolved within SRC-002's §15/§16; integration not done).

**E. Concept-only / not designed:** Wonder/Simulation mechanism; World model; End-to-end cycle.

**F. Meaning-to-technical mapping (§11 item 34 — MUST NOT be silently decided):** five questions (Grounded
Keeper of Origins scope; Origins granularity; Origins time-fields; Those-Three-To-Become-A-One no-context
mode; Holding's Person-Box representation) (Master §25; DD §5).

**G. Accepted-but-external (carried to §4 matrix):** the entire security/identity spine (SRC-001) and the
full TSC design (SRC-002) are accepted, un-built, and un-integrated (TSC partly integrated).

---

# 6. SOURCE-RANGE VERIFICATION REPORT (exactly what full bodies were read)

| Source | Path | Lines | Coverage this pass |
|---|---|---|---|
| SRC-044 Master v7_1 | `/mnt/project/NH_MASTER-19_CORRECTED_v7_1.md` | 1937 | Full heading map; bodies read L174–1404 (premise→§7R) in full, §8–§11 (L1406–1467), §16/§19/§20–§21 and §22–§25 (L1707–1937) in full; §11 mid-items and §17/§18 historical logs scanned via change-logs §20/§21/§25. |
| SRC-015 DD-S19_v2_2 | `/mnt/project/NH_DECISION_DEFAULTS-S19_v2_2.md` | 314 | Read in full (L1–315). |
| SRC-076 Cursor Rules v3.2 | `/mnt/project/cursorrules__1_` | 717 | Full heading/structure map (L1–634); rule content read via the Master's durable §6A summary (which the rules require to match the disk file) and DD §3M. |
| SRC-087 governance/archive companion | `/mnt/project/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | 5580 | Full structure map (Parts I–V); Part II security definitions read (L304–470, plus core definitions of SIA/SACL/BAI/pairing/recovery/emergency/BGMM at L720–1958); Part III TSC opener (L2038–2130). Part IV (wellbeing source) and Part V (superseded MASTER-19_FULL + AFTER_BGMM handoff) identified as embedded archive, not re-read as current authority. |
| SRC-001 accepted security/identity | embedded in SRC-087 Part II (gov L304–2037); also Reader Part 01 | ~1724 | Read via the governance embedding: provenance/status/contents + each of the 13 components' definitions and key rules. |
| SRC-002 accepted TSC v1 | embedded in SRC-087 Part III (gov L2038–3003); also Reader Part 01 | ~956 | Read provenance/status + the full 31-section contents list + §1 opener; integration points cross-read against Master §7E-TSC and DD §3N. |

**Honest scope notes.** (1) This audit is document-based; it performed **no fresh disk inspection**, so
every "BUILT AND DOCUMENTED AS VERIFIED" rests on the authority's documentation (S12–S16), not a
re-verification. (2) For the Master, the line-by-line conceptual bodies of every §7 subsystem were read;
a few mid-section spans of §7R (Decisions 4–7) and §19A–D detail were covered via the section's own
summary lines and the §20/§21 change logs rather than read line-by-line — the feature identity, status,
and boundaries were captured. (3) The governance companion's two embedded accepted companions are
byte-identical preservations of SRC-001/SRC-002 (each carries a `NH_SOURCE_BEGIN` hash header), so reading
them inside SRC-087 is reading SRC-001/SRC-002.

---

# 7. HISTORICAL SOURCES TO EXAMINE IN STAGE 3B (possible lost / weakened / superseded features)

These are NOT examined here. Stage 3B must walk the Stage 2 v1.1 §6 corrected queue and check each
against this current baseline for any feature that was once present and is now weakened, dropped, or
superseded — preserving every source.

1. **MASTER-19 comparison cluster {v1, v3, v6, FULL}** (SRC-041, 042, 043, 045) — internal order UNCLEAR;
   compare each against v7_1 for content the current authority may have dropped or changed.
2. **MASTER-18 full draft (S18)** (SRC-040) and **MASTER-17 full draft + 4 reader slices (S17)**
   (SRC-039; SRC-035–038) — the consolidation lineage that fed v7_1.
3. **MASTER-14 cluster (S13)** (SRC-027–034) — the 2a "built vs plumbing-only" correction; check the
   reading-record claims against the built baseline.
4. **MASTER-13 (S12)** (SRC-026); **MASTER-11 / 11.1 (S10)** (SRC-024, 025); **MASTER-10 / 10__1_ (S9)**
   (SRC-022, 023); **MASTER-9 / 9.2 / 9.4** (SRC-051, 052, 053); **MASTER-5/6/6__1_/7/8** (SRC-046–050) —
   the reality→story re-soul, the §13 live loop, the early engine/store design.
5. **Pre-spine standalone masters:** `MASTER_FILE_COMPLETE` + `__1_` (SRC-055, 056) and `MASTER_CONTEXT`
   (SRC-054) — earliest founding-principle and naming content (and the "Nes/Ness" conflict).
6. **Decision-Defaults lineage:** S17_AUDITED (SRC-013), S13 family (SRC-009–012), S12 (008), S10_1 (007),
   early DD (016/017/018/019) — for behavioral rules the current DD may have dropped.
7. **Addenda / deltas / continuity:** `section13_ADD` (SRC-057), `DELTA_S14` (SRC-020),
   `RECENT_CONTINUITY_NOTE_POST_MASTER17` (SRC-060), the two handoffs (SRC-004, 061).
8. **Design-source specs** (full mechanisms the Master may only summarize): Universal Filter Design ×3 +
   RULES (SRC-062–065), Meaning Engine B5 design (SRC-058; B1 body UNRECOVERABLE), Mobile spec (059),
   Canvas spec (006), chat front-door sketch (067), wellbeing baseline source (074), research
   architecture (085), search-pipeline security (086), risk review/OpenRouter (072, 073), INSIGHT (021),
   Build Checklist (003), Cursor brief (005).
9. **Prototypes / code / diagrams** (SRC-069–071, 078–084) and the **field-survey PDF** (075) — for any
   feature evidence not captured in prose.
10. **Provenance manifests v1–v5** (SRC-088–092) and the **superseded MASTER-19_FULL embedded in
    governance Part V** — for provenance cross-checks only.

---

## STATE AFTER STAGE 3A (nothing decided, nothing changed)
- Authority unchanged: v7_1 / DD-S19_v2_2 / Cursor Rules v3.2 / governance companion v1.
- No historical Master compared; no conflict resolved; no design judged; nothing integrated, patched, or
  decided; no organization chosen; no canonical Master drafted; Stage 3B not begun.
- The six current-authority + companion bodies are now feature-mapped; the accepted companions are placed
  against the Master only.

**STAGE 3A COMPLETE. AWAITING NESS.**
