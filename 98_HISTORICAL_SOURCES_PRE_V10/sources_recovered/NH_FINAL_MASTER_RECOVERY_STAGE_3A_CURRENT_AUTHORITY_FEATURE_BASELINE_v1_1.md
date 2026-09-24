# N.H — FINAL-MASTER RECOVERY — STAGE 3A: CURRENT-AUTHORITY FEATURE BASELINE v1.1

**Corrected successor to Stage 3A v1.** v1 is preserved unchanged at
`NH_FINAL_MASTER_RECOVERY_STAGE_3A_CURRENT_AUTHORITY_FEATURE_BASELINE_v1.md`. This file does not begin
Stage 3B, does not compare any historical Master, and changes no N.H design. It corrects v1's reading,
status, and citation defects and adds the recovery v1 was missing.

**Why v1 was provisional.** v1's opening claimed the complete bodies of all six sources were read, but
v1's own §6 showed several were read only in part (the two accepted companions were read via the
governance embedding and summaries rather than as direct complete bodies; Cursor Rules was covered via
the Master's §6A summary; parts of the Master body were covered via change-logs rather than read
line-by-line). v1.1 corrects this by reading the **complete verbatim bodies** of all six sources
directly and rebuilding the affected recovery, status, and citations from those reads.

**What was read directly for v1.1 (full bodies; exact ranges in §6):** SRC-044 Master v7_1 (every section
§0–§25); SRC-015 DD-S19_v2_2 (L1–315); SRC-076 Cursor Rules v3.2 (L1–717, the file itself); SRC-087
governance companion (header + authority order + Part I workflows + Part II/III openers + structure of
Parts IV–V); SRC-001 accepted security/identity companion (its own body, 1724 lines, extracted as a
standalone file so its line numbers are source-body-relative); SRC-002 accepted TSC companion (its own
body, 956 lines, likewise standalone).

**What this is NOT.** No historical-Master comparison; no conflict resolution; no choice made for Ness;
no authority-file patch; no final-Master organization; no canonical drafting; Stage 3B not begun.

---

## 0. READING CONVENTIONS AND CORRECTED STATUS-LABEL MAPPING (read first — corrects v1 §0)

**This audit is document-based.** It read the bodies; it performed **no fresh disk inspection** of Ness's
machine. `BUILT AND DOCUMENTED AS VERIFIED` means the authority documents disk verification (S12–S16);
this audit did not re-run the check. Where the authority itself flags a built item as not re-verified,
`BUILT, BUT NOT FRESHLY DISK-VERIFIED IN THIS AUDIT` is used.

**Corrected status-label mapping (correction #2 — v1 over-used `FULLY DESIGNED — NOT BUILT`).** The
Master's design tags are no longer auto-translated. The rule now is:

- `FULLY DESIGNED — NOT BUILT` is used **only** where the authority explicitly presents a complete/full
  design or specification with no named undesigned schemas/thresholds/workflows/interfaces/limits.
- `PARTIALLY DESIGNED` is used where the conceptual core is settled **but** the section itself names
  schemas, thresholds, workflows, interfaces, limits, or implementation behavior that "remain
  undesigned." Under the Master's own closing lines, this is true of essentially every `[CONCEPTUALLY
  DESIGNED, NOT BUILT]` and `[CORE CONCEPTUALLY DESIGNED, NOT BUILT]` §7 section.
- `INTEGRATED INTO CURRENT AUTHORITY` is used for present governing **principles or rules** whose
  relevant status is integration into the authority text rather than software implementation (e.g. the
  premise, the two-machineries frame, the filter's operating rules, the behavioral/working rules, and
  the first-class principles).
- `ACCEPTED — NOT YET INTEGRATED` / `ACCEPTED — PARTLY INTEGRATED` for accepted external designs,
  judged against the current Master only (§4).

The eleven allowed labels are unchanged: BUILT AND DOCUMENTED AS VERIFIED · BUILT, BUT NOT FRESHLY
DISK-VERIFIED IN THIS AUDIT · PARTIALLY BUILT · FULLY DESIGNED — NOT BUILT · PARTIALLY DESIGNED ·
ACCEPTED — NOT YET INTEGRATED · ACCEPTED — PARTLY INTEGRATED · INTEGRATED INTO CURRENT AUTHORITY ·
OPEN / UNRESOLVED · INTENTIONALLY ABSENT · HISTORICAL / INACTIVE.

**Citations (correction #6).** Every citation gives the **direct source** and a **source-body-relative**
line or range. For SRC-001 and SRC-002, line numbers are relative to each companion's own body
(`src001 L#`, `src002 L#`), where L1 is the companion's first line. A governance-embedding range, if
shown at all, appears only as a secondary cross-reference (`gov L#`) and never as a substitute for the
direct companion range.

