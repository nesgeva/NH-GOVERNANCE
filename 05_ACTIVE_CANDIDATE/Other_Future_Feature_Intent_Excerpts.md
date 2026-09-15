# כוונות עתידיות נוספות: יצירה, חיפוש ועזרה דרך מצלמה

EXACT SOURCE EXCERPTS — NOT A FULL DOCUMENT.

Source: `NESS_DESIGN_INPUTS/NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_1.md`

Source SHA-256: `900e4defa03ff21ceaadd6f2f7eff97dfbf584673b083b2884d6475b40eed10e`

Selection note: Feature families C-E, cross-feature links, global boundaries, and explicit non-decisions. Operational loop sections 0, 11 and 14 are omitted; this is not a full document.


## Exact excerpt: source lines 61–92

<!-- BEGIN EXACT SOURCE EXCERPT -->
# 1. Overall intent

I want N.H to grow beyond being only a memory-and-conversation system.

I want it to also become a system that can:

- experience and work with media with me;
- understand how music and media connect to my own inner meaning and creative work;
- understand the branching structure of how I think and converse;
- simulate possible next thought/conversation branches without pretending predictions are reality;
- help me navigate and understand the physical world in real time in a much later stage;
- become a serious creation workspace where I can actually make things with it;
- let me search my entire N.H memory through one powerful human-facing search surface.

These additions must still behave like N.H:

**N.H is my helper, not my decider.**

It may understand, connect, predict, simulate, prepare, search, compare, and suggest.

It must not silently turn:
- prediction into memory;
- interpretation into fact;
- similarity into identity;
- a draft into an accepted decision;
- a creation into an adopted rule;
- a media association into objective meaning;
- a proposed connection into a confirmed connection;
- a tool result into proof of success.

---


<!-- END EXACT SOURCE EXCERPT -->

## Exact excerpt: source lines 599–1244

<!-- BEGIN EXACT SOURCE EXCERPT -->
# 4. FEATURE FAMILY C — Live Physical-World Assistance Using Phone Camera + Location

## 4.1 Status and timing intent

This is a **far-future feature**.

It should not jump ahead of the current N.H build order.

I want it preserved in the design so it is not forgotten, but I do not want it to become a reason to derail or delay the core N.H system.

When this stage is eventually reached, I want the design process to be collaborative rather than an AI unilaterally filling in the experience.

---

## 4.2 Core capability

I want to be able to deliberately open a live session where my phone gives N.H temporary access to information such as:

- the current camera view;
- current location/GPS;
- possibly orientation/movement or other phone context if later justified and authorized.

Then N.H can help me understand or navigate the physical situation I am in.

Examples of the kind of experience I mean:

- "Where am I going?"
- "Which direction should I walk?"
- "What am I looking at?"
- "Where is the entrance?"
- "Which object is the one I need?"
- "Help me navigate this place."
- "Read/understand what is in front of me."
- "Stay with me while I move through this environment."

These are examples of capability, not a settled UI or autonomous-action policy.

---

## 4.3 Deliberate live session, not silent surveillance

The feature must be explicitly activated.

I do not want "camera access" to become:

- permanent background surveillance;
- hidden continuous recording;
- automatic uploading;
- automatic memory ingestion;
- silent location tracking.

A live assistance session and persistent recording are different permissions.

If N.H can answer a real-time question without permanently saving raw video/location history, that should remain a valid design direction.

---

## 4.4 Privacy of other people and places

The camera may see:

- strangers;
- family;
- private homes;
- documents;
- screens;
- addresses;
- faces;
- conversations;
- children;
- sensitive locations.

Therefore live visual assistance needs strong privacy handling.

The eventual design must distinguish at least:

- using a frame temporarily to answer me;
- storing a frame;
- storing extracted information;
- linking information into memory;
- recognizing a person;
- sharing anything externally.

Permission for the first must not silently grant the others.

---

## 4.5 Location is sensitive

Location must remain protected information.

The system must not turn a one-time request like:

> guide me to this entrance

into standing permission to record where I go.

Any historical location feature would need its own deliberate design and permission.

---

## 4.6 No false certainty

N.H must be able to say:

- "I can't see enough";
- "GPS is uncertain";
- "I may be identifying the wrong entrance";
- "the camera view is blocked";
- "I cannot safely tell from this image."

