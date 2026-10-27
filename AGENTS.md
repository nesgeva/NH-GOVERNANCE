# Project editing rules

## Purpose and authority

Ness owns product decisions. Keep N.H behavior clear for one LLM input. Wording edits cannot change behavior, weaken privacy, adopt proposals or imply unverified implementation.

## Organization

- README owns navigation and usage. SYSTEM owns purpose, components and status. MEMORY, SECURITY, EXPERIENCE and OPERATIONS own their domains. DECISIONS owns open questions. PROVENANCE points to historical evidence.
- Give each requirement one home. Link elsewhere. State universal rules once; add only actual domain exceptions or mechanisms.
- Edit existing owners. Use Git history instead of successor documents, per-chat handoffs, parallel masters, acceptance receipts, audit diaries or duplicates.
- Keep history outside active input. Never silently discard unique decisions or archive current requirements to pass the budget.
- Distinguish accepted behavior, preferences, proposals, future intentions, historical observations and unknowns. Preserve later explicit replacements and each answer's scope.
- Record unresolved questions once. Empty templates, absent boilerplate and duplicate references are not gaps.
- Keep schemas and exact values only when behavior or existing contracts require them. Never invent values, implementation choices or authority.

## Writing

- Use short complete sentences, concrete subjects, active verbs, bullets for parallel rules and tables for mappings.
- Cut introductions, repeated summaries, rhetorical questions, generic conclusions, reassurance, flattery and chatbot sign-offs.
- Use plain words. Avoid metaphors, inflated vocabulary, vague attribution, decorative examples, forced threes, synonym cycling and ornamental participles. Describe mechanisms with "is" or "has", not feelings or slogans.
- Avoid "not just X, but Y", false ranges, redundant bold labels, title-case headings, emojis, curly quotes and dash punctuation. Use periods or commas. Colons introduce lists or examples.
- Preserve negations, conditions, uncertainty, exceptions and permissions. Avoid ambiguous fragments or abbreviations. Keep implementation details out of product flows unless they affect Ness's decision.

## Explaining N.H to Ness

AI assistants, including ChatGPT, explain N.H in simple Hebrew through everyday use. Describe Ness's actions, N.H's responses, what Ness sees and what happens next. Assume no technical knowledge. Explain terms. Clarify confusion with context and simpler words, not just shorter text. See EXPERIENCE.md for conversation rules.

Example wording only, not adopted behavior: "אתה מחוץ לבית. אתה שולח לעוזר תמונה. אחר כך אתה מפעיל סנכרון ומשלים אימות. התמונה עוברת למחשב."

## Size and verification

- Keep the whole active project, including instructions, tools and filename labels, at or below 25,000 tokens in `cl100k_base` and `o200k_base`. Aim for 21,000 or fewer.
- Run `python3 tools/check_project.py` after edits. Install dependencies outside the project. Never exclude documents, hide text in binaries, add symlinks or weaken counting to pass.
- Export LLM bundles outside the project. Keep no generated duplicates here.
- Remove duplication or replace obsolete wording before additions. Add files only if no owner fits.
- Check meaning and status against sources. Counts, keywords and headings cannot prove preserved meaning.
- Verify file and runtime claims. State unchecked work. Finish only when the working tree meets the request.
