# N.H — FINAL-MASTER RECOVERY — STAGE 2: CHRONOLOGY VERIFICATION v1

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
| S19 / adoption (June 26 → 28) | MASTER-19 v1 → v3 → v6 → **v7_1 (adopted June 28)**; MASTER-19_FULL | DD-S19_v1 (v6, June 26) → **DD-S19_v2_2 (v7_1, June 28)** |

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
- **MASTER-19_CORRECTED_v1 (SRC-041)** and **_v3 (SRC-042)** — earlier corrected MASTER-19 bodies; share
  the consolidation preamble; carry **no internal supersession statement** naming each other.
  Classification: **earlier MASTER-19 lineage bodies; current authority is later.** Their relative order
  (v1 vs v3) and their precise relationship to v6 are **UNCLEAR from internal evidence** (version tokens
  alone do not prove it — §0A); to be settled by body comparison in the feature audit.
- **MASTER-19_CORRECTED_v6 (SRC-043)** — **VERIFIED PREDECESSOR** of v7_1: stated by v7_1's own body
  ("It supersedes NH_MASTER-19_CORRECTED_v6.md"), by the AFTER_BGMM handoff, and by every manifest
  ("MASTER-19 v6 — declared predecessor of v7_1").
- **MASTER-19_CORRECTED_v7_1 (SRC-044)** — **CONFIRMED CURRENT / VERIFIED SUCCESSOR.** Its own body:
  Session 18 conceptual design integrated; "the adopted authoritative N.H Master, explicitly adopted by
  Ness (June 28 2026); it supersedes NH_MASTER-19_CORRECTED_v6.md."
- **MASTER-19_FULL (SRC-045)** — same title and intro as the v6/v7 bodies ("MASTER-19: Full Backup with
  All Additions"; "complete S17 and S18 conceptual design AND all S19 restorations"); carries the
  consolidation preamble but **no adoption/supersession line**. Classification: **MASTER-19 lineage;
  exact ordinal position relative to v1/v3/v6/v7 is UNCLEAR** (no internal date/supersession beyond the
  shared preamble) — a `VERIFIED SIBLING / PARALLEL BRANCH` candidate to be placed by body comparison,
  not by the word "FULL."

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
        → MASTER-19 {v1, v3}··(order UNCLEAR)··→ v6 → **v7_1 (adopted June 28)**
        → MASTER-19_FULL  (M19 lineage; ordinal UNCLEAR)
```
`→` VERIFIED predecessor→successor · `∅` SOURCE BODY ABSENT · `··` UNCLEAR link · `⇒` parent→split/derived.

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
| `NH_MASTER-19_FULL.md` | SRC-045 | UNCLEAR (MASTER-19 lineage) | Same title/intro as v6/v7; contains S17+S18+S19; ordinal vs v1/v3/v6/v7 unproven — place by body comparison |
| `NH_MASTER-17_*` (4 slices) | SRC-035–038 | PARTIAL OR SPLIT REPRESENTATION | Derived reader slices of MASTER-17_full (SRC-039); VERIFIED via manifest + "DERIVED READER COPY" |
| `NH_MASTER_section13_ADD.md` | SRC-057 | VERIFIED ADDENDUM | June 21 / session 8; explicit "ADD TO MASTER AS §13" (the Live Loop) → folded into the spine at MASTER-9.3/9.4 |
| `NH_DELTA_S14.md` | SRC-020 | VERIFIED ADDENDUM / DELTA | Session 14 (June 23); "derived from MASTER-14_FINAL"; records S14 decisions toward absent MASTER-15 |
| `NH_DECISION_DEFAULTS_ADD.md` | SRC-017 | VERIFIED ADDENDUM | Session-8 DD add-on fragment |
| `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | SRC-004 | Handoff (provenance) | Security/identity/BGMM branch; v6-era; "none patched into the Master" |
| `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | SRC-061 | Handoff (provenance) | "Created June 28 2026"; pre-consolidation shared handoff |
| `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | SRC-060 | Continuity note (provenance) | Post-MASTER-17 (~June 24); explicitly not an authority |
| Manifests v1→v5 | SRC-088–092 | VERIFIED PREDECESSOR → SUCCESSOR chain | v2 supersedes v1; v3 supersedes v1–2; v4 supersedes v1–3; v5 supersedes v1–4 (carried forward from v4). v5 latest. Provenance-only |
| `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | SRC-001 | ACCEPTED (companion) | v6/S19_v1-era (~June 26); references MASTER-19_v6 as patch target; holds the **earlier** accepted TSC foundation; accepted, not yet patched |
| `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | SRC-002 | ACCEPTED (companion) + VERIFIED revision | The **later, full 31-section** TSC spec; references MASTER-19_v6; DD-S19_v2_2 points to it as the authoritative TSC spec. AFTER_BGMM = earlier foundation → TSC_v1 = fuller spec; **both accepted, both preserved** (acceptance-and-revision rule; not a recency supersession) |

---

## 5. EVIDENCE TABLE (exact source records and passages)

Citations give the SOURCE ID and the line within that body's verbatim content (as embedded in the
Reader Parts). Quotes are short; most are paraphrased.

