# NH_DECISION_TRIAGE_AND_DERIVATION_RULE_v0_3_CANDIDATE.md

**What this file is.** The procedure Claude and ChatGPT follow whenever they investigate, prepare or propose an answer to an **open N.H decision**. Written by Claude on 2026-09-28 at Ness's request, from his principle of that day (§1).

**Status: CANDIDATE** until Ness adopts it. It never overrides the authority order (V10 → Decision Defaults S19 v2_2 → cursorrules → Companion v1; the Map is subordinate). It never takes acceptance, adoption or build authorization away from Ness. If it conflicts with an authoritative file or an accepted record, that file wins and this rule gets a new version. It is never edited in place.

**Version note (v0_2, 2026-09-28).** v0_1 (SHA-256 `5857e9c0ba367757894ba85559410fa42a526eba197f2fe3cdc4ce9d302a1532`; kept) was reviewed independently by ChatGPT on 2026-09-28 at commit `c0bbd08`. The review raised 17 points, and Claude checked the key claims against the repository. This version applies all 17:
- the recovery check first (§3)
- premise checks (§4)
- a new kind **E** for evidence that is still needed (§5)
- separate tests for D and M, including indirect effects (§5)
- no step limit (§5)
- a narrowed and extended Ness-only list (§6)
- independence and disagreement handling, and dependency rechecks (§7)
- approvals bound to the exact batch; approval is not any other gate (§8, §2)
- version rules (§9)

It also aligns the rule with the existing route file, which v0_1 missed (§0).

**Version note (v0_3, 2026-09-28).** v0_2 (SHA-256 `0cfdaec3b4fb7394bebf215a8c65559e4bbe311f9e5482f2399670541323c8d6`; kept) was reviewed by ChatGPT, which kept §2–§8 and asked for three changes. Claude checked them against V10, the B16 bridge closure record and the Working Map's Register A/B, and applies all three:
- **E is a waiting state, not a resolution.** An item keeps its real kind and owner while evidence is gathered; an N item stays Ness-only; the rule records what brings it back; and E never counts as a resolved hole (§5, §7.5). Settings the sources expressly delegate to build time are RECOVERED as delegated.
- An equivalent implementation choice inside a recorded intent can be M, unless a source reserves it to Ness (§6.12).
- A missing second review blocks bulk approval only; R and N questions still reach Ness individually (§7.1).

§10 also gains one sentence.

**What counts as an open decision:**
- a NOT DECIDED box in Master-21
- an "undecided implementation slot"
- a gap-decisions item
- an open item in the decision index
- a build blocker "blocked on Ness"
- any similar hole

---

## 0. Where this rule sits

`03_WORKFLOW/NH_MASTER-21_TO_FINAL_SYSTEM_DESCRIPTION_ROUTE_v0_2_CANDIDATE.md` (the "detailed route") records Stage 2: Ness resolves the holes through one growing **gap-decisions file**. Its §2.4 says that assistants **may investigate, gather evidence and propose**, that they may **not settle a new design decision**, and that **Ness's explicit answer is what is recorded**.

This rule describes *how* the assistants investigate and propose. It changes nothing in the detailed route. A batch approval that Ness gives under §8 is his explicit answer, and only for the exact items it names.

## 1. Ness's principle (2026-09-28)

Many small and medium decisions can be worked out by Claude or ChatGPT by reasoning from the related decisions and parts they connect to. Most of them change neither N.H's behavior nor its features. The assistants do that reasoning, prepare the answers, and **present them to Ness at the end** for approval, so that Ness spends his own decisions on what really matters.

## 2. What this rule does not do

- **Writing Master-21:** the writer never fills a NOT DECIDED box by derivation (contract v1_0 §1.4; writer lessons 1.1, a working file Ness keeps). Master-21 keeps its holes marked.
- **Auditing:** auditors check; they don't answer holes.
- **Source conflicts:** they are never resolved by an assistant (§6).
- **Separate gates:** approving an answer here does **not**:
  - accept a package
  - adopt a Master
  - integrate files
  - authorize building
  - authorize any protected operation

  Each of those stays a separate explicit act by Ness (detailed route §4; cursorrules).
- **Runtime validation:** this is a project-review procedure. Two agreeing assistants do not establish truth, and they do not replace N.H's own runtime checks.

