#!/usr/bin/env python3
"""Syntax-check all runtime and Switch translation units from compile_commands.json."""
import json
import pathlib
import shlex
import subprocess

database = pathlib.Path("build-switch/compile_commands.json")
entries = json.loads(database.read_text(encoding="utf-8"))
selected = [
    entry for entry in entries
    if "runtime" in pathlib.PurePosixPath(entry["file"]).parts
    or "switch" in pathlib.PurePosixPath(entry["file"]).parts
]
if not selected:
    raise SystemExit("No runtime/Switch translation units found in compile_commands.json")

for entry in selected:
    args = entry.get("arguments") or shlex.split(entry["command"])
    cleaned = []
    skip_next = False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg == "-o":
            skip_next = True
            continue
        if arg == "-c":
            continue
        cleaned.append(arg)
    cleaned.append("-fsyntax-only")
    subprocess.run(cleaned, cwd=entry["directory"], check=True)

print(f"Runtime/Switch syntax checks passed: {len(selected)} translation units")
