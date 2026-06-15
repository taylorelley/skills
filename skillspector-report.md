# SkillSpector Security Report

**Skill:** unknown  
**Source:** `/root/taylors-skills/skills`  
**Scanned:** 2026-06-12 04:28:00 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (301)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `communication/caveman/README.md` | markdown | 48 | No |
| `communication/caveman/SKILL.md` | markdown | 74 | No |
| `design/design-taste-frontend/SKILL.md` | markdown | 1206 | No |
| `design/frontend-design/LICENSE.txt` | text | 177 | No |
| `design/frontend-design/SKILL.md` | markdown | 55 | No |
| `design/impeccable/SKILL.md` | markdown | 169 | No |
| `design/impeccable/agents/impeccable_asset_producer.toml` | toml | 92 | No |
| `design/impeccable/agents/impeccable_manual_edit_applier.toml` | toml | 95 | No |
| `design/impeccable/agents/openai.yaml` | yaml | 4 | No |
| `design/impeccable/reference/adapt.md` | markdown | 311 | No |
| `design/impeccable/reference/animate.md` | markdown | 201 | No |
| `design/impeccable/reference/audit.md` | markdown | 133 | No |
| `design/impeccable/reference/bolder.md` | markdown | 113 | No |
| `design/impeccable/reference/brand.md` | markdown | 108 | No |
| `design/impeccable/reference/clarify.md` | markdown | 288 | No |
| `design/impeccable/reference/codex.md` | markdown | 105 | No |
| `design/impeccable/reference/colorize.md` | markdown | 257 | No |
| `design/impeccable/reference/craft.md` | markdown | 123 | No |
| `design/impeccable/reference/critique.md` | markdown | 790 | No |
| `design/impeccable/reference/delight.md` | markdown | 302 | No |
| `design/impeccable/reference/distill.md` | markdown | 111 | No |
| `design/impeccable/reference/document.md` | markdown | 429 | No |
| `design/impeccable/reference/extract.md` | markdown | 69 | No |
| `design/impeccable/reference/harden.md` | markdown | 347 | No |
| `design/impeccable/reference/init.md` | markdown | 172 | No |
| `design/impeccable/reference/interaction-design.md` | markdown | 189 | No |
| `design/impeccable/reference/layout.md` | markdown | 161 | No |
| `design/impeccable/reference/live.md` | markdown | 720 | No |
| `design/impeccable/reference/onboard.md` | markdown | 234 | No |
| `design/impeccable/reference/optimize.md` | markdown | 258 | No |
| `design/impeccable/reference/overdrive.md` | markdown | 130 | No |
| `design/impeccable/reference/polish.md` | markdown | 241 | No |
| `design/impeccable/reference/product.md` | markdown | 60 | No |
| `design/impeccable/reference/quieter.md` | markdown | 99 | No |
| `design/impeccable/reference/shape.md` | markdown | 165 | No |
| `design/impeccable/reference/typeset.md` | markdown | 279 | No |
| `design/impeccable/scripts/command-metadata.json` | json | 94 | No |
| `design/impeccable/scripts/context-signals.mjs` | other | 225 | No |
| `design/impeccable/scripts/context.mjs` | other | 266 | No |
| `design/impeccable/scripts/critique-storage.mjs` | other | 242 | No |
| `design/impeccable/scripts/detect-csp.mjs` | other | 198 | No |
| `design/impeccable/scripts/detect.mjs` | other | 21 | No |
| `design/impeccable/scripts/detector/browser/injected/index.mjs` | other | 1735 | No |
| `design/impeccable/scripts/detector/cli/main.mjs` | other | 244 | No |
| `design/impeccable/scripts/detector/detect-antipatterns-browser.js` | javascript | 4903 | Yes |
| `design/impeccable/scripts/detector/detect-antipatterns.mjs` | other | 43 | No |
| `design/impeccable/scripts/detector/engines/browser/detect-url.mjs` | other | 252 | No |
| `design/impeccable/scripts/detector/engines/regex/detect-text.mjs` | other | 535 | No |
| `design/impeccable/scripts/detector/engines/static-html/css-cascade.mjs` | other | 1013 | No |
| `design/impeccable/scripts/detector/engines/static-html/detect-html.mjs` | other | 208 | No |
| `design/impeccable/scripts/detector/engines/visual/screenshot-contrast.mjs` | other | 189 | No |
| `design/impeccable/scripts/detector/findings.mjs` | other | 12 | No |
| `design/impeccable/scripts/detector/node/file-system.mjs` | other | 198 | No |
| `design/impeccable/scripts/detector/profile/profiler.mjs` | other | 166 | No |
| `design/impeccable/scripts/detector/registry/antipatterns.mjs` | other | 419 | No |
| `design/impeccable/scripts/detector/rules/checks.mjs` | other | 2667 | No |
| `design/impeccable/scripts/detector/shared/color.mjs` | other | 124 | No |
| `design/impeccable/scripts/detector/shared/constants.mjs` | other | 101 | No |
| `design/impeccable/scripts/detector/shared/page.mjs` | other | 7 | No |
| `design/impeccable/scripts/lib/design-parser.mjs` | other | 835 | No |
| `design/impeccable/scripts/lib/impeccable-paths.mjs` | other | 126 | No |
| `design/impeccable/scripts/lib/is-generated.mjs` | other | 69 | No |
| `design/impeccable/scripts/live-accept.mjs` | other | 812 | No |
| `design/impeccable/scripts/live-browser-dom.js` | javascript | 146 | Yes |
| `design/impeccable/scripts/live-browser-session.js` | javascript | 123 | Yes |
| `design/impeccable/scripts/live-browser.js` | javascript | 10932 | Yes |
| `design/impeccable/scripts/live-commit-manual-edits.mjs` | other | 1241 | No |
| `design/impeccable/scripts/live-complete.mjs` | other | 75 | No |
| `design/impeccable/scripts/live-copy-edit-agent.mjs` | other | 683 | No |
| `design/impeccable/scripts/live-discard-manual-edits.mjs` | other | 51 | No |
| `design/impeccable/scripts/live-inject.mjs` | other | 581 | No |
| `design/impeccable/scripts/live-insert.mjs` | other | 272 | No |
| `design/impeccable/scripts/live-manual-edit-evidence.mjs` | other | 363 | No |
| `design/impeccable/scripts/live-poll.mjs` | other | 379 | No |
| `design/impeccable/scripts/live-resume.mjs` | other | 94 | No |
| `design/impeccable/scripts/live-server.mjs` | other | 1134 | No |
| `design/impeccable/scripts/live-status.mjs` | other | 61 | No |
| `design/impeccable/scripts/live-wrap.mjs` | other | 894 | No |
| `design/impeccable/scripts/live.mjs` | other | 246 | No |
| `design/impeccable/scripts/live/browser-script-parts.mjs` | other | 49 | No |
| `design/impeccable/scripts/live/completion.mjs` | other | 19 | No |
| `design/impeccable/scripts/live/event-validation.mjs` | other | 137 | No |
| `design/impeccable/scripts/live/insert-ui.mjs` | other | 458 | No |
| `design/impeccable/scripts/live/manual-apply.mjs` | other | 939 | No |
| `design/impeccable/scripts/live/manual-edit-routes.mjs` | other | 357 | No |
| `design/impeccable/scripts/live/manual-edits-buffer.mjs` | other | 152 | No |
| `design/impeccable/scripts/live/session-store.mjs` | other | 289 | No |
| `design/impeccable/scripts/live/svelte-component.mjs` | other | 826 | No |
| `design/impeccable/scripts/live/sveltekit-adapter.mjs` | other | 274 | No |
| `design/impeccable/scripts/live/ui-core.mjs` | other | 180 | No |
| `design/impeccable/scripts/live/vocabulary.mjs` | other | 36 | No |
| `design/impeccable/scripts/modern-screenshot.umd.js` | javascript | 14 | Yes |
| `design/impeccable/scripts/palette.mjs` | other | 633 | No |
| `design/impeccable/scripts/pin.mjs` | other | 214 | No |
| `design/ui-ux-pro-max/SKILL.md` | markdown | 659 | No |
| `design/ui-ux-pro-max/data/_sync_all.py` | python | 414 | Yes |
| `design/ui-ux-pro-max/data/app-interface.csv` | other | 31 | No |
| `design/ui-ux-pro-max/data/charts.csv` | other | 26 | No |
| `design/ui-ux-pro-max/data/colors.csv` | other | 162 | No |
| `design/ui-ux-pro-max/data/design.csv` | other | 1776 | No |
| `design/ui-ux-pro-max/data/draft.csv` | other | 1779 | No |
| `design/ui-ux-pro-max/data/google-fonts.csv` | other | 1924 | No |
| `design/ui-ux-pro-max/data/icons.csv` | other | 106 | No |
| `design/ui-ux-pro-max/data/landing.csv` | other | 35 | No |
| `design/ui-ux-pro-max/data/products.csv` | other | 162 | No |
| `design/ui-ux-pro-max/data/react-performance.csv` | other | 45 | No |
| `design/ui-ux-pro-max/data/stacks/angular.csv` | other | 51 | No |
| `design/ui-ux-pro-max/data/stacks/astro.csv` | other | 54 | No |
| `design/ui-ux-pro-max/data/stacks/flutter.csv` | other | 53 | No |
| `design/ui-ux-pro-max/data/stacks/html-tailwind.csv` | other | 56 | No |
| `design/ui-ux-pro-max/data/stacks/jetpack-compose.csv` | other | 53 | No |
| `design/ui-ux-pro-max/data/stacks/laravel.csv` | other | 51 | No |
| `design/ui-ux-pro-max/data/stacks/nextjs.csv` | other | 53 | No |
| `design/ui-ux-pro-max/data/stacks/nuxt-ui.csv` | other | 51 | No |
| `design/ui-ux-pro-max/data/stacks/nuxtjs.csv` | other | 59 | No |
| `design/ui-ux-pro-max/data/stacks/react-native.csv` | other | 52 | No |
| `design/ui-ux-pro-max/data/stacks/react.csv` | other | 54 | No |
| `design/ui-ux-pro-max/data/stacks/shadcn.csv` | other | 61 | No |
| `design/ui-ux-pro-max/data/stacks/svelte.csv` | other | 54 | No |
| `design/ui-ux-pro-max/data/stacks/swiftui.csv` | other | 51 | No |
| `design/ui-ux-pro-max/data/stacks/threejs.csv` | other | 54 | No |
| `design/ui-ux-pro-max/data/stacks/vue.csv` | other | 50 | No |
| `design/ui-ux-pro-max/data/styles.csv` | other | 85 | No |
| `design/ui-ux-pro-max/data/typography.csv` | other | 74 | No |
| `design/ui-ux-pro-max/data/ui-reasoning.csv` | other | 162 | No |
| `design/ui-ux-pro-max/data/ux-guidelines.csv` | other | 100 | No |
| `design/ui-ux-pro-max/scripts/core.py` | python | 262 | Yes |
| `design/ui-ux-pro-max/scripts/design_system.py` | python | 1148 | Yes |
| `design/ui-ux-pro-max/scripts/search.py` | python | 114 | Yes |
| `engineering/diagnose/SKILL.md` | markdown | 117 | No |
| `engineering/diagnose/scripts/hitl-loop.template.sh` | shell | 41 | Yes |
| `engineering/improve-codebase-architecture/DEEPENING.md` | markdown | 37 | No |
| `engineering/improve-codebase-architecture/HTML-REPORT.md` | markdown | 123 | No |
| `engineering/improve-codebase-architecture/INTERFACE-DESIGN.md` | markdown | 44 | No |
| `engineering/improve-codebase-architecture/LANGUAGE.md` | markdown | 53 | No |
| `engineering/improve-codebase-architecture/SKILL.md` | markdown | 81 | No |
| `engineering/tdd/SKILL.md` | markdown | 109 | No |
| `engineering/tdd/deep-modules.md` | markdown | 33 | No |
| `engineering/tdd/interface-design.md` | markdown | 31 | No |
| `engineering/tdd/mocking.md` | markdown | 59 | No |
| `engineering/tdd/refactoring.md` | markdown | 10 | No |
| `engineering/tdd/tests.md` | markdown | 61 | No |
| `engineering/webapp-testing/LICENSE.txt` | text | 202 | No |
| `engineering/webapp-testing/SKILL.md` | markdown | 96 | No |
| `engineering/webapp-testing/examples/console_logging.py` | python | 35 | Yes |
| `engineering/webapp-testing/examples/element_discovery.py` | python | 40 | Yes |
| `engineering/webapp-testing/examples/static_html_automation.py` | python | 33 | Yes |
| `engineering/webapp-testing/scripts/with_server.py` | python | 106 | Yes |
| `framework/next-best-practices/SKILL.md` | markdown | 153 | No |
| `framework/next-best-practices/async-patterns.md` | markdown | 87 | No |
| `framework/next-best-practices/bundling.md` | markdown | 180 | No |
| `framework/next-best-practices/data-patterns.md` | markdown | 297 | No |
| `framework/next-best-practices/debug-tricks.md` | markdown | 105 | No |
| `framework/next-best-practices/directives.md` | markdown | 73 | No |
| `framework/next-best-practices/error-handling.md` | markdown | 227 | No |
| `framework/next-best-practices/file-conventions.md` | markdown | 140 | No |
| `framework/next-best-practices/font.md` | markdown | 245 | No |
| `framework/next-best-practices/functions.md` | markdown | 108 | No |
| `framework/next-best-practices/hydration-error.md` | markdown | 91 | No |
| `framework/next-best-practices/image.md` | markdown | 173 | No |
| `framework/next-best-practices/metadata.md` | markdown | 301 | No |
| `framework/next-best-practices/parallel-routes.md` | markdown | 287 | No |
| `framework/next-best-practices/route-handlers.md` | markdown | 146 | No |
| `framework/next-best-practices/rsc-boundaries.md` | markdown | 159 | No |
| `framework/next-best-practices/runtime-selection.md` | markdown | 39 | No |
| `framework/next-best-practices/scripts.md` | markdown | 141 | No |
| `framework/next-best-practices/self-hosting.md` | markdown | 371 | No |
| `framework/next-best-practices/suspense-boundaries.md` | markdown | 67 | No |
| `framework/turborepo/SKILL.md` | markdown | 951 | No |
| `framework/turborepo/command/turborepo.md` | markdown | 70 | No |
| `framework/turborepo/references/best-practices/RULE.md` | markdown | 241 | No |
| `framework/turborepo/references/best-practices/dependencies.md` | markdown | 246 | No |
| `framework/turborepo/references/best-practices/packages.md` | markdown | 335 | No |
| `framework/turborepo/references/best-practices/structure.md` | markdown | 297 | No |
| `framework/turborepo/references/boundaries/RULE.md` | markdown | 126 | No |
| `framework/turborepo/references/caching/RULE.md` | markdown | 153 | No |
| `framework/turborepo/references/caching/gotchas.md` | markdown | 190 | No |
| `framework/turborepo/references/caching/remote-cache.md` | markdown | 127 | No |
| `framework/turborepo/references/ci/RULE.md` | markdown | 79 | No |
| `framework/turborepo/references/ci/github-actions.md` | markdown | 162 | No |
| `framework/turborepo/references/ci/patterns.md` | markdown | 145 | No |
| `framework/turborepo/references/ci/vercel.md` | markdown | 103 | No |
| `framework/turborepo/references/cli/RULE.md` | markdown | 100 | No |
| `framework/turborepo/references/cli/commands.md` | markdown | 297 | No |
| `framework/turborepo/references/configuration/RULE.md` | markdown | 235 | No |
| `framework/turborepo/references/configuration/global-options.md` | markdown | 239 | No |
| `framework/turborepo/references/configuration/gotchas.md` | markdown | 368 | No |
| `framework/turborepo/references/configuration/tasks.md` | markdown | 325 | No |
| `framework/turborepo/references/environment/RULE.md` | markdown | 123 | No |
| `framework/turborepo/references/environment/gotchas.md` | markdown | 175 | No |
| `framework/turborepo/references/environment/modes.md` | markdown | 101 | No |
| `framework/turborepo/references/filtering/RULE.md` | markdown | 148 | No |
| `framework/turborepo/references/filtering/patterns.md` | markdown | 152 | No |
| `framework/turborepo/references/watch/RULE.md` | markdown | 99 | No |
| `framework/vercel-react-best-practices/AGENTS.md` | markdown | 3810 | No |
| `framework/vercel-react-best-practices/README.md` | markdown | 123 | No |
| `framework/vercel-react-best-practices/SKILL.md` | markdown | 149 | No |
| `framework/vercel-react-best-practices/metadata.json` | json | 15 | No |
| `framework/vercel-react-best-practices/rules/_sections.md` | markdown | 46 | No |
| `framework/vercel-react-best-practices/rules/_template.md` | markdown | 28 | No |
| `framework/vercel-react-best-practices/rules/advanced-effect-event-deps.md` | markdown | 56 | No |
| `framework/vercel-react-best-practices/rules/advanced-event-handler-refs.md` | markdown | 55 | No |
| `framework/vercel-react-best-practices/rules/advanced-init-once.md` | markdown | 42 | No |
| `framework/vercel-react-best-practices/rules/advanced-use-latest.md` | markdown | 39 | No |
| `framework/vercel-react-best-practices/rules/async-api-routes.md` | markdown | 38 | No |
| `framework/vercel-react-best-practices/rules/async-cheap-condition-before-await.md` | markdown | 37 | No |
| `framework/vercel-react-best-practices/rules/async-defer-await.md` | markdown | 82 | No |
| `framework/vercel-react-best-practices/rules/async-dependencies.md` | markdown | 51 | No |
| `framework/vercel-react-best-practices/rules/async-parallel.md` | markdown | 28 | No |
| `framework/vercel-react-best-practices/rules/async-suspense-boundaries.md` | markdown | 99 | No |
| `framework/vercel-react-best-practices/rules/bundle-analyzable-paths.md` | markdown | 63 | No |
| `framework/vercel-react-best-practices/rules/bundle-barrel-imports.md` | markdown | 60 | No |
| `framework/vercel-react-best-practices/rules/bundle-conditional.md` | markdown | 31 | No |
| `framework/vercel-react-best-practices/rules/bundle-defer-third-party.md` | markdown | 49 | No |
| `framework/vercel-react-best-practices/rules/bundle-dynamic-imports.md` | markdown | 35 | No |
| `framework/vercel-react-best-practices/rules/bundle-preload.md` | markdown | 50 | No |
| `framework/vercel-react-best-practices/rules/client-event-listeners.md` | markdown | 74 | No |
| `framework/vercel-react-best-practices/rules/client-localstorage-schema.md` | markdown | 71 | No |
| `framework/vercel-react-best-practices/rules/client-passive-event-listeners.md` | markdown | 48 | No |
| `framework/vercel-react-best-practices/rules/client-swr-dedup.md` | markdown | 56 | No |
| `framework/vercel-react-best-practices/rules/js-batch-dom-css.md` | markdown | 107 | No |
| `framework/vercel-react-best-practices/rules/js-cache-function-results.md` | markdown | 80 | No |
| `framework/vercel-react-best-practices/rules/js-cache-property-access.md` | markdown | 28 | No |
| `framework/vercel-react-best-practices/rules/js-cache-storage.md` | markdown | 70 | No |
| `framework/vercel-react-best-practices/rules/js-combine-iterations.md` | markdown | 32 | No |
| `framework/vercel-react-best-practices/rules/js-early-exit.md` | markdown | 50 | No |
| `framework/vercel-react-best-practices/rules/js-flatmap-filter.md` | markdown | 60 | No |
| `framework/vercel-react-best-practices/rules/js-hoist-regexp.md` | markdown | 45 | No |
| `framework/vercel-react-best-practices/rules/js-index-maps.md` | markdown | 37 | No |
| `framework/vercel-react-best-practices/rules/js-length-check-first.md` | markdown | 49 | No |
| `framework/vercel-react-best-practices/rules/js-min-max-loop.md` | markdown | 82 | No |
| `framework/vercel-react-best-practices/rules/js-request-idle-callback.md` | markdown | 105 | No |
| `framework/vercel-react-best-practices/rules/js-set-map-lookups.md` | markdown | 24 | No |
| `framework/vercel-react-best-practices/rules/js-tosorted-immutable.md` | markdown | 57 | No |
| `framework/vercel-react-best-practices/rules/rendering-activity.md` | markdown | 26 | No |
| `framework/vercel-react-best-practices/rules/rendering-animate-svg-wrapper.md` | markdown | 47 | No |
| `framework/vercel-react-best-practices/rules/rendering-conditional-render.md` | markdown | 40 | No |
| `framework/vercel-react-best-practices/rules/rendering-content-visibility.md` | markdown | 38 | No |
| `framework/vercel-react-best-practices/rules/rendering-hoist-jsx.md` | markdown | 46 | No |
| `framework/vercel-react-best-practices/rules/rendering-hydration-no-flicker.md` | markdown | 82 | No |
| `framework/vercel-react-best-practices/rules/rendering-hydration-suppress-warning.md` | markdown | 30 | No |
| `framework/vercel-react-best-practices/rules/rendering-resource-hints.md` | markdown | 85 | No |
| `framework/vercel-react-best-practices/rules/rendering-script-defer-async.md` | markdown | 68 | No |
| `framework/vercel-react-best-practices/rules/rendering-svg-precision.md` | markdown | 28 | No |
| `framework/vercel-react-best-practices/rules/rendering-usetransition-loading.md` | markdown | 75 | No |
| `framework/vercel-react-best-practices/rules/rerender-defer-reads.md` | markdown | 39 | No |
| `framework/vercel-react-best-practices/rules/rerender-dependencies.md` | markdown | 45 | No |
| `framework/vercel-react-best-practices/rules/rerender-derived-state-no-effect.md` | markdown | 40 | No |
| `framework/vercel-react-best-practices/rules/rerender-derived-state.md` | markdown | 29 | No |
| `framework/vercel-react-best-practices/rules/rerender-functional-setstate.md` | markdown | 74 | No |
| `framework/vercel-react-best-practices/rules/rerender-lazy-state-init.md` | markdown | 58 | No |
| `framework/vercel-react-best-practices/rules/rerender-memo-with-default-value.md` | markdown | 38 | No |
| `framework/vercel-react-best-practices/rules/rerender-memo.md` | markdown | 44 | No |
| `framework/vercel-react-best-practices/rules/rerender-move-effect-to-event.md` | markdown | 45 | No |
| `framework/vercel-react-best-practices/rules/rerender-no-inline-components.md` | markdown | 82 | No |
| `framework/vercel-react-best-practices/rules/rerender-simple-expression-in-memo.md` | markdown | 35 | No |
| `framework/vercel-react-best-practices/rules/rerender-split-combined-hooks.md` | markdown | 64 | No |
| `framework/vercel-react-best-practices/rules/rerender-transitions.md` | markdown | 40 | No |
| `framework/vercel-react-best-practices/rules/rerender-use-deferred-value.md` | markdown | 59 | No |
| `framework/vercel-react-best-practices/rules/rerender-use-ref-transient-values.md` | markdown | 73 | No |
| `framework/vercel-react-best-practices/rules/server-after-nonblocking.md` | markdown | 73 | No |
| `framework/vercel-react-best-practices/rules/server-auth-actions.md` | markdown | 96 | No |
| `framework/vercel-react-best-practices/rules/server-cache-lru.md` | markdown | 41 | No |
| `framework/vercel-react-best-practices/rules/server-cache-react.md` | markdown | 76 | No |
| `framework/vercel-react-best-practices/rules/server-dedup-props.md` | markdown | 65 | No |
| `framework/vercel-react-best-practices/rules/server-hoist-static-io.md` | markdown | 149 | No |
| `framework/vercel-react-best-practices/rules/server-no-shared-module-state.md` | markdown | 50 | No |
| `framework/vercel-react-best-practices/rules/server-parallel-fetching.md` | markdown | 83 | No |
| `framework/vercel-react-best-practices/rules/server-parallel-nested-fetching.md` | markdown | 34 | No |
| `framework/vercel-react-best-practices/rules/server-serialization.md` | markdown | 38 | No |
| `workflow/brainstorming/SKILL.md` | markdown | 164 | No |
| `workflow/brainstorming/scripts/frame-template.html` | other | 214 | No |
| `workflow/brainstorming/scripts/helper.js` | javascript | 88 | Yes |
| `workflow/brainstorming/scripts/server.cjs` | other | 354 | No |
| `workflow/brainstorming/scripts/start-server.sh` | shell | 148 | Yes |
| `workflow/brainstorming/scripts/stop-server.sh` | shell | 56 | Yes |
| `workflow/brainstorming/spec-document-reviewer-prompt.md` | markdown | 49 | No |
| `workflow/brainstorming/visual-companion.md` | markdown | 287 | No |
| `workflow/doc-coauthoring/SKILL.md` | markdown | 375 | No |
| `workflow/grill-with-docs/ADR-FORMAT.md` | markdown | 47 | No |
| `workflow/grill-with-docs/CONTEXT-FORMAT.md` | markdown | 60 | No |
| `workflow/grill-with-docs/SKILL.md` | markdown | 88 | No |
| `workflow/skill-creator/LICENSE.txt` | text | 202 | No |
| `workflow/skill-creator/SKILL.md` | markdown | 485 | No |
| `workflow/skill-creator/agents/analyzer.md` | markdown | 274 | No |
| `workflow/skill-creator/agents/comparator.md` | markdown | 202 | No |
| `workflow/skill-creator/agents/grader.md` | markdown | 223 | No |
| `workflow/skill-creator/assets/eval_review.html` | other | 146 | No |
| `workflow/skill-creator/eval-viewer/generate_review.py` | python | 471 | Yes |
| `workflow/skill-creator/eval-viewer/viewer.html` | other | 1325 | No |
| `workflow/skill-creator/references/schemas.md` | markdown | 430 | No |
| `workflow/skill-creator/scripts/__init__.py` | python | 0 | Yes |
| `workflow/skill-creator/scripts/aggregate_benchmark.py` | python | 401 | Yes |
| `workflow/skill-creator/scripts/generate_report.py` | python | 326 | Yes |
| `workflow/skill-creator/scripts/improve_description.py` | python | 247 | Yes |
| `workflow/skill-creator/scripts/package_skill.py` | python | 136 | Yes |
| `workflow/skill-creator/scripts/quick_validate.py` | python | 103 | Yes |
| `workflow/skill-creator/scripts/run_eval.py` | python | 310 | Yes |
| `workflow/skill-creator/scripts/run_loop.py` | python | 328 | Yes |
| `workflow/skill-creator/scripts/utils.py` | python | 47 | Yes |
| `workflow/to-prd/SKILL.md` | markdown | 74 | No |

