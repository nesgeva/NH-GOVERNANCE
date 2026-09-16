# N.H — Personal Idea Note: VR World, Rooms, and Offline AI Creation

**Filename:** `NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`  
**Status:** `TEMPORARY PERSONAL IDEA / DESIGN-INPUT NOTE — NOT AUTHORITY — NOT AN A19 CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT INTEGRATED — NOT IMPLEMENTED`  
**Owner of the idea:** Ness  
**Date preserved:** 2026-08-03

---

## 1. The idea in simple words

Ness wants **Ness's World** to become a real interactive three-dimensional world that can be entered through VR, while still being usable without VR.

Inside it, Ness could:

- enter existing virtual rooms or worlds;
- make his own rooms;
- ask N.H to build or change rooms;
- move, grab, open, reshape, combine, separate, summon, or dismiss things;
- speak naturally to N.H while inside the world;
- use memories, ideas, projects, people, places, imagined scenes, and simulations as material for spaces;
- keep the entire creative system local and offline wherever practical.

The strongest practical form of the idea is:

> **A local “world workshop” where N.H can use Blender or similar offline creation tools to prepare rooms, objects, environments, and changes, while a separate real-time engine lets Ness walk through and interact with them in VR or on a normal screen.**

This is not merely a separate VR feature. It is a possible practical form of the already-planned **A19 / Ness's World** experience.

---

## 2. Where this belongs in the existing N.H design

### Main owner: A19 — Ness's World / interface

This idea directly belongs under **Bundle 7, A19** because A19 already owns:

- rooms and spaces inside Ness's World;
- VR and other interaction methods;
- simulation and replay experience;
- physical movement and manipulation;
- how N.H appears and speaks inside the world;
- the visual language of the world;
- camera and VR privacy boundaries;
- accessibility alternatives.

A19 is still open and not accepted, adopted, integrated, or implemented. This note preserves a new design input for that future work; it does not settle A19 by itself.

### Existing A19 rules this idea must preserve

The following are already settled and are not reopened here:

1. The whole environment is called **Ness's World**.
2. The world itself begins blank and grows from Ness's life.
3. Opening Ness's World requires identity verification, N.H asking whether to open it, and a separate confirmation from Ness.
4. A new individual room may begin **blank, built from memories, or mixed**.
5. Ness's direct room-start choice overrides N.H's automatic choice.
6. A clear voice command from Ness changing the room start applies immediately without another confirmation.
7. Moving, merging, splitting, reshaping, or rewinding things in the world changes presentation, navigation, or an explicitly labelled simulation by default. It does not silently rewrite N.H memory, people, evidence, permissions, deletion state, or outside systems.
8. Simulation must not begin secretly.
9. Replay and generated simulation remain visibly different.
10. The plain white wooden door remains the normal doorway between spaces.
11. N.H remains available inside the world as a movable or summonable presence, with no single fixed visual form.

---

## 3. Refined concept: the Local Embodied World Workshop

**Working description, not a final feature name:**

The **Local Embodied World Workshop** would be the part of Ness's World that lets Ness and N.H create, import, arrange, revise, branch, and enter interactive rooms.

It could support four room sources:

### A. Existing room or world

Ness imports a room, environment, model, or world that already exists and is legally available for him to use.

N.H may help organize, adapt, optimize, label, or connect it, but the original source and licence stay visible.

### B. Ness-created room

Ness creates the room directly through voice, VR movement, desktop tools, sketches, references, or manual Blender work.

### C. N.H-created proposal

Ness describes a room and N.H prepares a proposed version locally. It remains a proposal until Ness enters, previews, accepts, changes, branches, or rejects it.

### D. Mixed room

Ness starts from an existing or memory-built room and changes it together with N.H. The room may combine imported objects, Ness-created objects, N.H-generated proposals, memory references, and clearly labelled simulation material.

These four forms fit the already-settled room-start choices: blank, memory-built, or mixed, with Ness always able to override N.H.

---

## 4. Practical offline tool direction

### Blender's likely role

Blender is a strong local creation tool for:

- modelling rooms and objects;
- changing geometry and materials;
- arranging scenes;
- animation;
- lighting;
- preparing reusable assets;
- exporting rooms and objects to a real-time world.

Blender has a Python API and can run scripts in background mode. This means a local N.H tool could eventually give Blender narrow, structured instructions without requiring a person to click every modelling step.

However, Blender should probably **not** be treated as the entire live Ness's World runtime. It is primarily the workshop that builds and changes assets and scenes.