## 3. Step 0: is the hole really still open?

Before an item is sorted or shown to Ness, run the recovery check of detailed route §2.3:
- the three recovery records named there
- the decision index, followed to its actual sources
- acceptance and closure records, and later decisions or supersession
- Master-21 itself

An answer that already exists is **RECOVERED**: it is recorded with its source and is **not** put to Ness as a new choice. Example: room-start questions that look open in older files are answered by accepted A19-RS.

## 4. Step 1: check every premise

- For every source a proposed answer relies on, confirm its **status** and **exact scope**.
  - A Master-21 card may carry CANDIDATE or INTENT material; its presence is not an approved decision.
  - A frozen candidate may have a valid acceptance receipt. The receipt counts, within its stated scope only. For example, the UE5 record accepts a direction, not the blueprint that came with it.
- Trace each derivation to the **underlying** sources, and keep their conditions.
- Proposed answers may **not** support each other in a circle.

## 5. Step 2: sort into one of five kinds

| Kind | Test | What the assistants do | Shown to Ness as |
|---|---|---|---|
| **D: required** | The approved decisions **require** this answer. "Compatible with" is not enough. | Derive it, with a complete, checkable explanation and a one-line summary. | One line in a batch |
| **M: equivalent options, AI-selected** | Every answer the approved decisions still permit has the **same effects** under §5.1. | Pick the simplest permitted answer and state why the options are equivalent. | One line in a batch, marked "AI-selected" |
| **E: waiting for evidence** (a state, not a resolution) | The item can't be answered yet: it needs measurement, testing, deferred work, or a blocked dependency first. | Keep the item's **underlying kind and owner** (D, M, R or N); an N item **stays Ness-only**. Record what evidence is needed, who or what produces it, and what brings it back for decision. Don't guess, and don't ask Ness to guess. E **never** counts as a resolved hole (detailed route §3.2). | A short waiting list, with its kind and owner shown |
| **R: real choice** | Answers the sources permit have different effects, and none is required. | Prepare the **real** options (as many as truly exist, never invented ones), what each changes, a recommendation, and the sources. | One by one |
| **N: Ness only** | Any item under §6. | Prepare it the same way as R. | One by one, flagged |

A setting the sources **expressly delegate** to build-time selection or calibration is RECOVERED as delegated, with the source and its conditions (for example V10 §25 "Build-Time Implementation Settings"). It is not E.

There is no step limit. A long, sound derivation can still be D, and a short one that hides a new decision is R.

**5.1 The equivalence test (for M).** Two answers are equivalent only if they don't differ in what N.H **does, says, stores, shows, refuses or asks**, or **whom it affects**. That includes indirect effects, failures and recovery, resource limits, and every operating condition the sources permit. A successful example or an unchanged screen does not prove equivalence; retrieval limits, retry timing and fallbacks can all change results. If unsure, the item is not M.

## 6. Ness only (kind N)

This list protects **new choices, and changes to existing ones**, within these subjects. It does not cover settled applications of them, or settings the sources explicitly delegate to build time; those are RECOVERED as delegated, or they are D or M. For example, V10 §25 "Build-Time Implementation Settings" leaves the maintenance timeout and the hardware key mechanism to build-time calibration and selection.

1. **Source conflicts**, and any answer that would override or reinterpret an earlier Ness decision.
2. **Privacy:** deletion, retention, sensitive data, what is held or shown.
3. **Identity, security and access:** speakers, biometrics, permissions, pairing, authority.
4. **Other people:** how N.H treats, records or reads anyone other than Ness.
5. **Wellbeing, health and emotional interpretation.**
6. **Money and legal commitments.**
7. **Autonomy:** anything N.H would do on its own, without asking, or outside the device.
8. **Permanent record meaning:** what is written into append-only stores (record shapes, identifiers, hashing, retention), and anything else that can't be undone.
9. **Fact versus interpretation, simulation versus reality, and evidence strength versus approval.**
10. **Meaning-dependent gold judgments, and the final adoption of any model.**
11. **Governance:** the authority order, stamps, adoption, and these rules themselves.
12. **New policy choices within Ness's recorded intents** (voice, phone app, vision, candor, security, reason-before-acting and others). Their settled applications are not re-asked. An implementation choice inside an intent that passes the §5.1 equivalence test can be M, **unless a source reserves that choice to Ness**. The line between policy and mechanics follows the Working Map: Register A (policy, Ness) and Register B (mechanics, preparable).

