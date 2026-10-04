# Chapter 3-j — Group A: C-ENGINE-C

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-j.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece describes Engine C's story-reading boundary and its interfaces. Engine C remains unbuilt. The accepted telling identity and firmness designs retain ACCEPTED stamps; their existence does not make the engine or a link to it BUILT. C-READ.10 — Reading-to-telling persistence and its descendants already hold the telling fields, identity, correspondence, commit, completion and recovery contracts in CH03-c. This piece reuses those cards. C-7B.3.4 — Clash preservation already holds the rule preserving conflicting tellings in CH02.

CH03-l owns the story-gold cases and their root-pinning route. CH05-a owns the full acceptance architecture and failure taxonomy; CH05-b the async worker; CH05-c retrieval scope/ranking/limits; CH06-b the complete Story Layer and theme lifecycle. No case is reconstructed from an A1 status record. The source map below names the remaining deferrals. Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`.
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.


<!-- BEGIN BEHAVIOR -->

### C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K)
Stamp: DESIGNED    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, The engine (2c) row] [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — The SMART engine layer that reads a root for its tellings and fills the reading's `story_layer`, beyond bare meaning and preceding-turn context. [V10 §7C] [MAP C-ENGINE-C]
- Takes in: DESIGNED — A target root, declared reading mode and story-bearing context, with root evidence separated from prior reading context. [V10 §7G] [MAP C-ENGINE-C]
- Does: DESIGNED — Produces one reading proposal per pass, submits it to the Reading Proposal Acceptance Check, and passes accepted story-reading material to the quarantine write boundary. [V10 §7G] [MAP C-ENGINE-C]
- Gives out: DESIGNED — A reading with embedded `story_layer` tellings, written through `append_reading()` to quarantine; those tellings feed Story Layer, clash handling and Computed View through their governed interfaces. [MAP C-ENGINE-C]
- Gives out: ACCEPTED — Complete semantic telling material accompanying the embedded entry, for the accepted first-class telling persistence contract; the system, not the mouth, assigns `telling_id` and `parent_reading_id`. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Must never: DESIGNED — Write directly to production, merge conflicting tellings, turn repetition into fact, invent connective tissue, merge the two evidence channels, or accept a telling solely because prior readings asserted it. [V10 §7G] [MAP C-ENGINE-C]
- Fails closed by: DESIGNED — Rejects an unacceptable proposal and records the specific reason. Insufficient root support leaves the telling omitted or marked `insufficient_context`; it never licenses invention. [V10 §7G]

TOGETHER
- Fed by: DESIGNED — C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): supplies the story-layer web that this engine realizes. [MAP C-7B] [MAP C-ENGINE-C]
- Fed by: DESIGNED — C-7B.3 — Story-Layer Web: supplies the story dimension to be filled from story-bearing input. [MAP C-7B]
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): supplies the context for the story pass. [MAP C-ENGINE-C]
- Fed by: DESIGNED — C-16 — Model Layer (§16): supplies the mouth used to propose the reading. [MAP C-ENGINE-C]
- Fed by: DESIGNED — C-ENGINE-C.1 — Story-layer engine pass: provides the bounded single-pass operation. [V10 §7G] [MAP C-ENGINE-C]
- Fed by: ACCEPTED — C-ENGINE-C.5 — Complete semantic telling proposal: supplies the grounded semantic payload needed by the accepted telling contract. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Fed by: DESIGNED — C-ENGINE-C.8 — Story-pass operation records: preserves the pass inputs, decisions and evidence basis. [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-ENGINE-C.2 — Story-layer evidence channels: root evidence and prior interpretations must remain distinct. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3 — Root-grounded telling: every telling requires supporting roots; prior readings alone cannot establish it. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.4 — Story proposal acceptance boundary: the mouth's proposal must pass the shared acceptance check, independently of its claimed confidence. [V10 §7G] [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-7B.3.4 — Clash preservation: disagreeing tellings stay separate; neither repetition nor engine output selects a winner. [V10 §7K] [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-ENGINE-C.7 — Story-bearing benchmark prerequisite: story-bearing gold is required before Engine C can be built or tested. [V10 §7C] [MAP C-ENGINE-C]
- Gated by: ACCEPTED — C-READ.10.14.6 — Engine C interface: the telling-identity interface retains its acceptance, later integration and separate implementation-authorization conditions. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-ENGINE-C.10 — Firmness proposal boundary: a firmness claim must obey the qualitative policy and carry its evidence basis. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3]
- Gated by: DESIGNED — C-ENGINE-C.11 — Theme proposal boundary: engine themes remain proposed and their retrieval influence must be recorded. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: DESIGNED — C-READ — Reading record, validator, writer (§6B): the proposed Engine C route uses the shared reading write boundary. [MAP C-ENGINE-C]
- Changes: DESIGNED — C-ENGINE-C.6 — Engine C quarantine handoff: supplies accepted reading and telling material for the quarantine route. [MAP C-ENGINE-C]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7B.3 — Story-Layer Web | Story-bearing input for the story dimension. | Supplies the story-layer engine's telling material to the web. | Story readings remain separate, grounded and revisable. | [MAP C-7B] [MAP C-ENGINE-C] |
| 2 · DESIGNED | C-READ — Reading record, validator, writer (§6B) | A story-bearing reading proposal. | Supplies accepted story-reading material to the shared write boundary. | A quarantine reading and its governed telling material; roots remain intact. | [MAP C-ENGINE-C] [V10 §7G] |
| 3 · DESIGNED | C-7K — Story Layer (§7K) | Tellings from engine passes, their roots/readings and perspective provenance, time, firmness evidence, theme proposals and Ness's theme actions. | Supplies story-bearing pass output. | Nothing in this card. | [V10 §7K] [MAP C-7K] |
| 4 · ACCEPTED | C-READ.10.14.6 — Engine C interface | NOT DECIDED | Supplies what this place relies on: the accepted embedded and complete telling material; its own design status is unchanged. | Nothing in this card. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §1] |

SUB-PARTS: C-ENGINE-C.1 — Story-layer engine pass; C-ENGINE-C.2 — Story-layer evidence channels; C-ENGINE-C.3 — Root-grounded telling; C-ENGINE-C.4 — Story proposal acceptance boundary; C-ENGINE-C.5 — Complete semantic telling proposal; C-ENGINE-C.6 — Engine C quarantine handoff; C-ENGINE-C.7 — Story-bearing benchmark prerequisite; C-ENGINE-C.8 — Story-pass operation records; C-ENGINE-C.9 — Inherited pass recovery; C-ENGINE-C.10 — Firmness proposal boundary; C-ENGINE-C.11 — Theme proposal boundary

### C-ENGINE-C.1 — Story-layer engine pass
Stamp: DESIGNED    Source: [V10 §7G] [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — One declared story-reading pass over one target root. [V10 §7G]
- Takes in: DESIGNED — The target, optional positional and semantic context, and the declared mode, purpose or angle. [V10 §7G]
- Does: DESIGNED — Obtains a mouth proposal and sends it through acceptance; multiple angles require multiple explicit passes. [V10 §7G]
- Gives out: DESIGNED — One separate reading with its own context inputs, engine version, configuration and timestamp. [V10 §7G]
- Must never: DESIGNED — Hide secondary interpretations outside the reading record, overwrite an earlier reading, or silently merge conflicting readings. [V10 §7G]
- Fails closed by: DESIGNED — An acceptance failure rejects the proposal and records its specific reason separately. [V10 §7G]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies the async operation identity and worker route used for the pass. [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): one target and one declared pass yield one reading, and the proposal must pass acceptance. [V10 §7G]
- Gated by: DESIGNED — C-ENGINE-C.9 — Inherited pass recovery: the worker's operation identity, idempotency and crash-recovery rules govern execution. [MAP C-ENGINE-C]
- Changes: DESIGNED — C-ENGINE-C.6 — Engine C quarantine handoff: delivers the accepted reading proposal for quarantine persistence. [MAP C-ENGINE-C]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | The target, optional positional and semantic context, and the declared mode, purpose or angle. | provides the bounded single-pass operation. | One separate reading with its own context inputs, engine version, configuration and timestamp. | [V10 §7G] [MAP C-ENGINE-C] |

SUB-PARTS: NONE

### C-ENGINE-C.2 — Story-layer evidence channels
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The separation of original source evidence from earlier interpretations in a story-layer pass. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — Prior roots and completed prior readings supplied for the pass. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Keeps them in two clearly labeled channels: root evidence and prior reading context. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Combine roots and readings into an undifferentiated evidence block or give an earlier interpretation the evidential status of its source. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: DESIGNED — Roots and readings stay in separate labeled channels; an earlier interpretation never takes the evidential status of its source. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: DESIGNED — C-ENGINE-C.2.1 — Root evidence channel: supplies original source material at its higher evidential status. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fed by: DESIGNED — C-ENGINE-C.2.2 — Prior reading context channel: supplies completed prior interpretations as interpretive context only. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3.2 — No circular story support: repeated interpretations cannot validate one another without roots. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | Prior roots and completed prior readings supplied for the pass. | root evidence and prior interpretations must remain distinct. | Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 2 · DESIGNED | C-ENGINE-C.2.1 — Root evidence channel | Prior roots and completed prior readings supplied for the pass. | original evidence must remain labeled and separate from prior readings. | Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 3 · DESIGNED | C-ENGINE-C.2.2 — Prior reading context channel | Prior roots and completed prior readings supplied for the pass. | prior interpretations must remain labeled as interpretations. | Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 4 · DESIGNED | C-ENGINE-C.3 — Root-grounded telling | Prior roots and completed prior readings supplied for the pass. | supplies separately labeled original and interpretive material. | Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 5 · DESIGNED | C-ENGINE-C.8 — Story-pass operation records | Prior roots and completed prior readings supplied for the pass. | supplies the identity of every root and reading presented on each channel. | Distinguishable source evidence and interpretive context, with every supplied root ID and reading ID preserved. | [V10 §7G / STORY-LAYER EVIDENCE RULES] [MAP C-ENGINE-C] |
| 6 · DESIGNED | C-7G.6 — Story-layer grounding boundary | Root evidence in one labeled channel and completed prior readings in a separate interpretation-context channel. | Keeps root evidence separate from prior interpretation context. | Nothing in this card. | [V10 §7G] |

SUB-PARTS: C-ENGINE-C.2.1 — Root evidence channel; C-ENGINE-C.2.2 — Prior reading context channel

### C-ENGINE-C.2.1 — Root evidence channel
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The story pass's channel for original source material. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — Supporting roots supplied to the pass. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Provides root evidence at higher evidential status than prior interpretations. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — Source material with its root IDs available for grounding and the audit trail. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Lose the distinction between source roots and interpretive readings. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): supplies source roots for the story-reading pass. [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-ENGINE-C.2 — Story-layer evidence channels: original evidence must remain labeled and separate from prior readings. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.2 — Story-layer evidence channels | Supporting roots supplied to the pass. | supplies original source material at its higher evidential status. | Source material with its root IDs available for grounding and the audit trail. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |

SUB-PARTS: NONE

### C-ENGINE-C.2.2 — Prior reading context channel
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The story pass's channel for completed earlier interpretations. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — Completed prior readings and their IDs. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Supports continuity, comparison and discovery without replacing root grounding. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — Labeled interpretive context with a preserved record of the reading IDs supplied. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Make an earlier assertion sufficient proof of a telling or use unfinished current-pass output as evidence. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: DESIGNED — Excludes unfinished current-pass output from eligibility as prior reading evidence. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): supplies prior reading context to the story pass. [MAP C-ENGINE-C] [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.2 — Story-layer evidence channels: prior interpretations must remain labeled as interpretations. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3.1 — Completed-prior-reading requirement: only completed prior readings are eligible. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.2 — Story-layer evidence channels | Completed prior readings and their IDs. | supplies completed prior interpretations as interpretive context only. | Labeled interpretive context with a preserved record of the reading IDs supplied. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |

SUB-PARTS: NONE

### C-ENGINE-C.3 — Root-grounded telling
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The grounding condition on every story telling. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — A telling proposal, supporting root IDs and any completed prior readings used as context. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Requires support in roots; prior readings may assist continuity, comparison or discovery. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — A root-grounded telling, or the honest weak-evidence outcome when support is insufficient. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Accept a telling merely because previous readings repeated it or let derived material indefinitely validate other derived material without roots. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: DESIGNED — Insufficient root support leaves the telling omitted or marked `insufficient_context`, never invented. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: DESIGNED — C-ENGINE-C.2 — Story-layer evidence channels: supplies separately labeled original and interpretive material. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3.1 — Completed-prior-reading requirement: unfinished current output cannot support its own proposal. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3.2 — No circular story support: derived repetition cannot replace original evidence. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: DESIGNED — C-ENGINE-C.3.3 — Insufficient root support: an unsupported telling must be omitted or honestly marked. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | A telling proposal, supporting root IDs and any completed prior readings used as context. | every telling requires supporting roots; prior readings alone cannot establish it. | A root-grounded telling, or the honest weak-evidence outcome when support is insufficient. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 2 · DESIGNED | C-ENGINE-C.3.2 — No circular story support | A telling proposal, supporting root IDs and any completed prior readings used as context. | supporting root IDs are required for every telling. | A root-grounded telling, or the honest weak-evidence outcome when support is insufficient. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 3 · DESIGNED | C-ENGINE-C.3.3 — Insufficient root support | A telling proposal, supporting root IDs and any completed prior readings used as context. | a telling must have support in the supplied roots. | A root-grounded telling, or the honest weak-evidence outcome when support is insufficient. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 4 · DESIGNED | C-7G.6 — Story-layer grounding boundary | Root evidence in one labeled channel and completed prior readings in a separate interpretation-context channel. | Gates this place: requires root support, completed prior readings and no circularity. | Nothing in this card. | [V10 §7G] |

SUB-PARTS: C-ENGINE-C.3.1 — Completed-prior-reading requirement; C-ENGINE-C.3.2 — No circular story support; C-ENGINE-C.3.3 — Insufficient root support

### C-ENGINE-C.3.1 — Completed-prior-reading requirement
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The eligibility limit on interpretive context for a story pass. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — A reading considered for use as evidence in the pass. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Allows only completed prior readings. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — Eligible completed context; unfinished current-pass output remains ineligible. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Use an unfinished output from the current pass as its own evidence. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: DESIGNED — Keeps that unfinished output out of the prior-reading evidence channel. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-ENGINE-C.3.2 — No circular story support: a pass cannot bootstrap its own support from unfinished output. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.2.2 — Prior reading context channel | A reading considered for use as evidence in the pass. | only completed prior readings are eligible. | Eligible completed context; unfinished current-pass output remains ineligible. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 2 · DESIGNED | C-ENGINE-C.3 — Root-grounded telling | A reading considered for use as evidence in the pass. | unfinished current output cannot support its own proposal. | Eligible completed context; unfinished current-pass output remains ineligible. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |

SUB-PARTS: NONE

### C-ENGINE-C.3.2 — No circular story support
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The prohibition on interpretations validating themselves through repetition. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — The support claimed for a proposed telling, including any earlier readings. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Requires supporting roots behind the telling instead of a chain consisting only of derived assertions. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — A grounding boundary that gives repetition no power to make a reading true. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Treat later repetition as proof of an earlier reading or permit an endless derived-material validation chain without root support. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Fails closed by: DESIGNED — A telling is not accepted solely on earlier readings' assertions. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-ENGINE-C.3 — Root-grounded telling: supporting root IDs are required for every telling. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.2 — Story-layer evidence channels | The support claimed for a proposed telling, including any earlier readings. | repeated interpretations cannot validate one another without roots. | A grounding boundary that gives repetition no power to make a reading true. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 2 · DESIGNED | C-ENGINE-C.3 — Root-grounded telling | The support claimed for a proposed telling, including any earlier readings. | derived repetition cannot replace original evidence. | A grounding boundary that gives repetition no power to make a reading true. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| 3 · DESIGNED | C-ENGINE-C.3.1 — Completed-prior-reading requirement | The support claimed for a proposed telling, including any earlier readings. | a pass cannot bootstrap its own support from unfinished output. | A grounding boundary that gives repetition no power to make a reading true. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |

SUB-PARTS: NONE

### C-ENGINE-C.3.3 — Insufficient root support
Stamp: DESIGNED    Source: [V10 §7G / STORY-LAYER EVIDENCE RULES]

ALONE
- What it is: DESIGNED — The story-pass outcome when roots do not adequately support a telling. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Takes in: DESIGNED — A telling for which root support is insufficient. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Does: DESIGNED — Omits the telling or marks it `insufficient_context`. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gives out: DESIGNED — An honest absence or context limitation. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: DESIGNED — Invent a telling to fill an evidential gap. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Must never: ACCEPTED — Manufacture an accepted empty `story_layer` by silently deleting a rejected telling from a failed proposal. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.5]
- Fails closed by: DESIGNED — Leaves unsupported telling content unasserted, preserving the omission or insufficiency. [V10 §7G / STORY-LAYER EVIDENCE RULES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-ENGINE-C.3 — Root-grounded telling: a telling must have support in the supplied roots. [V10 §7G / STORY-LAYER EVIDENCE RULES]
- Gated by: ACCEPTED — C-READ.10.3 — Reading and telling correspondence checks: required semantic acceptance cannot be bypassed by stripping an invalid telling from a rejected proposal. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.3 — Root-grounded telling | A telling for which root support is insufficient. | an unsupported telling must be omitted or honestly marked. | An honest absence or context limitation. | [V10 §7G / STORY-LAYER EVIDENCE RULES] |

SUB-PARTS: NONE

### C-ENGINE-C.4 — Story proposal acceptance boundary
Stamp: DESIGNED    Source: [V10 §7G] [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — The shared acceptance boundary between Engine C's mouth proposal and the reading record. [V10 §7G] [MAP C-ENGINE-C]
- Takes in: DESIGNED — The proposed reading, target root, supplied context, declared mode and supporting evidence. [V10 §7G]
- Does: DESIGNED — Submits the proposal to an explicit acceptance check that the mouth does not judge alone. L6 applies: model confidence is metadata, not authority. [V10 §7G] [MAP C-ENGINE-C]
- Gives out: DESIGNED — An acceptance result with its reasons, or a rejection with the specific failure reason preserved separately. [V10 §7G]
- Must never: DESIGNED — Accept a reading solely because the mouth claims confidence, allow unsupported certainty, or silently turn a rejected proposal into the accepted reading. [V10 §7G]
- Fails closed by: DESIGNED — Rejects a proposal that fails the required acceptance conditions and records why; unsupported certainty is rejected or downgraded by the acceptance layer. [V10 §7G]

TOGETHER
- Fed by: ACCEPTED — C-ENGINE-C.5 — Complete semantic telling proposal: supplies every semantic telling claim for grounding checks. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): acceptance depends on grounding, supplied context and the declared reading mode. [V10 §7G]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | The proposed reading, target root, supplied context, declared mode and supporting evidence. | the mouth's proposal must pass the shared acceptance check, independently of its claimed confidence. | An acceptance result with its reasons, or a rejection with the specific failure reason preserved separately. | [V10 §7G] [MAP C-ENGINE-C] |
| 2 · DESIGNED | C-ENGINE-C.8 — Story-pass operation records | The proposed reading, target root, supplied context, declared mode and supporting evidence. | supplies the acceptance or rejection reasoning to preserve. | An acceptance result with its reasons, or a rejection with the specific failure reason preserved separately. | [MAP C-ENGINE-C] [V10 §7G] |

SUB-PARTS: NONE

### C-ENGINE-C.5 — Complete semantic telling proposal
Stamp: ACCEPTED    Source: [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The complete SMART telling material proposed alongside each embedded `story_layer` entry. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Takes in: ACCEPTED — The target and supplied evidence, with deterministic pass-local evidence handles identifying only material actually supplied. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1]
- Does: ACCEPTED — Proposes `subject`, `perspective_owner`, optional `attribution_path`, `evidence_relationship`, `telling`, optional `stance`, optional `firmness` and its required `firmness_evidence_basis`, optional `source_event_time`, the support claim via handles, and the embedded entry. Every semantic claim passes acceptance before persistence preparation. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Gives out: ACCEPTED — One accepted semantic origin for the embedded entry and first-class telling payload. Its populated legacy `whose`, `theme` and `when` values are preserved mechanically as `legacy_whose`, `legacy_theme` and `embedded_when`; omission stays omission. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Must never: ACCEPTED — Generate or override source-carried `root_speaker` or parent-reading `role`, invent persistent raw record IDs, generate machine identity/idempotency/timestamp/schema fields, or add, normalize or enrich semantic content after acceptance. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — A semantic claim without support fails acceptance; invalid or ungrounded telling material cannot enter the durable manifest or become a card. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-READ.10.1 — Complete telling-card payload: defines the semantic fields and their separate mechanical counterparts. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-READ.10.1.3.1 — Pass-local support selection: constrains support claims to deterministic handles supplied with this pass. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1]
- Gated by: ACCEPTED — C-READ.10.3 — Reading and telling correspondence checks: every semantic claim must pass acceptance and both representations must retain the same accepted content. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Changes: ACCEPTED — C-READ.10 — Reading-to-telling persistence: hands over the accepted semantic material for mechanical assembly and exact-payload persistence. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | The target and supplied evidence, with deterministic pass-local evidence handles identifying only material actually supplied. | supplies the grounded semantic payload needed by the accepted telling contract. | One accepted semantic origin for the embedded entry and first-class telling payload. Its populated legacy `whose`, `theme` and `when` values are preserved mechanically as `legacy_whose`, `legacy_theme` and `embedded_when`; omission stays omission. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] |
| 2 · ACCEPTED | C-ENGINE-C.4 — Story proposal acceptance boundary | The target and supplied evidence, with deterministic pass-local evidence handles identifying only material actually supplied. | supplies every semantic telling claim for grounding checks. | One accepted semantic origin for the embedded entry and first-class telling payload. Its populated legacy `whose`, `theme` and `when` values are preserved mechanically as `legacy_whose`, `legacy_theme` and `embedded_when`; omission stays omission. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] |
| 3 · ACCEPTED | C-ENGINE-C.6 — Engine C quarantine handoff | The target and supplied evidence, with deterministic pass-local evidence handles identifying only material actually supplied. | supplies the accepted embedded and complete telling material. | One accepted semantic origin for the embedded entry and first-class telling payload. Its populated legacy `whose`, `theme` and `when` values are preserved mechanically as `legacy_whose`, `legacy_theme` and `embedded_when`; omission stays omission. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] |

SUB-PARTS: NONE

### C-ENGINE-C.6 — Engine C quarantine handoff
Stamp: DESIGNED    Source: [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — Engine C's planned handoff to the shared quarantine reading boundary. [MAP C-ENGINE-C]
- Takes in: DESIGNED — The accepted story-layer reading proposal. [V10 §7G] [MAP C-ENGINE-C]
- Does: DESIGNED — Uses `append_reading()` for quarantine output, with tellings carried inside `story_layer`. [MAP C-ENGINE-C]
- Does: ACCEPTED — Uses the shared persistence contract for the matching first-class cards and `prepared_reading_telling_envelope`; mechanical support resolution supplies `supporting_root_ids` without choosing new evidence. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Gives out: ACCEPTED — The accepted proposal may legitimately contain zero, one or several tellings. An empty set has a positive zero-telling completion sentinel; several tellings require a complete integrity-valid set before semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.5]
- Must never: DESIGNED — Send Engine C output directly into production. [MAP C-ENGINE-C]
- Must never: ACCEPTED — Treat an assigned telling identity or a partially committed set as sufficient for semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Incomplete or integrity-invalid telling sets remain unavailable for telling-level semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-ENGINE-C.5 — Complete semantic telling proposal: supplies the accepted embedded and complete telling material. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Gated by: DESIGNED — C-READ — Reading record, validator, writer (§6B): the engine route goes through the shared writer, never a direct production write. [MAP C-ENGINE-C]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: only a complete, integrity-valid set with valid completion proof permits telling-level semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Changes: DESIGNED — C-READ.4 — Quarantine readings destination: receives Engine C's planned story readings. [MAP C-ENGINE-C]
- Changes: ACCEPTED — C-READ.10 — Reading-to-telling persistence: receives the accepted payload for the shared identity, correspondence and commit protocol. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | The accepted story-layer reading proposal. | supplies accepted reading and telling material for the quarantine route. | The accepted proposal may legitimately contain zero, one or several tellings. An empty set has a positive zero-telling completion sentinel; several tellings require a complete integrity-valid set before semantic use. | [MAP C-ENGINE-C] [V10 §7G] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.5] |
| 2 · DESIGNED | C-ENGINE-C.1 — Story-layer engine pass | The accepted story-layer reading proposal. | delivers the accepted reading proposal for quarantine persistence. | The accepted proposal may legitimately contain zero, one or several tellings. An empty set has a positive zero-telling completion sentinel; several tellings require a complete integrity-valid set before semantic use. | [MAP C-ENGINE-C] [V10 §7G] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.5] |

SUB-PARTS: NONE

### C-ENGINE-C.7 — Story-bearing benchmark prerequisite
Stamp: DESIGNED    Source: [V10 §7C] [MAP C-ENGINE-C] [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The requirement for story-bearing gold before building or testing Engine C. [V10 §7C] [MAP C-ENGINE-C]
- Takes in: DESIGNED — Story-bearing gold cases suitable for testing the story-layer reading. [V10 §7C]
- Does: DESIGNED — Keeps the next engine layer behind that gold prerequisite; the protected order puts the live path before nightly deepening. [V10 §7C] [MAP C-GOLD]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat Engine C as built, invent the required gold cases, or assume wider/full-thread reading works without benchmarking. [MAP C-ENGINE-C] [MAP C-GOLD]
- Must never: ACCEPTED — Treat the A1 design-provenance seal as a runtime `.sealed` marker, real-root assignment, root pinning, or an executable benchmark. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Fails closed by: DESIGNED — Engine C cannot proceed to testing without story-bearing gold. [V10 §7C]

TOGETHER
- Fed by: DESIGNED — C-GOLD — Sealed gold sets v1, v2-B (§7C): the separate story-gold dependency supplies the required Engine C benchmark; the built v1/v2-B sets alone do not fill it. [MAP C-GOLD] [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-GOLD — Sealed gold sets v1, v2-B (§7C): the protected build order requires story-bearing gold first and benchmarked evidence for wider-thread claims. [MAP C-GOLD]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | Story-bearing gold cases suitable for testing the story-layer reading. | story-bearing gold is required before Engine C can be built or tested. | NOT DECIDED | [V10 §7C] [MAP C-ENGINE-C] |

SUB-PARTS: NONE

### C-ENGINE-C.8 — Story-pass operation records
Stamp: DESIGNED    Source: [V10 §0B] [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — The connected operational record of each story-layer pass. [V10 §0B] [MAP C-ENGINE-C]
- Takes in: DESIGNED — The actual pass, root IDs and reading IDs supplied on each channel, acceptance or rejection reasoning, and each produced telling with its evidence basis. [MAP C-ENGINE-C]
- Does: DESIGNED — Records those operations and their supplied evidence; each real operation receives one permanent log. [V10 §0B] [MAP C-ENGINE-C]
- Gives out: DESIGNED — An append-only, traceable account that remains living memory under the applicable access rules. [V10 §0B] [MAP C-ENGINE-C]
- Must never: DESIGNED — Leave a pass, supplied evidence or acceptance reason silent, destroy its record, count the log as extra support for the telling, or start an automatic log-about-log chain. [V10 §0B] [MAP C-ENGINE-C]
- Fails closed by: DESIGNED — A component without its traceable operation record is incomplete by design and is not adopted. [V10 §0B]

TOGETHER
- Fed by: DESIGNED — C-ENGINE-C.2 — Story-layer evidence channels: supplies the identity of every root and reading presented on each channel. [V10 §7G / STORY-LAYER EVIDENCE RULES] [MAP C-ENGINE-C]
- Fed by: DESIGNED — C-ENGINE-C.4 — Story proposal acceptance boundary: supplies the acceptance or rejection reasoning to preserve. [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): recorded evidence remains subject to access and authorization restrictions. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-C]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): identity and security authorization apply where required. [MAP C-ENGINE-C]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | The actual pass, root IDs and reading IDs supplied on each channel, acceptance or rejection reasoning, and each produced telling with its evidence basis. | preserves the pass inputs, decisions and evidence basis. | An append-only, traceable account that remains living memory under the applicable access rules. | [MAP C-ENGINE-C] [V10 §0B] |

SUB-PARTS: NONE

### C-ENGINE-C.9 — Inherited pass recovery
Stamp: DESIGNED    Source: [MAP C-ENGINE-C]

ALONE
- What it is: DESIGNED — Engine C's use of the shared async pass identity, idempotency and crash-recovery route. [MAP C-ENGINE-C]
- Takes in: DESIGNED — The story pass's operation identity and execution state. [MAP C-ENGINE-C]
- Does: DESIGNED — Runs on the post-root worker path and inherits its recovery behavior. [MAP C-ENGINE-C]
- Gives out: DESIGNED — One reading per pass under the worker's operation and duplicate-prevention boundary. [MAP C-ENGINE-C]
- Must never: ACCEPTED — Rerun or reinterpret model output as exact-payload crash recovery, or use recovery material as semantic evidence. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §1]
- Fails closed by: ACCEPTED — Telling-specific semantic use waits for the complete, valid telling set; identity alone does not release that gate. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): provides the governing async operation and crash-recovery route. [MAP C-ENGINE-C]
- Gated by: ACCEPTED — C-READ.10.7 — Reading-to-telling recovery: recovery must preserve the exact accepted payload and assigned identities. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §1]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: semantic fan-out stays blocked until completion and integrity are established. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C.1 — Story-layer engine pass | The story pass's operation identity and execution state. | the worker's operation identity, idempotency and crash-recovery rules govern execution. | One reading per pass under the worker's operation and duplicate-prevention boundary. | [MAP C-ENGINE-C] |

SUB-PARTS: NONE

### C-ENGINE-C.10 — Firmness proposal boundary
Stamp: ACCEPTED    Source: [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The engine's qualitative interpretation of how strongly the perspective owner appears to hold a stance. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §0]
- Takes in: ACCEPTED — Observable source-grounded signals and their attribution; direct self-report is stronger evidence than tone, wording style or repetition alone, while reported speech or uncertain attribution lowers evidential strength. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Uses `low_firmness`, `moderate_firmness`, `high_firmness`, `mixed_firmness`, `uncertain_firmness`, or the `omitted_no_support` outcome. Each non-omitted assignment records a source-grounded evidence basis; an honest unresolved boundary uses the less-claiming record. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — A provisional, revisable firmness claim beside `firmness_evidence_basis`. `omitted_no_support` leaves `firmness` absent on the accepted telling card and v1 embedded entry; it does not write a placeholder. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Force a firmness level, use numeric scores or hidden arithmetic, conflate firmness with truth/confidence/grounding/relevance/source reliability, claim direct access to an inner state, or strengthen a claim by repeating the same evidence. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Genuine conflict or ambiguity yields mixed or uncertain firmness; no usable support yields honest absence. Revision creates a new reading/telling beside the earlier one. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-READ.10.1.12 — firmness_evidence_basis: carries the observable, source-grounded basis for every non-omitted value. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-READ.10.1.11 — firmness: the established label meanings, omission rule and separate dimensions constrain the proposal. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | Observable source-grounded signals and their attribution; direct self-report is stronger evidence than tone, wording style or repetition alone, while reported speech or uncertain attribution lowers evidential strength. | a firmness claim must obey the qualitative policy and carry its evidence basis. | A provisional, revisable firmness claim beside `firmness_evidence_basis`. `omitted_no_support` leaves `firmness` absent on the accepted telling card and v1 embedded entry; it does not write a placeholder. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-ENGINE-C.11 — Theme proposal boundary
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — The engine's ability to propose a navigational theme without confirming it. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — One telling or patterns across multiple tellings, with supporting roots. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Proposes a theme and records supporting root IDs, telling/reading IDs, who or what proposed it, why the items appear connected, timestamp and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — A `proposed` theme; only Ness confirms it. A telling may have no theme, one theme or several themes. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Treat a proposal as a settled category, let aging or repetition confirm it, let a theme validate itself without roots, or allow an unrecorded theme influence on future readings. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: DESIGNED — Unresolved themes stay proposed indefinitely; later readings may challenge, omit or contradict even a confirmed theme. [V10 §7K / HYBRID THEME SYSTEM]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): supplies tellings and the hybrid-theme organization in which proposals remain distinct from confirmation. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: ACCEPTED — C-READ.10.14.8 — Telling-to-theme reference: a telling-level link uses the stable telling identity, retains root support and never copies or confirms the telling. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7K — Story Layer (§7K): confirmation remains Ness's act, and proposed themes cannot silently shape later reading. [V10 §7K / HYBRID THEME SYSTEM]
- Changes: DESIGNED — C-7K — Story Layer (§7K): adds proposed navigational themes with their supporting evidence and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | One telling or patterns across multiple tellings, with supporting roots. | engine themes remain proposed and their retrieval influence must be recorded. | A `proposed` theme; only Ness confirms it. A telling may have no theme, one theme or several themes. | [V10 §7K / HYBRID THEME SYSTEM] |
| 2 · DESIGNED | C-7K — Story Layer (§7K) | Tellings from engine passes, their roots/readings and perspective provenance, time, firmness evidence, theme proposals and Ness's theme actions. | Supplies proposed themes with support and uncertainty. | Nothing in this card. | [V10 §7K] [MAP C-7K] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece continuation entries

Both endpoints are named together; the earlier files remain unchanged.

| Using card | Defining or supplying card | Reciprocal entry | Source |
|---|---|---|---|
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | DESIGNED — USED BY continuation for Fed by: supplies the story-layer web that this engine realizes. | [MAP C-7B] [MAP C-ENGINE-C] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-7B.3 — Story-Layer Web | DESIGNED — USED BY continuation for Fed by: supplies the story dimension to be filled from story-bearing input. | [MAP C-7B] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Fed by: supplies the context for the story pass. | [MAP C-ENGINE-C] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-16 — Model Layer (§16) | DESIGNED — USED BY continuation for Fed by: supplies the mouth used to propose the reading. | [MAP C-ENGINE-C] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-7B.3.4 — Clash preservation | DESIGNED — USED BY continuation for Gated by: disagreeing tellings stay separate; neither repetition nor engine output selects a winner. | [V10 §7K] [MAP C-ENGINE-C] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-READ.10.14.6 — Engine C interface | ACCEPTED — USED BY continuation for Gated by: the telling-identity interface retains its acceptance, later integration and separate implementation-authorization conditions. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | C-READ — Reading record, validator, writer (§6B) | DESIGNED — USED BY continuation for Gated by: the proposed Engine C route uses the shared reading write boundary. | [MAP C-ENGINE-C] |
| C-ENGINE-C.1 — Story-layer engine pass | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — USED BY continuation for Fed by: supplies the async operation identity and worker route used for the pass. | [MAP C-ENGINE-C] |
| C-ENGINE-C.1 — Story-layer engine pass | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED — USED BY continuation for Gated by: one target and one declared pass yield one reading, and the proposal must pass acceptance. | [V10 §7G] |
| C-ENGINE-C.2.1 — Root evidence channel | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Fed by: supplies source roots for the story-reading pass. | [MAP C-ENGINE-C] |
| C-ENGINE-C.2.2 — Prior reading context channel | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Fed by: supplies prior reading context to the story pass. | [MAP C-ENGINE-C] [V10 §7G / STORY-LAYER EVIDENCE RULES] |
| C-ENGINE-C.3.3 — Insufficient root support | C-READ.10.3 — Reading and telling correspondence checks | ACCEPTED — USED BY continuation for Gated by: required semantic acceptance cannot be bypassed by stripping an invalid telling from a rejected proposal. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-ENGINE-C.4 — Story proposal acceptance boundary | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED — USED BY continuation for Gated by: acceptance depends on grounding, supplied context and the declared reading mode. | [V10 §7G] |
| C-ENGINE-C.5 — Complete semantic telling proposal | C-READ.10.1 — Complete telling-card payload | ACCEPTED — USED BY continuation for Fed by: defines the semantic fields and their separate mechanical counterparts. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2] |
| C-ENGINE-C.5 — Complete semantic telling proposal | C-READ.10.1.3.1 — Pass-local support selection | ACCEPTED — USED BY continuation for Fed by: constrains support claims to deterministic handles supplied with this pass. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §2.1] |
| C-ENGINE-C.5 — Complete semantic telling proposal | C-READ.10.3 — Reading and telling correspondence checks | ACCEPTED — USED BY continuation for Gated by: every semantic claim must pass acceptance and both representations must retain the same accepted content. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-ENGINE-C.5 — Complete semantic telling proposal | C-READ.10 — Reading-to-telling persistence | ACCEPTED — USED BY continuation for Changes: hands over the accepted semantic material for mechanical assembly and exact-payload persistence. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-ENGINE-C.6 — Engine C quarantine handoff | C-READ — Reading record, validator, writer (§6B) | DESIGNED — USED BY continuation for Gated by: the engine route goes through the shared writer, never a direct production write. | [MAP C-ENGINE-C] |
| C-ENGINE-C.6 — Engine C quarantine handoff | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED — USED BY continuation for Gated by: only a complete, integrity-valid set with valid completion proof permits telling-level semantic use. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-ENGINE-C.6 — Engine C quarantine handoff | C-READ.4 — Quarantine readings destination | DESIGNED — USED BY continuation for Changes: receives Engine C's planned story readings. | [MAP C-ENGINE-C] |
| C-ENGINE-C.6 — Engine C quarantine handoff | C-READ.10 — Reading-to-telling persistence | ACCEPTED — USED BY continuation for Changes: receives the accepted payload for the shared identity, correspondence and commit protocol. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | C-GOLD — Sealed gold sets v1, v2-B (§7C) | DESIGNED — USED BY continuation for Fed by: the separate story-gold dependency supplies the required Engine C benchmark; the built v1/v2-B sets alone do not fill it. | [MAP C-GOLD] [MAP C-ENGINE-C] |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | C-GOLD — Sealed gold sets v1, v2-B (§7C) | DESIGNED — USED BY continuation for Gated by: the protected build order requires story-bearing gold first and benchmarked evidence for wider-thread claims. | [MAP C-GOLD] |
| C-ENGINE-C.8 — Story-pass operation records | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: recorded evidence remains subject to access and authorization restrictions. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-C] |
| C-ENGINE-C.8 — Story-pass operation records | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — USED BY continuation for Gated by: identity and security authorization apply where required. | [MAP C-ENGINE-C] |
| C-ENGINE-C.9 — Inherited pass recovery | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — USED BY continuation for Fed by: provides the governing async operation and crash-recovery route. | [MAP C-ENGINE-C] |
| C-ENGINE-C.9 — Inherited pass recovery | C-READ.10.7 — Reading-to-telling recovery | ACCEPTED — USED BY continuation for Gated by: recovery must preserve the exact accepted payload and assigned identities. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §1] |
| C-ENGINE-C.9 — Inherited pass recovery | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED — USED BY continuation for Gated by: semantic fan-out stays blocked until completion and integrity are established. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-ENGINE-C.10 — Firmness proposal boundary | C-READ.10.1.12 — firmness_evidence_basis | ACCEPTED — USED BY continuation for Fed by: carries the observable, source-grounded basis for every non-omitted value. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] |
| C-ENGINE-C.10 — Firmness proposal boundary | C-READ.10.1.11 — firmness | ACCEPTED — USED BY continuation for Gated by: the established label meanings, omission rule and separate dimensions constrain the proposal. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] |
| C-ENGINE-C.11 — Theme proposal boundary | C-7K — Story Layer (§7K) | DESIGNED — USED BY continuation for Fed by: supplies tellings and the hybrid-theme organization in which proposals remain distinct from confirmation. | [V10 §7K / HYBRID THEME SYSTEM] |
| C-ENGINE-C.11 — Theme proposal boundary | C-READ.10.14.8 — Telling-to-theme reference | ACCEPTED — USED BY continuation for Gated by: a telling-level link uses the stable telling identity, retains root support and never copies or confirms the telling. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| C-ENGINE-C.11 — Theme proposal boundary | C-7K — Story Layer (§7K) | DESIGNED — USED BY continuation for Gated by: confirmation remains Ness's act, and proposed themes cannot silently shape later reading. | [V10 §7K / HYBRID THEME SYSTEM] |
| C-ENGINE-C.11 — Theme proposal boundary | C-7K — Story Layer (§7K) | DESIGNED — USED BY continuation for Changes: adds proposed navigational themes with their supporting evidence and uncertainty. | [V10 §7K / HYBRID THEME SYSTEM] |
| C-7B.3 — Story-Layer Web | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | DESIGNED — The existing CH02 Fed by link is reciprocated in C-ENGINE-C's USED BY table. | [MAP C-7B] [MAP C-ENGINE-C] |
| C-READ — Reading record, validator, writer (§6B) | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | DESIGNED — The existing CH03-b Fed by link is reciprocated in C-ENGINE-C's USED BY table. | [MAP C-ENGINE-C] [V10 §7G] |

## Appendix A carry-forward — this piece

| Part | Field | Occurrence | Value |
|---|---|---|---|
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | USED BY row 4 / Takes in there | 1 | NOT DECIDED |
| C-ENGINE-C.2 — Story-layer evidence channels | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.2.1 — Root evidence channel | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-C.2.1 — Root evidence channel | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.2.2 — Prior reading context channel | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.3 — Root-grounded telling | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.3.1 — Completed-prior-reading requirement | Fed by | 1 | NOT DECIDED |
| C-ENGINE-C.3.1 — Completed-prior-reading requirement | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.3.2 — No circular story support | Fed by | 1 | NOT DECIDED |
| C-ENGINE-C.3.2 — No circular story support | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.3.3 — Insufficient root support | Fed by | 1 | NOT DECIDED |
| C-ENGINE-C.3.3 — Insufficient root support | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.4 — Story proposal acceptance boundary | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | Gives out | 1 | NOT DECIDED |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.8 — Story-pass operation records | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.9 — Inherited pass recovery | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.10 — Firmness proposal boundary | Changes | 1 | NOT DECIDED |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | USED BY row 1 / Changes there | 1 | NOT DECIDED |

## Source coverage and explicit deferrals

| Source scope | Card or later piece | Coverage boundary |
|---|---|---|
| V10 status table and §7C Engine C | C-ENGINE-C; .7 | Story-layer engine remains unbuilt. Story-bearing gold precedes its construction/testing; neither accepted identity nor a design seal establishes a runtime engine. |
| MAP C-ENGINE-C, complete component card | C-ENGINE-C and all descendants | SMART owner; story-bearing input; evidence channels; quarantine; upstream/downstream interfaces; gates; inherited recovery; operation records; protected build boundaries. |
| V10 §7G, ONE READING PER PASS | C-ENGINE-C.1 | Single root, explicit mode, one separate reading per pass; no hidden second interpretation, overwrite or silent merge. |
| V10 §7G, STORY-LAYER EVIDENCE RULES through Audit trail | C-ENGINE-C.2–.3.3; .8 | Both channels; supporting root IDs; limited prior-reading use; circularity and unfinished-current-output prohibitions; weak-evidence outcome; supplied IDs preserved. |
| V10 §7G, confidence principle and acceptance interface | C-ENGINE-C.4; full validator and failure taxonomy left for CH05-a C-7G | Acceptance cannot be delegated to the mouth's confidence. Engine C hands its complete story proposal to the shared acceptance owner; full validator architecture remains with that owner. |
| V10 §7K, structured perspective, firmness and theme interfaces | C-ENGINE-C.5; .10; .11; existing C-READ.10.1 field cards | Engine proposal respects perspective separation, root grounding and uncertainty. Full Story Layer organization, schema and theme lifecycle left for CH06-b C-7K. |
| A2 §2.1 and §3 rule 7; §6 Engine C paragraph | C-ENGINE-C.5; .6; existing C-READ.10.1, C-READ.10.3 and C-READ.10.14.6 | Complete SMART proposal and pass-local handles; no mouth-generated system fields; shared persistence owns all mechanical identity, correspondence and recovery details already in CH03-c. |
| A2 §6 universal consumer rule | C-ENGINE-C.6; existing C-READ.10.10 | Stable telling identity is usable semantically only through the established complete/valid-set gate; identity is not truth or implementation authorization. |
| Firmness policy §§0–6 | C-ENGINE-C.10; existing C-READ.10.1.11 and C-READ.10.1.12 descendants | Six policy outcomes, honest field omission, evidence basis, qualitative hierarchy and separate dimensions; established label and signal cards reused. |
| A1 accepted design-closure §§5–7, verified through closure receipt | C-ENGINE-C.7; complete A1 gold contents and conditional root-pinning path left for CH03-l C-GOLD | Design-provenance seal does not establish real root IDs, runtime sealing or an executable benchmark. No case reconstructed from the historical blocker. |
| A1 historical blocker and unpinned-content acceptance receipt, whole | READ RECORD/status evidence only; remaining gold ownership in CH03-l | Earlier blocker and accepted replacement are distinct. Project history, audit workflow and package-completion procedures excluded from behavior cards under contract §1.3. |
| MAP C-ENGINE-C recovery and V10 §0B operation law | C-ENGINE-C.8; .9 | Actual pass, channel IDs, acceptance reasons and telling evidence recorded. Full async state machine left for CH05-b C-7GA; exact-payload telling recovery already in C-READ.10.7. |
| MAP C-GOLD protected build-order constraints | C-ENGINE-C.7; CH03-l C-GOLD; CH03-i C-ENGINE-AB.9 | Story gold first; live path before nightly deepening; wider/full-thread capability is a benchmarked future goal. No new scheduling or implementation mechanism. |

## Review of plain gates

| Card | Reason no other card is named |
|---|---|

## Coverage matrix — carried source inventory

The following inventory carries Chapter 3-a to 3-h placements and read status; Chapter 3-i's added placements are in Chapter 3-i's own inventory. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.


### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9. |
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
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: C-ENGINE-C.7. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
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
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
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
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
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
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.10. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces |
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
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |


## READ RECORD

The source files below match their Git blobs at `6a7160ba688ba4e433a31899162815df7e2bab17`. The four A1 records and the A2 and firmness closure receipts listed here were read whole. V10, the Map, A2's architecture and the firmness policy were reopened in the complete scoped passages listed in the source map; no new whole-file credit is claimed for those files. Earlier whole-read credit remains in the preceding chapters. The actual eight-case A1 content file remains pending for CH03-l; no case content is inferred from its receipts. Contract §§5–11 were reopened before writing; §11.3 is reopened after writing for the checks below. The lessons sheet and run instructions were read in full.

| Source file | SHA-256 |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | `f0ee0b07871373eb8dda0c83ab7186a51de35fe7ad0c5299bc41ae00078811b5` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | `8de0e340b6781f0d5bb31032d190bbd2eeedf58e9a4e98868c3d99a5d165716a` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | `40ed4f5ec457f03bb5bcb233e9ec0f05c36947fc2f8307c38e1ef826e4fb682d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | `6b5c6bcfd8ea7ddf73c85c60725146638345f8261da79c3c6b214b999a939709` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `a495871fba20ca03c19c024e77d1561cc90877ffa290c2ee19966c7026a21b2d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | `ce05634aea94f229346ee7b7fbbede3d83113c7c37292e50085d38597233ca64` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `88ef2b372ca99fe60b69a6a8891f6956ff6126ee634249bfb86f2f48839ccffa` |

Instruction fingerprints:
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` — SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` — SHA-256 `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` — SHA-256 `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |

