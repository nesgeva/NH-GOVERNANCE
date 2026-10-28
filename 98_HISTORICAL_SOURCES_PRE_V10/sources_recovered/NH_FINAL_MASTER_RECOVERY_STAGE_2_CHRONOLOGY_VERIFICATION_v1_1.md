# N.H — FINAL-MASTER RECOVERY — STAGE 2: CHRONOLOGY VERIFICATION v1.1

**This is the corrected successor to Stage 2 v1.** Stage 2 v1 is preserved unchanged, and all completed
chronology research is preserved. v1.1 applies only the planning/citation corrections listed in the
Correction Ledger (§11): the MASTER-19 v1/v3/v6/FULL cluster is no longer shown as a proven sequence; a
full SRC-001–092 source-accounting appendix is added; every citation is made unambiguous; the hardware
decision is moved out of the chronology evidence table into Stage 3; and the TSC wording is corrected.
No chronology finding was reversed and no architecture was touched.

**What this file is.** The chronology-verification pass required by Stage 1 v1.3 §9.1 step 2. It reads
the relevant full source bodies across Reader Parts 01–11 and establishes the *actual* relationships
among the Master files, Decision-Defaults files, off-spine Masters, addenda, deltas, handoffs,
provenance manifests, and the accepted companion designs — from **internal evidence only**.

**What this file is NOT.** No feature recovery, no judging which design is better, no architecture
conflict resolution, no integration, no patching of any authority file, no choice of the final
Master's organization, no canonical drafting. Where evidence does not prove a relationship, it is left
`UNCLEAR` or `CONFLICTING` and carried forward — never decided.

**Evidence rule applied (Stage 1 v1.3 §0A/§0B).** Filenames, numeric version tokens, copy suffixes,
sizes, upload order, and the labels `FINAL`/`FULL`/`CORRECTED`/`AUDITED` are **not** treated as proof.
Each verified relationship rests on an internal date, a session declaration, an explicit
predecessor/successor or supersede/regenerate statement, an embedded change log, a content
relationship, or a provenance record. The acceptance-and-revision rule is applied to the companions:
accepted designs stay accepted; recency alone never proves supersession; unclear apparent revisions
keep both versions and stay `UNCLEAR`/`CONFLICTING`.

**Preservation rule.** Every source is preserved. Chronology here may change a source's *position* in
the later queue; it never removes a source from the later feature audit.

---

## 1. THE CHRONOLOGY KEY (the spine of dated evidence)

A single internal fact unlocks most of the lineage: every numbered Master body carries a dated
session preamble, and most Decision-Defaults bodies state which Master/session they were
"regenerated/updated to match." Cross-referencing these gives the session→artifact map below, which is
**evidence-derived, not filename-derived**:

| Session (dated) | Master artifact named *inside the bodies* | Decision-Defaults artifact |
|---|---|---|
| — (June 19 2026) | `MASTER_FILE_COMPLETE` family (standalone "COMPLETE") | — |
| S2–S3 (June 20 2026) | MASTER-5 → 6 → 6__1_ → 7 | bare DD family |
| S4 (June 20 2026) | MASTER-8 | — |
| S5 (June 21 2026) | MASTER-9 | — |
| S7 (June 21 2026) | MASTER-9.2 (over absent 9.1) | — |
| S8 (June 21 2026) | MASTER-9.4 (over absent 9.3); `section13_ADD` = §13 source | DD `__1_`/`_ADD` (S8 lesson) |
| S9 (June 22 2026) | MASTER-10 / 10__1_ | DD `__2_` (S9 settled) |
| S10 afternoon (June 22) | MASTER-11 | — |
| S10 evening (June 22) | MASTER-11.1 | DD-S10_1 ("to match MASTER-11.1") |
| S11 (June 22) | MASTER-12 (ABSENT) | — |
| S12 (June 22 late) | MASTER-13 | DD-S12 ("to match MASTER-13") |
| S13 (June 23) | MASTER-14 cluster (+ FINAL variants) | DD-S13 family ("to match MASTER-14") |
| S14 (June 23) | MASTER-15 (ABSENT); `DELTA_S14` records it | — |
| S16 (June 24) | MASTER-16 (ABSENT) | — |
| S17 (June 24) | MASTER-17 full draft (corrected v2) + 4 reader slices | DD-S17_AUDITED ("regenerated from MASTER-17…") |
| S18 (June 24) | MASTER-18 full draft; S18 content adopted into MASTER-19_v7 | — |
| S19 / adoption (June 26 → 28) | MASTER-19 cluster {v1, v3, v6, FULL} — internal order UNCLEAR; only `v6 → v7_1` verified; **v7_1 adopted June 28** | DD-S19_v1 (v6, June 26) → **DD-S19_v2_2 (v7_1, June 28)** |

The +1 offset (session N produces "MASTER-(N+1)") holds through S13 and is corroborated by the
Decision-Defaults "to match MASTER-N" stamps; the S17–S19 consolidation breaks the strict offset and
is verified directly from the bodies' own statements instead.

---

## 2. VERIFIED MASTER CHRONOLOGY

Classifications per source. Evidence citations are in §6.

### 2.1 Pre-spine standalone "COMPLETE" / context family (June 19 and earlier)
- **`NH_MASTER_CONTEXT.md` (SRC-054)** — earliest context body. **VERIFIED PREDECESSOR** to the COMPLETE
  family on the founding principle and the name (COMPLETE explicitly "supersedes earlier master
  context"). **CONFLICTING** on spelling (mandates "Nes"); conflict preserved, not resolved.
- **`NH_MASTER_FILE_COMPLETE.md` (SRC-055)** — written June 19 2026; "supersedes earlier master
  context." 156 lines.
- **`NH_MASTER_FILE_COMPLETE__1_.md` (SRC-056)** — written June 19 2026; "supersedes all earlier
  master/context files"; 257 lines, fuller. **VERIFIED SIBLING / PARALLEL** of SRC-055 (same date,
  fuller body); which of 055/056 came first within June 19 is **UNCLEAR**.
