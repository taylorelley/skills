"""GitHub Actions output formatter."""

from typing import List
from scanner_types import ScanResult


def format_github_actions(results: List[ScanResult]) -> str:
    """Format findings as GitHub Actions annotations."""
    lines = []
    
    total_findings = sum(len(r.findings) for r in results)
    skills_with_issues = sum(1 for r in results if r.findings)
    
    lines.append(f"# Scanned {len(results)} skills, found {total_findings} issues in {skills_with_issues} skills")
    lines.append("")
    
    for result in results:
        if not result.findings:
            continue
        
        lines.append(f"## {result.skill_name} ({result.max_severity})")
        lines.append("")
        
        for finding in result.findings:
            # GitHub Actions annotation format
            severity_map = {
                "HIGH": "error",
                "MEDIUM": "warning",
                "LOW": "notice",
                "INFO": "notice",
            }
            annotation_type = severity_map.get(finding.severity, "notice")
            
            # Format: ::type file={file},line={line}::{message}
            annotation = f"::{annotation_type} file={finding.file},line={finding.line}::[{finding.rule}] {finding.message}"
            lines.append(annotation)
        
        lines.append("")
    
    return "\n".join(lines)
