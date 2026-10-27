#!/usr/bin/env python3
"""Count the complete project input and optionally export that exact input."""
import argparse
from pathlib import Path
import sys

try:
    import tiktoken
except ImportError:
    sys.exit("Install tools/requirements.txt in an environment outside this project.")

ROOT = Path(__file__).resolve().parents[1]
ROOT_METADATA = {".git", ".agents", ".aws", ".codex"}
LIMIT = 35_000


def collect(root):
    files = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if relative.parts[0] in ROOT_METADATA or "__pycache__" in relative.parts:
            continue
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed in the input: {relative}")
        if path.is_file():
            try:
                body = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as error:
                raise ValueError(f"Cannot count a non-UTF-8 file: {relative}") from error
            files.append((relative.as_posix(), body))
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, help="Export outside this project")
    args = parser.parse_args()
    if args.bundle and args.bundle.resolve().is_relative_to(ROOT):
        parser.error("Export outside the project to avoid duplicating its input.")
    try:
        files = collect(ROOT)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    bundle = "\n".join(f"# File: {name}\n\n{body}\n" for name, body in files)
    failures = []
    for name, body in files:
        if any(character in body for character in "\u2013\u2014\u2018\u2019\u201c\u201d"):
            failures.append(f"Use plain punctuation in {name}")
    print(f"Files: {len(files)}; UTF-8 bytes with file labels: {len(bundle.encode('utf-8'))}")
    for encoding in ("cl100k_base", "o200k_base"):
        tokens = len(tiktoken.get_encoding(encoding).encode(bundle, disallowed_special=()))
        print(f"{encoding}: {tokens:,} / {LIMIT:,} tokens")
        if tokens > LIMIT:
            failures.append(f"{encoding} must stay at or below {LIMIT:,} tokens")
    for failure in failures:
        print(failure, file=sys.stderr)
    if failures:
        return 1
    if args.bundle:
        args.bundle.write_text(bundle, encoding="utf-8")
        print(f"Exported {args.bundle.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