- **Relationship to the numbered spine:** the June-20 numbered Masters each declare they were "Rebuilt
  June 20 2026… from a full read of all project files." The June-19 COMPLETE family therefore sits
  **before** the numbered spine as part of the material the spine was rebuilt from. **VERIFIED** by date
  (June 19 < June 20) + the rebuild statement.

### 2.2 The numbered session spine (June 20–23)
- **MASTER-5 (SRC-046)** — June 20, session 2/3; companions still external. **VERIFIED** earliest
  numbered Master.
- **MASTER-6 (SRC-047) → MASTER-6__1_ (SRC-048)** — both session 3; 6__1_ additionally inlines
  `.cursorrules` v3.1 that 6 does not. **VERIFIED ADDENDUM/expansion** direction 6 → 6__1_ (same
  session, additive); strict ordinal otherwise **UNCLEAR**.
- **MASTER-7 (SRC-049)** — session 3; companions now fully inlined. **VERIFIED** successor to 6 family.
- **MASTER-8 (SRC-050)** — session 4; "this is MASTER-8," adds first running code. **VERIFIED
  PREDECESSOR → SUCCESSOR** (7 → 8).
- **MASTER-9 (SRC-051)** — session 5; "this is MASTER-9," four seeds / 11,374 records. **VERIFIED** (8 → 9).
- **MASTER-9.1 — SOURCE BODY ABSENT** (named by SRC-052 as its base).
- **MASTER-9_2 (SRC-052)** — session 7; "ADDITIVE update over MASTER-9.1." **VERIFIED ADDENDUM** over
  absent 9.1.
- **MASTER-9.3 — SOURCE BODY ABSENT** (session 8; named by SRC-053; `section13_ADD` is its §13 source).
- **MASTER-9_4 (SRC-053)** — session 8; "ADDITIVE update over MASTER-9.3," adds §14. **VERIFIED
  ADDENDUM** over absent 9.3.
- **MASTER-10 (SRC-022) / MASTER-10__1_ (SRC-023)** — session 9; "this is MASTER-10," reality rework.
  10__1_ carries one extra open-question item (g) absent from 10. **VERIFIED SIBLING / PARALLEL** (same
  session); 10 → 10__1_ additive direction likely, exact order **UNCLEAR**.
- **MASTER-11 (SRC-024)** — session 10 afternoon; "this is MASTER-11," reality→story re-soul.
  **VERIFIED PREDECESSOR → SUCCESSOR** (10 → 11).
- **MASTER-11_1 (SRC-025) = "MASTER-11.1"** — session 10 *evening*. **VERIFIED SUCCESSOR** to MASTER-11,
  established by DD-S10_1 stating it was updated "to match MASTER-11.1" with 2a structure closed and the
  DUMB-vs-SMART frame added (content absent from MASTER-11). 11 → 11.1.
