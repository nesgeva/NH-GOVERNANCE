# CURSOR BRIEF — Reading Validator + Reading-Shaped Writer
### Build target for `nh_accretive_store.py`. Store-touching change → DRY-RUN + BACKUP + explicit approval required (defaults stop-condition 2). Build against this spec exactly; do not improvise the gaps — there are none left open on purpose. Any ambiguity → stop and ask, do not guess.

*Derived from `NH_MASTER-14_FINAL.md` §6B + §11 item 20, with the three S14 decisions folded in (see `NH_DELTA_S14.md`). This brief is the spec; it is NOT yet approved code. Verify on disk before touching anything.*

---

## 0. WHAT THIS IS / IS NOT
- **IS:** add a reading validator and a reading-shaped writer to `nh_accretive_store.py`, plus a small shared helper. Populate `.nh_readings_store.jsonl` with well-formed readings (the writer; population by the engine comes later).
- **IS NOT:** any change to the roots file, the seal, the engine, retrieval, or Chroma. No reading is generated here — this is the *plumbing the engine will write through*. Zero interpretation logic.

## 1. FIRST STEP — VERIFY ON DISK (read-only, before any edit)
Re-confirm the live state (it was verified this session; confirm again at build time — trust disk, not this doc):
```
python -c "import inspect, nh_accretive_store as s; print(inspect.signature(s.append_reading)); print(inspect.signature(s.append_root))"
python -c "import nh_accretive_store as s; print(s.STORE_PATH, s.READINGS_PATH, s.SEALED_MARKER)"
python -c "import inspect, nh_accretive_store as s; print(inspect.getsource(s._validate_record))"
```
Expected: `append_reading` still root-shaped `(subject, content, re_reads, role, source_title=None, timestamp=None)`; `_validate_record` enforces the 7-field ROOT schema; constants present. If anything differs, STOP.

## 2. STRUCTURE (option C — extract shared, don't fuse)
- **`_check_common(record)`** — NEW small helper. The checks shared by roots and readings, written ONCE: `id` non-empty string; `timestamp` non-empty valid ISO 8601. Raises `ValueError` on violation.
- **`_validate_record(record)`** — EDIT (light): replace its inline `id` + `timestamp` checks with a call to `_check_common`. Everything else in it stays byte-for-byte. This is a touch on sealed-store-guarding code → the dry-run MUST re-prove the 5,521 roots still validate clean through the helper.
- **`_validate_reading(record)`** — NEW. The 12-field reading contract (§3 below). Calls `_check_common`, then the reading-specific checks.
- **`append_reading(...)`** — REPLACE the current root-shaped body with a reading-shaped writer (§4). Still routes to `READINGS_PATH`. Still append-only.

> Walls preserved: the root validator keeps its own simple body (only delegates the common bit); the reading path is its own function; proven and unproven code stay separated.

## 3. THE 12-FIELD READING CONTRACT (`_validate_reading`)
Record = dict with EXACTLY these keys (reject unexpected keys, reject missing keys):
`id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`

1. **`id`** — non-empty string (via `_check_common`). Immutable record identity.
2. **`reads`** — list, NON-EMPTY, of non-empty strings (root ids). *(Existence-in-roots is checked by the WRITER before commit, §4 — not here; the validator checks shape only.)*
3. **`meaning`** — non-empty string. The honest insufficient-context read is a VALID meaning (S14 decision 3) — do NOT special-case or reject it.
4. **`confidence`** — an OBJECT (dict), never a bare number. Checks:
   - key `interpretation_confidence` PRESENT and non-empty. **Do NOT enforce a value-form** (low/med/high vs 0–1 is deliberately unfrozen — S14 decision 2). Any non-empty value passes.
   - key `source_reliability` is OPTIONAL: either absent, or present-and-non-empty. Absent is legal (empty-when-unknown).
   - reject if `confidence` is a scalar, or if `interpretation_confidence` missing/empty.
