# N.H DECISION INDEX — PROPOSAL
**Filename:** `NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
**Status:** CANDIDATE — proposal only. Not authoritative. Not audited. Not accepted. Changes nothing.
**Revision note:** v0_10 = v0_9 corrected for the one verified issue in ChatGPT's audit of v0_9 (Part K.10); v0_9 (751 lines, 110,465 bytes, SHA-256 `08e6c4014aabf0c48c4822ec051605dddde9057b9bd9dc9cdc31df444abd4459`) is preserved unchanged as unpassed history. v0_9 = v0_8 corrected for the seven verified issues in ChatGPT's audit of v0_8 (Part K.9); v0_8 (738 lines, 108,797 bytes, SHA-256 `fa9df13613d820655f530a41d8a61e5ba28d5dce4e1bbf70702899c4444f901c`) is preserved unchanged as unpassed history. v0_8 = v0_7 corrected for the three verified issues in ChatGPT's audit of v0_7 (Part K.8); v0_7 (729 lines, 107,028 bytes, SHA-256 `424a61330e0ec2f3bf7a9a4933e4b218b602af547a3c12bebd30baf6f2919d28`) is preserved unchanged as unpassed history. v0_7 = accepted v0_6 updated only for currentness (Part K.7): A19-RS and A19-CI package-complete for their standalone scopes; the narrow UE5 runtime-direction acceptance (NHD-UE5-1, §1 and §49 only); the completed 2026-09-17 folder cleanup; and one deferred open item (the seven-web pass). v0_6 (712 lines, 92,076 bytes, SHA-256 `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9`) remains preserved unchanged as the accepted prior version — Ness accepted it by writing "I accept index v0_6." v0_6 = accepted v0_5 updated only to record the acceptance status already carried by its audited acceptance record, including Part A's approved identifier scheme, and Ness's later direct written confirmation of NHD-WR-20260916-2 (Part G.3 and matching pointers in Parts O, P and J; see Part K.6). v0_5 remains preserved unchanged as the accepted prior version. v0_5 = v0_4 corrected for the one verified issue in ChatGPT's fourth audit (Part K.5). v0_4 = v0_3 corrected for the four verified issues in ChatGPT's third audit (Part K.4). v0_3 = v0_2 corrected for the seven verified issues in ChatGPT's second audit (Part K.3). v0_2 = v0_1 corrected for the eleven issues of the first audit (Part K.2). v0_1 through v0_5 are preserved unchanged as history. Scope not broadened.
**Prepared:** 2026-09-16. Base v0_5 prepared by Claude on Ness's direct request following the ChatGPT-prepared six-point instruction of the same date; v0_6 prepared by ChatGPT on Ness's direct written instruction; v0_7 through v0_10 prepared by Claude on 2026-09-17 on ChatGPT's exact task instructions.
**Authority order (unchanged):** `NH_MASTER-20_CORRECTED_v10.md` (adopted 2026-06-29) → `NH_DECISION_DEFAULTS-S19_v2_2.md` → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. The Design and Wiring Map v1.6 is subordinate.
**What this file is:** an index that points INTO existing files. It never replaces the Master or any accepted package. It is the "index at the front of the book," not the book.
**What this file is not:** not a new Master, not a package, not an acceptance, not evidence of implementation.

## Sources reviewed in this version
| Source | Where | Identity |
|---|---|---|
| `NH_MASTER-20_CORRECTED_v10.md` | repo `01_AUTHORITATIVE/` | SHA-256 `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c`, 5,736 lines |
| Repository head | `github.com/nesgeva/NH-GOVERNANCE` | **current: commit `19071b51b61ecc1b943ea3cce6e024a8ba032cc7` (2026-09-17 02:24 +03:00), 148 tracked files: 96 in `04_ACCEPTED_STANDALONE_DESIGNS/`, 20 in `05_ACTIVE_CANDIDATE/`, 2 in `05_INACTIVE_CANDIDATE/`, 15 in `99_HISTORICAL_CANDIDATES/`.** Earlier reference point: commit `2e7a710b…` (2026-09-16 22:30 +03:00), 146 files. Passes 1–2 were run at `5e000f8f…` (2026-09-15, 138 files); the eight additions since are Ness's pushes of 2026-09-16 (`ca5713f`, `b45b98d`, `73f565c`, `bea3098`, `2e7a710`), all bytes verified — see M.10. Master identity unchanged across all heads. |
| 96 files in the accepted folder (81 at the first survey; +4 AIC/UDOK on 2026-09-16; +3 A19 receipts and +8 accepted sources moved in on 2026-09-17) | `04_ACCEPTED_STANDALONE_DESIGNS/` | Pass 2 done at package level (Part L); decision-by-decision rows (Pass 2b) pending |
| A19 checkpoint v1.2, `NH_DESIGN_ANSWERS.md`, `HISTORICAL_ANSWERS.md`, `00_CONTINUATION_CONTEXT.md`, Five Additions package, intent excerpts, UE5 package, personal A19 idea note | `05_ACTIVE_CANDIDATE/`, root | Pass 3 done (Part N) |
| `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | project file | §2–§4 read (voice compatibility) |
| A19-RS: `NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` (136 lines, 15,053 bytes, SHA-256 `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0`) and its closure record `NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (156 lines, 10,976 bytes, SHA-256 `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e`) | `04_ACCEPTED_STANDALONE_DESIGNS/` | read and recalculated 2026-09-17; PACKAGE_COMPLETE for the standalone room-start policy scope |
| A19-CI: `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` (180 lines, 18,830 bytes, SHA-256 `7bb426d211685ba9f96b2194163bcbb6750365ed689ef19b0614f5b217288451`) and its closure record `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (191 lines, 14,182 bytes, SHA-256 `8f22b0a1dd7b4393934af873993ef797437e8d312164b1676caecab2e240f18c`) | `04_ACCEPTED_STANDALONE_DESIGNS/` | read and recalculated 2026-09-17; PACKAGE_COMPLETE for the standalone ordinary-chat policy scope |
| UE5 runtime-direction acceptance record `NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` (239 lines, 22,212 bytes, SHA-256 `a5d6735f867d1c8680ee09ecf1bc9b24477469bdd6cd2c719444916eddfad7eb`) | `04_ACCEPTED_STANDALONE_DESIGNS/` | read and recalculated 2026-09-17; passed formal receipt for NHD-UE5-1 (§1 and §49 only) |
| Conversation working record 2026-07-21 (Claude chat "Design work map v1.3 → v1.4 update"), §4.1 | not in repo | July 21 room-initialization decisions |
| `NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | delivered record; not committed by its audit task | Records Ness's acceptance of v0_5 and approval of Part A; 74 lines, 7,516 bytes, SHA-256 `49245fbe6cac5809e89fe8eb53da2a7ab9761f909901caf6f0d70a2139ba017c`; ChatGPT PASS 2026-09-16 |
| Ness's direct written statement to ChatGPT, 2026-09-16 | current conversation; not yet in a project file | Confirms NHD-WR-20260916-2; quoted verbatim in Part G.3 |

---

## PART A — THE IDENTIFIER SCHEME (approved by Ness through the accepted v0_5 index; acceptance record v1_2)

**Rule 1 — frozen files are never touched.** IDs live in this index and point into the files. No accepted, adopted, or historical file is renumbered, rewritten, or annotated.

**Rule 2 — one stable form:** `NHD-<owner>-<n>`
- `NHD-A6-1` — decision 1 of package A6 (existing label `A6-1` kept exactly)
- `NHD-A13-1` — existing label `A13.1` (dot form collapses to hyphen in the index only; the file keeps its spelling)
- `NHD-M19A-3` — Master §19A, settled point 3
- `NHD-M11-9` — Master §11, item 9
- `NHD-H1753` — historical answer H1753 (H/N numbers kept as-is)
- `NHD-WR-20260721-1` — decision 1 from a working record dated 2026-07-21 (not yet in any file)

**Rule 3 — existing numbers win.** Where a package already labels a decision, that number is kept. Where it does not, numbers are assigned in document order within that package and the exact section + wording is recorded so the pointer is verifiable.

**Rule 4 — one decision, one ID.** The same decision stated in several documents gets one ID and several source rows. Similar wording does not merge different decisions.

**Rule 5 — IDs are permanent.** A replaced decision keeps its ID and gets `superseded_by: NHD-…`. Numbers are never reused.

**Rule 6 — every entry carries:** existing label · stable ID · plain-language meaning · exact file / version / section / line · acceptance evidence · component and bundle · later correction / replacement / conflict / dependency · status.

**Status vocabulary (fixed):**
`ness_decision` (Ness's recorded words) · `ness_intent` (Ness's stated wish/direction, not yet a decision) · `accepted_package` (package with acceptance record) · `master_settled` (settled wording in adopted Master) · `master_open` (Master says open) · `assistant_proposal` (Claude/ChatGPT wording not confirmed by Ness) · `superseded` · `evidence_missing` · `built` (disk-verified per Master) — note: `accepted` never implies `built`.

**Bundle 8 rule that this scheme enables:** every proposed wiring connection carries the `NHD-…` IDs that authorize it. No ID → the connection stays unresolved and is classed as `missing_source` (recovery task), `unfinished_mechanics` (Claude on exact instruction), or `new_design_choice` (Register A — Ness). Not every gap is Register A.

---

## PART B — PASS 1: MASTER V10 SECTION REGISTER
Every top-level section of the adopted Master, its own status tag, and its ID prefix. Status is the Master's own wording; nothing is upgraded.

| ID prefix | Line | Section | Master's own status |
|---|---|---|---|
| NHD-M0 | 199 | §0 The premise — never decide facts | DESIGNED — floor under every rule |
| NHD-M0A | 218 | §0A DUMB vs SMART | DESIGNED — top-level frame |
| NHD-M0B | 233 | §0B Full-transparency and living-record law | DESIGNED — foundational operating rule |
| NHD-M1 | 263 | §1 What N.H is | (statement) |
| NHD-M1A | 282 | §1A Input-agnostic principle | DESIGNED |
| NHD-M2 | 290 | §2 How to work with Ness | (working rules) |
| NHD-M3 | 320 | §3 Evolution old vs new | (historical) |
| NHD-M4 | 338 | §4 The machine | (hardware; see §11 item 3 for the RTX 3090 decision) |
| NHD-M5 | 349 | §5 Codebase map | (disk facts) |
| NHD-M6 | 384 | §6 Built & verified on disk | BUILT |
| NHD-M6A | 404 | §6A Code rules — cursorrules v3.2 | IN FORCE |
| NHD-M6B | 527 | §6B Accretive store — schema + state | BUILT & VERIFIED |
| NHD-M7 | 555 | §7 Universal Filter + Meaning Engine | engines A + B BUILT; §7E–§7P conceptually designed; §7D/§7Q partial |
| NHD-M7D | 633 | §7D Living State Web | PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7E | 673 | §7E Catalog front door (incl. §7E-TSC, 31 sections) | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7F | 1647 | §7F Context retrieval | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7G | 1673 | §7G Meaning Engine interior | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7H | 2114 | §7H Reread lifecycle | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7I | 2134 | §7I View layer | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7J | 2148 | §7J Contradiction and clash handling | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7K | 2182 | §7K Story layer | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7L | 2220 | §7L Person-boxes | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7M | 2252 | §7M Computed view | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7N | 2285 | §7N Action surfacing | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7O | 2316 | §7O Action-result return path | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7P | 2349 | §7P Permission and authority boundaries | CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7Q | 2405 | §7Q Privacy, deletion, sensitive data | PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M7R | 2503 | §7R Attention and relevance control | CORE CONCEPTUALLY DESIGNED, NOT BUILT |
| NHD-M8 | 2784 | §8 Research pipeline | DESIGNED — Brave not wired |
| NHD-M9 | 2813 | §9 Designed, not built — the rest | DESIGNED / CONCEPTUALLY DESIGNED |
| NHD-M9A | 2842 | §9A Image ingest | DESIGNED |
| NHD-M10 | 2845 | §10 Originality | (calibration) |
| NHD-M11 | 2852 | §11 What's open / next | (register — see Part C) |
| NHD-M11S | 2894 | §11-SETTLED (condensed) | (register of settled session outcomes S4–POST-S19) |
| NHD-M12 | 2908 | §12 Session 6 data rescue | recovery done; ingest FROZEN |
| NHD-M13 | 2911 | §13 The live loop | DESIGNED — not built |
| NHD-M14 | 2926 | §14 The chat front door | PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT (see Part E) |
| NHD-M15 | 2948 | §15 Session 10 housekeeping | done |
| NHD-M16 | 2953 | §16 Model layer — borrowed mouth + search model | DESIGNED + partly on disk |
| NHD-M17 | 2979 | §17 S16 correction log | historical |
| NHD-M18 | 2997 | §18 S17 consolidation log | historical |
| NHD-M19 | 3024 | §19 Interface, World, Interaction | IN-PROGRESS DESIGN, NOT BUILT (see Part D) |
| NHD-M20 | 3121 | §20 S18 change log | HISTORICAL SNAPSHOT (2026-06-24) |
| NHD-M21 | 3149 | §21 S19 change log | HISTORICAL SNAPSHOT (2026-06-25) |
| NHD-M22 | 3174 | §22 Wellbeing and behavioral baseline | DESIGNED — NOT BUILT |
| NHD-M23 | 3236 | §23 Mobile app — three-mode companion | DESIGNED — NOT BUILT |
| NHD-M24 | 3277 | §24 Connection capability | CONCEPTUALLY DESIGNED (S19), NOT BUILT |
| NHD-M25 | 3318 | §25 Voice security and identity (BOP, SIA, SACL, BAI, BGMM…) | ACCEPTED DESIGN — NOT BUILT |
| NHD-M26 | 4988 | §26 Personal learning and adaptation (incl. OOP, LMAC) | ACCEPTED DESIGN — NOT BUILT |
| NHD-M27 | 5697 | §27 Historical recovery and correction log | historical |

**Known stale wording in the Master itself (recorded, not corrected here):** the V10 header still says "NOT YET ADOPTED" with Master-19 v7_1 authoritative. Superseded by Ness's adoption of 2026-06-29. Correctable only through a future versioned Master candidate.

---

## PART C — MASTER §11 REGISTER (lines 2852–2892)
The Master's own open/settled list, item by item. Status = the Master's own words.

| ID | Item | Status per Master | Notes |
|---|---|---|---|
| NHD-M11-1 | Append-only accretive store | `built` (5,521 sealed); (c) live-flow wiring open | |
| NHD-M11-2 | Forced order 2a→2b→2c; Engine C next | A, B built; C needs story-bearing gold cases | A1 replacement gold set accepted as standalone package (Pass 2) |
| NHD-M11-2b | Detector recipe locked, live build deferred | `master_settled` (recipe) / open (build) | |
| NHD-M11-3 | Model wiring local-first; Chroma rebuild done; **hardware: RTX 3090 24GB supersedes RTX 5060 Ti 16GB** | `master_settled` | Archive §9 records the hardware drift as a conflict — the Master resolves it; archive is pre-adoption |
| NHD-M11-4 | Night-search — committed, later | `master_settled` (commitment) / open (build) | Brave query counter required |
| NHD-M11-5 | Image-ingest front door | open | §9A |
| NHD-M11-6 | Universal Filter / meaning engine = item 2c | in progress | |
| NHD-M11-7 | ChromaDB `nh_roots_v1` built; old 116k kept | `built` | |
| NHD-M11-8 | Research pipeline build | open | Brave cap required |
| NHD-M11-9 | Academic search source — **Semantic Scholar + OpenAlex; Google Scholar off** | `master_settled` (2026-06-29) | |
| NHD-M11-9h | Hetzner sovereignty sync | `superseded` (Ness, 2026-06-25: move away from Hetzner) | historical |
| NHD-M11-10..12 | nh_service disabled · mobile + canvas · HUD redesign | mixed | |
| NHD-M11-13 | [BUILT]-claims sweep | done (S13) | |
| NHD-M11-14 | Folder cleanup | open | disk housekeeping |
| NHD-M11-15 | Store-count reconciliation | closed (S12) | |
| NHD-M11-16 | WhatsApp archive ingest | deferred | |
| NHD-M11-17 | Low open design threads (spine, gate lags, clash UI, multi-box tagging, alias layer, schema rename) | open | |
| NHD-M11-18 | Multi-box sealed-batch architecture | concept settled; mechanics not designed | must precede a SECOND batch — cf. B11 (Pass 2) |
| NHD-M11-19 | Confidence = two-slot object | resolved (S14) | |
| NHD-M11-20 | Gold sets v1 + v2-B built & sealed | `built` | v1 8 cases, v2-B 7 cases; B3 miss cause not isolated |
| NHD-M11-21 | Reread lifecycle + view layer | conceptually designed, not built | §7H, §7I |
| NHD-M11-22 | Person-box contamination rule | governing rule designed; schema open | §7L |
| NHD-M11-23 | Off-board affirmation feedback seam | designed (weightless story-layer event) | B-AFFIRM accepted (Pass 2) |
| NHD-M11-24 | Privacy / threat model + redaction path | partial, not built | §7Q; B7 accepted (Pass 2) |
| NHD-M11-25 | Go-live hardening block | deferred; does not gate engine | |
| NHD-M11-26 | Model-replacement default | `master_settled` | new mouth tested on BOTH gold sets; no automatic mass reread |
| NHD-M11-27 | Quarantine phase + bootstrap retrieval rule | designed; store built (S14) | B16 accepted (Pass 2) |
| NHD-M11-28 | Living State Web | partial, not built | A6/B5/B6/B8 accepted in Bundle 4 (Pass 2) |
| NHD-M11-29 | Attention and relevance control — fourteen decisions | core designed (S18), not built | A4/B1/B-INT-1 accepted in Bundle 2 (Pass 2) |
| NHD-M11-30 | Wonder and simulation — scratch-space boundary settled; larger mechanism not designed | partial | A17 accepted with closure condition (Pass 3) |
| NHD-M11-31 | World model | NOT DESIGNED | A18 accepted in Bundle 4 (Pass 2) — Master wording stale |
| NHD-M11-32 | End-to-end cycle — post-root path designed; full cycle open | partial | B-CYCLE work = Bundle 8 |
| NHD-M11-33 | Interface, World, Interaction | in-progress | §19; A19 (Pass 3) |
| NHD-M11-34 | Meaning-to-technical mapping — five open questions in four groups | `master_open` | must stay recorded as open |
| NHD-M11-35 | TSC — accepted with later corrections; integrated at §7E-TSC | accepted design, not built | B15, B-INT-4 accepted (Pass 2) |

**Observation for Pass 5:** several §11 items say "not designed" or "open" while an accepted standalone package now exists (marked "Pass 2" above). These are the first confirmed stale-in-Master entries. They are not corrected here.

---

## PART D — MASTER §19 REGISTER (lines 3024–3120)

### D.1 §19A settled interface decisions — `master_settled`
| ID | Line | Settled point |
|---|---|---|
| NHD-M19A-1 | 3032 | Core direction — entering Ness's own world; world named "Ness's World" |
| NHD-M19A-2 | 3034 | Modes — Conversation mode and World mode; automatic switching may change presentation, must not act secretly |
| NHD-M19A-3 | 3036 | Opening Ness's World — identity-confirmation entry |
| NHD-M19A-4 | 3038 | Initial state and growth — world begins blank and grows from Ness's life |
| NHD-M19A-5 | 3040 | World properties |
| NHD-M19A-6 | 3042 | World-manipulation boundary |
| NHD-M19A-7 | 3044 | The white door |
| NHD-M19A-8 | 3046 | Chat as N.H's presence — chat available inside the world, not a fixed sidebar, movable/summonable/dismissable by voice |
| NHD-M19A-9 | 3048 | N.H's form — no single fixed form |
| NHD-M19A-10 | 3050 | Reading the room — small changes natural, big changes ask first |
| NHD-M19A-11 | 3052 | Voice — N.H speaks and listens; Ness may summon/silence/dismiss/turn off by voice |
| NHD-M19A-12 | 3054 | N.H reacting to Ness |
| NHD-M19A-13 | 3056 | Simulation basics — replay and simulation separate; simulation never begins secretly; entering simulation requires approval |
| NHD-M19A-14 | 3058 | Deep structure |
| NHD-M19A-15 | 3060 | Physical interaction methods desired (VR, camera hand tracking, mic, voice, mouse, keyboard, touch) |
| NHD-M19B-1 | 3066 | "Strongest current concept" — **in §19B PROVISIONAL CONCEPTS, not §19A**; the Master itself says it is a synthesis with varying settlement. Status: provisional, NOT `master_settled`. (v0_1 mislabeled this as NHD-M19A-16.) |
| NHD-M19E-0 | 3103 | Cross-audit note (in §19E): merge/split/reshape language could be read as mutating records; §19A now records that world manipulation is presentation-only. The settled point itself is NHD-M19A-6 (line 3042). |

### D.2 §19B provisional concepts (line 3064) — provisional; not settled. NHD-M19B-1 (line 3066) is listed in D.1 for continuity of numbering; nothing in §19B is `master_settled`.

### D.3 §19C unanswered questions (lines 3077–3083) — `master_open`
| ID | Question in Master | Later evidence (not a merge — see Part F) |
|---|---|---|
| NHD-M19C-1 | New space starts blank when creating from scratch? | A19 checkpoint v1.2 §12 (lines 238–250): "Create New World" leads to a blank white room — **different decision** (creation-path starting space), separate ID in Pass 3 |
| NHD-M19C-2 | Starts partly formed when N.H has enough memory? | — |
| NHD-M19C-3 | Can Ness choose blank / memory-built / mixed? | **answered** by NHD-WR-20260721-1 |
| NHD-M19C-4 | Can N.H choose automatically? | **answered** by NHD-WR-20260721-1 and -2 |
| NHD-M19C-5 | Can Ness change an automatic choice instantly by voice? | **answered** by NHD-WR-20260721-3 |
| NHD-M19C-6 | Additional list: opening transition; same-screen vs full-screen; desktop/mobile/VR differences; backtracking order; own direct door per recent space; full context of each correction preserved; learned-pattern display; challenging one learned pattern | Historical answers exist for several: H1546 (own direct door), N673/H1742 (full context of each correction), H1765 (backtracking order), H1757 (full learning history), H1760 (challenging one pattern) — Pass 3 maps each; the Master still lists them as unanswered |

### D.4 §19D paused design points (line 3087) — `master_open`
NHD-M19D-1 Simulation interior · NHD-M19D-2 Physical interaction · NHD-M19D-3 N.H's adaptive behavior · NHD-M19D-4 Exact visual language. Historical answers H1739/H1740/H1744/H1745/H1747/H1749/H1750/H1754/H1756/H1759/H1762/H1763 touch D-1 and D-2 (Pass 3).

### D.5 §19E open dependencies (line 3101) — `master_open`
NHD-M19E-1 Approval explicitness vs interface unobtrusiveness · NHD-M19E-2 Camera and VR as new front doors (privacy) · NHD-M19E-3 External actions from within the world (authority).

---

## PART E — MASTER §14 CHAT FRONT DOOR (lines 2926–2947)
| ID | Point | Status |
|---|---|---|
| NHD-M14-1 | Live chat is a first-class front door | `master_settled` (2026-06-29) |
| NHD-M14-2 | Every live-chat message captured automatically; no manual save marker | `master_settled` |
| NHD-M14-3 | Creation Filter is a mode inside the Meaning Engine (§7G), not a separate mechanism | `master_settled` |
| NHD-M14-4 | Two stages RAW → CATALOG; live chat may ask, nightly never asks | exploratory — Master line 2932: the remaining §14 content is "exploratory reference — revisit and confirm later" |
| NHD-M14-5 | Recorded-conversation label as provenance | exploratory (line 2932 names "recorded-conversation label" explicitly) |
| NHD-M14-6 | Speaker rule — connects, does not guess, does not claim | `master_settled` (S8) |
| NHD-M14-7 | Two-filter two-box layout | `superseded` (historical) |
| NHD-M14-8 | `re_reads` made visible for topic/spec referencing | exploratory (line 2932: "topic referencing mechanics") |
| NHD-M14-O1 | Exact Creation Mode implementation details | `master_open` |
| NHD-M14-O2 | Creation Store schema and file format | `master_open` |
| NHD-M14-O3 | Provisional-record detection behavior | `master_open` |

Chat *visual* layout (centered conversation, three-area ultrawide) is NOT in the Master; it lives in A19 checkpoint v1.2 §12 (Pass 3).

---

## PART F — VOICE INTERRUPTION: SETTLED vs NEW (for the separate voice discussion)

### F.1 Settled in Master V10 — preserved, not reopened
| ID | Line | Exact point |
|---|---|---|
| NHD-M26-VP | 5145–5147 | Voice priority rule: "When Ness speaks, N.H TTS stops immediately." Enforced by OOP during voice-mode function execution; recorded as an event root. |
| NHD-M25-BOP-VI | 3376–3377 | BOP event `voice_interrupt_of_nh`: Ness's voice began while N.H TTS active; carries timestamp **and position in N.H output stream**. Physical description only (DUMB). |
| NHD-M26-OOP-INT | 5283–5287 | OOP observes interruptions (voice or text) and corrections as physical facts; content enters as separate conversational root; interpretation belongs to §7G. |
| NHD-M25-DIAR | 3808–3810 | Diarization: parallel voice streams during overlap/interruption assessed independently. |
| NHD-M19A-11 | 3052 | Voice summon/silence/dismiss/off. |

### F.2 New ideas from the 2026-09-16 discussion — status `assistant_summary`, NOT Ness-recorded decisions until Ness confirms in his own words
| Working ref | Idea | Compatibility finding |
|---|---|---|
| V-NEW-1 | Complete final answer generated before speaking; speech = playback of existing text | **Compatible with, but NOT decided by,** the handoff package: §2 step 12 says only the validated final answer is surfaced; it says nothing about playback timing. No rule exists. (v0_1 said "supported" — too strong.) |
| V-NEW-2 | Unplayed remainder preserved as generated-not-heard | No rule exists; compatible with §0B |
| V-NEW-3 | Meaning Engine (§7G) decides remainder relevance | Consistent with DUMB/SMART: relevance is §7G's, never BOP's |
| V-NEW-4 | Resolving "that bit" to the spoken position | Position exists (NHD-M25-BOP-VI); resolving a reference to it is interpretation — §7G/§7D; genuinely new mechanics |
| V-NEW-5 | How long the remainder stays available | Open; handoff §3 forbids surfacing stale analysis after the conversation moved on |
| V-NEW-6 | Hebrew / English behavior | No rule found; handoff §3 allows the light model to change language; open |
| V-NEW-7 | Barge-in during a warm acknowledgment (handoff §4) vs during the final answer | **Claude's own question, `assistant_proposal`** — Ness did not raise it. Listed so it is not mistaken for something Ness said. |

**Three states that must never collapse:** generated text (exists in store) · audio played (BOP physical fact) · content known to have reached Ness (never a fact; at most a §7G reading). Playback is never proof of hearing or understanding. Identity and access: reuse §25/§26 and B-INT-5; nothing new.

---

## PART G — STRANDED DECISIONS RECOVERED SO FAR (Pass 4 preview)

### G.1 Room initialization — 2026-07-21
Source: Claude conversation "Design work map v1.3 → v1.4 update," working record §4.1, labeled "DIRECT NESS DECISIONS — PRESERVED IN THIS WORKING RECORD — NOT YET AN ACCEPTED A19 PACKAGE," provenance note "preserved exactly as Ness supplied them."

| ID | Decision (as recorded) | Status | Answers | Where still shown open |
|---|---|---|---|---|
| NHD-WR-20260721-1 | When a new room is created, Ness or N.H may choose: blank, built from memories, or mixed. | `ness_decision` — carried by accepted A19-RS v1_2 (PACKAGE_COMPLETE for its standalone scope, 2026-09-17) | NHD-M19C-3, -4 | Master §19C line 3079–3080; Map v1.6 line 638 |
| NHD-WR-20260721-2 | Ness's direct choice overrides N.H's automatic choice. | `ness_decision` — carried by accepted A19-RS v1_2 | NHD-M19C-4 | same |
| NHD-WR-20260721-3 | A clear voice command changes how the room begins immediately, without another confirmation. | `ness_decision` — carried by accepted A19-RS v1_2 | NHD-M19C-5 | same |

Repo check (2026-09-16, historical): at that time no file in the **GitHub repository** contained these three decisions. Superseded the same day and again on 2026-09-17 — see below.

**Correction (same day, after Ness uploaded the Unreal Engine 5 package):** the three decisions ARE carried in a file — `NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` (2026-08-14) §2.2 "Existing direct Ness room-start decisions," lines 90–103, in the same wording. That file was missing from GitHub until Ness pushed it on 2026-09-16 (commit `ca5713f`; bytes match the recorded hash). So the decisions are **not chat-only**; they are file-recorded in a non-authoritative package that is now in the repo. Status stays `ness_decision`. **Update 2026-09-17:** the three decisions are now carried by the accepted standalone package **A19-RS** — `NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` (136 lines, 15,053 bytes, SHA-256 `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0`), closure record `NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (156 lines, 10,976 bytes, SHA-256 `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e`) — **`PACKAGE_COMPLETE` for its accepted standalone room-start policy scope only.** The three starting forms remain options, not a selected default; all twelve A19-RS dependencies remain open; Master §19C questions 1 and 2 remain open, and §19C/Map v1.6/Companion still show questions 3–5 as open (future versioned currentness work). No Master/Map integration or implementation occurred. Ness is not asked to decide them again.