### READ-folder files not yet read whole

The pending list contains 94 files after the whole-read updates recorded for this piece. Scoped rereads do not remove a pending entry; the ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
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
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 17 behavior cards reviewed; delivery and source-status records remain outside behavior boxes.
§1.4 every gap written as NOT DECIDED: PASS — 19 empty fields/cells and exactly matching register entries.
§1.5 conflicts marked, none resolved: PASS — 0 new conflicts; earlier conflict records unchanged.
§3 exactly one stamp per line: PASS — 17 headers, 168 populated fields and 36 USED BY rows checked; empty boxes use only NOT DECIDED.
§4 every behavior line cited in the exact format: PASS — 27 distinct citations resolve in pinned sections; all populated fields and USED BY rows cited; support reviewed manually.
§5.4 one name per thing: PASS — 17 non-colliding IDs, official names and established sub-part names checked.
§6 all template fields present, in order, for every part: PASS — 17 templates and 185 field lines checked.
§6.3 reciprocity within this chapter: PASS — 29 internal links reciprocated; 34 outward links and 2 earlier incoming links covered by 36 rows naming both ends.
§6.4 every decided detail written in, no citation used in place of content: PASS — All engine-specific Map obligations are represented. Telling-field atoms, semantic correspondence, commit/recovery, firmness labels and evidence signals reuse the established CH03-c cards; clash preservation reuses CH02. Full shared validator, worker, retrieval, Story Layer and gold mechanics are named deferrals.
§6.5 sub-parts recursed to the bottom: PASS — 17 cards; source-map scope and reuse of established atomic cards manually reviewed.
§9 coverage matrix rows added for every file used: PASS — 10 pinned source identities and corresponding coverage entries checked; current placement/deferral table included.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all behavior boxes reviewed; source-defined approval conditions are descriptions of the system boundary.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`. The lessons sheet and run instructions were read in full; contract §§5–11 were reopened before writing and §11.3 afterward. Other source reads are the scoped sections in the source map, without a new whole-file claim.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 17 |
| field_lines | 185 |
| populated_fields | 168 |
| not_decided_fields_and_cells | 19 |
| used_by_rows | 36 |
| relationships | 63 |
| internal_relationships | 29 |
| external_relationships | 34 |
| continuation_rows | 36 |
| plain_gates | 0 |
| step_cards | 8 |
| source_names_checked | 33 |
| unique_citations | 27 |
| source_identities | 10 |
| earlier_identities | 12 |
| pending_source_paths | 94 |
| built_field_lines | 0 |
| misfiled_scan_fields | 185 |
| empty_restriction_failure_gate_boxes_reviewed | 1 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 at writing; audit 1B later confirmed errors, corrected in round 4B |

Manual review accompanying the mechanical scan:

- Reviewed every authored claim against the reopened source passages. Engine C remains unbuilt; accepted A1 design closure is distinct from executable gold. A2 semantic fields and source-carried/system fields remain separate. No one-mouth-call limit is inferred from one reading per pass.
- Reviewed every box and USED BY row. The one empty failure box concerns the root channel: its cited passage prescribes a boundary but does not specify a separate failure mechanism. Known prior-output exclusion, weak-evidence outcomes, acceptance rejection and telling eligibility are filled explicitly.
- All engine-specific Map obligations are represented. Telling-field atoms, semantic correspondence, commit/recovery, firmness labels and evidence signals reuse the established CH03-c cards; clash preservation reuses CH02. Full shared validator, worker, retrieval, Story Layer and gold mechanics are named deferrals.
- Reviewed source-bound prohibitions, no formula phrasing, no project workflow in behavior boxes. The story-gold card records the behavioral prerequisite and the distinction between a design seal and runtime readiness.
- Checked scope, reused cards, no BUILT statements, source pin, incoming/outgoing continuations and read claims against the finished draft. No case content or root pinning is claimed.

All named source paths were checked at the fixed pin. Runtime/store names are checked against source documentation; this is not a live N.H filesystem check. P-MAIN has no direct step for this piece’s top-level engine; side-path placements continue in CH11. The wording scan covers the whole file. The count table is compared with a final recount after this block is appended.
