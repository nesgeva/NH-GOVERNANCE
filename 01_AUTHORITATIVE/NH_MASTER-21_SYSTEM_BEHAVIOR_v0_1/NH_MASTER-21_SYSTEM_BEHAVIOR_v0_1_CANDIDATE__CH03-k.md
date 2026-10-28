# Chapter 3-k — Group A: C-INDEX

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-k.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers the clean-root Chroma index, its embedding model and metric, the rebuild utility and dry-run, old-collection protection, the protected rebuild-change boundary, the semantic retrieval interface and index operation records. Counts and run duration describe V10's recorded state. They are not universal future limits. CH05-c owns context-retrieval modes, limits, ranking policy, provenance and fallback; CH10-b owns the general model layer. The shared log lifecycle remains in CH02. No vector dimensions, distance thresholds, new storage formats or unrecorded failure mechanisms are supplied here.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; CR = `01_AUTHORITATIVE/cursorrules`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`.

<!-- BEGIN BEHAVIOR -->

### C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16)
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [MAP C-INDEX]

ALONE
- What it is: BUILT — The Chroma index `nh_roots_v1` in the recorded `chroma_db\` directory, rebuilt from 5,521 clean roots using `all-MiniLM-L6-v2` embeddings and cosine distance. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Physical stores on disk]
- Takes in: BUILT — The clean roots supplied to `nh_rebuild_chroma.py`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Accretive store + tooling]
- Does: BUILT — Represents those roots in the clean-root embedding index. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gives out: BUILT — The clean index containing 5,521 roots. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gives out: DESIGNED — Ranked semantic neighbors for a query through Context Retrieval; this DUMB tool sorts by meaning-distance. [MAP C-INDEX]
- Must never: DESIGNED — Touch the protected old collections during an ordinary rebuild or index operation, treat similarity as proof of relevance, or silently replace preceding-turn context with a semantic match. [MAP C-INDEX] [V10 §7F]
- Fails closed by: DESIGNED — The protected old collections stay untouched, similarity is never treated as proof of relevance, and preceding-turn context is never silently replaced by a semantic match. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [MAP C-INDEX] [V10 §7F]

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the 5,521 clean roots used to rebuild the index. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-INDEX.1 — nh_roots_v1: provides the current clean-root collection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Fed by: BUILT — C-INDEX.2 — nh_rebuild_chroma.py: builds the clean index from its root source. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row]
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: rebuilds must leave the retained collections untouched. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: a proposed protected-file change requires the specified declarations and authorization. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: every rebuild and index mutation requires its traceable operation record. [MAP C-INDEX] [V10 §0B]
- Changes: DESIGNED — C-INDEX.5 — Semantic retrieval interface: supplies the clean-index search surface for the semantic channel. [MAP C-INDEX]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | A query for semantic context. | Uses the index to obtain meaning-distance-ranked neighbors. | Receives semantic candidates, kept distinct from positional context. | [MAP C-INDEX] [V10 §7F] |
| 2 · DESIGNED | C-16.2 — Search before wording | The retrieval need before the generation call. | Provides the source-recorded clean embedding index and search model. | Nothing in this card. | [V10 §16] |

SUB-PARTS: C-INDEX.1 — nh_roots_v1; C-INDEX.2 — nh_rebuild_chroma.py; C-INDEX.3 — Old-collection protection; C-INDEX.4 — Rebuild change boundary; C-INDEX.5 — Semantic retrieval interface; C-INDEX.6 — Index operation records

### C-INDEX.1 — nh_roots_v1
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]

ALONE
- What it is: BUILT — The current clean-root Chroma collection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Takes in: BUILT — Embeddings of the 5,521 clean roots from the rebuild. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Does: BUILT — Holds those roots under the `all-MiniLM-L6-v2` embedding configuration and cosine-distance metric. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gives out: BUILT — The new clean index, distinct from the old 116,391-record collection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Physical stores on disk]
- Must never: DESIGNED — Be silently modified or dropped outside its protected boundary. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings: supplies the embedding representation used by this collection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Fed by: BUILT — C-INDEX.1.2 — Cosine distance: supplies the collection's configured distance metric. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Fed by: BUILT — C-INDEX.2 — nh_rebuild_chroma.py: rebuilds this collection from the clean roots. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the destination collection and replacement/append/rebuild behavior must be declared in a proposed change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | Embeddings of the 5,521 clean roots from the rebuild. | provides the current clean-root collection. | The new clean index, distinct from the old 116,391-record collection. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Physical stores on disk] |
| 2 · BUILT | C-INDEX.2 — nh_rebuild_chroma.py | Embeddings of the 5,521 clean roots from the rebuild. | creates the rebuilt clean-root collection. | The new clean index, distinct from the old 116,391-record collection. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Physical stores on disk] |
| 3 · DESIGNED | C-INDEX.5 — Semantic retrieval interface | Embeddings of the 5,521 clean roots from the rebuild. | supplies the current clean-root semantic index to the designed retrieval route. | The new clean index, distinct from the old 116,391-record collection. | [MAP C-INDEX] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Physical stores on disk] |

SUB-PARTS: C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings; C-INDEX.1.2 — Cosine distance

### C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]

ALONE
- What it is: BUILT — The embedding model used in the clean-root index, recorded on disk at `models\all-MiniLM-L6-v2`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Models on disk]
- Takes in: BUILT — Clean roots supplied for indexing. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Does: BUILT — Produces the `all-MiniLM-L6-v2` embedding representation used in `nh_roots_v1`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gives out: BUILT — The index's root embeddings. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Must never: DESIGNED — Conflate embedding search with the mouth's wording/generation job; the declared order is search first, word last. [V10 §16 / TWO MODELS, TWO JOBS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the clean-root material used by the index. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the embedding model must be explicitly identified in a proposed rebuild change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-INDEX.1 — nh_roots_v1 | Clean roots supplied for indexing. | supplies the embedding representation used by this collection. | The index's root embeddings. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] |
| 2 · BUILT | C-INDEX.1.2 — Cosine distance | Clean roots supplied for indexing. | provides the representation to which this configured metric applies. | The index's root embeddings. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] |

SUB-PARTS: NONE

### C-INDEX.1.2 — Cosine distance
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]

ALONE
- What it is: BUILT — The configured distance metric of `nh_roots_v1`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Takes in: BUILT — The index's `all-MiniLM-L6-v2` embedding representation. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Does: BUILT — Uses cosine distance in the clean-root index. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gives out: BUILT — Cosine-distance measurements for that index. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Must never: DESIGNED — Treat semantic similarity as proof of relevance or as a preceding conversational turn. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings: provides the representation to which this configured metric applies. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gated by: DESIGNED — C-7F — Context Retrieval (§7F): semantic matches retain their distinct provenance and cannot silently override positional context. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-INDEX.1 — nh_roots_v1 | The index's `all-MiniLM-L6-v2` embedding representation. | supplies the collection's configured distance metric. | Cosine-distance measurements for that index. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] |

SUB-PARTS: NONE

### C-INDEX.2 — nh_rebuild_chroma.py
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — The utility that rebuilds `nh_roots_v1` from clean roots. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row]
- Takes in: BUILT — The clean-root source used for the 5,521-root index. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Rebuilds the clean collection while keeping the old collections untouched. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row]
- Gives out: BUILT — The completed clean-root index; V10 records a 5,521-root full run taking 187.59 seconds. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Silently rename, overwrite, merge, delete or migrate `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the clean roots for the rebuild. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]
- Gated by: DESIGNED — C-INDEX.2.1 — --dry-run: the dry-run precedes the full rebuild. [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: protected changes must declare their behavior, destinations and checks and receive the required authorization. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: old collections stay untouched during the rebuild. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: BUILT — C-INDEX.1 — nh_roots_v1: creates the rebuilt clean-root collection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | The clean-root source used for the 5,521-root index. | builds the clean index from its root source. | The completed clean-root index; V10 records a 5,521-root full run taking 187.59 seconds. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] [V10 §5 / Accretive store + tooling] |
| 2 · BUILT | C-INDEX.1 — nh_roots_v1 | The clean-root source used for the 5,521-root index. | rebuilds this collection from the clean roots. | The completed clean-root index; V10 records a 5,521-root full run taking 187.59 seconds. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] |