### G.2 The question-and-answer tool is retired — 2026-09-16
Source: Ness, directly, in this conversation (voice): the system that ran the design question-and-answer rounds (the tool the intent excerpts were written "for," and that produced the H/N-numbered answers) is no longer in use — "I moved on about it. I don't want to use it anymore. Only the answers are important."

| ID | Decision (as stated) | Status | Effect on the index |
|---|---|---|---|
| NHD-WR-20260916-1 | The question-and-answer tool is retired by Ness's choice. Its answers remain valid evidence. **That is the whole decision.** | `ness_decision`, no package | Nobody should ask Ness to restart the tool. |
| (index handling — `assistant_proposal`, not Ness's decision) | Claude proposes to treat `HISTORICAL_ANSWERS.md` (+ provenance JSON) and the three intent-excerpt files as the surviving evidence, and to stop treating the full source `NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_1.md` as something that must be fetched. Ness has not said this; whether he still wants the full source file is his call. (v0_1 wrongly folded these two conclusions into the decision row.) | `assistant_proposal` | — |

**Kept separate on purpose:** Master §13 "THE LIVE LOOP [DESIGNED — not built]" (line 2911) is the N.H design concept that live conversation is itself an input. It is NOT the retired tool and is NOT affected by this decision.

### G.3 Implementation tool — 2026-09-16
| ID | Decision (as stated) | Status | Notes |
|---|---|---|---|
| NHD-WR-20260916-2 | Ness confirmed directly in writing to ChatGPT on 2026-09-16: **"I want Cursor to do the building of N.H. Not Claude Code, not ChatGPT."** | `ness_decision`, no package. This written confirmation resolves the earlier voice-transcription conflict. | This chooses who will build N.H. It does not authorize implementation to begin; the separate design-completion and building-permission requirements remain unchanged. |

---

## PART H — LABELING SURVEY OF THE 81 ACCEPTED FILES (input to Pass 2)
| Existing style | Files (examples) | Refs |
|---|---|---|
| `A6-1…A6-11` | Bundle 4 completion candidate; Bundle 2 completion | 30 |
| `B16-0…B16-4` | B16 package; B9 package | 57 |
| `A13.1…`, `A3.1…A3.5` | Bundle 6 policy / mechanical / closeout | 76 |
| `Decision 1…N` | Bundle 2 completion, B24 v7, Map v1.6 | 27 |
| `D1…D9` | A7, Bundle 5 closeout, B24 (Defaults-drift items) | 50 |
| `H####` / `N###` | HISTORICAL_ANSWERS.md, continuation context | 22 unique |
| Section numbering only, **no decision labels** | 69 of 81 files | — |
| No numbering at all | B10 v1_0, B-HOLD v1_0 | 2 |

Four incompatible styles coexist; ~85% of accepted files have no per-decision label. Pass 2 assigns `NHD-` IDs per Rule 3 without touching any file.

---

## PART I — COVERAGE STATEMENT FOR v0_1
**Done in this version:** identifier scheme; Master section register (all 48 top-level sections); §11 register (35 items); §19 register (A/C/D/E); §14 register; voice settled-vs-new table; one stranded-decision set (July 21); labeling survey.

**Not yet done (next passes):**
- Pass 1b: per-paragraph extraction inside §0–§0B, §7D–§7R, §13, §16, §22–§26 (the bulk of the Master's settled rules — several thousand lines).
- Pass 2: DONE at package level (Part L). Pass 2b: decision-by-decision rows inside each source — pending.
- Pass 3: DONE (Part N) — see N.8 for the small remainder.
- Pass 4: DONE (Part O), within the limit that only Ness–Claude chats are searchable.
- Pass 5: DONE (Part P).
- Pass 2b (decision-by-decision rows inside each accepted source) remains the one open pass; it follows scheme approval.

**No files were edited, replaced, uploaded, or merged. No code written. No disk state changed.**

---

## PART L — PASS 2: ACCEPTED PACKAGE REGISTER (`04_ACCEPTED_STANDALONE_DESIGNS/` — 81 files when surveyed on 2026-09-16; **85 after the AIC/UDOK pushes the same evening; 96 after the 2026-09-17 cleanup and the three A19 receipts** — the accepted sources formerly misplaced in `05_ACTIVE_CANDIDATE/` were moved in on 2026-09-17, see M.3)

### L.0 How acceptance is actually recorded in this repo (verified on the files)
Every accepted package follows one chain. The index records each link separately and never collapses them:
1. **Source candidate** — its internal status wording stays frozen at "CANDIDATE — NOT ACCEPTED" forever. That wording is NOT evidence the package is unaccepted.
2. **ChatGPT PASS** on the actual source bytes — recorded inside **most** receipts. **Not universal:** the A31 closure record and the A4 and B1 acceptance records contain no explicit PASS statement (they record Ness's acceptance and refer to the audit without the word PASS). This does not change their accepted status; it means the chain description varies by record. (v0_1 stated this as universal — corrected.)
3. **Ness's explicit acceptance** — recorded inside the receipt, dated.
4. **Closure receipt / acceptance record** — the file that carries 3 (and usually 2) + the source SHA-256. **Many** receipts carry a "DELIVERED, AWAITING INDEPENDENT AUDIT" status for their own audit; **not all do** — e.g. the A4 acceptance record and the AIC and UDOK closure records state no such condition. Bundle closeouts later re-verify the receipt chain for their own bundle (e.g. Bundle 5 closeout §10: "Ness acceptance recorded in every receipt — verified. ChatGPT PASS recorded in every receipt — verified." — a statement about Bundle 5's eleven receipts only). (v0_1/v0_2 stated the awaiting-audit condition as universal — corrected.)

**Index rule:** a package is `accepted_package` when link 3 (Ness's explicit acceptance) is present in a committed receipt; link 2 is recorded where the receipt states it. "Receipt's own audit: awaited" is recorded as a separate field, not as doubt about the acceptance. `accepted` never means `built`; every source here says NOT BUILT / NOT IMPLEMENTED.

### L.1 Package register
Columns: ID prefix · package · bundle · accepted source (version, folder) · acceptance evidence (record file, Ness acceptance date, PASS-on-source) · existing internal labels · plain meaning (index wording unless quoted).

| ID prefix | Package | Bundle | Accepted source | Acceptance evidence | Labels in file | Plain meaning |
|---|---|---|---|---|---|---|
| NHD-A1-BLK | A1 missing-source blocker | 1 | blocker record v1_0 (record only) | record dated Jun 30 / Jul 7 2026; historical blocker preserved, no longer blocking | section nos. | The original story-bearing gold cases can't be found; recorded honestly, replacement path chosen instead |
| NHD-A1 | A1 replacement story-bearing gold set (Engine C) | 1 | unpinned content v1_3 (04) | acceptance record v1_1 + closure record v1_0, Jul 11 2026, PASS | section nos. | The new set of test cases Engine C will be judged against; content, not yet pinned/sealed |
| NHD-A29 | A29 hold-until-enough policy | 1 | v1_0 (04) | closure record v1_0, Jul 7 2026, PASS | section nos. | When N.H doesn't have enough to read something well, it waits rather than guessing; chooses no durations |
| NHD-SLF | Story-Layer firmness scale | 1 | v1_0 (04) | closure record v1_0, Jul 7 2026, PASS | section nos. | Six firmness labels for story-layer material (Option B per Ness) |
| NHD-A31 | A31 grounded-enough threshold | 1 | v1_0 (04) | closure record v1_0, Jul 7 2026 (no explicit PASS wording in the record) | section nos. | Four labels for "grounded enough"; no numeric threshold created |
| NHD-B9 | B9 retry state architecture | 1 | v1_0 (04; the duplicate 05 copy was deleted 2026-09-17) | closure record v1_0, Jul 6 2026, PASS | uses B16-n refs | "Try again safely" — bounded, idempotent, no endless retry |
| NHD-B10 | B10 reread operation identity & recovery | 1 | v1_0 (04) | closure record v1_0, Jul 6 2026, PASS | **none** | "Read this again later, but do not duplicate" |
| NHD-BHOLD | B-HOLD hold-until-enough lifecycle | 1 | v1_0 (04) | closure record v1_0, Jul 6 2026, PASS | **none** | The "waiting shelf" — holds items without judging them |
| NHD-B11 | B11 active writable batch architecture | 1 | v1_4 (04) | closure record v1_0, Jul 6 2026, PASS | section nos. | How a new writable batch sits beside the sealed 5,521-root batch; must precede any new root batch |
| NHD-B16 | B16 quarantine → promotion evidence architecture | 1 | v1_0 (04) | closure record v1_0, Jul 6 2026, PASS | `B16-0…B16-4` | The safe gate that lets quarantined output become production, with evidence |
| NHD-B24 | B24 validator-first model boundary & benchmark | 1 | v7 (04) | package-complete record v1_0, Jul 3 2026, PASS | `Decision N`, `D1…` | The validator sits between any model and memory; benchmark rules; ties to dual-model handoff |
| NHD-B9W | B9 retry values wiring into B9/B10/B-HOLD/B24 | 1 | v1_4 (04; v1_0–v1_3 historical, in 99 since 2026-09-17) | closure record v1_0, Jul 12 2026, PASS | section nos. | Ness-decided retry values carried into the four consumers |
| NHD-B1CN | Bundle 1 B9/B10/B-HOLD coordination note | 1 | v1_0 (04) | closure record v1_0, Jul 6 2026, PASS | section nos. | Boundaries between the three so they never double-act |
| NHD-A25 | A25 reread-mode assignment policy | 1 | v1_2 (04; v1_0–v1_1 historical, in 99 since 2026-09-17) | closure record v1_0, Jul 11 2026, PASS | section nos. | Ness-decided reread modes; assignment producer left open |
| NHD-A25B10 | A25 → B10 reread-mode connection | 1 | v1_2 (04; v1_0, v1_1 also in 04 as historical provenance) | closure record **v1_1** (narrow correction of receipt v1_0), Jul 12 2026, PASS | section nos. | The governed link from mode policy to reread operation |
| NHD-A25MR | A25/B10 manual-reread compatibility | 1 | v1_0 (04) | closure record v1_0, Jul 12 2026, PASS | section nos. | Manual reread when no truthful assignment exists |
| NHD-BU1 | Bundle 1 normalization & closeout | 1 | v1_4 (04) | acceptance record v1_0 (Jul 7) + closure record v1_0 (Jul 12 2026), PASS | section nos. | Consolidates A1, A25, A29, A31, firmness, B9, B10, B11, B16, B24, B-HOLD; B-CYCLE-1/8 named as Bundle 8 |
| NHD-A4 | A4 relevance-mode declaration policy | 2 | v1_1 (04 since 2026-09-17; accepted via Bundle 2) | acceptance record v1_0, Jul 9 2026 (no explicit PASS wording in the record) | — | Option C: one shared relevance language + mandatory per-component declarations |
| NHD-B1 | B1 context retrieval parameter architecture | 2 | v1_0 (04 since 2026-09-17; accepted via Bundle 2) | acceptance record v1_0, Jul 9 2026 (no explicit PASS wording in the record) | — | Two always-separate retrieval channels; no values chosen |
| NHD-BU2 | Bundle 2 formal relevance declarations & completion (carries A4, B1, B26, B-INT-1) | 2 | v1_1 (04) | acceptance record v1_0 (Jul 9) + closure record v1_0 (Jul 12 2026), PASS | `Decision N`, `A6-n` refs | Ness's relevance/labeling/strictness decisions; B26 retrieval-failure (fail closed, no degraded continuation); B-INT-1 per-component §7R instantiation |
| NHD-BU3 | Bundle 3 story layer / person-boxes / themes / clashes (A5, A9, A14, B2, B3, B4, B19, B23, B25, B28, B-AFFIRM) | 3 | v1_2 (04 since 2026-09-17; previously misplaced in 05) | acceptance record v1_0, Jul 10 2026 | section nos. | Clash never closes; six append-only theme actions; B-AFFIRM narrowed to reading accept/reject |
| NHD-BU4 | Bundle 4 living state / computed view / action / world model (A6, A8, A18, B5, B6, B8, B27, B-INT-9) | 4 | v1_3 (04 since 2026-09-17; previously misplaced in 05) | acceptance record v1_0, Jul 11 2026, PASS | `A6-1…A6-11` | Eleven Living-State-Web decisions; action-risk mapping; layered world model (nine distinctions); 21 schemas; 17 record structures |
| NHD-A7 | A7 privacy, influence & third-party use policy | 5 | v1_1 (04) | closure record v1_0, Jul 13 2026, PASS | `D1…` refs | The concept-and-policy layer of the privacy system |
| NHD-A26 | A26 identity ↔ Personal-Mode relationship policy | 5 | v1_1 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | N.H may recognize Ness and still stay outside Personal Mode |
| NHD-A16 | A16 TSC archive event-name adoption policy | 5 | v1_0 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | Ness accepted the proposed active TSC archive-event name |
| NHD-A15 | A15 BOP acoustic condition-notes amendment policy | 5 | v1_1 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | Five measurable recording conditions BOP may note, physically only |
| NHD-B7 | B7 privacy enforcement & protected handling architecture | 5 | v1_3 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | The machinery under A7's promise |
| NHD-B15 | B15 TSC transactional store architecture | 5 | v1_4 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | The box the live session lives in |
| NHD-BINT4 | B-INT-4 TSC authorization / promotion / interrupted continuation wiring | 5 | v1_3 (04) | closure record **v1_1** (corrected), Jul 13 2026, PASS | section nos. | Connects permission machinery to the TSC lifecycle; authorization and promotion stay separate |
| NHD-BINT5 | B-INT-5 identity ↔ Personal-Mode access wiring | 5 | v1_5 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | "Who is present and what may be shown" wired to access |
| NHD-BINT6 | B-INT-6 §7Q-first / SACL-second output chain wiring | 5 | v1_3 (04) | closure record v1_0, Jul 13 2026, PASS | section nos. | One continuous output path; privacy before SACL, always |
| NHD-BINT7 | B-INT-7 initial Ness voice-profile enrollment bootstrap wiring | 5 | v1_1 (04) | closure record v1_0, Jul 14 2026, PASS | section nos. | How the first voice profile is captured honestly, incl. interrupted sessions |
| NHD-BINT8 | B-INT-8 connection capability waiting & acceptance routes wiring | 5 | v1_2 (04) | closure record v1_0, Jul 15 2026, PASS | section nos. | A possible relationship between two preserved things waits for Ness's route |
| NHD-BU5 | Bundle 5 final consolidation & closeout | 5 | v1_1 (04) | closure record v1_0, Jul 15 2026 (receipt awaiting audit) | `D1…` refs | Verifies the whole Bundle 5 receipt chain on the bytes |
| NHD-BU6P | Bundle 6 policy decisions | 6 | v1_0 (04) | closure record v1_0, Jul 13 2026, PASS | `A3.1…A3.5`, `A13.1…` | Ingest / provenance / research / creation / personal-learning policy answers |
| NHD-BU6M | Bundle 6 mechanical design | 6 | v1_4 (04) | closure record v1_0, Jul 13 2026, PASS | `A3.n`, `A13.n` | Activation source and lifecycle mechanics for the Bundle 6 components |
| NHD-BU6 | Bundle 6 final consolidation & closeout (A3, A10, A11, A12, A13, A27, A28, A30, A32, B12, B13, B14, B17, B18, B20, B21, B22, B-INT-2, B-INT-3) | 6 | v1_2 (04) | closure record **v1_1**, Jul 13 2026 | `A3.n`, `A13.n` | Bundle 6 fully closed; A32 point-back recorded, not integrated |
| NHD-A17 | A17 Wonder-to-memory policy | 7 (A19 area) | v1_0 (04) | closure record v1_0, Jul 18 2026, PASS — **formal closure awaits audit PASS of the record itself (§7)** | section nos. | Whether/how Ness-selected Wonder material may move toward normal memory |
| NHD-A22 | A22 phone-side modes policy | 7 | v1_1 (04) | closure record v1_0, Jul 18 2026, PASS | section nos. | Behavior policy of the phone-side modes |
| A19-RS (package ID; no `NHD-` form) | A19-RS room-start policy package — carries NHD-WR-20260721-1/2/3 | 7 (A19) | v1_2 (04) — `NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` (136 lines, 15,053 bytes, SHA-256 `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0`) | closure record v1_0 — `NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (156 lines, 10,976 bytes, SHA-256 `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e`) — Sep 17 2026, ChatGPT PASS on source bytes, Ness "I accept it", record audited PASS: **PACKAGE_COMPLETE for the standalone room-start policy scope only** | section nos. | A new individual room may begin blank, built from memories, or mixed; Ness or N.H may choose; Ness's direct choice overrides; a clear voice command changes it immediately without another confirmation. Twelve dependencies open; Master §19C Q1–2 open |
| A19-CI (package ID; no `NHD-` form) | A19-CI chat-interface policy package — carries NHD-WR-20260916-3 | 7 (A19) | v1_1 (04) — `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` (180 lines, 18,830 bytes, SHA-256 `7bb426d211685ba9f96b2194163bcbb6750365ed689ef19b0614f5b217288451`) | closure record v1_0 — `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (191 lines, 14,182 bytes, SHA-256 `8f22b0a1dd7b4393934af873993ef797437e8d312164b1676caecab2e240f18c`) — Sep 17 2026, ChatGPT PASS on source bytes, Ness "I accept A19-CI v1_1.", record accepted by Ness: **PACKAGE_COMPLETE for the standalone ordinary-chat policy scope only** | section nos. | Eight-part ordinary-chat decision; checkpoint §12.1/§12.2 and the four §18.1 layout items superseded; §§13–17 card material not cancelled or imported; colours undecided; extra features later; twelve dependencies open |
| NHD-A2 | A2 telling-object identity | (standalone) | v1_8 (04) | package-complete record v1_0, Jul 1 2026, PASS | section nos. | Identity of the "telling object"; Master integration pending; do not reopen |
| NHD-AIC | Authority Integrity Control Plane — mechanical design (Addition 1) | post-Bundle-6 additions | v1_10 (04 — pushed to GitHub 2026-09-16, commit b45b98d) | closure record v1_0, Aug 20 2026, `PACKAGE_COMPLETE` for standalone mechanical-design scope only | (Pass 2b) | The control plane that keeps authority decisions intact across components |
| NHD-UDOK | Unified Durable Operation Kernel — mechanical design (Addition 2) | post-Bundle-6 additions | v1_9 (04 — pushed to GitHub 2026-09-16, commit b45b98d) | closure record v1_0, Aug 21 2026, `PACKAGE_COMPLETE` for standalone mechanical-design scope only | (Pass 2b) | One durable operation kernel underneath the retry/hold/reread machinery |
| NHD-LDMH-P | Live dual-model handoff bundle placement & dependency record | 7/8 | v1_1 (04 since 2026-09-17) | acceptance record v1_0, Jul 13 2026, PASS | section nos. | Bundle 7 designs the model roles; Bundle 8 builds the connected handoff; no model chosen |

### L.2 Findings from Pass 2 (facts, not judgments)
- **Placement ≠ status (historical finding, resolved 2026-09-17):** when surveyed, the accepted Bundle 3 (v1_2) and Bundle 4 (v1_3) sources lived in `05_ACTIVE_CANDIDATE/` while their acceptance records lived in `04_ACCEPTED_STANDALONE_DESIGNS/`. On 2026-09-17 they — and the other misplaced accepted sources listed in M.3 — were moved into `04/` by 100%-similarity renames. Folder placement never created or removed acceptance; it now simply matches it.
- **Frozen "NOT ACCEPTED" wording in every accepted source.** Any tool or model that reads a source file alone will conclude it is unaccepted. Only the receipt proves acceptance. This is the second mechanical reason settled things get re-asked.
- **Many receipts record their own audit as awaited; some do not** (A4 acceptance record; AIC and UDOK closure records; others). Bundle closeouts re-verify chains for their bundle. No file records "receipt audited: PASS" per individual receipt. The index records this per record, as a field, not as a problem.
- **Two accepted sources carry no numbering at all** (B10 v1_0, B-HOLD v1_0). Rule 3 assigns document-order IDs for them.
- **Historical versions kept beside accepted ones** (A25→B10 v1_0/v1_1 in 04, retained by their receipt; B9 wiring v1_0–v1_3 and A25 v1_0–v1_1 were in 05 when surveyed and have been in 99 since the 2026-09-17 cleanup). The receipt names the accepted version; the others are provenance. Index cites only the receipt-named version as `accepted_package`; the rest as `superseded`.
- **Bundle 7 accepted standalone packages (as of 2026-09-17): A17, A22, A19-RS, A19-CI** — all narrow policy packages in the A19 area; A19 itself is not complete and otherwise has checkpoints only (Pass 3). **Bundle 8 has no accepted packages.**

### L.3 Pass 2 coverage statement
Done: package-level register for all 81 files (every source paired to its record; dates and PASS presence read from the records). **Not done:** decision-by-decision extraction inside each source (the `NHD-<pkg>-<n>` rows). That is Pass 2b, package by package, starting with the eleven `A6-n`, five `B16-n`, and the `A3.n` / `A13.n` sets because their numbers already exist.

---

## PART N — PASS 3: THE SEPTEMBER MATERIAL AND OTHER POST-JULY RECORDS

### N.0 Status note for this part (status is per section, not blanket)
- **N.1, N.2, N.4:** recorded under the **A19 working method Ness approved** (checkpoint v1.2 §1) or as direct dated answers with Ness's own words quoted → `ness_decision`. By the method's rule 6, saving is not acceptance, adoption, Master/Map integration, or permission to build.
- **N.3:** answers produced through the now-retired Q&A tool, preserved verbatim → `ness_decision` (evidence status per NHD-WR-20260916-1); not the A19 method.
- **N.5:** a Ness-approved strategic-direction package (2026-08-04) → `ness_decision` for the direction; its five additions are not designed as packages except where L.1 records AIC/UDOK acceptance.
- **N.6:** Ness's stated intent → `ness_intent`, not decisions.
- **N.9:** the ten-point direction and §2.2 → `ness_decision`. **Direction-accepted 2026-09-17: NHD-UE5-1 (§1's ten points and §49 only), formal receipt `NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` (239 lines, 22,212 bytes, SHA-256 `a5d6735f867d1c8680ee09ecf1bc9b24477469bdd6cd2c719444916eddfad7eb`), PASS.** All blueprint sections (§§5–8, §§11–14, §§25–39) remain `assistant_proposal`; the source stays a mixed-status document and is never `accepted_package` or `PACKAGE_COMPLETE`.
- Nothing in Part N is `accepted_package` unless L.1 says so, and nothing is integrated into Master V10.

### N.1 A19 Human-Experience Decisions Checkpoint v1.2 (2026-09-15, 818 lines) — `ness_decision`
| ID | § | Decision (as recorded) | Still open per the checkpoint itself |
|---|---|---|---|
| NHD-A19CP-3.1 | 3.1 | Initial entry into Ness's World is **not** a literal 3D door; it is an icon-based loading/transition. Corrects the earlier prototype. The physical door survives only in the Create-New-World path (§7). | loading-screen visuals, icon identity, timing |
| NHD-A19CP-3.2 | 3.2 | Entry icon: present during loading; hover → white aura; activation deliberate, not automatic; click starts transition; zoom and light may be used. | same |
| NHD-A19CP-4.1 | 4.1 | Main category space = **B, centered hub** (not open map, not free canvas, not hub-less). Context-sensitive reorganization still allowed inside it. | what the center is called and represents; scale; movement |
| NHD-A19CP-4.2 | 4.2 | The sample image was accepted for **structure only**; the dark-fantasy background is **not** adopted. | background/environment |
| NHD-A19CP-5.1 | 5.1 | The items are called **Categories** (not "doors") in this part. | — |
| NHD-A19CP-5.2 | 5.2 | Category panels have image + icon, feel somewhat 3D, customizable identity; Ness and N.H may both customize. | shape, depth, image treatment, icon placement, editing controls |
| NHD-A19CP-5.3 | 5.3 | Categories are visually connected (lines, custom lines, color, other forms) to show organization/relationships. | meaning of colors/line types/motion |
| NHD-A19CP-5.4 | 5.4 | The category structure is living: N.H may reorganize by context/connection/relevance, informed by nightly research and live use. **Design intention, not implemented.** | — |
| NHD-A19CP-6 | 6 | Selecting a category does **not** enter a final world; it opens panels of **preset experiences** (worlds, situations, stories, made / in-the-making). | how presets open; status language; count; ordering; return |
| NHD-A19CP-7 | 7 | **Create New World** is one preset option → a real spatial door → a **blank white room** as the creation starting space. Not the initial entry mechanism. | door appearance; room behavior; creation tools; how N.H appears there |
| NHD-A19CP-8 | 8 | Four earlier "blueprint-like" options: **UNRESOLVED / DEFERRED** — possibly chat-interface items; not to be invented or placed here. | ownership must be checked in interface files |
| NHD-A19CP-12.1 | 12.1 | Chat interface direction = the prototype `NH_interactive_2D_ultrawide.html` (SHA-256 `ca7e1e90…`, 24,266 bytes). **Status: `superseded`** — Ness later explicitly corrected that he did **not** approve that prototype as the chat interface (correction reported by ChatGPT's audit of 2026-09-16 and consistent with Ness's instruction to Claude the same day). The checkpoint v1.2 text still shows the selection (frozen); the supersession is recorded in accepted A19-CI §6. | superseded per accepted A19-CI v1_1 (2026-09-17) |
| NHD-A19CP-12.2 | 12.2 | Three-area ultrawide composition (deck left / conversation center / context right). **Status: `superseded`** together with 12.1. Replaced by NHD-WR-20260916-3 (below). The v0_1 question "does full-window chat keep the side areas?" is **withdrawn** — it reopened something Ness had already corrected. | — |
| NHD-WR-20260916-3 | — | **Ness's current chat-interface decisions** (stated in his 2026-09-16 instruction; confirmed by ChatGPT's record): normal scrolling conversation · ChatGPT-like basic behaviour · full-window PC chat, with smaller forms when appropriate · centred conversation area · Ness's messages on the right in rounded boxes · N.H's replies on the left as plain text, away from the far-left edge · colours undecided · extra features later. `ness_decision` — carried by accepted **A19-CI** v1_1 (PACKAGE_COMPLETE for its standalone ordinary-chat policy scope, 2026-09-17; closure record v1_0). On PC the chat *is* full-window (baseline), with a smaller presentation when appropriate. | colours; the "extra features"; the twelve A19-CI dependencies |
| NHD-A19CP-13 | 13.1–13.4 | **Card language:** a card is a general human-facing object for any point of interest (not only ideas); a card **points into** N.H and never becomes a second copy; moving/recoloring/grouping/returning a card never rewrites a root, reading, telling, Person-Box, or accepted connection; cards reach memory **by reference** and preserve object-type distinctions; category cards are routes/views, not duplicate stores; the Idea Deck is not a second Creation Store. | production card-type registry; persisted schema; view generation/sync |
| NHD-A19CP-14 | 14.1–14.2 | Idea Cards keep Bundle 6 provisional-creation rules (provisional ≠ confirmed; time/repetition/retrieval never confirm). For promising unfinished ideas: natural conversation **plus** an "Idea in progress" card that stays visibly provisional. | — |
| NHD-A19CP-15 | 15.1–15.3 | Ness may summon/expose a card in several natural ways (no single forced method; `/idea`, `/deck`, `/place` are examples, not frozen); cards are movable 2D conversational objects; returning a card to a deck deletes/changes/confirms nothing. | final command wording |
| NHD-A19CP-16 | 16.1–16.4 | Deliberate spatial placement beside conversation text is meaningful; the association must be remembered; placement creates context, **not automatic truth**; screenshot/visual-placement record boundary. | snapshot storage/reconstruction mechanism |
| NHD-A19CP-17 | 17.1–17.2 | Each card has a meaningful 2D icon; **N.H creates the icon.** | icon-generation tool/provider and its permission wiring |
| NHD-A19CP-18 | 18.1–18.3 | §18.1 lists the prototype behaviours as a baseline. **Split after Ness's correction:** (a) the *layout* items in that list — wide three-column composition, deck on the left, central chat, right-hand inspector — are the **superseded** chat layout (see 12.1/12.2 → NHD-WR-20260916-3) and are NOT a current reference; (b) the *card* items — draggable cards, clicking a message to choose the target, placing a card beside it, direct show/place/return commands, visible context-link explanation, remembered placement, return-to-deck ≠ deletion, underlying status preserved — are recorded independently in §13–§17 and keep their checkpoint status. §18.2 (prototype-only vs real N.H) and §18.3 (bundle ownership) stand. | Whether the card behaviours belong inside the new full-window chat is **not stated** by Ness's correction — open, Ness |
| NHD-A19CP-OPEN | 9, 19 | The checkpoint's own two open lists are preserved as `master_open`-equivalent for A19 (entry/return details, hub naming, category visuals, category→presets transition, presets, Create New World interior, plan Areas 2–7, card registry/schema/sync, Bundle 8 chat wiring, Meaning-Engine integration). | — |

### N.2 `NH_DESIGN_ANSWERS.md` — three answers dated 2026-09-14 — `ness_decision` (authority: Ness's own words quoted in the record, originating task `01a0a10f-…`)
| ID | Answer | Scope stated in the record |
|---|---|---|
| NHD-DA-20260914-1 | Room-design preview: default is **enter and explore** the proposed room before choosing; an image only if Ness asks in that case ("נכון"). | preview presentation only; no world/simulation entry, permission, layout, or memory effect |
| NHD-DA-20260914-2 | Simulated familiar person: **resemble the real person as closely as possible** ("דומה לו ככל שאפשר"), adapted to Ness's request per case. | visual resemblance only; no behavioral accuracy, no new photo/voice permission, no simulation start |
| NHD-DA-20260914-3 | General principle: N.H should be **flexible**, learn from Ness's requests/corrections/context, have multiple ways to act and present — applied throughout Wonder. **Exceptions:** the mini-agent and anything already fixed by explicit decisions. | product direction; no implemented capability, no learning mechanism chosen, no new permissions |

### N.3 `HISTORICAL_ANSWERS.md` — 22 preserved answers (H = earlier record, N = later; evidence review 2026-09-14; original timestamps not preserved) — `ness_decision`
Verbatim text stays in the file; the index points to it. Mapping to the Master's open lists (Part D):

| ID | Topic (editorial label in the file) | Addresses | Note |
|---|---|---|---|
| NHD-N673 / NHD-H1742 | full context of each correction | §19C additional: "full context of each correction preserved" | "Every time, always" — answered |
| NHD-H1546 | own direct door | §19C additional: "own direct door per recent space" | **The recorded answer is generic ("not specifically… I want N.H to know me so well…") and does not settle the door question.** Same text also appears under H1738. Treat as `evidence_missing` for the specific question. |
| NHD-H1738 | manually placed objects stay fixed | §19A-6 area | same generic text as H1546 — does not settle it |
| NHD-H1739 | motion-sickness feature | §19D-2 | explicitly **not wanted** |
| NHD-H1740 | emotional overload handling | §19D-2 | "wait for this specific setting" — deferred by Ness |
| NHD-H1744 / H1745 / H1747 | capture begins / what is captured / what stays transient | §19E-2 (camera/VR front doors) | per-device approval; automatic only on approved devices; N.H decides what's useful to keep; Ness can override/remove |
| NHD-H1749 | voice and gesture combine | §19D-2 | act when clear, ask when unsure |
| NHD-H1750 | tracking failure | §19D-2 | severity-based, tell Ness, ask when uncertain |
| NHD-H1752 → **superseded by** NHD-H1753 | evidence reconstruction | §19A-13 area (replay vs invention) | rebuild from real evidence; **leave blank and ask** rather than invent |
| NHD-H1754 | replay vs simulation difference | §19A-13 | N.H reminds which it is, inside the experience |
| NHD-H1756 | visibility of rest of world | §19D-1 | adaptive; Ness can override |
| NHD-H1757 | full learning history | §19C additional: "learned-pattern display" | N.H chooses what to show first; full history always available |
| NHD-H1759 | branching and reset | §19D-1 | permanent automatic preservation of the whole simulation path; return to any point without saving first. (Continuation context: the auto-resume-vs-checkpoint choice remains **undecided**.) |
| NHD-H1760 | challenging one learned pattern | §19C additional: "challenging one learned pattern" | preserve exact correction + context; apply when clear, ask when unsure |
| NHD-H1762 → **superseded by** NHD-H1763 | time controls / simulation authority | §19D-1 | N.H has standing default permission to act within simulation space across all simulation features; Ness can open/close/lock that authority at any time |
| NHD-H1765 | exact backtracking order | §19C additional: "backtracking order" | situational; Ness chooses or delegates; N.H has broad default permission for the return path |

Two later "question resets" (H2590, H2663) are preserved as history and do not erase these answers (file header).

### N.4 `00_CONTINUATION_CONTEXT.md` (2026-09-15) — transfer context; carries these standing facts
Unreal Engine 5 is the selected World/Wonder runtime direction (not implemented; direction-accepted 2026-09-17 as NHD-UE5-1 — see N.9) · Wonder is being designed directly, section by section; Hebrew in conversation, English in records · A17 accepted, formal closure awaits the receipt audit · **AIC and UDOK receipts** establish acceptance of their exact source bytes for limited scopes · **Memory Fabric remains inactive/unaccepted** · H1753 replaces H1752, H1763 replaces H1762.

### N.5 `NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` (2026-08-04) — `ness_decision` (approved strategic direction; not designed as packages; not integrated)
| ID | Addition | Later status per continuation context |
|---|---|---|
| NHD-FFA-1 | Authority Integrity Control Plane (AIC) | mechanical design v1_10 accepted Aug 20 2026, standalone scope only — package and receipt now on GitHub (2026-09-16) — see L.1 NHD-AIC |
| NHD-FFA-2 | Unified Durable Operation Kernel (UDOK) | mechanical design v1_9 accepted Aug 21 2026, standalone scope only — package and receipt now on GitHub (2026-09-16) — see L.1 NHD-UDOK |
| NHD-FFA-3 | Provenance-First Multi-Index Memory Fabric | mechanical design v1_4 candidate (Aug 25 2026, 2,108 lines) now on GitHub in `05_INACTIVE_CANDIDATE/` (2026-09-16) — NOT AUDITED, NOT ACCEPTED; inactive |
| NHD-FFA-4 | Bounded Self-Healing Execution Laboratory | no later record found |
| NHD-FFA-5 | Governed Capability Registry and Sandboxed Tool Forge | no later record found |
Staged plan in the package: record now → design in dependency order → whole-system wiring → later implementation.

### N.6 Intent excerpts (Ness's words, from the retired tool's input file; evidence of record per NHD-WR-20260916-1) — status `ness_intent`
| ID | Family | Core intent (file's own summary) |
|---|---|---|
| NHD-INT-A | Music & media | Experience music/media while talking with N.H; N.H understands exact musical moments (beats, drops, vocal changes); personal media meaning; media ↔ creative-project links; media history; a service such as Spotify stays separately authorized; "must never be reduced to simple playback." |
| NHD-INT-B | Thought branches & simulation | Actual conversation/thought structure; returning to old branches; several branches alive; branch view; unsent typing; temporary preparation; prediction must not distort conversation; branches ↔ memory. |
| NHD-INT-C | Camera / GPS live help | Deliberate live session, not silent surveillance; privacy of other people and places; location is sensitive; no false certainty. |
| NHD-INT-D | Creation workspace | Different from the existing Creation concept; draft is not decision; artifact provenance; working with existing files; code work; connection to projects. |
| NHD-INT-E | Search | Dimensions; across all N.H material; exact source vs interpreted result; positional vs semantic stay distinct; why a result matched; permission before search; search never changes memory; honest empty results. |
| NHD-INT-G | Global boundaries (8.1–8.9) | Never close the book · Ness is the decider · original ≠ interpretation · simulation stays simulation · append, never overwrite · provenance · privacy before convenience · no permission expansion · no hidden duplication. |
`ness_intent` (added to the Part A vocabulary): Ness's stated wish or direction, recorded in his words; not yet restated as a decision, not a package.

### N.7 Files and terms that were referenced but absent from GitHub when Pass 3 ran — recovery status (all files recovered and pushed on 2026-09-16; the only remaining item, the mini-agent, is undefined)
| Missing file / definition | Referenced by | Why it matters |
|---|---|---|
| `NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` — **FOUND: Ness supplied it on 2026-09-16** (SHA-256 `114a118c242ea553b11488eb6380da1458f3788084c4f86332ba45b9a6896273`, 2,263 lines, 53,190 bytes; **pushed to `05_ACTIVE_CANDIDATE/` 2026-09-16, commit `ca5713f`, bytes match**) | A19 checkpoints v1.0–v1.2 §11, `NH_DESIGN_ANSWERS.md`, continuation context, A19 remaining plan | It is "the included A19 source": the Unreal Engine 5 selection and the sections the September answers hang on (2.1–2.4, 3.6 MetaHuman, 9.5 temporary preview, 10.1, 15 simulated people, 19 procedural room creation). `NH_DESIGN_ANSWERS.md` links it at Ness's local path `/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NH-GOVERNANCE/05_ACTIVE_CANDIDATE/` — i.e. it existed in Ness's local clone (inside the retired tool's folder) and had not been pushed until 2026-09-16; now on GitHub. |
| AIC receipt · UDOK receipt — **FOUND 2026-09-16 in Ness's local snapshot (`NH_Custom_GPT_Knowledge_20260914.zip`)**: `NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` + its `…PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (Aug 20 2026) and `NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` + its `…PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (Aug 21 2026); both receipts: `PACKAGE_COMPLETE` for the standalone mechanical-design scope only; **all four pushed to GitHub 2026-09-16 (commit b45b98d), bytes verified** | continuation context | Evidence that Additions 1 and 2 were accepted (limited scope). Now on GitHub. |
| `NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` — **FOUND: Ness supplied it on 2026-09-16** (SHA-256 `0839e5dcfcff1fd41b65fd44403a2ad18408869fea38111300852a2074ce20f3`, 338 lines, 16,051 bytes; dated 2026-08-03; self-status "TEMPORARY PERSONAL IDEA / DESIGN-INPUT NOTE — NOT AUTHORITY — NOT AN A19 CANDIDATE"; **pushed to `05_ACTIVE_CANDIDATE/` 2026-09-16, commit `ca5713f`, bytes match**) | UE5 package §1 item 10, §45, §48 | The earlier personal A19 idea note the UE5 package builds on. Index status `ness_intent`: the "Local Embodied World Workshop" idea — VR world, rooms (existing / Ness-created / N.H-proposed / mixed), offline creation with Blender + a real-time runtime; its boundaries (room is not the memory; simulation is not reality; A17 stays active; real actions separate; camera/VR are protected front doors; immediate safe exit); five design stages, of which only Stage 1 (preservation) is done. Its §10 open ideas are carried as `ness_intent`, not decisions. The UE5 package later replaced its open "runtime candidate" role with Unreal Engine 5 (NHD-UE5-1 item 10). Entry: NHD-PIN-A19. |
| "the mini-agent" | `NH_DESIGN_ANSWERS.md` answer 3, continuation context, the retired tool's `AGENTS.md` | **Recovery result (ChatGPT, 2026-09-16): undefined.** No repository file defines it; no decisions fixing its appearance, role, or behaviour were found; in an earlier conversation Ness himself said he did not know what it referred to. The "exception" in the design answer rests on decisions that cannot be found. **Its meaning must not be invented.** |

### N.9 `NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` (2026-08-14; supplied by Ness 2026-09-16) — status per its own header: "NESS-SELECTED TECHNICAL DIRECTION + DESIGN / IMPLEMENTATION BLUEPRINT — NOT A19 PACKAGE COMPLETE — NOT MASTER/MAP INTEGRATED — NOT IMPLEMENTED" → index status `ness_decision` (direction) + `assistant_proposal` (blueprint sections). **Direction-accepted 2026-09-17:** NHD-UE5-1 — §1's ten points and §49 only — formal receipt `NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` (239 lines, 22,212 bytes, SHA-256 `a5d6735f867d1c8680ee09ecf1bc9b24477469bdd6cd2c719444916eddfad7eb`) (passed independent audit). The source remains a **mixed-status document**: never `accepted_package`, never `PACKAGE_COMPLETE`; §§5–8, §§11–14, §§25–39 remain proposals; no other section newly accepted; no UE5 minor release locked; no Master/Map integration, installation, build, test, or real-data connection occurred.
| ID | § / lines | Point |
|---|---|---|
| NHD-UE5-1 (**direction-accepted 2026-09-17**, receipt v1_1) | §1, 53–71 (and §49, 2249) | Ten-point direction: Unreal Engine 5 is the preferred real-time 3D runtime for Ness's World and Wonder; no custom 3D engine; runtime must work locally and offline; internet not a runtime requirement; online only for deliberate acquisition; **N.H remains outside Unreal**, talking through a narrow local bridge; Unreal is subordinate to N.H's privacy/authority/provenance/simulation/memory rules; **Wonder remains possibility, not reality**; World and Wonder may share the runtime as distinct modes; Blender stays optional for assets. |
| NHD-UE5-2.2 | §2.2, 90–103 | Carries NHD-WR-20260721-1/2/3 (room start: blank / from memories / mixed; Ness's choice overrides; voice command takes effect immediately). |
| NHD-UE5-2 | §2.1–2.5 | Preserves: Ness's World rules; world manipulation never rewrites memory; Wonder rules; replay / reconstruction / invention stay different. |
| NHD-UE5-9 | §9, 634–689 | Runtime modes: world presentation · replay · reconstruction · Wonder · temporary preview (§9.5 is the section NHD-DA-20260914-1 answers). |
| NHD-UE5-10.1 | §10.1, 725–729 | Hard rule: `proposed` may never automatically become `running`; simulation must not begin secretly. |
| NHD-UE5-15 | §15, 952–1008 | Simulated people (§15 is the section NHD-DA-20260914-2 answers); §15.3 reality rule: a simulated real person's behavior is never proof of that person's actual beliefs, intentions, or feelings. |
| NHD-UE5-16/17/18/19 | §16–§19 | Branching (no branch contamination) · time controls · white doors as interactive objects pointing to destination descriptors · procedural room creation (§19 is cited by NHD-DA-20260914-1). |
| NHD-UE5-23/24 | §23–§24 | Camera/mic/VR/sensor boundary; external-action firewall. |
| NHD-UE5-40 | §40, 2016–2035 | What should NOT be implemented. |
| NHD-UE5-45 | §45, 2121–2152 | Acceptance boundary: modifies nothing, closes nothing, builds nothing; "implementation blueprint" = how a later build should be done, not that it happened. |
| NHD-UE5-48 | §48, 2230–2246 | Sources it was aligned to — including "current remaining-design working records preserving the later direct A19 room-start decisions" and `NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` (was not in the repo; pushed 2026-09-16 — see N.7). |
| NHD-UE5-50 | §50 | Its own next step: preserve → audit → accept for the narrow runtime-direction scope if Ness chooses → consumed by A19/Bundle 7/Bundle 8 → implement only under later authorization. **Done 2026-09-17:** ChatGPT PASS on the source bytes; Ness accepted the narrow scope in writing; receipt `NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` (239 lines, 22,212 bytes, SHA-256 `a5d6735f867d1c8680ee09ecf1bc9b24477469bdd6cd2c719444916eddfad7eb`) passed audit. Blueprint sections remain proposals. |
Sections §5–§8, §11–§14, §25–§39 (architecture, bridge protocol, command/event vocabularies, logging, recovery, performance profiles, Unreal project structure, components, prototypes, build sequence, test suite) are blueprint material: `assistant_proposal`. The 2026-09-17 direction acceptance (NHD-UE5-1) did **not** accept them, and §49's future proof requirements are not authorization to build.

### N.8 Pass 3 coverage statement
Done: checkpoint v1.2 (all decision sections), DESIGN_ANSWERS (all three), HISTORICAL_ANSWERS (all 22, first lines read; full text in file), continuation context, Five Additions (names + later status), intent excerpts (family level). **Not done:** checkpoints v1.0/v1.1 diff against v1.2 (v1.2 says it preserves v1.1); A19 remaining-design plan v1.0 item list; `02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD` checked against the accepted Bundle 6 policy package; `NH_A2_CURRENT_STATUS_v1_1` currency check.

---

## PART O — PASS 4: DECISIONS FOUND ONLY IN CHAT RECORDS (search of Ness–Claude conversations, June–September 2026)

| Finding | Where | Status | What it means |
|---|---|---|---|
| The three July 21 room-start decisions | Claude working records 2026-07-21 (two chats) | `ness_decision` — **now also file-recorded** in the UE5 package §2.2 (pushed to GitHub 2026-09-16) | Recovered; no longer chat-only. **Carried by accepted A19-RS v1_2 since 2026-09-17** (PACKAGE_COMPLETE for its standalone scope). |
| `NH_REMAINING_DESIGN_WORK_MAP_v1_0…v1_4_WORKING_RECORD.md` (July 2026) | Delivered to Claude outputs for the ChatGPT project files; **not in the GitHub repo, not in the Sept 14 local snapshot** | working record (navigation), not authority | Its unique Ness content was the three room decisions (now in UE5 §2.2) plus "five preserved dual-model decision points under A21," which it sourced to the standalone handoff package already in the repo. Low loss risk; still worth pushing if Ness has it, because the UE5 package §48 and the personal idea note cite it. |
| June 25 outside-research decisions (pipeline scope; excerpt + full page; screenshot inert; fallback Option A) | Claude chat 2026-06-25 | `master_settled` — already in Master §8 (lines 2789–2811, "settled June 25 / corrected June 29 2026") | Not stranded. |
| June 25 Connection Capability conceptual design | Claude chat 2026-06-25 | `master_settled` — Master §24 (S19); B-INT-8 accepted | Not stranded. |
| Project growth-record shape (DUMB-only ledger vs interpretive log) | Claude chat 2026-07-27 | `assistant_proposal`, question left open; Ness did not answer | Not a decision. Recorded so nobody claims it was decided. |
| "the mini-agent" | Not found in any Claude chat, repo file, or the local snapshot | **recovery completed (ChatGPT, 2026-09-16): undefined** — no defining file or decision exists; Ness himself once said he did not know what it referred to | Nothing further to recover. Must not be invented. See N.7, P.3. |
| Voice interruption ideas (V-NEW-1…7) | This conversation, 2026-09-16 (voice) | `assistant_summary` until Ness states them | Part F.2. |
| Retired Q&A tool | This conversation, 2026-09-16 (voice) | `ness_decision` | Part G.2. |
| Cursor as the implementation/building tool (NHD-WR-20260916-2) | Ness's direct written statement to ChatGPT, 2026-09-16: "I want Cursor to do the building of N.H. Not Claude Code, not ChatGPT." | `ness_decision`; the earlier voice-transcription conflict is resolved | Part G.3. No implementation is authorized by this decision. |
| Chat interface correction (NHD-WR-20260916-3) — normal scrolling conversation · ChatGPT-like basic behaviour · full-window PC chat, with smaller presentation when appropriate · centred conversation area · Ness's messages on the right in rounded boxes · N.H's replies on the left as plain text, away from the far-left screen edge · colours undecided · extra features deferred until later | Ness's 2026-09-16 instruction to Claude; Ness's earlier correction to ChatGPT | `ness_decision`; **carried by accepted A19-CI v1_1 since 2026-09-17** (PACKAGE_COMPLETE for its standalone scope) | Part N.1 (12.1/12.2 superseded); P.3 record task. |

**Search limits:** only Ness–Claude chats are searchable from here. ChatGPT-side conversations (including all A19/Wonder sessions of September) are not; anything decided only there is recoverable only from ChatGPT or from files Ness exports.

---

## PART P — PASS 5: RECONCILIATION

### P.1 Where the same decision lives in several places (one ID, several pointers)
| Decision | Pointers |
|---|---|
| Room start: blank / from memories / mixed; Ness's choice wins; voice changes it instantly (NHD-WR-20260721-1/2/3) | Claude working record 2026-07-21 · UE5 package §2.2 (repo) · **accepted A19-RS v1_2 + closure record v1_0 (2026-09-17)** · answers Master §19C Q3–Q5 · Map v1.6 line 638 still lists as open |
| Chat interface | A19 checkpoint v1.1/v1.2 §12 (three-area prototype — **superseded**) · Ness's later correction (NHD-WR-20260916-3 — current; **accepted A19-CI v1_1 + closure record v1_0, 2026-09-17**) |
| Unreal Engine 5 as runtime (NHD-UE5-1) | UE5 package §1/§49 · **runtime-direction acceptance record v1_1 (§1 and §49 only, 2026-09-17)** · continuation context · A19 checkpoints §11 · `NH_DESIGN_ANSWERS.md` header |
| A17 Wonder-to-memory route | accepted A17 v1_0 + closure record · Master §11 item 30 (older, partial wording) · UE5 package §2.4/§43 |
| Voice priority — TTS stops when Ness speaks (NHD-M26-VP) | Master §26.4 lines 5145–5147 · Master §25.1 BOP event line 3376 · Master OOP signals 5283–5287 |
| Hardware direction RTX 3090 24GB (NHD-M11-3) | Master §11 item 3 · Companion (hardware-upgrade snapshot) · archive §9 recorded the old drift as a conflict — resolved by the Master |
| Academic sources Semantic Scholar + OpenAlex (NHD-M11-9) | Master §11 item 9 (2026-06-29) |
| Dual-model handoff concept | standalone decision package (Jul 1) · placement record v1_1 + acceptance (Jul 13) · B24 v7 references it · Remaining Design Work Map (A21 points, not in repo) |

### P.2 Stale entries — older text still says "open" or "not designed" while a newer record settles it (nothing corrected here; the next Master candidate corrects them)
| Older text | What is newer |
|---|---|
| Master V10 header: "NOT YET ADOPTED", Master-19 v7_1 authoritative | Ness's adoption 2026-06-29 (governs) |
| Master §11 item 31 "World model — NOT DESIGNED" | A18 accepted in Bundle 4 (Jul 11 2026) |
| Master §11 item 28 Living State Web "partial, not built"; item 29 §7R "core designed" | A6/B5/B6/B8 (Bundle 4), A4/B1/B-INT-1 (Bundle 2) accepted |
| Master §11 item 35 TSC "accepted with later corrections" | B15, B-INT-4 accepted (Jul 13 2026); A16 supersedes §11.35's archive-event naming (per the July working map's verified list) |
| Master §11 item 30 Wonder "larger mechanism not designed" | A17 accepted; UE5 package gives the runtime direction (not accepted yet) |
| Master §11 item 34 "five open meaning-to-technical questions" | Bundle 6 A3 answers accepted (Jul 13 2026) — Pass 2b should confirm all five are covered by the A3.1–A3.5 labels |
| Master §19C Q1–Q5 open | Q3–Q5 answered (NHD-WR-20260721, now carried by accepted A19-RS); Q1 partly touched by NHD-A19CP-7 (Create New World → blank white room); Q2 still open |
| Master §19C "additional unanswered" list | answered: full context of each correction (N673/H1742), backtracking order (H1765), learned-pattern display (H1757), challenging one pattern (H1760); still open: opening transition (partly: NHD-A19CP-3.1/3.2), same-screen vs full-screen, desktop/mobile/VR differences, own direct door (H1546 is generic — unresolved) |
| Master §19D paused points | partially answered by H1739/H1740/H1744–H1750/H1754/H1756/H1759/H1762/H1763; simulation interior direction in UE5 §9–§19 (not accepted) |
| Map v1.6 A19 open-slot list (line 638) and stale A25 entry (noted in Bundle 1 closeout) | as above; A25 accepted Jul 11 2026 |
| Companion v1 mirrors Master §19C (line 4978) | same staleness as the Master |
| Decision Defaults S19 v2_2 — recorded "Defaults-line drift" items D1–D9 | carried in A7 / Bundle 5 / B24; correction only via a future Defaults candidate (never adopted: v2_3) |
| `NH_A2_CURRENT_STATUS_v1_1.md` (Jul 1) | A2 v1_8 package-complete the same day; Pass 2b to check whether its pointers still hold |
| Archive `NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1.md` §2 authority = Master-19 v7_1 | pre-adoption snapshot; superseded by V10 adoption; its §9 name-spelling conflict ("Nes" in one file) stands as history — "Ness" everywhere current |

### P.3 Conflicts and genuinely open matters (owner named; nothing decided here)
| Item | Class | Owner |
|---|---|---|
| Chat interface record | **done 2026-09-17** — NHD-WR-20260916-3 carried by accepted A19-CI v1_1; checkpoint §12 supersession recorded there | — |
| Auto-resume vs checkpoint for simulation branches (H1759 context) | `new_design_choice` | Ness |
| Own direct door per recent space (H1546 generic) | `evidence_missing` → re-ask once, with H1546 shown | Ness via ChatGPT |
| Four "blueprint-like" items (NHD-A19CP-8) | **not recovered** (ChatGPT, 2026-09-16): §8 preserves only Ness's recollection; no file names them; the four category-layout options (open map / centred hub / floating canvas / adaptive) are probably not them | stays `UNRESOLVED / DEFERRED` as the checkpoint says; Ness if he remembers |
| The mini-agent | **undefined** after recovery (see N.7); the flexibility exception that names it cannot be applied until Ness says what it is — or drops it | Ness |
| `NH_REMAINING_DESIGN_WORK_MAP_v1_0…v1_4` not in repo | `missing_source` (low risk) | Ness (push if held) |
| Prototype `NH_interactive_2D_ultrawide.html` not in repo (SHA recorded) | historical only — the prototype is not approved as the chat interface | Ness (keep or not; no longer needed as a reference) |
| Local Master differs from GitHub Master by one line (§7R line 2535) | sync issue, not a design conflict; GitHub bytes are the pinned ones | Ness (replace local copy) |
| Voice V-NEW-1…7 | `assistant_summary` → Ness's own words needed, then Register A via ChatGPT instruction | Ness |
| UE5 package: narrow runtime-direction acceptance (its §50) | **done 2026-09-17** — NHD-UE5-1 direction-accepted (§1 and §49 only); receipt v1_1 passed; blueprint sections remain `assistant_proposal` | — |
| **Seven-web pass — mechanical-design package before Bundle 8?** The seven-web concept is established (Master §7B; Map C-7B); Engines A and B were prototyped — the Master records those early engine layers as built and run (§7C; Map C-ENGINE-AB); **no standalone, versioned, independently audited and accepted mechanical-design package exists for the complete seven-web pass**, and the Map's C-7B / C-ENGINE-AB descriptions are not such a package. Whether it should receive its own package before Bundle 8 is Ness's decision; **Ness has deferred it until the current work is done. Do not ask it now.** | `new_design_choice — deferred` | Ness |
| A17 closure receipt audit; every receipt's own audit | process | ChatGPT |
| Bundle 8 not started; B-INT-10, B-INT-11 whole-system application; B-CYCLE-1…9 | `unfinished_mechanics` | Claude, on exact instruction, after Bundle 7 |
| Memory Fabric v1_4 (Addition 3) | not audited, not accepted; inactive by Ness's continuation note | stays inactive until Ness reactivates |
| Additions 4 and 5 | no later record | Ness / ChatGPT (whether to design next) |

### P.4 What the ChatGPT audit of this index should check
1. Every line number in Parts B–F against `NH_MASTER-20_CORRECTED_v10.md` SHA `2d9ed4c6…`.
2. Every acceptance date and PASS statement in Part L against the receipt files.
3. Part M.10 byte comparison (re-run on the zip).
4. That no entry upgrades a status (candidate → accepted, accepted → built, intent → decision).
5. That Parts F.2, G.2, G.3, O contain nothing beyond what Ness actually said in this conversation.
6. That the A19-RS, A19-CI and NHD-UE5-1 statuses match their receipts exactly — package-complete only for the two standalone scopes; direction-accepted only for §1 and §49 — and that nothing beyond them is upgraded.

---

## PART M — REPOSITORY FILE CLASSIFICATION: WHICH FILES ARE CURRENT, WHICH ARE OLD
Ness asked which files are old files he never deleted. Classification below is by **evidence** (byte hashes, receipt-named versions, git last-change dates from the full 98-commit history). It is information for Ness. **The index deletes nothing and recommends nothing be deleted**; under the file-safety rules, removal of any file is Ness's call, and historical versions have provenance value.

### M.1 Exact duplicates — 8 files that were in `05_ACTIVE_CANDIDATE/`, byte-identical to the accepted copy in `04_ACCEPTED_STANDALONE_DESIGNS/` — **deleted 2026-09-17**
B10 v1_0 · B-HOLD v1_0 · B9 retry state v1_0 · Bundle 1 coordination note v1_0 · B11 v1_4 · A31 v1_0 · Story-Layer firmness v1_0 · A7 v1_1.
**Cleanup 2026-09-17:** only the duplicate `05/` copies were deleted; the accepted `04/` copies remain unchanged; Git history preserves the removed copies; deletion of a duplicate changes no package status or provenance. Exact filenames: `NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`, `NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md`, `NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`, `NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md`, `NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md`, `NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md`, `NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md`, `NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`.

### M.2 Superseded earlier versions of packages that were later accepted at a higher version (locations as surveyed on 2026-09-16; **cleanup 2026-09-17** below)
**Cleanup 2026-09-17:** fourteen of these drafts were moved from `05_ACTIVE_CANDIDATE/` to `99_HISTORICAL_CANDIDATES/` by 100%-similarity renames, bytes and historical status preserved; the moves accept, reject, supersede, or reopen nothing beyond the status already established: `NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_1_CANDIDATE.md`, `NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`, `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md`, `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_1_CANDIDATE.md`, `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_2_CANDIDATE.md`, `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_3_CANDIDATE.md`, `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_0_CANDIDATE.md`, `NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_1_CANDIDATE.md`, `NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_0_CANDIDATE.md`, `NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_0_CANDIDATE.md`, `NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_v1_0_CANDIDATE.md`, `NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_0_CANDIDATE.md`, `NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_1_CANDIDATE.md`, `NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_0_CANDIDATE.md`. Left in place on purpose: the A25→B10 v1_0/v1_1 candidates in `04/` (their receipt retains them) and the A19 checkpoint v1_0/v1_1 in `05/` (v1_2 says it preserves them).
| Old file | Accepted version (where) | Evidence |
|---|---|---|
| A2 telling-object v1_1 (Jun 30) | v1_8 (04) | package-complete record v1_0 names v1_8 |
| A2 v1_0 | — | already in `99_HISTORICAL_CANDIDATES/` (correctly placed) |
| Bundle 1 closeout v1_1 (Jul 8) | v1_4 (04) | closure record names v1_4 |
| B9 retry-values wiring v1_0, v1_1, v1_2, v1_3 (Jul 12) | v1_4 (04) | closure record names v1_4 |
| A25 reread-mode policy v1_0, v1_1 (Jul 12) | v1_2 (04) | closure record names v1_2 |
| A26 v1_0 (Jul 13) | v1_1 (04) | closure record names v1_1 |
| A7 v1_0 (Jul 13) | v1_1 (04) | closure record names v1_1 |
| Bundle 2 completion v1_0 (Jul 10) | v1_1 (04) | closure record names v1_1 |
| Bundle 3 completion v1_0, v1_1 (Jul 10) | v1_2 (04 since 2026-09-17 — see M.3) | acceptance record names v1_2 |
| Dual-model placement record v1_0 (Jul 13) | v1_1 (04 since 2026-09-17 — see M.3) | acceptance record names v1_1 |
| A25→B10 connection v1_0, v1_1 — **in `04/`** | v1_2 (04) | receipt v1_1 explicitly retains them as "historical candidate provenance — retained unchanged" |
| A19 checkpoint v1_0, v1_1 (Sep 15) | v1_2 (05) | v1_2 header: "This successor preserves the v1.1 checkpoint"; predecessors deliberately kept |

### M.3 Accepted sources that were misplaced in `05_ACTIVE_CANDIDATE/` — **moved to `04_ACCEPTED_STANDALONE_DESIGNS/` on 2026-09-17**
As surveyed on 2026-09-16, six accepted sources sat in `05/` while their acceptance/closure records sat in `04/`: Bundle 3 completion v1_2 · Bundle 4 completion v1_3 · A4 v1_1 · B1 v1_0 · A1 design-closure v1_1 · Dual-model handoff placement record v1_1. **Cleanup 2026-09-17:** all six, plus the two A19 packages accepted the same day (A19-RS v1_2, A19-CI v1_1), were moved into `04/` by 100%-similarity renames — eight moves: `NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`, `NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`, `NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`, `NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`, `NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`, `NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`, `NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`, `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`. Folder placement never created acceptance; it now matches it. Frozen receipts that name the old `05/` path keep that wording, because it was true when they were written.

### M.4 Current standalone decision packages (not superseded by anything)
`NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` (Jul 13; Ness-approved concept; not integrated) · `NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` (Aug 4; Ness-approved direction; not designed as packages).

### M.5 Current working / transfer records (all last changed 2026-09-15)
A19 checkpoint v1_2 · A19 remaining-design plan v1_0 · `NH_DESIGN_ANSWERS.md` · `HISTORICAL_ANSWERS.md` + `HISTORICAL_ANSWER_PROVENANCE.json` · `Music_Media_Intent_Excerpts.md` · `Thought_Branches_and_Simulation_Intent.md` · `Other_Future_Feature_Intent_Excerpts.md` · `02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` (self-described "temporary working record"; its content was later carried into the accepted Bundle 6 policy package — Pass 3 checks whether anything in it is NOT in the accepted package) · `00_CONTINUATION_CONTEXT.md`.

### M.6 Status/navigation notes that may be stale
`NH_A2_CURRENT_STATUS_v1_1.md` (Jul 1) — self-described "navigation and status pointer only." Written the same day A2 v1_8 went package-complete; whether it still describes the current state is for Pass 3 to check, and for Ness to decide whether to keep.

### M.7 Instruction files in `06_OPERATIONAL_INSTRUCTIONS/`
`NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_2_CANDIDATE.md` (Jun 30; the active Claude instructions match it) and four ChatGPT-side files added Sep 15, one carrying an upload suffix (`NH_Unified_Project_Instructions_Full (1).md`). Which of these is the live ChatGPT instruction set is not determinable from the repo — Ness knows.

### M.8 Authoritative and workflow files (Jun 30 / Jul 3) — current by definition
`01_AUTHORITATIVE/` (4 files) · `02_WORKING_MAP/` v1_6 candidate · `03_WORKFLOW/` (design-completion workflow v1_0; eight-bundle dependency plan v1_0) · `README.md`. Known stale wording inside them (V10 header "NOT YET ADOPTED"; Map v1.6 A19 open list) is recorded in Parts B and D, not corrected.

### M.10 Local snapshot (2026-09-14) vs GitHub — verified byte by byte
Source: `NH_Custom_GPT_Knowledge_20260914.zip` (121 embedded originals, each with a recorded SHA-256; extracted and compared by content against GitHub). The 106-of-107 result below holds against the **current head `2e7a710b`** (146 files); against the intermediate head `ca5713f` only 100 of the 107 snapshot repository files matched: the UE5 package was already there, but six snapshot-backed additions (AIC ×2, UDOK ×2, Memory Fabric, music intake) had not yet been pushed, and the Master differed by one colon — six missing plus the Master makes the seven non-matches. (v0_1–v0_3 named `ca5713f` — corrected.)
- **106 of 107 shared files are byte-identical.** (v0_1 said "the bundle appends one newline" — wrong: the extra newline came from Claude's own extraction step, which included the bundle's separator line. The bundle reproduces every recorded size and SHA-256 exactly; ChatGPT confirmed this independently. The seven snapshot-backed files pushed on 2026-09-16 were verified against the recorded hashes before upload, so the pushed bytes are correct.)
- **One real difference: `NH_MASTER-20_CORRECTED_v10.md`, line 2535 (§7R).** GitHub: `**The mouth model** (…)`; local: `**The mouth model:** (…)` — **exactly one colon** (v0_1 wrongly described a quote marker too; that was the diff tool's own `>` prefix). One character, but it changes the hash (GitHub `2d9ed4c6…`, local `611ababf…`). **Nine accepted receipts pin the GitHub hash.** The GitHub bytes are the adopted Master; the local copy has drifted. Replacing the local copy with the GitHub copy is a sync, not a governance edit — Ness's call.
- **Eight additions to GitHub since `5e000f8f`, all on 2026-09-16, all bytes verified:** seven were in the Sept 14 snapshot — the UE5 package (commit `ca5713f`), AIC v1_10 + receipt and UDOK v1_9 + receipt (`b45b98d`, into `04_ACCEPTED_STANDALONE_DESIGNS/`), Memory Fabric v1_4 and the music intake (`73f565c`, then moved into the new `05_INACTIVE_CANDIDATE/` by `bea3098`/`2e7a710`) — plus one that was **not** in the snapshot, the personal A19 idea note (`ca5713f`). GitHub (146 files) now holds everything the snapshot held; the eight files that sit in different folders locally vs on GitHub remain byte-identical.
- **Same content, different name:** local `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1_1_CANDIDATE.md` is byte-identical to GitHub's adopted `…_v1.md`. Nothing to push; the adopted name on GitHub stands.
- **Local layout was ahead of GitHub on placement (historical, at head `2e7a710b`):** locally, the six accepted sources listed in M.3 sat in `04_ACCEPTED…` while on GitHub they still sat in `05_ACTIVE_CANDIDATE/`. **No longer true after the 2026-09-17 cleanup** — GitHub now matches (M.3). The byte-comparison results above are historical results at their stated heads; the current head is `19071b51…`, 148 tracked files.
- **Loop-tool artifacts, not governance content:** `LOCAL_ADDITIONS/WORKFLOW_INSTRUCTIONS/AGENTS.md`, `EXCLUSIONS_AND_LIMITS_HE.md`, `INDEX_HE.md`, `ORIGINALS_HE.md`, `ONLINE_COMPARISON.json`, `SOURCE_MANIFEST.json`, `VERIFICATION.json`. Retired with the tool (NHD-WR-20260916-1); keep or drop is Ness's choice.

### M.9 Plain summary for Ness
- 8 exact duplicate copies — **deleted 2026-09-17** (the accepted copies stay in `04/`).
- 14 earlier drafts of things later accepted at a higher version — **moved to `99_HISTORICAL_CANDIDATES/` 2026-09-17**; a few others are deliberately kept where their receipts or successor keep them.
- 8 accepted sources that sat in the "candidate" folder — **moved to `04_ACCEPTED_STANDALONE_DESIGNS/` 2026-09-17** (six previously misplaced, plus A19-RS and A19-CI accepted that day).
- The current working / transfer records are listed in M.5; `05/` also retains deliberately preserved prior or superseded records (e.g. the A19 checkpoint v1_0/v1_1 and superseded index-acceptance-record history), so folder placement alone does not establish currentness or status.
- None of this was a design conflict. It was housekeeping; it is done, and it changed no decision, acceptance, authority, or file content.

---

## PART K — VERIFICATION LOG (2026-09-16; first run against head `5e000f8f`, 138 files; the repo advanced to `2e7a710b`, 146 files, the same evening — K.2/K.3 record the later checks)
| Check | Method | Result |
|---|---|---|
| 48 Master section lines (Part B) | printed each cited line from the real file | 48/48 match |
| §19A points 3032–3066, §19B 3064, §19C 3077/3079/3080/3083 | printed each cited line | all match |
| §19D, §19E heading lines | printed | **corrected**: 3086→3087, 3100→3101 |
| Line 3103 label | printed | **corrected**: line is in §19E cross-audit, not §19A; relabeled NHD-M19E-0; settled point is NHD-M19A-6 |
| Voice lines 5145, 3376, 5283, 5287, 3808 | printed | all match |
| Bundle 4 acceptance record names A6, A8, A18, B5, B6, B8, B27, B-INT-9 | grep on the record | confirmed (each present); record states Ness's explicit acceptance |
| Bundle 3 acceptance record names B-AFFIRM | grep | confirmed |
| Bundle 2 acceptance record names A4, B1, B26, B-INT-1 | grep | confirmed |
| A17 "accepted with closure condition" | read closure record §7 | confirmed: closure awaits ChatGPT audit PASS |
| B16, B7, B15, B-INT-4, A1 standalone files exist | ls | confirmed (2, 2, 2, 2, 4 files) |
| July 21 decisions absent from repo | grep for their wording | confirmed absent |
| Master hash | sha256sum | `2d9ed4c6…aa32c` matches the value recorded above |
| Part M duplicates | sha256sum over all .md, sorted, adjacent-equal | 8 identical pairs, all 05↔04 |
| Part M dates | `git log -1 --format=%cs -- <file>` on a full clone (98 commits) | per-file last-change dates as listed |
| Part M receipt-named versions | grep of version strings inside each receipt | as listed in M.2/M.3 |
| M.10 local-vs-GitHub | extracted 121 embedded originals; stripped bundle header; byte-compared to GitHub head `2e7a710b` (146 files) | 106 identical (the "+1 newline" in v0_1 was an extraction artifact); Master differs at line 2535 by one colon; receipts pinning GitHub hash: 9 |

## PART K.2 — CHATGPT INDEPENDENT AUDIT, 2026-09-16 → v0_2 CORRECTIONS
Result on the file ChatGPT received: **NOT PASS** (11 issues). Each was re-verified by Claude against the repo before correction; all 11 were confirmed.
| # | Issue | Verified | Correction in v0_2 |
|---|---|---|---|
| 1 | Ness attached an older 573-line download, not the 652-line file | yes | v0_2 was attached and its identity confirmed by ChatGPT |
| 2 | NHD-M19A-16 is in §19B (provisional), not §19A | yes — line 3064 is the §19B heading | relabeled NHD-M19B-1, provisional |
| 3 | NHD-M14-4/5/8 marked settled; Master line 2932 calls the remaining §14 content exploratory | yes | statuses changed to exploratory |
| 4 | Citations 3376, 3808, 5145 cover more than one line | yes | ranges 3376–3377, 3808–3810, 5145–5147 |
| 5 | F.2: handoff package does not decide pre-generation; V-NEW-7 is Claude's question | yes | V-NEW-1 → "compatible, not decided"; V-NEW-7 → `assistant_proposal` |
| 6 | L: 81→85 files; AIC/UDOK now on GitHub; PASS not universal (A31, A4, B1 records have none) | yes — grep: 0 "PASS" in each | L.0, L.1, N.5, N.7 updated |
| 7 | "Bundle appends a newline" is wrong; Master diff is one colon | yes — extraction artifact; `**The mouth model**` vs `**The mouth model:**` | M.10 and K corrected |
| 8 | Recovery statements outdated (files now pushed) | yes | M.10, J updated |
| 9 | Three-area prototype treated as standing; Ness had explicitly corrected it | consistent with Ness's 2026-09-16 instruction | 12.1/12.2 → `superseded`; NHD-WR-20260916-3 added; v0_1 question withdrawn |
| 10 | G.2 added conclusions beyond the retirement decision | yes | decision row reduced to Ness's words; extras moved to `assistant_proposal` |
| 11 | G.3 unsupported / conflicts with later records | ChatGPT reports conflicting records | G.3 → `needs_ness_confirmation` |
Recovery answers recorded: mini-agent undefined (N.7, P.3); four blueprint-like items not recovered (P.3).

## PART K.3 — CHATGPT SECOND AUDIT (v0_2, identity confirmed `13ca52aa…`) → v0_3 CORRECTIONS
Result: **NOT PASS** (7 issues). Each re-verified by Claude; all 7 confirmed.
| # | Issue | Verified | Correction in v0_3 |
|---|---|---|---|
| 1 | Repo identity still `5e000f8f`/138; current is `2e7a710b`/146 | yes | Sources table and Part K title updated; head progression recorded |
| 2 | Pushed-state residue in G.1, N.7, N.9; M.10 counted six, not eight additions (seven snapshot-backed + the idea note) | yes — idea note was not in the snapshot; UE5 package was | all four places corrected |
| 3 | NHD-A19CP-18 still treated the prototype (incl. the three-column layout) as a current reference | yes — §18.1 lists the layout | entry split: layout superseded; card behaviours keep §13–§17 status; cards-in-new-chat left open for Ness |
| 4 | Part O merged the Cursor statement into `ness_decision` | yes | rows split; Cursor → `needs_ness_confirmation` |
| 5 | Part O still asked ChatGPT to recover the mini-agent; omitted NHD-WR-20260916-3 | yes | mini-agent row → completed/undefined; chat-correction row added |
| 6 | N.0 applied one status to all of Part N | yes | N.0 rewritten per section |
| 7 | L.0/L.2 claimed every receipt records its own audit as awaited | yes — A4, AIC, UDOK records (and others) do not | both passages corrected; no universal claim |

## PART K.4 — CHATGPT THIRD AUDIT (v0_3, identity confirmed `d7695778…`) → v0_4 CORRECTIONS
Result: **NOT PASS** (4 issues). All verified and corrected.
| # | Issue | Correction in v0_4 |
|---|---|---|
| 1 | N.7 heading still said `missing_source`; UE5 row still ended "was never pushed" | heading rewritten as recovery status; sentence corrected |
| 2 | M.10 and the Part K row named `ca5713f`; the 106/107 result holds against `2e7a710b`; first bullet said six files | head corrected in both places; "seven snapshot-backed files" |
| 3 | Source table still said 81 files / Pass 2 pending / Pass 3 pending | rows updated |
| 4 | Part O chat-interface summary omitted four parts of NHD-WR-20260916-3 | all eight parts listed |

## PART K.5 — CHATGPT FOURTH AUDIT (v0_4, identity confirmed `17407acd…`) → v0_5 CORRECTION
Result: **NOT PASS** (1 issue). Verified and corrected.
| # | Issue | Correction in v0_5 |
|---|---|---|
| 1 | M.10 gave the wrong reason for 100/107 at `ca5713f`: the UE5 package was already pushed; the seven non-matches were six unpushed snapshot-backed files plus the Master's one-colon difference | sentence corrected |

## PART K.6 — POST-ACCEPTANCE UPDATE → v0_6
- ChatGPT independently audited `NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` (74 lines, 7,516 bytes, SHA-256 `49245fbe6cac5809e89fe8eb53da2a7ab9761f909901caf6f0d70a2139ba017c`) and returned PASS on 2026-09-16. That record carries Ness's acceptance of the exact v0_5 bytes; v0_5 remains preserved unchanged.
- Later in the same ChatGPT conversation, Ness directly confirmed NHD-WR-20260916-2 in writing: "I want Cursor to do the building of N.H. Not Claude Code, not ChatGPT."
- v0_6 records the already-settled v0_5 acceptance and Part A approval, and changes G.3 plus its matching Parts O, P and J pointers. It also adds only the matching provenance and source-table entries. It remains a candidate until independently audited and explicitly accepted by Ness.

## PART K.7 — POST-ACCEPTANCE CURRENTNESS UPDATE → v0_7 (2026-09-17)
- **Base:** accepted v0_6 — 712 lines, 92,076 bytes, SHA-256 `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` — accepted by Ness with the exact words "I accept index v0_6." v0_6 remains preserved unchanged; its internal `CANDIDATE` wording is frozen historical text.
- **A19 status updates recorded (three):** (1) A19-RS — `PACKAGE_COMPLETE` for its accepted standalone room-start policy scope only; source `NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` (136 lines, 15,053 bytes, SHA-256 `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0`); closure record `NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (156 lines, 10,976 bytes, SHA-256 `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e`). (2) A19-CI — `PACKAGE_COMPLETE` for its accepted standalone ordinary-chat policy scope only; source `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` (180 lines, 18,830 bytes, SHA-256 `7bb426d211685ba9f96b2194163bcbb6750365ed689ef19b0614f5b217288451`); closure record `NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` (191 lines, 14,182 bytes, SHA-256 `8f22b0a1dd7b4393934af873993ef797437e8d312164b1676caecab2e240f18c`). (3) NHD-UE5-1 — direction-accepted, §1's ten points and §49 only; formal receipt `NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` (239 lines, 22,212 bytes, SHA-256 `a5d6735f867d1c8680ee09ecf1bc9b24477469bdd6cd2c719444916eddfad7eb`); the UE5 source remains a mixed-status document, never `accepted_package` or `PACKAGE_COMPLETE`; §§5–8, §§11–14, §§25–39 remain proposals.
- **Cleanup recorded (repository organization only, commits `37ebed19…`–`19071b51…`):** 8 duplicate copies deleted from `05/` (accepted `04/` copies unchanged; Git history preserves them); 14 superseded drafts moved `05/` → `99/`; 8 accepted sources moved `05/` → `04/`; all 22 moves at 100 % similarity. The cleanup changed no decision, acceptance scope, authority, implementation state, or file content.
- **One deferred open item added (P.3, J):** the seven-web pass — concept established, Engines A and B prototyped/built and run, no accepted standalone mechanical-design package; whether it gets its own package before Bundle 8 is Ness's decision, deferred until the current work is done.
- **Nothing else changed.** Parts K.2–K.6 are historical audit records and were not rewritten. No decision meaning, identifier, or status was changed beyond the receipts named above; no dependency preserved by A19-RS, A19-CI, or the UE5 receipt was closed; A19, Bundle 7, and Bundle 8 remain incomplete; no Master/Map integration or implementation occurred.
- **Standing:** v0_7 remains a candidate until ChatGPT independently audits its actual bytes and Ness explicitly accepts it. Creating v0_7 accepts nothing.

## PART K.8 — CHATGPT AUDIT OF v0_7 → v0_8 CORRECTIONS (2026-09-17)
Result on v0_7 (identity confirmed `424a6133…`): **NOT PASS**, three issues, all verified and corrected here; everything else passed (the base identity and all six source/receipt identities, both package-complete scopes, the UE5 boundary, the cleanup counts confirmed against Git, the deferred seven-web item).
| # | Issue | Correction in v0_8 |
|---|---|---|
| 1 | L.1 had introduced two invented `NHD-`-prefixed forms for the A19-RS and A19-CI package rows — new identifiers conflicting with Part A; the accepted sources define `A19-RS` and `A19-CI` as package IDs only | the two L.1 rows now use `A19-RS` and `A19-CI`; no `NHD-` form exists for them anywhere in the index; the "no identifier changed" statement in K.7 is therefore true |
| 2 | M.2 abbreviated five of the fourteen moved filenames with "…" | all fourteen written out in full |
| 3 | The v0_7 delivery reported the diff as 65 added / 48 removed; Git reports 62 added / 45 removed | delivery counts now taken from `git diff --numstat` |
v0_7 remains unaccepted and preserved unchanged. v0_8 remains a candidate until ChatGPT independently audits its actual bytes and Ness explicitly accepts it.

## PART K.9 — CHATGPT AUDIT OF v0_8 → v0_9 CORRECTIONS (2026-09-17)
Result on v0_8 (identity confirmed `fa9df136…`): **NOT PASS** — six stale folder references and one count wording, all verified and corrected here. ChatGPT also noted that its v0_7 audit had missed these stale references. Everything else rechecked and passed.
| # | Issue | Correction in v0_9 |
|---|---|---|
| 1 | L.1 NHD-B9: "copy also in 05" — that duplicate was deleted | now says the 05 duplicate was deleted 2026-09-17 |
| 2 | L.1 NHD-B9W: B9 wiring v1_0–v1_3 "historical in 05" | in 99 since 2026-09-17 |
| 3 | L.1 NHD-A25: A25 v1_0–v1_1 "historical in 05" | in 99 since 2026-09-17 |
| 4 | L.2 repeated the two outdated historical locations | corrected as historical-at-survey / current-since-cleanup |
| 5 | M.2 located accepted Bundle 3 v1_2 in 05 | 04 since 2026-09-17 |
| 6 | M.2 located accepted dual-model placement v1_1 in 05 | 04 since 2026-09-17 |
| 7 | K.8 said "all seven source/receipt identities" | "the base identity and all six source/receipt identities" |
v0_8 remains unaccepted and preserved unchanged. v0_9 remains a candidate until ChatGPT independently audits its actual bytes and Ness explicitly accepts it.

## PART K.10 — CHATGPT AUDIT OF v0_9 → v0_10 CORRECTION (2026-09-17)
Result on v0_9 (identity confirmed `08e6c401…`): **NOT PASS** — one currentness error; everything else passed (identities, A19/UE5 boundaries, cleanup lists, identifiers, seven-web item, diff count).
| # | Issue | Correction in v0_10 |
|---|---|---|
| 1 | M.9 said "Everything dated Sep 15 and later in `05/` is your current working material" — too broad: `05/` also holds deliberately preserved prior or superseded records dated Sep 15 or later (A19 checkpoint v1_0/v1_1; superseded index-acceptance-record history), contradicting M.2 | sentence replaced: current records are those listed in M.5; `05/` also retains preserved prior/superseded records; folder placement alone does not establish currentness or status |
v0_9 remains unaccepted and preserved unchanged. v0_10 remains a candidate until ChatGPT independently audits its actual bytes and Ness explicitly accepts it.

## PART J — DECISIONS REQUIRING NESS (asked one at a time in conversation)
1. **Done 2026-09-16.** Ness's acceptance of v0_5 explicitly approved the identifier scheme in Part A; acceptance record v1_2 carries the scope.
2. Confirm that the three July 21 decisions (Part G.1) are his — evidence supports it; confirmation only, not re-deciding. (G.2 needs no confirmation: stated directly by Ness on 2026-09-16.)
2b. **Done 2026-09-16.** Ness confirmed G.3 directly in writing to ChatGPT: Cursor will do the building of N.H, not Claude Code or ChatGPT. This selects the builder and does not authorize implementation to begin.
3. Confirm which of the V-NEW-1…7 voice ideas (Part F.2) he adopts, in his own words, so they stop being `assistant_summary`.
4. (Done 2026-09-16.) All files found in N.7 are on GitHub. Remaining: the mini-agent — see P.3.
5. (Withdrawn — answered by Ness's earlier correction; see NHD-WR-20260916-3.)
6. **Deferred by Ness (2026-09-17) — do not ask now.** Whether the seven-web pass receives its own mechanical-design package before Bundle 8 (P.3). Ness will decide after the current work is done.
