# NH_VOICE_COMMANDS_INTENT_v0_2.md — Ness's intent: commands by voice, custom phrases, and approvals

**What this is.** Ness's new feature idea, recorded in his words on 2026-10-05, so that it is not lost. **It is an intent, not a design.** It decides nothing, adds nothing to Master-21, and is designed later through the normal route, after Ness decides its open questions. Prepared by Claude at Ness's request. Status: intent, for `05_INACTIVE_CANDIDATE/`.

**Version note (v0_2, 2026-10-05).** v0_1 (SHA-256 `d4749646e97fca4c4c25f3f265b169bfc406a30ddf1c8688bb2777686edbf9d8`; kept). Adds Ness's first answer and one tension to settle (§5). Nothing else changed.

## 1. Ness's words

"I want n.h to also make commands in general *the ones that doesn't do risky stuff* do them by me telling him to do that and him being able to activate commands that does some stuff and combinations and more... and phrases activates custom for me, and n.h is allowed to activate a couple of commands (commands are actions inside n.h system) he is allowed to activate commands if my saying is related to the command or helps it in some way and sometimes (when doing big commands and complicated stuff, it will need to ask for approvel (in voice that is me 100% or in a click on the button ui))"

In short:
- non-risky commands run when Ness tells N.H to;
- commands can be combined;
- custom phrases trigger commands for Ness;
- N.H may itself start some commands when what Ness says relates to them or helps them;
- big or complicated commands need Ness's approval, by his voice or by a button in the interface.

## 2. What Master-21 already has (checked at `nesgeva/NH-GOVERNANCE@9645157`)

- **Narrow voice commands only:**
  - a deliberate chat or voice command switches presentation mode, within existing approval boundaries (C-19.1.4 — Manual mode switching, V10 §19A);
  - a clear voice command changes a new room's starting form without further confirmation (C-19.15.6, accepted package A19 §4).
- **No general command system.** A search of the book found no custom or trigger phrases, no wake word and no macros (0 hits), and no rule for N.H starting commands itself.
- **Where "command" does appear** (about 500 times), it is narrow:
  - views and World entry (C-19);
  - a command as one type of input (C-BOP);
  - "an ordinary command alone cannot open" Ness's World, which needs identity confirmation (C-7GA, V10 §19A);
  - the phone must never execute raw operating-system commands from phone input (C-23, V10 §23);
  - a candidate list of allowed commands for the lab (C-NEW-LAB.1.7, not adopted).
- **An unconditional protected rule that this idea touches:** "Voice alone cannot unlock top-security" (C-SACL.16.1, from V10 §25.2's unconditional protected rules). Approval by voice therefore cannot be enough for any top-security action, however sure the voice is. This intent does not change that rule; only Ness can decide anything about it, explicitly.

## 3. Open questions (Ness's to decide; they join his question queue, route note v0_8 §9.9)

1. **The line between ordinary and big:** which commands are "not risky" and run on his word alone, and which are "big or complicated" and need approval? For example: a list Ness approves and can change.
2. **Custom phrases:** how does Ness create, change or remove a phrase, and what may one phrase start (a single command, or a combination)?
3. **N.H starting commands itself:** which commands may it start when Ness's words relate to them, and does it tell him each time?
4. **Approvals:** for which commands is his voice enough, and for which is the interface button needed? Top-security actions can never be approved by voice alone (§2).
5. **Combinations:** if one step of a combined command fails, what happens to the rest?

## 4. Related rules (unchanged)

- Ness's reason-before-act idea (2026-09-25; its status is not checked here): N.H reasons before acting on plain-language instructions; slash commands run as given.
- Speaker identity and access: C-SIA gives evidence, never permission; C-SACL sets access; C-BAI supplies biometric proof (accepted B-INT-5 §4).

## 5. Ness's answers (2026-10-05)

- **Question 1, which commands need his OK first:** all of these:
  - anything that deletes or changes his things;
  - anything big or with many steps;
  - a list Ness makes himself.
- **Tension to settle later (in his queue):** in the multi-chat idea, "take from this chat and put into this" runs "without needing to click (if it doesn't seem like it would do anything bad or ruin anything)". Both answers can hold if moving things between chats does not count as "changing his things". That line is Ness's to draw.
- Questions 2–5 are still open.