### Real-time world's likely role

A separate local real-time engine would handle:

- entering the room;
- VR rendering;
- hand or controller interaction;
- walking, flying, teleporting, or instant movement;
- doors and room transitions;
- physics and collision;
- voice interaction;
- desktop, mouse, keyboard, touch, and accessibility alternatives;
- live previews of proposed changes.

A strong first technical candidate is **Godot with OpenXR**, because it is open-source, can run locally, supports VR through OpenXR, and can import common 3D scene formats such as glTF/GLB. This is only a future implementation candidate, not an adopted N.H technology choice.

### Proposed relationship

A useful division would be:

> **Blender builds and edits. Godot runs and lets Ness inhabit the result. N.H coordinates the two through a restricted local tool layer.**

Other offline tools could later be added for textures, procedural generation, audio, avatars, motion, or specialised modelling. Blender should be a major tool, not an unnecessary single-tool prison.

---

## 5. How N.H could use Blender safely

N.H should not receive unlimited permission to run arbitrary Blender or operating-system code.

A safer future design would use a controlled sequence:

1. Ness asks for a room or change.
2. N.H creates a **structured scene proposal** describing intended objects, positions, scale, materials, lighting, doors, labels, and purpose.
3. A validator checks that the proposal stays inside the current room and authorised tool scope.
4. A narrow local Blender bridge converts approved scene operations into Blender Python actions.
5. Blender creates a **new version** of the room or asset; it never silently overwrites the accepted previous version.
6. The result is exported to a portable scene format such as GLB/glTF.
7. The real-time world opens a preview or branch.
8. Ness may accept, reject, revise, undo, compare, or keep several branches.
9. Every important change records what Ness asked, what N.H proposed, which tool performed it, what files were produced, and which version is active.

This would let N.H use Blender automatically while preserving control, history, reversibility, and safety.

---

## 6. The most important N.H boundaries

### The room is not the memory

A room may show memories, people, places, projects, readings, or connections, but the room scene is a **view and interaction space**, not the authoritative memory store.

Moving an object in VR does not silently change the underlying memory record.

### A simulation is not reality

Generated, reconstructed, imagined, and replayed material must remain distinguishable:

- **Replay:** based on actual preserved recordings or documented material.
- **Reconstruction:** an evidence-based attempt to rebuild something incomplete.
- **Invention / Wonder:** imagined possibility or generated material.
- **Simulation:** an explicitly entered interactive possibility space.

### A17 remains fully active

Wonder material stays isolated by default. Nothing generated in a room or simulation enters ordinary memory automatically.

Only material Ness deliberately selects may move toward memory, and even then it must pass through the normal privacy, provenance, intake, and acceptance protections. Its Wonder origin remains permanently visible.

### Real actions remain separate

A gesture inside the world must not automatically send a message, alter a real file, purchase something, contact someone, or change an outside system. Real-world actions require the normal N.H proposal and authority chain.

### Camera and VR are protected front doors

Hand tracking, room cameras, microphones, body tracking, and headset sensors may capture private surroundings and other people. Their capture-exclusion, privacy, temporary processing, storage, and visible-output rules must be explicitly designed under the existing privacy system before implementation.

### Immediate safe exit

The experience should eventually include an unmistakable instant exit and pause route for confusion, overload, tracking failure, fear, or discomfort. The exact behaviour remains an A19 design choice.

---

## 7. Connections to other N.H work

This idea mainly belongs to A19, but it may later connect to:

- **A17:** Wonder-to-memory policy; already accepted and must not be reopened.
- **A23:** conversation rehearsal; a future rehearsal could appear inside a labelled simulation room, but A23 keeps its own policy ownership.
- **A20 / B30:** phone and mobile experience; mobile may view or control parts of rooms later, but does not own the main VR world.
- **A21 / B29:** N.H's speaking model and voice pipeline; required for natural speech inside the world.
- **§7I and §7M:** views and what N.H chooses to show.
- **§7P:** authority for actions with real-world effects.
- **§7Q:** privacy, protected capture, and visible-output review.
- **§25 and accepted access wiring:** identity and Personal Mode access.
- **§0B:** transparent records of openings, mode changes, simulations, important manipulations, tool operations, and failures.
- **Bundle 8:** later whole-system wiring and connected-cycle design after the relevant Bundle 7 policy is accepted.

These are connection points, not permission to merge packages or begin their implementation now.

---

## 8. Design stages for this idea

### Stage 1 — Idea preservation — done by this note

Preserve the concept so it is not lost while current work continues.

