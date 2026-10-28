# N.H RECENT CONTINUITY NOTE — POST MASTER-17

**Purpose:** A compact handoff for a new ChatGPT or Claude conversation.

**Authority warning:** This file is **not** an architectural authority and does not replace the N.H Master.  
The current authority remains:

`NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`

Use this note only to explain what happened after that Master and where the work currently stands.

---

## 1. Current authority and file rules

- `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` is the current authoritative complete Master-17.
- The existing `NH_CHATGPT_PROJECT_HANDOFF_CLAUDE_S17.md` explains how Master-17 was created and audited.
- Do not overwrite Master-17.
- A future architectural adoption must create a new complete Master version.
- Split reader copies are reading aids only: **read from parts, edit the whole**.
- If any recent note conflicts with Master-17, the Master wins unless Ness explicitly adopts a later change.

---

## 2. Attention and Relevance Control — latest design status

After Master-17, Ness and Claude worked through the Attention and Relevance Control component. ChatGPT checked the resulting design.

**Current status:**  
**CORE CONCEPTUALLY DESIGNED, NOT BUILT, AND NOT YET ADOPTED INTO MASTER-17.**

It is a checked candidate for a future complete Master version.

### Main settled ideas

- Relevance is judged for a specific request and context; it is not a permanent hidden score attached to information.
- Relevance stays separate from truth, authority, currentness, privacy, and certainty.
- Simple structural conditions use deterministic gates.
- Graded judgments remain separate named dimensions with their own provenance rather than being collapsed into one secret score.
- Relevance is normally calculated when needed, with limited declared precomputation allowed.
- The component has a shared basic layer and a consumer-specific layer.
- Ness can inspect and directly correct a result for the current context.
- Reusable changes require a consequence preview and confirmation.
- Model-produced relevance judgments require validation and cannot silently exclude candidates at the first gate.
- Relevance results cannot write directly into the Living State Web.
- They may trigger a review, but they are not themselves evidence.
- Every relevance event records its request, purpose, context, producer versions, results, failures, unresolved items, and disagreements.
- Repeated similar corrections may cause N.H to suggest a shared mode change, but never apply one automatically.
- An unknown purpose type causes a halt and explanation rather than a guess.

### Remaining action

Ask Claude to integrate the complete checked Attention and Relevance Control design into a **new full Master candidate**, then audit it against Master-17 before adoption.

---

## 3. Local-first architecture clarification

N.H is normally local and offline.

### Normal operation

- The main model runs locally on Ness's PC.
- N.H's memory, records, permissions, evidence, retrieval, and functions remain local.
- Normal conversation does not use a cloud language model.

### Nightly research

Master-17 currently defines:

`Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate`

The resulting research is saved into N.H's local memory as dated readings.

The research does **not** train or become the mouth model.

### Phone access

The network is also used when Ness explicitly activates N.H's cloud tunnel for the phone model's three modes.

The cloud tunnel is not the normal operating state, and the mobile three-mode system is designed but not built.

---

## 4. What the model is supposed to do

Master-17 treats the language model as a borrowed, frozen, replaceable mouth.

N.H itself provides:

- personal memory;
- current research;
- source and date information;
- retrieval;
- truth and uncertainty boundaries;
- permissions;
- history;
- corrections.

The model's main job is to:

- understand the prepared context;
- reason across it;
- follow N.H's instructions;
- preserve uncertainty;
- explain the result clearly.

The practical principle is:

**Search first, word last.**

Because N.H supplies the personal and current information, it probably does not need to force a 70B model into normal operation merely to obtain more memorized knowledge.

A strong modern local model in roughly the 20B–30B range is the current practical target, but the final choice must be decided by N.H's sealed tests rather than parameter count alone.

---

## 5. Current model and hardware direction

This is a practical engineering direction, not an adopted Master-17 architectural rule.

### Model direction

The conversation selected **Dolphin 3.0 R1 Mistral 24B** as the first local mouth candidate to test because it appears close to N.H's local, replaceable, low-restriction requirements.

Before installation, the exact model files, runtime support, quantization, tool behavior, Hebrew quality, and refusal behavior still need to be verified.

It must be tested against:

- N.H sealed gold tests;
- Hebrew and English;
- ambiguous short replies;
- uncertainty and non-invention;
- structured outputs;
- low-restriction behavior;
- speed and context handling.

Changing the mouth does not change N.H's memory, truth rules, permissions, research pipeline, or authority boundaries.

### Hardware target

Ness's maximum total budget is **₪5,000**.

The practical target is:

- a tested used **RTX 3090 24GB**;
- a new, quality **850W power supply**;
- compatibility check and professional installation;
- full testing before payment.

The card must be tested for:

- recognition of all 24GB VRAM;
- memory errors;
- crashes and artifacts;
- core, hotspot, and VRAM temperatures;
- fan condition;
- physical damage or suspicious repairs;
- fit inside the case;
- correct power connections.

No advance payment.  
Payment only after the card passes a proper laboratory test.

A normal RTX 3090 is preferred over a 3090 Ti because the Ti adds heat and power use without increasing VRAM.

---

## 6. External-world understanding status

Master-17 already provides part of the foundation:

- multiple future input front doors such as text, image, video, audio, camera, and VR;
- separation between direct observation, reports, and inference;
- privacy and authority boundaries;
- the idea that N.H may react gently and allow Ness to correct it.

However, the actual external World Model is **not designed yet**.

Still open:

- how N.H identifies objects, people, movement, and events;
- how it keeps a continuing picture of the room;
- how camera and microphone information combine;
- how accidental gestures are separated from intentional ones;
- how it handles uncertainty and hidden objects;
- exact camera permission, retention, and deletion rules;
- the complete path from sensor observation to interpretation and response.

Plainly:

**The safety foundation exists, but the system that truly understands the physical surroundings still needs a full design session.**

---

## 7. Important future design tasks

These remain important future work:

1. Integrate Attention and Relevance Control into a new complete Master candidate.
2. Perform the final adoption audit of `NH_DECISION_DEFAULTS-S17_DRAFT.md`.
3. Design the external World Model and physical-surroundings understanding.
4. Design low-load behavior for sensory overload, panic, mental fog, or temporary shutdown.
5. Design biometric identity and security, including camera recognition, fallback PIN/password, and spoof protection.
6. Continue Interface, World, Voice, VR, and Simulation design without presenting open areas as completed.
7. Verify the chosen local mouth model by real N.H tests before making it permanent.

---

## 8. Working relationship and explanation rules

- Claude develops design.
- Ness and ChatGPT check it.
- Do not replace Claude's design unless Ness asks.
- Correct contradictions and precision problems without changing features.
- For N.H design explanations, use:
  - `[CHANGES FUNCTIONS — ...]`
  - `[DOES NOT CHANGE FUNCTIONS — ...]`
- Explain technical terms immediately in ordinary language.
- Keep related function changes compressed into simple sentences.
- When there is a genuine preference choice rather than a technical correction, ask Ness before deciding.
- Preserve Ness's authority and the append-only nature of N.H.

---

## 9. How to use this note in a new conversation

Upload:

1. `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`
2. this recent continuity note

Then say:

> Master-17 is the architectural authority.  
> The continuity note records recent work and candidate decisions after Master-17.  
> Do not silently treat the note as adopted architecture.  
> Use it to continue from the correct point, and ask before turning a candidate into a new Master version.