**Prohibitions stay prohibitions.** Behavior that an existing rule forbids is never presented as a selectable option just because the subject is on this list.

## 7. Safety rails

1. **Independence.** Claude and ChatGPT get the **same question and the same source versions**, in separate contexts, and neither sees the other's answer. Both first results are recorded before they are compared. If the second review is unavailable:
   - D and M items **cannot enter bulk approval**; they stay UNCHECKED.
   - R and N items still go to Ness **individually**, marked "second review: UNCHECKED".
2. **Disagreement.** Before escalating, check for different source versions, missed passages, scope mistakes, or wording that means the same thing. Only a remaining real difference becomes R. **An N item never drops to R**, whatever the assistants say. Only D and M items the assistants agree on go into bulk approval.
3. **Consistency.** Before a batch is shown, all its answers are checked against each other, against the decided material, and against the Master-21 cards they touch. Names and IDs are checked by script.
4. **Dependencies.** After any rejection, partial approval, reopening or changed source, recheck every answer that depends on it, across batches too. If Ness rejects A, an answer B that depends on A is no longer settled.
5. **Honest uncertainty.** When evidence is missing, the item is marked **E (waiting)** and keeps its underlying kind and owner. When an assistant can't tell whether the options differ, the item is **R**. Nothing is shown with more certainty than the reasoning supports.
6. **Nothing is built on an unapproved answer.** Every assistant answer is a proposal until Ness approves it (and see §2 for the separate gates).
7. **Origin is metadata, not a stamp.** In the gap-decisions record, each entry notes where its answer came from:
   - `DECIDED by Ness <date>`
   - `DERIVED (D), approved by Ness <date>, batch <id>`
   - `AI-SELECTED (M), approved by Ness <date>, batch <id>`
   - `RECOVERED from <source>`

   These notes never replace Master-21's stamps or the decision index's statuses, and they never appear in Master-21 behavior lines.
8. **Reopening.** Ness can reopen any answer. That creates a new versioned reconsideration. It does not promise to undo effects that have already happened in the real world.

## 8. Presentation and recording

- **Batches** aim for 20–40 items, grouped by part. That's a target, not a minimum; closely dependent items are kept together.
- **Each batch has a fixed identity:** an ID, a version, and a count by kind (RECOVERED, D, M, R, N, and E-waiting with each item's underlying kind). Every item has a stable gap reference and the part and field it affects.
- **D and M items** are one line each: the hole, the answer, the basis in a few words, and the kind. The full derivation stays attached. Ness answers "approve all", or "approve all except #…". **That answer applies only to that exact batch version.** It never carries over to a reordered or changed list.
- **R and N items** each get a short plain story: what the hole is, the real options, what each changes in N.H, the recommendation, and the sources. Ness answers item by item.
- **Recording** follows detailed route §2.5 (the gap, the IDs and location, the recovery checks and sources, the answer, the resulting rule, the dependencies, any supersession). Each entry also records its kind, its basis, its origin note (§7.7), the batch ID and version, and Ness's reply in his own words, with its scope. Existing NHD identifiers are kept. Every change is a new version of the gap-decisions file.

## 9. Versions and where this rule is read

- **Which version applies.** The rule in force is the **latest version Ness has adopted**. A newer candidate may be read, but it is not applied until Ness adopts it. A newer file name alone never activates a procedure.
- **Who reads it first.** Every chat that works on the gap-decisions file, the finished system description, the decision index, or a build round's decisions reads the version in force first.
- **Planned references,** each real only once actually installed:
  - this file in `05_ACTIVE_CANDIDATE/` of `nesgeva/NH-GOVERNANCE`
  - a pointer line in the Claude and ChatGPT project instructions
  - a copy in the Claude project files and the ChatGPT project sources
  - a pointer in the next version of the route note

## 10. Open item reported, not resolved

The review found a status mismatch. The Claude project instructions v1_4 (`06_OPERATIONAL_INSTRUCTIONS/`) say decision index v0_10 was accepted on 2026-09-17, while the v0_11 index file describes the index as not accepted. This rule doesn't settle which is right. It is for Ness. Reporting it is **not** a request to approve the index again.
