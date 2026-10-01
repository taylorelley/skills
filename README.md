# Taylor's Skills

A curated collection of agent skills. All contributed skills are automatically security-scanned on every PR/push via a [GitHub Actions workflow](.github/workflows/skill-security-scan.yml) for shell injection, data exfiltration, and secret theft.

## Categories

### Design
UI/UX design, visual polish, and aesthetics.

- **[design-taste-frontend](skills/design/design-taste-frontend/)** — Anti-slop frontend skill for landing pages, portfolios, and redesigns. Reads the brief, infers the right design direction, and ships interfaces that don't look templated.
- **[frontend-design](skills/design/frontend-design/)** — Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and avoiding templated defaults.
- **[impeccable](skills/design/impeccable/)** — Designs and iterates production-grade frontend interfaces. Real working code, committed design choices, exceptional craft. Covers websites, dashboards, product UI, and reusable design systems.
- **[interface-kit](skills/design/interface-kit/)** — Implementation guide for accessible, performant, polished UI. Covers animation, spatial design, typography, color systems, and component craft.
- **[ui-ux-pro-max](skills/design/ui-ux-pro-max/)** — Comprehensive UI/UX design intelligence with 50+ styles, 161 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 10 stacks.

### Engineering
Code quality, testing, debugging, and architecture.

- **[diagnose](skills/engineering/diagnose/)** — Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **[improve-codebase-architecture](skills/engineering/improve-codebase-architecture/)** — Find deepening opportunities in a codebase, informed by the domain language and ADRs. Turns shallow modules into deep, testable, AI-navigable ones.
- **[junior-to-senior](skills/engineering/junior-to-senior/)** — Adversarial senior-engineer review for agent-generated plans. Grounds the critique in the live codebase and current best practices, then rewrites the plan at the right altitude.
- **[safety-critical](skills/engineering/safety-critical/)** — Safety-critical software engineering for aviation CNS/ATM under DO-178C and DO-278A: assurance levels, requirements, traceability, structural coverage, and reviews.
- **[tdd](skills/engineering/tdd/)** — Test-driven development with red-green-refactor loop. Tests should verify behavior through public interfaces, not implementation details.
- **[webapp-testing](skills/engineering/webapp-testing/)** — Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, capturing screenshots, and viewing browser logs.

### Framework
Framework-specific best practices and tooling.

- **[next-best-practices](skills/framework/next-best-practices/)** — Next.js best practices covering file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, and bundling.
- **[turborepo](skills/framework/turborepo/)** — Turborepo monorepo build system guidance. Triggers on turbo.json, task pipelines, dependsOn, caching, remote cache, filtering, and CI optimization.
- **[vercel-react-best-practices](skills/framework/vercel-react-best-practices/)** — React and Next.js performance optimization guidelines from Vercel Engineering. 70 rules across 8 categories, prioritized by impact.

### Workflow
Planning, documentation, ideation, and skill development.

- **[agent-rules](skills/workflow/agent-rules/)** — Generate and maintain AGENTS.md files (and Copilot/other agent rule files) with verified commands, scoped sub-files, freshness checks, and quality scoring. Includes helper scripts, templates, and evals.

- **[brainstorming](skills/workflow/brainstorming/)** — Turn ideas into fully formed designs and specs through natural collaborative dialogue. Mandatory before any creative work.
- **[brand-naming](skills/workflow/brand-naming/)** — Brand naming frameworks, evaluation criteria, and templates for startup naming, including domain and trademark checks.
- **[create-agentsmd](skills/workflow/create-agentsmd/)** — Prompt for generating a high-quality AGENTS.md for a repository, following the agents.md convention.
- **[doc-coauthoring](skills/workflow/doc-coauthoring/)** — Structured workflow for co-authoring documentation, proposals, technical specs, and decision docs. Three stages: Context Gathering, Refinement & Structure, Reader Testing.
- **[grill-me](skills/workflow/grill-me/)** — Calibrated grilling session that stress-tests a plan or decision. Assesses your knowledge and desired pressure first, then asks one question at a time with recommended answers.
- **[grill-with-docs](skills/workflow/grill-with-docs/)** — Stress-tests a plan against the existing domain model, sharpens terminology, and updates documentation inline as decisions crystallise.

- **[skill-creator](skills/workflow/skill-creator/)** — Create new skills, modify and improve existing ones, and measure skill performance. Includes evals, benchmarking, and description optimization.
- **[to-prd](skills/workflow/to-prd/)** — Turn the current conversation context into a PRD and publish it to the project issue tracker.

### Communication
Token-efficient communication modes.

- **[fuck-slop](skills/communication/fuck-slop/)** — De-slop pass for any text. Detects and removes the statistical fingerprints of AI writing ("not X but Y", em-dash abuse, rule-of-three, puffery) and rewrites into the target register.
- **[caveman](skills/communication/caveman/)** — Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Supports lite, full, and ultra intensity levels.

## Installation

Skills are installed with the `npx skills` CLI from each source repository. Each skill's origin and content hash are recorded in [`skills-lock.json`](skills-lock.json); use the `source` field there to re-add or update a skill.

Each skill folder contains the full skill definition (`SKILL.md`) plus any supporting files, scripts, references, and data.

## Security Scanning

Every skill is checked by the [pragmatic scanner](scanner/README.md), which flags exploitable risks in executable files only (shell injection, data exfiltration, credential theft). To run it locally:

```bash
cd scanner
python3 scanner.py ../skills --format markdown
```

CI runs the same scan on every push and pull request touching `skills/` or `scanner/`, and fails on HIGH findings.

## Contributing a Skill

1. Place the skill in the matching category folder under `skills/` (`<category>/<skill-name>/SKILL.md`), keeping any bundled license files.
2. Add an entry to `skills-lock.json` (alphabetical; `computedHash` is the SHA-256 of `SKILL.md`).
3. Add a one-line entry to the category list above.
4. Run the scanner and confirm there are no findings.

## Structure

```
.
├── README.md
├── skills-lock.json   ← source and hash for each skill
├── scanner/           ← security scanner
├── .github/workflows/ ← CI scan
└── skills/
    ├── communication/
    ├── design/
    ├── engineering/
    ├── framework/
    └── workflow/
```