- **MASTER-12 — SOURCE BODY ABSENT** (session 11; implied by MASTER-13's "updated sessions 4–11").
- **MASTER-13 (SRC-026)** — session 12; "this is MASTER-13," large build (5,521 roots). **VERIFIED
  PREDECESSOR → SUCCESSOR** (11.1 → [12 absent] → 13).
- **MASTER-14 cluster** — `MASTER-14` (SRC-027), `__1_` (SRC-031), `__2_` (SRC-032), `__3_` (SRC-033),
  `__4_` (SRC-034), `MASTER-14_FINAL` (SRC-028), `_FINAL__2_` (SRC-029), `_FINAL__4_` (SRC-030): **all
  declare session 13 → "this is MASTER-14."** **VERIFIED SIBLING / PARALLEL BRANCH** (one session, one
  Master number, eight bodies). A **content-relationship correction direction is VERIFIED**: SRC-027
  overstates "2a — the reading record BUILT," while the `_FINAL`/`__N_` bodies correct this to "2a
  PLUMBING built; the 8-field reading record NOT coded," and DD-S13 independently records that the
  "2a built" overstatement was caught and corrected. So the corrected ("plumbing-only") bodies hold the
  settled S13 state. The **exact ordinal order among the eight is UNCLEAR** (same session/date; no
  per-body timestamps).
- **MASTER-15 — SOURCE BODY ABSENT** (session 14; `DELTA_S14` records S14 and is "derived from
  MASTER-14_FINAL").
- **MASTER-16 / MASTER-16_FINAL_CORRECTED — SOURCE BODY ABSENT** (session 16; named by the 17/18/19
  preambles: Engine B, gold v2-B, Chroma rebuild).

### 2.3 The S17–S19 consolidation lineage (June 24–28)
All of these carry the identical S14/S16 + "S17 DOCUMENT-CORRECTION PASS (June 24 2026)" preamble,
confirming one consolidation family:
- **MASTER-17_FULL_DRAFT_CORRECTED_v2 (SRC-039)** — the S17 full draft. **VERIFIED PARENT** of the four
  reader slices (manifest: "Source of the four reader slices"; slices carry "DERIVED READER COPY").
- **MASTER-17 reader slices** — `…00_INDEX_STATUS` (SRC-035), `…01_FOUNDATION_BUILT` (SRC-036),
  `…02_CONCEPTUAL_ARCHITECTURE` (SRC-037), `…03_ROADMAP_INTERFACE_HISTORY` (SRC-038): **PARTIAL OR
  SPLIT REPRESENTATION** of SRC-039 (VERIFIED). Not independent Masters.
- **MASTER-18_FULL_DRAFT_v1 (SRC-040)** — the S18 candidate full draft (manifest first-heading
  "MASTER-18 … full S18 candidate"). **VERIFIED** member of the consolidation lineage, after the S17
  draft.
- **The MASTER-19 comparison cluster — {`v1` (SRC-041), `v3` (SRC-042), `v6` (SRC-043),
  `FULL` (SRC-045)}** — all four share the S14/S16/S17 consolidation preamble, and **none carries an
  internal statement ordering it against the others.** They are therefore treated as **one internal
  MASTER-19 comparison cluster with UNCLEAR internal order** (version tokens and the word "FULL" are not
  proof — §0A). No `v1 → v3 → v6` sequence is asserted. Their internal order is a body-comparison
  question for the feature audit.
  - The **only explicitly verified terminal relationship** out of this cluster is **`v6 → v7_1`**:
    stated by v7_1's own body ("It supersedes NH_MASTER-19_CORRECTED_v6.md"), by the AFTER_BGMM handoff,
    and by every manifest ("MASTER-19 v6 — declared predecessor of v7_1"). This identifies v6 as the
    body directly preceding v7_1; it does **not** rank v1, v3, or FULL relative to v6.
  - `MASTER-19_FULL` (SRC-045) shares the v6/v7 title and intro ("MASTER-19: Full Backup with All
    Additions"; "complete S17 and S18 conceptual design AND all S19 restorations") and carries no
    adoption/supersession line; it sits inside the cluster, ordinal UNCLEAR.
- **MASTER-19_CORRECTED_v7_1 (SRC-044)** — **CONFIRMED CURRENT / VERIFIED SUCCESSOR.** Its own body:
  Session 18 conceptual design integrated; "the adopted authoritative N.H Master, explicitly adopted by
  Ness (June 28 2026); it supersedes NH_MASTER-19_CORRECTED_v6.md." This is the cluster's verified exit
  to the current authority.

### 2.4 Verified Master order (proven links only; absent nodes shown; unproven links marked)
```
[MASTER_CONTEXT] ⇒ MASTER_FILE_COMPLETE ≈ __1_   (June 19; CONTEXT superseded on name+principle)
        │  (June-19 standalone bodies; read into the June-20 rebuild)
        ▼
MASTER-5 → 6 → 6__1_ → 7 → 8(S4) → 9(S5) → [9.1∅] → 9.2(S7) → [9.3∅] → 9.4(S8)
        → 10/10__1_(S9) → 11(S10a) → 11.1(S10e) → [12∅,S11] → 13(S12)
        → {MASTER-14 cluster}(S13)  → [15∅,S14] → [16∅,S16]
        → MASTER-17_full(S17) ⇒ {4 reader slices}
        → MASTER-18_full(S18)
        → [ MASTER-19 cluster: {v1, v3, v6, FULL} — internal order UNCLEAR ]
                                   └─ verified: v6 → **v7_1 (adopted June 28)**
```
`→` VERIFIED predecessor→successor · `∅` SOURCE BODY ABSENT · `··` UNCLEAR link · `⇒` parent→split/derived ·
`[ … ]` comparison cluster with no proven internal order.

---

## 3. VERIFIED DECISION-DEFAULTS CHRONOLOGY

Most links are VERIFIED from each file's own "updated/regenerated to match MASTER-X" or
"Supersedes …" line.

- **bare `NH_DECISION_DEFAULTS.md` (SRC-016)** — earliest DD body; generic, no session stamp.
  **UNCLEAR** exact position within the early cluster.
- **`__1_` (SRC-018)** — carries the session-8 lesson. ~S8. **UNCLEAR** order vs bare.
- **`_ADD` (SRC-017)** — session-8 lesson add-on. **VERIFIED ADDENDUM** (S8 fragment).
- **`__2_` (SRC-019)** — carries "SETTLED as design (session 9)" items → **VERIFIED** later than the S8
  bodies (S9).
- **DD-S10_1 (SRC-007)** — "Updated session 10-evening (June 22 2026) to match MASTER-11.1."
  **VERIFIED**: ↔ MASTER-11.1; successor to the early cluster. (Also present as zip member
  `S10.1` — **EXACT DUPLICATE**.)
- **DD-S12 (SRC-008)** — "Updated session 12 (June 22 late) to match MASTER-13." **VERIFIED** (↔ MASTER-13).
- **DD-S13 (SRC-009)** — "Regenerated session 13 (June 23) to match MASTER-14." **VERIFIED** (↔ MASTER-14).
- **DD-S13 `__1_` (SRC-010), `__3_` (SRC-011), `__4_` (SRC-012)** — session-13 DD variants. **VERIFIED
  SIBLING / PARALLEL** (S13); **ordinal UNCLEAR**. (`__2_` = EXACT DUPLICATE of `__1_`; `__6_` = EXACT
  DUPLICATE of `__4_`.)
- **DD-S17_AUDITED_v1 (SRC-013)** — "Regenerated from `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` on June
  24 2026." **VERIFIED ADDENDUM/DERIVATIVE** of MASTER-17. **CONFLICTING** internal label (filename
  "AUDITED_v1" vs body titled "S17 — DRAFT"); preserved. (No DD body for S14/S16 — a verified gap, not
  a deletion.)
- **DD-S17_DRAFT / DD-S19_v2_1 — SOURCE BODY ABSENT.**
- **DD-S19_v1 (SRC-014)** — "Synced to `NH_MASTER-19_CORRECTED_v6.md` (adopted June 26 2026)";
  "Supersedes `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md`"; declared CANDIDATE. **VERIFIED PREDECESSOR →
  SUCCESSOR** over S17; tied to MASTER-19_v6.
- **DD-S19_v2_2 (SRC-015)** — **CONFIRMED CURRENT.** "Synced to `NH_MASTER-19_CORRECTED_v7_1.md`
  (adopted June 28 2026)"; "Supersedes `NH_DECISION_DEFAULTS-S19_v2_1.md` and all prior Decision
  Defaults versions"; AUTHORITATIVE. **VERIFIED** terminal node, tied to MASTER-19_v7_1.

**Verified DD order:**
```
[CONTEXT-era] → bare/__1_/_ADD(S8)··→ __2_(S9) → S10_1(S10e↔M11.1) → S12(↔M13) → S13 family(↔M14)
   → S17_AUDITED(↔M17, June 24) → [S17_DRAFT∅] → S19_v1(↔v6, June 26) → [v2_1∅] → **S19_v2_2(↔v7_1, June 28)**
```

---

## 4. PLACEMENT MAP — off-spine Masters, addenda, deltas, handoffs, manifests, companions

| Source | SRC | Classification | Placement (evidence-based) |
|---|---|---|---|
| `NH_MASTER_CONTEXT.md` | SRC-054 | VERIFIED PREDECESSOR + CONFLICTING | Earliest context; superseded on name/principle by COMPLETE (June 19); "Nes" spelling conflict preserved |
| `NH_MASTER_FILE_COMPLETE.md` / `__1_` | SRC-055 / 056 | VERIFIED SIBLING/PARALLEL | June 19 standalone "COMPLETE" masters; pre-spine; 056 fuller; 055↔056 order UNCLEAR |
| `NH_MASTER-19_FULL.md` | SRC-045 | UNCLEAR (member of the MASTER-19 comparison cluster) | Same title/intro as v6/v7; contains S17+S18+S19; no internal ordering statement — sits in the {v1, v3, v6, FULL} cluster, internal order UNCLEAR; place by body comparison |
| `NH_MASTER-17_*` (4 slices) | SRC-035–038 | PARTIAL OR SPLIT REPRESENTATION | Derived reader slices of MASTER-17_full (SRC-039); VERIFIED via manifest + "DERIVED READER COPY" |
| `NH_MASTER_section13_ADD.md` | SRC-057 | VERIFIED ADDENDUM | June 21 / session 8; explicit "ADD TO MASTER AS §13" (the Live Loop) → folded into the spine at MASTER-9.3/9.4 |
| `NH_DELTA_S14.md` | SRC-020 | VERIFIED ADDENDUM / DELTA | Session 14 (June 23); "derived from MASTER-14_FINAL"; records S14 decisions toward absent MASTER-15 |
| `NH_DECISION_DEFAULTS_ADD.md` | SRC-017 | VERIFIED ADDENDUM | Session-8 DD add-on fragment |
| `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | SRC-004 | Handoff (provenance) | Security/identity/BGMM branch; v6-era; "none patched into the Master" |
| `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | SRC-061 | Handoff (provenance) | "Created June 28 2026"; pre-consolidation shared handoff |
| `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | SRC-060 | Continuity note (provenance) | Post-MASTER-17 (~June 24); explicitly not an authority |
| Manifests v1→v5 | SRC-088–092 | VERIFIED PREDECESSOR → SUCCESSOR chain | v2 supersedes v1; v3 supersedes v1–2; v4 supersedes v1–3; v5 supersedes v1–4 (carried forward from v4). v5 latest. Provenance-only |
| `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | SRC-001 | ACCEPTED (companion) | v6/S19_v1-era (~June 26); references MASTER-19_v6 as patch target; holds the **earlier** accepted TSC foundation; accepted, not yet patched |
| `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | SRC-002 | ACCEPTED (companion) + VERIFIED LATER FULLER ACCEPTED SPECIFICATION / EXPANSION | The **later, full 31-section** TSC spec; references MASTER-19_v6; DD-S19_v2_2 points to it as the authoritative TSC spec. AFTER_BGMM = earlier foundation → TSC_v1 = **later, fuller accepted specification / expansion** of it. **Both accepted, both preserved.** No cited Ness decision states the foundation is replaced or superseded, so this is an expansion, not a supersession (acceptance-and-revision rule) |

---

## 5. EVIDENCE TABLE (exact source records and passages)

**Citation convention (read this first).**
- **Reader Part** is the part file the source body lives in, per the index map: Part 01 = SRC-001–012;
  Part 02 = SRC-013–027; Part 03 = SRC-028–038; Part 04 = SRC-039–040; Part 05 = SRC-041–042;
  Part 06 = SRC-043–044; Part 07 = SRC-045–051; Part 08 = SRC-052–069; Part 09 = SRC-070–086;
  Part 10 = SRC-087; Part 11 = SRC-088–092.
- **Line numbers are SOURCE-BODY-RELATIVE** — i.e., relative to each source file's *own* line 1 (the
  verbatim content as embedded), **not** Reader-Part-relative line offsets. `hdr` = the preservation
  block's metadata header (not part of the source body); `rows` = table rows inside a manifest body
  (also source-body-relative).
- Each row gives: Reader Part · SRC ID · exact line/range · short description of the supporting
  statement. Quotes are short; most are paraphrased.

| # | Relationship established | Reader Part · SRC · line(s) | Supporting statement |
|---|---|---|---|
| E1 | v7_1 supersedes v6; adopted June 28; integrates S18 | Part 06 · SRC-044 · L8 | body: "adopted authoritative… adopted by Ness (June 28 2026)… supersedes NH_MASTER-19_CORRECTED_v6.md" |
| E2 | v6 is the declared predecessor of v7_1 | Part 06 · SRC-043 · hdr; Part 11 · SRC-088–092 · rows | manifests: "MASTER-19 v6 — declared predecessor of v7_1" |
| E3 | DD-S19_v2_2 is current; supersedes all prior; tied to v7_1 (June 28) | Part 02 · SRC-015 · L3,L5,L8 | "Synced to …v7_1 (June 28 2026)"; "Supersedes …S19_v2_1.md and all prior Decision Defaults versions" |
| E4 | DD-S19_v1 supersedes S17; tied to v6 (June 26); candidate | Part 02 · SRC-014 · L3,L5,L7 | "Synced to …v6 (adopted June 26 2026)"; "Supersedes …S17_AUDITED_v1.md"; "CANDIDATE" |
| E5 | DD-S17 regenerated from MASTER-17_full on June 24 (derived) | Part 02 · SRC-013 · L4 | "Regenerated from NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md on June 24 2026… Derived FROM the Master" |
| E6 | MASTER-17_full is the source of the 4 reader slices | Part 11 · SRC-088 · L82 (+ SRC-090/091/092 · rows); Part 03 · SRC-035–038 · hdr | manifest: "Source of the four reader slices"; slice status "DERIVED READER COPY" |
| E7 | MASTER-14 cluster all = session 13; "2a built" overclaim corrected | Part 02 · SRC-027 · L4  vs  Part 03 · SRC-028/029/030/031–034 · L4; Part 01 · SRC-009 · L3 | SRC-027: "BUILT 2a — the reading record"; FINAL/__N_ bodies: "BUILT the 2a PLUMBING… NOT the full reading record"; DD-S13: "an overstatement, '2a built,' propagated to ten places before it was caught" |
| E8 | MASTER-13 = session 12 (large build) | Part 02 · SRC-026 · L4 | "Session 12 (June 22 2026, late)… this is MASTER-13" |
| E9 | MASTER-11.1 = session 10 evening, after MASTER-11 | Part 01 · SRC-007 · L3 | DD-S10_1: "Updated session 10-evening (June 22 2026) to match MASTER-11.1: 2a's STRUCTURE is now CLOSED… DUMB-vs-SMART machinery frame added" |
| E10 | MASTER-11 = session 10; reality→story re-soul | Part 02 · SRC-024 · L3,L7 | "session 10 (June 22 2026, afternoon)… this is MASTER-11"; "'reality-layer' is REPLACED by 'per-person STORY-layer'" |
| E11 | MASTER-10 = session 9; reality rework | Part 02 · SRC-022 · L3 | "session 9 (June 22 2026, past midnight)… this is MASTER-10" |
| E12 | MASTER-9.4 additive over absent 9.3 (S8); adds §14 | Part 08 · SRC-053 · L3 | "session 8… this is MASTER-9.4… ADDITIVE update over MASTER-9.3… 9.4 adds §14" |
| E13 | MASTER-9.2 additive over absent 9.1 (S7) | Part 08 · SRC-052 · L3 | "session 7… this is MASTER-9.2… ADDITIVE update over MASTER-9.1" |
| E14 | MASTER-9/8 = S5/S4 | Part 07 · SRC-051 · L3; Part 07 · SRC-050 · L3 | "session 5… this is MASTER-9"; "session 4… this is MASTER-8" |
| E15 | 6 → 6__1_ additive (6__1_ adds cursorrules v3.1) | Part 07 · SRC-047 · L3; Part 07 · SRC-048 · L3 | 6: embeds UF+ME; 6__1_: embeds UF+ME "AND the full in-force code ruleset (.cursorrules v3.1)" |
| E16 | COMPLETE family = June 19; supersedes earlier context | Part 08 · SRC-055 · L2; Part 08 · SRC-056 · L2 | "Written June 19 2026… Supersedes earlier master context… on the name" |
| E17 | section13_ADD = session 8 §13 (Live Loop) source | Part 08 · SRC-057 · L1,L4 | "ADD TO MASTER AS §13"; "June 21 2026 — session 8… DESIGNED the live loop (§13)" |
| E18 | DELTA_S14 = session 14, derived from MASTER-14_FINAL | Part 02 · SRC-020 · L2,L4 | "Session 14 (June 23 2026)"; "Derived from NH_MASTER-14_FINAL.md" |
| E19 | Manifest chain v1→v5 each supersedes prior; v5 latest | Part 11 · SRC-089 · L5; SRC-090 · L5; SRC-091 · L5; SRC-092 · L5 | v3: "Supersedes v1… and v2…"; v5: "Supersedes v1…v4… carried forward from v4 unchanged" |
| E20 | TSC_v1 = later, fuller accepted specification / expansion of the AFTER_BGMM TSC foundation; both accepted; no cited Ness decision states replacement/supersession | Part 01 · SRC-002 · L5,L20; Part 01 · SRC-001 · L11; Part 02 · SRC-015 · L218 | TSC_v1: "complete accepted 31-section… AFTER_BGMM preserves the earlier accepted TSC foundation"; AFTER_BGMM: patch target "MASTER-19_CORRECTED_v6"; DD-S19_v2_2: the TSC design is "the authoritative specification" — none of these states the foundation is replaced |
| E22 | DD-S12/S13 tied to MASTER-13/14 | Part 02 · SRC-008 · L3; Part 01 · SRC-009 · L3 | "Updated session 12… to match MASTER-13"; "Regenerated session 13… to match MASTER-14" |

*(The hardware decision row from Stage 2 v1 (E21, RTX 3090 vs the S16 RTX 5060 Ti plan) has been removed
from this chronology evidence table. It is a feature/decision matter, preserved for the Stage 3 feature
audit, not chronology evidence. E-numbering is otherwise kept stable; E21 is intentionally vacant.)*

---

## 6. CORRECTED COMPARISON QUEUE (for the later feature-recovery audit)

Reordered to follow the **verified** chronology. **Every source remains in the queue**; UNCLEAR
clusters stay in place and are compared internally during the audit (position may still change, never
inclusion). EXACT DUPLICATE pairs are skipped (no content delta).

### 6.1 Master queue (verified order)
1. `MASTER_CONTEXT` (SRC-054) → `MASTER_FILE_COMPLETE` (SRC-055) ↔ `__1_` (SRC-056) *(June-19 standalone; 055↔056 internal compare)*
2. → `MASTER-5` (SRC-046)
3. → `MASTER-6` (SRC-047) → `MASTER-6__1_` (SRC-048)
4. → `MASTER-7` (SRC-049)
5. → `MASTER-8` (SRC-050, S4)
6. → `MASTER-9` (SRC-051, S5)  *(gap: 9.1 ABSENT)*
7. → `MASTER-9_2` (SRC-052, S7)  *(gap: 9.3 ABSENT)*
8. → `MASTER-9_4` (SRC-053, S8)  *(compare against `section13_ADD` SRC-057 for §13)*
9. → `MASTER-10` (SRC-022) ↔ `MASTER-10__1_` (SRC-023) *(S9; internal compare)*
10. → `MASTER-11` (SRC-024, S10a) → `MASTER-11_1` (SRC-025, S10e)
11. → `MASTER-13` (SRC-026, S12)  *(gap: 12 ABSENT, S11)*
12. → **MASTER-14 cluster (S13)** — internal compare set, corrected-state bodies are the S13 reference:
    `MASTER-14` (SRC-027, overclaim) vs `_FINAL` (SRC-028), `_FINAL__2_` (SRC-029), `_FINAL__4_`
    (SRC-030), `__1_` (SRC-031), `__2_` (SRC-032), `__3_` (SRC-033), `__4_` (SRC-034)  *(gaps: 15, 16 ABSENT)*
13. → `MASTER-17_FULL_DRAFT_CORRECTED_v2` (SRC-039, S17) ⇒ compare its 4 reader slices (SRC-035–038) only for split-coverage, not as independent Masters
14. → `MASTER-18_FULL_DRAFT_v1` (SRC-040, S18)
15. → **MASTER-19 comparison cluster {v1, v3, v6, FULL}** (SRC-041, SRC-042, SRC-043, SRC-045) —
    one internal compare set; **internal order UNCLEAR, no `v1→v3→v6` asserted.** The single verified
    link out of the cluster is `v6 → v7_1`.
16. → **`MASTER-19_CORRECTED_v7_1` (SRC-044) — terminal / CONFIRMED CURRENT** (verified successor of v6)

### 6.2 Decision-Defaults queue (verified order)
1. bare `DD` (SRC-016) ·· `__1_` (SRC-018) *(order UNCLEAR)* + `_ADD` (SRC-017, addendum)
2. → `__2_` (SRC-019, S9)
3. → `DD-S10_1` (SRC-007, S10e)
4. → `DD-S12` (SRC-008, S12)
5. → **DD-S13 set (S13)**: `S13` (SRC-009) ↔ `__1_` (SRC-010) ↔ `__3_` (SRC-011) ↔ `__4_` (SRC-012) *(internal order UNCLEAR; `__2_`,`__6_` are EXACT DUPLICATEs — skipped)*
6. → `DD-S17_AUDITED_v1` (SRC-013, S17)  *(gap: S17_DRAFT ABSENT)*
7. → `DD-S19_v1` (SRC-014, v6/June 26)  *(gap: S19_v2_1 ABSENT)*
8. → **`DD-S19_v2_2` (SRC-015) — terminal / CONFIRMED CURRENT**

### 6.3 Companion / spec integration passes (after the spine walks)
- A. `AFTER_BGMM` (SRC-001) and `TSC_v1` (SRC-002) ↔ v7_1 — feature-by-feature, applying the
  acceptance-and-revision rule; TSC_v1 = the later, fuller accepted TSC specification / expansion,
  AFTER_BGMM = the earlier accepted TSC foundation; **both accepted, both preserved** (no cited Ness
  decision states replacement). (No patching in the audit.)
- B. Design specs (Universal Filter ×3 + RULES, Meaning Engine B5, Mobile, Canvas, chat-frontdoor,
  wellbeing baseline, research architecture, search-pipeline security) ↔ their Master sections — for
  full mechanisms the Master may only summarize.

---

## 7. UNRESOLVED-CHRONOLOGY REGISTER

Carried into the feature audit; none decided here.

**A. UNCLEAR internal order (same session/date; settle by body comparison):**
1. `MASTER-19` comparison cluster {`v1`, `v3`, `v6`, `FULL`} — internal order among the four
   (only `v6 → v7_1` is proven; no `v1→v3→v6` sequence).
2. `MASTER-19_FULL` (SRC-045) ordinal position inside that cluster.
3. `MASTER-14` cluster — exact order of the eight S13 bodies (correction *direction* known; ordinal not).
4. `MASTER-10` vs `MASTER-10__1_` (S9); `MASTER-6` vs `6__1_` (S3) — additive direction inferred, exact order not proven.
5. `MASTER_FILE_COMPLETE` vs `__1_` (both June 19).
6. DD bare vs `__1_` (both ~S8); DD-S13 `__1_`/`__3_`/`__4_` ordinal.

**B. CONFLICTING (both preserved):**
7. Name spelling — `MASTER_CONTEXT` mandates "Nes"; later bodies/authority use "Ness."
8. `DD-S17_AUDITED_v1` — filename "AUDITED_v1" vs internal title "S17 — DRAFT."

**C. SOURCE BODY ABSENT (named in evidence, not supplied — not rejected, §0A Rule 2):**
9. Masters: `MASTER-9.1`, `MASTER-9.3`, `MASTER-12`, `MASTER-15`, `MASTER-16`,
   `MASTER-16_FINAL_CORRECTED`, `MASTER-17_DRAFT`, plus the v1.3-noted `MASTER-19_v2/v4/v5/v7`.
10. Decision Defaults: `DD-S17_DRAFT`, `DD-S19_v2_1`.
11. Candidates: `MASTER-19_CORRECTED_v8`, `DD-S19_v2_3`, `cursorrules_v3_3`.

**D. SOURCE BODY UNRECOVERABLE:**
12. Batch-1 body of `NH_Meaning_Engine_Design.md` (historical SHA `18185908…`) — bytes gone; the B5
    body (SRC-058) is preserved separately and was not substituted.

---

## 8. STATE AFTER STAGE 2 (nothing decided, nothing changed)
- Authority unchanged: v7_1 / DD-S19_v2_2 / Cursor Rules v3.2 / governance companion v1.
- No feature compared, no conflict resolved, no design judged, nothing integrated or patched, no
  canonical Master drafted, no final-Master organization chosen.
- The verified chronologies, placement map, evidence table, corrected queue, and unresolved register
  above are the output of stage-order step 2.
- Next (Stage 1 v1.3 §9.1 step 3, on Ness's instruction): the full feature-recovery audit, walking the
  §6 corrected queue, applying the acceptance-and-revision rule.

**STAGE 2 COMPLETE. AWAITING NESS.**

---

## 9. SOURCE-RANGE VERIFICATION REPORT (what was actually read)

So nothing here rests on memory or on the Stage-1 hypothesis. All reads were of the verbatim source
bodies embedded in the Reader Parts (not the §4 index rows).

| Evidence gathered | Method | Coverage |
|---|---|---|
| Block metadata headers (filename, SRC ID, declared status, **Related-version family**) for all 92 bodies | `awk` over the BEGIN-SOURCE…VERBATIM-BEGINS headers, Parts 01–11 | All 92 source blocks |
| Internal chronology-signal lines (session declarations, dates, supersede/replace/regenerate/consolidate, "this is MASTER-X", "Synced to", "Supersedes", "derived FROM") in Master + Decision-Defaults bodies | `awk` line-scan inside VERBATIM-CONTENT, Parts 02–08, 11, UTF-8-sanitised | Every Master body and every Decision-Defaults body (titles/preambles + change-log lines) |
| Targeted provenance lines for `MASTER-11_1`, `MASTER-19_FULL`, `DD-S10_1/S12/S13`, `AFTER_BGMM`, `TSC_v1`, `section13_ADD`, `DELTA_S14`, continuity + shared handoff, `MASTER_CONTEXT` | two focused `awk` passes (first 6–8 content lines + keyword lines) | The specific bodies needed to close §2–§4 |
| Manifest rows (v1–v5) confirming v6→v7 predecessor, MASTER-17 split source, COMPLETE "supersedes" | included in the chronology-signal scan of Part 11 | SRC-088–092 |

### 9.1 What was NOT read in full (out of scope for chronology)
- The **full design bodies** of each Master beyond titles/preambles/change-logs (the line-by-line
  feature content is the Stage-3 feature audit, not chronology).
- The two binaries (survey PDF, `files__3_.zip`) — metadata only; not needed for chronology.
- Absent and unrecoverable bodies (§7C/§7D) — cannot be read.

### 9.2 Confidence note
The Master and Decision-Defaults chronologies rest on **explicit, dated, internal statements** and are
high-confidence VERIFIED. The remaining `UNCLEAR` items are same-session/same-date sibling orderings
and the MASTER-19 cluster {v1, v3, v6, FULL} internal-order questions, which by their nature cannot be
settled from dates or declarations and are correctly deferred to body comparison — not guessed.

### 9.3 Citation traceability and source accounting (v1.1 additions)
- **Citations are unambiguous (§5):** each carries Reader Part + SRC ID + exact line/range + a short
  description, and all `L#` line numbers are **source-body-relative** (relative to each source file's
  own line 1), not Reader-Part-relative. This pass used **headings, preambles, change logs, provenance
  statements, and targeted chronology lines — not every design body in full** (full-body reading is the
  Stage-3 feature audit).
- **Every source is accounted for (§10):** the appendix gives one primary disposition for every
  SRC-001–092 and confirms that **no source was dropped for being off-spine** — design specs,
  prototypes, code, notes, handoffs, manifests, and binaries are all carried forward (to the feature
  audit or as provenance), exactly as the verified Masters and Decision Defaults are.

**STAGE 2 v1.1 COMPLETE. AWAITING NESS.**

---

## 10. SOURCE-ACCOUNTING APPENDIX — one primary disposition for every SRC-001–092

**Purpose.** Confirm completeness: every preserved source has a primary disposition in this recovery,
and **no source was removed merely because it is not part of the Master or Decision-Defaults spine.**
Each SRC appears in exactly one bucket below (its *primary* disposition; many also appear elsewhere as
evidence). 92 unique source bodies, all present.

**Bucket 1 — CONFIRMED CURRENT authority (4):** SRC-015 (DD-S19_v2_2), SRC-044 (MASTER-19_v7_1),
SRC-076 (Cursor Rules v3.2), SRC-087 (governance/archive companion).

**Bucket 2 — Master spine, verified (23):** SRC-046 (M-5), 047 (M-6), 048 (M-6__1_), 049 (M-7),
050 (M-8), 051 (M-9), 052 (M-9.2), 053 (M-9.4), 022 (M-10), 023 (M-10__1_), 024 (M-11), 025 (M-11.1),
026 (M-13), 027/031/032/033/034 (M-14 cluster), 028/029/030 (M-14_FINAL cluster), 039 (M-17 full draft),
040 (M-18 full draft). → §6.1 queue.

**Bucket 3 — MASTER-19 comparison cluster, internal order UNCLEAR (4):** SRC-041 (v1), 042 (v3),
043 (v6), 045 (FULL). Only `v6 → v7_1` verified. → §6.1 item 15.

**Bucket 4 — Master split / pre-spine / context (7):** SRC-035–038 (M-17 reader slices — PARTIAL/SPLIT),
SRC-054 (MASTER_CONTEXT — pre-spine, CONFLICTING), SRC-055/056 (MASTER_FILE_COMPLETE family — June-19
standalone). → §4 / §6.1 item 1.

**Bucket 5 — Decision-Defaults spine, verified (12):** SRC-016 (bare), 018 (__1_), 019 (__2_),
017 (_ADD), 007 (S10_1), 008 (S12), 009 (S13), 010 (S13__1_), 011 (S13__3_), 012 (S13__4_),
013 (S17_AUDITED), 014 (S19_v1). → §6.2 queue.

**Bucket 6 — Addenda / deltas (2):** SRC-020 (DELTA_S14), SRC-057 (section13_ADD / §13). → §4.

**Bucket 7 — Accepted companions (2):** SRC-001 (AFTER_BGMM, accepted), SRC-002 (TSC_v1, accepted —
later fuller expansion). → §6.3-A.

**Bucket 8 — Design specs / sources, carried to the feature audit (16):** SRC-003 (Build_Checklist),
005 (Cursor brief — reading validator), 006 (Canvas spec), 021 (INSIGHT / design compass),
058 (Meaning Engine B5 design), 059 (Mobile spec), 062/063/064 (Universal Filter Design ×3),
065 (Universal Filter RULES), 067 (chat front-door sketch), 072/073 (risk review + OpenRouter ×2),
074 (wellbeing baseline), 085 (research architecture explained), 086 (search-pipeline security). → §6.3-B.

**Bucket 9 — Governance / roles (1):** SRC-066 (WORKING_ROLES). → governance (provenance).

**Bucket 10 — Handoffs / continuity / notes, provenance (4):** SRC-004 (handoff after BGMM),
060 (continuity note post-M17), 061 (shared handoff before consolidation), 068 (honest calibration
note). → §4.

**Bucket 11 — Prototypes / diagrams, provenance (6):** SRC-069/070 (live_mechanism HTML ×2),
071 (live_mechanism SVG), 078 (2a prototype HTML), 079 (architecture canvas HTML), 080 (icon HTML).

**Bucket 12 — Code, provenance (4):** SRC-081 (ingest_chatgpt.py), 082 (nh_log.py), 083 (nh_probe.py),
084 (nh_probe_truth.py).

**Bucket 13 — Provenance manifests (5):** SRC-088–092 (manifests v1→v5; verified supersession chain,
v5 latest). → §4.

**Bucket 14 — Binaries, provenance (2):** SRC-075 (survey PDF), SRC-077 (`files__3_.zip`).

**Tally:** 4 + 23 + 4 + 7 + 12 + 2 + 2 + 16 + 1 + 4 + 6 + 4 + 5 + 2 = **92.** Every SRC-001–092 is
accounted for; **none dropped for being off-spine.** Absent/unrecoverable items (§7C/§7D) are named
files with no body to dispose of, not preserved sources.

---

## 11. CORRECTION LEDGER (Stage 2 v1 → v1.1)

Stage 2 v1 is preserved unchanged; all chronology research is preserved. Each row is a planning/citation
correction only; no chronology finding was reversed and no architecture was touched.

| # | Where | v1 said (old) | v1.1 says (replacement) |
|---|---|---|---|
| 1 | §1 table; §2.3; §2.4 diagram; §6.1 queue; §7 register | Showed `MASTER-19 v1 → v3 → v6 → v7_1` (and FULL separately) as a sequence | The four bodies {v1, v3, v6, FULL} are **one MASTER-19 comparison cluster, internal order UNCLEAR**; no `v1→v3→v6` asserted; the **only verified terminal link is `v6 → v7_1`** |
| 2 | new §10 | (no full source accounting) | Added a **source-accounting appendix**: one primary disposition for every SRC-001–092 (14 buckets, tally = 92), confirming **no source was dropped for being off-spine** |
| 3 | §5 (header + every row) | Citations gave SRC + a `L#` with no stated convention | Every citation now states **Reader Part + SRC + exact line/range + description**; a convention note clarifies all `L#` are **source-body-relative** (not Reader-Part-relative); preserved the truthful statement that chronology used headings/preambles/change-logs/provenance/targeted lines, **not every design body in full** |
| 4 | §5 evidence table | Row **E21** asserted the RTX 3090 hardware decision as chronology evidence | **E21 removed** from the chronology evidence table; the hardware decision is **preserved for the Stage-3 feature audit** (E-numbering kept stable; E21 intentionally vacant) |
| 5 | §4 placement map; §5 E20; §6.3 | TSC_v1 labeled "**VERIFIED revision**"; "current full spec" | Relabeled **"VERIFIED LATER FULLER ACCEPTED SPECIFICATION / EXPANSION"** of the AFTER_BGMM TSC foundation; **both accepted TSC records preserved**; no cited Ness decision proves replacement/supersession |

**This file performs none of Stage 3.** No feature recovery, no judging which design is better, no
conflict resolution, no integration or patching, no final-Master organization choice, no canonical
drafting.

**STAGE 2 v1.1 COMPLETE. AWAITING NESS.**