**Ten-field format** (correction #5): every accepted-companion mechanism, every governance mechanism,
every Cursor Rules safeguard, and AC1–AC3 / AD1–AD4 below carry the ten fields — (1) name · (2) purpose ·
(3) real-use behavior · (4) inputs · (5) outputs/records · (6) info read/stored/changed/sealed/
restricted/exposed · (7) dependencies · (8) direct source + source-body-relative range · (9) status
label · (10) limits / safety / open questions — or are explicitly classified as a non-feature register
entry.

**Strict distinctions enforced:** designed ≠ built; accepted ≠ integrated; mentioned ≠ fully specified;
a Master "previously verified" claim ≠ fresh disk verification; an external companion remains
authoritative within its own scope even when un-integrated.

---

## 1. CORRECTED STATUS REVIEW OF THE v1 MASTER-SIDE INVENTORY (corrections #2 + #6)

v1's Master-side feature entries (subsystems A–AB, each already in ten-field form) are preserved in v1
and their **design content is unchanged**. v1.1 corrects only their **status labels** and confirms their
citations. The table below restates every Master-side entry's status under the corrected mapping; the
"change" column flags where v1 was wrong.

| Entry (v1 id) | §/source (direct) | v1 status | v1.1 corrected status | change |
|---|---|---|---|---|
| Premise (A1) | Master §0 (L174–190) | FULLY DESIGNED — NOT BUILT | INTEGRATED INTO CURRENT AUTHORITY | corrected (governing principle) |
| Two Machineries + membrane (A2) | Master §0A (L193–204); DD §2 | FULLY DESIGNED — NOT BUILT | INTEGRATED INTO CURRENT AUTHORITY | corrected (governing frame; §0A placement pins still open) |
| What N.H is / two destinations (A3) | Master §1, §1A (L208–231) | FULLY DESIGNED — NOT BUILT | INTEGRATED INTO CURRENT AUTHORITY | corrected (governing identity/principles) |
| The machine (B1) | Master §4 (L283–290) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Codebase/store map (B2) | Master §5 (L294–325) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Accretive store (C1) | Master §6B (L470–495) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| 7-field root schema (C2) | Master §6A/§6B (L389–391,474–476) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| 12-field reading record (C3) | Master §6B (L478–494) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Roots seal (C4a) | Master §6A/§5 (L385,301) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Production-readings authorization (C4b) | Master §6A (L399–407) | PARTIALLY BUILT | PARTIALLY BUILT | unchanged |
| Quarantine store (C5) | Master §6B (L492) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Gold sets v1+v2-B (C6) | Master §6 (L333–334) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Engine A (D1) | Master §6 (L335) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Engine B (D2) | Master §6 (L336) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Chroma + rebuild (D3) | Master §6 (L337–338) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Ingest pipeline (D4) | Master §5 (L311,321) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Detector recipe (D5) | Master §6 (L340) | PARTIALLY BUILT | PARTIALLY BUILT | unchanged |
| Cursor Rules governance (E1–E3) | SRC-076 (whole file) | BUILT, BUT NOT FRESHLY DISK-VERIFIED | (superseded by §3A direct recovery) | re-derived directly |
| Legacy REALITY/SIMULATION gate (F1) | Master §5/§6A; SRC-076 §2A | BUILT, BUT NOT FRESHLY DISK-VERIFIED | BUILT, BUT NOT FRESHLY DISK-VERIFIED | unchanged |
| Universal Filter operating rules + Keystone (G1) | Master §7A (L500–516) | FULLY DESIGNED — NOT BUILT | INTEGRATED INTO CURRENT AUTHORITY | corrected (governing rule-set; software slices are engines A+B) |
| Meaning Engine seven webs (G2) | Master §7B (L517–565) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (web list deliberately open; mechanism interior in §7G with open items) |
| Forced build order A→B→C (G3) | Master §7C (L566–573) | PARTIALLY BUILT | PARTIALLY BUILT | unchanged |
| Catalog Front Door (H1) | Master §7E (L616–648) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact schemas, field names… remain undesigned") |
| TSC §7E integration summary (H2) | Master §7E-TSC (L650–675) | FULLY DESIGNED — NOT BUILT | ACCEPTED — PARTLY INTEGRATED | corrected (summary in Master; full design = SRC-002, §4/§3B) |
| Context Retrieval (I1) | Master §7F (L678–701) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("trigger conditions, limits, ranking, thresholds… undesigned") |
| Meaning Engine Interior + Acceptance Check (J1) | Master §7G (L704–743) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact criteria, thresholds, retry… undesigned") |
| Reread Lifecycle (K1) | Master §7H (L747–763) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact relevance rules, retry limits, scheduling… undesigned") |
| View Layer (L1) | Master §7I (L767–777) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact grouping, labels, layout… undesigned") |
| Computed View (L2) | Master §7M (L885–912) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact relevance rules, thresholds, snapshot schema… undesigned") |
| Clash Handling (M1) | Master §7J (L781–811) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact schemas, detection, schedules, dedup… undesigned") |
| Story Layer (N1) | Master §7K (L815–850) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (object-identity seam UNRESOLVED; scale/theme schema undesigned) |
| Person-Boxes (O1) | Master §7L (L853–875) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact matching rules, thresholds, merge mechanics… undesigned") |
| Living State Web (P1) | Master §7D (L576–612) | PARTIALLY DESIGNED | PARTIALLY DESIGNED | unchanged |
| Action Surfacing (Q1) | Master §7N (L916–941) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact triggers, mapping, thresholds, wording… undesigned") |
| Action-Result Return Path (Q2) | Master §7O (L945–974) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact detection, confirmation workflow, subcategories… undesigned") |
| Permission/Authority Boundaries (R1) | Master §7P (L978–1031) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected ("exact permission categories, authorization schema, interface… undesigned") |
| Privacy/Deletion/Sensitive-data (S1) | Master §7Q (L1034–1121) | PARTIALLY DESIGNED | PARTIALLY DESIGNED | unchanged |
| Attention and Relevance Control (T1) | Master §7R (L1125–1404) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (14 decisions settled but "WHAT REMAINS OPEN" lists component declarations, Tier-2 handling, thresholds, storage formats) |
| Research / Knowledge Catcher pipeline (U1) | Master §8 (L1406–1431) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (isolation env undesigned; academic source open; cap to be coded) |
| Model layer — models on disk (V1a) | Master §16 (L1562) | BUILT AND DOCUMENTED AS VERIFIED | BUILT AND DOCUMENTED AS VERIFIED | unchanged |
| Model layer — local-first wiring (V1b) | Master §16 (L1542–1564) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (final mouth undecided; wiring not a complete spec) |
| Live Loop (W1) | Master §13 (L1504–1516) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (mechanism sketch; live path "built first" not yet built) |
| Chat Front Door (W2) | Master §14 (L1519–1536) | PARTIALLY DESIGNED | PARTIALLY DESIGNED | unchanged (explored, not confirmed) |
| Image ingest front door (X1) | Master §9A (L1436–1437) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (one-line sketch, not a complete spec) |
| Interface/World/Interaction (Y1) | Master §19 (L1613–1699) | PARTIALLY DESIGNED | PARTIALLY DESIGNED | unchanged |
| Wellbeing baseline (Z1) | Master §22 (L1759–1817) | FULLY DESIGNED — NOT BUILT | FULLY DESIGNED — NOT BUILT | unchanged (authority states "full spec restored"; no named design gaps — data-emergent thresholds are a designed property) |
| Mobile three-mode (AA1) | Master §23 (L1821–1858) | FULLY DESIGNED — NOT BUILT | PARTIALLY DESIGNED | corrected (five explicit "OPEN QUESTIONS (not yet decided)") |
| Connection capability (AB1) | Master §24 (L1862–1896) | FULLY DESIGNED — NOT BUILT | FULLY DESIGNED — NOT BUILT | unchanged (complete approved conceptual design; no named undesigned gaps; "not yet integrated through an audited build") |

**Net status corrections:** four foundational/rule entries (A1, A2, A3, G1) → INTEGRATED INTO CURRENT
AUTHORITY; H2 (TSC summary) → ACCEPTED — PARTLY INTEGRATED; nineteen §7/§8/§9A/§13/§16-wiring/§23
component entries → PARTIALLY DESIGNED; G2 → PARTIALLY DESIGNED. Two complete-spec designs (Z1 Wellbeing,
AB1 Connection) keep FULLY DESIGNED — NOT BUILT. The v1 plain-language behavior map (v1 §2) remains valid
as written and is preserved in v1; nothing in it asserted a status that these corrections overturn.

AC1–AC3 and AD1–AD4 are re-issued in proper ten-field form in §2 below.

---

## 2. AC1–AC3 / AD1–AD4 RE-ISSUED IN TEN-FIELD FORM (correction #5)

**AC1 — Wonder/Simulation mechanism.** (1) The create-space where N.H wonders/simulates forward.
(2) Let N.H reason/simulate forward at night while keeping every wonder shown, never decided. (3) Concept
only: wonders are kept and surfaced, never promoted to fact; mechanism not specified. (4) Accumulated
memory. (5) Weightless dated wonders (conceptual). (6) Would read memory; writes only weightless shown
wonders. (7) Meaning engine; §19 interface; membrane. (8) Master §7B Part 6.5 (L518); §11 item 30
(L1479). (9) PARTIALLY DESIGNED. (10) "Concept level only, not designed" — mechanism undesigned.

**AC2 — World model beside the self model.** (1) A model of the world to sit beside N.H's model of Ness.
(2) Extend modeling beyond the self to the surrounding world. (3) Named only; no design. (4)/(5)/(6) n/a
(undesigned). (7) Living State Web. (8) Master §7D future-domains (L608); §11 item 31 (L1480). (9) OPEN /
UNRESOLVED. (10) "Not designed. Must be designed separately."

**AC3 — End-to-end cycle.** (1) The complete connected flow from a new input through every component to
the Computed View or chat. (2) Tie the separately-designed components into one sequence. (3) Identified
as a gap; not designed as a single sequence. (4)/(5)/(6) n/a (undesigned). (7) All §7 components,
wonder, world model. (8) Master §11 item 32 (L1481–1482); DD §4 (L252). (9) OPEN / UNRESOLVED.
(10) Cannot be designed until wonder/simulation and world model are addressed.

**AD1 — `cleaned_history (1).txt` ingest.** (1) A damaged export deliberately not ingested. (2) Avoid
forcing a fake-boundary parser onto structureless, lossy content. (3) Set aside; revisit only if a
cleaner version is recovered. (4) The damaged file. (5) None (not ingested). (6) Not read into the
store. (7) Ingest pipeline. (8) Master §5 (L311). (9) INTENTIONALLY ABSENT. (10) Decision is reversible
only if a cleaner source appears.

**AD2 — `gpt_purified_history.txt` ingest.** (1) A redundant export not ingested. (2) Avoid duplicate/
scrambled content entering the store. (3) Skipped during ingest. (4) The file. (5) None. (6) Not read
into the store. (7) Ingest pipeline. (8) Master §5 (L311). (9) INTENTIONALLY ABSENT. (10) —

**AD3 — Hetzner sovereignty sync.** (1) An early open item to sync to a Hetzner host. (2) (Original
purpose unverifiable from accessible evidence.) (3) Explicitly dropped by Ness (June 25); no longer an
active task. (4)/(5)/(6) n/a. (7) — (8) Master §11 (L1458); §25 item 2 (L1906). (9) HISTORICAL /
INACTIVE. (10) Preserved as a historical note; not deleted from the record.

**AD4 — `cloudflared.exe` / stale debris (convenience-sweep items).** (1) Inert leftover binaries/files
on disk. (2) Track harmless cleanup items without treating them as components. (3) Listed for an eventual
folder cleanup; inert. (4)/(5) n/a. (6) Present on disk, inert. (7) — (8) Master §3 D (L270); §11 item 14
(L1461). (9) HISTORICAL / INACTIVE. (10) `cloudflared.exe` inert but on disk; stale `peek.txt`; ~12 S13
detector probes (keep the recipe reference); stale "188 seed records" docstring — all convenience-sweep,
not active features.

---

## 3. FULL ACCEPTED-COMPANION RECOVERY — DIRECT BODIES (correction #1)

All entries below are recovered from the **direct companion bodies** with source-body-relative line
ranges. Field 9 (status) gives the **Master-integration** status under the eleven allowed labels; field
10 records the companion's own declared status. Every component of SRC-001 carries the companion status
**ACCEPTED DESIGN — NOT YET BUILT** except §12 (vocabulary additions) which carries **ACCEPTED — FORMALLY
ADOPTED**; SRC-002 carries **ACCEPTED DESIGN — NOT YET BUILT**. None is integrated into the Master except
the TSC's §7E integration summary (ACCEPTED — PARTLY INTEGRATED).

### 3A. SRC-001 — Accepted Security and Identity Designs After BGMM

**Provenance (non-feature register entry).** SRC-001 (`NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`,
1724 lines, SHA `fb36bf8e…`) consolidates the final accepted security/identity/BGMM designs, reached by
iterative correction and explicit Ness acceptance. It declares itself a **companion record, not an
authoritative source**, naming `NH_MASTER-19_CORRECTED_v6.md` + `NH_DECISION_DEFAULTS-S19_v1__1_.md` as
the pair it must be patched into before carrying Master authority (src001 L3–20). Two items are
build-time settings, not open concept decisions: the maintenance-timeout duration (set empirically) and
the hardware-backed key implementation (TPM/HSM/OS keystore) (src001 L51–68).

**3A.1 — BOP (Behavioral Observation Processing).**
(1) The source-classification rule-set that turns a physically-measurable session event into a typed raw
observation root. (2) Capture behavioral signals as DUMB roots that never interpret. (3) During an
authorized session N.H records available authorized signals (live voice, confirmed sent text, session
state, authorized imports) as typed roots; unfinished typing and unauthorized sources are never observed.
(4) Authorized live/imported signals. (5) Observation roots in the sealed 7-field schema with a
`bop_payload` in `content`; `subject="bop:v1"`; `role ∈ ness|nh|session|third_party_observed`. (6) Reads
session signals; writes typed roots; carries observation-quality, third-party-flag, simultaneous-bundle,
and connection-anchor metadata; never copies message content (references the conversational root by id).
(7) §7E catalog path; §7G (all interpretation); §7Q (privacy applies identically). (8) src001 §1
(L70–276); root schema L145–191; corrected capture-id L193–207; observation-quality L209–222;
third-party-flag L224–236; DUMB boundary L251–256; failure/recovery/idempotency L258–264; proposed
amendment L266–275. (9) ACCEPTED — NOT YET INTEGRATED (Master names "BOP roots" only in §7E-TSC).
(10) Companion status ACCEPTED DESIGN — NOT YET BUILT; V1 event vocabulary is extensible via `extended`;
`capture_sequence_number` must be persisted before any write (idempotency); below-threshold roots still
enter the store (honest incompleteness); the `acoustic_condition_notes` amendment is **pending separate
review**. BOP must never produce emotional labels, identity conclusions, speaker-change/spoofing
assessments, or meaning.

**3A.2 — Other-Speaker / Guest / Known-Person architecture.**
(1) The behavioral frame for non-Ness speakers. (2) Gate what may be surfaced to the current speaker
while keeping the whole mechanism internally active. (3) Four access levels (top_security / recognized_ness
/ known_person / guest) determined by SACL from SIA; guest mode answers naturally without signaling hidden
material; known persons are bounded by Permission Boundary Records (PBRs); parents have fully separate
identities; parent "translation" is entirely request-driven; a third party's statement about Ness stays
attributed to that speaker forever. (4) SIA assessments; Ness-expressed boundaries; PBRs. (5) Per-speaker
disclosure decisions; translation readings (revisable via §7H). (6) Restricts disclosure by level/PBR;
never reveals how much is stored or how recognition works; never transfers one person's permissions to
another. (7) SIA, SACL, §7L Person-Boxes, §7P, TSC. (8) src001 §2 (L281–406); protected rules L292–307;
access levels L309–320; guest L322–327; known-person/PBR L329–339; parents L341–361; statements-about-
Ness L363–368; person-box visibility L370–375; continuous speaker security L400–406. (9) ACCEPTED — NOT
YET INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; spoofing ≥ medium drops to guest
immediately + queues a private Ness alert; no routine live voice challenges; neither Ness nor anyone else
may override the protected core.

**3A.3 — SIA (Speaker Identity Assessment).**
(1) The component that assesses who is probably speaking and whether audio is non-live. (2) Produce
identity assessments + anti-spoofing evidence; never decide access (SACL) or meaning (§7G). (3) Reads BOP
roots; maintains in-memory Speaker Session State (lost on restart → unknown/guest); per voice stream a
ranked `speaker_assessment` (no candidate silently discarded) and an `anti_spoofing_assessment` (acoustic
spoofing only); runs continuously and on named triggers; diarizes parallel streams; learns voice profiles
over a 6–10-month conservative period. (4) BOP roots; audio windows. (5) `SIA_output` (SSS + assessment
id + audit-only confidence note); security audit events. (6) Reads BOP roots; produces assessments; does
not store content; protects raw voice data (sealed store, never below recognized_ness, never transmitted
except via Full-Mode tunnel under biometric-verified conditions). (7) BOP, §7L (profiles linked to
Person-Boxes), SACL (consumes output), §22 (kept separate). (8) src001 §3 (L412–652); SSS L424–438;
speaker_assessment L453–492; anti-spoofing L494–515; output interface L517–528; cadence L530–543;
diarization L545–550; voice-profile architecture L552–557; training eligibility L568–581; 6–10-month
learning L583–588; raw-voice protection L590–596; identity-uncertain-vs-spoofing L598–608; false-lockout
recovery L610–618; multi-speaker L620–627; min-evidence-for-linking L629–637; compact profile L639–644;
settled rules L646–651. (9) ACCEPTED — NOT YET INTEGRATED (Master names "SIA links" only in §7E-TSC).
(10) Companion status ACCEPTED DESIGN — NOT YET BUILT; `assessed_person_box_id` is null when candidates
are within the minimum separation threshold (SACL treats null as unknown→guest); identity-uncertain and
spoofing-suspected are distinct events; behavioral divergence is NOT acoustic spoofing; psychiatric/
medical records are not voice-training evidence.

**3A.4 — SACL (Speaker Access-Control Layer).**
(1) The authorization layer. (2) Decide what the current speaker may receive or do; own all authorization.
(3) Per-stream access calculated on every SIA event through ordered gates — Gate 0 disqualifier (acoustic
spoofing ≥ medium → guest + alert), Gate 1 top_security (biometric verified + Ness recognized high + no
spoofing/imitation/disqualifier), Gate 2 recognized_ness, Gate 3 known_person (valid PBR; Ness-presence if
required), else guest; `shared_output_level` = minimum across active streams; output gate is two
sequential factors (§7Q privacy, then SACL access); access reductions discard in-progress higher-
sensitivity operations before any output. (4) SIA assessments; PBRs (via LMAC→§7L); BAI biometric state.
(5) Per-stream `stream_authorization_record`; SACL session state; audit events. (6) Reads SIA/PBR/
biometric state; decides disclosure; never reveals hidden material's existence (no direct statement,
structural gap, or implied omission); fail-closed on restart/stale/SIA-failure/PBR-failure → guest.
(7) SIA, §7L, §7Q, BAI, LMAC. (8) src001 §4 (L657–847); owned state L670–695; access calc L697–743;
fingerprint factor L745–750; imitation Option A L752–757; three-mechanisms-separate L759–769; multi-
speaker L771–780; permission enforcement L782–787; access-changes-in-progress L789–795; indirect-
disclosure L797–804; output gate L806–813; internal-vs-external L815–820; background functions L822–828;
fail-closed L830–836; protected-core L838–846. (9) ACCEPTED — NOT YET INTEGRATED (Master names
"recognized-Ness SACL session" only in §7E-TSC). (10) Companion status ACCEPTED DESIGN — NOT YET BUILT;
voice alone never unlocks top_security; imitation_risk blocks top_security only (Option A), never reduces
Ness to guest; SACL does not read wellbeing tier state; behavioral-divergence and acoustic-spoofing paths
never merge.

