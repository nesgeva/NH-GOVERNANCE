# N.H PROJECT HANDOFF — WHERE WE LEFT OFF WITH CLAUDE

## Purpose of this file

This file is a continuity note for ChatGPT inside the N.H project.

It explains what Claude was asked to do, what was completed, which files now matter, what must not be changed accidentally, and how future work should continue.

This is **not** an architectural authority.  
The complete N.H Master remains the source of truth.

---

## 1. What Claude was originally asked to do

Claude was instructed to create a new complete Master-17 without overwriting any earlier Master.

The task was to use the previous authoritative Master and the S17 design discussion to consolidate the newly designed areas, including:

- Catalog Front Door
- Pre-ingest holding area
- Context Retrieval
- Meaning Engine Interior
- Reading Proposal Acceptance Check
- Model confidence as metadata, not authority
- Story-layer evidence rules
- Reread Lifecycle
- View Layer
- Contradiction and Clash Handling
- Story Layer
- Person-Boxes
- Computed View
- Living State Web
- Action Surfacing
- Action-Result Return Path
- Permission and Authority Boundaries
- Authority Violation and Correction
- Privacy, Deletion, and Sensitive-Data Handling
- Interface, World, Voice, VR, and Simulation design

Claude was also told to preserve the earlier source files and produce a new version rather than editing them in place.

---

## 2. What happened after Claude produced the full draft

Claude produced a large full S17 draft.

ChatGPT then audited it in this order:

1. document and consistency issues;
2. preservation of the new concepts;
3. overall correctness across status, architecture, history, and cross-references.

The first full draft contained several real problems, including:

- build-script debris left inside the Markdown;
- inconsistent component statuses;
- privacy wording contradictions;
- causal overstatement in result states;
- View Layer / Computed View ordering ambiguity;
- mutation-like wording in an append-only architecture;
- pre-ingest visibility ambiguity;
- interface/world manipulation ambiguity;
- stale or overly absolute model wording;
- several smaller cross-section inconsistencies.

ChatGPT corrected those issues without intentionally changing N.H features.

A second consistency pass then corrected the remaining known issues.

---

## 3. Current authoritative Master

Treat this file as the current authoritative Master-17 unless Ness explicitly says otherwise:

`NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`

Source SHA-256 recorded during generation:

`cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152`

Important rules:

- Do not silently overwrite this file.
- Any future architectural update must create a new complete version.
- The previous Master remains preserved.
- Built claims still require disk verification before code work.
- Open or partial areas must remain labeled honestly rather than being presented as complete.

---

## 4. AI reader copies

The Master was split into smaller derived reader copies for focused work with Claude or ChatGPT:

- `NH_MASTER-17_00_INDEX_STATUS.md`
- `NH_MASTER-17_01_FOUNDATION_BUILT.md`
- `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md`
- `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md`

These are reading aids only.

### Usage rule

**Read from parts. Edit the whole.**

Use the reader copies for focused conversations, but never edit them independently.

For focused work:

- upload `00_INDEX_STATUS` and the relevant part.

For whole-system work:

- use the complete authoritative Master.

Whole-system work includes:

- architecture audits;
- contradiction checks;
- adoption decisions;
- defaults regeneration;
- build-order decisions;
- creating a new Master version;
- checking whether a new concept fits the entire system.

If the complete Master changes, regenerate the reader copies from the new Master.

---

## 5. Current Decision Defaults state

A new file was generated:

`NH_DECISION_DEFAULTS-S17_DRAFT.md`

It was regenerated from the corrected complete Master-17 rather than lightly patching the S16 defaults.

It includes updated guidance for:

- what is settled;
- what must not be re-asked;
- what still requires Ness's decision;
- session authority;
- artifact delivery;
- external action approval;
- privacy defaults;
- S17 component statuses;
- genuinely open forks.

Its current status is still:

**DRAFT**

Before calling it authoritative, compare it directly against the complete Master-17 and perform a final adoption audit.

The Master always wins if the defaults conflict with it.

---

## 6. Important S17 precision rules that must be protected

Future Claude or ChatGPT work must not regress these corrections:

