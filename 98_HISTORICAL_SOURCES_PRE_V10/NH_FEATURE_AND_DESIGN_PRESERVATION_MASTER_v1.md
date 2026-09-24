# N.H — FEATURE & DESIGN PRESERVATION MASTER  ·  v1

**One job: make sure no feature and no design can be quietly killed or dropped.**

This file holds, in one place, *every feature N.H has or was meant to have* — its **concept** (what it
means and why it exists) and its **base design** (how it is meant to work, at the level that has actually
been decided) — together with an honest status for each. It is the defensive floor: if a feature is ever
missing, weakened, or silently changed somewhere else, this file is where you check it against.

---

## WHAT THIS FILE IS — AND IS NOT

**It is** a preservation and defense layer — a complete, plain catalogue of features + base design +
status, built from the recovered feature inventory (Stage 3A baseline, the accepted companion designs,
and the June-28 candidate laws).

**It is NOT** the adopted Master. It does **not** replace `NH_MASTER-19_CORRECTED_v7_1.md`, does **not**
change Decision Defaults or Cursor Rules, does **not** adopt any candidate, and does **not** decide
anything on your behalf. Current authority is unchanged: **Master v7_1 · Defaults v2.2 · Cursor v3.2 ·
governance companion**. Where a feature is built, designed, accepted, candidate, open, or historical,
this file says so plainly and never upgrades one to another.

**Two separate layers, on purpose.** This file is the *design-preservation* layer (everything, kept safe).
Deciding what is **current vs not** is a *separate* layer — that is the one-card-at-a-time chooser, where
your own eye decides. Keeping them apart is what stops the circling: nothing is lost here, and selection
happens there.

## HOW TO READ AN ENTRY

Each entry is: **`ID — Name`  ·  `[STATUS]`**, then —
- **Concept** — what it is and why it exists (the meaning).
- **Base design** — the decided mechanism, at the level actually settled (no invented detail).
- **Depends on** — what must exist for it to work.
- **Source** — where it is evidenced in the authority/companion/candidate.
- **Open** — what is *not* yet decided (kept open, never quietly closed).

## STATUS LEGEND

- **BUILT & VERIFIED** — on disk and documented as verified (not re-checked live in this pass)
- **BUILT (not re-checked on disk)** — built per records, not freshly disk-verified
- **PARTLY BUILT** — some of it is built, some not
- **PARTLY DESIGNED** — design is partial; named pieces are still undesigned
- **DESIGNED — NOT BUILT** — concept/design complete; no code yet
- **ACCEPTED — NOT INTEGRATED** — accepted design; not yet folded into the authority files
- **IN CURRENT AUTHORITY** — a governing principle already in the Master/Defaults
- **CANDIDATE — NOT ADOPTED** — proposed in an unadopted file; feature-level evidence noted per entry
- **OPEN / UNRESOLVED** — named but not decided
- **INTENTIONALLY LEFT OUT** — deliberately excluded — kept as a decision, not a gap
- **HISTORICAL / INACTIVE** — past/abandoned — kept as history, not live design

---

# THE FEATURES

## A. Foundational premise and frame

### A1 — The Premise (never decide facts / never close the book)  ·  [DESIGNED — NOT BUILT]
**Concept.** The floor rule under every other rule. Stops reasoning from hardening into a closed, settled fact; the AI may reason, connect, lean, wonder — never close the book or promote a conclusion to "real."
**Base design.** Every conclusion stays a non-decisive, accreting layer; Ness decides off-board in real life, never as an engine step; recording *that* he reacted is allowed, the truth-verdict is not.
**Depends on.** Governs every subsystem.
**Source.** Master §0 (L174–190).
**Open.** "Hold firmly" ≠ "close"; the DUMB machinery may establish directly-verifiable machine-state/provenance facts, the SMART machinery never silently promotes interpretation to fact.

### A2 — The Two Machineries (DUMB vs SMART / psychologics) + the membrane  ·  [DESIGNED — NOT BUILT]
**Concept.** Top-level architectural frame splitting the system into data-moving vs person-reading halves. DUMB moves/holds data and is safe because it cannot interpret; SMART reads the person and is safe because it cannot close; the membrane is the boundary.
**Base design.** DUMB: append/point/carry/sort/gather only. SMART: everything weightless, dated, confidence-tagged, rejectable. (4)/
**Depends on.** Underlies the store, two-file split, person-box gather (DUMB) and the meaning webs, story layer, clash, wonder, NOTE (SMART).
**Source.** Master §0A (L193–204); DD §2 (L42–50).
**Open.** Open pins (§11 item 17 / DD §5): whether the name is "SMART" or "psychologics"; where the NOTE and clash sit within the frame. Pure-tape redaction path and "absence-is-read" guard are flagged needs.

