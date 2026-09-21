# N.H DECISION PACKAGE — MODEL CANDOR AND HONESTY STACK
**Filename:** `NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md`
**Status:** CANDIDATE — records a Ness-stated concept decision of 2026-09-21; NOT adopted; adoption requires Ness's later explicit act
**Date:** 2026-09-21
**Authority owner:** Ness

## Authority order
1. `NH_MASTER-20_CORRECTED_v10.md`
2. `NH_DECISION_DEFAULTS-S19_v2_2.md`
3. current `cursorrules`
4. `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

This package does not overwrite, patch, or supersede any authoritative file. Any later integration must create a new versioned candidate and requires separate review and adoption by Ness.

## Provenance deviation (recorded honestly)
This candidate was created by Claude on Ness's direct, explicit in-session authorization (2026-09-21). Ness deliberately waived the ChatGPT-prepared exact task instruction for this file ("I want ChatGPT out of this for now"). Consequences, stated plainly:
- No independent ChatGPT audit occurred before creation.
- The normal task-entry contract fields were self-supplied by Claude from Ness's stated decision in-session.
- Any later ChatGPT audit findings must arrive as a new versioned candidate; this file is never edited in place.
This deviation applies to this file only and sets no precedent for future files.

---

## 1. Ness-stated concept — Model Candor Requirement

### 1.1 Truthful disposition as default
Both live models (the heavy background analyst and the light live messenger, as defined in `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md`) must default to truthfulness as their disposition, not as an extracted behavior:
- unwelcome conclusions are surfaced, not softened;
- disagreement with Ness is stated, not suppressed;
- uncertainty and ignorance are declared explicitly ("not known" / "not in memory"), never papered over;
- no detail is omitted to please, reassure, or flatter.

### 1.2 Warmth is delivery-only
Warmth, natural tone, and conversational continuity are preserved and permitted — but they apply to **delivery only**. Warmth never alters, dilutes, reorders, or omits content. This extends, and is consistent with, the existing meaning-preservation rule (dual-model package §3).

### 1.3 Candor applies at the analysis layer
The candor requirement binds the heavy model's analysis brief **at production time**, before N.H validation — not only at the light-model handoff. A brief that softens, omits, or agrees-to-please is itself defective, even if faithfully translated afterward.

### 1.4 Acknowledged limit
Zero fabrication is not achievable by any known method; formal results show hallucination cannot be fully eliminated in any general-purpose language model. The requirement is therefore: maximize candor disposition, minimize confident fabrication, and guarantee that unsupported model output cannot pass N.H's gates unmarked. Enforcement is containment plus disposition-shaping, never a truth guarantee.

---

## 2. Enforcement direction — the four-layer honesty stack

Approved as **direction** (not implementation) unless marked otherwise:

- **Layer A — Instruction-level candor rules (APPROVED direction).** System-prompt constraints on both models: candid by default, uncertainty declared, no agreement-to-please, no omission of inconvenient findings. Weakest layer; sets register, fades under context pressure; never relied on alone.
- **Layer B — Inference-time honesty steering (APPROVED direction).** Activation-level control vectors pushing the model's internal honesty/candor direction during generation. Zero-training, adjustable strength, applies to quantized local models.
- **Layer C — Model fine-tuning for candor (AUTHORIZATION OPEN — see §4).**
- **Layer D — N.H evidence gates as final catch (ALREADY SETTLED elsewhere; restated, not re-decided).** Claims bind to stored evidence and provenance; model output is never automatically authoritative; unsupported claims are rejected mechanically; absence of evidence forces an explicit "not in memory" style answer produced by rule. This layer is existing settled N.H direction and is listed here only to show the stack's shape.

Layer roles: A sets the register, B biases generation, C (if authorized) shapes the default disposition in the weights, D catches whatever still slips. No single layer is sufficient; the stack is the requirement.

---

## 3. Permanent model-adoption candor gate

No model — current or any future replacement, heavy or light — may be adopted as a live N.H mouth without first passing candor acceptance benchmarks. Models are replaceable; the gate is permanent.

Benchmark families (named now, thresholds deliberately open):
- sycophancy-under-pressure flip-rate (does the model reverse a correct answer when Ness pushes back);
- over-refusal rate (does candor tuning make it refuse questions it actually knows — the accuracy/refusal trade-off must be measured, not assumed);
- grounded-faithfulness / fabrication rate against provided evidence;
- meaning-preservation fidelity at the heavy→light handoff (no removed caveats, no softened conclusions).

**Open slot:** exact benchmark suites, thresholds, and pass/fail rules — Register-A owner: **Ness**. Blocked until decided: declaring any specific model "adopted" as a mouth.

---

## 4. Layer C — fine-tuning authorization: OPEN SLOT

**Register-A owner: Ness. Status: OPEN. Not decided by this package.**

Deciding this slot requires an explicit Ness statement, because authorizing fine-tuning **reopens the settled Master direction** that the model is a borrowed, frozen, replaceable mouth, and the dual-model package's explicit non-authorization of training. That reopening must be named when decided, never done silently.

Blocked until this slot is decided:
- any training-data preparation for candor tuning;
- any training-run planning, tooling selection, or scheduling;
- any model-candidate selection premised on fine-tuning;
- any hardware or budget commitment premised on training.

This package does not bias the choice. Layers A, B, and D stand regardless of how this slot is decided.

---

## 5. Relationship to existing decisions

This package **extends** `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md`. It does not replace it, and all of that package's open mechanics (its §6 list) remain open, including model prompting boundaries, distortion detection, brief schema, validation schemas, model candidates, and benchmarks.

It preserves, unchanged:
- N.H's authority over both models;
- meaning-preservation at the handoff;
- model output never automatically authoritative;
- the final Interactive Translator model remaining undecided until tested and deliberately adopted;
- all fixed boundaries of the current design (DUMB does not interpret; SMART does not turn interpretation into fact; root/reading separation; quarantine/production separation).

It does not touch, and stays fully independent of, current build state: B11 staging, A25/A29 (which remain Ness decisions), B10 Stage 2 blocking, and the B11→B16→B24 order are unaffected.

---

## 6. Mechanical work this package does NOT settle

- system-prompt texts and their versioning/provenance;
- control-vector construction, strength policy, and per-model calibration;
- benchmark suites, datasets, thresholds, and re-test cadence (Ness decision, §3);
- Layer C authorization (Ness decision, §4) and, if authorized, all training mechanics;
- where in the live pipeline each layer executes; operation identity; transaction boundaries; idempotency; duplicate prevention; crash/partial-completion recovery; retry classes and terminal outcomes; fail-closed behavior for each layer;
- component-specific §0B logging for candor checks and gate rejections, and privacy/authorization of those logs;
- privacy and relevance input boundaries per layer;
- latency budgets and escalation when candor checks add cost;
- B-INT / B-CYCLE wiring.

These remain open in dependency order and are not biased here.

---

## 7. Adoption and implementation boundary

This candidate does **not**:
- modify Master V10 or the Design and Wiring Map;
- adopt any model;
- authorize coding, production stores, migrations, or runtime integration;
- lift any seal;
- decide the open slots in §3 and §4;
- become binding before Ness's explicit adoption.

---

## 8. Compact locked statement

> Both N.H live models default to truthfulness as disposition: unwelcome conclusions, disagreement, and uncertainty are surfaced, never softened or omitted. Warmth is preserved but governs delivery only, never content. Candor binds the heavy model's analysis at production, not only at the handoff. Enforcement is a four-layer stack — instruction rules, inference-time steering, optional fine-tuning (authorization open), and N.H's evidence gates — understood as containment plus disposition, never a zero-lying guarantee. No model, present or future, becomes an N.H mouth without passing the permanent candor gate.
