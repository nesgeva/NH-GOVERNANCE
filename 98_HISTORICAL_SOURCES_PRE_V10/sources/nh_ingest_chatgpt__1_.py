"""
nh_ingest_chatgpt.py — clean ingest of ChatGPT-export JSON into the accretive store.

Reads a ChatGPT conversations export (a list of conversation dicts), walks each
conversation's `mapping` tree in TRUE order (backward from current_node via parent
links, then reversed), and produces ONE clean root per qualifying message.

CLEAN means (fixing the old seed's mistake):
  - source_title goes in its OWN field, NOT glued into content
  - role (user/assistant) carried straight from author.role — never guessed
  - real message create_time used as the timestamp
  - content is the raw message text, untouched

DUMB on purpose: it copies and reorders. It does not interpret.

DRY_RUN = True  -> prints what it WOULD write, writes NOTHING.
DRY_RUN = False -> actually appends roots via nh_accretive_store.append_root.

A message is ingested ONLY if:
  - it has a message object
  - content_type == "text"
  - author.role in {"user", "assistant"}
  - the joined parts are non-empty after strip
Everything else (system, tool, empty, non-text) is skipped.
"""

import json
import sys
from datetime import datetime, timezone

# ---- CONFIG -------------------------------------------------------------
DRY_RUN = True                       # <- writes nothing while True
SOURCE_FILE = "conversations-002.json"
SUBJECT_TAG = "seed:conversations_002"   # provenance tag for this batch
KEEP_ROLES = {"user", "assistant"}
# -------------------------------------------------------------------------


def ordered_messages(conversation):
    """Rebuild the true message order for one conversation.

    Walk backward from current_node through parent links, then reverse.
    This follows the FINAL path of the conversation, skipping abandoned
    edit/regenerate branches.
    """
    mapping = conversation.get("mapping", {})
    node_id = conversation.get("current_node")

    # Fallback: if current_node is missing, find a leaf (node nothing points to as parent)
    if node_id is None or node_id not in mapping:
        children = {n.get("parent") for n in mapping.values()}
        leaves = [nid for nid in mapping if nid not in children]
        node_id = leaves[0] if leaves else None

    chain = []
    seen = set()
    while node_id is not None and node_id in mapping and node_id not in seen:
        seen.add(node_id)
        chain.append(mapping[node_id])
        node_id = mapping[node_id].get("parent")

    chain.reverse()   # was end->start; now start->end
    return chain


def message_to_root_fields(node, title):
    """Extract clean root fields from one mapping node, or None to skip."""
    msg = node.get("message")
    if not msg:
        return None

    author = msg.get("author") or {}
    role = author.get("role")
    if role not in KEEP_ROLES:
        return None

    content = msg.get("content") or {}
    if content.get("content_type") != "text":
        return None

    parts = content.get("parts") or []
    text = "\n".join(p for p in parts if isinstance(p, str)).strip()
    if not text:
        return None

    # timestamp: prefer the real message create_time (epoch seconds) -> ISO
    ct = msg.get("create_time")
    if isinstance(ct, (int, float)):
        ts = datetime.fromtimestamp(ct, tz=timezone.utc).isoformat()
    else:
        ts = datetime.now(timezone.utc).isoformat()

    return {
        "subject": SUBJECT_TAG,
        "content": text,
        "source_title": title,
        "role": role,            # carried, not guessed (see note below)
        "timestamp": ts,
    }


def main():
    with open(SOURCE_FILE, encoding="utf-8") as f:
        conversations = json.load(f)

    total = 0
    skipped_convs = 0
    sample = []

    for conv in conversations:
        title = conv.get("title") or "(untitled)"
        msgs = ordered_messages(conv)
        if not msgs:
            skipped_convs += 1
            continue
        for node in msgs:
            fields = message_to_root_fields(node, title)
            if fields is None:
                continue
            total += 1
            if len(sample) < 6:
                sample.append(fields)

            if not DRY_RUN:
                import nh_accretive_store as store
                store.append_root(
                    subject=fields["subject"],
                    content=fields["content"],
                    role=fields["role"],
                    source_title=fields["source_title"],
                    timestamp=fields["timestamp"],
                )

    print(f"SOURCE: {SOURCE_FILE}")
    print(f"conversations: {len(conversations)}  (skipped empty: {skipped_convs})")
    print(f"roots that WOULD be written: {total}")
    print(f"DRY_RUN = {DRY_RUN}  (writes nothing while True)\n")
    print("---- SAMPLE OF FIRST 6 ROOTS (in true order) ----")
    for i, r in enumerate(sample):
        print(f"\n[{i}] role={r['role']}  time={r['timestamp']}")
        print(f"    source_title: {r['source_title']}")
        print(f"    subject:      {r['subject']}")
        snippet = r["content"].replace("\n", " ")[:160]
        print(f"    content:      {snippet}")


if __name__ == "__main__":
    main()
