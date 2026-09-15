# כוונת תכנון: הסתעפויות מחשבה וסימולציה

EXACT SOURCE EXCERPTS — NOT A FULL DOCUMENT.

Source: `NESS_DESIGN_INPUTS/NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_1.md`

Source SHA-256: `900e4defa03ff21ceaadd6f2f7eff97dfbf584673b083b2884d6475b40eed10e`

Selection note: Feature-intent input, not accepted mechanics. Only product content is extracted; the source's operational loop instructions are excluded.


## Exact excerpt: source lines 388–598

<!-- BEGIN EXACT SOURCE EXCERPT -->
# 3. FEATURE FAMILY B — Branches Simulation and Thought-Branch Navigation

## 3.1 The basic idea

A large part of how I think is not linear.

A conversation may start with one subject, split into another, return to the first one, open a third idea, pause it, and later continue from somewhere much earlier.

I want N.H to understand this structure as **branches**, rather than forcing my thinking into one flat sequence.

There are two related but different capabilities:

1. **Branch Navigation** — understanding the branches that actually happened.
2. **Branches Simulation** — temporarily exploring where a branch might go next.

They must remain separate.

---

# 3A. Branch Navigation — the branches that actually happened

## 3A.1 Actual conversation/thought structure

N.H should be able to recognize and preserve structures such as:

- current branch;
- parent branch;
- child branch;
- sibling branch;
- temporarily paused branch;
- unresolved branch;
- returned branch;
- completed branch;
- abandoned branch where that status is actually known;
- branch reopened much later.

A branch may contain another branch, which can itself contain another branch.

The goal is to preserve the **real shape of the conversation and my thinking**, not just the chronological order of messages.

Chronology must still remain intact underneath.

Branch structure must be an additional connected view, not a rewrite of the original conversation.

---

## 3A.2 Returning to old branches

N.H should be able to understand things such as:

- "going back to what I said before";
- "about the other thing";
- "continue the earlier idea";
- "not this branch, the previous one";
- "we'll come back to this";
- a natural return to an older unresolved subject even without exact wording.

N.H may use evidence to propose that I returned to an earlier branch.

If it is uncertain, it must remain uncertain rather than forcing a merge.

---

## 3A.3 Several branches can stay alive

Leaving a subject does not necessarily mean I finished it.

The system should allow several branches to remain open simultaneously.

A branch should not be marked resolved simply because:
- time passed;
- another topic appeared;
- I stopped mentioning it;
- a model predicts that I am done.

This is especially important for long creative, emotional, technical, and planning conversations.

---

## 3A.4 Branch view

Eventually I want the user-facing system to be capable of showing the branch structure in a useful form.

That may later connect naturally to:
- the normal chat;
- memory browser;
- Ness's World;
- project views;
- creation views.

The exact visual form is not decided by this file.

The live design process should decide only what is necessary to make the capability coherent and leave presentation choices to the proper interface package where required.

---

# 3B. Branches Simulation — possible future branches

## 3B.1 Purpose

I want N.H to be able to temporarily explore **possible next branches** of a live conversation or thought process.

The purpose is to help N.H stay mentally ahead without pretending it can predict me.

It may use the confirmed current context to consider possibilities such as:

- I may continue the current subject;
- I may return to an older branch;
- I may need context from another project;
- a particular question may become relevant;
- two branches may be about to connect;
- information can be prepared in case the next confirmed turn needs it.

This is preparation and simulation.

It is not reality.

---

## 3B.2 Critical reality/simulation boundary

A predicted branch is NEVER my actual thought merely because N.H predicted it.

A prediction must not become:

- a real conversation event;
- a root representing something I said;
- a belief attributed to me;
- a confirmed creation;
- a decision;
- evidence that I intended something;
- a Person-Box fact;
- a real branch in conversation history.

Only what actually happens may become the real branch history.

The simulation may be wrong, completely.

That is normal.

---

## 3B.3 Unsent typing

The current N.H design must be checked carefully here.

My feature intent is **not permission for N.H to secretly read unfinished typing**.

Branches Simulation should work from confirmed, authorized context unless a separate later design explicitly establishes an opt-in draft/simulation surface.

The live loop must preserve any already-settled rule that unfinished typing is not observable.

Do not infer permission to inspect keystrokes, drafts, deleted text, or unsent messages from this feature.

---

## 3B.4 Temporary preparation

Branches Simulation may allow N.H to prepare temporary material such as:

- likely relevant context;
- candidate questions;
- possible connections;
- retrieval candidates;
- alternate response directions;
- reminders of unresolved parent branches.

Temporary preparation should disappear or remain simulation-only when it is not used, except for whatever minimal operational record N.H's general transparency rules require.

Simulation output must not gain evidentiary weight simply because it was generated.

---

## 3B.5 Prediction must not distort conversation

N.H must not try to force me toward the branch it predicted.

It must not:

- answer a question I did not ask;
- finish my thought for me as if known;
- treat its prediction as my intention;
- steer conversation merely to make its prediction correct;
- repeatedly surface predicted branches I ignored;
- claim it "knew" what I was going to say.

Predictions are tools for readiness, not control.

---

## 3B.6 Branches and memory

The design should connect Branch Navigation and Branches Simulation to existing N.H systems where appropriate:

- live chat;
- context retrieval;
- creation;
- attention/relevance;
- Living State Web;
- operational logging;
- Wonder/simulation boundary;
- memory browser;
- projects.

But it must preserve the core distinction:

**actual branch history = what happened**  
**branch simulation = what might happen**

---


<!-- END EXACT SOURCE EXCERPT -->