It must not invent physical certainty.

High-impact situations must remain governed by the normal N.H safety and permission rules.

---

# 5. FEATURE FAMILY D — General-Purpose Creation Workspace

## 5.1 Why this is different from the existing Creation concept

N.H already has important Creation concepts around recognizing and preserving creations such as:

- designs;
- ideas;
- rules;
- names;
- decisions;
- provisional creations.

I want to go further.

I want N.H to become an actual **place where I make things with it**, not only a system that notices that I created an idea.

The Creation Store and the Creation Workspace may connect, but they are not necessarily the same responsibility.

The live design process should reuse existing Creation architecture rather than replacing it.

---

## 5.2 What I want to create with N.H

Examples include:

- notes;
- outlines;
- plans;
- explanations;
- letters;
- scripts;
- screenplays;
- stories;
- project documents;
- design documents;
- specifications;
- presentations;
- structured research outputs;
- diagrams;
- images where a capable tool is available;
- data/artifact files;
- eventually software/code where I separately authorize that kind of work.

The important idea is:

**N.H can help produce a real working artifact, not only talk about producing one.**

---

## 5.3 Workspace behavior

I want to be able to work iteratively:

1. create something;
2. inspect it;
3. ask for a change;
4. compare versions;
5. preserve earlier versions;
6. continue later;
7. connect the work to its project/context;
8. deliberately decide when something is final enough for its intended use.

A later revision should not silently destroy the earlier version.

---

## 5.4 Draft is not decision

This is critical.

A document N.H helps me draft is not automatically:

- my settled belief;
- a confirmed N.H design;
- an accepted N.H rule;
- an adopted policy;
- permission to act;
- permission to build;
- a real-world message that has been sent.

For N.H project work in particular:

**creating a design artifact is not the same as accepting the design.**

The workspace must preserve that distinction.

---

## 5.5 Artifact provenance

A created artifact should be able to preserve useful history such as:

- project it belongs to;
- why it was created;
- source material used;
- which parts came from me;
- which parts were proposed/generated by N.H or a tool;
- revisions;
- explicit decisions that shaped it;
- current status;
- links to predecessor/successor versions.

The exact schema belongs to design work.

The meaning requirement is that N.H must not erase authorship/provenance merely because the final artifact reads smoothly.

---

## 5.6 Working with existing files

Eventually I want N.H to be able to help me work on existing artifacts as well.

Examples:

- read a document;
- suggest edits;
- create a new version;
- transform format;
- compare versions;
- update a project artifact;
- create a derivative file.

Existing file protection/version rules must still apply.

No silent overwrite should become the default merely because the Creation Workspace exists.

---

## 5.7 Code and executable work

Eventually, the workspace may include coding/tool-assisted building.

But:

**designing the Creation Workspace is NOT blanket permission for N.H to execute code or change my machine.**

Writing code as an artifact, running code, changing N.H, committing Git changes, and affecting external systems are different permission levels.

They must remain governed by the normal N.H action/authority system.

---

## 5.8 Connection to projects

I want a project to become a real working context.

A project may connect:

- conversations;
- memories;
- research;
- media references;
- files;
- drafts;
- decisions;
- unresolved questions;
- tasks/actions;
- versions.

The Creation Workspace should make it practical to move from:

> "I have an idea"

to:

> "Here is the actual evolving work."

without breaking N.H's distinction between memory, interpretation, proposal, decision, and executed action.

---

# 6. FEATURE FAMILY E — Unified Faceted Memory Search

## 6.1 The basic idea

N.H already has memory retrieval, semantic/positional context, browsing concepts, Person-Boxes, project views, current/history views, and other ways of reaching information.

I also want **one direct human-facing search capability across the complete usable N.H memory**.

I should be able to deliberately search rather than waiting for N.H to surface something.

---

## 6.2 Search dimensions

I want to be able to search/filter by useful dimensions such as:

- person;
- event;
- date or period;
- source;
- conversation/thread;
- project;
- theme;
- status.

Where existing N.H design already defines another appropriate filter, the design may reuse it rather than inventing duplicate categories.

The important capability is that filters can work together.

Example:

