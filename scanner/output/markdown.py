"""Markdown output formatter."""

from typing import List
from scanner_types import ScanResult


def format_markdown(results: List[ScanResult]) -> str:
    """Format findings as human-readable markdown."""
    lines = []
    
    total_findings = sum(len(r.findings) for r in results)
    skills_with_issues = sum(1 for r in results if r.findings)
    
    lines.append("# Skill Security Scan Report")
    lines.append("")
    lines.append(f"**Skills scanned:** {len(results)}")
    lines.append(f"**Skills with issues:** {skills_with_issues}")
    lines.append(f"**Total findings:** {total_findings}")
    lines.append("")
    
    # Summary table
    lines.append("## Summary")
    lines.append("")
    lines.append("| Skill | Status | Severity | Findings |")
    lines.append("|-------|--------|----------|----------|")
    
    for result in results:
        status = "✅ SAFE" if not result.findings else "⚠️ ISSUES"
        lines.append(f"| {result.skill_name} | {status} | {result.max_severity} | {len(result.findings)} |")
    
    lines.append("")
    
    # Detailed findings
    if any(r.findings for r in results):
        lines.append("## Findings")
        lines.append("")
        
        for result in results:
            if not result.findings:
                continue
            
            lines.append(f"### {result.skill_name}")
            lines.append("")
            lines.append(f"- **Files scanned:** {result.files_scanned}")
            lines.append(f"- **Executable files:** {result.executable_files}")
            lines.append(f"- **Max severity:** {result.max_severity}")
            lines.append("")
            
            for finding in result.findings:
                severity_icon = {
                    "HIGH": "🔴",
                    "MEDIUM": "🟡",
                    "LOW": "🟢",
                    "INFO": "ℹ️",
                }.get(finding.severity, "•")
                
                lines.append(f"#### {severity_icon} {finding.severity}: {finding.rule}")
                lines.append("")
                lines.append(f"**File:** `{finding.file}:{finding.line}`")
                lines.append("")
                lines.append(f"**Message:** {finding.message}")
                lines.append("")
                
                if finding.context:
                    lines.append("**Context:**")
                    lines.append("```")
                    lines.append(finding.context)
                    lines.append("```")
                    lines.append("")
    
    return "\n".join(lines)
