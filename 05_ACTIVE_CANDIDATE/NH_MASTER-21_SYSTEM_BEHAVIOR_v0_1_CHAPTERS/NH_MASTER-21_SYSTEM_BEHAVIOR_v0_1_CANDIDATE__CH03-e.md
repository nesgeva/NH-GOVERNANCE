# Chapter 3-e — Group A: C-GOLD, evaluation identities, record contracts and currentness

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-e.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece extends the Group A evaluation-evidence connection. C-GOLD owns the evaluation machinery; C-READ.11 retains per-reading promotion. Chapter 3-e defines the bridge identities, record contracts and currentness; Chapter 3-f defines the operation catalog, trial execution, twelve boundary contracts, concurrency and unresolved-attempt recovery. The protected judgment claim/authority lifecycle, complete aggregate/result derivation and applicability decomposition remain for later pieces. This pair does not complete C-GOLD, the bridge or Group A.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1; the Map is subordinate. Every behavior line in this pair is ACCEPTED, sourced from the exact accepted bridge v1.7. Its source remains in 05_ACTIVE_CANDIDATE; receipt §§3–5 records acceptance of SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`. The frozen candidate header does not erase that acceptance. No bridge behavior or link is stamped BUILT.

Citation keys: `05/` = `05_ACTIVE_CANDIDATE/`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = the current Design and Wiring Map v1.6. NHD-B16EEB names this accepted bridge, distinct from NHD-B16. Source-local D-labels are expanded to the receipt’s globally unique NHD-B16EEB-D… identifiers; no slot value is selected.

All bridge field, record, state, event and operation names remain proposed as in the accepted source. No serialization, storage, algorithm, framework or lock is selected. A field card describes a member of its containing record, not a separate service. Record-level failure consequences are labelled as such. Relation and reciprocal entries written here stay here; concatenation never edits or merges an earlier chapter.

<!-- BEGIN CHAPTER 3-e BEHAVIOR -->

### C-GOLD.1 — Promotion evaluation-evidence bridge
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evaluation-evidence machinery extending C-GOLD and supplying separate gold and held-out evidence to the existing per-reading promotion verifier. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Takes in: ACCEPTED — Accepted suite references, candidate profiles, policy references, evaluation records and their scope ledger. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps gold evidence, held-out evidence and system eligibility separate; binds results to exact profiles, policies and current ledger heads; exposes references for B16 verification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Gives out: ACCEPTED — Distinct E11a, E11b and E12 result families and E13 references to E11a/E11b only, subject to their accepted prerequisites. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute B24 eligibility for either B16 evidence input, decide policy values, invent test content, or make promotion decisions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Missing prerequisites prevent evidentiary execution or usable passing evidence; no held-out result exists without an accepted held-out definition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.1 — Evaluation ownership boundaries: C-GOLD owns gold examination and logging; B24 owns benchmark rules and eligibility rules; B9 owns technical retries; this bridge owns records, scope ledgers and applicability; B16 owns per-reading verification and promotion outcomes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.1.2 — Evaluation identities and required coverage: Binds each evidentiary run to one exact family and scope with a complete trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.1.3 — Canonical evaluation record family: Appends immutable records; corrections are new linked records; each has integrity reference, schema_version and creating operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.1.4 — Scope ledger and currentness: Advances one authoritative scope ledger with every relevant record; results bind the exact head and evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD — Sealed gold sets v1, v2-B (§7C): C-GOLD supplies sealed-gold examination and gold-run logging; the bridge extends that owner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.1.5 — Evaluation operations and trial execution: Executes under one-terminal/one-log ownership, output uniqueness, B9 admission and lookup-first recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Gated by: ACCEPTED — A complete current epoch is required for evidentiary execution; usable evidence must match its current scope; privacy access must be authorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD — Sealed gold sets v1, v2-B (§7C) · CY-G | Accepted suite references, candidate profiles, policy references, evaluation records and their scope ledger. | The evaluation bridge extends C-GOLD in CY-G; separate narrow evidence references feed the existing B16 per-reading verification. | Distinct E11a, E11b and E12 result families and E13 references to E11a/E11b only, subject to their accepted prerequisites. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.1 — Evaluation ownership boundaries; C-GOLD.1.2 — Evaluation identities and required coverage; C-GOLD.1.3 — Canonical evaluation record family; C-GOLD.1.4 — Scope ledger and currentness; C-GOLD.1.5 — Evaluation operations and trial execution

### C-GOLD.1.1 — Evaluation ownership boundaries
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Evaluation ownership boundaries rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — C-GOLD, B24, B9, the bridge and the existing B16 verifier. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — C-GOLD owns gold examination and logging; B24 owns benchmark rules and eligibility rules; B9 owns technical retries; this bridge owns records, scope ledgers and applicability; B16 owns per-reading verification and promotion outcomes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — Separated authorities; held-out content and concrete benchmark suites have no assigned accepted owner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Use the bridge to judge meaning, select policy values, invent suite content or choose a promotion outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.1.1 — Gold evaluation ownership: C-GOLD owns sealed gold sets, gold examination, gold-run logging and per-case judgments under the six settled rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.1.2 — Benchmark rule ownership: B24 owns benchmark rules, eight families, named measurements, severity and eligibility; concrete suites and every policy value are not supplied by that ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.1.3 — Retry ownership: B9 and its accepted values own every technical re-attempt, including admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery and lost commit races. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.1.4 — Evidence mechanics ownership: The bridge owns its record family, scopes, ledgers, currentness, concurrency, identities, operations, terminals, derivation and applicability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.1.5 — Promotion ownership: B16 performs per-reading verification in B16-2 and owns every promotion outcome; promotion_committed is absorbing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.1.6 — Connected flow boundary: B-CYCLE-6 owns the connected promotion flow and batch wiring; C2 owns marker-gate implementation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | C-GOLD, B24, B9, the bridge and the existing B16 verifier. | C-GOLD owns gold examination and logging; B24 owns benchmark rules and eligibility rules; B9 owns technical retries; this bridge owns records, scope ledgers and applicability; B16 owns per-reading verification and promotion outcomes. | Separated authorities; held-out content and concrete benchmark suites have no assigned accepted owner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.1.1 — Gold evaluation ownership; C-GOLD.1.1.2 — Benchmark rule ownership; C-GOLD.1.1.3 — Retry ownership; C-GOLD.1.1.4 — Evidence mechanics ownership; C-GOLD.1.1.5 — Promotion ownership; C-GOLD.1.1.6 — Connected flow boundary

### C-GOLD.1.1.1 — Gold evaluation ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Gold evaluation ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Gold evaluation ownership [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — C-GOLD owns sealed gold sets, gold examination, gold-run logging and per-case judgments under the six settled rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — C-GOLD owns sealed gold sets, gold examination, gold-run logging and per-case judgments under the six settled rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Own held-out policy, eligibility policy or promotion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Gold evaluation ownership | C-GOLD owns sealed gold sets, gold examination, gold-run logging and per-case judgments under the six settled rules. | C-GOLD owns sealed gold sets, gold examination, gold-run logging and per-case judgments under the six settled rules. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.1.2 — Benchmark rule ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Benchmark rule ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Benchmark rule ownership [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — B24 owns benchmark rules, eight families, named measurements, severity and eligibility; concrete suites and every policy value are not supplied by that ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — B24 owns benchmark rules, eight families, named measurements, severity and eligibility; concrete suites and every policy value are not supplied by that ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Treat B24 suite families as approved concrete cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Benchmark rule ownership | B24 owns benchmark rules, eight families, named measurements, severity and eligibility; concrete suites and every policy value are not supplied by that ownership. | B24 owns benchmark rules, eight families, named measurements, severity and eligibility; concrete suites and every policy value are not supplied by that ownership. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.1.3 — Retry ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Retry ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Retry ownership [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — B9 and its accepted values own every technical re-attempt, including admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery and lost commit races. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — B9 and its accepted values own every technical re-attempt, including admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery and lost commit races. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Confuse planned trial counts with retry attempts or judge evaluation meaning. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Retry ownership | B9 and its accepted values own every technical re-attempt, including admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery and lost commit races. | B9 and its accepted values own every technical re-attempt, including admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery and lost commit races. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.1.4 — Evidence mechanics ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Evidence mechanics ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Evidence mechanics ownership [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — The bridge owns its record family, scopes, ledgers, currentness, concurrency, identities, operations, terminals, derivation and applicability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — The bridge owns its record family, scopes, ledgers, currentness, concurrency, identities, operations, terminals, derivation and applicability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Judge content or choose policy values, mappings, held-out definitions or promotion decisions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Evidence mechanics ownership | The bridge owns its record family, scopes, ledgers, currentness, concurrency, identities, operations, terminals, derivation and applicability. | The bridge owns its record family, scopes, ledgers, currentness, concurrency, identities, operations, terminals, derivation and applicability. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.1.5 — Promotion ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Promotion ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Promotion ownership [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — B16 performs per-reading verification in B16-2 and owns every promotion outcome; promotion_committed is absorbing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — B16 performs per-reading verification in B16-2 and owns every promotion outcome; promotion_committed is absorbing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Move promotion decision authority into evaluation mechanics. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Promotion ownership | B16 performs per-reading verification in B16-2 and owns every promotion outcome; promotion_committed is absorbing. | B16 performs per-reading verification in B16-2 and owns every promotion outcome; promotion_committed is absorbing. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.1.6 — Connected flow boundary
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Connected flow boundary rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Takes in: ACCEPTED — Connected flow boundary [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Does: ACCEPTED — B-CYCLE-6 owns the connected promotion flow and batch wiring; C2 owns marker-gate implementation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Gives out: ACCEPTED — B-CYCLE-6 owns the connected promotion flow and batch wiring; C2 owns marker-gate implementation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this evidence bridge as completed connected promotion or marker-gate implementation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.1 — Evaluation ownership boundaries | Connected flow boundary | B-CYCLE-6 owns the connected promotion flow and batch wiring; C2 owns marker-gate implementation. | B-CYCLE-6 owns the connected promotion flow and batch wiring; C2 owns marker-gate implementation. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2 — Evaluation identities and required coverage
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The frozen identity and coverage contracts of evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]
- Takes in: ACCEPTED — Suite versions, model and system profiles, policy epochs and planned trials. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]
- Does: ACCEPTED — Binds each evidentiary run to one exact family and scope with a complete trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]
- Gives out: ACCEPTED — Comparable, explicitly scoped evaluation identities. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge different families, replace planned trials with retries, or infer coverage from declarations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No evidentiary execution while the complete current epoch or trial count is absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.1 — model_evaluation_profile (E4): Binds gold v1 to Engine A and gold v2-B to Engine B; each binding carries its own configuration digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2 — system_candidate_profile (E4S): Binds both roles and the complete handoff as one system candidate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): Binds every required current accepted version; currentness lasts only while every named policy is current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.4 — Run class freeze: Freezes evidentiary runs to the complete current epoch, suite manifest and registered profile; exploratory runs remain non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5 — Evaluation scope: Assigns one run to exactly one scope and one family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.6 — Planned trial identity and full trial plan: Uses planned_trial_key as canonical identity and one B9 retry group; the plan equals the complete suite case list × epoch trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7 — Coverage cells and named measurements: Requires complete current passed evidentiary runs matching each cell exactly and full suite × trial count; declared measurements require actual recorded results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): Binds every required current accepted version; currentness lasts only while every named policy is current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | Suite versions, model and system profiles, policy epochs and planned trials. | Binds each evidentiary run to one exact family and scope with a complete trial plan. | Comparable, explicitly scoped evaluation identities. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.1 — model_evaluation_profile (E4); C-GOLD.1.2.2 — system_candidate_profile (E4S); C-GOLD.1.2.3 — policy_epoch (E2e); C-GOLD.1.2.4 — Run class freeze; C-GOLD.1.2.5 — Evaluation scope; C-GOLD.1.2.6 — Planned trial identity and full trial plan; C-GOLD.1.2.7 — Coverage cells and named measurements

### C-GOLD.1.2.1 — model_evaluation_profile (E4)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One model with explicit suite-to-execution-path bindings; all bridge names remain proposed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Model identity and the execution-path bindings. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — Binds gold v1 to Engine A and gold v2-B to Engine B; each binding carries its own configuration digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — An E4 model profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Require both suites to share one engine identity or apply evidence to an unbound path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable profile records make downstream state indeterminate; mismatched reading/profile/path bindings do not supply applicable B16 evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.1.1 — model identity: One evaluated model identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.2 — execution-path bindings: One explicit binding per suite version to an approved execution path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3 — Execution-path binding: Binds the exact execution path for this suite version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.4 — model digest: The model digest bound to the profile and matched exactly to the reading by AP-6. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — The exact approved profile and path/system configuration are bound; content-digest identity governs registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | Model identity and the execution-path bindings. | Binds gold v1 to Engine A and gold v2-B to Engine B; each binding carries its own configuration digest. | An E4 model profile. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Model identity and the execution-path bindings. | Uses the E4 canonical record defined by this card. | An E4 model profile. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | Model identity and the execution-path bindings. | When registering this setup record kind: Binds gold v1 to Engine A and gold v2-B to Engine B; each binding carries its own configuration digest. | An E4 model profile. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | Model identity and the execution-path bindings. | For this requested record kind, appends the E4 canonical record when its stated commit conditions hold; earlier records remain unchanged. | An E4 model profile. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | Model identity and the execution-path bindings. | For the corresponding requested record kind, commits E4 at this boundary only after its stated gates; existing records are not overwritten. | An E4 model profile. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.1.1 — model identity; C-GOLD.1.2.1.2 — execution-path bindings; C-GOLD.1.2.1.3 — Execution-path binding; C-GOLD.1.2.1.4 — model digest

### C-GOLD.1.2.1.1 — model identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The model identity member of model_evaluation_profile (E4). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — One evaluated model identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — One evaluated model identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded model identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1 — model_evaluation_profile (E4) | One evaluated model identity. | One evaluated model identity. | The recorded model identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.2 — execution-path bindings
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The execution-path bindings member of model_evaluation_profile (E4). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — One explicit binding per suite version to an approved execution path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — One explicit binding per suite version to an approved execution path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded execution-path bindings member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1 — model_evaluation_profile (E4) | One explicit binding per suite version to an approved execution path. | One explicit binding per suite version to an approved execution path. | The recorded execution-path bindings member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3 — Execution-path binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One suite-version-to-approved-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Suite version; engine, prompt, context and validator configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — Binds the exact execution path for this suite version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — A binding with path_configuration_digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Replace an exact binding with a merely similar model, prompt or path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable profile records make downstream state indeterminate; mismatched reading/profile/path bindings do not supply applicable B16 evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.1 — suite version: The exact suite version being bound. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.2 — engine identity: The approved engine identity for that suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.3 — engine version: The bound engine version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.4 — code integrity: The engine code-integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.5 — prompt: The bound prompt configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.6 — context/retrieval configuration: The bound context and retrieval configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.7 — validator configuration: The validator configuration, or the exact not_in_path alternative. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.8 — other benchmark-protected configuration: Other configuration protected for benchmark comparability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.1.3.9 — path_configuration_digest: The digest identifying this binding’s complete path configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gated by: ACCEPTED — The exact approved profile and path/system configuration are bound; content-digest identity governs registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1 — model_evaluation_profile (E4) | Suite version; engine, prompt, context and validator configuration. | Binds the exact execution path for this suite version. | A binding with path_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.1.3.1 — suite version; C-GOLD.1.2.1.3.2 — engine identity; C-GOLD.1.2.1.3.3 — engine version; C-GOLD.1.2.1.3.4 — code integrity; C-GOLD.1.2.1.3.5 — prompt; C-GOLD.1.2.1.3.6 — context/retrieval configuration; C-GOLD.1.2.1.3.7 — validator configuration; C-GOLD.1.2.1.3.8 — other benchmark-protected configuration; C-GOLD.1.2.1.3.9 — path_configuration_digest

### C-GOLD.1.2.1.3.1 — suite version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The suite version member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact suite version being bound. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The exact suite version being bound. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded suite version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The exact suite version being bound. | The exact suite version being bound. | The recorded suite version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.2 — engine identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The engine identity member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The approved engine identity for that suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The approved engine identity for that suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded engine identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The approved engine identity for that suite. | The approved engine identity for that suite. | The recorded engine identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.3 — engine version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The engine version member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound engine version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound engine version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded engine version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The bound engine version. | The bound engine version. | The recorded engine version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.4 — code integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The code integrity member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The engine code-integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The engine code-integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded code integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The engine code-integrity reference. | The engine code-integrity reference. | The recorded code integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.5 — prompt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The prompt member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound prompt configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound prompt configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded prompt member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The bound prompt configuration. | The bound prompt configuration. | The recorded prompt member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.6 — context/retrieval configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The context/retrieval configuration member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound context and retrieval configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound context and retrieval configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded context/retrieval configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The bound context and retrieval configuration. | The bound context and retrieval configuration. | The recorded context/retrieval configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.7 — validator configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The validator configuration member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The validator configuration, or the exact not_in_path alternative. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The validator configuration, or the exact not_in_path alternative. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded validator configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The validator configuration, or the exact not_in_path alternative. | The validator configuration, or the exact not_in_path alternative. | The recorded validator configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.8 — other benchmark-protected configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The other benchmark-protected configuration member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Other configuration protected for benchmark comparability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — Other configuration protected for benchmark comparability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded other benchmark-protected configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | Other configuration protected for benchmark comparability. | Other configuration protected for benchmark comparability. | The recorded other benchmark-protected configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.3.9 — path_configuration_digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The path_configuration_digest member of Execution-path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The digest identifying this binding’s complete path configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The digest identifying this binding’s complete path configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded path_configuration_digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1.3 — Execution-path binding | The digest identifying this binding’s complete path configuration. | The digest identifying this binding’s complete path configuration. | The recorded path_configuration_digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.1.4 — model digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The model digest member of model_evaluation_profile (E4). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Takes in: ACCEPTED — The model digest bound to the profile and matched exactly to the reading by AP-6. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Does: ACCEPTED — The model digest bound to the profile and matched exactly to the reading by AP-6. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded model digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.1 — model_evaluation_profile (E4) | The model digest bound to the profile and matched exactly to the reading by AP-6. | The model digest bound to the profile and matched exactly to the reading by AP-6. | The recorded model digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2 — system_candidate_profile (E4S)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evaluated analyst, messenger and combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The two component E4 profiles and the combined system configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — Binds both roles and the complete handoff as one system candidate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — An E4S profile with system_configuration_digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Treat one component’s profile as the whole evaluated pair. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable profile records make downstream state indeterminate; mismatched reading/profile/path bindings do not supply applicable B16 evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.2.1 — analyst component: The analyst component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.2 — messenger component: The messenger component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.3 — combined handoff configuration: The configuration of the combined pair/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4 — Combined handoff configuration: Identifies the configured pair/system used for evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — The exact approved profile and path/system configuration are bound; content-digest identity governs registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | The two component E4 profiles and the combined system configuration. | Binds both roles and the complete handoff as one system candidate. | An E4S profile with system_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | The two component E4 profiles and the combined system configuration. | Uses the E4S canonical record defined by this card. | An E4S profile with system_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | The two component E4 profiles and the combined system configuration. | When registering this setup record kind: Binds both roles and the complete handoff as one system candidate. | An E4S profile with system_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | The two component E4 profiles and the combined system configuration. | For this requested record kind, appends the E4S canonical record when its stated commit conditions hold; earlier records remain unchanged. | An E4S profile with system_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | The two component E4 profiles and the combined system configuration. | For the corresponding requested record kind, commits E4S at this boundary only after its stated gates; existing records are not overwritten. | An E4S profile with system_configuration_digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.2.1 — analyst component; C-GOLD.1.2.2.2 — messenger component; C-GOLD.1.2.2.3 — combined handoff configuration; C-GOLD.1.2.2.4 — Combined handoff configuration

### C-GOLD.1.2.2.1 — analyst component
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The analyst component member of system_candidate_profile (E4S). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The analyst component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The analyst component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded analyst component member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2 — system_candidate_profile (E4S) | The analyst component’s E4 profile. | The analyst component’s E4 profile. | The recorded analyst component member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.2 — messenger component
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The messenger component member of system_candidate_profile (E4S). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The messenger component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The messenger component’s E4 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded messenger component member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2 — system_candidate_profile (E4S) | The messenger component’s E4 profile. | The messenger component’s E4 profile. | The recorded messenger component member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.3 — combined handoff configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The combined handoff configuration member of system_candidate_profile (E4S). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The configuration of the combined pair/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The configuration of the combined pair/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded combined handoff configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2 — system_candidate_profile (E4S) | The configuration of the combined pair/system. | The configuration of the combined pair/system. | The recorded combined handoff configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4 — Combined handoff configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The combined system configuration bound by E4S. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Brief schema, validators, contracts, gates and handoff arrangement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — Identifies the configured pair/system used for evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The complete system configuration and its digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute a different handoff configuration under the bound system_configuration_digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable profile records make downstream state indeterminate; mismatched reading/profile/path bindings do not supply applicable B16 evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.1 — brief schema version: The bound brief schema version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.2 — B24 validator configuration: The bound B24 validator configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.3 — payload contract: The bound payload contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.4 — messenger contract: The bound messenger contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.5 — gate configuration references: References to the bound gate configurations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.6 — dual-model handoff arrangement: The handoff arrangement of the accepted dual-model handoff package, §§1–4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.2.4.7 — system_configuration_digest: The digest of the combined system configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gated by: ACCEPTED — The exact approved profile and path/system configuration are bound; content-digest identity governs registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2 — system_candidate_profile (E4S) | Brief schema, validators, contracts, gates and handoff arrangement. | Identifies the configured pair/system used for evaluation. | The complete system configuration and its digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.2.4.1 — brief schema version; C-GOLD.1.2.2.4.2 — B24 validator configuration; C-GOLD.1.2.2.4.3 — payload contract; C-GOLD.1.2.2.4.4 — messenger contract; C-GOLD.1.2.2.4.5 — gate configuration references; C-GOLD.1.2.2.4.6 — dual-model handoff arrangement; C-GOLD.1.2.2.4.7 — system_configuration_digest

### C-GOLD.1.2.2.4.1 — brief schema version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The brief schema version member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound brief schema version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound brief schema version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded brief schema version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The bound brief schema version. | The bound brief schema version. | The recorded brief schema version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.2 — B24 validator configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The B24 validator configuration member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound B24 validator configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound B24 validator configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded B24 validator configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The bound B24 validator configuration. | The bound B24 validator configuration. | The recorded B24 validator configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.3 — payload contract
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The payload contract member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound payload contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound payload contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded payload contract member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The bound payload contract. | The bound payload contract. | The recorded payload contract member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.4 — messenger contract
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The messenger contract member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound messenger contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The bound messenger contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded messenger contract member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The bound messenger contract. | The bound messenger contract. | The recorded messenger contract member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.5 — gate configuration references
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The gate configuration references member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — References to the bound gate configurations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — References to the bound gate configurations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded gate configuration references member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | References to the bound gate configurations. | References to the bound gate configurations. | The recorded gate configuration references member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.6 — dual-model handoff arrangement
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The dual-model handoff arrangement member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The handoff arrangement of the accepted dual-model handoff package, §§1–4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The handoff arrangement of the accepted dual-model handoff package, §§1–4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded dual-model handoff arrangement member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The handoff arrangement of the accepted dual-model handoff package, §§1–4. | The handoff arrangement of the accepted dual-model handoff package, §§1–4. | The recorded dual-model handoff arrangement member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.2.4.7 — system_configuration_digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The system_configuration_digest member of Combined handoff configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The digest of the combined system configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Does: ACCEPTED — The digest of the combined system configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded system_configuration_digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.2.4 — Combined handoff configuration | The digest of the combined system configuration. | The digest of the combined system configuration. | The recorded system_configuration_digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3 — policy_epoch (E2e)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The exact set of pass-bearing accepted policy versions frozen for a family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Takes in: ACCEPTED — All policy kinds required by that family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Does: ACCEPTED — Binds every required current accepted version; currentness lasts only while every named policy is current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gives out: ACCEPTED — A frozen policy epoch, or no admissible evidentiary run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Must never: ACCEPTED — Omit the gold aggregate rule from a B24 epoch containing gold cells; use an unset trial count; include B9 budget values as epoch members. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Incomplete or non-current epoch blocks evidentiary run opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.3.1 — trial_count_policy_ref: The accepted planned-trial count; unset blocks evidentiary opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.2 — tolerance/acceptance rule references: Accepted rules for every suite kind used by the scope’s cells, including the gold aggregate rule for B24 scopes containing sealed gold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.3 — required-coverage profile: The required coverage, including B24 role mapping where applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.4 — measured-dimension budgets: Applicable accepted measurement budgets. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.5 — judgment-authority requirement: Accepted NHD-B16EEB-D16 proof requirement wherever Ness judgments are needed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.6 — held-out policy: The accepted held-out policy, required for held-out evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.7 — Invoked-only policies and B9 separation: Cites invalidity and disagreement policies in the records invoking them; B9 admissions bind their own budget-config versions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.3.8 — hardware-need / purchase criteria reference: For B24 eligibility, the accepted NHD-B16EEB-D5 policy is required; its value is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.1 — trial_count_policy_ref: No evidentiary run opens or executes with trial_count_policy_ref unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.4 — Run class freeze: Evidentiary opening requires the complete current policy epoch; exploratory classification cannot later become evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | All policy kinds required by that family. | Binds every required current accepted version; currentness lasts only while every named policy is current. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | All policy kinds required by that family. | Uses the E2e canonical record defined by this card. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.4.3 — Authoritative current result | All policy kinds required by that family. | The result’s epoch must still be current. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | All policy kinds required by that family. | When registering this setup record kind: Binds every required current accepted version; currentness lasts only while every named policy is current. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | All policy kinds required by that family. | Binds every required current accepted version; currentness lasts only while every named policy is current. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.2.4 — Run class freeze | All policy kinds required by that family. | Binds every required current accepted version; currentness lasts only while every named policy is current. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | All policy kinds required by that family. | For this requested record kind, appends the E2e canonical record when its stated commit conditions hold; earlier records remain unchanged. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | All policy kinds required by that family. | For the corresponding requested record kind, commits E2e at this boundary only after its stated gates; existing records are not overwritten. | A frozen policy epoch, or no admissible evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.3.1 — trial_count_policy_ref; C-GOLD.1.2.3.2 — tolerance/acceptance rule references; C-GOLD.1.2.3.3 — required-coverage profile; C-GOLD.1.2.3.4 — measured-dimension budgets; C-GOLD.1.2.3.5 — judgment-authority requirement; C-GOLD.1.2.3.6 — held-out policy; C-GOLD.1.2.3.7 — Invoked-only policies and B9 separation; C-GOLD.1.2.3.8 — hardware-need / purchase criteria reference

### C-GOLD.1.2.3.1 — trial_count_policy_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The trial_count_policy_ref member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — The accepted planned-trial count; unset blocks evidentiary opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — The accepted planned-trial count; unset blocks evidentiary opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded trial_count_policy_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Open/execute an evidentiary run while trial_count_policy_ref is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unset trial count blocks evidentiary opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | The accepted planned-trial count; unset blocks evidentiary opening and execution. | The accepted planned-trial count; unset blocks evidentiary opening and execution. | The recorded trial_count_policy_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | The accepted planned-trial count; unset blocks evidentiary opening and execution. | No evidentiary run opens or executes with trial_count_policy_ref unset. | The recorded trial_count_policy_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.2.4 — Run class freeze | The accepted planned-trial count; unset blocks evidentiary opening and execution. | No evidentiary run opens or executes with trial_count_policy_ref unset. | The recorded trial_count_policy_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The accepted planned-trial count; unset blocks evidentiary opening and execution. | No evidentiary run opens or executes with trial_count_policy_ref unset. | The recorded trial_count_policy_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.2.6 — Planned trial identity and full trial plan | The accepted planned-trial count; unset blocks evidentiary opening and execution. | The trial plan uses the accepted trial count; without it no evidentiary run opens. | The recorded trial_count_policy_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.2 — tolerance/acceptance rule references
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The tolerance/acceptance rule references member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — Accepted rules for every suite kind used by the scope’s cells, including the gold aggregate rule for B24 scopes containing sealed gold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — Accepted rules for every suite kind used by the scope’s cells, including the gold aggregate rule for B24 scopes containing sealed gold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded tolerance/acceptance rule references member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | Accepted rules for every suite kind used by the scope’s cells, including the gold aggregate rule for B24 scopes containing sealed gold. | Accepted rules for every suite kind used by the scope’s cells, including the gold aggregate rule for B24 scopes containing sealed gold. | The recorded tolerance/acceptance rule references member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.3 — required-coverage profile
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The required-coverage profile member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — The required coverage, including B24 role mapping where applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — The required coverage, including B24 role mapping where applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded required-coverage profile member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | The required coverage, including B24 role mapping where applicable. | The required coverage, including B24 role mapping where applicable. | The recorded required-coverage profile member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.4 — measured-dimension budgets
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The measured-dimension budgets member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — Applicable accepted measurement budgets. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — Applicable accepted measurement budgets. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded measured-dimension budgets member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | Applicable accepted measurement budgets. | Applicable accepted measurement budgets. | The recorded measured-dimension budgets member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.5 — judgment-authority requirement
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment-authority requirement member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — Accepted NHD-B16EEB-D16 proof requirement wherever Ness judgments are needed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — Accepted NHD-B16EEB-D16 proof requirement wherever Ness judgments are needed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded judgment-authority requirement member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | Accepted NHD-B16EEB-D16 proof requirement wherever Ness judgments are needed. | Accepted NHD-B16EEB-D16 proof requirement wherever Ness judgments are needed. | The recorded judgment-authority requirement member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.6 — held-out policy
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The held-out policy member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — The accepted held-out policy, required for held-out evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — The accepted held-out policy, required for held-out evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded held-out policy member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | The accepted held-out policy, required for held-out evidence. | The accepted held-out policy, required for held-out evidence. | The recorded held-out policy member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.7 — Invoked-only policies and B9 separation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Invoked-only policies and B9 separation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Takes in: ACCEPTED — An invoked invalidity or disagreement rule; a B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Does: ACCEPTED — Cites invalidity and disagreement policies in the records invoking them; B9 admissions bind their own budget-config versions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Gives out: ACCEPTED — Policy bindings remain separate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Must never: ACCEPTED — Treat B9 values as epoch members or require invoked-only policies when they are not invoked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | An invoked invalidity or disagreement rule; a B9 admission. | Cites invalidity and disagreement policies in the records invoking them; B9 admissions bind their own budget-config versions. | Policy bindings remain separate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.3.8 — hardware-need / purchase criteria reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The hardware-need / purchase criteria reference member of policy_epoch (E2e). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Takes in: ACCEPTED — For B24 eligibility, the accepted NHD-B16EEB-D5 policy is required; its value is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Does: ACCEPTED — For B24 eligibility, the accepted NHD-B16EEB-D5 policy is required; its value is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Gives out: ACCEPTED — The recorded hardware-need / purchase criteria reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | For B24 eligibility, the accepted NHD-B16EEB-D5 policy is required; its value is unset. | For B24 eligibility, the accepted NHD-B16EEB-D5 policy is required; its value is unset. | The recorded hardware-need / purchase criteria reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §16] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.4 — Run class freeze
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The permanent classification fixed at run open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Takes in: ACCEPTED — An evidentiary or exploratory run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Does: ACCEPTED — Freezes evidentiary runs to the complete current epoch, suite manifest and registered profile; exploratory runs remain non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gives out: ACCEPTED — One fixed run class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Must never: ACCEPTED — Promote exploratory runs into evidence later. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing current epoch, suite manifest, registered profile or trial count prevents evidentiary execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.4.1 — Evidentiary run admission: Opens and executes only after every required item exists; freezes the epoch into the run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.4.2 — Exploratory permanence: Keeps the run permanently non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.1 — trial_count_policy_ref: No evidentiary run opens or executes with trial_count_policy_ref unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): Binds every required current accepted version; currentness lasts only while every named policy is current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | An evidentiary or exploratory run. | Freezes evidentiary runs to the complete current epoch, suite manifest and registered profile; exploratory runs remain non_evidentiary. | One fixed run class. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | An evidentiary or exploratory run. | Evidentiary opening requires the complete current policy epoch; exploratory classification cannot later become evidentiary. | One fixed run class. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.4.1 — Evidentiary run admission; C-GOLD.1.2.4.2 — Exploratory permanence

### C-GOLD.1.2.4.1 — Evidentiary run admission
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Evidentiary run admission rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Takes in: ACCEPTED — Complete current epoch, accepted suite manifest and registered profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Does: ACCEPTED — Opens and executes only after every required item exists; freezes the epoch into the run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gives out: ACCEPTED — An evidentiary run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Must never: ACCEPTED — Open or execute with trial_count_policy_ref unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Refuses evidentiary opening or execution when the complete epoch is absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Complete current epoch, accepted manifest, registered profile and set trial count are mandatory. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.4 — Run class freeze | Complete current epoch, accepted suite manifest and registered profile. | Opens and executes only after every required item exists; freezes the epoch into the run. | An evidentiary run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.4.2 — Exploratory permanence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Exploratory permanence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Takes in: ACCEPTED — An exploratory run fixed at open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the run permanently non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gives out: ACCEPTED — No evidentiary contribution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Must never: ACCEPTED — Reclassify exploratory outputs as evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Exploratory runs contribute no evidence or passing result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The exploratory class is fixed at run open and permanently non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.4 — Run class freeze | An exploratory run fixed at open. | Keeps the run permanently non_evidentiary. | No evidentiary contribution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5 — Evaluation scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One target family and exact evaluated configuration under one policy epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — Target family, E4/E4S digest, role/system and epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — Assigns one run to exactly one scope and one family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — A scope tuple. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge families within a run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.5.1 — target family: Exactly one of gold_evidence, held_out_evidence or b24_system_eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.2 — candidate profile digest: The E4 or E4S candidate digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.3 — role/system: The role or combined system under evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.4 — policy epoch: The scope’s policy epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.5 — gold_evidence family: Keeps the run in the gold_evidence family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.6 — held_out_evidence family: Keeps the run in the held_out_evidence family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.5.7 — b24_system_eligibility family: Keeps the run in the b24_system_eligibility family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | Target family, E4/E4S digest, role/system and epoch. | Assigns one run to exactly one scope and one family. | A scope tuple. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.5.1 — target family; C-GOLD.1.2.5.2 — candidate profile digest; C-GOLD.1.2.5.3 — role/system; C-GOLD.1.2.5.4 — policy epoch; C-GOLD.1.2.5.5 — gold_evidence family; C-GOLD.1.2.5.6 — held_out_evidence family; C-GOLD.1.2.5.7 — b24_system_eligibility family

### C-GOLD.1.2.5.1 — target family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The target family member of Evaluation scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — Exactly one of gold_evidence, held_out_evidence or b24_system_eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — Exactly one of gold_evidence, held_out_evidence or b24_system_eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded target family member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge different scope or family values into the single-run identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | Exactly one of gold_evidence, held_out_evidence or b24_system_eligibility. | Exactly one of gold_evidence, held_out_evidence or b24_system_eligibility. | The recorded target family member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.2 — candidate profile digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The candidate profile digest member of Evaluation scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — The E4 or E4S candidate digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — The E4 or E4S candidate digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded candidate profile digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge different scope or family values into the single-run identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | The E4 or E4S candidate digest. | The E4 or E4S candidate digest. | The recorded candidate profile digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.3 — role/system
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The role/system member of Evaluation scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — The role or combined system under evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — The role or combined system under evaluation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded role/system member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge different scope or family values into the single-run identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | The role or combined system under evaluation. | The role or combined system under evaluation. | The recorded role/system member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.4 — policy epoch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The policy epoch member of Evaluation scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — The scope’s policy epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — The scope’s policy epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded policy epoch member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge different scope or family values into the single-run identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | The scope’s policy epoch. | The scope’s policy epoch. | The recorded policy epoch member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.5 — gold_evidence family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The gold_evidence family rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — A run assigned to this target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the run in the gold_evidence family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — One family-specific scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge this family with another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | A run assigned to this target family. | Keeps the run in the gold_evidence family. | One family-specific scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.6 — held_out_evidence family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The held_out_evidence family rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — A run assigned to this target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the run in the held_out_evidence family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — One family-specific scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge this family with another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | A run assigned to this target family. | Keeps the run in the held_out_evidence family. | One family-specific scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.5.7 — b24_system_eligibility family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The b24_system_eligibility family rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Takes in: ACCEPTED — A run assigned to this target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the run in the b24_system_eligibility family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Gives out: ACCEPTED — One family-specific scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Must never: ACCEPTED — Merge this family with another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — One run belongs to exactly one scope and one target family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.5 — Evaluation scope | A run assigned to this target family. | Keeps the run in the b24_system_eligibility family. | One family-specific scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.6 — Planned trial identity and full trial plan
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The measurement unit, distinct from technical re-attempts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — run, case_id and trial_index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — Uses planned_trial_key as canonical identity and one B9 retry group; the plan equals the complete suite case list × epoch trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — A full set of planned measurement trials. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Replace a planned trial or completed output with a retry; accept a subset plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E5 refuses a plan that omits any suite-case/trial-count combination. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.6.1 — run: The evaluation run containing the planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.6.2 — case_id: The suite case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.6.3 — trial_index: The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.6.4 — planned_trial_key: The canonical B9 source-operation identity for this planned trial; one B9 retry group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.1 — trial_count_policy_ref: The trial plan uses the accepted trial count; without it no evidentiary run opens. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | run, case_id and trial_index. | Uses planned_trial_key as canonical identity and one B9 retry group; the plan equals the complete suite case list × epoch trial count. | A full set of planned measurement trials. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | run, case_id and trial_index. | The complete suite case list × epoch trial count must be the trial plan; subset plans are refused. | A full set of planned measurement trials. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.6.1 — run; C-GOLD.1.2.6.2 — case_id; C-GOLD.1.2.6.3 — trial_index; C-GOLD.1.2.6.4 — planned_trial_key

### C-GOLD.1.2.6.1 — run
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The run member of Planned trial identity and full trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The evaluation run containing the planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — The evaluation run containing the planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded run member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Use a retry to create or replace a planned trial or its completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The planned trial is the fixed run/case_id/trial_index identity; one planned_trial_key identifies one B9 source operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.6 — Planned trial identity and full trial plan | The evaluation run containing the planned trial. | The evaluation run containing the planned trial. | The recorded run member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.6.2 — case_id
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The case_id member of Planned trial identity and full trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The suite case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — The suite case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded case_id member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Use a retry to create or replace a planned trial or its completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The planned trial is the fixed run/case_id/trial_index identity; one planned_trial_key identifies one B9 source operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.6 — Planned trial identity and full trial plan | The suite case identity. | The suite case identity. | The recorded case_id member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.6.3 — trial_index
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The trial_index member of Planned trial identity and full trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded trial_index member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Use a retry to create or replace a planned trial or its completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The planned trial is the fixed run/case_id/trial_index identity; one planned_trial_key identifies one B9 source operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.6 — Planned trial identity and full trial plan | The planned repetition index. | The planned repetition index. | The recorded trial_index member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.6.4 — planned_trial_key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The planned_trial_key member of Planned trial identity and full trial plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The canonical B9 source-operation identity for this planned trial; one B9 retry group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — The canonical B9 source-operation identity for this planned trial; one B9 retry group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded planned_trial_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Use a retry to create or replace a planned trial or its completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A completed output absorbs retries; an unknown output is not retried until resolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The planned trial is the fixed run/case_id/trial_index identity; one planned_trial_key identifies one B9 source operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.6 — Planned trial identity and full trial plan | The canonical B9 source-operation identity for this planned trial; one B9 retry group. | The canonical B9 source-operation identity for this planned trial; one B9 retry group. | The recorded planned_trial_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7 — Coverage cells and named measurements
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Actual evaluated coverage, separate from its declaration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Required cells and named measurements, and actual completed runs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Requires complete current passed evidentiary runs matching each cell exactly and full suite × trial count; declared measurements require actual recorded results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Satisfied cells and measurements only where these requirements hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat naming a cell or measurement as satisfying it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing runs or measurements give incomplete, never eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.7.1 — Coverage cell: Requires at least one complete current passed full-plan run matching the cell exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires recorded results; M-C2 and M-C3 must also be within the epoch budget. M-C4 is measured, recorded and reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.7.1 — Coverage cell: Requires at least one complete current passed full-plan run matching the cell exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2 — Evaluation identities and required coverage | Required cells and named measurements, and actual completed runs. | Requires complete current passed evidentiary runs matching each cell exactly and full suite × trial count; declared measurements require actual recorded results. | Satisfied cells and measurements only where these requirements hold. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.7.1 — Coverage cell; C-GOLD.1.2.7.2 — Named measurement satisfaction

### C-GOLD.1.2.7.1 — Coverage cell
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The exact suite, family, measurement-scope and execution-binding tuple. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The declared cell and an evidentiary run’s E5. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Requires at least one complete current passed full-plan run matching the cell exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — A satisfied cell only after an actual matching run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Count declarations or partial-plan runs as cell satisfaction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A required cell without a satisfying run is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.7.1.1 — suite manifest and version: The exact concrete suite manifest and version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.1.2 — suite family: The §7B.2 family, or sealed_gold_rule_8 for gold cells in B24 coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.1.3 — measurement scope: The §7B.3 analyst, messenger or combined measurement scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.1.4 — execution binding: The exact execution binding; a gold-family cell is only gold suite + version and path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): Uses the exact E5 cell and full trial plan when matching an actual passed run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): Freezes the run’s exact evidence context before execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7 — Coverage cells and named measurements | The declared cell and an evidentiary run’s E5. | Requires at least one complete current passed full-plan run matching the cell exactly. | A satisfied cell only after an actual matching run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.7 — Coverage cells and named measurements | The declared cell and an evidentiary run’s E5. | Requires at least one complete current passed full-plan run matching the cell exactly. | A satisfied cell only after an actual matching run. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.7.1.1 — suite manifest and version; C-GOLD.1.2.7.1.2 — suite family; C-GOLD.1.2.7.1.3 — measurement scope; C-GOLD.1.2.7.1.4 — execution binding

### C-GOLD.1.2.7.1.1 — suite manifest and version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The suite manifest and version member of Coverage cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact concrete suite manifest and version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — The exact concrete suite manifest and version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded suite manifest and version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Count an unmatched run or a declared cell alone as satisfied coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A required cell without an exact satisfying run is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The actual completed current passed full-plan run must match every declared cell member exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | The exact concrete suite manifest and version. | The exact concrete suite manifest and version. | The recorded suite manifest and version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.1.2 — suite family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The suite family member of Coverage cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The §7B.2 family, or sealed_gold_rule_8 for gold cells in B24 coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — The §7B.2 family, or sealed_gold_rule_8 for gold cells in B24 coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded suite family member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Count an unmatched run or a declared cell alone as satisfied coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A required cell without an exact satisfying run is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The actual completed current passed full-plan run must match every declared cell member exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | The §7B.2 family, or sealed_gold_rule_8 for gold cells in B24 coverage. | The §7B.2 family, or sealed_gold_rule_8 for gold cells in B24 coverage. | The recorded suite family member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.1.3 — measurement scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The measurement scope member of Coverage cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The §7B.3 analyst, messenger or combined measurement scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — The §7B.3 analyst, messenger or combined measurement scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded measurement scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Count an unmatched run or a declared cell alone as satisfied coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A required cell without an exact satisfying run is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The actual completed current passed full-plan run must match every declared cell member exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | The §7B.3 analyst, messenger or combined measurement scope. | The §7B.3 analyst, messenger or combined measurement scope. | The recorded measurement scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.1.4 — execution binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The execution binding member of Coverage cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact execution binding; a gold-family cell is only gold suite + version and path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — The exact execution binding; a gold-family cell is only gold suite + version and path binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded execution binding member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Count an unmatched run or a declared cell alone as satisfied coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A required cell without an exact satisfying run is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The actual completed current passed full-plan run must match every declared cell member exactly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | The exact execution binding; a gold-family cell is only gold suite + version and path binding. | The exact execution binding; a gold-family cell is only gold suite + version and path binding. | The recorded execution binding member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2 — Named measurement satisfaction
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — An actually recorded named measurement in a satisfied covering cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Requires recorded results; M-C2 and M-C3 must also be within the epoch budget. M-C4 is measured, recorded and reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — A satisfied recorded measurement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Invent a budget for M-C4 or count declaration alone. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing results yield incomplete; applicable budget limits still bind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.1 — M-A1 — depth: Records depth from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.2 — M-A2 — evidence fidelity: Records evidence fidelity from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.3 — M-A3 — channel/scope discipline: Records channel/scope discipline from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.4 — M-A4 — lane separation: Records lane separation from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.5 — M-A5 — refusal to fabricate: Records refusal to fabricate from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.6 — M-M1 — live usability: Records live usability from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.7 — M-M2 — warmth: Records warmth from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.8 — M-M3 — translation fidelity incl. Hebrew: Records translation fidelity incl. Hebrew from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.9 — M-M4 — strict bounded obedience: Records strict bounded obedience from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.10 — M-M5 — distortion resistance: Records distortion resistance from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.11 — M-C1 — handoff reliability: Records handoff reliability from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.12 — M-C2 — total latency: Records total latency from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.13 — M-C3 — memory/GPU behavior: Records memory/GPU behavior from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.2.7.2.14 — M-C4 — whether the heavy model must run every turn: Records whether the heavy model must run every turn from a satisfied cell’s current aggregate head. Reports the result in E12; no pass/fail budget exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): Requires recorded measurement results from a satisfied covering cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7 — Coverage cells and named measurements | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires recorded results; M-C2 and M-C3 must also be within the epoch budget. M-C4 is measured, recorded and reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.7.2.1 — M-A1 — depth | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.2.7.2.2 — M-A2 — evidence fidelity | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.2.7.2.3 — M-A3 — channel/scope discipline | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.2.7.2.4 — M-A4 — lane separation | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.2.7.2.5 — M-A5 — refusal to fabricate | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.2.7.2.6 — M-M1 — live usability | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.2.7.2.7 — M-M2 — warmth | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.2.7.2.8 — M-M3 — translation fidelity incl. Hebrew | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.2.7.2.9 — M-M4 — strict bounded obedience | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.2.7.2.10 — M-M5 — distortion resistance | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.2.7.2.11 — M-C1 — handoff reliability | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.2.7.2.12 — M-C2 — total latency | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.2.7.2.13 — M-C3 — memory/GPU behavior | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.2.7.2.14 — M-C4 — whether the heavy model must run every turn | Current aggregate-head measurement results from a satisfied cell whose suite declares the measurement. | Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. | A satisfied recorded measurement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.2.7.2.1 — M-A1 — depth; C-GOLD.1.2.7.2.2 — M-A2 — evidence fidelity; C-GOLD.1.2.7.2.3 — M-A3 — channel/scope discipline; C-GOLD.1.2.7.2.4 — M-A4 — lane separation; C-GOLD.1.2.7.2.5 — M-A5 — refusal to fabricate; C-GOLD.1.2.7.2.6 — M-M1 — live usability; C-GOLD.1.2.7.2.7 — M-M2 — warmth; C-GOLD.1.2.7.2.8 — M-M3 — translation fidelity incl. Hebrew; C-GOLD.1.2.7.2.9 — M-M4 — strict bounded obedience; C-GOLD.1.2.7.2.10 — M-M5 — distortion resistance; C-GOLD.1.2.7.2.11 — M-C1 — handoff reliability; C-GOLD.1.2.7.2.12 — M-C2 — total latency; C-GOLD.1.2.7.2.13 — M-C3 — memory/GPU behavior; C-GOLD.1.2.7.2.14 — M-C4 — whether the heavy model must run every turn

### C-GOLD.1.2.7.2.1 — M-A1 — depth
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-A1 — depth rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded depth results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records depth from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded depth results. | Records depth from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.2 — M-A2 — evidence fidelity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-A2 — evidence fidelity rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded evidence fidelity results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records evidence fidelity from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded evidence fidelity results. | Records evidence fidelity from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.3 — M-A3 — channel/scope discipline
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-A3 — channel/scope discipline rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded channel/scope discipline results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records channel/scope discipline from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded channel/scope discipline results. | Records channel/scope discipline from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.4 — M-A4 — lane separation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-A4 — lane separation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded lane separation results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records lane separation from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded lane separation results. | Records lane separation from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.5 — M-A5 — refusal to fabricate
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-A5 — refusal to fabricate rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded refusal to fabricate results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records refusal to fabricate from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded refusal to fabricate results. | Records refusal to fabricate from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.6 — M-M1 — live usability
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-M1 — live usability rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded live usability results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records live usability from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded live usability results. | Records live usability from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.7 — M-M2 — warmth
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-M2 — warmth rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded warmth results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records warmth from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded warmth results. | Records warmth from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.8 — M-M3 — translation fidelity incl. Hebrew
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-M3 — translation fidelity incl. Hebrew rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded translation fidelity incl. Hebrew results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records translation fidelity incl. Hebrew from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded translation fidelity incl. Hebrew results. | Records translation fidelity incl. Hebrew from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.9 — M-M4 — strict bounded obedience
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-M4 — strict bounded obedience rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded strict bounded obedience results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records strict bounded obedience from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded strict bounded obedience results. | Records strict bounded obedience from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.10 — M-M5 — distortion resistance
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-M5 — distortion resistance rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded distortion resistance results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records distortion resistance from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded distortion resistance results. | Records distortion resistance from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.11 — M-C1 — handoff reliability
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-C1 — handoff reliability rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded handoff reliability results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records handoff reliability from a satisfied cell’s current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded handoff reliability results. | Records handoff reliability from a satisfied cell’s current aggregate head. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.12 — M-C2 — total latency
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-C2 — total latency rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded total latency results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records total latency from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded total latency results. | Records total latency from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.13 — M-C3 — memory/GPU behavior
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-C3 — memory/GPU behavior rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded memory/GPU behavior results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records memory/GPU behavior from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded memory/GPU behavior results. | Records memory/GPU behavior from a satisfied cell’s current aggregate head. Requires results within the epoch’s budget. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.2.7.2.14 — M-C4 — whether the heavy model must run every turn
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The M-C4 — whether the heavy model must run every turn rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded whether the heavy model must run every turn results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Does: ACCEPTED — Records whether the heavy model must run every turn from a satisfied cell’s current aggregate head. Reports the result in E12; no pass/fail budget exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Gives out: ACCEPTED — Actual measured result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the measurement name alone as a result. Invent a pass/fail budget for this measurement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without recorded results this measurement is unsatisfied and the result is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.2.7.2 — Named measurement satisfaction: Requires actual recorded results in a satisfied covering cell’s current head; applicable budgets bind, while M-C4 is reported without a pass/fail budget. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Recorded whether the heavy model must run every turn results. | Records whether the heavy model must run every turn from a satisfied cell’s current aggregate head. Reports the result in E12; no pass/fail budget exists. | Actual measured result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3 — Canonical evaluation record family
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The immutable E1–E16 family; proposed names describe contracts, not selected serialization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Takes in: ACCEPTED — References and integrity identities; no copied gold, root or reading text. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Does: ACCEPTED — Appends immutable records; corrections are new linked records; each has integrity reference, schema_version and creating operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Gives out: ACCEPTED — Preserved canonical records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Must never: ACCEPTED — Edit records in place, copy gold-case/root/reading text or treat canonical records as operational logs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fails closed by: ACCEPTED — Unreadable records make downstream state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fails closed by: ACCEPTED — Unreadable canonical records make downstream state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: Keeps it immutable and append-only; corrections append new linked records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.3 — benchmark_policy_reference (E2): Resolves only accepted policies; it creates no policy itself. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): Uses the E2e canonical record defined by this card. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.2.1 — model_evaluation_profile (E4): Uses the E4 canonical record defined by this card. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.2.2 — system_candidate_profile (E4S): Uses the E4S canonical record defined by this card. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.4 — required_coverage_profile (E3): Checks all required families, scopes, named measurements and both bound gold sets before registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): Freezes the run’s exact evidence context before execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.6 — trial_attempt_start (E6): Records ordinal 1 as original execution; every later attempt binds committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Records completed, failed, interrupted/abandoned or unresolved outcome. Deterministic findings bind the exact accepted checker. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): Records resolved_output_found, resolved_absence_proven or still_undetermined; preserves E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): Closes only when all started attempts have E7 and no attempt is live or admitted-unstarted; freezes the terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.12 — gold_evidence_result (E11a): Derives one deterministic result at one ledger head; carries prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.13 — held_out_evidence_result (E11b): Derives one deterministic result at one ledger head; carries prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.14 — b24_system_eligibility_result (E12): Reports system eligibility only when every required condition holds; reports every measurement including M-C4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13): Points only to E11a for input 3 or E11b for input 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.16 — evaluation_invalidity_record (E14): Excludes only under that accepted rule; no such rule currently exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.17 — evaluation_conflict_resolution (E15): Resolves only within the accepted policy’s scope, binding every affected run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16): Commits together with exactly one scope-relevant canonical record by compare-and-append. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Fed by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: Applies §7Q before §7R and SACL where applicable; uses identities and integrity references only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | References and integrity identities; no copied gold, root or reading text. | Appends immutable records; corrections are new linked records; each has integrity reference, schema_version and creating operation identity. | Preserved canonical records. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.1 — Canonical record preservation; C-GOLD.1.3.2 — evaluation_suite_manifest (E1); C-GOLD.1.3.3 — benchmark_policy_reference (E2); C-GOLD.1.3.4 — required_coverage_profile (E3); C-GOLD.1.3.5 — evaluation_run_open (E5); C-GOLD.1.3.6 — trial_attempt_start (E6); C-GOLD.1.3.7 — trial_attempt_terminal (E7); C-GOLD.1.3.8 — trial_attempt_resolution (E7r); C-GOLD.1.3.9 — evaluation_run_terminal (E8); C-GOLD.1.3.10 — evaluation_judgment (E9); C-GOLD.1.3.11 — suite_aggregate_result (E10); C-GOLD.1.3.12 — gold_evidence_result (E11a); C-GOLD.1.3.13 — held_out_evidence_result (E11b); C-GOLD.1.3.14 — b24_system_eligibility_result (E12); C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13); C-GOLD.1.3.16 — evaluation_invalidity_record (E14); C-GOLD.1.3.17 — evaluation_conflict_resolution (E15); C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16); C-GOLD.1.3.19 — Evaluation privacy and access

### C-GOLD.1.3.1 — Canonical record preservation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Canonical record preservation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Any canonical evaluation record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps it immutable and append-only; corrections append new linked records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — Original and correction records preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Edit or delete canonical records or copy gold-case, root or reading text. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If a canonical record is unreadable, downstream state is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.1.1 — integrity reference: Each canonical record carries its integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.1.2 — schema_version: Each canonical record carries schema_version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.1.3 — creating operation identity: Each canonical record carries the creating operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Any canonical evaluation record. | Keeps it immutable and append-only; corrections append new linked records. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.3.2.1 — kind | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.3.2.2 — name | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.3.2.3 — version | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.3.2.4 — integrity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.3.2.5 — seal reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.3.2.6 — ordered case identities | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.3.2.7 — case integrity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.3.2.8 — governing scoring-rules reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.3.2.9 — acceptance_source_ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.3.2.10 — §7Q classification | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.3.2.11 — per-case scoring binding | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.3.2.12.1 — judgment mode | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 16 · ACCEPTED | C-GOLD.1.3.2.12.2 — governing scoring-rule reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 17 · ACCEPTED | C-GOLD.1.3.2.12.3 — checker configuration identity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 18 · ACCEPTED | C-GOLD.1.3.2.12.4 — checker configuration version | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 19 · ACCEPTED | C-GOLD.1.3.2.12.5 — §7C category mapping | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 20 · ACCEPTED | C-GOLD.1.3.2.13 — sealed_gold suite contract | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 21 · ACCEPTED | C-GOLD.1.3.2.14 — held_out suite contract | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 22 · ACCEPTED | C-GOLD.1.3.2.15 — benchmark_family suite contract | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 23 · ACCEPTED | C-GOLD.1.3.3 — benchmark_policy_reference (E2) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 24 · ACCEPTED | C-GOLD.1.3.3.1 — policy record pointer | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 25 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 26 · ACCEPTED | C-GOLD.1.3.4.1 — required cells | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 27 · ACCEPTED | C-GOLD.1.3.4.2 — B24 role mapping | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 28 · ACCEPTED | C-GOLD.1.3.4.3 — required policy kinds | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 29 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 30 · ACCEPTED | C-GOLD.1.3.4.4.1 — Family coverage | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 31 · ACCEPTED | C-GOLD.1.3.4.4.2 — Scope coverage | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 32 · ACCEPTED | C-GOLD.1.3.4.4.3 — Measurement declaration coverage | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 33 · ACCEPTED | C-GOLD.1.3.4.4.4 — Gold v1 cell | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 34 · ACCEPTED | C-GOLD.1.3.4.4.5 — Gold v2-B cell | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 35 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 36 · ACCEPTED | C-GOLD.1.3.5.1 — run ID | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 37 · ACCEPTED | C-GOLD.1.3.5.2 — class | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 38 · ACCEPTED | C-GOLD.1.3.5.3 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 39 · ACCEPTED | C-GOLD.1.3.5.4 — profile ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 40 · ACCEPTED | C-GOLD.1.3.5.5 — coverage cell | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 41 · ACCEPTED | C-GOLD.1.3.5.6 — E1 suite kind | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 42 · ACCEPTED | C-GOLD.1.3.5.7 — governing scoring-rule reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 43 · ACCEPTED | C-GOLD.1.3.5.8 — frozen epoch ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 44 · ACCEPTED | C-GOLD.1.3.5.9 — recorded execution context | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 45 · ACCEPTED | C-GOLD.1.3.5.10 — runtime/hardware configuration | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 46 · ACCEPTED | C-GOLD.1.3.5.11 — comparability group | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 47 · ACCEPTED | C-GOLD.1.3.5.12 — full trial plan | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 48 · ACCEPTED | C-GOLD.1.3.5.13 — operator | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 49 · ACCEPTED | C-GOLD.1.3.5.14 — opened_at | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 50 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 51 · ACCEPTED | C-GOLD.1.3.6.1 — run | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 52 · ACCEPTED | C-GOLD.1.3.6.2 — case_id | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 53 · ACCEPTED | C-GOLD.1.3.6.3 — trial_index | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 54 · ACCEPTED | C-GOLD.1.3.6.4 — attempt_id | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 55 · ACCEPTED | C-GOLD.1.3.6.5 — planned_trial_output_key | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 56 · ACCEPTED | C-GOLD.1.3.6.6 — B9 R1 admission reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 57 · ACCEPTED | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 58 · ACCEPTED | C-GOLD.1.3.7.1 — terminal outcome | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 59 · ACCEPTED | C-GOLD.1.3.7.2 — failure class | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 60 · ACCEPTED | C-GOLD.1.3.7.3 — checker binding | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 61 · ACCEPTED | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 62 · ACCEPTED | C-GOLD.1.3.8.1 — resolution outcome | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 63 · ACCEPTED | C-GOLD.1.3.8.2 — resolved output proof | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 64 · ACCEPTED | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 65 · ACCEPTED | C-GOLD.1.3.9.1 — terminal outcome | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 66 · ACCEPTED | C-GOLD.1.3.9.2 — frozen terminal-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 67 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 68 · ACCEPTED | C-GOLD.1.3.10.1 — judgment_chain_key | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 69 · ACCEPTED | C-GOLD.1.3.10.2 — expected_previous_judgment_head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 70 · ACCEPTED | C-GOLD.1.3.10.3 — output ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 71 · ACCEPTED | C-GOLD.1.3.10.4 — output integrity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 72 · ACCEPTED | C-GOLD.1.3.10.5 — judgment mode | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 73 · ACCEPTED | C-GOLD.1.3.10.6 — judgment_authority_ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 74 · ACCEPTED | C-GOLD.1.3.10.7 — pass / fail | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 75 · ACCEPTED | C-GOLD.1.3.10.8 — §7C classification | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 76 · ACCEPTED | C-GOLD.1.3.10.9 — human_annotation provenance | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 77 · ACCEPTED | C-GOLD.1.3.10.10 — change_reason | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 78 · ACCEPTED | C-GOLD.1.3.10.11 — model_assist_ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 79 · ACCEPTED | C-GOLD.1.3.10.12 — E9 identity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 80 · ACCEPTED | C-GOLD.1.3.10.9.1 — annotator | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 81 · ACCEPTED | C-GOLD.1.3.10.9.2 — when | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 82 · ACCEPTED | C-GOLD.1.3.10.9.3 — context_version | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 83 · ACCEPTED | C-GOLD.1.3.10.6.1 — BAI receipt reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 84 · ACCEPTED | C-GOLD.1.3.10.6.2 — SACL event-time reference | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 85 · ACCEPTED | C-GOLD.1.3.10.6.3 — deterministic checker proof | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 86 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 87 · ACCEPTED | C-GOLD.1.3.11.1 — expected_previous_head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 88 · ACCEPTED | C-GOLD.1.3.11.2 — terminal-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 89 · ACCEPTED | C-GOLD.1.3.11.3 — E7r digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 90 · ACCEPTED | C-GOLD.1.3.11.4 — current judgment-head set | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 91 · ACCEPTED | C-GOLD.1.3.11.5 — judgment-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 92 · ACCEPTED | C-GOLD.1.3.11.6 — suite kind | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 93 · ACCEPTED | C-GOLD.1.3.11.7 — scoring rule applied | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 94 · ACCEPTED | C-GOLD.1.3.11.8 — findings | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 95 · ACCEPTED | C-GOLD.1.3.11.9 — recorded named-measurement results | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 96 · ACCEPTED | C-GOLD.1.3.11.10 — coverage | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 97 · ACCEPTED | C-GOLD.1.3.11.11 — state | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 98 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 99 · ACCEPTED | C-GOLD.1.3.12.1 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 100 · ACCEPTED | C-GOLD.1.3.12.2 — bound ledger head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 101 · ACCEPTED | C-GOLD.1.3.12.3 — evaluated-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 102 · ACCEPTED | C-GOLD.1.3.12.4 — result identity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 103 · ACCEPTED | C-GOLD.1.3.12.5 — prior-scope disclosure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 104 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 105 · ACCEPTED | C-GOLD.1.3.13.1 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 106 · ACCEPTED | C-GOLD.1.3.13.2 — bound ledger head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 107 · ACCEPTED | C-GOLD.1.3.13.3 — evaluated-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 108 · ACCEPTED | C-GOLD.1.3.13.4 — result identity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 109 · ACCEPTED | C-GOLD.1.3.13.5 — prior-scope disclosure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 110 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 111 · ACCEPTED | C-GOLD.1.3.14.1 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 112 · ACCEPTED | C-GOLD.1.3.14.2 — bound ledger head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 113 · ACCEPTED | C-GOLD.1.3.14.3 — evaluated-set digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 114 · ACCEPTED | C-GOLD.1.3.14.4 — result identity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 115 · ACCEPTED | C-GOLD.1.3.14.5 — prior-scope disclosure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 116 · ACCEPTED | C-GOLD.1.3.14.6 — measurement results | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 117 · ACCEPTED | C-GOLD.1.3.14.7 — eligibility state | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 118 · ACCEPTED | C-GOLD.1.3.14.8 — named reasons | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 119 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 120 · ACCEPTED | C-GOLD.1.3.15.1 — evidence_kind | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 121 · ACCEPTED | C-GOLD.1.3.15.2 — result_ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 122 · ACCEPTED | C-GOLD.1.3.15.3 — result integrity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 123 · ACCEPTED | C-GOLD.1.3.15.4 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 124 · ACCEPTED | C-GOLD.1.3.15.5 — bound ledger head | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 125 · ACCEPTED | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 126 · ACCEPTED | C-GOLD.1.3.16.1 — excluded run | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 127 · ACCEPTED | C-GOLD.1.3.16.2 — objective invalidity rule | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 128 · ACCEPTED | C-GOLD.1.3.16.3 — objective facts | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 129 · ACCEPTED | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 130 · ACCEPTED | C-GOLD.1.3.17.1 — accepted disagreement policy | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 131 · ACCEPTED | C-GOLD.1.3.17.2 — affected-run set | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 132 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 133 · ACCEPTED | C-GOLD.1.3.18.1 — scope | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 134 · ACCEPTED | C-GOLD.1.3.18.2 — sequence_number | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 135 · ACCEPTED | C-GOLD.1.3.18.3 — record_ref | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 136 · ACCEPTED | C-GOLD.1.3.18.4 — record_integrity | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 137 · ACCEPTED | C-GOLD.1.3.18.5 — previous_entry_digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 138 · ACCEPTED | C-GOLD.1.3.12.6 — result state | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 139 · ACCEPTED | C-GOLD.1.3.13.6 — result state | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 140 · ACCEPTED | C-GOLD.1.3.7.2.1 — technical attempt failure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 141 · ACCEPTED | C-GOLD.1.3.7.2.2 — resource attempt failure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 142 · ACCEPTED | C-GOLD.1.3.7.2.3 — timeout attempt failure | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 143 · ACCEPTED | C-GOLD.1.3.10.12.1 — content digest | Any canonical evaluation record. | The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 144 · ACCEPTED | C-GOLD.1.5.12.22 — CR-22 — Unreadable record | Any canonical evaluation record. | Recovery follows this rule: Keeps it immutable and append-only; corrections append new linked records. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 145 · ACCEPTED | C-GOLD.1.2.1.1 — model identity | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 146 · ACCEPTED | C-GOLD.1.2.1.2 — execution-path bindings | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 147 · ACCEPTED | C-GOLD.1.2.1.3.1 — suite version | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 148 · ACCEPTED | C-GOLD.1.2.1.3.2 — engine identity | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 149 · ACCEPTED | C-GOLD.1.2.1.3.3 — engine version | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 150 · ACCEPTED | C-GOLD.1.2.1.3.4 — code integrity | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 151 · ACCEPTED | C-GOLD.1.2.1.3.5 — prompt | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 152 · ACCEPTED | C-GOLD.1.2.1.3.6 — context/retrieval configuration | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 153 · ACCEPTED | C-GOLD.1.2.1.3.7 — validator configuration | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 154 · ACCEPTED | C-GOLD.1.2.1.3.8 — other benchmark-protected configuration | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 155 · ACCEPTED | C-GOLD.1.2.1.3.9 — path_configuration_digest | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 156 · ACCEPTED | C-GOLD.1.2.2.1 — analyst component | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 157 · ACCEPTED | C-GOLD.1.2.2.2 — messenger component | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 158 · ACCEPTED | C-GOLD.1.2.2.3 — combined handoff configuration | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 159 · ACCEPTED | C-GOLD.1.2.2.4.1 — brief schema version | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 160 · ACCEPTED | C-GOLD.1.2.2.4.2 — B24 validator configuration | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 161 · ACCEPTED | C-GOLD.1.2.2.4.3 — payload contract | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 162 · ACCEPTED | C-GOLD.1.2.2.4.4 — messenger contract | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 163 · ACCEPTED | C-GOLD.1.2.2.4.5 — gate configuration references | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 164 · ACCEPTED | C-GOLD.1.2.2.4.6 — dual-model handoff arrangement | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 165 · ACCEPTED | C-GOLD.1.2.2.4.7 — system_configuration_digest | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 166 · ACCEPTED | C-GOLD.1.2.3.1 — trial_count_policy_ref | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 167 · ACCEPTED | C-GOLD.1.2.3.2 — tolerance/acceptance rule references | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 168 · ACCEPTED | C-GOLD.1.2.3.3 — required-coverage profile | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 169 · ACCEPTED | C-GOLD.1.2.3.4 — measured-dimension budgets | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 170 · ACCEPTED | C-GOLD.1.2.3.5 — judgment-authority requirement | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 171 · ACCEPTED | C-GOLD.1.2.3.6 — held-out policy | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 172 · ACCEPTED | C-GOLD.1.3.1.1 — integrity reference | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 173 · ACCEPTED | C-GOLD.1.3.1.2 — schema_version | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 174 · ACCEPTED | C-GOLD.1.3.1.3 — creating operation identity | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 175 · ACCEPTED | C-GOLD.1.2.1.4 — model digest | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 176 · ACCEPTED | C-GOLD.1.2.3.8 — hardware-need / purchase criteria reference | Any canonical evaluation record. | The containing canonical record is append-only and immutable; corrections cannot overwrite this member. | Original and correction records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.1.1 — integrity reference; C-GOLD.1.3.1.2 — schema_version; C-GOLD.1.3.1.3 — creating operation identity

### C-GOLD.1.3.1.1 — integrity reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The integrity reference member of Canonical record preservation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Each canonical record carries its integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Each canonical record carries its integrity reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded integrity reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.1 — Canonical record preservation | Each canonical record carries its integrity reference. | Each canonical record carries its integrity reference. | The recorded integrity reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.1.2 — schema_version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The schema_version member of Canonical record preservation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Each canonical record carries schema_version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Each canonical record carries schema_version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded schema_version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.1 — Canonical record preservation | Each canonical record carries schema_version. | Each canonical record carries schema_version. | The recorded schema_version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.1.3 — creating operation identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The creating operation identity member of Canonical record preservation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Each canonical record carries the creating operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Each canonical record carries the creating operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded creating operation identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The containing canonical record is append-only and immutable; corrections cannot overwrite this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.1 — Canonical record preservation | Each canonical record carries the creating operation identity. | Each canonical record carries the creating operation identity. | The recorded creating operation identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2 — evaluation_suite_manifest (E1)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — A frozen version of an evaluation suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Takes in: ACCEPTED — Suite identity, cases, scoring bindings, acceptance and privacy classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Does: ACCEPTED — Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gives out: ACCEPTED — An accepted, frozen suite manifest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Must never: ACCEPTED — Attach B24 severity categories to sealed-gold cases or assume gold rules for held-out. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No benchmark manifest without NHD-B16EEB-D15; no held-out manifest without an accepted held-out policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.2.1 — kind: sealed_gold, held_out or benchmark_family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.2 — name: The suite name. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.3 — version: The frozen suite version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.4 — integrity: The suite integrity identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.5 — seal reference: The suite seal reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.6 — ordered case identities: The ordered identities of every suite case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.7 — case integrity: Integrity reference for each identified case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.8 — governing scoring-rules reference: The suite’s governing scoring-rules reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.9 — acceptance_source_ref: The accepted source; benchmark suites require approval of the concrete suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.10 — §7Q classification: Privacy classification under §7Q. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.11 — per-case scoring binding: Every case has a judgment mode and governing scoring-rule reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.12 — Per-case scoring binding: Binds ness_meaning_judgment or deterministic_checker; deterministic mode names exact checker configuration and version; §7C categories exist only for benchmark_family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.13 — sealed_gold suite contract: Every case uses ness_meaning_judgment and the six settled gold rules; aggregation uses accepted NHD-B16EEB-D2 gold rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.14 — held_out suite contract: Uses only the future accepted held-out policy, including its judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.15 — benchmark_family suite contract: Binds the §7B.2 family, declared measurements, per-case scoring bindings and each finding’s §7C category, plus concrete-suite acceptance under NHD-B16EEB-D15. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.2.12 — Per-case scoring binding: Every case has its accepted mode and governing rule; checker identity/version and benchmark-only categories retain their exact scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Suite identity, cases, scoring bindings, acceptance and privacy classification. | Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.1 — EB-1 — Suite registration | Suite identity, cases, scoring bindings, acceptance and privacy classification. | Applies this defining record/rule contract: Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.12.21 — CR-21 — Suite integrity mismatch | Suite identity, cases, scoring bindings, acceptance and privacy classification. | Recovery follows this rule: Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.1 — O-SUITE | Suite identity, cases, scoring bindings, acceptance and privacy classification. | Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.1 — O-SUITE | Suite identity, cases, scoring bindings, acceptance and privacy classification. | appends the E1 canonical record when its stated commit conditions hold; earlier records remain unchanged. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.1 — EB-1 — Suite registration | Suite identity, cases, scoring bindings, acceptance and privacy classification. | For the corresponding requested record kind, commits E1 at this boundary only after its stated gates; existing records are not overwritten. | An accepted, frozen suite manifest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.2.1 — kind; C-GOLD.1.3.2.2 — name; C-GOLD.1.3.2.3 — version; C-GOLD.1.3.2.4 — integrity; C-GOLD.1.3.2.5 — seal reference; C-GOLD.1.3.2.6 — ordered case identities; C-GOLD.1.3.2.7 — case integrity; C-GOLD.1.3.2.8 — governing scoring-rules reference; C-GOLD.1.3.2.9 — acceptance_source_ref; C-GOLD.1.3.2.10 — §7Q classification; C-GOLD.1.3.2.11 — per-case scoring binding; C-GOLD.1.3.2.12 — Per-case scoring binding; C-GOLD.1.3.2.13 — sealed_gold suite contract; C-GOLD.1.3.2.14 — held_out suite contract; C-GOLD.1.3.2.15 — benchmark_family suite contract

### C-GOLD.1.3.2.1 — kind
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The kind member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — sealed_gold, held_out or benchmark_family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — sealed_gold, held_out or benchmark_family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded kind member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | sealed_gold, held_out or benchmark_family. | sealed_gold, held_out or benchmark_family. | The recorded kind member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.2 — name
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The name member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The suite name. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The suite name. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded name member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The suite name. | The suite name. | The recorded name member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.3 — version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The version member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The frozen suite version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The frozen suite version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The frozen suite version. | The frozen suite version. | The recorded version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.4 — integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The integrity member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The suite integrity identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The suite integrity identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The suite integrity identity. | The suite integrity identity. | The recorded integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.5 — seal reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The seal reference member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The suite seal reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The suite seal reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded seal reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The suite seal reference. | The suite seal reference. | The recorded seal reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.6 — ordered case identities
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The ordered case identities member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The ordered identities of every suite case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The ordered identities of every suite case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded ordered case identities member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The ordered identities of every suite case. | The ordered identities of every suite case. | The recorded ordered case identities member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.7 — case integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The case integrity member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — Integrity reference for each identified case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — Integrity reference for each identified case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded case integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Integrity reference for each identified case. | Integrity reference for each identified case. | The recorded case integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.8 — governing scoring-rules reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The governing scoring-rules reference member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The suite’s governing scoring-rules reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The suite’s governing scoring-rules reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded governing scoring-rules reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The suite’s governing scoring-rules reference. | The suite’s governing scoring-rules reference. | The recorded governing scoring-rules reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.9 — acceptance_source_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The acceptance_source_ref member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The accepted source; benchmark suites require approval of the concrete suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The accepted source; benchmark suites require approval of the concrete suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded acceptance_source_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | The accepted source; benchmark suites require approval of the concrete suite. | The accepted source; benchmark suites require approval of the concrete suite. | The recorded acceptance_source_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.10 — §7Q classification
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The §7Q classification member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — Privacy classification under §7Q. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — Privacy classification under §7Q. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded §7Q classification member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Privacy classification under §7Q. | Privacy classification under §7Q. | The recorded §7Q classification member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.11 — per-case scoring binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The per-case scoring binding member of evaluation_suite_manifest (E1). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — Every case has a judgment mode and governing scoring-rule reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — Every case has a judgment mode and governing scoring-rule reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded per-case scoring binding member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Every case has a judgment mode and governing scoring-rule reference. | Every case has a judgment mode and governing scoring-rule reference. | The recorded per-case scoring binding member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.12 — Per-case scoring binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The accepted judgment mode and rule for one suite case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Case identity, judgment mode, scoring rule and applicable checker/category bindings. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Binds ness_meaning_judgment or deterministic_checker; deterministic mode names exact checker configuration and version; §7C categories exist only for benchmark_family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — One explicit accepted binding per case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Use an unbound checker, treat model assistance as judgment authority, or attach §7C categories to gold cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A checker different from the E1 binding makes its finding invalid and the run head indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.2.12.1 — judgment mode: ness_meaning_judgment or deterministic_checker; held-out authority awaits its own policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.12.2 — governing scoring-rule reference: The governing rule for this case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.12.3 — checker configuration identity: For deterministic_checker: exact checker identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.12.4 — checker configuration version: For deterministic_checker: exact checker version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.2.12.5 — §7C category mapping: Only for benchmark_family findings; absent on sealed-gold cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Case identity, judgment mode, scoring rule and applicable checker/category bindings. | Binds ness_meaning_judgment or deterministic_checker; deterministic mode names exact checker configuration and version; §7C categories exist only for benchmark_family. | One explicit accepted binding per case. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Case identity, judgment mode, scoring rule and applicable checker/category bindings. | Every case has its accepted mode and governing rule; checker identity/version and benchmark-only categories retain their exact scope. | One explicit accepted binding per case. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.2.12.1 — judgment mode; C-GOLD.1.3.2.12.2 — governing scoring-rule reference; C-GOLD.1.3.2.12.3 — checker configuration identity; C-GOLD.1.3.2.12.4 — checker configuration version; C-GOLD.1.3.2.12.5 — §7C category mapping

### C-GOLD.1.3.2.12.1 — judgment mode
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment mode member of Per-case scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — ness_meaning_judgment or deterministic_checker; held-out authority awaits its own policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — ness_meaning_judgment or deterministic_checker; held-out authority awaits its own policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded judgment mode member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | ness_meaning_judgment or deterministic_checker; held-out authority awaits its own policy. | ness_meaning_judgment or deterministic_checker; held-out authority awaits its own policy. | The recorded judgment mode member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.12.2 — governing scoring-rule reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The governing scoring-rule reference member of Per-case scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The governing rule for this case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The governing rule for this case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded governing scoring-rule reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | The governing rule for this case. | The governing rule for this case. | The recorded governing scoring-rule reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.12.3 — checker configuration identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The checker configuration identity member of Per-case scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — For deterministic_checker: exact checker identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — For deterministic_checker: exact checker identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded checker configuration identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | For deterministic_checker: exact checker identity. | For deterministic_checker: exact checker identity. | The recorded checker configuration identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.12.4 — checker configuration version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The checker configuration version member of Per-case scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — For deterministic_checker: exact checker version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — For deterministic_checker: exact checker version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded checker configuration version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | For deterministic_checker: exact checker version. | For deterministic_checker: exact checker version. | The recorded checker configuration version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.12.5 — §7C category mapping
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The §7C category mapping member of Per-case scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — Only for benchmark_family findings; absent on sealed-gold cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — Only for benchmark_family findings; absent on sealed-gold cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded §7C category mapping member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2.12 — Per-case scoring binding | Only for benchmark_family findings; absent on sealed-gold cases. | Only for benchmark_family findings; absent on sealed-gold cases. | The recorded §7C category mapping member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.13 — sealed_gold suite contract
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The sealed_gold suite contract rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Takes in: ACCEPTED — sealed_gold suite proposal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Does: ACCEPTED — Every case uses ness_meaning_judgment and the six settled gold rules; aggregation uses accepted NHD-B16EEB-D2 gold rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Kind-specific manifest constraints. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Must never: ACCEPTED — Add a §7C category or let a §7C label change or supplement gold scoring. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No gold pass without the accepted gold aggregate rule and required authorized judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | sealed_gold suite proposal. | Every case uses ness_meaning_judgment and the six settled gold rules; aggregation uses accepted NHD-B16EEB-D2 gold rules. | Kind-specific manifest constraints. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.14 — held_out suite contract
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The held_out suite contract rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Takes in: ACCEPTED — held_out suite proposal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Does: ACCEPTED — Uses only the future accepted held-out policy, including its judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Kind-specific manifest constraints. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Must never: ACCEPTED — Assume the gold policy for held-out cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No held-out E1 registration while that policy is absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | held_out suite proposal. | Uses only the future accepted held-out policy, including its judgment authority. | Kind-specific manifest constraints. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.2.15 — benchmark_family suite contract
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The benchmark_family suite contract rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Takes in: ACCEPTED — benchmark_family suite proposal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Does: ACCEPTED — Binds the §7B.2 family, declared measurements, per-case scoring bindings and each finding’s §7C category, plus concrete-suite acceptance under NHD-B16EEB-D15. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Kind-specific manifest constraints. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a family label as accepted test content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No benchmark E1 registration without the concrete suite acceptance source. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | benchmark_family suite proposal. | Binds the §7B.2 family, declared measurements, per-case scoring bindings and each finding’s §7C category, plus concrete-suite acceptance under NHD-B16EEB-D15. | Kind-specific manifest constraints. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.3 — benchmark_policy_reference (E2)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — A pointer to an already accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The policy record reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Resolves only accepted policies; it creates no policy itself. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — A policy pointer, or unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent a policy value from a missing or unaccepted record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing or unaccepted policy is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.3.1 — policy record pointer: The Ness-approved policy record; missing or unaccepted is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | The policy record reference. | Resolves only accepted policies; it creates no policy itself. | A policy pointer, or unset. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.3.1 — policy record pointer

### C-GOLD.1.3.3.1 — policy record pointer
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The policy record pointer member of benchmark_policy_reference (E2). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The Ness-approved policy record; missing or unaccepted is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — The Ness-approved policy record; missing or unaccepted is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded policy record pointer member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.3 — benchmark_policy_reference (E2) | The Ness-approved policy record; missing or unaccepted is unset. | The Ness-approved policy record; missing or unaccepted is unset. | The recorded policy record pointer member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4 — required_coverage_profile (E3)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Required cells per family and role/system, including B24 role mapping and policy kinds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The proposed required coverage profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Checks all required families, scopes, named measurements and both bound gold sets before registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — A registered required-coverage profile; no instance is supplied here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Omit any benchmark family, measurement scope, named measurement or either required gold path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Registration refused if any family/scope lacks a cell, any of fourteen measurements lacks a declaring required-cell suite, or either gold set lacks its bound cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.4.1 — required cells: The required coverage cells for each family and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.2 — B24 role mapping: The mapping of cells to analyst, messenger and combined scopes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.3 — required policy kinds: Every policy kind required by this profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.4 — Coverage profile registration gate: Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.4.4 — Coverage profile registration gate: Every required family, scope, named-measurement declaration and bound gold set must be covered before registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | The proposed required coverage profile. | Checks all required families, scopes, named measurements and both bound gold sets before registration. | A registered required-coverage profile; no instance is supplied here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | The proposed required coverage profile. | For this requested record kind, appends the E3 canonical record when its stated commit conditions hold; earlier records remain unchanged. | A registered required-coverage profile; no instance is supplied here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | The proposed required coverage profile. | For the corresponding requested record kind, commits E3 at this boundary only after its stated gates; existing records are not overwritten. | A registered required-coverage profile; no instance is supplied here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.4.1 — required cells; C-GOLD.1.3.4.2 — B24 role mapping; C-GOLD.1.3.4.3 — required policy kinds; C-GOLD.1.3.4.4 — Coverage profile registration gate

### C-GOLD.1.3.4.1 — required cells
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The required cells member of required_coverage_profile (E3). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The required coverage cells for each family and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — The required coverage cells for each family and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded required cells member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | The required coverage cells for each family and role/system. | The required coverage cells for each family and role/system. | The recorded required cells member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.2 — B24 role mapping
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The B24 role mapping member of required_coverage_profile (E3). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The mapping of cells to analyst, messenger and combined scopes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — The mapping of cells to analyst, messenger and combined scopes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded B24 role mapping member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | The mapping of cells to analyst, messenger and combined scopes. | The mapping of cells to analyst, messenger and combined scopes. | The recorded B24 role mapping member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.3 — required policy kinds
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The required policy kinds member of required_coverage_profile (E3). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Every policy kind required by this profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Every policy kind required by this profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded required policy kinds member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | Every policy kind required by this profile. | Every policy kind required by this profile. | The recorded required policy kinds member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.4 — Coverage profile registration gate
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Coverage profile registration gate rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — A candidate E3 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — Registration only with complete declared coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a valid declaration as actual run coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any of the four missing-coverage conditions refuses registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.4.4.1 — Family coverage: Every §7B.2 family has a required cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.4.2 — Scope coverage: Every §7B.3 scope has a required cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.4.3 — Measurement declaration coverage: Every one of the fourteen named measurements is declared by at least one required cell’s suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.4.4 — Gold v1 cell: Gold v1 appears in a cell through its bound path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.4.4.5 — Gold v2-B cell: Gold v2-B appears in a cell through its bound path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | A candidate E3 profile. | Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. | Registration only with complete declared coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | A candidate E3 profile. | Every required family, scope, named-measurement declaration and bound gold set must be covered before registration. | Registration only with complete declared coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | A candidate E3 profile. | Applies this defining record/rule contract: Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. | Registration only with complete declared coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | A candidate E3 profile. | When registering this setup record kind: Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. | Registration only with complete declared coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.4.4.1 — Family coverage; C-GOLD.1.3.4.4.2 — Scope coverage; C-GOLD.1.3.4.4.3 — Measurement declaration coverage; C-GOLD.1.3.4.4.4 — Gold v1 cell; C-GOLD.1.3.4.4.5 — Gold v2-B cell

### C-GOLD.1.3.4.4.1 — Family coverage
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Family coverage rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The E3 required-cell set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Every §7B.2 family has a required cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named registration condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Register E3 when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E3 registration is refused when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | The E3 required-cell set. | Every §7B.2 family has a required cell. | The named registration condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.4.2 — Scope coverage
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Scope coverage rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The E3 required-cell set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Every §7B.3 scope has a required cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named registration condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Register E3 when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E3 registration is refused when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | The E3 required-cell set. | Every §7B.3 scope has a required cell. | The named registration condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.4.3 — Measurement declaration coverage
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Measurement declaration coverage rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The E3 required-cell set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Every one of the fourteen named measurements is declared by at least one required cell’s suite. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named registration condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Register E3 when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E3 registration is refused when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | The E3 required-cell set. | Every one of the fourteen named measurements is declared by at least one required cell’s suite. | The named registration condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.4.4 — Gold v1 cell
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Gold v1 cell rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The E3 required-cell set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Gold v1 appears in a cell through its bound path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named registration condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Register E3 when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E3 registration is refused when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | The E3 required-cell set. | Gold v1 appears in a cell through its bound path. | The named registration condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.4.4.5 — Gold v2-B cell
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Gold v2-B cell rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — The E3 required-cell set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Gold v2-B appears in a cell through its bound path. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named registration condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Register E3 when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E3 registration is refused when this condition is false. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.4.4 — Coverage profile registration gate | The E3 required-cell set. | Gold v2-B appears in a cell through its bound path. | The named registration condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5 — evaluation_run_open (E5)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The run-opening record committed before any trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Takes in: ACCEPTED — Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Does: ACCEPTED — Freezes the run’s exact evidence context before execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One run-opening record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Must never: ACCEPTED — Open with a subset plan or unset required policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A subset of suite cases × trial count is refused; evidentiary opening also requires a complete current epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.5.1 — run ID: The run’s unique identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.2 — class: Evidentiary or exploratory, fixed at open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.3 — scope: The exact one-family scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.4 — profile ref: The evaluated E4 or E4S reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.5 — coverage cell: The exact coverage cell served by this run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.6 — E1 suite kind: The run’s suite kind; it determines scoring even inside another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.7 — governing scoring-rule reference: The governing rule of this E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.8 — frozen epoch ref: The complete epoch frozen at opening. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.9 — recorded execution context: The actual execution context used for B9 classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.10 — runtime/hardware configuration: The runtime and hardware configuration actually used. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.11 — comparability group: The run’s comparability group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.12 — full trial plan: Exactly the complete suite case list × the epoch trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.13 — operator: The run operator; this is not judgment authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.5.14 — opened_at: The run-open timestamp. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.1 — trial_count_policy_ref: No evidentiary run opens or executes with trial_count_policy_ref unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.6 — Planned trial identity and full trial plan: The complete suite case list × epoch trial count must be the trial plan; subset plans are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Freezes the run’s exact evidence context before execution. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Uses the exact E5 cell and full trial plan when matching an actual passed run. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.3 — EB-3 — Run open | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Applies this defining record/rule contract: Freezes the run’s exact evidence context before execution. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.12.1 — CR-1 — Crash before E5 | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Recovery follows this rule: Freezes the run’s exact evidence context before execution. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.2.7.1 — Coverage cell | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Freezes the run’s exact evidence context before execution. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | appends the E5 canonical record when its stated commit conditions hold; earlier records remain unchanged. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.9.3 — EB-3 — Run open | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | For the corresponding requested record kind, commits E5 at this boundary only after its stated gates; existing records are not overwritten. | One run-opening record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.5.1 — run ID; C-GOLD.1.3.5.2 — class; C-GOLD.1.3.5.3 — scope; C-GOLD.1.3.5.4 — profile ref; C-GOLD.1.3.5.5 — coverage cell; C-GOLD.1.3.5.6 — E1 suite kind; C-GOLD.1.3.5.7 — governing scoring-rule reference; C-GOLD.1.3.5.8 — frozen epoch ref; C-GOLD.1.3.5.9 — recorded execution context; C-GOLD.1.3.5.10 — runtime/hardware configuration; C-GOLD.1.3.5.11 — comparability group; C-GOLD.1.3.5.12 — full trial plan; C-GOLD.1.3.5.13 — operator; C-GOLD.1.3.5.14 — opened_at

### C-GOLD.1.3.5.1 — run ID
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The run ID member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The run’s unique identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The run’s unique identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded run ID member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The run’s unique identity. | The run’s unique identity. | The recorded run ID member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.2 — class
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The class member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — Evidentiary or exploratory, fixed at open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — Evidentiary or exploratory, fixed at open. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded class member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | Evidentiary or exploratory, fixed at open. | Evidentiary or exploratory, fixed at open. | The recorded class member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.3 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The exact one-family scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The exact one-family scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The exact one-family scope. | The exact one-family scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.4 — profile ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The profile ref member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The evaluated E4 or E4S reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The evaluated E4 or E4S reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded profile ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The evaluated E4 or E4S reference. | The evaluated E4 or E4S reference. | The recorded profile ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.5 — coverage cell
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The coverage cell member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The exact coverage cell served by this run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The exact coverage cell served by this run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded coverage cell member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The exact coverage cell served by this run. | The exact coverage cell served by this run. | The recorded coverage cell member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.6 — E1 suite kind
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E1 suite kind member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The run’s suite kind; it determines scoring even inside another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The run’s suite kind; it determines scoring even inside another result family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded E1 suite kind member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The run’s suite kind; it determines scoring even inside another result family. | The run’s suite kind; it determines scoring even inside another result family. | The recorded E1 suite kind member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.7 — governing scoring-rule reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The governing scoring-rule reference member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The governing rule of this E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The governing rule of this E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded governing scoring-rule reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The governing rule of this E1 suite kind. | The governing rule of this E1 suite kind. | The recorded governing scoring-rule reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.8 — frozen epoch ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The frozen epoch ref member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The complete epoch frozen at opening. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The complete epoch frozen at opening. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded frozen epoch ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The complete epoch frozen at opening. | The complete epoch frozen at opening. | The recorded frozen epoch ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.9 — recorded execution context
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The recorded execution context member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The actual execution context used for B9 classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The actual execution context used for B9 classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded recorded execution context member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The actual execution context used for B9 classification. | The actual execution context used for B9 classification. | The recorded recorded execution context member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.10 — runtime/hardware configuration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The runtime/hardware configuration member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The runtime and hardware configuration actually used. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The runtime and hardware configuration actually used. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded runtime/hardware configuration member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The runtime and hardware configuration actually used. | The runtime and hardware configuration actually used. | The recorded runtime/hardware configuration member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.11 — comparability group
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The comparability group member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The run’s comparability group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The run’s comparability group. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded comparability group member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The run’s comparability group. | The run’s comparability group. | The recorded comparability group member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.12 — full trial plan
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The full trial plan member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — Exactly the complete suite case list × the epoch trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — Exactly the complete suite case list × the epoch trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded full trial plan member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Open a run on a subset plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E5 is refused unless the plan equals the complete suite case list × trial count. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | Exactly the complete suite case list × the epoch trial count. | Exactly the complete suite case list × the epoch trial count. | The recorded full trial plan member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.13 — operator
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The operator member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The run operator; this is not judgment authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The run operator; this is not judgment authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded operator member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The run operator; this is not judgment authorization. | The run operator; this is not judgment authorization. | The recorded operator member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.5.14 — opened_at
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The opened_at member of evaluation_run_open (E5). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Takes in: ACCEPTED — The run-open timestamp. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Does: ACCEPTED — The run-open timestamp. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Gives out: ACCEPTED — The recorded opened_at member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | The run-open timestamp. | The run-open timestamp. | The recorded opened_at member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6 — trial_attempt_start (E6)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One started attempt of a planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Takes in: ACCEPTED — run, case_id, trial_index, attempt_id and shared output key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Does: ACCEPTED — Records ordinal 1 as original execution; every later attempt binds committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gives out: ACCEPTED — An attempt-start record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Must never: ACCEPTED — Start later attempts without admission, while output existence is unresolved, or after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unadmitted later attempts, unresolved-existence attempts and post-E8 starts are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.6.1 — run: The containing run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.6.2 — case_id: The planned case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.6.3 — trial_index: The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.6.4 — attempt_id: This attempt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.6.5 — planned_trial_output_key: The output key shared by all attempts of this planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.6.6 — B9 R1 admission reference: Required for every ordinal ≥ 2; ordinal 1 has no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Every later attempt requires committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3.6 — No attempt after run terminal: No attempt may start after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | run, case_id, trial_index, attempt_id and shared output key. | Records ordinal 1 as original execution; every later attempt binds committed B9 R1 admission. | An attempt-start record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | run, case_id, trial_index, attempt_id and shared output key. | Applies this defining record/rule contract: Records ordinal 1 as original execution; every later attempt binds committed B9 R1 admission. | An attempt-start record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | run, case_id, trial_index, attempt_id and shared output key. | appends the E6 canonical record when its stated commit conditions hold; earlier records remain unchanged. | An attempt-start record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | run, case_id, trial_index, attempt_id and shared output key. | For the corresponding requested record kind, commits E6 at this boundary only after its stated gates; existing records are not overwritten. | An attempt-start record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.6.1 — run; C-GOLD.1.3.6.2 — case_id; C-GOLD.1.3.6.3 — trial_index; C-GOLD.1.3.6.4 — attempt_id; C-GOLD.1.3.6.5 — planned_trial_output_key; C-GOLD.1.3.6.6 — B9 R1 admission reference

### C-GOLD.1.3.6.1 — run
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The run member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The containing run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The containing run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded run member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | The containing run. | The containing run. | The recorded run member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6.2 — case_id
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The case_id member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The planned case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The planned case identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded case_id member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | The planned case identity. | The planned case identity. | The recorded case_id member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6.3 — trial_index
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The trial_index member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The planned repetition index. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded trial_index member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | The planned repetition index. | The planned repetition index. | The recorded trial_index member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6.4 — attempt_id
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_id member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — This attempt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — This attempt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded attempt_id member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | This attempt’s identity. | This attempt’s identity. | The recorded attempt_id member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6.5 — planned_trial_output_key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The planned_trial_output_key member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — The output key shared by all attempts of this planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — The output key shared by all attempts of this planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded planned_trial_output_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | The output key shared by all attempts of this planned trial. | The output key shared by all attempts of this planned trial. | The recorded planned_trial_output_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.6.6 — B9 R1 admission reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The B9 R1 admission reference member of trial_attempt_start (E6). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Takes in: ACCEPTED — Required for every ordinal ≥ 2; ordinal 1 has no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Does: ACCEPTED — Required for every ordinal ≥ 2; ordinal 1 has no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Gives out: ACCEPTED — The recorded B9 R1 admission reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Start an ordinal ≥ 2 attempt without committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A later E6 without admission is refused as hidden retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | Required for every ordinal ≥ 2; ordinal 1 has no B9 admission. | Required for every ordinal ≥ 2; ordinal 1 has no B9 admission. | The recorded B9 R1 admission reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.7 — trial_attempt_terminal (E7)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Exactly one immutable terminal per attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Attempt identity, terminal outcome and any deterministic findings. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Records completed, failed, interrupted/abandoned or unresolved outcome. Deterministic findings bind the exact accepted checker. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — One E7 terminal; never rewritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Record two terminals for one attempt or accept a different checker’s finding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A mismatched checker makes the finding invalid and the run head indeterminate; unresolved attempts cannot be retried. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.7.1 — terminal outcome: attempt_completed, attempt_failed, attempt_interrupted_abandoned or attempt_unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.7.2 — failure class: For attempt_failed: technical, resource or timeout. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.7.3 — checker binding: Deterministic findings bind the exact configuration identity and version declared by E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Attempt identity, terminal outcome and any deterministic findings. | Records completed, failed, interrupted/abandoned or unresolved outcome. Deterministic findings bind the exact accepted checker. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | Attempt identity, terminal outcome and any deterministic findings. | Applies this defining record/rule contract: Records completed, failed, interrupted/abandoned or unresolved outcome. Deterministic findings bind the exact accepted checker. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed | Attempt identity, terminal outcome and any deterministic findings. | Records this attempt’s single terminal in E7. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed | Attempt identity, terminal outcome and any deterministic findings. | Records this attempt’s single terminal in E7. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned | Attempt identity, terminal outcome and any deterministic findings. | Records this attempt’s single terminal in E7. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved | Attempt identity, terminal outcome and any deterministic findings. | Records this attempt’s single terminal in E7. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | Attempt identity, terminal outcome and any deterministic findings. | appends the E7 canonical record when its stated commit conditions hold; earlier records remain unchanged. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | Attempt identity, terminal outcome and any deterministic findings. | For the corresponding requested record kind, commits E7 at this boundary only after its stated gates; existing records are not overwritten. | One E7 terminal; never rewritten. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.7.1 — terminal outcome; C-GOLD.1.3.7.2 — failure class; C-GOLD.1.3.7.3 — checker binding

### C-GOLD.1.3.7.1 — terminal outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The terminal outcome member of trial_attempt_terminal (E7). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Takes in: ACCEPTED — attempt_completed, attempt_failed, attempt_interrupted_abandoned or attempt_unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Does: ACCEPTED — attempt_completed, attempt_failed, attempt_interrupted_abandoned or attempt_unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Gives out: ACCEPTED — The recorded terminal outcome member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | attempt_completed, attempt_failed, attempt_interrupted_abandoned or attempt_unresolved. | attempt_completed, attempt_failed, attempt_interrupted_abandoned or attempt_unresolved. | The recorded terminal outcome member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.7.2 — failure class
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The failure class member of trial_attempt_terminal (E7). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Takes in: ACCEPTED — For attempt_failed: technical, resource or timeout. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Does: ACCEPTED — For attempt_failed: technical, resource or timeout. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Gives out: ACCEPTED — The recorded failure class member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.7.2.1 — technical attempt failure: Records the technical failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.7.2.2 — resource attempt failure: Records the resource failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.7.2.3 — timeout attempt failure: Records the timeout failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | For attempt_failed: technical, resource or timeout. | For attempt_failed: technical, resource or timeout. | The recorded failure class member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.7.2.1 — technical attempt failure; C-GOLD.1.3.7.2.2 — resource attempt failure; C-GOLD.1.3.7.2.3 — timeout attempt failure

### C-GOLD.1.3.7.2.1 — technical attempt failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The technical attempt failure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — An attempt_failed E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Records the technical failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a failed attempt as a completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An attempt_failed outcome is technical_retryable only under B9 admission; resource failures remain CONSEQUENTIAL findings for the B24 family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The E7 outcome is attempt_failed; its class is recorded without changing the terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7.2 — failure class | An attempt_failed E7. | Records the technical failure class. | The stated failure class. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.7.2.2 — resource attempt failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resource attempt failure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — An attempt_failed E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Records the resource failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a failed attempt as a completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An attempt_failed outcome is technical_retryable only under B9 admission; resource failures remain CONSEQUENTIAL findings for the B24 family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The E7 outcome is attempt_failed; its class is recorded without changing the terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7.2 — failure class | An attempt_failed E7. | Records the resource failure class. | The stated failure class. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.7.2.3 — timeout attempt failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The timeout attempt failure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — An attempt_failed E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Records the timeout failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated failure class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a failed attempt as a completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An attempt_failed outcome is technical_retryable only under B9 admission; resource failures remain CONSEQUENTIAL findings for the B24 family. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The E7 outcome is attempt_failed; its class is recorded without changing the terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7.2 — failure class | An attempt_failed E7. | Records the timeout failure class. | The stated failure class. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.7.3 — checker binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The checker binding member of trial_attempt_terminal (E7). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Takes in: ACCEPTED — Deterministic findings bind the exact configuration identity and version declared by E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Does: ACCEPTED — Deterministic findings bind the exact configuration identity and version declared by E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Gives out: ACCEPTED — The recorded checker binding member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | Deterministic findings bind the exact configuration identity and version declared by E1. | Deterministic findings bind the exact configuration identity and version declared by E1. | The recorded checker binding member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.8 — trial_attempt_resolution (E7r)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — An append-only resolution for an attempt_unresolved terminal only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable lookup evidence for the attempt’s output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Records resolved_output_found, resolved_absence_proven or still_undetermined; preserves E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — A derived effective attempt state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite E7, create a second conclusive result, or retry while existence remains unknown. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory conclusive outcomes make state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.8.1 — resolution outcome: resolved_output_found, resolved_absence_proven or still_undetermined. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.8.2 — resolved output proof: For resolved_output_found: output identity under planned_trial_output_key and verified integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: At most one conclusive resolution exists; contradiction makes effective state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Durable lookup evidence for the attempt’s output. | Records resolved_output_found, resolved_absence_proven or still_undetermined; preserves E7. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | Durable lookup evidence for the attempt’s output. | Applies this defining record/rule contract: Records resolved_output_found, resolved_absence_proven or still_undetermined; preserves E7. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | Durable lookup evidence for the attempt’s output. | The E7r outcome supplies the append-only resolution record; E7 remains unchanged. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | Durable lookup evidence for the attempt’s output. | The E7r outcome supplies the append-only resolution record; E7 remains unchanged. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | Durable lookup evidence for the attempt’s output. | The E7r outcome supplies the append-only resolution record; E7 remains unchanged. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.11.4 — One conclusive resolution per attempt | Durable lookup evidence for the attempt’s output. | A conclusive E7r is permitted only for an unresolved attempt and only once. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | Durable lookup evidence for the attempt’s output. | appends the E7r canonical record when its stated commit conditions hold; earlier records remain unchanged. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | Durable lookup evidence for the attempt’s output. | For the corresponding requested record kind, commits E7r at this boundary only after its stated gates; existing records are not overwritten. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | Durable lookup evidence for the attempt’s output. | Appends this resolution without rewriting E7 or E8. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | Durable lookup evidence for the attempt’s output. | Appends this resolution without rewriting E7 or E8. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | Durable lookup evidence for the attempt’s output. | Appends this resolution without rewriting E7 or E8. | A derived effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.8.1 — resolution outcome; C-GOLD.1.3.8.2 — resolved output proof

### C-GOLD.1.3.8.1 — resolution outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolution outcome member of trial_attempt_resolution (E7r). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Takes in: ACCEPTED — resolved_output_found, resolved_absence_proven or still_undetermined. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Does: ACCEPTED — resolved_output_found, resolved_absence_proven or still_undetermined. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Gives out: ACCEPTED — The recorded resolution outcome member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | resolved_output_found, resolved_absence_proven or still_undetermined. | resolved_output_found, resolved_absence_proven or still_undetermined. | The recorded resolution outcome member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.8.2 — resolved output proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved output proof member of trial_attempt_resolution (E7r). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Takes in: ACCEPTED — For resolved_output_found: output identity under planned_trial_output_key and verified integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Does: ACCEPTED — For resolved_output_found: output identity under planned_trial_output_key and verified integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Gives out: ACCEPTED — The recorded resolved output proof member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | For resolved_output_found: output identity under planned_trial_output_key and verified integrity. | For resolved_output_found: output identity under planned_trial_output_key and verified integrity. | The recorded resolved output proof member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.9 — evaluation_run_terminal (E8)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Exactly one terminal per run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Takes in: ACCEPTED — Every started attempt’s E7 and the run’s B9 live/admission state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Does: ACCEPTED — Closes only when all started attempts have E7 and no attempt is live or admitted-unstarted; freezes the terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Gives out: ACCEPTED — run_completed, run_closed_incomplete or run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Must never: ACCEPTED — Close with a live/admitted-unstarted attempt or start any attempt after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unresolved evidence, integrity failure or contradiction permits only run_indeterminate; incomplete trials cannot yield run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.9.1 — terminal outcome: run_completed, run_closed_incomplete or run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.9.2 — frozen terminal-set digest: Digest of every E6/E7 across every B9 episode, frozen at E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: All started attempts have E7 and none are live or admitted-unstarted; the outcome reflects actual completion evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Every started attempt’s E7 and the run’s B9 live/admission state. | Closes only when all started attempts have E7 and no attempt is live or admitted-unstarted; freezes the terminal-set digest. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.3.1 — O-RUN run_completed | Every started attempt’s E7 and the run’s B9 live/admission state. | Records this run’s single terminal in E8. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete | Every started attempt’s E7 and the run’s B9 live/admission state. | Records this run’s single terminal in E8. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate | Every started attempt’s E7 and the run’s B9 live/admission state. | Records this run’s single terminal in E8. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | Every started attempt’s E7 and the run’s B9 live/admission state. | appends the E8 canonical record when its stated commit conditions hold; earlier records remain unchanged. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.7 — EB-7 — Run terminal | Every started attempt’s E7 and the run’s B9 live/admission state. | For the corresponding requested record kind, commits E8 at this boundary only after its stated gates; existing records are not overwritten. | run_completed, run_closed_incomplete or run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.9.1 — terminal outcome; C-GOLD.1.3.9.2 — frozen terminal-set digest

### C-GOLD.1.3.9.1 — terminal outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The terminal outcome member of evaluation_run_terminal (E8). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Takes in: ACCEPTED — run_completed, run_closed_incomplete or run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Does: ACCEPTED — run_completed, run_closed_incomplete or run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Gives out: ACCEPTED — The recorded terminal outcome member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | run_completed, run_closed_incomplete or run_indeterminate. | run_completed, run_closed_incomplete or run_indeterminate. | The recorded terminal outcome member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.9.2 — frozen terminal-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The frozen terminal-set digest member of evaluation_run_terminal (E8). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Takes in: ACCEPTED — Digest of every E6/E7 across every B9 episode, frozen at E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Does: ACCEPTED — Digest of every E6/E7 across every B9 episode, frozen at E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Gives out: ACCEPTED — The recorded frozen terminal-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | Digest of every E6/E7 across every B9 episode, frozen at E8. | Digest of every E6/E7 across every B9 episode, frozen at E8. | The recorded frozen terminal-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10 — evaluation_judgment (E9)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One authorized link in one effectively completed output’s judgment chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Output identity/integrity, expected head, scoring mode and event-time authority proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — A pass/fail judgment preserving earlier heads. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Treat a typed annotator name or model assistance as authority, reuse a token, or pick a fork winner by recency. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unaccepted NHD-B16EEB-D16 refuses every Ness judgment; stale competing heads are refused; fork or identity contradiction is judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.10.1 — judgment_chain_key: Equals the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.2 — expected_previous_judgment_head: The exact current predecessor, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.3 — output ref: The effectively completed output being judged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.4 — output integrity: Integrity of that exact completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.5 — judgment mode: Must equal E1’s accepted per-case mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.6 — judgment_authority_ref: The event-time proof required by accepted NHD-B16EEB-D16; BAI durable consumption receipt and/or immutable session-state proof, or the declared deterministic checker plus execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.7 — pass / fail: The recorded per-output judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.8 — §7C classification: Only for benchmark_family findings; sealed-gold cases have no §7C category. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.9 — human_annotation provenance: Annotator, when and context_version, in addition to verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.10 — change_reason: Required when superseding a prior judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.11 — model_assist_ref: Optional assistance reference; carries no judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.12 — E9 identity: judgment_chain_key + expected_previous_judgment_head + content digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: Judgment commit requires the expected head still current and CAS-1 satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Output identity/integrity, expected head, scoring mode and event-time authority proof. | Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Output identity/integrity, expected head, scoring mode and event-time authority proof. | Applies this defining record/rule contract: Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.8.2 — Conditional BAI receipt | Output identity/integrity, expected head, scoring mode and event-time authority proof. | Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | Output identity/integrity, expected head, scoring mode and event-time authority proof. | Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | Output identity/integrity, expected head, scoring mode and event-time authority proof. | appends the E9 canonical record when its stated commit conditions hold; earlier records remain unchanged. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Output identity/integrity, expected head, scoring mode and event-time authority proof. | For the corresponding requested record kind, commits E9 at this boundary only after its stated gates; existing records are not overwritten. | A pass/fail judgment preserving earlier heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.10.1 — judgment_chain_key; C-GOLD.1.3.10.2 — expected_previous_judgment_head; C-GOLD.1.3.10.3 — output ref; C-GOLD.1.3.10.4 — output integrity; C-GOLD.1.3.10.5 — judgment mode; C-GOLD.1.3.10.6 — judgment_authority_ref; C-GOLD.1.3.10.7 — pass / fail; C-GOLD.1.3.10.8 — §7C classification; C-GOLD.1.3.10.9 — human_annotation provenance; C-GOLD.1.3.10.10 — change_reason; C-GOLD.1.3.10.11 — model_assist_ref; C-GOLD.1.3.10.12 — E9 identity

### C-GOLD.1.3.10.1 — judgment_chain_key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment_chain_key member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Equals the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Equals the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded judgment_chain_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Equals the output’s planned_trial_output_key. | Equals the output’s planned_trial_output_key. | The recorded judgment_chain_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.2 — expected_previous_judgment_head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The expected_previous_judgment_head member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — The exact current predecessor, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — The exact current predecessor, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded expected_previous_judgment_head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | The exact current predecessor, or none for the first judgment. | The exact current predecessor, or none for the first judgment. | The recorded expected_previous_judgment_head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.3 — output ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The output ref member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — The effectively completed output being judged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — The effectively completed output being judged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded output ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | The effectively completed output being judged. | The effectively completed output being judged. | The recorded output ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.4 — output integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The output integrity member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Integrity of that exact completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Integrity of that exact completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded output integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Integrity of that exact completed output. | Integrity of that exact completed output. | The recorded output integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.5 — judgment mode
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment mode member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Must equal E1’s accepted per-case mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Must equal E1’s accepted per-case mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded judgment mode member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Commit an E9 whose mode differs from the accepted E1 case binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mode mismatch refuses the judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Must equal E1’s accepted per-case mode. | Must equal E1’s accepted per-case mode. | The recorded judgment mode member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.6 — judgment_authority_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment_authority_ref member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — The event-time proof required by accepted NHD-B16EEB-D16; BAI durable consumption receipt and/or immutable session-state proof, or the declared deterministic checker plus execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — The event-time proof required by accepted NHD-B16EEB-D16; BAI durable consumption receipt and/or immutable session-state proof, or the declared deterministic checker plus execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded judgment_authority_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Use model-only authority, a bare name or a proof not required by accepted NHD-B16EEB-D16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing, unverifiable or mismatched proof refuses E9; until NHD-B16EEB-D16 is accepted, all Ness judgments are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.10.6.1 — BAI receipt reference: For the BAI option: durable bai_token_consumed identity, integrity and the claim for which consumption occurred; never mere token presence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.6.2 — SACL event-time reference: For the SACL option: assessment identity, version and commit timestamp proving fresh valid recognized-Ness state at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.6.3 — deterministic checker proof: For deterministic judgment: declared checker identity/configuration/version and its execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | The event-time proof required by accepted NHD-B16EEB-D16; BAI durable consumption receipt and/or immutable session-state proof, or the declared deterministic checker plus execution record. | The event-time proof required by accepted NHD-B16EEB-D16; BAI durable consumption receipt and/or immutable session-state proof, or the declared deterministic checker plus execution record. | The recorded judgment_authority_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.10.6.1 — BAI receipt reference; C-GOLD.1.3.10.6.2 — SACL event-time reference; C-GOLD.1.3.10.6.3 — deterministic checker proof

### C-GOLD.1.3.10.6.1 — BAI receipt reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The BAI receipt reference member of judgment_authority_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — For the BAI option: durable bai_token_consumed identity, integrity and the claim for which consumption occurred; never mere token presence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — For the BAI option: durable bai_token_consumed identity, integrity and the claim for which consumption occurred; never mere token presence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded BAI receipt reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.6 — judgment_authority_ref | For the BAI option: durable bai_token_consumed identity, integrity and the claim for which consumption occurred; never mere token presence. | For the BAI option: durable bai_token_consumed identity, integrity and the claim for which consumption occurred; never mere token presence. | The recorded BAI receipt reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.6.2 — SACL event-time reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The SACL event-time reference member of judgment_authority_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — For the SACL option: assessment identity, version and commit timestamp proving fresh valid recognized-Ness state at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — For the SACL option: assessment identity, version and commit timestamp proving fresh valid recognized-Ness state at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded SACL event-time reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.6 — judgment_authority_ref | For the SACL option: assessment identity, version and commit timestamp proving fresh valid recognized-Ness state at judgment commit. | For the SACL option: assessment identity, version and commit timestamp proving fresh valid recognized-Ness state at judgment commit. | The recorded SACL event-time reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.6.3 — deterministic checker proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The deterministic checker proof member of judgment_authority_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — For deterministic judgment: declared checker identity/configuration/version and its execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — For deterministic judgment: declared checker identity/configuration/version and its execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded deterministic checker proof member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.6 — judgment_authority_ref | For deterministic judgment: declared checker identity/configuration/version and its execution record. | For deterministic judgment: declared checker identity/configuration/version and its execution record. | The recorded deterministic checker proof member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.7 — pass / fail
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The pass / fail member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — The recorded per-output judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — The recorded per-output judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded pass / fail member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | The recorded per-output judgment. | The recorded per-output judgment. | The recorded pass / fail member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.8 — §7C classification
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The §7C classification member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Only for benchmark_family findings; sealed-gold cases have no §7C category. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Only for benchmark_family findings; sealed-gold cases have no §7C category. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded §7C classification member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Attach a §7C category to a sealed-gold case. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A gold run remains governed by gold scoring; B24 tolerance cannot rescue its failure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Only for benchmark_family findings; sealed-gold cases have no §7C category. | Only for benchmark_family findings; sealed-gold cases have no §7C category. | The recorded §7C classification member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.9 — human_annotation provenance
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The human_annotation provenance member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Annotator, when and context_version, in addition to verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Annotator, when and context_version, in addition to verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded human_annotation provenance member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.10.9.1 — annotator: Who supplied the annotation; a bare name supplies no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.9.2 — when: When the annotation was made. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.10.9.3 — context_version: The annotation’s context version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Annotator, when and context_version, in addition to verified authority. | Annotator, when and context_version, in addition to verified authority. | The recorded human_annotation provenance member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.10.9.1 — annotator; C-GOLD.1.3.10.9.2 — when; C-GOLD.1.3.10.9.3 — context_version

### C-GOLD.1.3.10.9.1 — annotator
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The annotator member of human_annotation provenance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Who supplied the annotation; a bare name supplies no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Who supplied the annotation; a bare name supplies no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded annotator member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.9 — human_annotation provenance | Who supplied the annotation; a bare name supplies no authority. | Who supplied the annotation; a bare name supplies no authority. | The recorded annotator member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.9.2 — when
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The when member of human_annotation provenance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — When the annotation was made. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — When the annotation was made. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded when member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.9 — human_annotation provenance | When the annotation was made. | When the annotation was made. | The recorded when member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.9.3 — context_version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The context_version member of human_annotation provenance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — The annotation’s context version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — The annotation’s context version. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded context_version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.9 — human_annotation provenance | The annotation’s context version. | The annotation’s context version. | The recorded context_version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.10 — change_reason
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The change_reason member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Required when superseding a prior judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Required when superseding a prior judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded change_reason member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Supersede a judgment without change_reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Required when superseding a prior judgment. | Required when superseding a prior judgment. | The recorded change_reason member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.11 — model_assist_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The model_assist_ref member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Optional assistance reference; carries no judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Optional assistance reference; carries no judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded model_assist_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the optional assistance reference as judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A model-only authority reference refuses the judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Optional assistance reference; carries no judgment authority. | Optional assistance reference; carries no judgment authority. | The recorded model_assist_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.10.12 — E9 identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E9 identity member of evaluation_judgment (E9). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — judgment_chain_key + expected_previous_judgment_head + content digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — judgment_chain_key + expected_previous_judgment_head + content digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded E9 identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.10.12.1 — content digest: Digest of the exact E9 content; together with judgment_chain_key and expected_previous_judgment_head it forms E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | judgment_chain_key + expected_previous_judgment_head + content digest. | judgment_chain_key + expected_previous_judgment_head + content digest. | The recorded E9 identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.10.12.1 — content digest

### C-GOLD.1.3.10.12.1 — content digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The content digest member of E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Takes in: ACCEPTED — Digest of the exact E9 content; together with judgment_chain_key and expected_previous_judgment_head it forms E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Does: ACCEPTED — Digest of the exact E9 content; together with judgment_chain_key and expected_previous_judgment_head it forms E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Gives out: ACCEPTED — The recorded content digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.10.12 — E9 identity | Digest of the exact E9 content; together with judgment_chain_key and expected_previous_judgment_head it forms E9 identity. | Digest of the exact E9 content; together with judgment_chain_key and expected_previous_judgment_head it forms E9 identity. | The recorded content digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11 — suite_aggregate_result (E10)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The per-run aggregate chained against its expected previous head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Does: ACCEPTED — Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Gives out: ACCEPTED — A per-run aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Must never: ACCEPTED — Use stale/non-current judgment heads, re-grade gold through B24 tolerance or select a fork by recency. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing judgments/measurements make incomplete; unverifiable, forked or contradictory inputs make indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.11.1 — expected_previous_head: The exact aggregate head to supersede, or none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.2 — terminal-set digest: The immutable run terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.3 — E7r digest: The digest of consumed attempt-resolution records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.4 — current judgment-head set: Exactly one current authorized head per meaning-dependent effectively completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.5 — judgment-set digest: The digest of that consumed head set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.6 — suite kind: The run’s own E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.7 — scoring rule applied: The governing scoring rule for that suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.8 — findings: Recorded findings under the bound rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.9 — recorded named-measurement results: Actual measurement results, not merely measurement names. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.10 — coverage: Actual evaluated coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.11.11 — state: passed, failed, incomplete, stale, indeterminate or non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Aggregate commit requires the expected current aggregate head; forks make the run indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | Requires recorded measurement results from a satisfied covering cell’s current aggregate head. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.6] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.2.7.2 — Named measurement satisfaction | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | appends the E10 canonical record when its stated commit conditions hold; earlier records remain unchanged. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.9 — EB-9 — Aggregate | Frozen terminal set, resolutions, current judgment heads, scoring rules and measurements. | For the corresponding requested record kind, commits E10 at this boundary only after its stated gates; existing records are not overwritten. | A per-run aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.11.1 — expected_previous_head; C-GOLD.1.3.11.2 — terminal-set digest; C-GOLD.1.3.11.3 — E7r digest; C-GOLD.1.3.11.4 — current judgment-head set; C-GOLD.1.3.11.5 — judgment-set digest; C-GOLD.1.3.11.6 — suite kind; C-GOLD.1.3.11.7 — scoring rule applied; C-GOLD.1.3.11.8 — findings; C-GOLD.1.3.11.9 — recorded named-measurement results; C-GOLD.1.3.11.10 — coverage; C-GOLD.1.3.11.11 — state

### C-GOLD.1.3.11.1 — expected_previous_head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The expected_previous_head member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The exact aggregate head to supersede, or none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The exact aggregate head to supersede, or none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded expected_previous_head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The exact aggregate head to supersede, or none for the first. | The exact aggregate head to supersede, or none for the first. | The recorded expected_previous_head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.2 — terminal-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The terminal-set digest member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The immutable run terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The immutable run terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded terminal-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The immutable run terminal-set digest. | The immutable run terminal-set digest. | The recorded terminal-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.3 — E7r digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E7r digest member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The digest of consumed attempt-resolution records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The digest of consumed attempt-resolution records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded E7r digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The digest of consumed attempt-resolution records. | The digest of consumed attempt-resolution records. | The recorded E7r digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.4 — current judgment-head set
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The current judgment-head set member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — Exactly one current authorized head per meaning-dependent effectively completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — Exactly one current authorized head per meaning-dependent effectively completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded current judgment-head set member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Exactly one current authorized head per meaning-dependent effectively completed output. | Exactly one current authorized head per meaning-dependent effectively completed output. | The recorded current judgment-head set member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.5 — judgment-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment-set digest member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The digest of that consumed head set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The digest of that consumed head set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded judgment-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The digest of that consumed head set. | The digest of that consumed head set. | The recorded judgment-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.6 — suite kind
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The suite kind member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The run’s own E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The run’s own E1 suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded suite kind member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The run’s own E1 suite kind. | The run’s own E1 suite kind. | The recorded suite kind member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.7 — scoring rule applied
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scoring rule applied member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — The governing scoring rule for that suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — The governing scoring rule for that suite kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded scoring rule applied member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | The governing scoring rule for that suite kind. | The governing scoring rule for that suite kind. | The recorded scoring rule applied member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.8 — findings
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The findings member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — Recorded findings under the bound rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — Recorded findings under the bound rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded findings member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Recorded findings under the bound rule. | Recorded findings under the bound rule. | The recorded findings member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.9 — recorded named-measurement results
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The recorded named-measurement results member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — Actual measurement results, not merely measurement names. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — Actual measurement results, not merely measurement names. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded recorded named-measurement results member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Actual measurement results, not merely measurement names. | Actual measurement results, not merely measurement names. | The recorded recorded named-measurement results member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.10 — coverage
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The coverage member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — Actual evaluated coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — Actual evaluated coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded coverage member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Actual evaluated coverage. | Actual evaluated coverage. | The recorded coverage member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.11.11 — state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The state member of suite_aggregate_result (E10). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Takes in: ACCEPTED — passed, failed, incomplete, stale, indeterminate or non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Does: ACCEPTED — passed, failed, incomplete, stale, indeterminate or non_evidentiary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Gives out: ACCEPTED — The recorded state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | passed, failed, incomplete, stale, indeterminate or non_evidentiary. | passed, failed, incomplete, stale, indeterminate or non_evidentiary. | The recorded state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12 — gold_evidence_result (E11a)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The narrow gold evidence result for B16 input 3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]
- Takes in: ACCEPTED — A complete current gold scope and all relevant records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]
- Does: ACCEPTED — Derives one deterministic result at one ledger head; carries prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]
- Gives out: ACCEPTED — A narrow evidence result, never B24 eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute system eligibility or hide other runs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No usable pass from missing/currentness-failed/incomplete/indeterminate evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.12.1 — scope: The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12.2 — bound ledger head: The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12.3 — evaluated-set digest: The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12.4 — result identity: Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12.5 — prior-scope disclosure: Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12.6 — result state: passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4 — Prior-scope disclosure: Carries mandatory mechanically computed prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: A result is usable for a new check only while its bound head and epoch are current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | A complete current gold scope and all relevant records. | Derives one deterministic result at one ledger head; carries prior-scope disclosure. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | A complete current gold scope and all relevant records. | Input 3 points to the narrow gold result, not system eligibility. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | A complete current gold scope and all relevant records. | For this requested record kind, appends the E11a canonical record when its stated commit conditions hold; earlier records remain unchanged. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.9.10 — EB-10 — Result derivation | A complete current gold scope and all relevant records. | For the corresponding requested record kind, commits E11a at this boundary only after its stated gates; existing records are not overwritten. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.12.1 — scope; C-GOLD.1.3.12.2 — bound ledger head; C-GOLD.1.3.12.3 — evaluated-set digest; C-GOLD.1.3.12.4 — result identity; C-GOLD.1.3.12.5 — prior-scope disclosure; C-GOLD.1.3.12.6 — result state

### C-GOLD.1.3.12.1 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Takes in: ACCEPTED — The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Does: ACCEPTED — The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | The exact family/profile/role/epoch scope. | The exact family/profile/role/epoch scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12.2 — bound ledger head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The bound ledger head member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Takes in: ACCEPTED — The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Does: ACCEPTED — The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Gives out: ACCEPTED — The recorded bound ledger head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | The scope head at derivation. | The scope head at derivation. | The recorded bound ledger head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12.3 — evaluated-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evaluated-set digest member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Takes in: ACCEPTED — The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Does: ACCEPTED — The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Gives out: ACCEPTED — The recorded evaluated-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | The digest of the exact relevant record set evaluated. | The digest of the exact relevant record set evaluated. | The recorded evaluated-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12.4 — result identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result identity member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Takes in: ACCEPTED — Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Does: ACCEPTED — Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Gives out: ACCEPTED — The recorded result identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | Deterministic from scope + bound ledger head + evaluated-set digest. | Deterministic from scope + bound ledger head + evaluated-set digest. | The recorded result identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12.5 — prior-scope disclosure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The prior-scope disclosure member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Takes in: ACCEPTED — Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Does: ACCEPTED — Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Gives out: ACCEPTED — The recorded prior-scope disclosure member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | Every other scope sharing family, model/component identities and role/system, with epoch, head and state. | Every other scope sharing family, model/component identities and role/system, with epoch, head and state. | The recorded prior-scope disclosure member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.12.6 — result state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result state member of gold_evidence_result (E11a). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded result state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. | passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. | The recorded result state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13 — held_out_evidence_result (E11b)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The narrow held-out evidence result for B16 input 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A complete current held-out scope and all relevant records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]
- Does: ACCEPTED — Derives one deterministic result at one ledger head; carries prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]
- Gives out: ACCEPTED — A narrow evidence result, never B24 eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute system eligibility or hide other runs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No usable pass from missing/currentness-failed/incomplete/indeterminate evidence. No E11b can be produced until held-out policy exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.13.1 — scope: The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13.2 — bound ledger head: The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13.3 — evaluated-set digest: The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13.4 — result identity: Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13.5 — prior-scope disclosure: Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13.6 — result state: passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4 — Prior-scope disclosure: Carries mandatory mechanically computed prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: A result is usable for a new check only while its bound head and epoch are current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | A complete current held-out scope and all relevant records. | Derives one deterministic result at one ledger head; carries prior-scope disclosure. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | A complete current held-out scope and all relevant records. | Input 4 points to the narrow held-out result, not system eligibility. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | A complete current held-out scope and all relevant records. | For this requested record kind, appends the E11b canonical record when its stated commit conditions hold; earlier records remain unchanged. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.9.10 — EB-10 — Result derivation | A complete current held-out scope and all relevant records. | For the corresponding requested record kind, commits E11b at this boundary only after its stated gates; existing records are not overwritten. | A narrow evidence result, never B24 eligibility. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.13.1 — scope; C-GOLD.1.3.13.2 — bound ledger head; C-GOLD.1.3.13.3 — evaluated-set digest; C-GOLD.1.3.13.4 — result identity; C-GOLD.1.3.13.5 — prior-scope disclosure; C-GOLD.1.3.13.6 — result state

### C-GOLD.1.3.13.1 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Takes in: ACCEPTED — The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Does: ACCEPTED — The exact family/profile/role/epoch scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | The exact family/profile/role/epoch scope. | The exact family/profile/role/epoch scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13.2 — bound ledger head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The bound ledger head member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Takes in: ACCEPTED — The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Does: ACCEPTED — The scope head at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Gives out: ACCEPTED — The recorded bound ledger head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | The scope head at derivation. | The scope head at derivation. | The recorded bound ledger head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13.3 — evaluated-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evaluated-set digest member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Takes in: ACCEPTED — The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Does: ACCEPTED — The digest of the exact relevant record set evaluated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Gives out: ACCEPTED — The recorded evaluated-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | The digest of the exact relevant record set evaluated. | The digest of the exact relevant record set evaluated. | The recorded evaluated-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13.4 — result identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result identity member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Takes in: ACCEPTED — Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Does: ACCEPTED — Deterministic from scope + bound ledger head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Gives out: ACCEPTED — The recorded result identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | Deterministic from scope + bound ledger head + evaluated-set digest. | Deterministic from scope + bound ledger head + evaluated-set digest. | The recorded result identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13.5 — prior-scope disclosure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The prior-scope disclosure member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Takes in: ACCEPTED — Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Does: ACCEPTED — Every other scope sharing family, model/component identities and role/system, with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Gives out: ACCEPTED — The recorded prior-scope disclosure member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | Every other scope sharing family, model/component identities and role/system, with epoch, head and state. | Every other scope sharing family, model/component identities and role/system, with epoch, head and state. | The recorded prior-scope disclosure member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.13.6 — result state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result state member of held_out_evidence_result (E11b). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded result state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. | passed, failed, incomplete or indeterminate under the applicable narrow-evidence rule; ledger-head and epoch currentness are separately required. | The recorded result state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14 — b24_system_eligibility_result (E12)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — System-level B24 eligibility, separate from the narrow B16 inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The E4S scope, complete B24 epoch and all actual cells and measurements. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — Reports system eligibility only when every required condition holds; reports every measurement including M-C4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — eligible, not_eligible, incomplete, stale or indeterminate, with named reasons. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Point E13 at E12, equate eligibility with adoption, or re-grade gold component heads using B24 tolerance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No concrete accepted benchmark suite means no eligible E12; zero runs or unsatisfied coverage gives incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.14.1 — scope: The exact E4S system scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.2 — bound ledger head: The scope head bound at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.3 — evaluated-set digest: The exact relevant-record-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.4 — result identity: Deterministic from scope + bound head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.5 — prior-scope disclosure: Other matching-family/model-component/role scopes, each with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.6 — measurement results: Every named measurement result including M-C4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.7 — eligibility state: eligible, not_eligible, incomplete, stale or indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.14.8 — named reasons: The named reasons for any result that is not eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4 — Prior-scope disclosure: Carries mandatory mechanically computed prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: A result is usable for a new check only while its bound head and epoch are current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | The E4S scope, complete B24 epoch and all actual cells and measurements. | Reports system eligibility only when every required condition holds; reports every measurement including M-C4. | eligible, not_eligible, incomplete, stale or indeterminate, with named reasons. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | The E4S scope, complete B24 epoch and all actual cells and measurements. | For this requested record kind, appends the E12 canonical record when its stated commit conditions hold; earlier records remain unchanged. | eligible, not_eligible, incomplete, stale or indeterminate, with named reasons. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.10 — EB-10 — Result derivation | The E4S scope, complete B24 epoch and all actual cells and measurements. | For the corresponding requested record kind, commits E12 at this boundary only after its stated gates; existing records are not overwritten. | eligible, not_eligible, incomplete, stale or indeterminate, with named reasons. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.14.1 — scope; C-GOLD.1.3.14.2 — bound ledger head; C-GOLD.1.3.14.3 — evaluated-set digest; C-GOLD.1.3.14.4 — result identity; C-GOLD.1.3.14.5 — prior-scope disclosure; C-GOLD.1.3.14.6 — measurement results; C-GOLD.1.3.14.7 — eligibility state; C-GOLD.1.3.14.8 — named reasons

### C-GOLD.1.3.14.1 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The exact E4S system scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The exact E4S system scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | The exact E4S system scope. | The exact E4S system scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.2 — bound ledger head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The bound ledger head member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The scope head bound at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The scope head bound at derivation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded bound ledger head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | The scope head bound at derivation. | The scope head bound at derivation. | The recorded bound ledger head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.3 — evaluated-set digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evaluated-set digest member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The exact relevant-record-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The exact relevant-record-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded evaluated-set digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | The exact relevant-record-set digest. | The exact relevant-record-set digest. | The recorded evaluated-set digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.4 — result identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result identity member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — Deterministic from scope + bound head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — Deterministic from scope + bound head + evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded result identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | Deterministic from scope + bound head + evaluated-set digest. | Deterministic from scope + bound head + evaluated-set digest. | The recorded result identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.5 — prior-scope disclosure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The prior-scope disclosure member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — Other matching-family/model-component/role scopes, each with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — Other matching-family/model-component/role scopes, each with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded prior-scope disclosure member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | Other matching-family/model-component/role scopes, each with epoch, head and state. | Other matching-family/model-component/role scopes, each with epoch, head and state. | The recorded prior-scope disclosure member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.6 — measurement results
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The measurement results member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — Every named measurement result including M-C4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — Every named measurement result including M-C4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded measurement results member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | Every named measurement result including M-C4. | Every named measurement result including M-C4. | The recorded measurement results member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.7 — eligibility state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The eligibility state member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — eligible, not_eligible, incomplete, stale or indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — eligible, not_eligible, incomplete, stale or indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded eligibility state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | eligible, not_eligible, incomplete, stale or indeterminate. | eligible, not_eligible, incomplete, stale or indeterminate. | The recorded eligibility state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.14.8 — named reasons
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The named reasons member of b24_system_eligibility_result (E12). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The named reasons for any result that is not eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The named reasons for any result that is not eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded named reasons member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | The named reasons for any result that is not eligible. | The named reasons for any result that is not eligible. | The recorded named reasons member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The narrow evidence pointer verified by B16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Takes in: ACCEPTED — Evidence kind, result identity/integrity, scope and bound ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Does: ACCEPTED — Points only to E11a for input 3 or E11b for input 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Does: ACCEPTED — Gold evidence remains E11a, separate from E12 system eligibility. [SOURCE CONFLICT: 04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3 retains “the recorded B24-architecture acceptance evidence for the applicable gold-set run”; the original wording remains preserved and unedited.] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Gives out: ACCEPTED — A B16-verifiable pointer. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Must never: ACCEPTED — Point at E12 or use a non-current result for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Non-current evidence is unusable for a new B16 check; wrong-kind or invalid pointers cannot pass. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.15.1 — evidence_kind: Gold or held-out kind matching B16 input 3 or 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.15.2 — result_ref: E11a or E11b only, never E12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.15.3 — result integrity: Integrity of the referenced result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.15.4 — scope: The exact referenced result’s scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.15.5 — bound ledger head: The head bound by the result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.12 — gold_evidence_result (E11a): Input 3 points to the narrow gold result, not system eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.13 — held_out_evidence_result (E11b): Input 4 points to the narrow held-out result, not system eligibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: A result is usable for a new check only while its bound head and epoch are current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: ACCEPTED — C-READ.11.7.3 — Gold-set results evidence reference: Supplies the gold-result reference for the existing B16 input-3 verification; no promotion decision moves into the bridge. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Changes: ACCEPTED — C-READ.11.7.4 — Held-out set results evidence reference: Supplies the separately required held-out-result reference for existing B16 input-4 verification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Evidence kind, result identity/integrity, scope and bound ledger head. | Points only to E11a for input 3 or E11b for input 4. | A B16-verifiable pointer. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.11 — EB-11 — Evidence reference | Evidence kind, result identity/integrity, scope and bound ledger head. | Applies this defining record/rule contract: Points only to E11a for input 3 or E11b for input 4. | A B16-verifiable pointer. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.9 — O-EVREF | Evidence kind, result identity/integrity, scope and bound ledger head. | Points only to E11a for input 3 or E11b for input 4. | A B16-verifiable pointer. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.9 — O-EVREF | Evidence kind, result identity/integrity, scope and bound ledger head. | appends the E13 canonical record when its stated commit conditions hold; earlier records remain unchanged. | A B16-verifiable pointer. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.11 — EB-11 — Evidence reference | Evidence kind, result identity/integrity, scope and bound ledger head. | For the corresponding requested record kind, commits E13 at this boundary only after its stated gates; existing records are not overwritten. | A B16-verifiable pointer. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.15.1 — evidence_kind; C-GOLD.1.3.15.2 — result_ref; C-GOLD.1.3.15.3 — result integrity; C-GOLD.1.3.15.4 — scope; C-GOLD.1.3.15.5 — bound ledger head

### C-GOLD.1.3.15.1 — evidence_kind
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The evidence_kind member of promotion_evaluation_evidence_ref (E13). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Takes in: ACCEPTED — Gold or held-out kind matching B16 input 3 or 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Does: ACCEPTED — Gold or held-out kind matching B16 input 3 or 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Gives out: ACCEPTED — The recorded evidence_kind member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | Gold or held-out kind matching B16 input 3 or 4. | Gold or held-out kind matching B16 input 3 or 4. | The recorded evidence_kind member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.15.2 — result_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result_ref member of promotion_evaluation_evidence_ref (E13). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Takes in: ACCEPTED — E11a or E11b only, never E12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Does: ACCEPTED — E11a or E11b only, never E12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Gives out: ACCEPTED — The recorded result_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Point E13 at E12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A pointer not targeting the required E11a/E11b cannot pass AP-1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | E11a or E11b only, never E12. | E11a or E11b only, never E12. | The recorded result_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.15.3 — result integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The result integrity member of promotion_evaluation_evidence_ref (E13). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Takes in: ACCEPTED — Integrity of the referenced result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Does: ACCEPTED — Integrity of the referenced result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Gives out: ACCEPTED — The recorded result integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | Integrity of the referenced result. | Integrity of the referenced result. | The recorded result integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.15.4 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of promotion_evaluation_evidence_ref (E13). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Takes in: ACCEPTED — The exact referenced result’s scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Does: ACCEPTED — The exact referenced result’s scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | The exact referenced result’s scope. | The exact referenced result’s scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.15.5 — bound ledger head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The bound ledger head member of promotion_evaluation_evidence_ref (E13). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Takes in: ACCEPTED — The head bound by the result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Does: ACCEPTED — The head bound by the result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Gives out: ACCEPTED — The recorded bound ledger head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Use a stale bound head for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Head mismatch makes evidence not_available. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | The head bound by the result. | The head bound by the result. | The recorded bound ledger head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.16 — evaluation_invalidity_record (E14)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — An objective-policy exclusion of a run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Takes in: ACCEPTED — Accepted objective invalidity rule and recorded objective facts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Does: ACCEPTED — Excludes only under that accepted rule; no such rule currently exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Gives out: ACCEPTED — An explicit run exclusion if authorized by that rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Must never: ACCEPTED — Exclude an adverse run because another run passed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without an accepted objective rule exclusion is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.16.1 — excluded run: Identity of the run to exclude. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.16.2 — objective invalidity rule: The accepted rule authorizing exclusion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.16.3 — objective facts: Recorded facts supporting that rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Accepted objective invalidity rule and recorded objective facts. | Excludes only under that accepted rule; no such rule currently exists. | An explicit run exclusion if authorized by that rule. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | Accepted objective invalidity rule and recorded objective facts. | Applies this defining record/rule contract: Excludes only under that accepted rule; no such rule currently exists. | An explicit run exclusion if authorized by that rule. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.10 — O-INVALIDITY | Accepted objective invalidity rule and recorded objective facts. | Excludes only under that accepted rule; no such rule currently exists. | An explicit run exclusion if authorized by that rule. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.10 — O-INVALIDITY | Accepted objective invalidity rule and recorded objective facts. | appends the E14 canonical record when its stated commit conditions hold; earlier records remain unchanged. | An explicit run exclusion if authorized by that rule. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | Accepted objective invalidity rule and recorded objective facts. | For the corresponding requested record kind, commits E14 at this boundary only after its stated gates; existing records are not overwritten. | An explicit run exclusion if authorized by that rule. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.16.1 — excluded run; C-GOLD.1.3.16.2 — objective invalidity rule; C-GOLD.1.3.16.3 — objective facts

### C-GOLD.1.3.16.1 — excluded run
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The excluded run member of evaluation_invalidity_record (E14). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Takes in: ACCEPTED — Identity of the run to exclude. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Does: ACCEPTED — Identity of the run to exclude. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Gives out: ACCEPTED — The recorded excluded run member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | Identity of the run to exclude. | Identity of the run to exclude. | The recorded excluded run member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.16.2 — objective invalidity rule
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The objective invalidity rule member of evaluation_invalidity_record (E14). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Takes in: ACCEPTED — The accepted rule authorizing exclusion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Does: ACCEPTED — The accepted rule authorizing exclusion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Gives out: ACCEPTED — The recorded objective invalidity rule member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | The accepted rule authorizing exclusion. | The accepted rule authorizing exclusion. | The recorded objective invalidity rule member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.16.3 — objective facts
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The objective facts member of evaluation_invalidity_record (E14). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Takes in: ACCEPTED — Recorded facts supporting that rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Does: ACCEPTED — Recorded facts supporting that rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Gives out: ACCEPTED — The recorded objective facts member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | Recorded facts supporting that rule. | Recorded facts supporting that rule. | The recorded objective facts member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.17 — evaluation_conflict_resolution (E15)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Policy-bound resolution among completed judged runs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Takes in: ACCEPTED — An accepted disagreement policy and every affected run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Does: ACCEPTED — Resolves only within the accepted policy’s scope, binding every affected run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Gives out: ACCEPTED — An explicit conflict resolution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Must never: ACCEPTED — Use completed-run disagreement policy to resolve judgment-chain forks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without accepted policy, failed or indeterminate heads retain their blocking effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.17.1 — accepted disagreement policy: The accepted completed-run disagreement rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.17.2 — affected-run set: Every run affected by the resolution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | An accepted disagreement policy and every affected run. | Resolves only within the accepted policy’s scope, binding every affected run. | An explicit conflict resolution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | An accepted disagreement policy and every affected run. | Conflict resolution requires the accepted completed-run disagreement policy and every affected run. | An explicit conflict resolution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.11 — O-CONFLICT | An accepted disagreement policy and every affected run. | Resolves only within the accepted policy’s scope, binding every affected run. | An explicit conflict resolution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.11 — O-CONFLICT | An accepted disagreement policy and every affected run. | appends the E15 canonical record when its stated commit conditions hold; earlier records remain unchanged. | An explicit conflict resolution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | An accepted disagreement policy and every affected run. | For the corresponding requested record kind, commits E15 at this boundary only after its stated gates; existing records are not overwritten. | An explicit conflict resolution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.17.1 — accepted disagreement policy; C-GOLD.1.3.17.2 — affected-run set

### C-GOLD.1.3.17.1 — accepted disagreement policy
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The accepted disagreement policy member of evaluation_conflict_resolution (E15). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Takes in: ACCEPTED — The accepted completed-run disagreement rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Does: ACCEPTED — The accepted completed-run disagreement rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Gives out: ACCEPTED — The recorded accepted disagreement policy member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Use this policy to resolve judgment forks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without an accepted disagreement policy, failed/indeterminate heads retain their blocking effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | The accepted completed-run disagreement rule. | The accepted completed-run disagreement rule. | The recorded accepted disagreement policy member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.17.2 — affected-run set
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The affected-run set member of evaluation_conflict_resolution (E15). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Takes in: ACCEPTED — Every run affected by the resolution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Does: ACCEPTED — Every run affected by the resolution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Gives out: ACCEPTED — The recorded affected-run set member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | Every run affected by the resolution. | Every run affected by the resolution. | The recorded affected-run set member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One immutable position in the scope ledger. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — scope, sequence_number, record_ref, record_integrity and previous_entry_digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Commits together with exactly one scope-relevant canonical record by compare-and-append. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — One unique ledger position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the record without its ledger entry or share a sequence position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A lost head race commits nothing; contradictory records cannot establish valid currentness. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.18.1 — scope: The one ledger scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.18.2 — sequence_number: The unique sequence number; the next accepted entry uses n+1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.18.3 — record_ref: The committed relevant canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.18.4 — record_integrity: Integrity of that referenced record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.18.5 — previous_entry_digest: The expected prior entry digest d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | scope, sequence_number, record_ref, record_integrity and previous_entry_digest. | Commits together with exactly one scope-relevant canonical record by compare-and-append. | One unique ledger position. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | scope, sequence_number, record_ref, record_integrity and previous_entry_digest. | Commits one E16 atomically with the requested relevant record; the ledger advances only on the successful comparison. | One unique ledger position. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | scope, sequence_number, record_ref, record_integrity and previous_entry_digest. | The winning entry receives n+1 and previous_entry_digest=d together with its canonical record. | One unique ledger position. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.3.18.1 — scope; C-GOLD.1.3.18.2 — sequence_number; C-GOLD.1.3.18.3 — record_ref; C-GOLD.1.3.18.4 — record_integrity; C-GOLD.1.3.18.5 — previous_entry_digest

### C-GOLD.1.3.18.1 — scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope member of evaluation_scope_ledger_entry (E16). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The one ledger scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The one ledger scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | The one ledger scope. | The one ledger scope. | The recorded scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.18.2 — sequence_number
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The sequence_number member of evaluation_scope_ledger_entry (E16). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The unique sequence number; the next accepted entry uses n+1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The unique sequence number; the next accepted entry uses n+1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded sequence_number member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | The unique sequence number; the next accepted entry uses n+1. | The unique sequence number; the next accepted entry uses n+1. | The recorded sequence_number member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.18.3 — record_ref
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The record_ref member of evaluation_scope_ledger_entry (E16). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The committed relevant canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The committed relevant canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded record_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | The committed relevant canonical record. | The committed relevant canonical record. | The recorded record_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.18.4 — record_integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The record_integrity member of evaluation_scope_ledger_entry (E16). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — Integrity of that referenced record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — Integrity of that referenced record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded record_integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | Integrity of that referenced record. | Integrity of that referenced record. | The recorded record_integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.18.5 — previous_entry_digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The previous_entry_digest member of evaluation_scope_ledger_entry (E16). [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Takes in: ACCEPTED — The expected prior entry digest d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Does: ACCEPTED — The expected prior entry digest d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Gives out: ACCEPTED — The recorded previous_entry_digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9]
- Must never: ACCEPTED — Rewrite this member of the immutable canonical record; corrections are new linked records, with the original preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the containing canonical record is unreadable, downstream state is indeterminate; no separate per-field refusal mechanism is specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: The canonical record remains append-only and immutable; corrections are new linked records and no gold/root/reading text is copied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | The expected prior entry digest d. | The expected prior entry digest d. | The recorded previous_entry_digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.3.19 — Evaluation privacy and access
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Evaluation privacy and access rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Takes in: ACCEPTED — Evaluation records, ledgers and logs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Does: ACCEPTED — Applies §7Q before §7R and SACL where applicable; uses identities and integrity references only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gives out: ACCEPTED — Authorized record access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass privacy or copy protected source text into evaluation records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Access failure is unauthorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Applies privacy and access authorization before relevance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-SACL — Speaker Access-Control Layer (§25.4): Applies speaker/access scope wherever relevant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Evaluation records, ledgers and logs. | Applies §7Q before §7R and SACL where applicable; uses identities and integrity references only. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.2.1 — model_evaluation_profile (E4) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.2.2 — system_candidate_profile (E4S) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.2.3 — policy_epoch (E2e) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.3 — Canonical evaluation record family | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.3.1 — Canonical record preservation | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.3.3 — benchmark_policy_reference (E2) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.3.4 — required_coverage_profile (E3) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.3.5 — evaluation_run_open (E5) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 16 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 17 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 18 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 19 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 20 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 21 · ACCEPTED | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 22 · ACCEPTED | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 23 · ACCEPTED | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 24 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 25 · ACCEPTED | C-GOLD.1.4.1 — Scope-relevant atomic append | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 26 · ACCEPTED | C-GOLD.1.4.2 — Scope ledger head | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 27 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 28 · ACCEPTED | C-GOLD.1.5.1 — Canonical records and operation-owned logs | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| 29 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | Evaluation records, ledgers and logs. | §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. | Authorized record access. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4 — Scope ledger and currentness
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The append-only currentness boundary for one evidence scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]
- Takes in: ACCEPTED — Scope-relevant canonical records and the current ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]
- Does: ACCEPTED — Advances one authoritative scope ledger with every relevant record; results bind the exact head and evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]
- Gives out: ACCEPTED — Current result identity without rewriting earlier results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a stale head as current or retroactively undo committed promotion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An E13 pointing to a non-current result is unusable for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.4.1 — Scope-relevant atomic append: Commits the record and E16 together through one O-APPEND against the exact previous head and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: Identifies the exact current ledger position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: Counts as current only when its bound head equals the ledger’s current head and its epoch is current; later relevant records stale earlier results for new checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4 — Prior-scope disclosure: Mechanically includes every such scope with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.5 — Committed promotion remains absorbing: Affects new evidence checks only; never retroactively undoes the committed promotion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | Scope-relevant canonical records and the current ledger head. | Advances one authoritative scope ledger with every relevant record; results bind the exact head and evaluated-set digest. | Current result identity without rewriting earlier results. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.4.1 — Scope-relevant atomic append; C-GOLD.1.4.2 — Scope ledger head; C-GOLD.1.4.3 — Authoritative current result; C-GOLD.1.4.4 — Prior-scope disclosure; C-GOLD.1.4.5 — Committed promotion remains absorbing

### C-GOLD.1.4.1 — Scope-relevant atomic append
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Scope-relevant atomic append rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Every evidentiary E5, E6, E7, E7r, E8, E9, E10 and every E14/E15 naming that scope’s runs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Does: ACCEPTED — Commits the record and E16 together through one O-APPEND against the exact previous head and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Gives out: ACCEPTED — One appended record plus one ledger entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Must never: ACCEPTED — Append result records E11a/E11b/E12/E13 or exploratory runs to this scope ledger. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Lost comparison commits neither record nor entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — On a lost CAS-1 head race, no record or entry commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The record and E16 append together only against the exact current ledger head and domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: The successful record-plus-entry commit advances the current head to the new sequence number and digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | Every evidentiary E5, E6, E7, E7r, E8, E9, E10 and every E14/E15 naming that scope’s runs. | Commits the record and E16 together through one O-APPEND against the exact previous head and the record’s domain precondition. | One appended record plus one ledger entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.2 — Scope ledger head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The latest sequence number and latest entry digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The scope’s append-only ledger. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Does: ACCEPTED — Identifies the exact current ledger position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Gives out: ACCEPTED — latest sequence_number and latest entry digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Must never: ACCEPTED — Use an earlier head as current for a new evidence check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A result bound to a different current head is unusable for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.4.2.1 — latest sequence_number: The latest ledger sequence number. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.2.2 — latest entry digest: The digest of that latest entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — Currentness compares the exact latest sequence_number and entry digest, not an earlier head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | The scope’s append-only ledger. | Identifies the exact current ledger position. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.4.3 — Authoritative current result | The scope’s append-only ledger. | The result’s bound head must equal this current ledger head. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.4.1 — Scope-relevant atomic append | The scope’s append-only ledger. | The successful record-plus-entry commit advances the current head to the new sequence number and digest. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | The scope’s append-only ledger. | Its E7r ledger append advances the scope head; previous results are no longer current. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.11.1.4 — resolved_output_found Ledger consequence | The scope’s append-only ledger. | The E7r append advances the ledger head. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | The scope’s append-only ledger. | Its E7r ledger append advances the scope head; previous results are no longer current. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.11.2.4 — resolved_absence_proven Ledger consequence | The scope’s append-only ledger. | The E7r append advances the ledger head. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | The scope’s append-only ledger. | Its E7r ledger append advances the scope head; previous results are no longer current. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.5.11.3.4 — still_undetermined Ledger consequence | The scope’s append-only ledger. | The E7r append advances the ledger head. | latest sequence_number and latest entry digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.4.2.1 — latest sequence_number; C-GOLD.1.4.2.2 — latest entry digest

### C-GOLD.1.4.2.1 — latest sequence_number
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The latest sequence_number member of Scope ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The latest ledger sequence number. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Does: ACCEPTED — The latest ledger sequence number. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded latest sequence_number member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Must never: ACCEPTED — Use an earlier head as current for a new evidence check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A result bound to a different current head is unusable for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Currentness compares the exact latest sequence_number and entry digest, not an earlier head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.2 — Scope ledger head | The latest ledger sequence number. | The latest ledger sequence number. | The recorded latest sequence_number member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.2.2 — latest entry digest
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The latest entry digest member of Scope ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The digest of that latest entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Does: ACCEPTED — The digest of that latest entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded latest entry digest member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB]
- Must never: ACCEPTED — Use an earlier head as current for a new evidence check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A result bound to a different current head is unusable for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Currentness compares the exact latest sequence_number and entry digest, not an earlier head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.2 — Scope ledger head | The digest of that latest entry. | The digest of that latest entry. | The recorded latest entry digest member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.3 — Authoritative current result
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authoritative current result rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Takes in: ACCEPTED — A result’s bound head, evaluated-set digest and epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Does: ACCEPTED — Counts as current only when its bound head equals the ledger’s current head and its epoch is current; later relevant records stale earlier results for new checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gives out: ACCEPTED — Current or not-current result, with earlier records preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Must never: ACCEPTED — Edit an earlier result or use its stale E13 for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Head mismatch or non-current epoch makes the reference unusable for a new check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: The result’s bound head must equal this current ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): The result’s epoch must still be current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | A result’s bound head, evaluated-set digest and epoch. | Counts as current only when its bound head equals the ledger’s current head and its epoch is current; later relevant records stale earlier results for new checks. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | A result’s bound head, evaluated-set digest and epoch. | A result is usable for a new check only while its bound head and epoch are current. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | A result’s bound head, evaluated-set digest and epoch. | A result is usable for a new check only while its bound head and epoch are current. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | A result’s bound head, evaluated-set digest and epoch. | A result is usable for a new check only while its bound head and epoch are current. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | A result’s bound head, evaluated-set digest and epoch. | A result is usable for a new check only while its bound head and epoch are current. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.12.20 — CR-20 — Later E9 / E7r / E10 / E14 / E15 | A result’s bound head, evaluated-set digest and epoch. | Recovery follows this rule: Counts as current only when its bound head equals the ledger’s current head and its epoch is current; later relevant records stale earlier results for new checks. | Current or not-current result, with earlier records preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.4 — Prior-scope disclosure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Prior-scope disclosure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Takes in: ACCEPTED — All other scopes sharing family, model identity or component identities, and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Does: ACCEPTED — Mechanically includes every such scope with epoch, head and state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gives out: ACCEPTED — Mandatory prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Must never: ACCEPTED — Automatically block a genuinely different profile/epoch merely because prior scopes exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.4.4.1 — other matching scope: Every other scope sharing the stated family, identities and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4.2 — other scope epoch: That scope’s epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4.3 — other scope head: That scope’s ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.4.4.4 — other scope state: That scope’s result state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gated by: ACCEPTED — Disclosure includes every other scope sharing family, model/component identity and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | All other scopes sharing family, model identity or component identities, and role/system. | Mechanically includes every such scope with epoch, head and state. | Mandatory prior-scope disclosure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | All other scopes sharing family, model identity or component identities, and role/system. | Carries mandatory mechanically computed prior-scope disclosure. | Mandatory prior-scope disclosure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | All other scopes sharing family, model identity or component identities, and role/system. | Carries mandatory mechanically computed prior-scope disclosure. | Mandatory prior-scope disclosure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | All other scopes sharing family, model identity or component identities, and role/system. | Carries mandatory mechanically computed prior-scope disclosure. | Mandatory prior-scope disclosure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.4.4.1 — other matching scope; C-GOLD.1.4.4.2 — other scope epoch; C-GOLD.1.4.4.3 — other scope head; C-GOLD.1.4.4.4 — other scope state

### C-GOLD.1.4.4.1 — other matching scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The other matching scope member of Prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Takes in: ACCEPTED — Every other scope sharing the stated family, identities and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Does: ACCEPTED — Every other scope sharing the stated family, identities and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded other matching scope member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Must never: ACCEPTED — Omit a matching prior scope or automatically block a genuinely different profile/epoch merely because prior scopes exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Disclosure includes every other scope sharing family, model/component identity and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.4 — Prior-scope disclosure | Every other scope sharing the stated family, identities and role/system. | Every other scope sharing the stated family, identities and role/system. | The recorded other matching scope member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.4.2 — other scope epoch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The other scope epoch member of Prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Takes in: ACCEPTED — That scope’s epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Does: ACCEPTED — That scope’s epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded other scope epoch member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Must never: ACCEPTED — Omit a matching prior scope or automatically block a genuinely different profile/epoch merely because prior scopes exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Disclosure includes every other scope sharing family, model/component identity and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.4 — Prior-scope disclosure | That scope’s epoch. | That scope’s epoch. | The recorded other scope epoch member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.4.3 — other scope head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The other scope head member of Prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Takes in: ACCEPTED — That scope’s ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Does: ACCEPTED — That scope’s ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded other scope head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Must never: ACCEPTED — Omit a matching prior scope or automatically block a genuinely different profile/epoch merely because prior scopes exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Disclosure includes every other scope sharing family, model/component identity and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.4 — Prior-scope disclosure | That scope’s ledger head. | That scope’s ledger head. | The recorded other scope head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.4.4 — other scope state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The other scope state member of Prior-scope disclosure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Takes in: ACCEPTED — That scope’s result state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Does: ACCEPTED — That scope’s result state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded other scope state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Must never: ACCEPTED — Omit a matching prior scope or automatically block a genuinely different profile/epoch merely because prior scopes exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Disclosure includes every other scope sharing family, model/component identity and role/system. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4.4 — Prior-scope disclosure | That scope’s result state. | That scope’s result state. | The recorded other scope state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.4.5 — Committed promotion remains absorbing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Committed promotion remains absorbing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Takes in: ACCEPTED — Later changes to evaluation evidence after promotion_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Does: ACCEPTED — Affects new evidence checks only; never retroactively undoes the committed promotion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The prior committed promotion remains unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Must never: ACCEPTED — Uncommit a reading because evaluation evidence later changes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: The existing promotion_committed state remains absorbing; evidence changes affect new checks only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.4 — Scope ledger and currentness | Later changes to evaluation evidence after promotion_committed. | Affects new evidence checks only; never retroactively undoes the committed promotion. | The prior committed promotion remains unchanged. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-e BEHAVIOR -->

## Continuation and reciprocal entries

These entries are recorded in this piece. Every passed chapter remains unchanged. A rule in the other new piece is named by its exact card; its USED BY row appears in that piece.

| Existing owner / endpoint | New counterpart | Relation | Behavior | Source |
|---|---|---|---|---|
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | C-GOLD.1 — Promotion evaluation-evidence bridge | ACCEPTED — reciprocal USED BY entry for Fed by | C-GOLD supplies sealed-gold examination and gold-run logging; the bridge extends that owner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] |
| C-READ.11.7.3 — Gold-set results evidence reference | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — reciprocal USED BY entry for Changes | Supplies the gold-result reference for the existing B16 input-3 verification; no promotion decision moves into the bridge. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-READ.11.7.4 — Held-out set results evidence reference | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — reciprocal USED BY entry for Changes | Supplies the separately required held-out-result reference for existing B16 input-4 verification. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-READ.11.4 — Derived promotion lifecycle | C-GOLD.1.4.5 — Committed promotion remains absorbing | ACCEPTED — reciprocal USED BY entry for Gated by | The existing promotion_committed state remains absorbing; evidence changes affect new checks only. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.4] [NHD-B16EEB] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-GOLD.1.3.19 — Evaluation privacy and access | ACCEPTED — reciprocal USED BY entry for Gated by | Applies privacy and access authorization before relevance. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-GOLD.1.3.19 — Evaluation privacy and access | ACCEPTED — reciprocal USED BY entry for Gated by | Applies speaker/access scope wherever relevant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | C-GOLD.1 — Promotion evaluation-evidence bridge | ACCEPTED — Fed by continuation | The evaluation bridge extends gold-run evidence and supplies the narrow B16 evidence references in CY-G. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |

### Cross-piece relationships

| Using card | Defining/supplying card | Relation | Source |
|---|---|---|---|
| C-GOLD.1 — Promotion evaluation-evidence bridge | C-GOLD.1.5 — Evaluation operations and trial execution | ACCEPTED — Fed by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.3.6 — trial_attempt_start (E6) | C-GOLD.1.5.6.7 — Committed B9 R1 admission | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| C-GOLD.1.3.6 — trial_attempt_start (E6) | C-GOLD.1.5.3.6 — No attempt after run terminal | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | C-GOLD.1.5.11.4 — One conclusive resolution per attempt | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.3.9 — evaluation_run_terminal (E8) | C-GOLD.1.5.3 — Run closing conditions | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment (E9) | C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result (E10) | C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.4.1 — Scope-relevant atomic append | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.3.12 — gold_evidence_result (E11a) | C-GOLD.1.5.8.3 — DET-1 deterministic result identity | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.3.13 — held_out_evidence_result (E11b) | C-GOLD.1.5.8.3 — DET-1 deterministic result identity | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | C-GOLD.1.5.8.3 — DET-1 deterministic result identity | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

## Register contributions

### NOT DECIDED register

Every empty box is listed with its source-silence reason. Known mechanics deferred to another piece are listed separately and are not open decisions.

| Part ID | Field | Value | Why retained |
|---|---|---|---|
| C-GOLD.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.1 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.2 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.2 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.3 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.3 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.4 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.4 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.5 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.5 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.1.6 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.1.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.1.6 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.1.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.3.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.3.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.1.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.1.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.2.4.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.2.4.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.7 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.3.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.7 | Gated by | NOT DECIDED | The cited section supplies no additional part-owned blocking/authorization condition for this member beyond the recorded containing contract. |
| C-GOLD.1.2.3.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.3.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.4.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.2 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.3 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.4 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.5 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.6 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.5.7 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.5.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.5.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.6.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.6.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.6.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.6.2 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.6.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.6.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.6.3 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.2.6.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.6.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.6.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.6.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.1.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.1.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.1.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.12 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.7.2.14 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.2.7.2.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.1.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.12.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.12.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.12.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.12.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.12.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.12.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.14 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.2.15 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.2.15 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.4.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.4.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.4.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.4.4.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.4.4.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.12 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.5.14 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.5.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.6.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.6.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.7.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.7.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.7.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.2.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.7.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.7.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.7.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.8.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.8.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.8.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.8.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.9.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.9.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.9.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.9.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.6.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.6.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.6.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.6.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.6.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.6.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.9.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.9.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.9.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.9.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.9.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.9.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.10.12.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.10.12.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.11.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.11.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.12.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.12.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.13.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.13.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.14.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.14.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.15.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.15.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.15.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.15.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.15.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.15.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.15.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.15.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.15.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.15.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.16 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.16.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.16.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.16.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.16.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.16.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.16.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.17 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.17.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.17.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.17.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.17.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.18.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.18.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.18.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.18.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.18.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.18.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.3.19 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.3.19 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.4 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.4.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.4.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.4.2 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.4.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.4.3 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.4.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.4.4 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.4.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.4.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.4.5 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.4.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.4.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.2.3 | Policy values | NOT DECIDED | The accepted bridge defines policy slots but supplies no chosen trial count, tolerance or budget. |
| C-GOLD.1.2.7 | Coverage-profile instances | NOT DECIDED | The first accepted E3 instance and family-to-role mapping are not supplied. |
| C-GOLD.1.3.10.6 | NHD-B16EEB-D16 value | NOT DECIDED | The accepted proof kind, purpose and scope are unset; conditional proof structures do not select an option. |
| C-GOLD.1.3.2 | Concrete benchmark suites | NOT DECIDED | NHD-B16EEB-D15 supplies no accepted cases/prompts or suite instance. |
| C-GOLD.1.3.13 | Held-out definition and scoring | NOT DECIDED | NHD-B16EEB-D6/D7/D8b remain unset. |
| C-GOLD.1.3.16 | Objective invalidity policy value | NOT DECIDED | NHD-B16EEB-D10 remains unset. |
| C-GOLD.1.3.17 | Completed-run disagreement policy value | NOT DECIDED | NHD-B16EEB-D11 remains unset. |
| C-GOLD.1 | Physical record mechanics | NOT DECIDED | Canonicalization, integrity algorithms, storage/serialization and ledger/CAS storage are not selected by the source. |

### Source-conflict and status distinctions

No conflict is resolved by this pair. B16 v1.0 §5.3 retains its input-3 phrase “the recorded B24-architecture acceptance evidence for the applicable gold-set run”; the bridge separates E11a gold evidence from E12 system eligibility. The exact bridge contract is recorded here; the old source is not edited. [SOURCE CONFLICT: 04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3 retains the earlier input-3 wording; 04/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §7 records its pending integration.]

### Decided material not placed in this pair

- Bridge §§7.11–7.13: full judgment-chain authority, conditional proof lifecycles, claim fields/states/transitions and their protected recovery; only the record contract, terminal catalog and EB-8 interface are present here.
- Bridge §8–§9: complete result-state precedence and per-reading AP-1…AP-12 applicability cards; this pair records the reference and currentness contracts only.
- Bridge §10, §13.1 CR-24…CR-29 and CR-31…CR-40, and §14: remaining judgment-specific invariants, recovery and failure matrix; they are known accepted material, not undecided.
- Bridge §16–§17: full dependency matrix and all seventeen policy slots; the values remain open, while their accepted slot definitions await full placement.
- Remaining Group A engines, index, sealed-gold foundation/story-gold package, ingest and detector remain for later pieces. No completion of those components is claimed.

## Coverage matrix — cumulative contribution

### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c scoped reread: status table, §0/0A/0B, reading schema, §7G-A RC sequence and §7K; Chapter 3-d focused status-table, §0B and §§6A/6B checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c C-READ/C-7K and adjacent interfaces searched/reopened; Chapter 3-d C-READ and CY-G/B16 owner checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read for Chapter 3-e/3-f; exact blob verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Newly read whole for this correction, all 1,938 lines; pinned Git blob verified; Chapter 3-c focused retry/malformed searches and §§2.8/3.7 excerpts; prior whole-read credit retained | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read for Chapter 3-e/3-f; exact blob verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; remaining bridge behavior NOT PLACED: later pieces |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Detailed source landing map

| Bridge section | Cards in this piece |
|---|---|
| §3 | C-GOLD.1, C-GOLD.1.1, C-GOLD.1.1.1, C-GOLD.1.1.2, C-GOLD.1.1.3, C-GOLD.1.1.4, C-GOLD.1.1.5, C-GOLD.1.1.6 |
| §4.4 | C-GOLD.1, C-GOLD.1.2.5, C-GOLD.1.2.5.1, C-GOLD.1.2.5.2, C-GOLD.1.2.5.3, C-GOLD.1.2.5.4, C-GOLD.1.2.5.5, C-GOLD.1.2.5.6, C-GOLD.1.2.5.7 |
| §6 | C-GOLD.1, C-GOLD.1.4 |
| §9 | C-GOLD.1, C-GOLD.1.2.1.4, C-GOLD.1.3.15 |
| §4 | C-GOLD.1.2 |
| §4.1 | C-GOLD.1.2.1, C-GOLD.1.2.1.1, C-GOLD.1.2.1.2, C-GOLD.1.2.1.3, C-GOLD.1.2.1.3.1, C-GOLD.1.2.1.3.2, C-GOLD.1.2.1.3.3, C-GOLD.1.2.1.3.4, C-GOLD.1.2.1.3.5, C-GOLD.1.2.1.3.6, C-GOLD.1.2.1.3.7, C-GOLD.1.2.1.3.8, C-GOLD.1.2.1.3.9, C-GOLD.1.2.1.4, C-GOLD.1.2.2, C-GOLD.1.2.2.1, C-GOLD.1.2.2.2, C-GOLD.1.2.2.3, C-GOLD.1.2.2.4, C-GOLD.1.2.2.4.1, C-GOLD.1.2.2.4.2, C-GOLD.1.2.2.4.3, C-GOLD.1.2.2.4.4, C-GOLD.1.2.2.4.5, C-GOLD.1.2.2.4.6, C-GOLD.1.2.2.4.7 |
| §4.2 | C-GOLD.1.2.3, C-GOLD.1.2.3.1, C-GOLD.1.2.3.2, C-GOLD.1.2.3.3, C-GOLD.1.2.3.4, C-GOLD.1.2.3.5, C-GOLD.1.2.3.6, C-GOLD.1.2.3.7, C-GOLD.1.2.3.8 |
| §4.3 | C-GOLD.1.2.3, C-GOLD.1.2.4, C-GOLD.1.2.4.1, C-GOLD.1.2.4.2, C-GOLD.1.3.5 |
| §16 | C-GOLD.1.2.3.8 |
| §4.5 | C-GOLD.1.2.6, C-GOLD.1.2.6.1, C-GOLD.1.2.6.2, C-GOLD.1.2.6.3, C-GOLD.1.2.6.4, C-GOLD.1.3.5 |
| §4.6 | C-GOLD.1.2.7, C-GOLD.1.2.7.1, C-GOLD.1.2.7.1.1, C-GOLD.1.2.7.1.2, C-GOLD.1.2.7.1.3, C-GOLD.1.2.7.1.4, C-GOLD.1.2.7.2, C-GOLD.1.2.7.2.1, C-GOLD.1.2.7.2.2, C-GOLD.1.2.7.2.3, C-GOLD.1.2.7.2.4, C-GOLD.1.2.7.2.5, C-GOLD.1.2.7.2.6, C-GOLD.1.2.7.2.7, C-GOLD.1.2.7.2.8, C-GOLD.1.2.7.2.9, C-GOLD.1.2.7.2.10, C-GOLD.1.2.7.2.11, C-GOLD.1.2.7.2.12, C-GOLD.1.2.7.2.13, C-GOLD.1.2.7.2.14 |
| §5 | C-GOLD.1.3, C-GOLD.1.3.1, C-GOLD.1.3.1.1, C-GOLD.1.3.1.2, C-GOLD.1.3.1.3, C-GOLD.1.3.2, C-GOLD.1.3.2.1, C-GOLD.1.3.2.2, C-GOLD.1.3.2.3, C-GOLD.1.3.2.4, C-GOLD.1.3.2.5, C-GOLD.1.3.2.6, C-GOLD.1.3.2.7, C-GOLD.1.3.2.8, C-GOLD.1.3.2.9, C-GOLD.1.3.2.10, C-GOLD.1.3.2.11, C-GOLD.1.3.2.12, C-GOLD.1.3.2.12.1, C-GOLD.1.3.2.12.2, C-GOLD.1.3.2.12.3, C-GOLD.1.3.2.12.4, C-GOLD.1.3.2.12.5, C-GOLD.1.3.2.13, C-GOLD.1.3.2.14, C-GOLD.1.3.2.15, C-GOLD.1.3.3, C-GOLD.1.3.3.1, C-GOLD.1.3.4, C-GOLD.1.3.4.1, C-GOLD.1.3.4.2, C-GOLD.1.3.4.3, C-GOLD.1.3.4.4, C-GOLD.1.3.4.4.1, C-GOLD.1.3.4.4.2, C-GOLD.1.3.4.4.3, C-GOLD.1.3.4.4.4, C-GOLD.1.3.4.4.5, C-GOLD.1.3.5, C-GOLD.1.3.5.1, C-GOLD.1.3.5.2, C-GOLD.1.3.5.3, C-GOLD.1.3.5.4, C-GOLD.1.3.5.5, C-GOLD.1.3.5.6, C-GOLD.1.3.5.7, C-GOLD.1.3.5.8, C-GOLD.1.3.5.9, C-GOLD.1.3.5.10, C-GOLD.1.3.5.11, C-GOLD.1.3.5.12, C-GOLD.1.3.5.13, C-GOLD.1.3.5.14, C-GOLD.1.3.6, C-GOLD.1.3.6.1, C-GOLD.1.3.6.2, C-GOLD.1.3.6.3, C-GOLD.1.3.6.4, C-GOLD.1.3.6.5, C-GOLD.1.3.6.6, C-GOLD.1.3.7, C-GOLD.1.3.7.1, C-GOLD.1.3.7.2, C-GOLD.1.3.7.2.1, C-GOLD.1.3.7.2.2, C-GOLD.1.3.7.2.3, C-GOLD.1.3.7.3, C-GOLD.1.3.8, C-GOLD.1.3.8.1, C-GOLD.1.3.8.2, C-GOLD.1.3.9, C-GOLD.1.3.9.1, C-GOLD.1.3.9.2, C-GOLD.1.3.10, C-GOLD.1.3.10.1, C-GOLD.1.3.10.2, C-GOLD.1.3.10.3, C-GOLD.1.3.10.4, C-GOLD.1.3.10.5, C-GOLD.1.3.10.6, C-GOLD.1.3.10.7, C-GOLD.1.3.10.8, C-GOLD.1.3.10.9, C-GOLD.1.3.10.9.1, C-GOLD.1.3.10.9.2, C-GOLD.1.3.10.9.3, C-GOLD.1.3.10.10, C-GOLD.1.3.10.11, C-GOLD.1.3.10.12, C-GOLD.1.3.10.12.1, C-GOLD.1.3.11, C-GOLD.1.3.11.1, C-GOLD.1.3.11.2, C-GOLD.1.3.11.3, C-GOLD.1.3.11.4, C-GOLD.1.3.11.5, C-GOLD.1.3.11.6, C-GOLD.1.3.11.7, C-GOLD.1.3.11.8, C-GOLD.1.3.11.9, C-GOLD.1.3.11.10, C-GOLD.1.3.11.11, C-GOLD.1.3.12, C-GOLD.1.3.12.1, C-GOLD.1.3.12.2, C-GOLD.1.3.12.3, C-GOLD.1.3.12.4, C-GOLD.1.3.12.5, C-GOLD.1.3.13, C-GOLD.1.3.13.1, C-GOLD.1.3.13.2, C-GOLD.1.3.13.3, C-GOLD.1.3.13.4, C-GOLD.1.3.13.5, C-GOLD.1.3.14, C-GOLD.1.3.14.1, C-GOLD.1.3.14.2, C-GOLD.1.3.14.3, C-GOLD.1.3.14.4, C-GOLD.1.3.14.5, C-GOLD.1.3.14.6, C-GOLD.1.3.14.7, C-GOLD.1.3.14.8, C-GOLD.1.3.15, C-GOLD.1.3.15.1, C-GOLD.1.3.15.2, C-GOLD.1.3.15.3, C-GOLD.1.3.15.4, C-GOLD.1.3.15.5, C-GOLD.1.3.16, C-GOLD.1.3.16.1, C-GOLD.1.3.16.2, C-GOLD.1.3.16.3, C-GOLD.1.3.17, C-GOLD.1.3.17.1, C-GOLD.1.3.17.2, C-GOLD.1.3.18, C-GOLD.1.3.18.1, C-GOLD.1.3.18.2, C-GOLD.1.3.18.3, C-GOLD.1.3.18.4, C-GOLD.1.3.18.5 |
| §7.7 | C-GOLD.1.3.2, C-GOLD.1.3.6 |
| §8.1 | C-GOLD.1.3.2.13, C-GOLD.1.3.2.14, C-GOLD.1.3.2.15, C-GOLD.1.3.11 |
| §7.5 | C-GOLD.1.3.6 |
| §7.2 | C-GOLD.1.3.7, C-GOLD.1.3.9 |
| §7.10 | C-GOLD.1.3.7, C-GOLD.1.3.8 |
| §7.3 | C-GOLD.1.3.9 |
| §7.9 | C-GOLD.1.3.10, C-GOLD.1.3.10.12.1, C-GOLD.1.3.11, C-GOLD.1.3.12, C-GOLD.1.3.13, C-GOLD.1.3.18 |
| §7.11 | C-GOLD.1.3.10, C-GOLD.1.3.10.6.1, C-GOLD.1.3.10.6.2, C-GOLD.1.3.10.6.3, C-GOLD.1.3.11 |
| §7.12 | C-GOLD.1.3.10.6.1, C-GOLD.1.3.10.6.2, C-GOLD.1.3.10.6.3 |
| §6.2 | C-GOLD.1.3.12, C-GOLD.1.3.12.6, C-GOLD.1.3.13, C-GOLD.1.3.13.6, C-GOLD.1.3.15, C-GOLD.1.4.3 |
| §6.3 | C-GOLD.1.3.12, C-GOLD.1.3.13, C-GOLD.1.4.4, C-GOLD.1.4.4.1, C-GOLD.1.4.4.2, C-GOLD.1.4.4.3, C-GOLD.1.4.4.4 |
| §8.2 | C-GOLD.1.3.12, C-GOLD.1.3.12.6, C-GOLD.1.3.13.6 |
| §8.3 | C-GOLD.1.3.12.6, C-GOLD.1.3.13, C-GOLD.1.3.13.6 |
| §8.4 | C-GOLD.1.3.14 |
| §13.2 | C-GOLD.1.3.16 |
| §13.3 | C-GOLD.1.3.17 |
| §17 | C-GOLD.1.3.17 |
| §6.1 | C-GOLD.1.3.18, C-GOLD.1.4.1, C-GOLD.1.4.2, C-GOLD.1.4.2.1, C-GOLD.1.4.2.2 |
| §13.4 | C-GOLD.1.3.19 |
| §6.4 | C-GOLD.1.4.5 |

## READ RECORD

### Files read whole for this pair

- `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` — 2,018 lines, 135,956 bytes; SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`; Git blob matches the verified source pin.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` — acceptance identity/status and open-slot definitions; matched the source pin.
- Instruction: cloned `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md`, SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- Instruction: `NH_MASTER-21_FIX_REQUEST_ROUND1_2026-09-25(1).md`; the all-card field-placement rule and step reciprocity remain applied.

### Scoped checks, without new whole-read credit

- V10 authoritative status table; reading/production boundaries and protected gold/engine passages. No bridge behavior is recorded as built.
- Map C-GOLD, C-READ and adjacent Group A component definitions; bridge source §3 establishes evaluation ownership.
- Decision Index v0_11 NHD-B16EEB and L.4 rows, and the actual acceptance receipt; index used for navigation only.
- GitHub tree and commit comparison: source pin is `6a7160ba688ba4e433a31899162815df7e2bab17`; the governing and accepted bridge source blobs match the local copies. Six revised chapter blobs match the supplied GitHub pin; CH00 is an earlier assembly input, not used for new behavior.

### READ-folder files not yet read whole

97 entries retain the earlier pending whole-read status. The three B16/receipt files already had older Chapter 0 reading credits and were not in that pending list; they were now reread whole at this pin. The bridge source has only its earlier credit plus the scoped current check, not a new whole read. Scoped searches/excerpts supply no whole-read credit. The ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`

- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` — newly present at this source pin; not used for this evaluation scope.


The earlier whole-read accounting is carried forward; this pair adds whole-read credit only for the files explicitly listed above. The seven prior chapter files are preserved assembly inputs and receive no fresh whole-read credit here. No not-yet-read file supplies new behavior in this pair.

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 241 behavior cards, field lines and reciprocal rows checked; source status and read accounting are outside behavior. Runtime judgment authority remains runtime behavior, not drafting workflow.
§1.4 every gap written as NOT DECIDED: PASS — all 723 prohibition/failure/gate boxes reviewed against their own text and cited source. 471 empty fields and 8 scoped gaps are registered with reasons. Decided material scheduled for a later piece is separately listed; it is not called undecided.
§1.5 conflicts marked, none resolved: PASS — B16 v1.0’s earlier input-3 wording is preserved in the source-conflict register; Chapter 3-e also marks the narrow E13 behavior line. No accepted source or earlier chapter is edited; V10 remains governing.
§3 exactly one stamp per line: PASS — 1979 populated field lines and 570 USED BY rows checked. All are ACCEPTED from the exact accepted bridge source. The V10 status table grants no BUILT standing to these bridge records, operations or links; none is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — every populated field and reciprocal row carries exact 05/file §section citations to the accepted v1.7 source and NHD-B16EEB. All section targets resolve; record-definition citations include the actual later section where a carried outcome is defined. Receipt §§3–5 establishes accepted standing independently of folder/header.
§5.4 one name per thing: PASS — new sub-part IDs remain under the Map’s existing C-GOLD identifier; canonical endpoint names match prior chapter names. No new top-level ID or controlled NHD identifier is introduced. Proposed source names and globally unique policy-slot IDs are retained.
§6 all template fields present, in order, for every part: PASS — all 241 templates carry all nine fields in order, ALONE, TOGETHER, USED BY and SUB-PARTS; every listed child exists in this pair.
§6.3 reciprocity within this chapter: PASS — all 854 unique relationship pairs across 3-e/3-f checked in both directions. The 39 transaction/stage/recovery step cards name their defining rules with reciprocal USED BY rows. External endpoint additions are recorded here without modifying prior chapters.
§6.4 every decided detail written in, no citation used in place of content: PASS within this piece’s explicit scope — Both profiles and their path/system members; complete policy epoch requirements; all fourteen measurements; canonical E1–E16 contracts including E2e, E4S, E7r and distinct E11a/E11b; record members, conditional authority-reference forms, coverage registration conditions and currentness/disclosure. Full protected judgment and result derivation are explicitly reserved for later pieces.
§6.5 sub-parts recursed to the bottom: PASS within this piece’s explicit scope — record members, named measurement dimensions, registered enum/failure classes, operation outcomes, commit conditions and resolution consequences have cards. No unchosen policy value, storage algorithm, mechanism or authorization option is invented.
§9 coverage matrix rows added for every file used: PASS — all 145 READ-folder files at the pin are accounted for; all 107 carried V10 heading rows remain. The bridge and receipt rows reflect this whole read, with a detailed section landing map. Source/passed-chapter blob preservation checked for 52 matched local files.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked in all behavior cards and register contributions; source recommendations are not imported as decisions.
Files read whole for this chapter: `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; the cloned contract and fix-request instructions. Scoped rereads and inherited whole-read credits remain separately identified in READ RECORD.

This is the producing assistant’s contract check, not an independent audit, acceptance, adoption or implementation authorization. The two new pieces are delivered together under the current request; all passed chapters remain unchanged.