SUB-PARTS: C-INDEX.2.1 — --dry-run

### C-INDEX.2.1 — --dry-run
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — The rebuild utility's verified dry-run flag. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row]
- Takes in: BUILT — A 10-root test selection. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Runs the small rebuild test and retrieval check. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — The checked 10-root test run. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Silently modify any of the protected old collections during the test. [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the clean-root material for the small test. [V10 §5 / Accretive store + tooling]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: a proposed change must explain how dry-run precedes the full rebuild and how retrieval correctness is checked. [CR §7. PROTECTED FILES / LAYER 3]
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: the small test must leave the protected old collections untouched. [CR §7. PROTECTED FILES / LAYER 3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-INDEX.2 — nh_rebuild_chroma.py | A 10-root test selection. | the dry-run precedes the full rebuild. | The checked 10-root test run. | [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, `nh_rebuild_chroma.py` row] |

SUB-PARTS: NONE

### C-INDEX.3 — Old-collection protection
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]

ALONE
- What it is: DESIGNED — The boundary preserving the old Chroma collections during clean-index work. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3]
- Does: DESIGNED — Requires the old collections to remain untouched unless Ness separately and explicitly authorizes otherwise. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — The preserved old collections alongside the clean-root index. [MAP C-INDEX]
- Must never: DESIGNED — Silently rename, overwrite, merge, delete or migrate the old collections, or destroy the retained `nh_reality_core` index. [CR §7. PROTECTED FILES / LAYER 3] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row]
- Fails closed by: DESIGNED — Without Ness's separate explicit authorization, the old collections remain untouched and the retained `nh_reality_core` index is preserved. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row]

TOGETHER
- Fed by: BUILT — C-INDEX.3.1 — nh_reality_core: identifies the retained old collection protected from destruction and unapproved alteration. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row] [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.3.2 — nh_test_asm: identifies the old test collection that must remain untouched. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.3.3 — nh_simulation_core: identifies the old simulation collection that must remain untouched. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: any separately authorized exception must be explicit; a routine rebuild is no silent authorization. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | rebuilds must leave the retained collections untouched. | The preserved old collections alongside the clean-root index. | [V10 §6A / PROTECTED FILES AND STORES] [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] |
| 2 · DESIGNED | C-INDEX.2 — nh_rebuild_chroma.py | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | old collections stay untouched during the rebuild. | The preserved old collections alongside the clean-root index. | [V10 §6A / PROTECTED FILES AND STORES] [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] |
| 3 · DESIGNED | C-INDEX.2.1 — --dry-run | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | the small test must leave the protected old collections untouched. | The preserved old collections alongside the clean-root index. | [CR §7. PROTECTED FILES / LAYER 3] [MAP C-INDEX] |
| 4 · DESIGNED | C-INDEX.3.1 — nh_reality_core | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | clean-index operations must preserve this old collection. | The preserved old collections alongside the clean-root index. | [V10 §6A / PROTECTED FILES AND STORES] [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] |
| 5 · DESIGNED | C-INDEX.3.2 — nh_test_asm | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | a rebuild may not silently alter this collection. | The preserved old collections alongside the clean-root index. | [V10 §6A / PROTECTED FILES AND STORES] [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] |
| 6 · DESIGNED | C-INDEX.3.3 — nh_simulation_core | A proposed rebuild or index operation that could affect `nh_reality_core`, `nh_test_asm` or `nh_simulation_core`. | changes require Ness's separate explicit authorization. | The preserved old collections alongside the clean-root index. | [V10 §6A / PROTECTED FILES AND STORES] [MAP C-INDEX] [CR §7. PROTECTED FILES / LAYER 3] |

SUB-PARTS: C-INDEX.3.1 — nh_reality_core; C-INDEX.3.2 — nh_test_asm; C-INDEX.3.3 — nh_simulation_core

### C-INDEX.3.1 — nh_reality_core
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row]

