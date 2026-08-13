#!/usr/bin/env python3
"""Traceability gap checker for DO-178C / DO-278A projects.

Scans a project for `@req`, `@design`, and `@test` annotations and reports gaps in
both directions of the traceability chain:

  forward   requirement -> code, requirement -> test
  backward  code -> requirement, test -> requirement

Structural coverage tools do not find these gaps; they find untested *code*. A
requirement that nobody implemented, or a function that implements nothing anyone
asked for, is invisible to a coverage report and is exactly what an SOI review
looks for. Run this before you claim a traceability matrix is complete.

Usage:
    python3 trace_check.py [--project-root DIR] [--json] [--quiet]

Exit status is 1 when any gap is found, so this can gate a commit or a build.
Defaults follow the directory layout in AGENTS.md.template; override with the
--reqs / --tests / --src options if the project uses a different layout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Annotation forms accepted:  @req ID          @req ID, ID, ID
# Bare IDs are comma or whitespace separated; trailing prose after a colon is ignored.
ANNOTATION = re.compile(r"@(req|design|test|derived|parent)\s+([A-Za-z0-9\-_,\s]+)")
ID_TOKEN = re.compile(r"[A-Za-z]+(?:-[A-Za-z0-9]+)+")

C_KEYWORDS = {
    "if", "for", "while", "switch", "return", "typedef", "struct", "enum",
    "union", "else", "do", "case", "default", "sizeof", "static_assert",
}


@dataclass
class Requirement:
    ident: str
    path: Path
    status: str = ""
    parents: list[str] = field(default_factory=list)


@dataclass
class Function:
    name: str
    path: Path
    line: int
    reqs: list[str] = field(default_factory=list)
    derived: list[str] = field(default_factory=list)


@dataclass
class TestCase:
    ident: str
    path: Path
    reqs: list[str] = field(default_factory=list)


def extract(text: str, kind: str) -> list[str]:
    """Pull every ID referenced by a given annotation kind, in order, deduplicated."""
    found: list[str] = []
    for match in ANNOTATION.finditer(text):
        if match.group(1) != kind:
            continue
        for token in ID_TOKEN.findall(match.group(2)):
            if token not in found:
                found.append(token)
    return found


def collect_requirements(paths: list[Path]) -> dict[str, Requirement]:
    reqs: dict[str, Requirement] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        idents = extract(text, "req")
        if not idents:
            continue
        # The first @req in a requirement file is the requirement it defines;
        # later ones are references to other requirements.
        ident = idents[0]
        status = ""
        status_match = re.search(r"@status\s+(\S+)", text)
        if status_match:
            status = status_match.group(1)
        reqs[ident] = Requirement(
            ident=ident,
            path=path,
            status=status,
            parents=extract(text, "parent"),
        )
    return reqs


def collect_tests(paths: list[Path]) -> dict[str, TestCase]:
    tests: dict[str, TestCase] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        idents = extract(text, "test")
        if not idents:
            continue
        ident = idents[0]
        tests[ident] = TestCase(ident=ident, path=path, reqs=extract(text, "req"))
    return tests


def preceding_comment(lines: list[str], start: int) -> str:
    """Return the comment block immediately above line index `start`."""
    idx = start - 1
    while idx >= 0 and not lines[idx].strip():
        idx -= 1
    if idx < 0 or not lines[idx].strip().endswith("*/"):
        return ""
    end = idx
    while idx >= 0 and "/*" not in lines[idx]:
        idx -= 1
    return "\n".join(lines[max(idx, 0):end + 1])


def find_body_end(lines: list[str], brace_line: int) -> int:
    """Given the line holding a function's opening brace, find its closing brace."""
    depth = 0
    for idx in range(brace_line, len(lines)):
        depth += lines[idx].count("{") - lines[idx].count("}")
        if depth <= 0 and idx > brace_line - 1 and "{" in "".join(lines[brace_line:idx + 1]):
            return idx
    return len(lines) - 1


def collect_functions(paths: list[Path]) -> list[Function]:
    """Heuristic C function-definition scanner.

    Not a parser. It looks for a definition starting in column 0 whose parameter
    list closes and is followed by an opening brace. That covers ordinary
    safety-critical C, where the coding standard already forbids the exotic
    constructs a real parser would be needed for.
    """
    functions: list[Function] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        idx = 0
        while idx < len(lines):
            line = lines[idx]
            stripped = line.strip()
            starts_at_margin = line[:1] not in (" ", "\t", "", "#", "}", "/", "*")
            if not starts_at_margin or "(" not in line or stripped.endswith(";"):
                idx += 1
                continue
            first_word = re.match(r"[A-Za-z_]\w*", stripped)
            if not first_word or first_word.group(0) in C_KEYWORDS:
                idx += 1
                continue

            # Accumulate the signature until the parameter list closes.
            signature = line
            end_idx = idx
            while signature.count("(") > signature.count(")") and end_idx + 1 < len(lines):
                end_idx += 1
                signature += " " + lines[end_idx].strip()
            if signature.count("(") != signature.count(")"):
                idx += 1
                continue

            after = signature.split(")")[-1].strip()
            brace_line = end_idx
            if not after.startswith("{"):
                nxt = end_idx + 1
                while nxt < len(lines) and not lines[nxt].strip():
                    nxt += 1
                if nxt >= len(lines) or not lines[nxt].strip().startswith("{"):
                    idx += 1
                    continue
                brace_line = nxt

            name_match = re.findall(r"(\w+)\s*\(", signature)
            if not name_match:
                idx = brace_line + 1
                continue
            name = name_match[0]

            doc = preceding_comment(lines, idx)
            body_end = find_body_end(lines, brace_line)
            body = "\n".join(lines[brace_line:body_end + 1])
            scope = doc + "\n" + body

            functions.append(Function(
                name=name,
                path=path,
                line=idx + 1,
                reqs=extract(scope, "req"),
                derived=extract(scope, "derived"),
            ))
            idx = body_end + 1
    return functions