> Show me things connected to [person], from [period], in [project], where the status is unresolved.

The exact query language/UI is open unless already settled elsewhere.

---

## 6.3 Search across different kinds of N.H material

A unified search should be able to lead me to appropriate accessible objects such as:

- original roots/source material;
- readings;
- historical readings;
- story-layer material;
- Person-Box material;
- projects;
- creations;
- accepted connections;
- unresolved/proposed connections;
- operational history where I am permitted to view it;
- media references;
- action/result history;
- other future N.H object types.

The search system must not flatten all of these into the same thing.

A source record and an AI interpretation must remain visibly different types of result.

---

## 6.4 Exact source versus interpreted result

Search results should preserve the difference between:

- original material;
- N.H reading;
- human judgment;
- computed/current view;
- simulated material;
- unresolved material.

If I search for:

> "things where I felt abandoned"

N.H may find:
- exact statements where I said that;
- readings that infer something related;
- story-layer material;
- related events.

Those should not all be displayed as equally direct evidence.

---

## 6.5 Positional and semantic search remain distinct

The existing N.H distinction must remain:

- **positional context** = what actually occurred before/after/around an item;
- **semantic retrieval** = other things that appear related in meaning.

Unified search must not blur that.

If a result is semantically related, N.H should not present it as though it was part of the same original conversation.

---

## 6.6 Why a result matched

Where practical, I want the search experience to explain the basis of a result.

Examples:

- exact text match;
- person link;
- project link;
- date range;
- source;
- accepted connection;
- theme;
- semantic similarity;
- current computed relationship.

The system should not need to expose raw internal scoring.

The point is to avoid mysterious results that look authoritative merely because search returned them.

---

## 6.7 Privacy and permission before search

Search is not a bypass around privacy.

A powerful search interface must still obey:

- identity/access;
- private-material rules;
- sealed/restricted material;
- third-party protections;
- influence-removal rules;
- sensitive-data boundaries;
- explicit compartment rules.

"The information exists" does not automatically mean every search mode may display it.

---

## 6.8 Search must not change memory

Searching is read/retrieval behavior.

A search result must not become more true merely because it was retrieved.

Repeated searches must not turn one source into multiple independent pieces of evidence.

Opening a result must not silently accept, promote, merge, or confirm it.

---

## 6.9 Honest empty and failed searches

N.H must distinguish:

- nothing matched;
- results exist but are inaccessible under current permissions;
- search could not complete;
- an index/source is unavailable;
- only weak/uncertain semantic matches exist.

It must not fill an empty search with invented relevance.

---

# 7. Cross-feature connections I want preserved

The five feature families above should not become isolated apps inside N.H.

Where compatible with current architecture, I want them connected.

Examples:

## Media ↔ Creation

A musical moment can become a creative reference for a scene/project.

## Media ↔ Memory

A song may connect to a life period, person, event, or personal meaning.

## Media ↔ Search

I should eventually be able to find:
> songs/segments I connected to this character/project/theme.

## Branches ↔ Chat

The real branch structure comes from actual live conversation.

## Branches ↔ Search

I may want to find the point where one idea branched away from another.

## Branches ↔ Creation

A paused creative branch may later become a separate project idea or draft.

## Branches Simulation ↔ Attention/Context

Possible next branches may help N.H prepare context, but may never become facts.

## Camera/GPS ↔ Live Conversation

Physical-world assistance should feel like talking to N.H while N.H can temporarily see the same environment.

## Camera/GPS ↔ Memory

Persistent memory is a separate permission. A live visual assistance session does not automatically become a stored life record.

## Creation ↔ Search

I should be able to find drafts, versions, project artifacts, and the conversations/decisions that produced them.

---

# 8. Global rules these features must inherit

The live design process must preserve all relevant N.H rules, including at minimum:

## 8.1 Never-close-the-book

N.H interpretation remains revisable.

## 8.2 Ness is the decider

N.H may help, simulate, suggest, and prepare.

Ness owns meaning/policy/acceptance/adoption and real-world authorization where required.

## 8.3 Original material stays distinct from interpretation

A song, message, camera frame, conversation, or file must not be rewritten into an AI interpretation.

## 8.4 Simulation stays simulation

Predicted branches and imagined possibilities never become real events automatically.