ALONE
- What it is: BUILT — The old, unaligned Chroma index containing 116,391 records. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row]
- Takes in: NOT DECIDED
- Does: DESIGNED — Remains retained while `nh_roots_v1` is being proven for production. [V10 §6A / THE THREE-LAYER ARCHITECTURE] [CR §4B. CURRENT STORES / CHROMA COLLECTIONS]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Be destroyed or silently altered, merged, renamed, overwritten or migrated by clean-index work. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row] [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: clean-index operations must preserve this old collection. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.3 — Old-collection protection | NOT DECIDED | identifies the retained old collection protected from destruction and unapproved alteration. | NOT DECIDED | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_reality_core` row] [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.3.2 — nh_test_asm
Stamp: DESIGNED    Source: [V10 §5 / Physical stores on disk] [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The protected old Chroma collection `nh_test_asm`; V10 records 1,180 entries. [V10 §5 / Physical stores on disk]
- Takes in: NOT DECIDED
- Does: DESIGNED — Remains untouched by ordinary rebuild work. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Be silently renamed, overwritten, merged, deleted or migrated. [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: a rebuild may not silently alter this collection. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.3 — Old-collection protection | NOT DECIDED | identifies the old test collection that must remain untouched. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.3.3 — nh_simulation_core
Stamp: DESIGNED    Source: [V10 §5 / Physical stores on disk] [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The protected old Chroma collection `nh_simulation_core`; V10 records 263 entries. [V10 §5 / Physical stores on disk]
- Takes in: NOT DECIDED
- Does: DESIGNED — Remains preserved outside an ordinary clean-index rebuild's effects. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Be silently renamed, overwritten, merged, deleted or migrated during index work. [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: DESIGNED — `nh_simulation_core` stays preserved; without Ness's separate explicit authorization, index work does not rename, overwrite, merge, delete or migrate it. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.3 — Old-collection protection: changes require Ness's separate explicit authorization. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.3 — Old-collection protection | NOT DECIDED | identifies the old simulation collection that must remain untouched. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4 — Rebuild change boundary
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]

ALONE
- What it is: DESIGNED — The protected-code boundary for a proposed change to `nh_rebuild_chroma.py`. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]
- Does: DESIGNED — Requires those declarations, the dry-run protocol (a PROPOSED CHANGE block naming the file, one sentence on what changes, every store touched with Layer 3 quarantine or production stated explicitly, and the gate function used by exact name and file; then the full proposed code with no placeholders; then a wait for "APPROVED" before applying) and `CONFIRMED: modify nh_rebuild_chroma.py` before the protected edit. [V10 §6A / PROTECTED FILES AND STORES] [V10 §6A / DRY-RUN PROTOCOL]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Make the protected change without its explicit authorization, omit any required declaration, or silently alter the old collections. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: DESIGNED — The protected edit may not proceed without the required explicit confirmation and change declarations. [V10 §6A / PROTECTED FILES AND STORES]

TOGETHER
- Fed by: DESIGNED — C-INDEX.4.1 — Changed rebuild behavior declaration: states the exact behavior affected. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.2 — Source and expected-count declaration: states the root store and expected count. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.3 — Embedding-model declaration: identifies the model to be used. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.4 — Destination declaration: identifies the destination Chroma collection. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.5 — Record-treatment declaration: states whether records will be replaced, appended or rebuilt. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.6 — Dry-run-use declaration: explains use of dry-run before full rebuilding. [CR §7. PROTECTED FILES / LAYER 3]
- Fed by: DESIGNED — C-INDEX.4.7 — Retrieval-check declaration: explains how correctness will be checked. [V10 §6A / PROTECTED FILES AND STORES]
- Fed by: DESIGNED — C-INDEX.4.8 — Gold-rerun declaration: states whether the gold sets must be rerun. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: DESIGNED — Ness must explicitly authorize the protected file change; any exception affecting old collections requires separate explicit authorization. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | a proposed protected-file change requires the specified declarations and authorization. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 2 · DESIGNED | C-INDEX.1 — nh_roots_v1 | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the destination collection and replacement/append/rebuild behavior must be declared in a proposed change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 3 · DESIGNED | C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the embedding model must be explicitly identified in a proposed rebuild change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 4 · DESIGNED | C-INDEX.2 — nh_rebuild_chroma.py | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | protected changes must declare their behavior, destinations and checks and receive the required authorization. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 5 · DESIGNED | C-INDEX.2.1 — --dry-run | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | a proposed change must explain how dry-run precedes the full rebuild and how retrieval correctness is checked. | NOT DECIDED | [CR §7. PROTECTED FILES / LAYER 3] [V10 §6A / PROTECTED FILES AND STORES] |
| 6 · DESIGNED | C-INDEX.3 — Old-collection protection | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | any separately authorized exception must be explicit; a routine rebuild is no silent authorization. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 7 · DESIGNED | C-INDEX.4.1 — Changed rebuild behavior declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | this declaration is required before a protected rebuild change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 8 · DESIGNED | C-INDEX.4.2 — Source and expected-count declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the proposed change must identify both source and expected count. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 9 · DESIGNED | C-INDEX.4.3 — Embedding-model declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the embedding model is a required declaration for the change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 10 · DESIGNED | C-INDEX.4.4 — Destination declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | destination identification is required before the protected change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 11 · DESIGNED | C-INDEX.4.5 — Record-treatment declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | record treatment must be explicit in the proposed change. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 12 · DESIGNED | C-INDEX.4.6 — Dry-run-use declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the dry-run approach is required in the proposed-change declaration. | NOT DECIDED | [CR §7. PROTECTED FILES / LAYER 3] [V10 §6A / PROTECTED FILES AND STORES] |
| 13 · DESIGNED | C-INDEX.4.7 — Retrieval-check declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the change requires a stated retrieval-correctness check. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |
| 14 · DESIGNED | C-INDEX.4.8 — Gold-rerun declaration | A proposed change declaring: the exact rebuild behavior changed; source root store and expected root count; embedding model; destination Chroma collection; replacement, append or rebuild treatment; use of `--dry-run` before full rebuilding; retrieval-correctness check; and whether gold sets must be rerun. | the change must say whether the gold sets must be rerun. | NOT DECIDED | [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3] |

SUB-PARTS: C-INDEX.4.1 — Changed rebuild behavior declaration; C-INDEX.4.2 — Source and expected-count declaration; C-INDEX.4.3 — Embedding-model declaration; C-INDEX.4.4 — Destination declaration; C-INDEX.4.5 — Record-treatment declaration; C-INDEX.4.6 — Dry-run-use declaration; C-INDEX.4.7 — Retrieval-check declaration; C-INDEX.4.8 — Gold-rerun declaration

### C-INDEX.4.1 — Changed rebuild behavior declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required identification of the exact rebuild behavior being changed. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The proposed change to rebuild behavior. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Makes that behavior explicit in the protected-change declaration. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — A statement of the exact behavior affected. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Leave the proposed behavioral change unspecified. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: this declaration is required before a protected rebuild change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The proposed change to rebuild behavior. | states the exact behavior affected. | A statement of the exact behavior affected. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.2 — Source and expected-count declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required source-root-store and expected-root-count statement. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The intended source store and the root count expected from it. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Declares both the source and expectation for the proposed rebuild. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — The source/count pair to be assessed with the change. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Omit either the source root store or the expected count. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the proposed change must identify both source and expected count. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The intended source store and the root count expected from it. | states the root store and expected count. | The source/count pair to be assessed with the change. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.3 — Embedding-model declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required model statement for a proposed rebuild change. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The embedding model intended for the rebuild. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Names that model in the proposed change. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — An explicit embedding-model declaration. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Leave the embedding-model choice undeclared. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the embedding model is a required declaration for the change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The embedding model intended for the rebuild. | identifies the model to be used. | An explicit embedding-model declaration. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.4 — Destination declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The proposed rebuild's required destination statement. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The intended destination Chroma collection. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Identifies the collection the proposed operation would affect. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — A declared Chroma destination. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Leave the destination collection unnamed. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: destination identification is required before the protected change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The intended destination Chroma collection. | identifies the destination Chroma collection. | A declared Chroma destination. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.5 — Record-treatment declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required statement of what the proposed operation does to existing records. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The intended replacement, append or rebuild treatment. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — States whether records will be replaced, appended or rebuilt. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — A declared record-treatment choice. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Hide or omit the intended treatment of existing records. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: record treatment must be explicit in the proposed change. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The intended replacement, append or rebuild treatment. | states whether records will be replaced, appended or rebuilt. | A declared record-treatment choice. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.6 — Dry-run-use declaration
Stamp: DESIGNED    Source: [CR §7. PROTECTED FILES / LAYER 3]

ALONE
- What it is: DESIGNED — The required explanation of how the dry-run flag will be used. [CR §7. PROTECTED FILES / LAYER 3]
- Takes in: DESIGNED — The proposed use of `--dry-run` before the full rebuild. [CR §7. PROTECTED FILES / LAYER 3]
- Does: DESIGNED — Makes that pre-full-rebuild test use explicit. [CR §7. PROTECTED FILES / LAYER 3]
- Gives out: DESIGNED — The declared dry-run approach for the change. [CR §7. PROTECTED FILES / LAYER 3]
- Must never: DESIGNED — Omit how dry-run will be used before the full operation. [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the dry-run approach is required in the proposed-change declaration. [CR §7. PROTECTED FILES / LAYER 3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The proposed use of `--dry-run` before the full rebuild. | explains use of dry-run before full rebuilding. | The declared dry-run approach for the change. | [CR §7. PROTECTED FILES / LAYER 3] |

SUB-PARTS: NONE

### C-INDEX.4.7 — Retrieval-check declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required retrieval-correctness check statement. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — The proposed way to check retrieval correctness. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — States how that correctness will be checked for the rebuild change. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — An explicit retrieval-check declaration. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Leave the correctness-check approach unspecified. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the change requires a stated retrieval-correctness check. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | The proposed way to check retrieval correctness. | explains how correctness will be checked. | An explicit retrieval-check declaration. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.4.8 — Gold-rerun declaration
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The required statement of whether the proposed change needs gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — Whether the gold sets must be rerun after the rebuild change. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Records that requirement explicitly in the proposed change. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — The declared gold-rerun requirement. [V10 §6A / PROTECTED FILES AND STORES]
- Must never: DESIGNED — Leave whether the gold sets require rerunning unstated. [V10 §6A / PROTECTED FILES AND STORES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.4 — Rebuild change boundary: the change must say whether the gold sets must be rerun. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.4 — Rebuild change boundary | Whether the gold sets must be rerun after the rebuild change. | states whether the gold sets must be rerun. | The declared gold-rerun requirement. | [V10 §6A / PROTECTED FILES AND STORES] |

SUB-PARTS: NONE

### C-INDEX.5 — Semantic retrieval interface
Stamp: DESIGNED    Source: [MAP C-INDEX] [V10 §7F]

ALONE
- What it is: DESIGNED — The index's query-to-ranked-neighbors interface used by Context Retrieval's semantic channel. [MAP C-INDEX]
- Takes in: DESIGNED — A semantic query from Context Retrieval. [MAP C-INDEX]
- Does: DESIGNED — Supplies meaning-distance neighbors as semantic matches, keeping their evidential role distinct from same-thread preceding turns. [MAP C-INDEX] [V10 §7F]
- Gives out: DESIGNED — Ranked semantic neighbors; a genuine lack of relevant results is distinguished from index error, stale/incomplete index, timeout or unreachable service. [MAP C-INDEX] [V10 §7F]
- Must never: DESIGNED — Claim successful retrieval after a system failure, treat a semantic match as direct context, override positional context silently, or call similarity proof of relevance. [V10 §7F]
- Fails closed by: DESIGNED — A system failure is reported as index error, stale or incomplete index, timeout or unreachable service, never as successful retrieval or as a genuine lack of results. [MAP C-INDEX] [V10 §7F]

TOGETHER
- Fed by: DESIGNED — C-INDEX.1 — nh_roots_v1: supplies the current clean-root semantic index to the designed retrieval route. [MAP C-INDEX]
- Gated by: DESIGNED — C-7F — Context Retrieval (§7F): the owning mode determines the bounded retrieval parameters and preserves the separate semantic channel. [V10 §7F]
- Changes: DESIGNED — C-7F — Context Retrieval (§7F): supplies ranked neighbors to its semantic context channel; retrieval-event logging remains with that owner. [MAP C-INDEX]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | A semantic query from Context Retrieval. | supplies the clean-index search surface for the semantic channel. | Ranked semantic neighbors; a genuine lack of relevant results is distinguished from index error, stale/incomplete index, timeout or unreachable service. | [MAP C-INDEX] [V10 §7F] |

SUB-PARTS: NONE

### C-INDEX.6 — Index operation records
Stamp: DESIGNED    Source: [MAP C-INDEX] [V10 §0B]

ALONE
- What it is: DESIGNED — The mandatory operational record of every rebuild and every index mutation. [MAP C-INDEX]
- Takes in: DESIGNED — The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. [MAP C-INDEX]
- Does: DESIGNED — Records each rebuild with that metadata and each index mutation, one permanent record per real operation. [MAP C-INDEX] [V10 §0B]
- Gives out: DESIGNED — Connected, append-only records available as living memory under applicable access and authorization rules. [V10 §0B] [MAP C-INDEX]
- Must never: DESIGNED — Leave a rebuild or mutation silent, destroy its trace, treat the log as another evidential vote, or automatically generate an endless chain of logs about logs. [V10 §0B]
- Fails closed by: DESIGNED — A component without its traceable operation record is incomplete by design and is not adopted. [V10 §0B]

TOGETHER
- Fed by: DESIGNED — C-INDEX.6.1 — Rebuild source store: identifies where this operation obtained its roots. [MAP C-INDEX]
- Fed by: DESIGNED — C-INDEX.6.2 — Rebuild expected count: supplies the root count expected for the operation. [MAP C-INDEX]
- Fed by: DESIGNED — C-INDEX.6.3 — Rebuild actual count: supplies the root count actually handled. [MAP C-INDEX]
- Fed by: DESIGNED — C-INDEX.6.4 — Rebuild embedding model: identifies the model used in this operation. [MAP C-INDEX]
- Fed by: DESIGNED — C-INDEX.6.5 — Rebuild destination collection: identifies the collection affected by the rebuild. [MAP C-INDEX]
- Fed by: DESIGNED — C-INDEX.6.6 — Rebuild timing: supplies this operation's timing. [MAP C-INDEX]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): a permanent index-operation record does not bypass access or protection rules. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-INDEX]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): identity/security authorization applies where required. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | every rebuild and index mutation requires its traceable operation record. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 2 · DESIGNED | C-INDEX.6.1 — Rebuild source store | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | each rebuild requires its source-store metadata. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 3 · DESIGNED | C-INDEX.6.2 — Rebuild expected count | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | expected and actual counts must both be recorded for the rebuild. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 4 · DESIGNED | C-INDEX.6.3 — Rebuild actual count | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | the rebuild record requires the actual count as well as the expectation. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 5 · DESIGNED | C-INDEX.6.4 — Rebuild embedding model | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | every rebuild record must identify its embedding model. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 6 · DESIGNED | C-INDEX.6.5 — Rebuild destination collection | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | the destination must be recorded for each rebuild. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |
| 7 · DESIGNED | C-INDEX.6.6 — Rebuild timing | The actual operation, its source store, expected count, actual count, embedding model, destination collection and timing. | each rebuild requires recorded timing. | Connected, append-only records available as living memory under applicable access and authorization rules. | [MAP C-INDEX] [V10 §0B] |

SUB-PARTS: C-INDEX.6.1 — Rebuild source store; C-INDEX.6.2 — Rebuild expected count; C-INDEX.6.3 — Rebuild actual count; C-INDEX.6.4 — Rebuild embedding model; C-INDEX.6.5 — Rebuild destination collection; C-INDEX.6.6 — Rebuild timing

### C-INDEX.6.1 — Rebuild source store
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The source-store component of a rebuild's operation record. [MAP C-INDEX]
- Takes in: DESIGNED — The root store used by that rebuild. [MAP C-INDEX]
- Does: DESIGNED — Preserves which source store supplied the operation. [MAP C-INDEX]
- Gives out: DESIGNED — Recorded source-store provenance for the rebuild. [MAP C-INDEX]
- Must never: DESIGNED — Leave the rebuild's source store unrecorded. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: each rebuild requires its source-store metadata. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | The root store used by that rebuild. | identifies where this operation obtained its roots. | Recorded source-store provenance for the rebuild. | [MAP C-INDEX] |

SUB-PARTS: NONE

### C-INDEX.6.2 — Rebuild expected count
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The expected root count retained with a rebuild record. [MAP C-INDEX]
- Takes in: DESIGNED — The root count expected for the operation. [MAP C-INDEX]
- Does: DESIGNED — Records that expectation alongside the actual count. [MAP C-INDEX]
- Gives out: DESIGNED — The preserved expected count for comparison with what the rebuild handled. [MAP C-INDEX]
- Must never: DESIGNED — Omit the expected count from the rebuild's required metadata. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: expected and actual counts must both be recorded for the rebuild. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | The root count expected for the operation. | supplies the root count expected for the operation. | The preserved expected count for comparison with what the rebuild handled. | [MAP C-INDEX] |

SUB-PARTS: NONE

### C-INDEX.6.3 — Rebuild actual count
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The actual root count recorded for a rebuild. [MAP C-INDEX]
- Takes in: DESIGNED — The count actually handled by the operation. [MAP C-INDEX]
- Does: DESIGNED — Retains that actual count with the expected count. [MAP C-INDEX]
- Gives out: DESIGNED — A recorded account of the rebuild's actual count. [MAP C-INDEX]
- Must never: DESIGNED — Leave the actual count absent from the operation record. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: the rebuild record requires the actual count as well as the expectation. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | The count actually handled by the operation. | supplies the root count actually handled. | A recorded account of the rebuild's actual count. | [MAP C-INDEX] |

SUB-PARTS: NONE

### C-INDEX.6.4 — Rebuild embedding model
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The embedding-model provenance kept for each rebuild. [MAP C-INDEX]
- Takes in: DESIGNED — The embedding model used in the operation. [MAP C-INDEX]
- Does: DESIGNED — Records the operation's model with its other rebuild metadata. [MAP C-INDEX]
- Gives out: DESIGNED — A traceable association between the rebuild and its embedding model. [MAP C-INDEX]
- Must never: DESIGNED — Leave the model used by the rebuild unrecorded. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: every rebuild record must identify its embedding model. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | The embedding model used in the operation. | identifies the model used in this operation. | A traceable association between the rebuild and its embedding model. | [MAP C-INDEX] |

SUB-PARTS: NONE

### C-INDEX.6.5 — Rebuild destination collection
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The destination-collection provenance of the rebuild. [MAP C-INDEX]
- Takes in: DESIGNED — The Chroma collection used as this operation's destination. [MAP C-INDEX]
- Does: DESIGNED — Keeps the destination collection in the rebuild's record. [MAP C-INDEX]
- Gives out: DESIGNED — A preserved record of which collection the operation targeted. [MAP C-INDEX]
- Must never: DESIGNED — Omit the destination collection from the required rebuild metadata. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: the destination must be recorded for each rebuild. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | The Chroma collection used as this operation's destination. | identifies the collection affected by the rebuild. | A preserved record of which collection the operation targeted. | [MAP C-INDEX] |

SUB-PARTS: NONE

### C-INDEX.6.6 — Rebuild timing
Stamp: DESIGNED    Source: [MAP C-INDEX]

ALONE
- What it is: DESIGNED — The timing metadata preserved for a rebuild operation. [MAP C-INDEX]
- Takes in: DESIGNED — That rebuild's timing. [MAP C-INDEX]
- Does: DESIGNED — Records the timing with the rebuild's source, counts, model and destination. [MAP C-INDEX]
- Gives out: DESIGNED — Preserved timing associated with the actual rebuild. [MAP C-INDEX]
- Must never: DESIGNED — Leave timing out of the mandatory rebuild record. [MAP C-INDEX]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-INDEX.6 — Index operation records: each rebuild requires recorded timing. [MAP C-INDEX]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-INDEX.6 — Index operation records | That rebuild's timing. | supplies this operation's timing. | Preserved timing associated with the actual rebuild. | [MAP C-INDEX] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece continuation entries

Both endpoints are named together; the earlier files remain unchanged.

| Using card | Defining or supplying card | Reciprocal entry | Source |
|---|---|---|---|
| C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the 5,521 clean roots used to rebuild the index. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] [V10 §5 / Accretive store + tooling] |
| C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the clean-root material used by the index. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] |
| C-INDEX.1.2 — Cosine distance | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Gated by: semantic matches retain their distinct provenance and cannot silently override positional context. | [V10 §7F] |
| C-INDEX.2 — nh_rebuild_chroma.py | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the clean roots for the rebuild. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Chroma `nh_roots_v1` row] |
| C-INDEX.2.1 — --dry-run | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the clean-root material for the small test. | [V10 §5 / Accretive store + tooling] |
| C-INDEX.5 — Semantic retrieval interface | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Gated by: the owning mode determines the bounded retrieval parameters and preserves the separate semantic channel. | [V10 §7F] |
| C-INDEX.5 — Semantic retrieval interface | C-7F — Context Retrieval (§7F) | DESIGNED — USED BY continuation for Changes: supplies ranked neighbors to its semantic context channel; retrieval-event logging remains with that owner. | [MAP C-INDEX] |
| C-INDEX.6 — Index operation records | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: a permanent index-operation record does not bypass access or protection rules. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-INDEX] |
| C-INDEX.6 — Index operation records | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — USED BY continuation for Gated by: identity/security authorization applies where required. | [MAP C-INDEX] |
| C-7F — Context Retrieval (§7F) | C-INDEX — Chroma `nh_roots_v1` + `all-MiniLM-L6-v2` (§5, §16) | DESIGNED — C-7F's semantic-channel use is recorded in C-INDEX's USED BY table; its Fed by counterpart is carried to CH05-c. | [MAP C-INDEX] [V10 §7F] |

## Appendix A carry-forward — this piece

| Part | Field | Occurrence | Value |
|---|---|---|---|
| C-INDEX.1 — nh_roots_v1 | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.1 — nh_roots_v1 | Changes | 1 | NOT DECIDED |
| C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.1.1 — all-MiniLM-L6-v2 embeddings | Changes | 1 | NOT DECIDED |
| C-INDEX.1.2 — Cosine distance | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.1.2 — Cosine distance | Changes | 1 | NOT DECIDED |
| C-INDEX.2 — nh_rebuild_chroma.py | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.2.1 — --dry-run | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.2.1 — --dry-run | Changes | 1 | NOT DECIDED |
| C-INDEX.3 — Old-collection protection | Changes | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | Takes in | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | Gives out | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | Fed by | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | Changes | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | Takes in | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | Gives out | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | Fed by | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | Changes | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | Takes in | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | Gives out | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | Fed by | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | Changes | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | Gives out | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | Changes | 1 | NOT DECIDED |
| C-INDEX.4.1 — Changed rebuild behavior declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.1 — Changed rebuild behavior declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.1 — Changed rebuild behavior declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.2 — Source and expected-count declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.2 — Source and expected-count declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.2 — Source and expected-count declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.3 — Embedding-model declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.3 — Embedding-model declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.3 — Embedding-model declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.4 — Destination declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.4 — Destination declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.4 — Destination declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.5 — Record-treatment declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.5 — Record-treatment declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.5 — Record-treatment declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.6 — Dry-run-use declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.6 — Dry-run-use declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.6 — Dry-run-use declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.7 — Retrieval-check declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.7 — Retrieval-check declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.7 — Retrieval-check declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.4.8 — Gold-rerun declaration | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.4.8 — Gold-rerun declaration | Fed by | 1 | NOT DECIDED |
| C-INDEX.4.8 — Gold-rerun declaration | Changes | 1 | NOT DECIDED |
| C-INDEX.6 — Index operation records | Changes | 1 | NOT DECIDED |
| C-INDEX.6.1 — Rebuild source store | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.1 — Rebuild source store | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.1 — Rebuild source store | Changes | 1 | NOT DECIDED |
| C-INDEX.6.2 — Rebuild expected count | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.2 — Rebuild expected count | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.2 — Rebuild expected count | Changes | 1 | NOT DECIDED |
| C-INDEX.6.3 — Rebuild actual count | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.3 — Rebuild actual count | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.3 — Rebuild actual count | Changes | 1 | NOT DECIDED |
| C-INDEX.6.4 — Rebuild embedding model | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.4 — Rebuild embedding model | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.4 — Rebuild embedding model | Changes | 1 | NOT DECIDED |
| C-INDEX.6.5 — Rebuild destination collection | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.5 — Rebuild destination collection | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.5 — Rebuild destination collection | Changes | 1 | NOT DECIDED |
| C-INDEX.6.6 — Rebuild timing | Fails closed by | 1 | NOT DECIDED |
| C-INDEX.6.6 — Rebuild timing | Fed by | 1 | NOT DECIDED |
| C-INDEX.6.6 — Rebuild timing | Changes | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-INDEX.3.1 — nh_reality_core | USED BY row 1 / Changes there | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-INDEX.3.2 — nh_test_asm | USED BY row 1 / Changes there | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-INDEX.3.3 — nh_simulation_core | USED BY row 1 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 1 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 2 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 3 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 4 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 5 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 6 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 7 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 8 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 9 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 10 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 11 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 12 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 13 / Changes there | 1 | NOT DECIDED |
| C-INDEX.4 — Rebuild change boundary | USED BY row 14 / Changes there | 1 | NOT DECIDED |

## Source coverage and explicit deferrals

| Source scope | Card or later piece | Coverage boundary |
|---|---|---|
| V10 status table, Chroma nh_roots_v1, rebuild utility and old nh_reality_core rows | C-INDEX; .1; .1.1; .1.2; .2; .2.1; .3.1 | Only the expressly built collection, embedding/metric configuration and rebuild/dry-run behavior receive BUILT. |
| V10 §5, physical Chroma stores and rebuild entry | C-INDEX.1–.3.3 | All four collection names and recorded counts; current embedding model; ten-root dry-run and retrieval check; full-run count and duration; old collections untouched. |
| V10 §6A, THREE-LAYER ARCHITECTURE, Layer 1 and Layer 3 paragraphs | C-INDEX.1; .3.1 | Active clean index distinguished from the retained old index; no claim that the old collection is the new retrieval source. |
| V10 §6A, PROTECTED FILES AND STORES, rebuild and Chroma paragraphs | C-INDEX.3; .4 | Protected code boundary, all eight proposed-change declarations, separate authorization and protected collections. |
| CR §4B, CHROMA COLLECTIONS; §7 Layer 3 rebuild paragraph | C-INDEX.3–.4 | Current retrieval collection and no silent rename, overwrite, merge, delete or migration of old collections. |
| MAP C-INDEX, entire card | C-INDEX and descendants | DUMB meaning-distance tool; roots-to-index and query-to-neighbors interface; old-collection protection; each rebuild and mutation logged with all named metadata. |
| V10 §7F, semantic-channel meaning and system-failure distinction | C-INDEX.5; full retrieval provenance, modes, parameters, ceilings and fallback mechanics left for CH05-c C-7F | Semantic similarity is not preceding-turn context or proof of relevance. Index error, stale/incomplete index, timeout and unreachable service remain failures, distinct from a genuine empty result. |
| V10 §16, TWO MODELS TWO JOBS paragraph | C-INDEX.1.1; general model layer left for CH10-b C-16 | Embedding search and mouth wording are separate jobs; search first, word last. |
| V10 §0B, whole operational-law section | C-INDEX.6 and its metadata fields; shared log lifecycle remains in CH02 | One real operation/one log, no silence/destruction/double evidence or automatic recursive logging; access/authorization remains applicable. |
| Existing CH03-a C-STORE USED BY entry for C-INDEX | C-INDEX Fed by C-STORE; continuation row | The built clean-root supply relationship is reciprocated without modifying CH03-a. |

## Review of plain gates

| Card | Reason no other card is named |
|---|---|
| C-INDEX.4 — Rebuild change boundary | Ness's explicit authorization is a person's act, permitted as a plain gate by lessons 3.3. |

## Coverage matrix — carried source inventory

The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped reread for CH03-k; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-k; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped reread for CH03-k; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: C-ENGINE-C.7. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Read whole for CH03-j | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Newly read whole for this correction, all 1,938 lines; pinned Git blob verified; Chapter 3-c focused retry/malformed searches and §§2.8/3.7 excerpts; prior whole-read credit retained | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.10. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Detailed source landing map

| Bridge section | Cards in this piece |
|---|---|
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |



## READ RECORD

The source files below match their Git blobs at `6a7160ba688ba4e433a31899162815df7e2bab17`. The complete scoped passages listed in the source map were reopened. No source file receives a new whole-read claim in this piece; earlier whole-read credit remains in the preceding chapters. Searches in Decision Defaults were discovery only and supplied no new behavior. Contract §§5–11 were reopened before writing; §11.3 is reopened after writing for the checks below. The lessons sheet and run instructions were read in full.

| Source file | SHA-256 |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/cursorrules` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |

Instruction fingerprints:
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` — SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` — SHA-256 `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` — SHA-256 `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |
| CH03-j | `0b2bb5079af523e3f101705704316b1092f4a536575eff11ff020bd1eaa13a20` |

### READ-folder files not yet read whole

The pending list contains 94 files after the whole-read updates recorded for this piece. Scoped rereads do not remove a pending entry; the ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 27 behavior cards reviewed; delivery and source-status records remain outside behavior boxes.
§1.4 every gap written as NOT DECIDED: PASS — 89 empty fields/cells and exactly matching register entries.
§1.5 conflicts marked, none resolved: PASS — 0 new conflicts; earlier conflict records unchanged.
§3 exactly one stamp per line: PASS — 27 headers, 199 populated fields and 56 USED BY rows checked; empty boxes use only NOT DECIDED.
§4 every behavior line cited in the exact format: PASS — 17 distinct citations resolve in pinned sections; all populated fields and USED BY rows cited; support reviewed manually.
§5.4 one name per thing: PASS — 27 non-colliding IDs, official names and established sub-part names checked.
§6 all template fields present, in order, for every part: PASS — 27 templates and 268 field lines checked.
§6.3 reciprocity within this chapter: PASS — 54 internal links reciprocated; 9 outward links and 1 documented incoming uses covered by 10 rows naming both ends.
§6.4 every decided detail written in, no citation used in place of content: PASS — All four collection names, their recorded counts, the embedding model, cosine metric, rebuild utility, 10-root dry-run, recorded full-run duration, eight protected-change declarations and six rebuild-record metadata members are represented. No vector dimension, metric threshold, runtime API or logging format is inferred. Full context-retrieval mechanics are assigned to CH05-c.
§6.5 sub-parts recursed to the bottom: PASS — 27 cards; source-map scope and reuse of established atomic cards manually reviewed.
§9 coverage matrix rows added for every file used: PASS — 3 pinned source identities and corresponding coverage entries checked; current placement/deferral table included.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all behavior boxes reviewed; source-defined approval conditions are descriptions of the system boundary.
Files read whole for this chapter: None newly read whole. The lessons sheet and run instructions were read in full; contract §§5–11 were reopened before writing and §11.3 afterward. Other source reads are the scoped sections in the source map, without a new whole-file claim.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 27 |
| field_lines | 268 |
| populated_fields | 199 |
| not_decided_fields_and_cells | 89 |
| used_by_rows | 56 |
| relationships | 63 |
| internal_relationships | 54 |
| external_relationships | 9 |
| continuation_rows | 10 |
| plain_gates | 1 |
| step_cards | 3 |
| source_names_checked | 23 |
| unique_citations | 17 |
| source_identities | 3 |
| earlier_identities | 13 |
| pending_source_paths | 94 |
| built_field_lines | 37 |
| misfiled_scan_fields | 268 |
| empty_restriction_failure_gate_boxes_reviewed | 21 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 at writing; audit 1B later confirmed errors, corrected in round 4B |

Manual review accompanying the mechanical scan:

- All boxes reviewed against the pinned status rows and scoped source passages. The index, embeddings, metric, rebuild, dry-run and old nh_reality_core existence match explicit V10 BUILT rows. The dry-run-before-full-rebuild requirement is DESIGNED: the sources do not establish an implemented automatic gate. Retrieval routing, declarations, logging and old-collection authorization remain DESIGNED.
- Reviewed every field and USED BY row. The protected-edit stop without confirmation/declarations is filled from its explicit precondition. Remaining empty failure boxes have no stated failure mechanism in their cited source; V10 §7F explicitly leaves system-failure fallback undesigned. The per-declaration and log-field sources require those values but define no separate failure transition or serialization.
- All four collection names, their recorded counts, the embedding model, cosine metric, rebuild utility, 10-root dry-run, recorded full-run duration, eight protected-change declarations and six rebuild-record metadata members are represented. No vector dimension, metric threshold, runtime API or logging format is inferred. Full context-retrieval mechanics are assigned to CH05-c.
- Direct prohibitions preserve the named collection restrictions. The protected code-change boundary is N.H source behavior allowed by the contract; no Master-21 writing, auditing or upload workflow appears in behavior boxes.
- Checked counts, BUILT boundaries, source pin, exact names and source/file coverage. The cumulative inventory now carries the completed Writing 1 contributions and the previous pending-read list without resetting either. The C-7F incoming use is a continuation to its future chapter, not a claim that its card already exists.

All named source paths were checked at the fixed pin. Runtime/store names are checked against source documentation; this is not a live N.H filesystem check. P-MAIN has no direct C-INDEX step. The semantic-context use and side-path placements continue through C-7F in CH05-c and CH11. The wording scan covers the whole file. The count table is compared with a final recount after this block is appended.
