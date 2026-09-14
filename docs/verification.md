# Verification record — 2026-09-13

## Build and content

- `npm run build`: 12 static pages generated.
- `npm run check`: 327 local links/assets, all page fragments, eight lesson records and Python snippet syntax, eight practice question records, and JavaScript syntax passed.
- `ffprobe`: the included MP4 is 12.000 seconds, H.264, 129,072 bytes. Chromium playback succeeded.
- Versioned Apache Spark 3.5.7 documentation was used to check core claims. References are linked in each lesson. This is a deliberate reference baseline, not a latest-version claim.
- PySpark execution was not tested: the local environment has neither PySpark nor a Java runtime. Every example says so on the rendered page.

## Chromium browser checks

Executed through Playwright CLI using isolated browser contexts and a local HTTP preview:

- Site search, matched results, and Escape dismissal.
- Completion tracking across reloads.
- Scenario filters combined with query text, empty results, and answer disclosure.
- Notebook creation, editing, deletion, and persistence across reloads.
- HTML-like question input rendered as literal text.
- Export download, import deduplication, backup restoration, and invalid import preserving current notes.
- Shuffle and local filter step controls; playback and pause.
- MP4 playback.
- All 12 pages checked for document overflow at 320, 390, 768, and 1280 CSS pixels (48 combinations).
- Mobile navigation opens, makes links interactive, and dismisses on Escape.
- Lessons, navigation, and answer disclosure remain available with JavaScript disabled at phone width.
- Blocked localStorage preserves a newly entered note in page memory and displays an explicit export warning.
- A stale tab does not overwrite another tab's saved note; it retains its own change in page memory for export.
- An otherwise valid imported note with a javascript: reference URL is rejected without changing saved notes.
- The lab's step controls remain usable with reduced motion enabled.
- Zero JavaScript page errors in the main browser pass.

Two defects found and corrected during verification: search-input Escape could leave the dialog open; a preformatted example could increase the minimum article width on phones. The full browser pass succeeded after both fixes.

Visual inspection covered the desktop overview and lesson, phone overview and lesson, and desktop canvas/video page. Screenshots are in ignored `output/playwright/`.

## Publication at initial validation

At the time of the initial local validation, the directory had no git repository and `anchitgupt/learn-spark` did not resolve via `gh repo view`. Publication was subsequently authorized. Current build and deployment results are recorded in the repository's GitHub Actions runs; this document records the local checks before publication.

# Execution flow update — 2026-09-14

## Content and build

- Added the complete execution-flow capstone, a six-phase interactive walkthrough, an original architecture diagram, one user-reported interview question, and three authored follow-ups.
- Reviewed claims against Apache Spark 3.5.7 documentation and tagged source, including driver startup, lazy query planning, scheduler responsibilities, exchange types, task resource requests, adaptive execution, and failure handling. The lesson links its references and explains corrections to the supplied draft.
- `npm run build`: 13 static pages generated.
- `npm run check`: 436 local links/assets, nine lesson schemas and example syntax, 12 question records, source/search/phase anchors, and all three JavaScript files passed.
- Independently checked the example arithmetic: India 900, USA 1050, UK 1200. Output order is unspecified. The example was not executed in Spark; documentation/source review and syntax/arithmetic checks do not constitute cluster runtime validation.

## Chromium browser checks