def resolve(root: Path, patterns: list[str]) -> list[Path]:
    out: list[Path] = []
    for pattern in patterns:
        out.extend(p for p in sorted(root.glob(pattern)) if p.is_file())
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--project-root", default=".", type=Path)
    parser.add_argument("--reqs", nargs="*", default=["docs/requirements/**/*.md"])
    parser.add_argument("--tests", nargs="*", default=["test/cases/**/*.md"])
    parser.add_argument("--src", nargs="*", default=["src/**/*.c", "src/**/*.h"])
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--quiet", action="store_true", help="print only gaps")
    args = parser.parse_args()

    root = args.project_root.resolve()
    if not root.is_dir():
        print(f"error: no such directory: {root}", file=sys.stderr)
        return 2

    requirements = collect_requirements(resolve(root, args.reqs))
    tests = collect_tests(resolve(root, args.tests))
    functions = collect_functions(resolve(root, args.src))

    implemented: dict[str, list[str]] = {}
    for fn in functions:
        for ident in fn.reqs:
            implemented.setdefault(ident, []).append(f"{fn.path.relative_to(root)}:{fn.line} {fn.name}()")

    tested: dict[str, list[str]] = {}
    for test in tests.values():
        for ident in test.reqs:
            tested.setdefault(ident, []).append(test.ident)

    gaps: dict[str, list[dict]] = {
        "requirement_not_implemented": [],
        "requirement_not_tested": [],
        "orphan_code": [],
        "dangling_test_reference": [],
        "dangling_code_reference": [],
    }

    for ident, req in sorted(requirements.items()):
        rel = str(req.path.relative_to(root))
        if ident not in implemented:
            gaps["requirement_not_implemented"].append({"id": ident, "defined_in": rel})
        if ident not in tested:
            gaps["requirement_not_tested"].append({"id": ident, "defined_in": rel})

    for fn in functions:
        if not fn.reqs and not fn.derived:
            gaps["orphan_code"].append({
                "function": fn.name,
                "location": f"{fn.path.relative_to(root)}:{fn.line}",
            })
        for ident in fn.reqs:
            if ident not in requirements:
                gaps["dangling_code_reference"].append({
                    "id": ident,
                    "location": f"{fn.path.relative_to(root)}:{fn.line}",
                })

    for test in sorted(tests.values(), key=lambda t: t.ident):
        for ident in test.reqs:
            if ident not in requirements:
                gaps["dangling_test_reference"].append({
                    "id": ident,
                    "test": test.ident,
                    "defined_in": str(test.path.relative_to(root)),
                })

    total = sum(len(v) for v in gaps.values())

    if args.json:
        print(json.dumps({
            "summary": {
                "requirements": len(requirements),
                "test_cases": len(tests),
                "functions": len(functions),
                "gaps": total,
            },
            "gaps": gaps,
        }, indent=2))
        return 1 if total else 0

    if not args.quiet:
        print(f"Scanned {root}")
        print(f"  requirements : {len(requirements)}")
        print(f"  test cases   : {len(tests)}")
        print(f"  functions    : {len(functions)}")
        print()

    labels = {
        "requirement_not_implemented": "FORWARD GAP — requirement with no implementing code",
        "requirement_not_tested": "FORWARD GAP — requirement with no test case",
        "orphan_code": "BACKWARD GAP — function with no @req or @derived annotation",
        "dangling_code_reference": "DANGLING — code cites a requirement that does not exist",
        "dangling_test_reference": "DANGLING — test cites a requirement that does not exist",
    }

    for key, label in labels.items():
        entries = gaps[key]
        if not entries:
            continue
        print(f"{label}  ({len(entries)})")
        for entry in entries:
            detail = "  ".join(f"{k}={v}" for k, v in entry.items())
            print(f"    {detail}")
        print()

    if total == 0:
        print("No traceability gaps found.")
        print("Note: this checks annotation linkage only. It does not verify that a test")
        print("actually exercises the requirement it claims, or that a requirement is correct.")
        return 0

    print(f"{total} gap(s) found. Each is a finding that must be resolved or justified")
    print("before the traceability matrix can be claimed complete.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