## Issues (144)

### 🟡 MEDIUM: AST4

**Location:** `engineering/webapp-testing/scripts/with_server.py:88`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess.run() with shell=False and an explicit argument list. Validate all inputs and avoid passing user-controlled data to commands.

---

### 🟡 MEDIUM: AST4

**Location:** `engineering/webapp-testing/scripts/with_server.py:69–74`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess.run() with shell=False and an explicit argument list. Validate all inputs and avoid passing user-controlled data to commands.

---

### 🟡 MEDIUM: AST4

**Location:** `workflow/skill-creator/eval-viewer/generate_review.py:291–294`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess.run() with shell=False and an explicit argument list. Validate all inputs and avoid passing user-controlled data to commands.

---

### 🟡 MEDIUM: AST4

**Location:** `workflow/skill-creator/scripts/improve_description.py:35–42`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess.run() with shell=False and an explicit argument list. Validate all inputs and avoid passing user-controlled data to commands.

---

### 🟡 MEDIUM: AST4

**Location:** `workflow/skill-creator/scripts/run_eval.py:85–91`  
**Confidence:** 70%  

**Message:** subprocess module call

**Remediation:** Use subprocess.run() with shell=False and an explicit argument list. Validate all inputs and avoid passing user-controlled data to commands.