5. **`role`** — non-empty string (speaker carried from the root).
6. **`story_layer`** — a LIST. EMPTY LIST IS LEGAL. If non-empty, each item is a dict whose keys are a subset of `{whose, stance, firmness, telling, theme, when}` (all optional); reject any other key; reject a literal `"unknown"` value (unknowns are OMITTED, not filled).
7. **`mode`** — an OBJECT: `label` (non-empty string, open word — do NOT validate against a fixed menu) + `classification_confidence` (present, non-empty; local field, unrelated to #4).
8. **`timestamp`** — non-empty valid ISO 8601 (via `_check_common`). Meaning = CREATION time of the reading.
9. **`produced_by`** — an OBJECT. `origin` PRESENT and ∈ {`observed`,`imported`,`simulated`,`generated`,`reaction`,`human_annotation`}. For engine origins, expect model/digest/engine/prompt/config/retrieval-input fields (validate present as a group; exact sub-shape may stay permissive for now). For `origin="human_annotation"`, expect annotation provenance instead (annotator/when/context-version). Required on every reading.
10. **`schema_version`** — PRESENT, non-empty. First reading = `"v1"`.
11. **`derived_from`** — a LIST of parent reading ids. MUST be present. `[]` is legal (and is the value when the reading is fresh from roots).
12. **`idempotency_key`** — non-empty string. Operation identity, SEPARATE from `id`.

### THE GOVERNING RULE — gate on SHAPE, never on confidence
Reject MALFORMED. NEVER reject UNCERTAIN. A reading with low/weak confidence is well-formed → it gets written and marked. Only a structurally broken record is refused. (R5 — rejecting on confidence sneaks the manual gate back in.) The validator certifies *well-formed*, NOT *correct* — accuracy is decided later against sealed gold, never by the validator.

## 4. THE WRITER (`append_reading`) — SAFETY CONTRACT
The writer builds the record, validates it (`_validate_reading`), and appends it to `READINGS_PATH`. Requirements:
- **Verify-root-before-commit:** every id in `reads` MUST exist in the sealed roots store. If any is missing → raise, write nothing. (No dangling readings.)
- **Atomic / crash-safe append:** never leave a torn/partial JSONL line. A crash mid-write leaves the file either fully-with or fully-without the record. (Write-and-flush a complete line; no half-records.)
- **Idempotent on `idempotency_key`:** if the key was already committed, REJECT (write nothing) — a crash-and-retry must not double-write. `id` stays the immutable record identity; the key guards the operation. (A content hash is NOT the retry guarantee.)
- **Append-only:** open mode `"a"`/`"r"` only — never `"w"`. Same discipline as the root store.
- **Writes to `READINGS_PATH` only** — NEVER the roots file, NEVER past the seal.
- The roots file and `.nh_roots.sealed` are NOT touched by anything in this build.

## 5. WHAT NOT TO DO (explicit guards)
- Do NOT enforce a confidence value-form (#4) — leave it loose; pinning it later is a NEW schema_version.
- Do NOT validate `mode.label` against a fixed list of allowed words.
- Do NOT reject a reading for being uncertain, weak, empty-story, or insufficient-context.
- Do NOT fuse the root and reading validators into one branching function — keep them separate (option C).
- Do NOT modify `_validate_record` beyond swapping id/timestamp checks for the `_check_common` call.
- Do NOT write to, rename, unseal, or back-fill the roots file. Do NOT add `schema_version` to the sealed roots (they are implicit v1, tolerated-absent on read).
- Do NOT generate or infer any reading content — no interpretation in this layer.

## 6. DRY-RUN + APPROVAL PROTOCOL (store-touching → mandatory)
1. **Backup first** — copy-aside `.nh_readings_store.jsonl` (if it exists) and `nh_accretive_store.py` before any edit. Roots are already sealed + backed up (`bak_preseal`); confirm, don't re-touch.
2. **Dry-run / unit tests against FIXTURES** — build small hand-made reading fixtures from the sealed gold FORMAT and prove:
   - a well-formed reading passes `_validate_reading` and writes to the sibling;
   - each single malformed field (missing key, scalar confidence, bad origin, missing derived_from, `reads` pointing at a non-existent root, `"unknown"` in a telling) is REJECTED;
   - a low/weak/empty-story/insufficient-context reading is ACCEPTED (gate-on-shape proof);
   - a repeated `idempotency_key` is rejected (no double-write);
   - **the 5,521 roots STILL validate clean** through the edited `_validate_record` + `_check_common` (regression proof);
   - roots count stays exactly 5,521 and the seal still refuses an `append_root`.
3. **Show the diff + dry-run output to Ness. Wait for explicit "APPROVED".** No production write before that.
4. **Ness runs and verifies on disk.** Cursor does not self-confirm success.

## 7. OUT OF SCOPE (named, not built here)
Engine / interpretation logic; the gold annotation + seal; retrieval reading-the-view; the confidence value-form; the insufficient-context RETRY trigger; multi-box addressing; Chroma rebuild. This brief delivers ONLY: `_check_common`, the light `_validate_record` edit, `_validate_reading`, and the reading-shaped `append_reading` writer — validated, dry-run, approved, verified.

---
*Spec only — nothing approved until the dry-run diff is reviewed and Ness says APPROVED. On any conflict with the master, the master's status table wins. Trust disk, not this doc.*