### A3 — What N.H is / two destinations / two purposes  ·  [DESIGNED — NOT BUILT]
**Concept.** Defines the system: sovereign local memory+meaning helper; "Jarvis is the memory + soul + gathering + mouth wired together," not the model. Every eligible accepted input goes to TWO places — a sealed raw root and a reading beside it (why there are two files); runs INWARD (mirror of Ness's own thinking) and OUTWARD (translate new data through his lens) at once.
**Base design.** New input is read by the webs and lands as a reading; growth lands in memory, never the frozen mouth.
**Depends on.** Accretive store, filter/engine, mouth.
**Source.** Master §1 (L208–223), §1A (L227–231); DD §1 (L32–38).
**Open.** הכל יחסי — meaning is never final, always relative and relative-to-whom.


## B. The machine and codebase

### B1 — The machine (hardware + launch)  ·  [BUILT & VERIFIED]
**Concept.** The physical host. Local, offline-by-default desktop; only research connectors and the mobile Full-Mode tunnel touch the network.
**Base design.** Launched by `run_app.pyw` → pywebview at localhost:8080. (4)/
**Depends on.** All components run here.
**Source.** Master §4 (L283–290).
**Open.** RTX 2060 6GB runs 3B models ~35–50 tok/s, 7–8B slow (~7–9 tok/s), limited context; settled upgrade direction RTX 3090 24GB (purchase-time verification required — a hardware decision, carried for the audit not as chronology).

### B2 — Codebase map / three physical store sets  ·  [BUILT & VERIFIED]
**Concept.** Inventory of code modules and on-disk stores. Tells each layer which files/stores it owns.
**Base design.** Protected core modules (old gate stack) still run harmlessly; Layer-3 accretive files are the active build target. (4)/
**Depends on.** cursorrules protection.
**Source.** Master §5 (L294–325).
**Open.** "Verify on disk; the doc's remembered state has been wrong repeatedly."


## C. Built storage substrate

### C1 — The accretive store (append-only roots-of-record)  ·  [BUILT & VERIFIED]
**Concept.** The DUMB-machinery heart. Append-only store of raw root records; schema-validated before every append; roots file sealed.
**Base design.** `append_root()` refuses while `.nh_roots.sealed` exists; no direct file writes permitted.
**Depends on.** `nh_accretive_store.py` is the sole write boundary.
**Source.** Master §6B (L470–495), §5 (L300–301); DD §3C (L77–84).
**Open.** Production readings path gated (see C4); seed-only; multi-box architecture undesigned (must precede any second batch).

### C2 — 7-field root schema (v1, sealed)  ·  [BUILT & VERIFIED]
**Concept.** The immutable shape of a root. Fixed fields so roots are stable and never reinterpreted.
**Base design.** All seven required on every root; immutable once written; only change is audited destruction (§7Q).
**Depends on.** Accretive store; ingest pipeline.
**Source.** Master §6A schema constraints (L389–391), §6B (L474–476); DD §3B (L70–75).
**Open.** Do not reinterpret `subject`; schema change needs a new `schema_version` and Ness's adoption; a future rename (`source_batch`) is an open item.

### C3 — 12-field reading record (validator + writer)  ·  [BUILT & VERIFIED]
**Concept.** The interpretive layer that points at roots. Hold a reading beside a root without copying its text.
**Base design.** `_validate_reading()` gates SHAPE only (rejects malformed, never uncertain); writer verifies each `reads` root id exists in the sealed store, checks idempotency, routes to quarantine/production.
**Depends on.** Accretive store, mouth/engines.
**Source.** Master §6B (L478–494), §6A (L393–395); DD §3A (L56–68).
**Open.** `source_reliability` not-yet-knowable value form is **unverified from live code** — must be confirmed from the live validator before v3.2 fully adopted; no `reason`/`why` field by design.

### C4 — Roots seal + production-readings authorization (dual gate)  ·  [BUILT & VERIFIED]
**Concept.** Two protections guarding new writes. Prevent accidental root appends and premature production readings.
**Base design.** `.nh_roots.sealed` blocks `append_root`; production readings require both a Ness-created `.nh_readings_production_authorized` marker AND an approved dry-run.
**Depends on.** Accretive store; Cursor behavioral rule.
**Source.** Master §6A (L385, L399–407), §5 (L301–303); DD §3C (L82).
**Open.** Whether `append_reading()` currently contains any production-path check is unverified from live code.

### C5 — Quarantine readings store  ·  [BUILT & VERIFIED]
**Concept.** Test sink for engine output. Keep all engine readings out of production.
**Base design.** Both engines write here, never production.
**Depends on.** Reading writer.
**Source.** Master §5 (L303), §6B (L492).
**Open.** Production store absent by design.

### C6 — Gold sets v1 and v2-B (sealed outside exam)  ·  [BUILT & VERIFIED]
**Concept.** Sealed answer keys for grading engine readings. An outside exam only Ness grades; engine output may fail but may never alter a case.
**Base design.** Engine runs against the cases; Ness scores by semantic match by hand.
**Depends on.** Engines A/B.
**Source.** Master §6 (L333–334), §6B (L304–307); DD §3D (L85–92), gold-scoring six rules (L90).
**Open.** `story_layer` not graded in v1/v2-B; a correction is a new versioned gold; a context gold set v1 was drafted/approved but not yet placed or sealed.


## D. Built engines and tooling

### D1 — Engine A (`nh_engine_minimal.py`)  ·  [BUILT & VERIFIED]
**Concept.** Bare reader. Read one root with no context and lay a 12-field reading beside it.
**Base design.** `read_root(root_id)` → mouth ("say what the {role} is doing; don't describe/answer/invent") → reading → quarantine; `run_on_gold()` runs the 8 v1 cases.
**Depends on.** Accretive store, mouth model.
**Source.** Master §6 (L335), §5 (L317), §7C (L570).
**Open.** `MOUTH_MODEL` is a test candidate only; benchmark-protected.

### D2 — Engine B (`nh_engine_b.py`)  ·  [BUILT & VERIFIED]
**Concept.** Context reader. Read a root in the context of the preceding turns in the same thread.
**Base design.** `read_root_b` → `_get_preceding_turns(n=3)` (position-based, same `source_title`, full content, no truncation) → BACKGROUND/END BACKGROUND framing → mouth → reading → quarantine; `run_on_gold()` runs 7 v2-B cases.
**Depends on.** Accretive store, mouth, `source_title` grouping.
**Source.** Master §6 (L336), §5 (L318), §7C (L571); DD §3E (L94–100).
**Open.** Cause of the remaining miss NOT isolated (model capability, prompt framing, context format, run variance all possible); n=3 is the experiment's setting, not a universal future limit.

### D3 — Chroma `nh_roots_v1` + `nh_rebuild_chroma.py`  ·  [BUILT & VERIFIED]
**Concept.** Semantic index of clean roots. Retrieve roots by meaning-distance.
**Base design.** Rebuild script has a `--dry-run` (10-root test + retrieval check); full run = 5,521 roots in ~187.59s; never touches old collections.
**Depends on.** Accretive store, embedding model.
**Source.** Master §6 (L337–338), §5 (L309, L319).
**Open.** Old collections must not be modified/dropped.

### D4 — Ingest pipeline (`nh_ingest_chatgpt.py`)  ·  [BUILT & VERIFIED]
**Concept.** Clean ChatGPT-export parser. Turn JSON exports into clean roots.
**Base design.** Tree-walk ordering, clean fields, junk-skip; ran on three JSON sources → 5,521 roots.
**Depends on.** Accretive store, seal.
**Source.** Master §5 (L311, L321), §6B (L476); DD §3C.
**Open.** Existing dry-run/test-path mechanism not confirmed; `gpt_purified` and `cleaned_history` deliberately not ingested.

### D5 — Speaker-detector recipe (`nh_embed_confirm_speaker.py` reference)  ·  [PARTLY BUILT]
**Concept.** Fallback for role-less sources. Propose a speaker when source lacks `role`.
**Base design.** Investigated ten methods; embed+shape (LogReg C=0.1, 5-fold) reached ~94.89%; recipe locked, NOT deployed (read-only probes).
**Depends on.** Embedding model.
**Source.** Master §6 (L340), §6A (L422), §7C (L567).
**Open.** A proposal stays a proposal until confirmed by Ness or source evidence; never silently written to `role`.


## E. Code governance — Cursor Rules v3.2 (operational authority)

### E1 — Three-layer architecture + permanent prohibitions  ·  [BUILT (not re-checked on disk)]
**Concept.** The operative ruleset Cursor obeys. Keep three coexisting code layers separate and protect both the legacy gate and the accretive store.
**Base design.** Layer 1 legacy read-only; Layer 2 still-running gate; Layer 3 active build target; "Cursor proposes, Ness approves, Cursor implements"; never touch `.env`, PIN hash, vault, tokens; never write test/mock data into production; never build a parallel gate.
**Depends on.** All build work.
**Source.** Cursor Rules v3.2 (SRC-076) IDENTITY+§1 (L51–181), §6 three-layer map (L413–462); Master §6A (L357–376); DD §3M (L195–202).
**Open.** Stale "188 seed records" docstring in `_validate_record` pending cleanup.

### E2 — Protected files/stores + dry-run protocol + five protection decisions  ·  [BUILT (not re-checked on disk)]
**Concept.** Change-control gate for sensitive files. No edit to a protected file without "CONFIRMED: modify [file]" + a full PROPOSED CHANGE dry-run and "APPROVED."
**Base design.** Lists Layer-2 and Layer-3 protected files; five settled decisions (engine benchmark protection; ingest protection; rebuild no-touch-old-collections; production-readings dual-authorization; `nh_baseline_engine.py` creation gate).
**Depends on.** All Layer-3 work.
**Source.** Cursor Rules §7–§8 (L463–573); Master §6A (L410–457); DD §3M (L201).
**Open.** `nh_baseline_engine.py` creation gate carries six §22 prerequisites.

### E3 — Pull Sovereignty + "before adding any feature that touches memory  ·  [BUILT (not re-checked on disk)]
**Concept.** Behavioral guardrails. No unsolicited autonomous tasks; watch for unexpected agent file spawns; check before extending memory.
**Base design.** Stop-and-look if a tool call queues more files than asked.
**Depends on.** Cursor.
**Source.** Cursor Rules §10–§11 (L597–633).
**Open.** —


## F. Legacy gate (still running)

### F1 — REALITY/SIMULATION gate stack (Layer 2)  ·  [BUILT (not re-checked on disk)]
**Concept.** The old sovereignty mechanism. Gate unverified content into REALITY only through one authorized path.
**Base design.** `promote_to_memory()` in `nh_context_router.py` is the one gate; `ContextRouter.write()` is NOT a gate (the exact June-19 bypass); `NH_PROMOTE_TOKEN` active; status labels INFERRED/GENERATED/ VERIFIED/REPORTED_SPEECH apply here.
**Depends on.** Governs running chat, HUD, research pipeline.
**Source.** Master §5 (L297), §6A (L371–373, L381); Cursor Rules §2A (L183–221); DD §3M (L199).
**Open.** Still-active legacy (not inactive); to be reconciled only when the new filter is complete and Ness declares the new model active; do not rip out early.


## G. Universal Filter + Meaning Engine (design)

### G1 — Universal Filter (R0–R12) + the Keystone  ·  [DESIGNED — NOT BUILT]
**Concept.** The operating rules of the one continuous reader. One filter, not two stages: finding a meaning-boundary and naming its type are one act; meaning comes from wide context; classification never locks; memory only adds.
**Base design.** Words flow in → the reader tracks meaning → when the type shifts it closes a statement, tags it, opens the next; a later context re-colors an old statement by adding a layer, never editing.
**Depends on.** Meaning engine, accretive store.
**Source.** Master §7A (L500–516); DD §2/§6.
**Open.** Ness steers/affirms off-board; the membrane is the boundary.

### G2 — The Meaning Engine seven webs + parts  ·  [DESIGNED — NOT BUILT]
**Concept.** The reading mechanism. A piece's meaning is how dimensions relate across webs, not one flat tag.
**Base design.** The piece runs through INTENT, DEIXIS, COMMON-GROUND, IMPLICATURE, THEORY-OF-MIND, TIME/SEQUENCE, RE-READING together in one pass; the parts include the Pure Tape (Part 0), nightly research (Part 4, feeds memory not the mouth), inform-don't-ask (Part 6), wonder/simulation (Part 6.5), the LOG (Part 7), the NOTE/why (Part 7.5).
**Depends on.** Mouth, store, webs.
**Source.** Master §7B (L517–565).
**Open.** Wonder/ simulation mechanism is concept-only; "register/mode" placement was an early open thread.

### G3 — The Forced Build Order + engine layers A→B→C  ·  [PARTLY BUILT]
**Concept.** The never-re-fought build sequence. 2a (reading record) → 2b (detector) → 2c (engine A→B→C); build the live path before nightly deepening.
**Base design.** A ✅ built, B ✅ built, C (story-layer) next, needs story-bearing gold cases. (4)/
**Depends on.** Store, engines, gold.
**Source.** Master §7C (L566–573); DD §3E/§4.
**Open.** Engine C blocked on story-bearing gold cases.


## H. Catalog Front Door + Temporary Session Cache

### H1 — Catalog Front Door (two gates / minimum intake envelope / four enrichment categories)  ·  [DESIGNED — NOT BUILT]
**Concept.** The capture-and-normalize entry stage. Separate raw capture from root ingestion; a root cannot be sealed until required catalog fields resolve; raw material never destroyed for an unresolved field.
**Base design.** Each front door produces a minimum intake envelope (capture_id, raw payload/ref, timestamp, source-type, format, source metadata, provenance); a unified pre-ingest holding area carries items with a blocker list through `held→ready→promoting→promoted` (+ rejected/excluded/error); promotion to the sealed store is atomic and idempotent.
**Depends on.** §7Q precedence; speaker/thread rules; accretive store.
**Source.** Master §7E (L616–648).
**Open.** Four enrichment categories (source facts / mechanical derivations / machine proposals / forbidden semantic interpretation); exact schemas/field names undesigned; `role` and `source_title` resolution rules; never silent drop.

### H2 — Temporary Session Cache (TSC) — §7E integration summary  ·  [DESIGNED — NOT BUILT]
**Concept.** Organized holding mode within §7E for sessions involving people other than Ness. Hold an entire third-party session under a fingerprint-authorization blocker until Ness authorizes promotion.
**Base design.** Every item enters §7E carrying `"pending_fingerprint_authorization"`; a transactional structural DB organizes order/attribution/branches/BOP+SIA links/N.H outputs/lifecycle; on close the cache seals immutably and waits indefinitely; the blocker lifts only via a purpose-bound BAI token `"tsc_promotion:<session_id>"` consumed with a confirmed recognized-Ness SACL session; then items promote through the normal §7E lifecycle preserving order.
**Depends on.** §7E, §7Q, BAI, SACL, BOP, SIA, `append_root()`.
**Source.** Master §7E-TSC (L650–675); DD §3N (L204–218).
**Open.** Inspection uses a separate `"tsc_inspection:<session_id>"` token; the full 31-section spec is the authoritative specification and is external.


## I. Context Retrieval (§7F)

### I1 — Two-channel context retrieval (positional vs semantic)  ·  [DESIGNED — NOT BUILT]
**Concept.** Supplies context to a reading pass. Keep "what came immediately before in this thread" (positional) strictly separate from "what else may relate" (semantic).
**Base design.** Each retrieved item carries retrieval provenance; both channels shown in separate prompt sections; a conflict is surfaced, not silently resolved; per-mode parameters; genuine no-context is a normal condition, distinct from system failure.
**Depends on.** Engine, Chroma, `source_title`.
**Source.** Master §7F (L678–701); DD §3G (L119).
**Open.** Trigger conditions, exact limits, ranking, thresholds, and safety-ceiling values undesigned; each mode must declare its §7R relevance config later.


## J. Meaning Engine Interior + Acceptance Check (§7G)

### J1 — One-reading-per-pass + Reading Proposal Acceptance Check  ·  [DESIGNED — NOT BUILT]
**Concept.** The interior reading flow and its gate. One pass = one reading record for one target root; the mouth does not judge its own output.
**Base design.** Flow: target root + optional context + declared mode → mouth proposal → acceptance check → reading record; acceptance verifies grounding, no invention, channels not confused, honest uncertainty, mode followed; failures recorded as distinct reasons.
**Depends on.** Mouth, context retrieval, store.
**Source.** Master §7G (L704–743); DD §3G (L120).
**Open.** FIRST-CLASS: model confidence is metadata, not authority; story-layer evidence kept in two labeled channels; circular support forbidden; exact criteria/thresholds/retry undesigned.


## K. Reread Lifecycle (§7H)

### K1 — Reread triggers (manual / condition-based / scheduled retry)  ·  [DESIGNED — NOT BUILT]
**Concept.** Controls when an old reading is re-read. A reread never happens without an explicit recorded reason.
**Base design.** Three trigger types only; time passing alone is never a condition; a reread creates a NEW reading, never overwrites; rejection is recorded and may make a reading eligible.
**Depends on.** Meaning engine, §7R.
**Source.** Master §7H (L747–763); DD §3G (L121).
**Open.** Exact relevance rules, retry limits, scheduling undesigned.


## L. View Layer + Computed View (§7I, §7M)

### L1 — View Layer (current + history)  ·  [DESIGNED — NOT BUILT]
**Concept.** Per-root presentation of readings. Simple by default, complete on demand; ordering is presentation only, never authority.
**Base design.** Current view surfaces the newest usable reading and surfaces conflicts explicitly; history view shows strict chronology; nothing deleted/hidden/overwritten.
**Depends on.** Computed View seven-factor ordering when claiming "current best."
**Source.** Master §7I (L767–777).
**Open.** Exact grouping/labels/layout undesigned.

### L2 — Computed View (seven-factor ordering, immutable snapshots)  ·  [DESIGNED — NOT BUILT]
**Concept.** The present-facing surface. Assemble the most useful current picture without altering objects or declaring a winner.
**Base design.** Seven explicit factors (Ness's judgment → root-evidence strength → grounding → relevance → context quality → clashes-surfaced → recency tie-break) with no hidden score; triggered updates only; each update writes a new immutable snapshot.
**Depends on.** Most other subsystems; §7R for factor 4.
**Source.** Master §7M (L885–912); DD §3G (L126).
**Open.** Must be able to say "no clear current view"; exact relevance rules/thresholds/snapshot schema undesigned.


## M. Clash Handling (§7J)

### M1 — Contradiction/clash records (six types, two detection modes)  ·  [DESIGNED — NOT BUILT]
**Concept.** Records conflicts without resolving them. Distinguish genuine contradiction from contextual difference; never resolve.
**Base design.** Six clash types; triggered + periodic detection produce the same record type; the same clash never spawns duplicates (later detection appends an event); Ness's response is a separate linked event; downstream actions are separate linked records.
**Depends on.** Meaning engine, view/computed view, person-boxes.
**Source.** Master §7J (L781–811); DD §3G (L123).
**Open.** A clash is not automatically an error; exact schemas/detection/ dedup undesigned.


## N. Story Layer (§7K)

### N1 — Story Layer (tellings, structured perspective, firmness, hybrid themes)  ·  [DESIGNED — NOT BUILT]
**Concept.** Holds per-person tellings across time. Record tellings unaltered; keep each person's story separate; preserve clash; never merge into one narrative.
**Base design.** Tellings connect by explicit shared attributes (navigational links, not merges); structured perspective model (`root_speaker`, `subject`, `perspective_owner`, optional `attribution_path`); firmness inferred from observable signals and kept separate from model confidence; themes are engine-proposed, Ness-confirmed navigation categories.
**Depends on.** Meaning engine, person-boxes, clash.
**Source.** Master §7K (L815–850); DD §3G (L124).
**Open.** **Object-identity seam UNRESOLVED** — tellings are embedded in `story_layer`; no standalone telling record/ID exists; must be designed before story/person-box/clash/deletion code relies on telling-level links; firmness scale and theme schema undesigned.


## O. Person-Boxes (§7L)

### O1 — Person-Boxes (gather, proposal-based anchors, merges)  ·  [DESIGNED — NOT BUILT]
**Concept.** Stable identity anchor per person. Gather everything linked to a person without synthesizing a profile.
**Base design.** Links roots/readings/tellings/themes/clashes/responses/other boxes (links never copies); uncertain identity is normal; proposed anchors never silently become confirmed boxes; merges require explicit resolution and never rewrite history.
**Depends on.** Story layer, clash, computed view.
**Source.** Master §7L (L853–875); DD §3G (L125).
**Open.** SETTLED FACT: Ness has a Person-Box (June 25) — its creation/anchoring/maintenance not yet designed; matching/ merge mechanics undesigned.


## P. Living State Web (§7D)

### P1 — Living State Web (state/transition modeling)  ·  [PARTLY DESIGNED]
**Concept.** Future layer to model a person moving through states over time. Beyond meaning/memory: model state, transitions, open loops, relationships, causal hypotheses, counterfactuals, values/constraints.
**Base design.** S17 designed node/edge types, a grounding rule (every node carries source + root ids; circular support forbidden), and a currency rule (existence vs currentness are independent; six currency statuses; time alone never marks a state ended).
**Depends on.** Computed View, Story Layer, Person-Boxes, §7P, §7Q, §7R.
**Source.** Master §7D (L576–612); DD §3G (L131).
**Open.** Many domains and all implementation details undesigned (schema, evidence thresholds, aging windows, transition conditions, world model, purpose-aware lenses, build-order position, currency-review-trigger authorization).


## Q. Action lifecycle (§7N, §7O)

### Q1 — Action Surfacing (permission-controlled hybrid)  ·  [DESIGNED — NOT BUILT]
**Concept.** Surfaces possible actions. Show possibilities (never instructions/decisions); Ness is sole decider.
**Base design.** Two modes (on request always; proactive only under an authorized relevance rule); every possibility labeled "one possible option," records what it derived from + uncertainty; six Ness-response states; rejection is never treated as failure; no repeat surfacing without a new trigger.
**Depends on.** Living State Web, §7P, §7R.
**Source.** Master §7N (L916–941); DD §3G (L127).
**Open.** Action-category→risk-level mapping, evidence/ permission thresholds, interface wording undesigned.

### Q2 — Action-Result Return Path (two result types, six result states)  ·  [DESIGNED — NOT BUILT]
**Concept.** Handles what happened after an action. Never let the system declare an action's result on its own.
**Base design.** Explicit reported result (Ness reports, enters as a normal root) vs detected possible result (a proposal linking material to an action, never a silent declaration); causation never inferred from timing/similarity; three separate linked objects (action, result root, connection); six result states.
**Depends on.** §7N, §7P, reread, Living State Web.
**Source.** Master §7O (L945–974); DD §3G (L128).
**Open.** Detection rules, confirmation workflow, subcategories undesigned.


## R. Permission and Authority Boundaries (§7P)

### R1 — Permission/Authority Boundaries (three action states, four risk levels, two authority layers)  ·  [DESIGNED — NOT BUILT]
**Concept.** The boundary between helper and actor. Define what N.H may do alone, must preview, must ask, or may never do.
**Base design.** Suggesting/Preparing/Executing; four risk levels (internal read-only → internal write → prepared external → executed external); standing vs moment-level authority; silence is never approval; absolute boundary requires per-instance confirmation for medical/legal/financial/privacy/relationship/ destructive/irreversible actions; on violation, stop-and-surface is default; five separate linked objects; a narrow emergency-stop exception cannot reverse a completed world.
**Depends on.** Action surfacing/result, all external action.
**Source.** Master §7P (L978–1031); DD §3G (L129).
**Open.** Exact permission categories, authorization-object schema, and interface undesigned.


## S. Privacy, Deletion, Sensitive-Data (§7Q)

### S1 — Privacy/deletion/sensitive-data handling (five operations, four levels, two-stage access)  ·  [PARTLY DESIGNED]
**Concept.** Governs capture, classification, access, display, and deletion of sensitive material. Protect secrets and third-party data; keep Ness's own access open while restricting external exposure.
**Base design.** Five distinct operations (exclusion/hiding/restriction/redaction/deletion); four sensitivity levels; deletion is blocking and verification-based with five outcomes (`verified_complete` the only "complete") and a content-free tombstone; two-layer capture exclusion (non-negotiable core vs Ness-configured); third-party baseline; two-stage output access control (pre-retrieval eligibility + pre-output review); model-provider refusals recorded as mouth limitations.
**Depends on.** Catalog, computed view, story, person-boxes, Living State Web, §7R prerequisite.
**Source.** Master §7Q (L1034–1121); DD §3G (L130).
**Open.** CENTRAL RULE: private access for Ness open by default. Many mechanics undesigned (exact eligibility rules, exclusion detection, cryptographic erasure, derivative discovery, backup deletion, minor-data rules, verification procedures).


## T. Attention and Relevance Control (§7R)

### T1 — Attention and Relevance Control (two-layer judgment, fourteen decisions)  ·  [DESIGNED — NOT BUILT]
**Concept.** Decides what is worth showing/retrieving/acting on, by explicit auditable rule. Provide a shared relevance definition every surfacing component uses.
**Base design.** Output = a context boolean gate + graded named dimensions each with provenance (no hidden score); three producer types per dimension (deterministic rules, embedding model, mouth-for-declared-interpretive-only); on-demand by default (no global relevance state); two-tier mode contract; Ness inspects/overrides per-judgment and changes modes via consequence preview; mouth-dimension validation; disagreement and relevance-event records; pattern-observation rule; halt on unrecognized purpose type.
**Depends on.** §7Q prerequisite; consumed by Context Retrieval, Computed View, Action Surfacing, Reread, Living State Web.
**Source.** Master §7R (L1125–1404); DD §3H (L133–142).
**Open.** RELEVANCE IS NOT TRUTH/EVIDENCE/AUTHORITY/PERMANENT; per-component mode declarations, Tier-2 handling, thresholds, storage formats remain open.


## U. Research / Knowledge Catcher pipeline (§8)

### U1 — Research pipeline (Brave → synthesis → gate; source preservation)  ·  [DESIGNED — NOT BUILT]
**Concept.** Brings outside info into the review queue and re-checks stored info against sources. Gather raw web data and check stored claims, landing findings in MEMORY as readings, never the mouth.
**Base design.** Brave (raw JSON) → one auditable OpenRouter/llama synthesis (text-in/text-out only, no tools/file/network) → create-space → gate; auto-reject never auto-delete; rejected-bin "look don't touch" display; source preservation saves a plain-text excerpt + a frozen full-page screenshot (inert) with provenance/hash; fallback marks SOURCE PRESERVATION INCOMPLETE.
**Depends on.** Legacy gate, mouth/synthesis model, store.
**Source.** Master §8 (L1406–1431); DD §5 (L264–265).
**Open.** Brave has NO spending cap — a query counter/daily cap MUST be coded; live full-page capture needs an isolated environment (undesigned); academic source open (Semantic Scholar vs OpenAlex vs both); screenshot-as-inert-image proposal not yet decided; re-check schedule only with Ness's explicit approval.


## V. Model layer (§16)

### V1 — The borrowed frozen mouth + embedding/search model + synthesis model  ·  [BUILT & VERIFIED]
**Concept.** The swappable language layer. The model is a commodity mouth; everything that makes N.H its own lives outside it; search first, word last; growth lands in memory not the mouth; uncensored by design.
**Base design.** `dolphin-llama3` (8B) is the CURRENT TEST MODEL on disk (not the adopted final Interactive Translator); `all-MiniLM-L6-v2` is the tiny search model; an OpenRouter synthesis model serves research.
**Depends on.** Engines, retrieval, research.
**Source.** Master §16 (L1542–1567), §4; DD §3F (L102–113).
**Open.** Final mouth UNDECIDED; Dolphin 3.0 R1 Mistral 24B is the first post-upgrade candidate (untested); a new mouth must pass BOTH sealed gold sets before replacing the current one; Hebrew quality weak-but-workable, gated on bigger model/VRAM; model-provider limits are mouth limits.


## W. Live path: Live Loop + Chat Front Door (§13, §14)

### W1 — The Live Loop  ·  [DESIGNED — NOT BUILT]
**Concept.** The fire-and-let-go concurrency design. Deep work never blocks the chat; the deep side announces itself back; parallel topics become mechanically possible.
**Base design.** The chat speaks fresh from a silent memory pull; the loop carries N.H's own output toward memory only as an append-only proposal, never a closing/REALITY write.
**Depends on.** Store, membrane.
**Source.** Master §13 (L1504–1517).
**Open.** THE GUARD: the fast loop must never become a closing/REALITY-write path.

### W2 — The Chat Front Door  ·  [PARTLY DESIGNED]
**Concept.** The live chat as a first-class input. Treat Ness↔N.H chat as recorded input (speaker carried, connect-not-claim, point-back shown, mechanism never narrated).
**Base design.** Two-filter path riding the live loop; the point-back is the one clickable thing shown.
**Depends on.** Live loop, store, membrane.
**Source.** Master §14 (L1519–1536); DD §5 (L276).
**Open.** Two open questions: creation-filter as a distinct mechanism vs a mode; always-capture vs deliberate-capture.


## X. Image ingest front door (§9A)

### X1 — Image ingest (first worked front-door example)  ·  [DESIGNED — NOT BUILT]
**Concept.** A worked example of a new front door. Show how a non-text input becomes engine-readable pieces.
**Base design.** Metadata → plain description → context meaning → Ness confirms.
**Depends on.** Catalog front door, engine.
**Source.** Master §9A (L1436–1437).
**Open.** Precondition for WhatsApp media ingest (deferred).


## Y. Interface, World, and Interaction (§19)

### Y1 — Interface/world/interaction system  ·  [PARTLY DESIGNED]
**Concept.** The future interactive environment ("Ness's World"). A navigable space for architecture and solving.
**Base design.** Settled: world manipulation is presentation/navigation/explicitly-labeled-simulation only by default (does not mutate records).
**Depends on.** §7P (authority), §7Q (camera/VR front doors), simulation.
**Source.** Master §19 (L1613–1699).
**Open.** Simulation interior, gesture vocabulary, VR, camera, accessibility, visual language largely undesigned; three open cross-component dependencies (approval-explicitness vs unobtrusiveness; camera/VR as new front doors; external actions from within the world).


## Z. Wellbeing and Behavioral Baseline System (§22)

### Z1 — Wellbeing/behavioral baseline (Ness vs Ness)  ·  [DESIGNED — NOT BUILT]
**Concept.** A self-monitoring layer protecting both data integrity and Ness's wellbeing. Detect when Ness's judgment is off-baseline (since REALITY rests on his judgment).
**Base design.** Builds the baseline passively from demonstrated behavior (promotion/rejection patterns, conversation/decision patterns); a monthly surface Ness can refine but not override; four tiers (silent flag → mirror signal → queue throttling → REALITY freeze); unlock via a psychiatric/medical appointment record used as a calibration anchor.
**Depends on.** Legacy gate; `nh_baseline_engine.py` (uncreated).
**Source.** Master §22 (L1759–1817); DD §3K (L178–185).
**Open.** Build- order gate (AFTER the search pipeline is stable and the queue has been healthy ≥1 month); six creation prerequisites; the one honest limitation — it validates internal consistency, not health; appointment anchors not optional; advisory only.


## AA. Mobile App — Three-Mode Companion (§23)

### AA1 — Mobile three-mode companion  ·  [DESIGNED — NOT BUILT]
**Concept.** A phone companion in three modes. Nothing connects to the real N.H automatically, ever.
**Base design.** Mode 1 Full (deliberate fingerprint/Face-ID/PIN tunnel that Ness opens and closes; not passive); Modes 2/3 an independent local AI (online learns; offline runs on what it knows) with its own memory; Manual Sync sends local memory to the desktop through the same SIMULATION review gate, no shortcuts.
**Depends on.** `nh_auth.py`, legacy gate.
**Source.** Master §23 (L1821–1858); DD §3L (L187–193).
**Open.** Security requirements non-negotiable (auth-gated tunnel; no raw OS command execution; remove `nh_pc_agent.py` `run:`; encryption at rest; SIMULATION-first); open: on-device model choice, local memory format, iOS/ Android background feasibility, Full-Mode tunnel wiring, Manual-Sync content scope.


## AB. Connection Capability (§24)

### AB1 — Connection capability (lasting connections + pending proposals)  ·  [DESIGNED — NOT BUILT]
**Concept.** Connects pieces that belong to the same situation without merging originals. From Ness's side, one ability; the split is internal.
**Base design.** Part one = a lasting connection record (type, decision status, certainty kept separate from decision, confirmer, evidence, correction history); part two = Context Retrieval (gathers, creates no lasting connection); a waiting area holds pending proposals (accepted/ rejected/undecided); connections may come only from three approved bases (direct recorded relationship; Ness's confirmation; a narrow authorized rule); certainty controls use; a one-way rule.
**Depends on.** Context Retrieval, §7G.
**Source.** Master §24 (L1862–1896); DD §3J (L174–176).
**Open.** ACCEPTED ≠ CERTAIN; pending connections may guide investigation silently but never support a claim/judgment/recommendation/action; five source types kept separate.


## AC. Concept-only / not-designed areas (named in the authority)

### AC1 — Wonder/Simulation mechanism  ·  [PARTLY DESIGNED]
**Concept.** Concept in §7B (the create-space, wonders kept and shown); mechanism not designed.
**Source.** (Master §7B; DD §5 L271.)

### AC2 — World model beside the self model  ·  [OPEN / UNRESOLVED]
**Concept.** Named in the Living State Web domain list; not designed.
**Source.** (Master §7D L608; DD §5 L272.)

### AC3 — End-to-end cycle  ·  [OPEN / UNRESOLVED]
**Concept.** The complete connected flow from new input through all components to Computed View/chat is identified but not designed as one sequence.
**Source.** (DD §4 L252, §5 L273.)


## AD. Intentionally absent / historical (named in the authority)

### AD1 — `cleaned_history (1).txt` ingest  ·  [INTENTIONALLY LEFT OUT]
**Concept.** Deliberately not ingested (damaged).
**Source.** (Master §5 L311.)

### AD2 — `gpt_purified` ingest  ·  [INTENTIONALLY LEFT OUT]
**Concept.** Skipped (0 unique, redundant/scrambled).
**Source.** (Master §5 L311.)

### AD3 — Hetzner sovereignty sync  ·  [HISTORICAL / INACTIVE]
**Concept.** Explicitly superseded by Ness (June 25); no longer an active task.
**Source.** (Master §11 L1458, §25 L1906.)

### AD4 — `nh_peek.py`  ·  [HISTORICAL / INACTIVE]
**Concept.** Throwaway viewer, not on disk (superseded by `nh_log.py`); harmless phantom.
**Source.** (Master §6 context.)


## NEW. June-28 candidate laws (feature-accepted, files not adopted)

### F1 — Two-level sensitive-content protection  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** protect different sensitive material at the right strength — Level 1 (live secrets/credentials) vs Level 2 (private personal info).
**Base design.** Level 1 is sealed, never displayed/quoted/exported/summarized in raw form under any circumstance including to Ness; Level 2 is protected from unauthorized access but available to Ness by default after identity verification.
**Depends on.** §0B handling records; §7Q operations; identity verification/SACL/BAI (claimed unchanged).
**Source.** `v8 §0A L201–225`, `§0B L272–282`, `§7Q tiers L1163–1185`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F2 — Sealed execution boundary  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** let authorized functions use Level-1 raw content without exposing it.
**Base design.** raw Level-1 content is processed only inside a protected boundary; only the "minimum safe result" may leave; the result must not reconstruct/reveal/allow-inference of the raw content; every entry is logged via the opaque ID.
**Depends on.** F1, F3, F4.
**Source.** `v8 §0A L213`, `§0B L274`, `§7Q Layer A L1177–1185`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F3 — Opaque protected-record identifiers  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** let ordinary records reference sealed items without leaking where/how they are stored.
**Base design.** ordinary records carry only an opaque ID + the full handling/use log; they never carry the raw content, physical location, encryption details, or access path.
**Depends on.** F1, F2, F4.
**Source.** `v8 §0A L205–215`, `§0B L278`, `§7Q L1122–1130`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F4 — Full-Transparency and Living-Record Law (§0B)  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** permanently record and connect everything N.H does, as active memory.
**Base design.** universal recording of all external info and all internal cognition/operations; each record carries 10 specified fields; records are living memory subject to retrieval/connection/reread (not passive audit); invisibility-in-chat is not an exception to recording; mandatory connections.
**Depends on.** every component; the meaning engine; §7Q.
**Source.** `v8 §0B L226–287`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F5 — Mandatory use and non-use records  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** record how every record is used, including when it is deliberately not used.
**Base design.** every retrieval/read/pass-to-mouth/accept/reject/ignore/connect/ examine is a recorded use event with stated fields; a candidate evaluated and set aside is a recorded **non-use** with its reason.
**Depends on.** F4.
**Source.** `v8 §0B L260`; enforced in `DD §0 L33` and `Cursor §1A L79–103`. *Open:* see conflict K6 (self-reference) and K8 (double-influence).
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F6 — Triggered recursive self-examination  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** let N.H examine its own logs/decisions/ understandings and use the results, without continuous auto-recursion.
**Base design.** examination is triggered (relevance signal, system purpose, design rule, detected inconsistency, Ness's question, or authorized trigger), runs as deep as the trigger requires with no fixed maximum, and is itself recorded; "no uncontrolled automatic recursion in the absence of a trigger."
**Depends on.** F4.
**Source.** `v8 §0B L254–258`. *Open:* see conflict K7.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F7 — Six privacy operations  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** a distinct, non-interchangeable operation set for §7Q.
**Base design.** Exclusion, **Sealed isolation (new)**, Hiding, Restriction, Redaction, Deletion — each defined, each preserving internal usability "unless a separate influence-removal instruction applies."
**Depends on.** F1, F8, F9.
**Source.** `v8 §7Q L1120–1136`
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F8 — Non-destructive deletion  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** redefine "deletion" as visibility removal, never erasure.
**Base design.** deletion removes material from ordinary visible output/paths only; content is preserved, connected, internally usable; cryptographic erasure of the only copy is prohibited; outcome states `protected_complete` / `protected_with_declared_limits` / `incomplete` / `blocked` / `failed`; a positive **history record** (not a tombstone) is kept; the prior "make inaccessible to all internal functions" rule is marked REJECTED.
**Depends on.** F4, F9.
**Source.** `v8 §7Q L1138–1162`, `§0A L223–225`, `§0B L284–286`
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F9 — Separate influence-removal instruction  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** separate "hide from view" from "stop influencing N.H."
**Base design.** stopping a record's internal influence (readings/retrieval/connections/ reasoning) requires an explicit separate instruction stating scope, affected components, and start time; it does not follow automatically from deletion or hiding, and is recorded separately.
**Depends on.** F8, F4.
**Source.** `v8 §7Q L1146–1148`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F10 — Defaults (v2.3) enforcement rules  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** propagate F4/F7/F8 into the behavioral guide.
**Base design.** §0 override requiring per-component operational recordkeeping (silent operations prohibited); §3 §7Q entry restated to six operations / two levels / non-destructive deletion / five outcome states; §6 new "EVERYTHING IS RECORDED" principle + deletion principle flipped + pure-tape principle updated.
**Depends on.** F4–F9.
**Source.** `v2.3 L33, L137, L309, L313, L317`.
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated

### F11 — Cursor (v3.3) enforcement rules  ·  [CANDIDATE — NOT ADOPTED]
**Concept.** propagate F4/F8 into the coding rules.
**Base design.** §1A rule making any internal operation without a mandatory append-only linked record a "prohibited function" (enumerated operations + required fields); §1A rule forbidding code that permanently destroys or cryptographically erases the only copy of any content (deletion = non-destructive visibility removal).
**Depends on.** F4, F8.
**Source.** `v3.3 §1A L79–103` (transparency), `L105–108` (no-destruction)
**Status detail.** CANDIDATE — feature-acceptance evidence found (prior session), files not adopted, not integrated


---

## CLOSING — HOW THIS FILE PROTECTS THE DESIGN

- **No-loss.** Every feature ever designed or wanted has an entry here, including the ones intentionally
  left out and the historical ones — kept as decisions and history, not deleted.
- **No silent change.** Status is honest per entry. Nothing is shown as built when it is only designed, or
  adopted when it is only a candidate.
- **Defense check.** If any other file (or any tool) ever drops, weakens, or rewrites a feature, compare it
  against this entry. A difference here is the alarm.
- **Selection is elsewhere.** What is *current* is decided by you in the chooser, one card at a time. This
  file does not pre-decide that.

### The three-file plan (this is file 1)
This is **File 1 — the design-preservation basis** (concept + base design of every feature). The other two
files are yours to define when ready; a natural split is **File 2 — your current/not-current selection**
(the chooser's export: which of these are live) and **File 3 — the build state** (what is actually on disk
vs designed vs to-build). File 1 protects the design; File 2 records what you keep; File 3 tracks building
it. Nothing here commits you to that split — say the word and we shape 2 and 3 together.

*Generated 2026-06-28 from the recovered feature inventory. Derived reference —
not authority, not adopted, changes nothing. Current authority remains v7_1 / v2.2 / v3.2 / governance companion.*