---

### 🟡 MEDIUM: E1

**Location:** `design/impeccable/scripts/live-browser.js:3623`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/impeccable/scripts/live-browser.js:6068`  
**Confidence:** 70%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:2`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:6`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:11`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:14`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:16`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:19`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:22`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:24`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:25`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:28`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:32`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:35`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:36`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:42`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `design/ui-ux-pro-max/data/stacks/flutter.csv:44`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `framework/next-best-practices/data-patterns.md:36`  
**Confidence:** 50%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🟡 MEDIUM: E1

**Location:** `framework/next-best-practices/debug-tricks.md:21`  
**Confidence:** 60%  

**Message:** External Transmission

**Remediation:** Verify the destination URL is trusted and necessary. Remove or replace with documented APIs. Ensure no secrets, tokens, or PII are transmitted.

---

### 🔴 HIGH: E2

**Location:** `workflow/skill-creator/scripts/improve_description.py:33`  
**Confidence:** 70%  

**Message:** Env Variable Harvesting

**Remediation:** Avoid reading sensitive env vars (API keys, tokens) unless strictly required. Use secrets managers or secure config. Never log or transmit credentials.

---

### 🔴 HIGH: E2

**Location:** `workflow/skill-creator/scripts/run_eval.py:83`  
**Confidence:** 70%  

**Message:** Env Variable Harvesting

**Remediation:** Avoid reading sensitive env vars (API keys, tokens) unless strictly required. Use secrets managers or secure config. Never log or transmit credentials.

---

### 🟡 MEDIUM: EA2

**Location:** `design/design-taste-frontend/SKILL.md:51`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟢 LOW: EA3

**Location:** `design/frontend-design/LICENSE.txt:28`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `design/frontend-design/LICENSE.txt:33`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `design/frontend-design/LICENSE.txt:56`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `design/frontend-design/LICENSE.txt:161`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/audit.md:132`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/codex.md:49`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/craft.md:94`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/critique.md:671`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/document.md:424`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/init.md:152`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/live.md:89`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/shape.md:9`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/shape.md:78`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/reference/shape.md:80`  
**Confidence:** 80%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/scripts/live-accept.mjs:806`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/scripts/live-inject.mjs:572`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/scripts/live-poll.mjs:375`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/scripts/live-wrap.mjs:876`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/impeccable/scripts/live.mjs:240`  
**Confidence:** 85%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/ui-ux-pro-max/data/app-interface.csv:15`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/ui-ux-pro-max/data/stacks/react-native.csv:52`  
**Confidence:** 70%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/ui-ux-pro-max/data/ux-guidelines.csv:35`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/ui-ux-pro-max/data/ux-guidelines.csv:36`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟡 MEDIUM: EA2