This file does not decide the remaining A19 experience questions and does not create a formal candidate.

### Stage 2 — A19 experience and policy design

Later A19 work decides what using this feels like, including:

- VR-first, desktop-first, or equal modes;
- first-person, observer, or both;
- how rooms open and close;
- how Ness exits instantly;
- how room branches, resets, saves, and reopening work;
- what N.H may change automatically;
- when a preview or approval is required;
- gesture and voice behaviour;
- tracking failure and accidental-action prevention;
- emotional-overload behaviour;
- reconstruction, replay, invention, and simulation labelling;
- camera and headset privacy experience;
- accessibility alternatives.

### Stage 3 — Mechanical design

After the experience rules are settled, later mechanical design defines:

- scene and room identities;
- version and branch identities;
- exact safe Blender-operation vocabulary;
- import validation and provenance;
- save, undo, retry, crash recovery, and partial-operation handling;
- duplicate prevention;
- permissions and tool boundaries;
- logs and evidence;
- how room objects point to N.H material without becoming the memory store;
- how the real-time engine and creation tools communicate offline.

### Stage 4 — Bundle 8 wiring and audit

Connect the accepted A19 design to the rest of N.H, check all privacy, authority, voice, memory, Wonder, and recovery paths, and preserve Layer 2 / Layer 3 coexistence.

### Stage 5 — Implementation, only after separate Ness permission

Choose and install actual tools, create prototypes, connect Blender, build the VR runtime, and test on hardware.

No implementation is authorised by this note.

---

## 9. A sensible future first prototype

A future prototype could remain extremely small:

- one offline room;
- one plain white door;
- one movable N.H presence;
- voice plus mouse/keyboard, with VR as an optional second interface;
- a few objects that can be grabbed and rearranged;
- one object linked read-only to a preserved N.H item;
- one labelled Wonder object;
- one Blender-generated proposed change shown as a reversible branch;
- no automatic memory write;
- no external action;
- one instant stop/exit control.

The purpose would not be to build the whole world. It would prove whether the Blender → validated asset → real-time room loop feels natural and remains safe.

This is a prototype concept only, not current build permission.

---

## 10. Open ideas to remember for the eventual A19 discussion

These are not answers and do not need to be decided now:

- Should N.H alter a room live while Ness is inside, or normally prepare a preview branch first?
- Which small changes may happen naturally, and which count as big changes requiring approval?
- Should VR be the main experience, or one equal way to enter alongside desktop and mobile?
- Should Ness have a visible body/avatar, hands only, or selectable forms?
- Should an imported world stay visually separate from N.H-created areas, or be allowed to blend after clear permission?
- How should N.H show that an object is real evidence, a reconstruction, a memory view, a Wonder idea, or an invented simulation prop?
- How should rooms save over time: one history, branches, snapshots, or all three?
- What happens when Blender cannot complete a requested change safely?
- What is the immediate voice, gesture, controller, and keyboard exit command?
- How can the system reduce motion sickness, sensory overload, and visual confusion?

---

## 11. Why this idea matters

This idea makes the existing Ness's World design more practical:

- **Blender or similar tools** give N.H a way to make real 3D content locally.
- **A real-time OpenXR-capable engine** gives Ness a place to inhabit and interact with that content.
- **The N.H boundaries** keep imagination separate from evidence, scenes separate from memory, and virtual gestures separate from real-world authority.
- **Offline-first operation** supports privacy and the larger local N.H direction.
- **Versioned proposals and branches** let the world evolve without losing its history.

The core remembered idea is:

> **Ness's World can become an offline, interactive VR and desktop world made of rooms that Ness can enter, build, import, and reshape. N.H can use Blender or other local creation tools automatically through a restricted, reversible, well-recorded pipeline, while a real-time engine runs the living world. The rooms remain views or labelled simulations and never silently rewrite memory or reality.**

---

## 12. Source basis checked for this note

This note was aligned against:

- `NH_MASTER-20_CORRECTED_v10.md`, especially §19A–§19E;
- `NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`, C-19 / A19;
- `NH_REMAINING_DESIGN_WORK_MAP_v1_4_WORKING_RECORD.md`;
- accepted `NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` and its closure record;
- `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`;
- `NH_CHATGPT_PROJECT_INSTRUCTIONS_FULL_v1_2.md`;
- official Blender documentation on local Python scripting and background operation;
- official Godot documentation on OpenXR and glTF/GLB scene handling.

This source list records alignment only. It gives this personal note no authority and no implementation permission.