- S17 did **not** finish every part of N.H.
- S17 completed the core conceptual architecture of the major components addressed during the session.
- Several larger areas remain open.
- Living State Web is **partially conceptually designed, not built**.
- Privacy, deletion, and sensitive-data handling are **partially conceptually designed, not built**.
- Attention and relevance control are not designed.
- Wonder/simulation is concept-level only; the mechanism is not designed.
- The World Model is not designed.
- The connected end-to-end cycle is identified but not designed.
- Engine B scored 6.5/7 on the tested setup.
- That result does not prove a universal 8B ceiling.
- The cause of the remaining miss was not isolated.
- Model capability, prompt framing, context format, and run variance remain possible contributors.
- Model confidence is metadata, not authority.
- Positional and semantic retrieval must remain separate and labeled.
- Story-layer root evidence and prior-reading context must remain separate.
- Circular derived support is forbidden.
- Success, partial success, and failure must not silently establish causation.
- Observed outcome, proposed action relationship, and Ness's judgment remain separate.
- History is append-only; changes normally create linked new events or versions.
- Held pre-ingest raw content must not influence semantic systems unless a future authorized inspection mode is explicitly designed.
- World manipulation is presentation, navigation, or simulation-only by default.
- World interaction must not silently rewrite underlying records or execute external actions.
- Private access for Ness is open by default unless an explicit restriction applies.
- External exposure and secondary uses are restricted by default.
- Model-provider refusals are mouth limitations, not N.H privacy rules or truth judgments.

---

## 7. How to handle future Claude output

When Ness sends a new Claude-produced N.H file, review it in this order:

### First: issues

Check for:

- contradictions;
- stale statuses;
- omitted sections;
- duplicated rules;
- accidental build commands or procedural debris;
- broken cross-references;
- unsupported certainty;
- silent mutation of append-only objects;
- provenance mistakes;
- changed historical logs;
- inconsistent filenames or version claims.

### Second: concept preservation

Trace each affected concept and determine whether it was:

- preserved accurately;
- weakened;
- overstated;
- moved incorrectly;
- merged with another concept;
- contradicted;
- omitted;
- accidentally turned into a built feature;
- accidentally turned back into an undesigned feature.

### Third: complete consistency

Check agreement among:

- the authoritative status table;
- the component body sections;
- the open/next list;
- historical and correction logs;
- closing principles;
- Decision Defaults;
- reader copies, if regenerated.

Do not rewrite or expand the design unless Ness asks.  
First report what happened to the existing design.

---

## 8. Rules for asking Claude to make future changes

When Claude is asked to update N.H:

- Use the complete authoritative Master as the direct base.
- Never use only a split reader file as the base for a new Master.
- Create a new complete version.
- Never overwrite the existing authoritative Master.
- Preserve all settled features unless Ness explicitly changes them.
- Correct wording or consistency without inventing new architecture.
- Mark conceptual, partial, built, planned, and open statuses precisely.
- Keep historical logs historical.
- Add a new correction/change log for the new version.
- Deliver an actual complete file, not only a patch or summary.
- Treat the result as a candidate until Ness reviews and adopts it.

---

## 9. Current practical next step

Claude's Master-17 consolidation task is complete.

The next unfinished documentation task is:

**Audit `NH_DECISION_DEFAULTS-S17_DRAFT.md` against `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`, correct any mismatch without changing features, and then let Ness decide whether to adopt it.**

Do not ask Claude to rebuild Master-17 again unless Ness explicitly wants a new version or discovers a real issue.

---

## 10. Compact continuation instruction for ChatGPT

When this project resumes, follow this instruction:

> The current complete architectural authority is `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`. The split files are reader copies only and must never be edited independently. Claude's Master-17 consolidation is finished. Preserve the corrected S17 design and statuses. The current pending documentation task is to audit and, if necessary, correct `NH_DECISION_DEFAULTS-S17_DRAFT.md` against the complete Master before adoption. For any future Claude output, inspect issues first, then concept preservation, then whole-document consistency. Never overwrite an authoritative file; create a new complete version.