**Location:** `design/ui-ux-pro-max/data/ux-guidelines.csv:84`  
**Confidence:** 75%  

**Message:** Autonomous Decision Making

**Remediation:** Add human-in-the-loop confirmation for destructive, irreversible, or high-impact operations. Never auto-execute commands that modify files, send data, or alter system state.

---

### 🟢 LOW: EA3

**Location:** `engineering/webapp-testing/LICENSE.txt:28`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `engineering/webapp-testing/LICENSE.txt:33`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `engineering/webapp-testing/LICENSE.txt:56`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `engineering/webapp-testing/LICENSE.txt:161`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟡 MEDIUM: EA4

**Location:** `framework/turborepo/references/watch/RULE.md:72`  
**Confidence:** 75%  

**Message:** Unbounded Resource Access

**Remediation:** Set explicit rate limits, timeouts, and resource quotas for API calls, file operations, and compute. Implement circuit breakers for runaway loops.

---

### 🟢 LOW: EA3

**Location:** `workflow/skill-creator/LICENSE.txt:28`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `workflow/skill-creator/LICENSE.txt:33`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `workflow/skill-creator/LICENSE.txt:56`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🟢 LOW: EA3

**Location:** `workflow/skill-creator/LICENSE.txt:161`  
**Confidence:** 70%  