- All six phases select correctly; keyboard activation, previous/next boundaries, and phase status work.
- Existing eight-lesson completion data resumes at the new lesson and advances from 8/9 to 9/9. Existing saved questions and answers remain intact, and the notebook includes the new topic.
- Question provenance distinguishes one interview-reported question from 11 authored practice questions; scenario and text filters work.
- Search finds the capstone and links directly to the reported question; Escape dismisses the dialog.
- All 13 pages checked at 320, 390, 768, and 1280 CSS pixels: 52 combinations without document overflow.
- Mobile navigation includes the capstone and dismisses on Escape.
- With JavaScript disabled, all six phase panels remain readable, interactive controls are hidden, and answers remain expandable at phone width.
- Phase controls work with reduced motion enabled. No JavaScript page errors occurred.
- Visually inspected desktop and phone walkthrough screenshots and the architecture diagram. Screenshots remain in ignored `output/playwright/`.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `365f9722bac227feceecaaa03df45c3eebed3c3e` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34803026339](https://github.com/anchitgupt/learn-spark/actions/runs/34803026339) completed successfully.
- All 26 public build files returned HTTP 200 and matched the local build byte for byte after deployment.
- Live lesson: https://anchitgupt.github.io/learn-spark/execution-flow.html

# Prediction exercises update — 2026-09-14

## Content and build

- Added a tenth lesson, "Predict what Spark will do": a shared classic PySpark 3.5.7 baseline (four Range partitions, four SQL shuffle partitions, AQE disabled), three prediction exercises (filter → count, groupBy → write, join → aggregate), an AQE comparison, and three authored practice questions. None is presented as a reported interview question.
- Exercise records live in `content/predictions.json` and render through `scripts/predictions.py` as native disclosures. The lesson adds no JavaScript or browser storage.
- `npm run build`: 14 static pages generated.
- `npm run check`: 517 local links/assets, ten lesson schemas and example syntax, 15 question records, three prediction exercises (IDs, lesson references, source anchors, and Python syntax for every code block on the lesson page), and all three JavaScript files passed. `git diff --check` was clean.
- Independently checked the example arithmetic: nine rows survive the filter (input partition counts 0, 3, 3, 3); bucket totals 900, 1050, 1200; Domestic 1950 and International 1200. The examples were not executed in Spark: PySpark and a Java runtime are not installed on this machine. Task counts remain source-reviewed predictions, not runtime observations.

## Chromium browser checks

46 automated checks passed in headless Chromium 151 through Playwright against a local HTTP preview, with reduced motion enabled unless noted.

- Saved progress for the previous nine lessons displays as 9/10 and resumes at the new lesson. Marking it understood reaches 10/10 and keeps the existing saved note.
- All three answer disclosures and interviewer follow-ups open by keyboard and mouse at 1280 and 390 CSS pixels. Rendered expected results and flow steps match the content file.
- The copy button copies the exercise snippet exactly.
- Search finds each exercise and links to its anchor; Escape dismisses the dialog.
- The notebook offers the new topic. A note saved under it persists after reload beside the existing note.
- The questions page renders 15 cards, including the three new practice questions; the Scenario filter shows nine.
- Mobile navigation lists the new lesson and dismisses on Escape.
- All 14 pages checked at 320, 390, 768, and 1280 CSS pixels with every disclosure open: 56 combinations without document overflow.
- With JavaScript disabled at phone width, copy buttons are hidden, every answer and follow-up opens by keyboard, and the page does not overflow.
- No JavaScript page errors or console errors occurred.

An earlier browser run timed out clicking the second exercise disclosure while several browser pages were open in different states. It did not reproduce: with default motion settings (smooth scrolling enabled), all three disclosures opened by mouse at 390 and 1280 CSS pixels.

Visually inspected desktop and phone screenshots of the opened exercises. The skip link and sticky header that appear mid-image are element-screenshot artifacts; on the live page the skip link stays off-screen until focused. Screenshots remain in ignored `output/playwright/`.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `75a5d20ce9635402ba9ef7dbf085f93c94891699` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34805147063](https://github.com/anchitgupt/learn-spark/actions/runs/34805147063) completed successfully.
- All 27 public build files returned HTTP 200 and matched the local build byte for byte after deployment.
- Live lesson: https://anchitgupt.github.io/learn-spark/predict-execution.html

# Content and check fixes — 2026-09-14

## Content and build

- Search results no longer index HTML. `_site/search.json` text is flattened with an HTML parser, so tags and entities (previously 10 of 28 entries, such as `&gt;` and link markup) are removed. All 28 entries are now markup-free.
- Every question record carries `origin` (`reported` or `practice`), and `scripts/check.py` requires it. The eight original authored questions are marked `practice`.
- The three prediction questions use `"exercise": "<id>"` and no longer copy the spoken answer and follow-up from `content/predictions.json`; the builder resolves that text at build time, and the checker rejects answers copied from an exercise.
- Lesson pages label their chapter from a new `chapter` field in `content/lessons.json` instead of the hardcoded "FUNDAMENTALS": the capstone reads "CAPSTONE / LESSON 09" and the prediction lesson "PRACTICE / LESSON 10".
- `scripts/build.py` resolves exercises, topics, and exercise-linked questions through one helper that exits with a readable message. Scratch copies with each of the three reference types corrupted exited with status 1 and named the file, record, and unknown ID; previously they raised bare `StopIteration` or `KeyError`.

## Checks

- `npm run build`: 14 static pages generated.
- `npm run check`: PASS — 14 pages, 517 local links/assets, ten lesson schemas and example syntax, 15 question records, three prediction exercises, and JavaScript syntax. `git diff --check` was clean.
- The 46-check Playwright browser pass was not run again for this batch; the changed output is covered by `scripts/check.py`.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `a20f9b8d59ef5caf4c97dff95e2b1aaf55f152d9` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34816426019](https://github.com/anchitgupt/learn-spark/actions/runs/34816426019) completed successfully.
- All 27 public build files returned HTTP 200 and matched the local build byte for byte after deployment.
- Live question bank: https://anchitgupt.github.io/learn-spark/questions.html
# Accessibility audit — 2026-09-14

## Findings and fixes

First audit of contrast, screen-reader structure, target size, and Lighthouse. Findings were reproduced against the local build with axe-core 4.10.2 on all 14 pages at 390 and 1280 CSS pixels, and with Lighthouse 12.

- Contrast: eleven muted colors were below 4.5:1 (breadcrumb 3.72, sidebar lesson numbers 3.19–3.45, code labels and notes 4.18–4.44, pitfall text 4.44, and similar). All now clear 4.5:1 on every background they appear on (lowest 4.6:1). The pitfall needed a direct `.pitfall p` override because the global `p` rule sets its color directly.
- Landmarks: the lesson pitfall callout was an `aside` nested inside the article; it is now a `div`. The table of contents and course sidebar now carry distinct labels ("On this page", "Course"), and the breadcrumb separator is `aria-hidden`.
- Keyboard: every `<pre>` code block is focusable (`tabindex="0"`), so horizontally scrollable code is reachable without a pointer.
- Target size: footer, back, hero, source-list, and question-meta links were under 24 px and now measure 24–30 px. The full-size diagram link now covers the whole image (671×425) instead of a 20 px inline strip. Links inside sentences stay as-is under the WCAG 2.5.8 inline exception.
- Label in name: the search trigger's ⌘ K hint is now rendered from CSS and hidden from assistive technology so the accessible name matches the visible text.

## Checks

- axe-core 4.10.2: zero violations on all 14 pages at 390 px; zero on the audited pages at 1280 px where the sidebar and table of contents are visible.
- Lighthouse 12 accessibility: 100 on the homepage and on the execution-flow lesson, with no failing or advisory items.
- A tap-target sweep at 390 px leaves no sub-24 px target except prose links (WCAG inline exception). Screenshots and audit JSON remain in ignored `output/playwright/`.
- `npm run build` and `npm run check` pass (14 pages, 517 local links/assets, ten lesson schemas, 15 questions, three prediction exercises, JavaScript syntax); `git diff --check` was clean. Screenshots were inspected at desktop and phone widths; no visual regressions from the color and padding changes.
- Limits: hover/focus styling, forced-colors mode, and real screen-reader runs were not part of this pass. Lighthouse ran against the local build; live assets are checked against the generated build after deployment.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `acca9789a62f9ff1c3f8a3070dac24da00bd62cd` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34818961223](https://github.com/anchitgupt/learn-spark/actions/runs/34818961223) completed successfully.
- All 27 public build files returned HTTP 200 and matched the local build byte for byte after deployment.
- Live lesson: https://anchitgupt.github.io/learn-spark/execution-flow.html

# Browser test harness — 2026-09-14

## What it covers

`scripts/browser_test.py` (also `npm run test:browser`) serves the built `_site` on an ephemeral port and drives headless Playwright through 66 checks: all 14 pages load; completion progress seeds, toggles, and persists; prediction disclosures open by mouse and keyboard; the copy button copies exactly and confirms; search loads, finds the groupBy exercise, and dismisses; question filters and the no-match state; notebook add/edit/export/delete/import, including duplicate skipping and invalid-file rejection; the six-phase execution walkthrough; the visual lab step controls; mobile navigation and focus return; the no-JavaScript pass at phone width; a horizontal-overflow sweep at 320/390/768/1280 px with every disclosure open; and zero JavaScript console errors.

## Checks

- First run: `PASS: 66 browser checks passed` in about 5 seconds against the current build (Python Playwright 1.58, headless Chromium, reduced motion).
- The harness is deliberately not part of the GitHub Actions workflow, which continues to run content, link, and JavaScript syntax checks only.
- New-machine setup: `python3 -m pip install playwright` and `python3 -m playwright install chromium`; an installed Chrome is used as a fallback.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `fb32a203f32ffa5bf333cec6ee6ab3721671855b` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34819485811](https://github.com/anchitgupt/learn-spark/actions/runs/34819485811) completed successfully.
- All 27 public build files returned HTTP 200 and matched the local build byte for byte after deployment; this change adds repository tooling and documentation only, so the published site is unchanged.

# Executor memory lesson — 2026-09-14

## Content

- Added "Executor memory, spill & out-of-memory errors" as the ninth fundamentals lesson (slug `executor-memory`, lesson 09 of 11), placed between "Caching & fault tolerance" and the execution-flow capstone. Existing slugs and saved progress remain valid; the capstone and prediction lesson renumber to 10 and 11 automatically.
- The lesson covers the executor memory model (heap plus overhead, the 300 MiB reserve, `spark.memory.fraction` and `spark.memory.storageFraction`, execution-versus-storage eviction), what spills and how the Spark UI reports it (Shuffle spill memory/disk, peak execution memory, SQL operator spill size), the three out-of-memory failure locations (driver, executor task, container/overhead, plus PySpark workers), and a debugging order that shrinks the unit of work before changing memory sizes.
- Claims are tied to the versioned sources: the tuning and configuration guides (3.5.7), the Web UI guide for metric meanings, and the `UnifiedMemoryManager` and `UnsafeExternalSorter` sources. The lesson deliberately avoids exact counts: it tells the reader to read spill relative to the stage and compare tasks rather than expect fixed numbers. The example was not executed in Spark on this machine, and the page says so.

## Checks

- `npm run build` and `npm run check`: 15 pages, 572 local links/assets, 11 lesson schemas and example syntax, 15 questions, three prediction exercises, JavaScript syntax pass; `git diff --check` clean.
- `python3 scripts/browser_test.py`: 66 checks pass with the 15-page site; the suite's progress checks now derive lesson counts from content instead of hardcoding them.
- axe-core 4.10.2 on the new lesson: zero violations at 1280 and 390 CSS pixels. Screenshots were inspected at both widths (`output/playwright/executor-memory-*.png`).

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.