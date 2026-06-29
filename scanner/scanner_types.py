"""Data types for scanner."""

from dataclasses import dataclass
from typing import List


@dataclass
class Finding:
    file: str
    line: int
    severity: str  # HIGH, MEDIUM, LOW, INFO
    rule: str
    message: str
    context: str = ""


@dataclass
class ScanResult:
    skill_name: str
    findings: List[Finding]
    files_scanned: int
    executable_files: int

    @property
    def max_severity(self) -> str:
        if not self.findings:
            return "SAFE"
        severities = [f.severity for f in self.findings]
        for s in ["HIGH", "MEDIUM", "LOW", "INFO"]:
            if s in severities:
                return s
        return "SAFE"