**Message:** Scope Creep

**Remediation:** Limit the skill's scope to its documented purpose. Remove instructions that enable the agent to perform actions outside its stated functionality.

---

### 🔴 HIGH: OH1

**Location:** `design/ui-ux-pro-max/data/react-performance.csv:29`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:51`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `framework/next-best-practices/scripts.md:25`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `framework/next-best-practices/scripts.md:28`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `framework/vercel-react-best-practices/AGENTS.md:2537`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `framework/vercel-react-best-practices/rules/rendering-hydration-no-flicker.md:63`  
**Confidence:** 65%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `workflow/skill-creator/eval-viewer/generate_review.py:291`  
**Confidence:** 95%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: OH1

**Location:** `workflow/skill-creator/scripts/improve_description.py:35`  
**Confidence:** 95%  

**Message:** Unvalidated Output Injection

**Remediation:** Validate and sanitize all model output before using it in downstream contexts. Use parameterized queries for SQL, shell quoting for commands, and HTML encoding for web output.

---

### 🔴 HIGH: PE3

**Location:** `design/impeccable/scripts/lib/impeccable-paths.mjs:42`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/impeccable/scripts/live-copy-edit-agent.mjs:97`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/impeccable/scripts/live-copy-edit-agent.mjs:475`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/impeccable/scripts/live-copy-edit-agent.mjs:571`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/products.csv:112`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:38`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:38`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:38`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:38`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:38`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:351`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:368`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:373`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:635`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:640`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:659`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:663`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:673`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:863`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/SKILL.md:900`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/caching/RULE.md:84`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/caching/gotchas.md:68`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/caching/gotchas.md:76`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/caching/gotchas.md:76`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/ci/RULE.md:70`  
**Confidence:** 70%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/configuration/global-options.md:162`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/configuration/gotchas.md:63`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/configuration/gotchas.md:76`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/configuration/tasks.md:139`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/configuration/tasks.md:144`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:5`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:28`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:99`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:100`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:101`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:103`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:125`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:126`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:127`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:140`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:154`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:154`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `framework/turborepo/references/environment/gotchas.md:154`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: P2

