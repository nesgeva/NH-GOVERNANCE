# Project editing rules

## Purpose and authority

Keep N.H's intended behavior clear enough for one LLM input. Ness owns product decisions. Simplifying wording does not authorize changing behavior, weakening privacy, activating proposals, or claiming unverified implementation.

## Organization

- README is navigation and usage only. SYSTEM owns purpose, components, and status. MEMORY, SECURITY, EXPERIENCE, and OPERATIONS each own their domain. DECISIONS holds genuine open questions. PROVENANCE points to historical evidence.
- Give each requirement one home. Link to it elsewhere. State universal rules once; add only a domain's actual exception or mechanism.
- Edit the existing owner file. Use Git for revision history. Do not create successor documents, per-chat handoffs, parallel masters, acceptance receipts, audit diaries, or documents that merely repeat another document.
- Keep historical source material outside the active input. Never silently discard unique decisions or archive current requirements merely to pass the budget.
- Separate accepted behavior, recorded preference, proposal, future intention, historical observation, and unknown. Preserve later explicit replacements and the scope of each answer.
- Record a real unresolved question once. Empty template cells, absent boilerplate, and duplicated references are not new product gaps.
- Keep schemas and exact values only where they constrain behavior or an existing contract. Never invent missing values, implementation choices, or authority.

## Writing

- Prefer short complete sentences, bullets for parallel rules, and tables for mappings. Use concrete subjects and active verbs.
- Cut introductions, summaries that repeat the body, rhetorical questions, generic conclusions, reassurance, flattery, and chatbot sign-offs.
- Use plain words. Avoid abstract metaphors, inflated vocabulary, vague attribution, decorative examples, forced groups of three, synonym cycling, and ornamental participle clauses.
- Say what a component does. Use "is" and "has" where accurate. Do not replace mechanisms with feelings or slogans.
- Avoid "not just X, but Y", false ranges, redundant bold labels, title-case headings, decorative emojis, curly quotes, and dash punctuation. Use periods or commas. Colons introduce actual lists or examples.
- Preserve required negations, conditions, uncertainty, exceptions, and permission boundaries. Do not make concise text ambiguous through fragments, abbreviations, or dropped words.
- Keep product flows free of implementation chatter unless it affects Ness's decision. Explain technical matters with a concrete example when needed.

## Size and verification

- The entire active project, including these instructions, tooling, and filename labels, must remain below 20,000 tokens in both `cl100k_base` and `o200k_base`. Aim below 18,000 for headroom.
- Run `python3 tools/check_project.py` after changes. Install dependencies outside the project. Do not exclude a document, hide text in binaries, add symlinks, or weaken the counter to pass.
- Export LLM bundles outside the project. Never retain duplicate generated bundles here.
- Before adding text, remove duplication or replace obsolete wording. Add a file only when none of the existing owners fits.
- Review meaning and status against actual sources. A token count, keyword match, or heading inventory cannot prove semantic preservation.
- Verify claims about actual files or runtime behavior. Say plainly what was not checked. Do not report complete until the actual working tree meets the requested outcome.
