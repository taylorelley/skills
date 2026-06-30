# Taylor's Skills

A curated collection of agent skills.

## Categories

### Design
UI/UX design, visual polish, and aesthetics.

- **[design-taste-frontend](design/design-taste-frontend/)** — Anti-slop frontend skill for landing pages, portfolios, and redesigns. Reads the brief, infers the right design direction, and ships interfaces that don't look templated.
- **[frontend-design](design/frontend-design/)** — Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and avoiding templated defaults.
- **[impeccable](design/impeccable/)** — Designs and iterates production-grade frontend interfaces. Real working code, committed design choices, exceptional craft. Covers websites, dashboards, product UI, and reusable design systems.
- **[ui-ux-pro-max](design/ui-ux-pro-max/)** — Comprehensive UI/UX design intelligence with 50+ styles, 161 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 10 stacks.

### Engineering
Code quality, testing, debugging, and architecture.

- **[diagnose](engineering/diagnose/)** — Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **[improve-codebase-architecture](engineering/improve-codebase-architecture/)** — Find deepening opportunities in a codebase, informed by the domain language and ADRs. Turns shallow modules into deep, testable, AI-navigable ones.
- **[tdd](engineering/tdd/)** — Test-driven development with red-green-refactor loop. Tests should verify behavior through public interfaces, not implementation details.
- **[webapp-testing](engineering/webapp-testing/)** — Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, capturing screenshots, and viewing browser logs.

### Framework
Framework-specific best practices and tooling.

- **[next-best-practices](framework/next-best-practices/)** — Next.js best practices covering file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, and bundling.
- **[turborepo](framework/turborepo/)** — Turborepo monorepo build system guidance. Triggers on turbo.json, task pipelines, dependsOn, caching, remote cache, filtering, and CI optimization.
- **[vercel-react-best-practices](framework/vercel-react-best-practices/)** — React and Next.js performance optimization guidelines from Vercel Engineering. 70 rules across 8 categories, prioritized by impact.

### Workflow
Planning, documentation, ideation, and skill development.

- **[brainstorming](workflow/brainstorming/)** — Turn ideas into fully formed designs and specs through natural collaborative dialogue. Mandatory before any creative work.
- **[doc-coauthoring](workflow/doc-coauthoring/)** — Structured workflow for co-authoring documentation, proposals, technical specs, and decision docs. Three stages: Context Gathering, Refinement & Structure, Reader Testing.
- **[grill-with-docs](workflow/grill-with-docs/)** — Stress-tests a plan against the existing domain model, sharpens terminology, and updates documentation inline as decisions crystallise.
- **[skill-creator](workflow/skill-creator/)** — Create new skills, modify and improve existing ones, and measure skill performance. Includes evals, benchmarking, and description optimization.
- **[to-prd](workflow/to-prd/)** — Turn the current conversation context into a PRD and publish it to the project issue tracker.

### Communication
Token-efficient communication modes.

- **[caveman](communication/caveman/)** — Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping full technical accuracy. Supports lite, full, and ultra intensity levels.

## Installation

Skills are installed using the `npx skills` CLI from each source repository. To re-add a skill, use the original command documented in the skill's folder or in git history.

Each skill folder contains the full skill definition (`SKILL.md`) plus any supporting files, scripts, references, and data.

## Structure

```
skills/
├── README.md          ← you are here
├── communication/
├── design/
├── engineering/
├── framework/
└── workflow/
```