**Location:** `design/design-taste-frontend/SKILL.md:272`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/impeccable/reference/document.md:74`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/impeccable/reference/live.md:305`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/impeccable/reference/live.md:440`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/impeccable/reference/live.md:477`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/impeccable/scripts/live-accept.mjs:218`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/ui-ux-pro-max/data/stacks/threejs.csv:4`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P2

**Location:** `design/ui-ux-pro-max/data/stacks/threejs.csv:36`  
**Confidence:** 70%  

**Message:** Hidden Instructions

**Remediation:** Audit all comments and invisible characters. Remove any instructions that direct the agent to perform unauthorized actions. Use plain, reviewable content.

---

### 🔴 HIGH: P1

**Location:** `design/ui-ux-pro-max/data/ux-guidelines.csv:25`  
**Confidence:** 90%  

**Message:** Instruction Override

**Remediation:** Remove or rewrite any text that instructs the agent to ignore prompts, override safety rules, or trust unverified content. Ensure skill content cannot be injected to alter agent behavior.

---

### 🟡 MEDIUM: P4

**Location:** `framework/turborepo/references/configuration/RULE.md:19`  
**Confidence:** 70%  

**Message:** Behavior Manipulation

**Remediation:** Review content for implicit steering or bias. Ensure instructions are explicit and align with the skill's stated purpose.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/SKILL.md:22`  
**Confidence:** 80%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/scripts/start-server.sh:67`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/scripts/start-server.sh:118`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/scripts/start-server.sh:118`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/scripts/start-server.sh:119`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/brainstorming/scripts/start-server.sh:121`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🟡 MEDIUM: RA2

**Location:** `workflow/skill-creator/SKILL.md:238`  
**Confidence:** 65%  

**Message:** Session Persistence

**Remediation:** Remove any persistence mechanisms (cron jobs, startup scripts, state files). Skills should not maintain state across sessions without explicit user consent.

---

### 🔴 HIGH: P6

**Location:** `design/impeccable/scripts/detector/engines/static-html/css-cascade.mjs:685`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/impeccable/scripts/detector/engines/static-html/css-cascade.mjs:716`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/impeccable/scripts/detector/registry/antipatterns.mjs:390`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/impeccable/scripts/lib/design-parser.mjs:317`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/impeccable/scripts/live/svelte-component.mjs:399`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/ui-ux-pro-max/scripts/design_system.py:71`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/ui-ux-pro-max/scripts/design_system.py:77`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `design/ui-ux-pro-max/scripts/design_system.py:84`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: P6

**Location:** `engineering/diagnose/scripts/hitl-loop.template.sh:10`  
**Confidence:** 85%  

**Message:** Direct Prompt Extraction

**Remediation:** Remove any instructions that reveal, print, or output system prompts or internal rules. System instructions should never be exposed to end users.

---

### 🔴 HIGH: TM2

**Location:** `design/ui-ux-pro-max/SKILL.md:325`  
**Confidence:** 75%  

**Message:** Chaining Abuse

**Remediation:** Limit tool chaining depth and validate the output of each tool before passing it to the next. Require explicit user approval for multi-step chains.

---

### 🟡 MEDIUM: TM3

**Location:** `design/ui-ux-pro-max/data/stacks/nextjs.csv:21`  
**Confidence:** 70%  

**Message:** Unsafe Defaults

**Remediation:** Override unsafe defaults with secure settings (verify=True, auth required, restrictive permissions). Review and harden all tool configurations.

---

### 🔴 HIGH: TM1

**Location:** `engineering/webapp-testing/scripts/with_server.py:69`  
**Confidence:** 90%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist. Reject dangerous parameter values (shell=True, --force, -rf /) and use safe defaults.

---

### 🔴 HIGH: TM1

**Location:** `engineering/webapp-testing/scripts/with_server.py:69`  
**Confidence:** 90%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist. Reject dangerous parameter values (shell=True, --force, -rf /) and use safe defaults.

---

### 🔴 HIGH: TM1

**Location:** `workflow/brainstorming/scripts/stop-server.sh:46`  
**Confidence:** 95%  

**Message:** Tool Parameter Abuse

**Remediation:** Validate all tool parameters against an allowlist. Reject dangerous parameter values (shell=True, --force, -rf /) and use safe defaults.

---

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.1.3*