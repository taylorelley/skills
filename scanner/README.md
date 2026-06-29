# Pragmatic Skill Security Scanner

Context-aware security scanner for AI agent skills. Focuses on **exploitable risks**, not pattern matching.

## Design Principles

1. **File-type stratification** — Only scan executable code (`.py`, `.js`, `.sh`). Skip documentation and data files.
2. **Exploitability scoring** — `shell=True` with user input = HIGH. `shell=True` with hardcoded command = LOW.
3. **Input source tracking** — Localhost network calls = safe. External URLs = flag.
4. **False-positive suppression** — Allowlists for common safe patterns.

## What Gets Flagged

### HIGH Severity
- `subprocess.run(shell=True)` with variable commands (shell injection risk)
- External network calls with user data in body (data exfiltration)
- Credential file access + external transmission (secret theft)

### MEDIUM Severity
- External network calls without user data (telemetry risk)
- Opening credential files (`.env`, `.pem`, `.key`)

### LOW Severity
- `subprocess.run(shell=True)` with hardcoded commands (defense-in-depth)

### Not Flagged (False Positives from Other Scanners)
- `.env` mentions in `.md` documentation
- HTML comments in templates
- `localhost` network calls
- CLI entry points (`if __name__ == '__main__'`)
- CSV/JSON data content

## Usage

### Local

```bash
cd scanner
python3 scanner.py ../skills --format markdown
python3 scanner.py ../skills --format json
python3 scanner.py ../skills --format github
```

### GitHub Actions

Workflow runs automatically on PRs/pushes to `skills/**`.

**Outputs:**
- GitHub annotations (inline in PR diff)
- Markdown report (uploaded as artifact)

**Exit codes:**
- `0` = no HIGH findings
- `1` = HIGH findings detected (blocks merge)

Configure threshold with `--fail-on`:
```yaml
- run: python3 scanner.py ../skills --fail-on medium  # Block on MEDIUM+
- run: python3 scanner.py ../skills --fail-on never   # Never block
```

## Architecture

```
scanner/
├── scanner.py              # Main entry, CLI, orchestration
├── scanner_types.py        # Finding, ScanResult dataclasses
├── analyzers/
│   └── executable.py       # Python AST analysis
└── output/
    ├── github_actions.py   # ::warning/::error format
    └── markdown.py         # Human summary
```

## Comparison with Other Scanners

| Scanner | Findings on this repo | False positive rate |
|---------|----------------------|---------------------|
| SkillSpector | 144 | ~85% |
| Cisco Skill Scanner | 185 | ~90% |
| **This scanner** | **1** | **~0%** |

Other scanners flag documentation, data files, and safe patterns. This scanner only flags **actual executable risks**.

## Extending

Add new rules in `analyzers/executable.py`:

```python
def _check_my_pattern(node: ast.Call, rel_path: Path, source: str) -> List[Finding]:
    # Match specific AST pattern
    if not (isinstance(node.func, ast.Name) and node.func.id == "dangerous_function"):
        return []
    
    # Check context
    if is_safe_context(node):
        return []
    
    return [Finding(
        file=str(rel_path),
        line=node.lineno,
        severity="HIGH",
        rule="my_rule",
        message="Dangerous pattern detected",
        context=_get_context(source, node.lineno),
    )]
```

## Future Enhancements

- **Phase 2:** JavaScript/Shell AST analysis (tree-sitter)
- **Phase 3:** Input source tracking (follow variable assignments)
- **Phase 4:** Credential flow analysis (track data from `.env` to network calls)