| # | Relationship established | Source(s) | Passage cited |
|---|---|---|---|
| E1 | v7_1 supersedes v6; adopted June 28; integrates S18 | SRC-044 L8 | body: "adopted authoritative… adopted by Ness (June 28 2026)… supersedes NH_MASTER-19_CORRECTED_v6.md" |
| E2 | v6 is the declared predecessor of v7_1 | SRC-043 hdr; SRC-088–092 (rows); AFTER_BGMM handoff | manifests: "MASTER-19 v6 — declared predecessor of v7_1" |
| E3 | DD-S19_v2_2 is current; supersedes all prior; tied to v7_1 (June 28) | SRC-015 L3,L5,L8 | "Synced to …v7_1 (June 28 2026)"; "Supersedes …S19_v2_1.md and all prior Decision Defaults versions" |
| E4 | DD-S19_v1 supersedes S17; tied to v6 (June 26); candidate | SRC-014 L3,L5,L7 | "Synced to …v6 (adopted June 26 2026)"; "Supersedes …S17_AUDITED_v1.md"; "CANDIDATE" |
| E5 | DD-S17 regenerated from MASTER-17_full on June 24 (derived) | SRC-013 L4 | "Regenerated from NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md on June 24 2026… Derived FROM the Master" |
| E6 | MASTER-17_full is the source of the 4 reader slices | SRC-088 L82; SRC-090/091/092 rows; SRC-035–038 hdrs | manifest: "Source of the four reader slices"; slice status "DERIVED READER COPY" |
| E7 | MASTER-14 cluster all = session 13; "2a built" overclaim corrected | SRC-027 L4 vs SRC-028/029/030/031–034 L4; SRC-009 L3 | SRC-027: "BUILT 2a — the reading record"; FINAL bodies: "BUILT the 2a PLUMBING… NOT the full reading record"; DD-S13: "an overstatement, '2a built,' propagated to ten places before it was caught" |
| E8 | MASTER-13 = session 12 (large build) | SRC-026 L4 | "Session 12 (June 22 2026, late)… this is MASTER-13" |
| E9 | MASTER-11.1 = session 10 evening, after MASTER-11 | SRC-007 L3 | DD-S10_1: "Updated session 10-evening (June 22 2026) to match MASTER-11.1: 2a's STRUCTURE is now CLOSED… DUMB-vs-SMART machinery frame added" |
| E10 | MASTER-11 = session 10; reality→story re-soul | SRC-024 L3,L7 | "session 10 (June 22 2026, afternoon)… this is MASTER-11"; "'reality-layer' is REPLACED by 'per-person STORY-layer'" |
| E11 | MASTER-10 = session 9; reality rework | SRC-022 L3 | "session 9 (June 22 2026, past midnight)… this is MASTER-10" |
| E12 | MASTER-9.4 additive over absent 9.3 (S8); adds §14 | SRC-053 L3 | "session 8… this is MASTER-9.4… ADDITIVE update over MASTER-9.3… 9.4 adds §14" |
| E13 | MASTER-9.2 additive over absent 9.1 (S7) | SRC-052 L3 | "session 7… this is MASTER-9.2… ADDITIVE update over MASTER-9.1" |
| E14 | MASTER-9/8 = S5/S4 | SRC-051 L3; SRC-050 L3 | "session 5… this is MASTER-9"; "session 4… this is MASTER-8" |
| E15 | 6 → 6__1_ additive (6__1_ adds cursorrules v3.1) | SRC-047 L3; SRC-048 L3 | 6: embeds UF+ME; 6__1_: embeds UF+ME "AND the full in-force code ruleset (.cursorrules v3.1)" |
| E16 | COMPLETE family = June 19; supersedes earlier context | SRC-055 L2; SRC-056 L2 | "Written June 19 2026… Supersedes earlier master context… on the name" |
| E17 | section13_ADD = session 8 §13 (Live Loop) source | SRC-057 L1,L4 | "ADD TO MASTER AS §13"; "June 21 2026 — session 8… DESIGNED the live loop (§13)" |
| E18 | DELTA_S14 = session 14, derived from MASTER-14_FINAL | SRC-020 L2,L4 | "Session 14 (June 23 2026)"; "Derived from NH_MASTER-14_FINAL.md" |
| E19 | Manifest chain v1→v5 each supersedes prior; v5 latest | SRC-089 L5; SRC-090 L5; SRC-091 L5; SRC-092 L5 | v3: "Supersedes v1… and v2…"; v5: "Supersedes v1…v4… carried forward from v4 unchanged" |
| E20 | TSC_v1 = later full 31-section spec; AFTER_BGMM = earlier TSC foundation; both reference v6; both accepted | SRC-002 L5,L20; SRC-001 L11; SRC-015 L218 | TSC_v1: "complete accepted 31-section… AFTER_BGMM preserves the earlier accepted TSC foundation"; AFTER_BGMM: patch target "MASTER-19_CORRECTED_v6"; DD-S19_v2_2: TSC design is "the authoritative specification" |
| E21 | Hardware RTX 3090 supersedes the S16 RTX 5060 Ti plan (a dated decision, the S16 plan sealed) | SRC-015 L109 (and across M19 bodies) | "RTX 3090 24GB (supersedes S16 RTX 5060 Ti 16GB plan)… preserved as a dated decision snapshot" |
| E22 | DD-S12/S13 tied to MASTER-13/14 | SRC-008 L3; SRC-009 L3 | "Updated session 12… to match MASTER-13"; "Regenerated session 13… to match MASTER-14" |

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
15. → `MASTER-19_CORRECTED_v1` (SRC-041) ·· `_v3` (SRC-042)  *(internal order UNCLEAR — compare bodies)*
16. → `MASTER-19_CORRECTED_v6` (SRC-043)
17. → **`MASTER-19_CORRECTED_v7_1` (SRC-044) — terminal / CONFIRMED CURRENT**
18. Parallel placement pass: `MASTER-19_FULL` (SRC-045) ↔ the v1→v7_1 chain *(ordinal UNCLEAR; place by body)*

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
  acceptance-and-revision rule; TSC_v1 = current full spec, AFTER_BGMM = earlier foundation; both
  preserved. (No patching in the audit.)
- B. Design specs (Universal Filter ×3 + RULES, Meaning Engine B5, Mobile, Canvas, chat-frontdoor,
  wellbeing baseline, research architecture, search-pipeline security) ↔ their Master sections — for
  full mechanisms the Master may only summarize.

---

## 7. UNRESOLVED-CHRONOLOGY REGISTER

Carried into the feature audit; none decided here.

**A. UNCLEAR internal order (same session/date; settle by body comparison):**
1. `MASTER-19_CORRECTED_v1` vs `_v3`, and their precise relationship to `v6` (only v6→v7_1 is proven).
2. `MASTER-19_FULL` (SRC-045) ordinal position within the MASTER-19 lineage.
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
and the MASTER-19 v1/v3/FULL ordinal questions, which by their nature cannot be settled from dates or
declarations and are correctly deferred to body comparison — not guessed.

**STAGE 2 v1 COMPLETE. AWAITING NESS.**