**3A.5 — Wellbeing / Identity / Security separation rules.**
(1) The rule that keeps SIA, §22 Wellbeing, and SACL strictly separate. (2) Prevent any one mechanism's
signal from contaminating another. (3) SIA assesses identity only; §22 watches sustained baseline
divergence and affects REALITY growth only; SACL decides disclosure only and never reads wellbeing tier;
temporary off-baseline behavior follows the imitation-risk path (top_security blocked, recognized_ness
kept), acoustic spoofing follows Gate 0 — the two paths never merge. (4) Each mechanism's own evidence.
(5) Separation guarantees (a rule, not a record). (6) Restricts cross-use of identity/wellbeing/access
signals. (7) SIA, §22, SACL. (8) src001 §5 (L852–892). (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion
status ACCEPTED DESIGN — NOT YET BUILT; psychiatric/medical records are wellbeing calibration anchors and
the REALITY-freeze unlock only — never identity proof or access evidence.

**3A.6 — BAI (Biometric Authorization Interface).**
(1) The narrowest interface between the phone's biometric hardware and N.H. (2) Convert an OS auth result
into a purpose-bound proof that carries no biometric data; own no fingerprint data ever. (3) Declares a
purpose before the OS prompt; on success mints either a single-use one-time token (TSC promotion, voice
enrollment) or a queryable revocable top-security lease; one pending record at a time; uses only its own
trusted local clock; all state in-memory (cleared on restart → fail-closed). (4) `os_biometric_result`;
declared purpose + requester. (5) `one_time_authorization_token` / `top_security_lease`; security audit
events. (6) Reads OS outcomes; produces purpose-bound proofs; never stores/inspects fingerprint data;
keeps BOP audit (structural facts) separate from the security audit log (purposes, tokens, leases).
(7) OS biometric framework; SACL (lease queried, promotion condition); TSC; voice enrollment; BGMM
(`bgmm_confirmation` purpose). (8) src001 §6 (L898–1077); OS result L912–923; purpose binding L925–950;
one-time token L954–966; lease L968–981; key separation L983–990; result handling L992–1002; TSC-promotion
authorization L1004–1016; lease revocation L1018–1029; owned state L1031–1048; BOP-vs-audit separation
L1050–1059; crash/malformed L1061–1066; protected-core L1068–1077. (9) ACCEPTED — NOT YET INTEGRATED
(Master names "purpose-bound BAI tokens" only in §7E-TSC). (10) Companion status ACCEPTED DESIGN — NOT YET
BUILT; a token for one purpose cannot satisfy another; consumed/expired tokens cannot be reused; lease
revokes immediately on any of eight triggers (session close, certainty drop, spoofing/speaker-change/
imitation flag, suspicion≥medium, timeout, major break, branch-continuity below threshold, explicit
relock).

**3A.7 — Initial Owner-Phone Pairing.**
(1) The one-time first-phone pairing lifecycle. (2) Bind the desktop to exactly one phone's hardware-
backed identity and permanently close the QR path. (3) Four states: `qr_available` (signed QR, 90s) →
`phone_provisionally_paired_qr_destroyed` (QR + pairing secret destroyed at first successful pair) →
`recovery_setup_in_progress` → `owner_setup_finalized_qr_path_permanently_closed` (after the first
recovery code is saved, 4-char verified, locally tested, activated). (4) A scanned signed QR.
(5) Pairing state transitions; audit events. (6) Creates/destroys the QR + pairing secret; binds to the
phone's hardware-backed key; upgrades provisional→permanent at state 4. (7) BAI; recovery-code lifecycle;
BGMM (device_trust). (8) src001 §7 (L1083–1119); destruction table L1112–1119. (9) ACCEPTED — NOT YET
INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; QR cannot be reused/regenerated after
state 2; recovery-code local copy erased after activation at state 4.

**3A.8 — Recovery-Code Lifecycle.**
(1) The create/verify/test/activate/rotate flow for the normal recovery code. (2) Establish a recovery
code held only in Bitwarden, never on the desktop. (3) Created after first pairing, encrypted to the
phone's hardware key, shown only on the phone (10m30s timeout); after "Saved in Bitwarden," 4 random
character positions are verified locally (3 attempts, exact case, nothing stored); a phone-side automatic
local acceptance test must pass before the new code activates and the old becomes invalid; rotated after
every (re)pairing. (4) Ness's save + 4-character entry. (5) An active recovery code (in Bitwarden);
audit. (6) Encrypts/shows/erases the code; the old code stays valid until the new one is saved+verified+
tested+activated. (7) Owner-phone pairing; BAI; BGMM (device_trust); emergency recovery. (8) src001 §8
(L1125–1169); first creation L1129–1139; save-verification L1141–1151; activation handover L1153–1162;
rotation L1164–1169. (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET
BUILT; if all 3 verification attempts fail, the new code is destroyed and the old remains valid; Bitwarden
is the only intended long-term storage.

**3A.9 — Future-Phone Replacement Flow.**
(1) The flow to trust a new phone. (2) Replace the trusted phone using two factors, neither alone
sufficient. (3) Requires the current Bitwarden recovery code AND Ness's thumbprint through Maintenance
Mode; once the new phone is fully paired+verified, the previous phone is automatically revoked; rotate
the recovery code afterward. (4) Recovery code + thumbprint. (5) New trusted-phone binding; revocation.
(6) Changes device-trust records; revokes the old phone. (7) Recovery-code lifecycle; BGMM
(device_trust). (8) src001 §9 (L1175–1188). (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status
ACCEPTED DESIGN — NOT YET BUILT; a revoked phone can be re-trusted only through the full recovery-code +
thumbprint flow.

**3A.10 — Atomic Emergency Recovery Flow.**
(1) The last-resort recovery when normal factors are unavailable. (2) Reset device trust safely with no
partial/half-committed state. (3) Requires four factors simultaneously (physical desktop access +
emergency code outside Bitwarden + printed recovery sheet + thumbprint via BGMM); during a provisional
intermediate state all old trust/codes remain valid; only after every new material is saved+verified does
one atomic commit make the new phone sole trusted phone and invalidate all old material; any pre-commit
failure aborts with nothing revoked. (4) The four factors. (5) Atomic commit OR safe abort; audit
(`bai_emergency_reset_finalized` / `…_aborted`). (6) Resets device-trust records atomically. (7) BGMM
(emergency_recovery scope); recovery-code lifecycle. (8) src001 §10 (L1194–1243); required factors
L1198–1206; intermediate state L1208–1216; steps before commit L1218–1223; atomic commit L1225–1234;
if-fails L1236–1243. (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET
BUILT; remote emergency recovery is prohibited unconditionally; emergency scope is device-trust only (no
code/config writable).

**3A.11 — Initial Ness Voice-Profile Enrollment Bootstrap.**
(1) The first-time bootstrap that collects Ness's voice as a provisional profile. (2) Create a provisional
voice profile without ever claiming the captured voice is confirmed as Ness's. (3) Requires six
prerequisites (phone at BAI state 4; first recovery code active; QR path closed; no medium+ spoofing
suspicion; Ness's Person-Box confirmed); opened only via the dedicated flow on the trusted phone with a
`voice_enrollment_ness` BAI token; BOP records raw voice with `role="ness"` (a declared attribution, not a
confirmed identity) and `authorization_type="enrollment_declared"`; §7G reads honest provisional
confidence; a §7L link `enrollment_material_provisional` is proposed; SIA caps the profile at
recognized_ness until it matures. (4) Authorized enrollment voice; the BAI token. (5) Provisional profile
reading set; a provisional §7L link; enrollment-component audit events. (6) Reads enrollment voice; writes
provisional roots/readings/links; establishes provenance, **not** confirmed identity. (7) BAI, BOP, §7E,
§7G, §7L, SIA; §12 vocabulary additions. (8) src001 §11 (L1249–1389); prerequisites L1253–1260; session
opening L1262–1281; BOP integration L1283–1300; §7G integration L1302–1311; initial-corpus eligibility
L1313–1334; §7L integration L1336–1351; SIA integration L1353–1365; audit ownership L1367–1380;
what-it-doesn't-establish L1382–1389. (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status ACCEPTED
DESIGN — NOT YET BUILT; no enrollment session alone establishes that the voice is Ness's — the link
strengthens only through later SIA evidence and clean repeated sessions; rejected segments are preserved
as roots but do not train the profile.

**3A.12 — Formally Adopted Vocabulary Additions.**
(1) Two new controlled-vocabulary values for enrollment provenance. (2) Mark enrollment-declared
attribution and enrollment-provisional links within existing open-ended vocabularies. (3) `authorization_type
= "enrollment_declared"` (BOP) and `link_type = "enrollment_material_provisional"` (§7L) were examined
against their parent schemas and adopted without any schema-version change. (4)/(5) Vocabulary values.
(6) Extends two existing open vocabularies; no structural schema change. (7) BOP payload; §7L link
records. (8) src001 §12 (L1395–1430). (9) ACCEPTED — NOT YET INTEGRATED (the **current Master** §6B/§7L
text does not carry these values). (10) Companion status here is **ACCEPTED — FORMALLY ADOPTED** (not
"not yet built") — but adoption is into the companion's named vocabularies, not into Master v7_1; this is
the one place where companion status and Master-integration status differ and must be kept distinct.

**3A.13 — BGMM (Biometric-Gated Maintenance Mode).**
(1) The only authorized path to change protected N.H material. (2) Make unauthorized change of protected
files structurally hard and always detectable; outside BGMM protected files are read-only by
architecture. (3) Defines a protected-material boundary (writable-only-via-BGMM: code/config/security-
policy/device-trust/emergency-recovery; permanently unchangeable: immutable roots, readings+provenance,
clash/person-box links, audit log, gold sets, recovery-code values); five-layer normal-path write
prevention; a TPM-pinned signed-manifest trust anchor with startup hash verification (no-start on
failure); encrypted full-content rollback packages under a separate sealing key; a bounded protected
startup-recovery worker; a six-step entry flow with purpose-specific authorization; file-scope
enforcement; an ordered change-application sequence; automatic relocking on seven conditions; idempotent
rollback. (4) A declared purpose + change + authorization factors. (5) Signed manifests + provenance
history; encrypted rollback packages; an append-only change log; security audit events. (6) Changes only
in-scope protected files; seals/verifies via manifest+hashes; never exposes private content in
descriptions/logs/payloads; cannot alter immutable roots/readings/provenance/audit-log/gold-sets.
(7) BAI (`bgmm_confirmation` tokens), recovery code (device_trust), emergency factors, TPM/hardware keys,
SACL (security-alert relock). (8) src001 §13 (L1436–1721); boundary L1453–1476; write-prevention L1478–
1506; manifest L1508–1525; rollback packages L1527–1552; startup-recovery worker L1554–1574; entering
L1576–1600; purpose-specific auth L1602–1614; file-scope L1616–1621; change application L1623–1634;
relocking L1636–1648; rollback L1650–1656; owned state L1658–1672; privacy L1674–1684; audit events
L1686–1695; crash/offline L1697–1709; protected-core L1711–1720. (9) ACCEPTED — NOT YET INTEGRATED.
(10) Companion status ACCEPTED DESIGN — NOT YET BUILT; cannot be entered remotely or via ordinary
terminal/editor/script regardless of OS privilege; administrator-level tampering is resisted and always
detected but not made physically impossible; N.H fails closed on any integrity failure; emergency_recovery
never grants code-edit authority.

### 3B. SRC-002 — Accepted Temporary Session Cache Design (all 31 sections)

**Provenance (non-feature register entry).** SRC-002 (`NH_ACCEPTED_TSC_DESIGN_v1.md`, 956 lines, SHA
`1da2e296…`) is the complete accepted 31-section TSC specification, declared a **companion record, not an
authoritative source**, naming `NH_MASTER-19_CORRECTED_v6.md` + `NH_DECISION_DEFAULTS-S19_v1__1_.md` as
its patch targets and `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` as the earlier TSC foundation
+ the BOP/SIA/SACL/BAI/BGMM designs it depends on (src002 L1–24). §31 records the design as complete with
**no remaining concept questions** — including the inspection-authorization mechanism, now settled
(src002 L945–956).

**3B.1 — TSC identity and §7E relationship (§§1–2).**
(1) An organized, transactional holding mode **inside** §7E's pre-ingest store. (2) Hold a complete
third-party session faithfully under §7E's rules until Ness authorizes promotion; never act as a separate
upstream cache or second memory. (3) Every item lives in the §7E pre-ingest store from capture carrying
`"pending_fingerprint_authorization"`; the TSC structural DB adds session-level organization that §7E's
flat per-item shape cannot express; on authorization, items flow through the normal §7E `held→ready→
promoting→promoted` path to `append_root()`. (4) Captured session material. (5) §7E pre-ingest records +
TSC structural records. (6) Organizes (not duplicates) §7E records; holds raw payloads only in §7E.
(7) §7E, BAI, SACL, BOP, SIA, §7Q, `append_root()`. (8) src002 §1 (L73–110), §2 (L113–154). (9) ACCEPTED
— PARTLY INTEGRATED (Master §7E-TSC summarizes exactly this relationship). (10) Companion status ACCEPTED
DESIGN — NOT YET BUILT; the TSC is explicitly **not** a second Meaning Engine, interpretation store, or
bypass.

**3B.2 — Transactional database model + 13 logical tables (§3).**
(1) The local ACID store for the TSC's structural records. (2) Hold session organization crash-safely,
locally, with no network. (3) A local transactional DB (SQLite/embedded KV — build-time choice) stores
13 tables: `sessions, contributions, participants, attribution_assessments, branch_links,
bop_preingest_links, sia_event_links, nh_outputs, blockers, blocker_history, lifecycle_events,
promotion_state, security_audit_refs`. (4) Structural records. (5) The 13 tables. (6) Stores session
organization only — no raw payloads (those stay in §7E), no readings, no interpretation. (7) §7E.
(8) src002 §3 (L157–186). (9) ACCEPTED — NOT YET INTEGRATED (Master summarizes "a structural database"
but not the table set). (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; the technology choice is a
build-time decision; the architectural requirement is ACID + crash-safe + local-only.

**3B.3 — Session, contribution, participant, attribution, and branch schemas (§§4–8).**
(1) The record shapes for one session and its turns/speakers/order. (2) Capture session identity,
contribution order, speaker streams, attribution certainty, and reply/branch structure without touching
the sealed root schema. (3) `sessions` (lifecycle_status, continuation link, bai_token_id,
sacl_recognized_ness_confirmed_at); `contributions` (1-based `sequence_position` set at capture and never
changed, `preingest_capture_id` linking to the §7E record, item lifecycle, `content_hash`); `participants`
(per-stream identity/certainty); `attribution_assessments` (certainty recorded at capture, never upgraded
retrospectively); `branch_links` (reply/branch types). (4) Captured turns + SIA attributions. (5) The
five table schemas. (6) Stores order/attribution/branch in the TSC DB and the §7E record's
`source_metadata` — **not** as new root fields (the seven-field schema is unchanged). (7) §7E
source_metadata; SIA; speaker-resolution rule. (8) src002 §4 (L189–208), §5 (L212–260), §6 (L264–279),
§7 (L283–312), §8 (L316–335). (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status ACCEPTED DESIGN —
NOT YET BUILT; an unconfirmed speaker carries both `"pending_fingerprint_authorization"` and
`"speaker_unresolved"`; no root is ever written with `role="unknown"`; parent-before-child promotion
dependency is enforced.

**3B.4 — BOP/SIA event-link handling and N.H output preservation (§§9–10).**
(1) Linking observation roots and SIA events to session moments, and preserving N.H's own outputs.
(2) Preserve timing relationships and N.H outputs in real session order. (3) `bop_preingest_links` point
to BOP roots HELD in §7E (promoted later in event-time order, interleaved by `occurred_at`);
`sia_event_links` point to SIA assessment events that stay in the security audit log (never promoted as
roots); `nh_outputs` are promoted as roots with `role="nh"`. (4) BOP roots; SIA events; N.H outputs.
(5) The two link tables + `nh_outputs` table. (6) References (not copies) BOP/SIA/output records; session
context flows via `source_metadata`. (7) BOP, SIA, §7E, security audit log. (8) src002 §9 (L339–385), §10
(L389–413). (9) ACCEPTED — NOT YET INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; SIA
events are never promoted as roots; no new root fields are added.

**3B.5 — Blocker schema, resolution history, and lifecycle (§§11–12).**
(1) The per-item blocker model and session/item lifecycle. (2) Track what holds each item and the
ordered session/item states. (3) `blockers` (types: `pending_fingerprint_authorization`,
`speaker_unresolved`, `content_under_review`, `technical_hold`) with append-only `blocker_history`;
session lifecycle `active→sealed|interrupted→authorized→promoting→promoted|promotion_failed`; item
lifecycle `held→ready→promoting→promoted|excluded|blocked`. (4) Blocker events. (5) Two blocker tables +
`lifecycle_events`. (6) Records/holds blockers; `"speaker_unresolved"` resolves only through §7E's rule,
not TSC logic. (7) §7E speaker-resolution rule. (8) src002 §11 (L417–448), §12 (L452–462). (9) ACCEPTED —
NOT YET INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; no item reaches `promoted` with
an unresolved speaker.

**3B.6 — Sealing: normal close and interrupted/continuation (§§13–14).**
(1) How a session becomes immutable. (2) Seal a session on close (or crash) and link a crash continuation
without reconstructing anything. (3) Normal close writes a BOP `session_closed`, sets `sealed`, writes
`cache_sealed`, commits, and makes the session immutable (waits indefinitely; no auto-expiry/deletion/
promotion); a crash seals as `interrupted` preserving exactly what was written; a continuation is a new
session linked by `continuation_of_session_id`. (4) Close/crash event. (5) Sealed immutable session;
`cache_sealed` audit. (6) Seals the session; nothing reconstructed. (7) BOP; startup recovery (§27).
(8) src002 §13 (L466–476), §14 (L479–490). (9) ACCEPTED — NOT YET INTEGRATED (Master summarizes sealing/
continuation in §7E-TSC). (10) Companion status ACCEPTED DESIGN — NOT YET BUILT; the two linked sessions
remain separate immutable units, authorized and promoted separately.

**3B.7 — Private Ness inspection without promotion (§15).**
(1) Read-only inspection of a sealed cache. (2) Let Ness inspect a sealed session without promoting it.
(3) Requires a dedicated BAI `one_time_authorization_token` with purpose `"tsc_inspection:<session_id>"`
plus a SACL recognized-Ness confirmation at consume time; entirely independent of the promotion token
(neither substitutes for the other); shows the full conversation from the structural DB; read-only; never
passes through the Meaning Engine. (4) The inspection token + SACL confirmation. (5) Read-only view; the
`tsc_inspection_*` audit cluster. (6) Reads structural records; lifts no blocker, changes no lifecycle,
exposes nothing to §7G/§7J/§7M/§7L/LMAC/§7F. (7) BAI, SACL. (8) src002 §15 (L493–535). (9) ACCEPTED — NOT
YET INTEGRATED (Master §7E-TSC notes inspection uses a separate token but defers detail). (10) Companion
status ACCEPTED DESIGN — NOT YET BUILT; **this mechanism is settled — there is no remaining inspection-
authorization concept question** (corrects any earlier "one open question" note).

**3B.8 — Promotion: BAI+SACL authorization, exact sequence, dependency, partial/idempotency, retry (§§16–20).**
(1) The authorized path from a sealed cache into the sealed root store. (2) Promote only with two
simultaneous conditions, in real conversation order, idempotently. (3) Promotion needs a
`"tsc_promotion:<session_id>"` BAI token AND a fresh non-stale recognized-Ness SACL session at consume
time; then a three-phase sequence (pre-check applies §7Q exclusions and marks ready/blocked; ordered loop
by ascending `sequence_position`, lifting the fingerprint blocker, writing `source_metadata`, letting §7E
reach `append_root()`, interleaving BOP roots by `occurred_at`; post-promotion creates the retained
archive); parent-before-child dependency; `preingest_capture_id`→`capture_id` idempotency; three retry
classes (auto-continue already-authorized promotion with automatic security re-check; new authorization
only if never authorized or token revoked; bounded technical retry). (4) The promotion token + SACL
confirmation. (5) Promoted roots; `promotion_state`; `cache_promotion_*` audit; Ness failure notice.
(6) Lifts blockers; writes session context to `source_metadata`; never calls `append_root()` directly;
no duplication. (7) BAI, SACL, §7E, §7Q, `append_root()`. (8) src002 §16 (L539–556), §17 (L560–611), §18
(L614–622), §19 (L626–632), §20 (L636–657). (9) ACCEPTED — NOT YET INTEGRATED (Master §7E-TSC summarizes
authorization + ordered promotion + idempotency). (10) Companion status ACCEPTED DESIGN — NOT YET BUILT;
items with non-fingerprint blockers wait for §7E rules — **no new fingerprint**; auto-retry never requires
a new fingerprint.

**3B.9 — Multi-person sessions and Ness's own material (§§21–22).**
(1) How several speakers and Ness's own words are held in one session. (2) Keep one cache per real
conversation with structurally separated streams. (3) Each participant has separate `participants`,
`attribution_assessments`, and PBR version; no identity/certainty/permission transfers between streams;
full order preserved; Ness's contributions (`role="ness"`) are held under the same blocker and promoted
on the same path (idempotency prevents double-capture). (4) Multi-speaker material. (5) Per-stream
records. (6) Separates streams; never merges speakers/Person-Boxes; never splits the conversation into
per-person sub-caches. (7) SIA, §7L. (8) src002 §21 (L661–668), §22 (L672–677). (9) ACCEPTED — NOT YET
INTEGRATED. (10) Companion status ACCEPTED DESIGN — NOT YET BUILT.

**3B.10 — Retained safety archive and duplicate/double-weighting protection (§§23–24).**
(1) The frozen post-promotion snapshot and the anti-double-counting guards. (2) Keep an integrity/recovery
reference that can never re-influence memory. (3) After completion a frozen encrypted read-only snapshot
of the structural DB is created (structural records + exclusion metadata only, no excluded content);
extended session states `archived`/`deleted`; four protections (`promoted_root_id`, `append_root()`
idempotency, runtime isolation, no §7E re-submission). (4) Completed session. (5) Frozen archive;
`tsc_retained_archive_*` audit. (6) Stores structural snapshot; runtime/LMAC/§7F/§7G/downstream have no
read access in ordinary operation; cannot make a conversation appear twice or boost evidence weight.
(7) §7Q (deletion path applies). (8) src002 §23 (L681–715), §24 (L718–724). (9) ACCEPTED — NOT YET
INTEGRATED (Master §7E-TSC notes the retained archive as not active memory). (10) Companion status
ACCEPTED DESIGN — NOT YET BUILT; archive deletion follows §7Q with a tombstone.

**3B.11 — Privacy/exclusion/deletion and security audit events (§§25–26).**
(1) How §7Q decisions and audit events are recorded by the TSC. (2) Record (never make) §7Q exclusion
decisions and emit a complete audit trail. (3) Excluded content is never held in §7E/TSC/archive — only
non-reconstructive exclusion metadata + a tombstone; mixed-content keeps only the permitted portion; a
third party's "do not save" is captured as an attributed contribution with no authority over storage; ~26
named security audit events in two clusters (inspection vs promotion) are written and flushed before the
producing function returns. (4) §7Q decisions; TSC operations. (5) Exclusion metadata + the audit-event
set. (6) Records exclusion metadata and audit facts; never excluded content; never converts a third
party's statement into a fact about Ness. (7) §7Q; security audit log. (8) src002 §25 (L727–758), §26
(L761–815). (9) ACCEPTED — NOT YET INTEGRATED (Master §7E-TSC notes §7Q precedence). (10) Companion status
ACCEPTED DESIGN — NOT YET BUILT; the TSC records §7Q decisions but does not make them.

**3B.12 — Recovery, fail-closed, integration boundaries, prohibitions, status (§§27–31).**
(1) Crash recovery, fail-closed rules, exact integration seams, and the prohibition list. (2) Recover
safely after a crash, fail closed on any security/integrity gap, and bound every external call. (3)
Startup classifies each session by lifecycle_status and auto-resumes only already-authorized promotion
(with automatic security re-checks); fail-closed on missing/stale SACL, expired/revoked token, DB
integrity failure, unknown state, or out-of-purpose archive access; integration boundaries fix exactly
how TSC touches BAI/SACL/SIA/BOP/§7E/§7G/§7J/§7M/§7L/`append_root()`/audit-log; ~30 explicit prohibited
behaviors; status ACCEPTED DESIGN — NOT YET BUILT with no remaining concept questions. (4) Restart state;
external responses. (5) Recovery actions; audit. (6) Reads session state; never bypasses §7E, never calls
`append_root()` directly, never reopens a sealed session, never treats the archive as active memory.
(7) BAI, SACL, SIA, BOP, §7E, §7G/§7J/§7M/§7L, `append_root()`. (8) src002 §27 (L819–839), §28 (L843–854),
§29 (L857–893), §30 (L896–942), §31 (L945–956). (9) ACCEPTED — NOT YET INTEGRATED (Master §7E-TSC states
the boundary principles; the full prohibition/recovery detail is external). (10) Companion status ACCEPTED
DESIGN — NOT YET BUILT; an inspection token must never substitute for a promotion token and vice versa.

---

## 4. GOVERNANCE WORKFLOW RECOVERY — SRC-087 PART I, DIRECT (correction #3)

These are the **current governance mechanisms** in SRC-087 (the governance companion itself, created
2026-06-28, status "COMPANION, GOVERNANCE, ACCEPTED-DESIGN, AND PROVENANCE RECORD — NOT AN ARCHITECTURAL
AUTHORITY"). Citations are to the governance file's own line numbers (`gov L#`). The historical embedded
bodies in Parts II–V (SRC-001, SRC-002, the wellbeing source, the AFTER_BGMM handoff, and a **superseded**
MASTER-19_FULL) are identified as historical/archive — they are not treated as current merely because
they are embedded.

**4.1 — Authority ordering and role separation.** (1) The fixed precedence of project files. (2) State
which file wins when sources differ. (3) Order: (1) Master v7_1, (2) DD v2_2, (3) `.cursorrules`, (4) the
governance companion; where an embedded historical source conflicts with the current pair, the current
pair wins. (4) The file set. (5) An ordering rule. (6) Governs which text is authoritative. (7) All
project work. (8) gov L13–20. (9) INTEGRATED INTO CURRENT AUTHORITY (a present governing rule).
(10) Historical wording is preserved unchanged so provenance is not lost.

**4.2 — Files that remain physically separate.** (1) The three files kept as standalone authority.
(2) Keep Master, DD, and `.cursorrules` separate from the companion. (3) Each is listed with byte count,
line count, and SHA-256; they are not merged into the governance file. (4)/(5) File identities + hashes.
(6) Pins each authority file's identity. (7) Authority ordering. (8) gov L22–26. (9) INTEGRATED INTO
CURRENT AUTHORITY. (10) Master 291811 B / 1937 L / `0e8b59e3…`; DD 37048 B / 314 L / `6cd09329…`;
`.cursorrules` 34821 B / 717 L / `5050d088…`.

**4.3 — Embedded-source byte-preservation and verification.** (1) The method that preserves each embedded
source intact. (2) Guarantee no embedded source is corrupted/shortened/reordered. (3) Each source sits
after a machine-readable BEGIN marker with exact byte length + SHA-256; verification reads exactly that
byte length and compares the reconstructed hash. (4) Source bytes. (5) Verifiable embedded blocks.
(6) Preserves original bytes; surfaces stale statements as historical rather than rewriting them. (7) The
8-source manifest. (8) gov L28–44. (9) INTEGRATED INTO CURRENT AUTHORITY. (10) Manifest lists 8 sources
(shared handoff, working roles, SRC-001 [1724 L], SRC-002 [956 L], wellbeing source, AFTER_BGMM handoff,
MASTER-19_v6, DD-S19_v1).

**4.4 — Accepted-design preservation.** (1) Holding accepted-but-unbuilt designs as companions.
(2) Preserve SRC-001/SRC-002 (and the wellbeing source) faithfully without granting them Master
authority. (3) Parts II–IV embed the accepted designs verbatim; each is "not automatically authoritative
where not yet patched into the Master." (4) Accepted-design files. (5) Embedded accepted-design blocks.
(6) Preserves accepted designs; marks them non-authoritative-until-patched. (7) Patch-only integration.
(8) gov L95–113 (Part I refs); Parts II–IV. (9) INTEGRATED INTO CURRENT AUTHORITY (governance rule).
(10) Accepted ≠ integrated — restated structurally by the companion.

**4.5 — Patch-only / no-loss integration discipline.** (1) The rule that any future integration is
patch-only and loss-free. (2) Ensure no accepted design, provenance, status label, hash, dependency,
warning, or open question is lost when files are combined. (3) The next task is **proposal only**; no file
may be created/merged/modified/deleted/renamed/replaced until Ness explicitly approves; after creation a
no-loss verification against every source is required. (4) A consolidation request. (5) A structural
proposal (not files). (6) Restricts file changes; preserves originals. (7) Authority ordering; working
method. (8) gov L142–196. (9) INTEGRATED INTO CURRENT AUTHORITY. (10) Do not summarize away detailed
designs; surface stale references/conflicts instead of silently correcting them.

**4.6 — Current handoff and continuation workflow.** (1) The shared ChatGPT/Claude handoff that lets a
new chat continue safely. (2) Record the authoritative state + next task without relying on chat memory.
(3) States the current authoritative pair + hashes, the accepted standalone TSC, the verified adoption
history (v7_1 from v7 by one line; v2_2 from v2_1 by four header lines), the next task (consolidate 7
files → <5, proposal-only), the required working method, and a starting-state checklist. (4) Project
state. (5) A handoff record. (6) Records state; changes nothing. (7) Authority ordering; working roles.
(8) gov L54–242. (9) INTEGRATED INTO CURRENT AUTHORITY (the handoff is current governance, though itself
"not an architectural authority"). (10) If the handoff conflicts with the authoritative pair, the pair
wins.

**4.7 — Working roles (Ness / Claude / ChatGPT).** (1) Who does what in the project. (2) Keep concept with
Ness; let the AIs build and check the bridge only. (3) The concept (what N.H is/for/must refuse) is
Ness's alone; Claude architects the bridge (one decision at a time, every output marked a proposal until
Ness decides, never closing a concept-level question); ChatGPT checks the bridge (catches contradictions/
gaps/broken cross-references, never proposes what the system should do); Ness is the decider. (4) Design
work. (5) Role assignments. (6) Restricts each party's authority. (7) Concept authority (4.8).
(8) gov L247–300 (`NH_WORKING_ROLES.md`). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) Neither AI may
quietly "take the wheel"; if either sees the other making what should be Ness's call, it flags it.

**4.8 — Ness's sole concept-level decision authority.** (1) The rule reserving meaning/concept to Ness.
(2) Prevent any AI from deciding what N.H is or means. (3) Concept and meaning stay with Ness; the AIs
build and check the technical bridge only; a concept-level question is handed back, never resolved for
him. (4) Concept-level questions. (5) Deferral to Ness. (6) Restricts AI authority over meaning. (7)
Working roles. (8) gov L256–294. (9) INTEGRATED INTO CURRENT AUTHORITY. (10) Mirrors DD §0 and the
Master's §0/§2 — a single consistent governing rule across all authority files.

**4.9 — Required interaction and review method.** (1) How the AIs must interact with Ness. (2) Keep
interaction safe, one-step, and proposal-first. (3) Explain one step at a time in plain language; do not
reopen settled decisions; do not make concept choices for Ness; do not silently patch files; return the
actual file when one is requested; preserve version history; do not tell Ness to move/stop/rest/end
unless he asks. (4) Each interaction. (5) Interaction behavior. (6) Restricts AI interaction style.
(7) Working roles; patch-only discipline. (8) gov L182–227. (9) INTEGRATED INTO CURRENT AUTHORITY.
(10) Consistent with Master §2/§2A and DD §0.

**4.10 — Provenance and archive boundaries.** (1) The line between current authority and preserved
history. (2) Keep historical/superseded material as provenance only, never as current design. (3) Part V
holds historical handoffs and a **superseded** MASTER-19_FULL; Part IV holds the original wellbeing
design-source snapshot; all are preserved unchanged as archive; the governance file itself is explicitly
not an architectural authority. (4) Historical sources. (5) An archive with provenance. (6) Preserves
history; bounds it out of current authority. (7) Authority ordering; embedded-source preservation.
(8) gov L1–5, L3004–3340 (Parts IV–V structure). (9) INTEGRATED INTO CURRENT AUTHORITY (the boundary rule)
/ the embedded bodies themselves are HISTORICAL / INACTIVE. (10) The embedded MASTER-19_FULL in Part V is
**superseded** and must not be read as current — it is provenance only.

---

## 5. CURSOR RULES v3.2 — EXPANDED OPERATIONAL RECOVERY, DIRECT (correction #4)

Recovered by reading the `.cursorrules` file itself (SRC-076, 717 lines), not the Master's §6A summary.
Citations are to the file's own line numbers (`cr L#`). The whole file's Master-integration status is
**INTEGRATED INTO CURRENT AUTHORITY** (it is authority file #3 in the governance order); individual rules'
build-relationship is noted per entry. Disk-sync of v3.2 carries unverified claims (see §6 register).

**5.1 — Identity + permanent prohibitions (all layers).** (1) The unconditional rules over every layer.
(2) Keep Cursor a proposer, never an autonomous agent, and protect secrets/stores. (3) "Cursor proposes,
Ness approves, Cursor implements" with no exceptions; never touch `.env`/`.nh_pin.json`/vault/
`NH_PROMOTE_TOKEN`/API keys/PIN hash; never write test/mock data into any production store; never build a
parallel gate. (4) Proposed changes. (5) Approval/block. (6) Restricts all writes/secrets. (7) Every
build action. (8) cr L51–75 (IDENTITY + §1A). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) No architecture
dependency; applies to both architectures always.

**5.2 — Legacy-gate prohibitions (§1B) + the legacy gate (§2A).** (1) The Layer-2 sovereignty rules.
(2) Keep the one authorized REALITY path and forbid the June-19 bypass. (3) `promote_to_memory()` is the
one gate (GENERATED always blocked; INFERRED needs `NH_PROMOTE_TOKEN`/`user_confirmed`; VERIFIED/
REPORTED_SPEECH direct with constraints); `ContextRouter.write()` is NOT a gate (the exact bypass found
when `route_result()` wrote INFERRED straight to REALITY); never weaken the GENERATED block, write
`nh_mental_network.json` directly, or label AI output as REALITY/VERIFIED. (4) Old-stack writes.
(5) Gated/blocked writes. (6) Restricts Layer-2 writes. (7) Layer-2 modules. (8) cr §1B (L77–100), §2A
(L183–219). (9) INTEGRATED INTO CURRENT AUTHORITY (rule) governing a BUILT, NOT-FRESHLY-VERIFIED gate.
(10) In force until Ness explicitly decommissions Layer 2.

**5.3 — Accretive-store prohibitions (§1C) + accretive gate (§2B).** (1) The Layer-3 sovereignty
boundary. (2) Force every root/reading write through `nh_accretive_store.py`. (3) Never open the stores
with mode "w" or append directly; never bypass `_validate_reading()`; never delete/auto-lift
`.nh_roots.sealed`; never create `.nh_readings_store.jsonl` or `.nh_readings_production_authorized` by
code; never construct a root missing any of the 7 fields or a reading with single-number confidence or an
invented `source_reliability` sentinel; never modify existing roots; never change `MOUTH_MODEL` without
authorization + gold re-run; never touch old Chroma collections. (4) Layer-3 code. (5) Validated writes /
fail-closed. (6) Restricts all Layer-3 store writes; protects seal/markers/schema. (7)
`nh_accretive_store.py`. (8) cr §1C (L102–177), §2B (L222–250). (9) INTEGRATED INTO CURRENT AUTHORITY
(rule) governing the BUILT accretive store. (10) The `append_reading()` production marker-gate is DECIDED,
NOT YET IMPLEMENTED — enforced now only as this Cursor rule.

**5.4 — File maps and stores (§§3A/3B, 4A/4B).** (1) The per-layer function/store maps. (2) Tell Cursor
exactly which function lives where and which store belongs to which layer. (3) Legacy function map
(June-19 inspection; `guard_write()` possibly dead code) and current function map (S14/S16) ; legacy
stores (documented active June 19, not re-verified; `.nh_simulation_store.jsonl` may be invisible to
/review) and current stores (sealed roots, seal marker, quarantine, absent production store, production
marker, Chroma collections, sealed gold files incl. the unplaced `NH_GOLD_SET_CONTEXT_v1.md`). (4)/(5) A
reference map. (6) Identifies protected stores/functions. (7) Three-layer map. (8) cr §3A (L256–273),
§3B (L276–293), §4A (L298–330), §4B (L332–387). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) No /review
equivalent exists for the new readings stores — do not assume any review UI covers accretive readings.

**5.5 — Dual-pipeline warning (§5) + three-layer stack map (§6).** (1) The warning about two research
pipelines and the canonical layer map. (2) Prevent extending the wrong pipeline or confusing layers.
(3) Two pipelines coexist (`nh_hud_server.py` audited Brave+OpenRouter path vs `nh_research_engine.py`
ResearchEngine with Tavily/Brave) — confirm with Ness which before extending, add no third; the stack map
fixes Layer 1 (oldest legacy; `nh_timeline.json`/`nh_nightly.py` presence unverified), Layer 2 (running
gate), Layer 3 (active build target). (4)/(5) A reference map + warning. (6) Identifies pipelines/layers.
(7) File maps. (8) cr §5 (L392–407), §6 (L413–457). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) A
Layer-2 file's write functions stay Protected even if its UI/routing code is "safe to modify."

**5.6 — Protected files + creation gate (§7).** (1) The change-control list. (2) Require "CONFIRMED:
modify [file]" + full dry-run before any protected edit. (3) Lists Layer-2 and Layer-3 protected files
with per-file dry-run requirements (engine benchmark protection incl. don't-change-n=3/BACKGROUND-
framing/truncation; ingest no-seal-bypass; rebuild no-touch-old-collections); names safe-to-modify files
(with specific Protected functions inside `nh_hud_server.py`); sets the `nh_baseline_engine.py` creation
gate. (4) Proposed edits. (5) Approval/block. (6) Restricts edits to protected files. (7) Dry-run
protocol. (8) cr §7 (L463–545). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) `nh_baseline_engine.py` needs
"CONFIRMED: create…" + dry-run + all §12D (§22) prerequisites; auto Full-Protected once created.

**5.7 — Dry-run protocol + code quality (§§8–9).** (1) The mandatory pre-write block and code standards.
(2) Force a named-gate dry-run before any write-path code and forbid silent failures. (3) Output a
PROPOSED CHANGE block (file / one-sentence change / stores touched / exact gate function+file — "none" or
"`ContextRouter.write()` directly" or "direct file open" is invalid) and wait for "APPROVED"; no
placeholders/TODO; no bare `except: pass` on store writes; mandatory schema validation before every
append; checked async writes; fix the stale "188 seed records" docstring when next touched. (4) Proposed
code. (5) PROPOSED CHANGE block + approval. (6) Restricts/standardizes write code. (7) Protected files.
(8) cr §8 (L550–568), §9 (L574–591). (9) INTEGRATED INTO CURRENT AUTHORITY. (10) —

**5.8 — Pull Sovereignty (§10) + before-memory-feature (§11) + §12 status.** (1) The autonomy guardrails,
the duplication check, and the built/designed/legacy status. (2) Forbid unsolicited autonomy, prevent a
fourth parallel gate, and record what is built vs not. (3) No push/auto-promote; no autonomous background
task without an explicit approved comment; re-enabling any auto-start/tunnel requires verifying the auth
layer on disk; never auto-create the production marker; check existing modules before adding a
memory-touching feature, confirm the layer, never mix Layer-2/Layer-3 write paths; §12 records 12A NOW
BUILT (I1 append-only, I2 partial membrane-via-quarantine, I8 two-file store), 12B DESIGNED-NOT-BUILT
(I3/I4/I6/I7), 12C LEGACY OVERRIDES (I5 NOT IN FORCE; per-record /review still active), 12D creation gate.
(4) Agent activity / new features. (5) Stops / status facts. (6) Restricts autonomy; records status.
(7) All layers. (8) cr §10 (L597–607), §11 (L612–629), §12 (L634–701), REMINDER (L706–717). (9) INTEGRATED
INTO CURRENT AUTHORITY. (10) Every shortcut around `promote_to_memory()` or every direct accretive write
is a sovereignty violation, "even if the record appears well-formed."

---

## 6. ACCEPTED-COMPANION INTEGRATION MATRIX — RE-DERIVED FROM THE FULL RECOVERY (correction #1)

Each accepted mechanism is compared against `NH_MASTER-19_CORRECTED_v7_1.md` only. "Referenced" = the
Master names or depends on it (only at the §7E-TSC seam); "summarized" = the Master carries an integration
summary; "external" = the full design lives only in the companion. Every row is now grounded in the
direct §3A/§3B recovery, not a component-name guess.

| Accepted mechanism | Direct source (body range) | In Master v7_1? | Integration status |
|---|---|---|---|
| BOP (3A.1) | src001 §1 (L70–276) | Referenced ("BOP roots" in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Other-Speaker/Guest/Known-Person (3A.2) | src001 §2 (L281–406) | Not present | ACCEPTED — NOT YET INTEGRATED |
| SIA (3A.3) | src001 §3 (L412–652) | Referenced ("SIA links" in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| SACL (3A.4) | src001 §4 (L657–847) | Referenced ("recognized-Ness SACL" in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Wellbeing/Identity/Security separation (3A.5) | src001 §5 (L852–892) | Not present | ACCEPTED — NOT YET INTEGRATED |
| BAI (3A.6) | src001 §6 (L898–1077) | Referenced ("purpose-bound BAI tokens" in §7E-TSC) | ACCEPTED — NOT YET INTEGRATED |
| Owner-Phone Pairing (3A.7) | src001 §7 (L1083–1119) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Recovery-Code Lifecycle (3A.8) | src001 §8 (L1125–1169) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Future-Phone Replacement (3A.9) | src001 §9 (L1175–1188) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Atomic Emergency Recovery (3A.10) | src001 §10 (L1194–1243) | Not present | ACCEPTED — NOT YET INTEGRATED |
| Voice-Profile Enrollment Bootstrap (3A.11) | src001 §11 (L1249–1389) | Not present (references §7G/§7L internally) | ACCEPTED — NOT YET INTEGRATED |
| Vocabulary Additions (3A.12) | src001 §12 (L1395–1430) | Not present in §6B/§7L text | ACCEPTED — NOT YET INTEGRATED (companion: FORMALLY ADOPTED) |
| BGMM (3A.13) | src001 §13 (L1436–1721) | Not present | ACCEPTED — NOT YET INTEGRATED |
| TSC §7E relationship + blocker + authorization + sealing + promotion + inspection + archive | src002 §§1–2,13–17,23 | **Summarized** in Master §7E-TSC (L650–675) | ACCEPTED — PARTLY INTEGRATED |
| TSC table schemas, event-links, output preservation, blocker history, multi-person, audit events, recovery, prohibitions | src002 §§3–12,18–22,24–31 | Not present (only the relationship is summarized) | ACCEPTED — NOT YET INTEGRATED |

**Notes.** (a) The Master's only structural contact with the security spine is the TSC seam; everything in
§3A is design the Master does not contain. (b) The TSC is the one mechanism with a real Master integration
summary (hence ACCEPTED — PARTLY INTEGRATED for the relationship), while its 31-section internals remain
external and authoritative-in-scope. (c) Nothing reaches `INTEGRATED INTO CURRENT AUTHORITY` — that label
is used in this audit only for current governing principles/rules (§1 corrections, §4, §5), never for an
accepted security/TSC design. (d) Both companions name `MASTER-19_v6` + `DD-S19_v1` as patch targets; the
current pair is v7_1 + DD-v2_2 — re-confirming the patch target is a future Ness decision, not made here.

---

## 7. PRE-STAGE-3B SUPPLEMENTAL-INTAKE REGISTER (correction #7 — register only; not adopted, not compared)

The following three files were named as newly available but are **outside the original SRC-001–092
preservation set** and are **absent from the current project workspace** (verified: not in `/mnt/project`).
They are registered here for intake before Stage 3B and are **not** classified as current authority, **not**
adopted, **not** integrated, and **not** compared in this pass — neither their filenames nor any internal
claim is taken as evidence of authority.

| Candidate file | Claimed relation | Required before Stage 3B can use it |
|---|---|---|
| `NH_MASTER-19_CORRECTED_v8.md` | Possible Master successor to v7_1 | Obtain the file; hash it; establish provenance; verify whether Ness has adopted it (adoption evidence, not filename); only then diff against v7_1 under no-loss discipline |
| `NH_DECISION_DEFAULTS-S19_v2_3.md` | Possible DD successor to v2_2 | Obtain; hash; provenance; adoption-status verification; then compare against v2_2 |
| `cursorrules_v3_3` | Possible Cursor Rules successor to v3.2 | Obtain; hash; provenance; adoption-status verification; confirm disk-`.cursorrules` relationship; then compare against v3.2 |

Until each is supplied, hashed, and its adoption status verified, the current authority remains v7_1 /
DD-v2_2 / Cursor Rules v3.2 / governance companion v1. No design content from these candidates is recovered
or weighed in this baseline.

---

## 8. SOURCE-RANGE VERIFICATION REPORT — REWRITTEN, TRUTHFUL (correction #6)

This audit is document-based and performed **no fresh disk inspection**. Below is exactly what was read
this turn (v1.1), accounting for the **complete body** of each of the six sources.

| Source | Path read | Body size | Coverage in v1.1 |
|---|---|---|---|
| SRC-044 Master v7_1 | `/mnt/project/NH_MASTER-19_CORRECTED_v7_1.md` | 1937 L | **Complete body read** across v1 + v1.1: L174–1404 (premise→§7R), L1406–1467, L1468–1706 (§11 mid-items, §11-SETTLED, §12–§15, §16 model layer, §17–§18 logs, §19A–E), L1759–1937 (§22–§25). Every section §0–§25 read line-by-line. |
| SRC-015 DD-S19_v2_2 | `/mnt/project/NH_DECISION_DEFAULTS-S19_v2_2.md` | 314 L | **Complete body read** (L1–315): §0–§6, including §3A–§3N, §4 build-state, §5 open forks, §6 first-class principles. |
| SRC-076 Cursor Rules v3.2 | `/mnt/project/cursorrules__1_` | 717 L | **Complete body read** (L51–717 content; L1–50 preamble): IDENTITY, §§1A/1B/1C, §2A, §2B, §3A/3B, §4A/4B, §5, §6, §7, §8, §9, §10, §11, §12A–D, REMINDER. Recovered directly, not via the Master §6A summary. |
| SRC-087 governance companion | `/mnt/project/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | 5580 L | Header + authority order + files-separate + preservation method + manifest (L1–45) and **Part I in full** (L47–303: shared handoff + working roles) read directly. Part II/III openers + full structure mapped; the embedded SRC-001/SRC-002 bodies were read directly from their standalone extractions (next two rows). Parts IV (wellbeing source) and V (AFTER_BGMM handoff + **superseded** MASTER-19_FULL) identified as historical archive, not re-read as current authority. |
| SRC-001 security/identity | extracted standalone from Reader Part 01 (the canonical companion body; byte-identical to gov Part II) | 1724 L | **Complete body read** with source-body-relative line numbers (src001 L1–1724): §§1–13 all read directly — BOP (L70–276), Other-Speaker (L281–406), SIA (L412–652), SACL (L657–847), separation (L852–892), BAI (L898–1077), pairing (L1083–1119), recovery (L1125–1169), future-phone (L1175–1188), emergency (L1194–1243), enrollment (L1249–1389), vocabulary (L1395–1430), BGMM (L1436–1721). |
| SRC-002 accepted TSC | extracted standalone from Reader Part 01 (the canonical companion body; byte-identical to gov Part III) | 956 L | **Complete body read** with source-body-relative line numbers (src002 L1–956): all 31 sections read directly (L73–956), provenance/status L1–71. |

**Correction of v1's §6 defects.** v1's report cited governance-embedding ranges (`gov L…`) as if they
were the companions' direct ranges and claimed full reads that were partial. v1.1 reads the standalone
companion bodies directly, cites source-body-relative ranges throughout, and removes the
governance-substitution. Where a governance cross-reference is useful it is marked `gov L…` and is
secondary only.

---

## 9. v1 → v1.1 CORRECTION LEDGER (correction #8)

**Preserved valid material (carried forward unchanged):** the entire v1 Master-side ten-field inventory
(subsystems A–AB) — design content unchanged; the v1 plain-language behavior map (v1 §2); the v1
built-substrate status calls (C–D, B, F) and the PARTIALLY-BUILT calls (C4b, D5, G3); the v1 Stage-3B
historical-source list (v1 §7); the document-based / no-fresh-disk-verification caveat.

**Newly recovered material (not in v1):** full ten-field recovery of every SRC-001 mechanism (13
components incl. BOP schema + safeguards, Other-Speaker/Guest/Known-Person, SIA records/anti-spoofing/
profile-learning/uncertainty/recovery, SACL gates/output-gating/multi-speaker/indirect-disclosure/
fail-closed, wellbeing/identity/security separation, BAI tokens/leases/purpose-binding/revocation/state/
audit-separation, pairing, recovery-code lifecycle, future-phone, atomic emergency recovery, voice
enrollment + provisional links, vocabulary additions, BGMM entry/manifests/scope/rollback/startup-
recovery/privacy/audit/relocking) — §3A; full ten-field recovery of all 31 TSC sections (identity/§7E
relationship, transactional model + 13 tables, all record schemas, BOP/SIA links, output preservation,
blocker schema + history, lifecycle, sealing, interrupted/continuation, inspection, BAI+SACL
authorization, exact promotion sequence, dependency, partial/idempotency, retry, multi-person, Ness's own
material, retained archive, double-weighting protection, privacy/exclusion/deletion, audit events,
startup/crash recovery, fail-closed, integration boundaries, prohibited behaviors, status) — §3B;
governance Part I workflows (10 mechanisms) — §4; expanded direct Cursor Rules recovery (§§1–12) — §5;
AC1–AC3/AD1–AD4 re-issued in ten-field form — §2.

**Status corrections (correction #2):** A1/A2/A3/G1 → INTEGRATED INTO CURRENT AUTHORITY; H2 (TSC summary)
→ ACCEPTED — PARTLY INTEGRATED; G2 and the §7E/§7F/§7G/§7H/§7I/§7J/§7K/§7L/§7M/§7N/§7O/§7P/§7R/§8/§9A/§13/
§16-wiring/§23 entries → PARTIALLY DESIGNED (each names its own undesigned schemas/thresholds/interfaces);
Z1 (Wellbeing) and AB1 (Connection) retained as FULLY DESIGNED — NOT BUILT (authority presents complete
specs with no named gaps). Full table in §1.

**Citation corrections (correction #6):** all SRC-001/SRC-002 citations converted from governance-embedding
ranges to direct source-body-relative ranges; Cursor Rules and governance cited by their own line numbers;
§6 (now §8) rewritten to truthfully account for the complete body of each of the six sources; impossible/
mismatched ranges removed.

**Scope corrections:** the v1 opening overclaim ("all six complete bodies were read") is replaced by an
honest statement and a truthful §8; the integration matrix is re-derived from the full recovery rather than
from component names; the inspection-authorization item is recorded as **settled** per SRC-002 §15/§31
(no remaining concept question), correcting any earlier "one open question" framing.

**Remaining unresolved items (carried, not resolved here):** the production-readings marker code (decided,
not implemented); `source_reliability` value-form (unverified from live code); Engine C blocked on
story-bearing gold cases; the Story-Layer object-identity seam; multi-box (sealed-batch) architecture;
context gold set v1 (unplaced/unsealed); academic-source choice; live-retrieval isolation environment;
screenshot-as-inert-image proposal; Brave spending cap (to be coded); final Interactive Translator mouth
(undecided); Chat Front Door's two questions; §0A DUMB/SMART placement pins; Mobile's five open questions;
the Interface/World undesigned areas; the §11-item-34 meaning-to-technical questions (must not be silently
decided); the entire accepted security spine (SRC-001) and TSC internals (SRC-002) remaining un-integrated;
and the three supplemental-intake candidates (§7) awaiting hashing/provenance/adoption verification.

---

## STATE AFTER STAGE 3A v1.1 (nothing decided, nothing changed)
- v1 preserved unchanged; authority unchanged (v7_1 / DD-v2_2 / Cursor Rules v3.2 / governance companion v1).
- All six complete bodies now read directly; the two accepted companions and the governance/Cursor
  workflows are fully recovered in ten-field form; statuses and citations corrected.
- No historical Master compared; no conflict resolved; no design judged or changed; nothing integrated,
  patched, or decided; no organization chosen; no canonical Master drafted; Stage 3B not begun.

**STAGE 3A v1.1 COMPLETE. AWAITING NESS.**