## 8.5 Append/preserve history rather than silently overwrite

Changed meaning, changed drafts, changed associations, and corrections should preserve the earlier state where the governing system requires history.

## 8.6 Provenance matters

N.H should be able to answer:
- where this came from;
- who said it;
- what media/source it referred to;
- when the association was made;
- whether it was observed, imported, inferred, generated, simulated, or stated by Ness.

## 8.7 Privacy before convenience

A useful feature is not permission to weaken:
- identity;
- private access;
- third-party privacy;
- protected material handling;
- external-action authorization.

## 8.8 No permission expansion

Permission to:
- play media
does not mean:
- change my account.

Permission to:
- use camera temporarily
does not mean:
- record continuously.

Permission to:
- create a draft
does not mean:
- send/publish it.

Permission to:
- write code
does not mean:
- execute or deploy it.

Permission to:
- search memory
does not mean:
- expose every protected record.

## 8.9 No hidden duplication

If current N.H architecture already has the correct owner for part of these features, extend/connect that owner.

Do not create a parallel:
- memory system;
- connection system;
- creation truth system;
- permission system;
- privacy system;
- Person-Box system;
- simulation-to-reality shortcut.

---

# 9. What I am NOT deciding in this file

This file intentionally does **not** settle technical architecture that should be designed only after the current N.H sources are checked.

It does not decide:

- database schemas;
- exact record names;
- controlled IDs;
- API/provider choices beyond examples such as Spotify;
- exact UI layout;
- exact search syntax;
- final visualization of branches;
- storage engine;
- embedding model;
- music-analysis model;
- camera model;
- GPS framework;
- background-process architecture;
- latency targets;
- exact retention periods;
- exact provider terms/copyright handling implementation;
- final package boundaries;
- final build order unless already required by N.H dependencies.

Those are design/mechanical questions for the proper package.

If one of them is actually already settled by current N.H authority, preserve the existing answer.

---

# 10. Earlier wellbeing/de-escalation ideas — explicitly NOT promoted by this file

Earlier project discussions also contained a set of AI-proposed wellbeing/de-escalation ideas, including things such as:

- physiological sensor fusion;
- a clearance-cue detector;
- safe-approach/ally prompting;
- graduated safe modes;
- a multi-checkpoint re-read logger;
- an arousal-cost dashboard;
- a partial-uncertainty shortcut;
- ally-feedback capture.

**Do not treat those as Ness-approved feature intent from this file.**

They were previously described as proposed ideas requiring evaluation, and some involve health/physiological inference that would require especially careful real-world validation.

If Ness later wants any of them, they must be brought forward separately and checked against the existing Wellbeing/BOP/privacy design.

This file does not authorize or request their design.

---


<!-- END EXACT SOURCE EXCERPT -->

## Exact excerpt: source lines 1273–1298

<!-- BEGIN EXACT SOURCE EXCERPT -->
# 12. Feature-intent summary

The additional capability areas I want preserved for future N.H design are:

### A. Personal Media Meaning and Live Media Experience
A first-class music/media experience inside N.H: playback while talking, exact timestamp awareness, deep musical understanding, personal meaning, and project/scene/character links.

### B. Branches Simulation and Thought-Branch Navigation
Represent the real branching shape of my conversations and temporarily simulate possible next branches without treating prediction or unsent thought as reality.

### C. Live Physical-World Assistance
A far-future, deliberately activated phone-camera + location mode for real-time assistance in the physical world, with strict privacy and no silent persistent surveillance.

### D. General-Purpose Creation Workspace
A real place to make, revise, version, connect, and preserve documents and other artifacts with N.H, while keeping drafts separate from decisions, acceptance, execution, and authority.

### E. Unified Faceted Memory Search
One human-facing search surface over N.H that can combine person/event/date/source/conversation/project/theme/status and return original material, readings, projects, creations, and other accessible objects without flattening their meaning or authority.

---

# 13. Final intent sentence

**I want these features designed as natural extensions of N.H — not bolted-on apps — while keeping the same core N.H laws: preserve the real source, keep interpretations revisable, keep simulation separate from reality, protect privacy and permissions, connect everything honestly, and leave the final decisions to me.**

---

<!-- END EXACT SOURCE EXCERPT -->
