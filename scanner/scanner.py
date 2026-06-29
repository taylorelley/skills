#!/usr/bin/env python3
"""Pragmatic skill security scanner for AI agent skills."""

import argparse
import json
import sys
from pathlib import Path
from typing import List
from dataclasses import asdict

from scanner_types import Finding, ScanResult
from analyzers.executable import analyze_python_file
from output.github_actions import format_github_actions
from output.markdown import format_markdown


def should_scan_file(path: Path) -> bool:
    """File-type stratification: only scan executable code."""
    suffix = path.suffix.lower()
    
    # Executable code: full analysis
    if suffix in {".py", ".js", ".mjs", ".cjs", ".sh", ".bash"}:
        return True
    
    # Documentation: skip (patterns in docs are not executable)
    if suffix in {".md", ".txt", ".rst"}:
        return False
    
    # Data files: skip (CSV/JSON content is not code)
    if suffix in {".csv", ".json", ".yaml", ".yml", ".toml"}:
        return False
    
    return False


def scan_skill(skill_dir: Path) -> ScanResult:
    """Scan a single skill directory."""
    findings: List[Finding] = []
    files_scanned = 0
    executable_files = 0
    
    for path in skill_dir.rglob("*"):
        if not path.is_file():
            continue
        
        files_scanned += 1
        
        if not should_scan_file(path):
            continue
        
        executable_files += 1
        
        # Analyze based on file type
        if path.suffix == ".py":
            findings.extend(analyze_python_file(path, skill_dir))
    
    return ScanResult(
        skill_name=skill_dir.name,
        findings=findings,
        files_scanned=files_scanned,
        executable_files=executable_files,
    )


def scan_skills_directory(skills_dir: Path) -> List[ScanResult]:
    """Scan all skills in directory."""
    results = []
    
    for skill_path in sorted(skills_dir.iterdir()):
        if not skill_path.is_dir():
            continue
        
        # Skip hidden directories
        if skill_path.name.startswith("."):
            continue
        
        result = scan_skill(skill_path)
        results.append(result)
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Pragmatic skill security scanner")
    parser.add_argument("directory", type=Path, help="Skills directory to scan")
    parser.add_argument(
        "--format",
        choices=["json", "github", "markdown"],
        default="markdown",
        help="Output format",
    )
    parser.add_argument(
        "--fail-on",
        choices=["high", "medium", "low", "never"],
        default="high",
        help="Exit with error if findings at this severity or higher",
    )
    
    args = parser.parse_args()
    
    if not args.directory.exists():
        print(f"Error: {args.directory} does not exist", file=sys.stderr)
        sys.exit(1)
    
    results = scan_skills_directory(args.directory)
    
    # Output results
    if args.format == "json":
        output = {
            "skills": [
                {
                    "name": r.skill_name,
                    "max_severity": r.max_severity,
                    "findings_count": len(r.findings),
                    "files_scanned": r.files_scanned,
                    "executable_files": r.executable_files,
                    "findings": [asdict(f) for f in r.findings],
                }
                for r in results
            ]
        }
        print(json.dumps(output, indent=2))
    
    elif args.format == "github":
        print(format_github_actions(results))
    
    elif args.format == "markdown":
        print(format_markdown(results))
    
    # Exit code based on severity threshold
    if args.fail_on != "never":
        severity_order = {"high": 3, "medium": 2, "low": 1}
        threshold = severity_order[args.fail_on]
        
        for result in results:
            for finding in result.findings:
                finding_level = severity_order.get(finding.severity.lower(), 0)
                if finding_level >= threshold:
                    sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
