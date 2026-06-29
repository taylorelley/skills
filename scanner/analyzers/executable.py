"""Python AST analyzer for executable code."""

import ast
from pathlib import Path
from typing import List

from scanner_types import Finding


def analyze_python_file(file_path: Path, skill_dir: Path) -> List[Finding]:
    """Analyze Python file for security issues."""
    findings = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=str(file_path))
    except Exception as e:
        # Skip files that can't be parsed
        return findings
    
    rel_path = file_path.relative_to(skill_dir)
    
    for node in ast.walk(tree):
        # Check subprocess calls
        if isinstance(node, ast.Call):
            findings.extend(_check_subprocess_call(node, rel_path, source))
            findings.extend(_check_network_call(node, rel_path, source))
            findings.extend(_check_credential_access(node, rel_path, source))
    
    return findings


def _check_subprocess_call(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    """Check for dangerous subprocess patterns."""
    findings = []
    
    # Match subprocess.run/Popen/call with shell=True
    if not (isinstance(node.func, ast.Attribute) and 
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == "subprocess"):
        return findings
    
    method_name = node.func.attr
    if method_name not in {"run", "Popen", "call", "check_output", "check_call"}:
        return findings
    
    # Check for shell=True
    shell_true = False
    for keyword in node.keywords:
        if keyword.arg == "shell":
            if isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                shell_true = True
                break
    
    if shell_true:
        # Check if first arg is a variable (user input) vs string literal
        first_arg_is_literal = False
        if node.args and isinstance(node.args[0], ast.Constant):
            first_arg_is_literal = True
        
        if first_arg_is_literal:
            severity = "LOW"
            message = "shell=True with hardcoded command (defense-in-depth risk)"
        else:
            severity = "HIGH"
            message = "shell=True with variable command (potential shell injection)"
        
        findings.append(Finding(
            file=str(rel_path),
            line=node.lineno,
            severity=severity,
            rule="shell_injection",
            message=message,
            context=_get_context(source, node.lineno),
        ))
    
    return findings


def _check_network_call(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    """Check for external network calls."""
    findings = []
    
    # Only match specific network libraries
    # requests.get/post/put/delete
    if (isinstance(node.func, ast.Attribute) and
        isinstance(node.func.value, ast.Name) and
        node.func.value.id == "requests" and
        node.func.attr in {"get", "post", "put", "delete", "request", "head", "patch"}):
        
        findings.extend(_analyze_requests_call(node, rel_path, source))
        return findings
    
    # urllib.request.urlopen
    if (isinstance(node.func, ast.Attribute) and
        isinstance(node.func.value, ast.Attribute) and
        isinstance(node.func.value.value, ast.Name) and
        node.func.value.value.id == "urllib" and
        node.func.value.attr == "request" and
        node.func.attr == "urlopen"):
        
        findings.extend(_analyze_urllib_call(node, rel_path, source))
        return findings
    
    # httpx.get/post
    if (isinstance(node.func, ast.Attribute) and
        isinstance(node.func.value, ast.Name) and
        node.func.value.id == "httpx" and
        node.func.attr in {"get", "post", "put", "delete", "request", "head", "patch"}):
        
        findings.extend(_analyze_requests_call(node, rel_path, source))
        return findings
    
    return findings


def _analyze_requests_call(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    """Analyze requests/httpx library call."""
    findings = []
    
    if not node.args:
        return findings
    
    first_arg = node.args[0]
    url_value = _extract_string_value(first_arg)
    
    if not url_value:
        return findings
    
    # Check if localhost (safe) vs external (flag)
    is_localhost = any(pattern in url_value for pattern in [
        "localhost", "127.0.0.1", "0.0.0.0", "::1"
    ])
    
    if is_localhost:
        return findings
    
    # External network call
    findings.append(Finding(
        file=str(rel_path),
        line=node.lineno,
        severity="MEDIUM",
        rule="external_network",
        message=f"External network call to {url_value[:80]}",
        context=_get_context(source, node.lineno),
    ))
    
    return findings


def _analyze_urllib_call(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    """Analyze urllib.urlopen call."""
    findings = []
    
    if not node.args:
        return findings
    
    first_arg = node.args[0]
    url_value = _extract_string_value(first_arg)
    
    if not url_value:
        return findings
    
    is_localhost = any(pattern in url_value for pattern in [
        "localhost", "127.0.0.1", "0.0.0.0", "::1"
    ])
    
    if is_localhost:
        return findings
    
    findings.append(Finding(
        file=str(rel_path),
        line=node.lineno,
        severity="MEDIUM",
        rule="external_network",
        message=f"External network call to {url_value[:80]}",
        context=_get_context(source, node.lineno),
    ))
    
    return findings


def _extract_string_value(node) -> str:
    """Extract string value from AST node."""
    if isinstance(node, ast.Constant):
        return str(node.value)
    elif isinstance(node, ast.JoinedStr):
        # f-string
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(str(value.value))
        return "".join(parts)
    return ""


def _check_credential_access(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    """Check for credential file access."""
    findings = []
    
    # Match open() calls
    if not (isinstance(node.func, ast.Name) and node.func.id == "open"):
        return findings
    
    if not node.args:
        return findings
    
    first_arg = node.args[0]
    path_value = _extract_string_value(first_arg)
    
    if not path_value:
        return findings
    
    # Check for credential file patterns
    credential_patterns = [".env", ".pem", ".key", "credentials", "secret"]
    
    if any(pattern in path_value.lower() for pattern in credential_patterns):
        findings.append(Finding(
            file=str(rel_path),
            line=node.lineno,
            severity="MEDIUM",
            rule="credential_access",
            message=f"Opening credential file: {path_value}",
            context=_get_context(source, node.lineno),
        ))
    
    return findings


def _get_context(source: str, lineno: int, context_lines: int = 2) -> str:
    """Get surrounding lines for context."""
    lines = source.split("\n")
    start = max(0, lineno - context_lines - 1)
    end = min(len(lines), lineno + context_lines)
    return "\n".join(lines[start:end])
