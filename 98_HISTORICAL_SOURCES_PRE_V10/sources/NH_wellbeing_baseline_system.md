# N.H — Wellbeing & Behavioral Baseline System
*Designed June 18, 2026. Emerged from ChatGPT feedback discussion.*

---

## What this is

A self-monitoring layer that protects both N.H's data integrity and Nes's personal wellbeing simultaneously — not as two separate features, but as one unified mechanism. The core insight: REALITY is built from Nes's judgment. When his judgment is compromised, both need protecting at the same time.

---

## The core philosophy (critical — do not dilute this)

This system does NOT measure Nes against external standards, clinical definitions, or universal distress signals. It measures Nes against **Nes**. His own baseline. His own patterns. His own values as expressed through his actual behavior over time — not what he says he believes, but what he consistently does.

The system learns who Nes is at his most grounded, and watches for meaningful divergence from that.

---

## Why Nes can't be the validator

When Nes is off-baseline, his judgment about whether the baseline is correct is also off-baseline. You can't see the shape you're in from inside the shape. This is the same reason self-diagnosis is unreliable in medicine. So:

- Nes does NOT approve or reject the baseline
- Nes does NOT decide if the system's assessment is correct
- The system validates itself against **internal consistency across time** — not against Nes's current opinion

This is not a limitation. This is the design. It's the only version that actually works.

---

## How the baseline gets built (passive, not written)

Nes does not write a constitution or define his values in a single session. That approach fails because:
- It may never get written
- A single session may not represent a truly clear state
- The stated version of values differs from the behavioral version

Instead, the system builds the baseline from behavior:
- Every REALITY promotion decision
- Every SIMULATION rejection
- Every conversation pattern
- Every type of question asked
- Every decision made across all sessions

Over time, consistent patterns emerge. These patterns *are* the baseline. Not declared values — demonstrated values.

**Periodic surface:** Monthly, the system generates a short summary of observed patterns. Nes can read it, make small corrections if something feels wrong, but cannot override the statistical picture — only refine it at the edges. The system decides if the correction is consistent with the broader pattern.

**Compounds over time:** More accurate at 6 months than at 1 month. More accurate at 1 year than at 6 months. The data does the work, not the complexity of the model.

---

## What triggers the system

### Physical triggers
Standard rate-limiting and safety thresholds — similar to how other well-designed AI systems handle physical wellbeing signals. Binary and visible. Either you can or you can't.

### Mental/behavioral triggers
This is the novel part. The system watches for:
- Actions that contradict values Nes consistently demonstrates
- Decision patterns that diverge from established baseline
- Language and reasoning patterns shifting in Nes-specific ways
- Behavior in one type of context contradicting behavior in another type of context
- Sustained divergence across multiple sessions (not a single bad day)

**Important:** A single session of divergence = noise. Sustained pattern across multiple types of interactions = signal. The threshold needs tuning once real data accumulates.

The specific patterns that constitute warning signals will be defined and refined over time as the system learns. They cannot be fully specified in advance — they emerge from the data.

---

## What happens when triggered (tiered response)

**Tier 1 — Silent flag:** System logs the divergence internally. No action taken. Monitoring intensifies.

**Tier 2 — Mirror signal:** System surfaces something to Nes directly. Not an alarm. A mirror. Something like: "Here's what I'm noticing. Here's how it compares to your baseline patterns. Are you aware of this?" Informational only — Nes can continue normally.

**Tier 3 — Queue throttling:** REALITY promotion slows. New records still enter SIMULATION normally. Queue builds but integrity is protected.

**Tier 4 — REALITY freeze:** REALITY promotion pauses entirely. Dry mode and research still work fully. N.H still functions as a thinking partner. Only REALITY growth stops.

**Unlock mechanism:** Upload of a document (psychiatric or medical appointment record) that the system treats as a verified good-state calibration point. Nes still does all the actual reviewing — the document is a forcing function and calibration anchor, not proof to anyone else.

---

## The psychiatric appointment as calibration anchor

This is more than an unlock key. It's a periodic external reference point — a moment where someone qualified looked at Nes and said "this is a good-state period." The system treats these timestamps as verified ground-truth reference points for the baseline.

Over time, the system can compare current patterns against the baseline established during verified good-state periods. This solves the hardest problem: if Nes has been in a compromised state for long enough, that state becomes the baseline. The appointment anchors prevent the baseline from drifting entirely into a compromised state.

---

## The one honest limitation

The system can validate internal consistency — "these patterns held across 6 months." It cannot validate whether those patterns represent a *healthy* version of Nes or a *consistently unhealthy* one. The appointment anchors are the solution to this. They are not optional — they are the only external reference in an otherwise fully self-referential system.

---

## Why this is architecturally clean

- No second person ever touches REALITY — sovereignty is preserved
- No external standard defines what "wrong" looks like — it's always Nes vs. Nes
- The gate is still only Nes — the system just adds conditions on when the gate opens
- Dry mode and research always work — the system never becomes useless
- Gets more accurate over time — compounds rather than degrades

---

## Implementation notes (for Cursor, when the time comes)

**Data sources for baseline engine:**
- `.nh_memory_store.jsonl` — promotion decision history
- `.nh_simulation_graph.jsonl` — rejection patterns
- Conversation logs — language and reasoning patterns
- Session metadata — timing, frequency, types of queries

**New record type needed:**
- `CALIBRATION_ANCHOR` — psychiatric/medical appointment document, timestamped, stored in REALITY, used as ground-truth reference by baseline engine

**New file (do not build until pipeline is complete):**
- `nh_baseline_engine.py` — pattern analysis, divergence detection, tier triggering
- This touches REALITY indirectly (reads patterns, triggers freezes) — treat as a Protected File when it exists

**Build order:** This comes AFTER the search pipeline is complete and stable. Do not start this until the pipeline is running nightly and the review queue has been healthy for at least a month. Baseline engine needs real data to work — building it before data exists is building an empty shell.

---

## Why this is novel

Behavioral baseline monitoring exists in cybersecurity (detecting account compromise). Longitudinal self-modeling exists in academic psychology research. Using a system's own decision history as training data for a model of the owner's judgment — that specific combination, for this purpose, for one person's sovereign AI — is a new application of existing ideas.

It is completely codeable with existing technology. Every component has a Python library. The sophistication comes from the design, not the implementation complexity.

---

## Status

Designed. Not yet built. Deliberately deferred until the search pipeline is complete and producing real data.
