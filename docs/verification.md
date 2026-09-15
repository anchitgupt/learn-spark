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

## Publication check

- Implementation commit `7ae3713a030ce49641d2389d4a844b740a4ad05b` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34821294435](https://github.com/anchitgupt/learn-spark/actions/runs/34821294435) completed successfully.
- All 28 public build files returned HTTP 200 and matched the local build byte for byte after deployment.
- Live lesson: https://anchitgupt.github.io/learn-spark/executor-memory.html
# Spark UI lesson — 2026-09-14

## Content

- Added "Reading the Spark UI and fixing slow jobs" as the tenth fundamentals lesson (slug `spark-ui`, lesson 10 of 12), placed between "Executor memory, spill & out-of-memory errors" and the execution-flow capstone. Existing slugs and saved progress remain valid; the capstone and prediction lesson renumber to 11 and 12 automatically.
- The lesson teaches a diagnosis order: Jobs tab to the longest job, Stages tab to the longest stage, per-task distribution (duration, input, shuffle, spill, GC) to separate general pressure from a straggler, SQL tab operator metrics (output rows, shuffle bytes, spill size, peak memory) to name the expensive operator, then fixes in layout → reuse → eligible AQE → configuration order.
- Claims are tied to versioned 3.5.7 sources: the Web UI guide (Jobs/Stages/Storage/Executors/Environment/SQL tabs, stage summary metrics, SQL operator metrics), the tuning guide (2–3 tasks per core, reduce-task parallelism, locality levels), and the SQL performance tuning guide (shuffle partitions, AQE coalescing/broadcast/skew features, enabled by default since 3.2). The lesson deliberately avoids exact counts: it tells the reader to compare tasks against the median and read the stage rather than expect fixed numbers. The example was not executed in Spark on this machine, and the page says so.
- Added two authored practice questions (`practice-spark-ui-slow-job`, `practice-spark-ui-straggler`); none is presented as a reported interview question.

## Checks

- `npm run build` and `npm run check`: 16 pages, 629 local links/assets, 12 lesson schemas and example syntax, 17 questions, three prediction exercises, JavaScript syntax pass; `git diff --check` clean.
- `python3 scripts/browser_test.py`: 66 checks pass with the 16-page site.
- axe-core 4.10.2 on the new lesson: zero violations at 1280 and 390 CSS pixels. Screenshots were inspected at both widths (`output/playwright/spark-ui-*.png`).

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check

- Implementation commit `7955261e4d331f4c9aa51943525c09a388b5abb8` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34823257502](https://github.com/anchitgupt/learn-spark/actions/runs/34823257502) completed successfully.
- All 29 public build files returned HTTP 200 and matched the local build byte for byte after deployment (one CSS fetch lagged the CDN on the first sweep, then matched on recheck).
- Live lesson: https://anchitgupt.github.io/learn-spark/spark-ui.html

# Web-inspired interview questions — 2026-09-14

## Content and sources

- Added 12 original practice questions inspired by public interview-topic lists from Adaface, DataCamp, and DataCodingHub. The bank now has 29 questions: one interview-reported, sixteen authored practice, and twelve web-inspired practice questions.
- Topics: RDD map/flatMap, reduceByKey versus groupByKey, unionByName, null-safe joins, semi/anti joins, broadcast hint limits, RDD/DataFrame cache defaults, checkpoint reliability, accumulator retries, Python UDFs and Arrow, window ranking ties, and AQE versus dynamic allocation.
- Each new record retains `origin: "practice"` and includes a question-inspiration link, versioned Apache technical references, the Spark 3.5.7 baseline, and the review date. Answers and follow-ups use original wording; online list answers were not imported as verified facts.
- Checked the relevant Spark 3.5.7 API/guide pages and the versioned `AggUtils.scala` source for partial aggregation. Preserved qualifications around accumulator retries, join eligibility, null multiplicity, API-specific cache defaults, local checkpoint reliability, and Arrow UDF execution.
- The new questions contain no runnable example blocks. Their explanations were checked against documentation/source, not executed in a Spark runtime. The card disclosures state this limitation and distinguish inspiration from technical evidence.

## Implementation and validation

- Source links, attribution, baseline, and review scope render within each new question's answer disclosure. Existing questions retain their previous provenance and lesson-source fallback.
- The content checker validates inspiration metadata, practice provenance, review dates, and versioned Apache reference URLs. The browser suite checks reference association with each card, new-question search, and no-JavaScript access to references.
- `npm run build`: 16 pages built.
- `npm run check`: 16 pages, 644 local links/assets, 12 lesson schemas/examples, 29 questions, and 3 prediction exercises passed, plus JavaScript syntax checks.
- `npm run test:browser`: all 69 checks passed, including every page at 320/390/768/1280 CSS pixels with disclosures open.
- The first browser pass detected a 320 px overflow from the `pyspark.sql.DataFrame.localCheckpoint` reference title. Confirmed its right edge at 335.75 px, added wrapping within the reference list, and reran the full suite successfully.
- No Spark runtime execution or publication was performed in this batch.

# Storage formats lesson and file-format questions — 2026-09-14

## Content

- Added "Storage formats: Parquet, ORC & Avro" as the eleventh fundamentals lesson (slug `storage-formats`, lesson 11 of 13), placed between "Reading the Spark UI and fixing slow jobs" and the execution-flow capstone. Existing slugs and saved progress remain valid; the capstone and prediction lessons renumber to 12 and 13 automatically.
- The lesson covers row versus column layout, the Parquet physical hierarchy (row groups, column chunks, pages, footer read first, write-once files), page encodings and the dictionary fallback, bloom filters, the four levels at which a scan skips data, file and partition sizing with the small-file problem, schema evolution, and table formats (Delta Lake, Iceberg, Hudi) as metadata layers outside the Spark baseline.
- Added a versioned SVG asset `assets/parquet-layout.svg` (row groups, per-column chunks with pages and min/max, footer read first) rendered through `scripts/build.py` with alt text and a caption, modeled on the supplied layout diagram. Added thirteen file-format practice questions (`format-*`, `collection: "file-formats"`) mapped to the new lesson, each with versioned references, a review date, and the 3.5.7 baseline.
- Checker extensions: a question `topic` now resolves against lessons or `content/question-topics.json`; questions validate `collection`; approved sources add the official documentation of the Apache Parquet, ORC, Avro, and Iceberg projects and the Delta Lake project alongside versioned Spark docs and `apache/spark` source. The README records the policy.
- Claims checked against the Parquet project's file-format and encoding pages (single-pass writing, metadata read first, encodings, bloom filters), the Spark 3.5.7 Parquet/ORC/Avro data-source guides, the SQL tuning guide, the Iceberg table spec, and the Delta Lake documentation. The example was not executed in Spark on this machine; the lesson page says so.

## Checks

- `npm run build` and `npm run check`: 17 pages, 719 local links/assets, 13 lesson schemas and example syntax, 42 questions, three prediction exercises; JavaScript syntax pass; `git diff --check` clean.
- `python3 scripts/browser_test.py`: 73 checks pass with the 17-page site, including the new diagram render, the storage search result, and the lesson's disclosure.
- axe-core 4.10.2 on `storage-formats.html`: zero violations at 1280 and 390 CSS pixels. Screenshots were inspected at both widths (`output/playwright/storage-formats-*.png`, `storage-parquet-diagram.png`).

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

# Senior DE interview bank — 2026-09-14

## Content

- Added 34 reviewed practice questions covering the supplied senior-bank sections: architecture and execution (job/stage/task, deploy modes, driver state, narrow versus wide, laziness, RDD/DataFrame/Dataset), partitioning and shuffle (repartition/coalesce, partition counts, shuffle partitions, shuffle writes, fetch throttling, bucketing), joins (strategies, selection, broadcast limits, sort-merge versus shuffled hash, outer joins, a 10 TB join), memory and OOM (layout, driver versus executor OOM, memoryOverhead), skew and tuning (skew fixes, salting, few-task stages, spill, speculation), Catalyst and AQE (planning phases, whole-stage codegen, AQE scope and limits, pushdown blockers), and PySpark specifics (UDF cost, pandas UDFs, order of preference).
- `content/senior-interview-guide.json` indexes 40 prompts in 7 groups. Six prompts link to existing reviewed cards rather than duplicating answers (the reported flow question, the cache and checkpoint questions, skew detection), and the Python-memory prompt links to the memoryOverhead card, so one card serves two bank prompts. The guide renders as native disclosures above the question bank with its prompt count.
- Answers correct the supplied draft where it oversimplified: one action can trigger several jobs; the driver holds the DAG and task schedulers, map-output tracker, and block-manager master state; null outer-join keys never match rather than concentrating work (rewriting them to a sentinel creates the hot key); broadcast eligibility depends on join type and keys, and a hint is not a size promise; salting's duplication and final-shuffle costs are stated; speculation's duplicate-attempt risk is stated.
- Claims checked against versioned Spark 3.5.7 documentation (configuration, tuning, Web UI, RDD, SQL performance tuning, data source and Arrow guides) and the `DAGScheduler`, `QueryExecution`, and `WholeStageCodegenExec` sources; the codegen summary is quoted from the source file. The questions were not executed in a Spark runtime; the cards state the documentation-review limitation.

## Checks

- `npm run build` and `npm run check`: 17 pages, 793 local links/assets, 13 lesson schemas and example syntax, 76 questions, three prediction exercises; JavaScript syntax pass; `git diff --check` clean. The checker now validates the senior guide: group structure, prompt and link targets, full coverage of `senior-de` questions, and the rendered prompt count.
- `python3 scripts/browser_test.py`: 78 checks pass, including guide rendering, group expansion, prompt-link navigation, and the updated text-filter expectations.
- axe-core 4.10.2 on `questions.html` with the guide expanded: zero violations at 1280 and 390 CSS pixels. The expanded guide screenshot was inspected (`output/playwright/senior-guide.png`).

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check (web questions, storage formats, and senior bank)

- Implementation commits `6b946de` (web-inspired questions), `2fce063` (storage formats and file-format questions), and `f8a7a9b` (senior bank and guide) pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34838525509](https://github.com/anchitgupt/learn-spark/actions/runs/34838525509) and [34839144597](https://github.com/anchitgupt/learn-spark/actions/runs/34839144597) completed successfully.
- All 31 public build files returned HTTP 200 and matched the local build byte for byte after deployment; the live questions page shows the 40-prompt, 7-group senior guide.
- Live pages: https://anchitgupt.github.io/learn-spark/storage-formats.html and https://anchitgupt.github.io/learn-spark/questions.html

# Complete senior-bank coverage — 2026-09-15

## Scope and method

- Closed the gaps found against the supplied senior DE bank: sections 7 (Delta Lake and storage), 8 (Structured Streaming), 10 (coding round), 11 (design and scenario), and 12 (incident stories) had no questions, and Catalyst/AQE and PySpark UDFs had questions but no lesson. Also completed the deferred jobs/stages/tasks study sheet and a sweep of common interview topics still missing.
- Added seven lessons (Catalyst, code generation & AQE; PySpark UDFs, Arrow & the Python boundary; Delta Lake; Structured Streaming; Count the jobs, stages, and tasks; The PySpark coding round; Designing data pipelines), 69 questions, 8 measured counting exercises, two diagrams (`assets/delta-log.svg`, `assets/streaming-microbatch.svg`), and five senior-guide groups. Seven existing cards were corrected and nine moved to the new lessons with unchanged IDs. The storage-formats lesson's "one task per file" claim was corrected to file packing charged by `spark.sql.files.openCostInBytes`.
- Runtime: a private JDK 17 (Temurin 17.0.20.1) with PySpark 3.5.7, delta-spark 3.2.1, pandas, and PyArrow, installed outside the repository. Examples ran in local mode (`local[2]` or `local[4]`; one demonstration on `local-cluster[2,1,1024]`). Every published lesson code block, exercise, and runtime-noted card was run; outputs are copied from logs. Run scripts and logs stay outside the repository.
- Drafting ran in seven parallel workstreams, each writing drafts and evidence outside the repository. Every draft was reviewed against its run logs and sources before integration; review notes and coordinator corrections follow.
- Generator changes: chapter-grouped sidebar and homepage (`scripts/chapters.py`), lesson diagrams and runtime notes from content, several exercise lessons with `label` and `observed`, Coding and Design question filters, preformatted multi-line outputs, prose-only lesson search text, and title-first search ranking. The checker validates chapters, diagram assets, runtime notes, question types and collections, Delta Lake 3.2.1 sources, Python syntax of every lesson code block, per-lesson exercise anchors, and senior-guide coverage; placeholder topic labels were retired.

## Coordinator review

### Review: pipeline-design
- Reviewed lesson, 10 cards, guide groups, verification notes, and all run logs; observed outputs match published claims.
- Corrected AQE skew-join scope: OptimizeSkewedJoin.scala (v3.5.7) handles SortMergeJoinExec and ShuffledHashJoinExec, not only sort-merge joins. Fixed in the incident-stories section and story-skew-fix.
- TODO at integration: existing card `senior-aqe` says "splitting skewed sort-merge join partitions" — widen to include shuffled hash joins unless the catalyst workstream already corrected it.

### Review: delta-lake
- Reviewed lesson, 10 cards, guide, verification, and logs (log_conflict, merge_dv, optimize_skipping, vacuum_timetravel, schema_cdf, small_files, lesson_code); published numbers match logs.
- Accepted new card senior-parquet-orc-avro (no existing card covers all three formats).
- Applied the workstream's correction to the existing storage-formats lesson: "one task per file" replaced with file packing charged by spark.sql.files.openCostInBytes (observed 400 tiny files -> 13 scan partitions in delta-lake/runs/small_files.log).

### Review: coding-round
- Reviewed lesson (7 sections, every block generated from runs/blocks with log output), 6 cards, guide, verification notes. Accepted.
- Guide item "Join a stream to a slowly changing dimension" depends on coding-stream-scd-join from the streaming workstream.

### Review: gap-sweep
- Reviewed 16 authored cards and verification notes. Accepted.
- assertDataFrameEqual behavior was observed with a one-line np.NaN shim because PySpark 3.5.7's pyspark.testing import fails under NumPy 2.0.2 in this runtime; the unit-test card states the environment caveat without claiming a supported NumPy range.

### Review: catalyst-udfs
- Reviewed both lessons, 8 new cards, 7 card corrections with old/new text side by side, verification notes. Accepted.
- The senior-aqe correction now says "splits skewed join partitions" and the catalyst-aqe lesson states that the 3.5.7 rule matches sort-merge and shuffled hash joins, resolving the pipeline-design TODO.
- Coordinator added a runtime note and reviewed date 2026-09-15 to each corrected card, because the corrected answers cite local observations recorded in the local run folder.

### Review: structured-streaming
- Reviewed lesson (6 sections, diagram rendered and inspected), 11 cards, guide group, verification notes, and run list r01-r11. Accepted.
- coding-stream-scd-join is placed in the "Coding round" guide group by the coding-round guide file.

### Review: count-spark-work
- Reviewed lesson (5 sections), 8 exercises with observed counts, 8 exercise-linked cards, verification notes with per-action REST tables. Accepted; the sheet's answers were not used.
- Coordinator separated the prose lines of the lesson output from the printed REST summary so the printout renders preformatted.
- Cards receive collection "metrics-sheet" at integration so they render as supplied practice.

## Workstream records

## Catalyst, AQE, and PySpark UDF lessons — 2026-09-15

### Content

- Added "Catalyst, code generation & AQE" (slug `catalyst-aqe`, FUNDAMENTALS, 6 sections): the four plans printed by `explain("extended")`, other explain modes, physical planning (strategies in rule order, first plan taken, statistics and CBO), preparation rules (EnsureRequirements, CollapseCodegenStages) and codegen boundaries, what blocks predicate pushdown and partition pruning (observed table), AQE coalescing, runtime join switching and skew splitting as they appear in the plan, and AQE's limits. Links `lazy-evaluation.html`, `spark-ui.html`, `joins-skew.html`, and `storage-formats.html` by page.
- Added "PySpark UDFs, Arrow & the Python boundary" (slug `pyspark-udfs`, FUNDAMENTALS, 5 sections): where Python runs (driver versus Python worker processes), what a row-at-a-time UDF sends across the boundary, BatchEvalPython/ArrowEvalPython in the plan, codegen and pushdown effects, double evaluation of deterministic UDFs, Arrow-optimized Python UDFs versus pandas UDFs and pandas function APIs, `maxRecordsPerBatch`, Python worker memory (`spark.executor.pyspark.memory` versus `memoryOverhead`), and the order of preference with a labeled local timing illustration. Links `dataframes.html`, `catalyst-aqe.html`, and `executor-memory.html`.
- Added 8 authored questions (no `collection`): `catalyst-analyze-cbo`, `catalyst-explain-no-codegen-markers`, `catalyst-first-physical-plan`, `catalyst-aqe-broadcast-shuffle-cost`, `pyudf-mapinpandas-applyinpandas`, `pyudf-topandas-arrow-driver`, `pyudf-arrow-batch-size`, `pyudf-udf-evaluated-twice`.
- Proposed corrections for 7 existing cards (`card-corrections.json`); `senior-whole-stage-codegen` and `web-python-udf-arrow` were re-checked and left unchanged.
- Corrections to the supplied bank draft:
  - "Physical candidates (CBO)": in 3.5.7 `QueryExecution.createSparkPlan` takes the first plan (`next()`, source comment), join choice is rule-ordered over estimates, and CBO (`spark.sql.cbo.enabled`, default false) affects logical estimates and join reordering only with collected statistics.
  - "Casts on the partition column block pushdown": false for file-source partition pruning — `cast(day as string) = '2026-09-02'` stayed a PartitionFilter and read 2 of 6 files. Casts on data columns do block Parquet pushdown (only `IsNotNull` pushed).
  - "Some OR predicates": an OR of two data-column predicates was pushed as `Or(...)`; an OR mixing a partition column and a data column was neither pruned nor pushed.
  - "They break codegen and pushdown": they split codegen (operators on either side still generate code) and block pushdown only of predicates depending on the UDF; unrelated filters still moved below it.
  - "Pandas/Arrow UDFs 10–100× faster": not a supportable general multiplier. Arrow-optimized Python UDFs still call the function per row (3.5.7 `worker.py`; guide: "executed row-by-row"). Local illustration only: built-in 0.15 s, pandas UDF 0.38 s, Arrow Python UDF 0.60 s, Python UDF 1.22 s.
  - "Types: scalar, grouped map, grouped agg": 3.5.7 prefers type hints (Series→Series, Iterator variants, Series→scalar); grouped map is the `applyInPandas` function API, and `PandasUDFType` "will be deprecated".
  - "AQE switch SMJ→BHJ": correct, but it happens after the shuffle map stages were written; SMJ→SHJ needs `maxShuffledHashJoinLocalMapThreshold` > 0 (default 0). Skew handling in the 3.5.7 rule matches sort-merge and shuffled hash joins.
  - "Where does Python memory come from? memoryOverhead": true only while `spark.executor.pyspark.memory` is unset; when set, it is added to the YARN/Kubernetes request and split per core as an RLIMIT_AS limit in each worker (not enforced on macOS).
- Sources checked: Spark 3.5.7 docs (EXPLAIN, ANALYZE TABLE, SQL performance tuning, configuration, Parquet data source, built-in functions, Arrow/pandas user guide, PySpark API pages for `udf`, `pandas_udf`, `mapInPandas`, `applyInPandas`, `toPandas`, `explain`) and v3.5.7 source (`QueryExecution`, `QueryPlanner`, `SparkStrategies`, `SizeInBytesOnlyStatsPlanVisitor`, `CostBasedJoinReorder`, `EnsureRequirements`, `WholeStageCodegenExec`, `FileSourceStrategy`, `DataSourceStrategy`, `ExtractPythonUDFs`, `EvalPythonExec`, `BatchEvalPythonExec`, `AdaptiveSparkPlanExec`, `InsertAdaptiveSparkPlan`, `OptimizeSkewedJoin`, `PythonRunner`, `python/pyspark/worker.py`). Every URL returned HTTP 200. Some docstrings were read from the installed PySpark 3.5.7 package, because WebFetch returned only navigation for those API pages. The published pages are generated from the same docstrings, and each page was confirmed to resolve.

### Runtime evidence

Environment: local PySpark 3.5.7, `local[2]`, JDK 17, pandas and PyArrow installed, driver memory 1g, on 2026-09-15. Scripts and logs are in the local run folder.

- `confs.py` → `SET -v` in 3.5.7: `spark.sql.cbo.enabled=false`, `spark.sql.cbo.joinReorder.enabled=false`, `spark.sql.adaptive.enabled=true`, `coalescePartitions.parallelismFirst=true` ("It's recommended to set this config to false"), `maxShuffledHashJoinLocalMapThreshold=0b`, `skewJoin.skewedPartitionFactor=5.0`, `skewedPartitionThresholdInBytes=256MB`, `spark.sql.execution.arrow.maxRecordsPerBatch=10000`, `spark.sql.execution.pythonUDF.arrow.enabled=false`.
- `lesson_code_catalyst.py` (lesson snippet, default settings) → extended explain printed parsed (`'Aggregate ['category] ...`), analyzed, optimized (`Filter (isnotnull(amount#2) AND (amount#2 > 10.0))`), and physical `AdaptiveSparkPlan isFinalPlan=false` with `Exchange hashpartitioning(category#1, 200), ENSURE_REQUIREMENTS` and no `*(n)`. After `collect()`, `explain()` printed `isFinalPlan=true`, `== Final Plan ==` with `*(2) HashAggregate`, `AQEShuffleRead coalesced`, `ShuffleQueryStage 0`, `*(1)` partial aggregate/project/filter/scan, then `== Initial Plan ==`.
- `catalyst_explain.py` → `formatted` output with numbered operators; `collect_list` → `ObjectHashAggregate` without star; under AQE before execution, `explain codegen` → "Found 0 WholeStageCodegen subtrees."
- `codegen_cbo.py` → AQE off: `*(1)`/`*(2)` shown before execution, "Found 2 WholeStageCodegen subtrees"; Python UDF plan `*(1)` → `BatchEvalPython` → `*(2)`; `transform` Project printed without star. Filter estimate for `amount > 900` on 1,000 rows: no stats 5.5 KiB; table stats with CBO off 5.5 KiB; table stats with CBO on `sizeInBytes=19.5 KiB, rowCount=1.00E+3`; column stats with CBO on `sizeInBytes=2000.0 B, rowCount=100`; column stats with CBO off 5.5 KiB.
- `pushdown_udf.py` + `pruning_check.py` (3,000 rows, partitioned by `day` inferred as `date`, 3 partitions, 6 files) → built-in `amount > 400`: `PushedFilters: [IsNotNull(amount), GreaterThan(amount,400)]`; Python UDF: `PushedFilters: []`, `Filter pythonUDF0` over `BatchEvalPython`; both counts 594. `cast(amount as string) = 450`: `PushedFilters: [IsNotNull(amount)]`. `rand(7) < 0.5` conjunct: deterministic part still pushed. `user_id < 10 OR amount > 400`: `Or(LessThan(user_id,10),GreaterThan(amount,400))`. Scan metrics with AQE off: no filter 6 files/3 partitions; `day =` 2 files/1 partition; `cast(day as string) =` 2 files/1 partition (`PartitionFilters: [isnotnull(day#12), (cast(day#12 as string) = 2026-09-02)]`); Python UDF on day 6 files/3 partitions; `day = ... OR amount > 400` 6 files/3 partitions, no partition or pushed filter.
- `aqe_runtime.py` → coalesce: 200 shuffle partitions, 10 keys; reduce stage 1 task (`AQEShuffleRead coalesced`), with coalescing disabled 200 tasks. Join (`autoBroadcastJoinThreshold` 1 MiB, shuffle partitions 8): dim side estimate `Statistics(sizeInBytes=13.4 MiB)`; initial `SortMergeJoin`; final `BroadcastHashJoin [fk#42L], [pk#46L], Inner, BuildLeft` over `BroadcastQueryStage 2` and `AQEShuffleRead local` / `ShuffleQueryStage 0` and `1`; inferred `Filter ((fk#42L < 50) ...)` on the fact side. Skew (thresholds lowered to 10KB, coalescing off, broadcast off): `SortMergeJoin(skew=true)`, `AQEShuffleRead skewed`, join stage 9 tasks versus 8 partitions.
- `lesson_code_udfs.py` (lesson snippet) and `udf_compare.py` → built-in `*(1) Project [id#0, upper(name#1) ...]`; Python UDF `BatchEvalPython`; Arrow Python UDF `ArrowEvalPython [...], 101`; pandas UDF `ArrowEvalPython [...], 200`; `id > 1` filter below the UDF in all. Driver Python PID 31455, worker PIDs [31531, 31532]. Batch sizes for 25,000 rows in one partition: default → (5000 ×1 batch, 10000 ×2 batches); `maxRecordsPerBatch=1000` → all 1000. Plans: Iterator UDF `ArrowEvalPython ... 200`; Series→scalar `AggregateInPandas` over `Sort` + `Exchange`; `applyInPandas` → `FlatMapGroupsInPandas` over `Sort` + `Exchange`; `mapInPandas` → `MapInPandas` over scan. `toPandas` 500,000 rows: Arrow 0.42 s, no Arrow 1.46 s. Timing illustration (2,000,000 cached strings, best of 3, sum of `length(upper(name))` = 22888890): built-in 0.15 s, Python UDF 1.22 s, Arrow Python UDF 0.60 s, pandas UDF 0.38 s.
- `eager_nondet.py` → `orders.select("amont")` raised `AnalysisException [UNRESOLVED_COLUMN.WITH_SUGGESTION]` at definition. A deterministic UDF selected and then filtered produced two `BatchEvalPython` operators; the same UDF with `asNondeterministic()` produced one, with the filter above it.
- `build_drafts.py` → writes the JSON drafts and checks balanced HTML, section-source anchors, escaped angle brackets, Python syntax of both `code` fields, answer word counts (60–170), and ID uniqueness against `existing-questions.txt`.

### Limits

- `spark.executor.pyspark.memory` enforcement, YARN/Kubernetes container accounting, and container-kill behavior are documentation- and source-reviewed only. The configuration reference says the limit is not enforced on macOS.
- The per-core split of PySpark memory (`PythonRunner.getWorkerMemoryMb`: `mem / cores`) and the `hugeMethodLimit` codegen fallback are source-reviewed only.
- Shuffled hash join handling in `OptimizeSkewedJoin`, and the preparation-rule order, are source-reviewed only. The skew run used lowered thresholds on a laptop-sized dataset; the defaults (5× median and 256 MB) were not exercised.
- The join-switch run lowered `spark.sql.autoBroadcastJoinThreshold` to 1 MiB so a small local file could show the switch.
- Timings come from one laptop running concurrently with other agents. They illustrate relative overhead for one trivial function and are not benchmarks.
- Attribute IDs, plan IDs, and PIDs vary between runs.

## Delta Lake lesson and storage questions — 2026-09-15

Baseline: Apache Spark 3.5.7 with Delta Lake 3.2.1. The `docs.delta.io/3.2.1/…` paths return 404, so every Delta documentation claim was checked against the version-tagged documentation sources in the Delta repository (`github.com/delta-io/delta/blob/v3.2.1/docs/source/*.md`), `PROTOCOL.md`, and Scala source at the same tag.

### Content

- New lesson `delta-lake` (chapter LAKEHOUSE): "Delta Lake: transactions, MERGE & maintenance". Six sections: the transaction log, commits and conflicts, MERGE cost, layout (statistics, partitioning, Z-order, OPTIMIZE), VACUUM/time travel/RESTORE, and schema enforcement and evolution. It links back to `storage-formats.html` instead of repeating Parquet internals.
- New original diagram `assets/delta-log.svg` (role="img", title, desc): data files, `_delta_log` commits with add/remove actions, a checkpoint, a reader resolving snapshot 11, and two writers racing for version 12. It uses the `parquet-layout.svg` palette, with viewBox 880×520 and a minimum font size of 14.
- Senior-bank cards (collection `senior-de`), indexed as the guide group "Delta Lake and storage", in bank order: `delta-acid-object-storage`, `delta-merge-cost`, `delta-zorder-vs-partitioning`, `delta-optimize-vacuum`, `senior-parquet-orc-avro`, `senior-small-files`.
- Authored cards: `delta-conflict-types`, `delta-time-travel-vacuum`, `delta-merge-schema-evolution`, `delta-change-data-feed`.
- `senior-parquet-orc-avro` is a new card because no existing card answers the three-way prompt. `format-orc-vs-parquet` omits Avro; `format-avro-role` and `format-row-vs-columnar` omit ORC. The new card is short and defers depth to those cards.

Corrections to the supplied bank draft:

- "A write commits by atomically creating the next log file." That atomicity is the storage system's mutual exclusion (put-if-absent), not Delta's own. The Delta 3.2.1 storage docs say S3 does not provide mutual exclusion and that concurrent writes from multiple Spark drivers can lead to data loss. The alternatives are a single driver or the experimental `S3DynamoDBLogStore` on every writer. HDFS and Azure provide the guarantee; GCS needs the correct LogStore configured.
- "MERGE: two passes (find matching files, rewrite them)." The phases are right (inner join to find touched files, then a join that rewrites them, then one commit). The draft misses that the cost is rewrite volume: every unmodified row in a touched file is copied (observed 72 copied rows for 3 updates). Deletion vectors change this to writing only changed rows plus DVs (observed 0 copied rows), at the price of a protocol upgrade (reader 3 / writer 7) and read-time filtering. "Low shuffle merge" is labeled as a Databricks feature, not OSS Delta.
- "VACUUM removes unreferenced files past the retention window." Clarified: VACUUM removes files that no version inside the retention window still needs, meaning files the current version no longer references whose removal is older than the threshold (7 days by default). Log files expire on a separate 30-day clock.
- "Small files: one task per file." Wrong for Spark 3.5.7 file scans, which pack files into partitions using `maxPartitionBytes` plus `openCostInBytes` per file. Observed: 400 files became 13 partitions. **The existing `storage-formats` lesson section "Reading less" says "one task per file"; the coordinator should correct it.**
- "Small files: no effective pushdown." Too strong. Pushdown still applies (PushedFilters shown on 400 tiny files); the problem is per-file overhead (observed 2.89 s versus 0.46 s).
- "ORC: better ACID legacy in Hive." Attributed: ACID transactional tables are a Hive feature implemented on ORC base and delta files (ORC project docs), not a property the ORC format gives a Spark job. "Parquet: columnar + predicate pushdown" was also misleading as a differentiator, since ORC supports pushdown too.
- "Z-order for high-cardinality co-located filtering." Kept, with the qualifiers the docs require: statistics exist only for the first 32 columns by default, locality weakens per extra column, and ZORDER is not idempotent.

### Runtime evidence

Environment: local PySpark 3.5.7, `local[2]`, JDK 17, delta-spark 3.2.1 from local jars, run 2026-09-15. Scripts and full logs are in `runs/`.

- `runs/log_conflict.py`
  - Commit 0 held `commitInfo` (WRITE), `metaData`, `protocol` (minReaderVersion 1, minWriterVersion 2), and two `add` actions whose stats are JSON with numRecords, minValues, maxValues, and nullCount.
  - Commit 1 (DELETE `order_id = 1`) held `commitInfo` with `"readVersion": 0` and `numCopiedRows 3`, plus `remove` (with `deletionTimestamp`, `dataChange: true`) for the 4-row file and `add` for a 3-row file.
  - After commit 10, the log contained `00000000000000000010.checkpoint.parquet` and `_last_checkpoint` `{"version":10,"size":14,…,"numOfAddFiles":11,…}`; the checkpoint rows were add 11, remove 1, metaData 1, protocol 1. The log directory also contained an empty `_commits` directory.
  - Blind INSERT pairs (3 rounds): `{'A': 'ok', 'B': 'ok'}` each time; history readVersion pairs 0/0, 2/2, 4/4.
  - UPDATE vs DELETE: `('ConcurrentAppendException', …, '[DELTA_CONCURRENT_APPEND] ConcurrentAppendException: Files were added to the root of the table by a concurrent update. Please try the operation again.')` on DELETE.
  - UPDATE vs `INSERT … SELECT` from the same table: the UPDATE got the same exception, and the INSERT committed with `isBlindAppend false`.
- `runs/merge_dv.py`: 100 rows in 4 files; MERGE with 5 source rows (3 matches in 3 files, 2 inserts).
  - Default: `numTargetFilesRemoved 3, numTargetFilesAdded 1, numTargetRowsUpdated 3, numTargetRowsInserted 2, numTargetRowsCopied 72, numTargetDeletionVectorsAdded 0, numOutputRows 77`.
  - With `delta.enableDeletionVectors = true`: `numTargetFilesRemoved 0, numTargetFilesAdded 2, numTargetRowsCopied 0, numTargetDeletionVectorsAdded 3, numOutputRows 5`. The commit re-added 3 paths with `deletionVector {"storageType": "u", …, "cardinality": 1}` and removed the same paths without a DV. `DESCRIBE DETAIL`: minReaderVersion 3, minWriterVersion 7, tableFeatures `['appendOnly', 'deletionVectors', 'invariants']`.
- `runs/optimize_zorder.py`
  - OPTIMIZE on 40 tiny files: `numFilesAdded 1, numFilesRemoved 40, totalConsideredFiles 40, numBatches 1`; history operationParameters `{'predicate': '[]', 'auto': 'false', 'zOrderBy': '[]', 'clusterBy': '[]'}`. A second OPTIMIZE: `numFilesAdded 0, numFilesRemoved 0`.
  - OPTIMIZE ZORDER BY (user_id) with an 8 KiB maxFileSize: `numFilesAdded 7, numFilesRemoved 40`; zOrderStats `strategyName='all'`.
  - A 34-column table's add stats had 32 minValues columns, the last being `c31`.
  - This script's "files read" figure used `input_file_name()` and so counted files with matching rows, not files scanned. It was superseded by `optimize_skipping.py`.
- `runs/optimize_skipping.py`: scan-node metric "number of files read", from the Spark UI REST API, for `user_id BETWEEN 100 AND 120`. Unoptimized: 40 of 40 (2,000 output rows); OPTIMIZE (8 KiB): 8 of 8; OPTIMIZE ZORDER BY: 1 of 7 (286 output rows). Each matched the count of files whose logged min/max overlaps the range, and the plan location was `PreparedDeltaFileIndex`.
- `runs/vacuum_restore.py`
  - RESTORE TO VERSION AS OF 0 on an unvacuumed table: `{'table_size_after_restore': 789, 'num_of_files_after_restore': 1, 'num_removed_files': 1, 'num_restored_files': 1, 'removed_files_size': 774, 'restored_files_size': 789}`; history version 3 RESTORE; row count back to 10.
  - VACUUM history: `VACUUM START {'numFilesToDelete': '2'}`, `VACUUM END {'numDeletedFiles': '2'}`.
  - This script's time-travel check used `count()`, which succeeded; re-tested below.
- `runs/vacuum_timetravel.py`
  - `VACUUM RETAIN 0 HOURS` with the check on: `IllegalArgumentException: requirement failed: Are you sure you would like to vacuum files with such a low retention period? If you have writers that are currently writing to this table, there is a risk that you may corrupt the state of your Delta table. … you may turn off this check by setting:`
  - DRY RUN at default retention listed 0 files; RETAIN 0 HOURS DRY RUN listed 2.
  - After vacuum, version 0 `count()` returned 10 with physical plan `LocalTableScan [count]`.
  - `collect()` raised `org.apache.spark.SparkFileNotFoundException: File file:/…/part-00000-8f20765d-….snappy.parquet does not exist`, and `VERSION AS OF 1` failed the same way.
  - RESTORE failed with `IllegalArgumentException: Not all files from version 0 are available in file system. Missed files (top 100 files): part-00000-8f20765d-….snappy.parquet.`
- `runs/schema_cdf.py`
  - Extra-column append: `AnalysisException: [_LEGACY_ERROR_TEMP_DELTA_0007] A schema mismatch detected when writing to the Delta table`. Wrong type: `[DELTA_FAILED_TO_MERGE_FIELDS] Failed to merge fields 'name' and 'name'`. The mergeSchema append gave `struct<id:bigint,name:string,tier:string>`.
  - MERGE `*` with autoMerge off: schema `struct<id:bigint,name:string>`, rows `[(1,'a'),(2,'B'),(9,'z')]`. Explicit `SET tier`: `[DELTA_MERGE_UNRESOLVED_EXPRESSION] Cannot resolve tier in UPDATE clause given columns t.id, t.name`. With autoMerge on: `struct<id:bigint,name:string,tier:string>`, rows `[(1,'a',None),(2,'B','gold'),(9,'z','silver')]`.
  - CDF: inserts at v0; `update_preimage b` and `update_postimage B` at v1; `delete` at v2; two `cdc-*.snappy.parquet` files in `_change_data`.
- `runs/small_files.py`: 400 tiny Parquet files, defaultParallelism 2, maxPartitionBytes 134217728b, openCostInBytes 4194304b.
  - Scan partitions: 13 with defaults, and 40 with openCostInBytes=1 and maxPartitionBytes=16 KiB.
  - Three filtered counts took 2.89 s over 400 files versus 0.46 s over one file. This is a single local measurement, not a benchmark.
  - The formatted plan showed `PushedFilters: [IsNotNull(id), EqualTo(id,12345)]`.
- `runs/lesson_code.py`: runs the published lesson snippet exactly (setup prefix: `session(..., delta=True)`). Output: `commitInfo MERGE`, `add part-00000-776305dc-25`, `remove part-00001-c06b0d77-e3`, `remove part-00000-ab29c81e-47`, `{'numTargetFilesRemoved': '2', 'numTargetFilesAdded': '1', 'numTargetRowsUpdated': '2', 'numTargetRowsInserted': '1', 'numTargetRowsCopied': '48'}`.

### Limits

- **S3, GCS, Azure, and DynamoDB LogStore behavior:** documentation-reviewed only (Delta 3.2.1 `delta-storage.md`); all runs used the local file system. The docs' statement that S3 lacks mutual exclusion predates S3 conditional writes; the lesson attributes it to the 3.2.1 docs rather than asserting current S3 behavior.
- **Conflict types other than `ConcurrentAppendException`:** documentation-reviewed only. The races are timing-dependent; each failing pair conflicted on its first attempt here.
- **Checkpoint contents and interval:** the default of 10 is from `DeltaConfig.scala` at v3.2.1 and was observed. Multi-part checkpoints, log compaction, and V2 checkpoints were not exercised.
- **Deletion vector behavior for DELETE and UPDATE:** documentation-reviewed. MERGE with DVs was run. Read-time cost of DVs and `REORG TABLE … APPLY (PURGE)` were not run.
- **OPTIMIZE defaults:** the 1 GiB maxFileSize is from `DeltaSQLConf.scala` at v3.2.1; it was not observed at scale. Optimized writes and auto compaction are documentation-reviewed only.
- **The `count()`-from-statistics behavior** was observed in this runtime only. The config that controls it was not verified, so it is not named.
- **Low shuffle merge, liquid clustering, and other Databricks features** are mentioned only as vendor-specific (low shuffle merge) or not at all.
- **Timing numbers** come from one local run on a shared machine and show direction only.
- **ORC and Hive ACID** is documentation-reviewed (`orc.apache.org/docs/acid.html`); Hive was not run.

## Structured Streaming lesson and senior bank section 8 — 2026-09-15

**Content**

- Added the lesson `structured-streaming` (chapter `STREAMING`): "Structured Streaming: micro-batches, state & exactly-once". It has six sections: the micro-batch loop, triggers, exactly-once, state/watermarks/output modes, changes on the same checkpoint, and `lastProgress`. It also adds the diagram `assets/streaming-microbatch.svg` (offsets log before the batch, commits log after the sink, state store beside the stateful operator), a runnable watermark example, and 19 versioned sources.
- Added six `senior-de` cards for bank section 8, with guide group "Structured Streaming": `stream-microbatch-vs-continuous`, `stream-exactly-once`, `stream-watermarks-late-data`, `stream-output-modes`, `stream-checkpoint-contents`, `stream-trigger-types`.
- Added the section 10 coding card `coding-stream-scd-join`.
- Added four authored cards: `stream-dedup-within-watermark`, `stream-foreachbatch-idempotence`, `stream-state-growth-rocksdb`, `stream-lastprogress-falling-behind`.
- Corrections to the supplied draft answers:
  - *Micro-batch vs continuous.* The draft contrasts "~100 ms–seconds with full Catalyst" against "~1 ms but limited operations" and omits the guarantee. Continuous processing is experimental in 3.5.7 and **at-least-once**. It supports only map-like operations, the Kafka and rate sources, and the Kafka, memory and console sinks, and it does not retry failed tasks. Both engines go through Catalyst; continuous mode rejects unsupported operators. The latencies are the guide's best-case figures.
  - *Exactly-once.* The draft says offsets and state are "committed together". They are not one atomic commit. `offsets/N` is written before the batch runs, state versions are written by tasks, the sink writes, and `commits/N` is written last. Exactly-once comes from re-running an uncommitted batch over the same offsets into a sink that tolerates the replay. The Kafka and foreach sinks are at-least-once; `foreachBatch` depends on the user's code.
  - *Watermarks.* The draft says "data later than the watermark is dropped". The guarantee is one-directional: data within the delay is never dropped, and older data may or may not be. The watermark is computed at the end of a batch (max event time minus delay) and used by the next batch; with multiple inputs it is the minimum by default. For windowed aggregations the late-row test uses the **window end**, not the row timestamp. State is evicted only in append or update mode.
  - *Output modes.* The draft gives definitions only. Added which queries allow which modes: append on an aggregation needs a watermark; complete needs an aggregation; stream-stream joins are append-only. Append output is delayed until the watermark passes the window end.
  - *Checkpoint directory.* The draft lists offsets, commits and state. Added `metadata` (the stable query id) and `sources/` (for example the file source's seen-files log), plus the settings pinned in `offsets/N`: shuffle partitions, state store provider, and watermark policy. Also added that Spark's state schema check compares field count, types, and nullability compatibility, not names (`StateSchemaCompatibilityChecker`), so some incompatible changes are **not** detected.
  - *Triggers.* The draft pairs `once` and `availableNow` as the same thing. `once` is deprecated in the 3.5.7 guide. `availableNow` may run several batches honoring source limits, processes uncommitted batches first, and advances the watermark with a final no-data batch. Continuous is experimental.
  - *Stream–static join (coding prompt).* The static side is re-planned per micro-batch, but whether it sees updates depends on the static DataFrame (see runtime evidence). Stream-static output reflects the dimension at processing time, not event time.

**Runtime evidence** (local PySpark 3.5.7, `local[2]`, JDK 17, Delta Lake 3.2.1 where noted; scripts and logs in the local run folder)

- `r01_checkpoint_restart.py`: JSON file source into a Parquet sink with `availableNow`.
  - The checkpoint after two runs held `metadata`, `offsets/0`, `offsets/1`, `commits/0`, `commits/1`, `sources/0/0`, `sources/0/1`.
  - `offsets/1` held `{"batchWatermarkMs":0,"batchTimestampMs":…,"conf":{…"spark.sql.streaming.stateStore.providerClass":"…HDFSBackedStateStoreProvider",…"spark.sql.streaming.multipleWatermarkPolicy":"min",…"spark.sql.shuffle.partitions":"2"}}` followed by `{"logOffset":1}`. `commits/1` held `{"nextBatchWatermarkMs":0}`. `sources/0/1` recorded `b.json` with `"batchId":1`.
  - A restart with no new files produced progress `(2, 0)` and the sink stayed at 3 rows. A restart with one new file produced `(2, 1)` and 4 rows total.
  - `lastProgress.durationMs` keys: `addBatch, commitOffsets, getBatch, latestOffset, queryPlanning, triggerExecution, walCommit`. The source `latestOffset` was `null`. `id` equaled the id in `metadata`.
- `r02_watermark.py update|append`: 10-minute watermark, 5-minute windows, output captured per batch with `foreachBatch`.
  - Update mode:
    - batch 0 `[('12:00','12:05',2), ('12:05','12:10',1)]`, then no-data batch 1 at watermark 11:57;
    - batch 2 `[('12:00','12:05',3), ('12:20','12:25',1)]` (late 12:03 counted), then no-data batch 3 at watermark 12:10;
    - batch 4 (12:04, 12:09, 12:11) output `[('12:10','12:15',1)]` with `numRowsDroppedByWatermark=2`.
  - Append mode:
    - `12:00` (count 3) and `12:05` windows emitted only in no-data batch 3 (watermark 12:10);
    - `12:10` and `12:20` windows emitted in no-data batch 6 (watermark 12:30).
  - A first attempt that called `orderBy` inside `foreachBatch` reported doubled state metrics (`numRowsTotal=4` for two windows, dropped 4). Sorting in Python gave the correct 2 and 2. A range sort adds a sampling job that executes the batch plan twice.
- `r11_window_end_rule.py`: watermark 12:12. A late 12:11:30 row was **counted** (window 12:10 became 2, since the window ends 12:15); a 12:09 row was dropped (`dropped 1`). This matches the `GetStructField(window, 1)` (window end) `LessThanOrEqual` predicate in `statefulOperators.scala`.
- `r03_output_modes.py`: output-mode legality and update vs complete output.
  - Append on `groupBy("city").count()`: `AnalysisException: Append output mode not supported when there are streaming aggregations on streaming DataFrames/DataSets without watermark`.
  - Complete without aggregation: `AnalysisException: Complete output mode not supported when there are no streaming aggregations on streaming DataFrames/Datasets`.
  - Update emitted `[Delhi 1, Pune 1]`, `[Pune 2]`, `[Mumbai 1]`. Complete emitted `[Delhi 1, Pune 1]`, `[Delhi 1, Pune 2]`, `[Delhi 1, Mumbai 1, Pune 2]`.
- `r04_foreachbatch.py [persist]` (Delta): `foreachBatch` wrote each batch to Parquet (plain append) and to Delta (`txnAppId`/`txnVersion=batchId`), then raised after writing batch 1.
  - After the crash: `commits` = `['0']`, `offsets` = `['0','1']`. The restart re-ran batch 1.
  - Parquet rows `[(1,0),(2,0),(3,1),(3,1)]` (duplicate); Delta rows `[(1,0),(2,0),(3,1)]`.
  - Without `persist`, batch 0 (2 rows) reported `numInputRows` 6 and the replayed batch 1 reported 2. With `persist`, they were 2 and 1.
- `r10_lesson_snippets.py`: the lesson `code` and the section code block, run verbatim with a stated setup prefix (session, an orders file stream, paths).
  - The lesson code printed batch 0 `[('12:00', 2), ('12:05', 1)]`, batch 2 `[('12:00', 3), ('12:20', 1)]`, and batch 4 `[]` with dropped 1.
  - The `foreachBatch` block wrote 2 rows. After deleting `commits/0` (and its `.crc`) it replayed batch 0: still 2 rows, Delta versions `[0]`. Deleting only `commits/0` made the restart fail with "Multiple streaming queries are concurrently using …/commits", because the leftover checksum file blocked the rewrite.
- `r05c_stream_static_isolated.py <variant>` (Delta; one Spark application per variant; a separate Spark application updated the dimension between micro-batches):
  - `delta` (uncached `spark.read.format("delta").load`): batch 1 `[(12,1,'Platinum'), (13,3,'Bronze')]`, the new version.
  - `delta_cached`: batch 1 `[(12,1,'Silver'), (13,3,None)]`, stale. The plan showed `InMemoryTableScan`, and a fresh batch read of the same path in that session also returned the cached old rows.
  - `parquet` (uncached directory read, updater appended a file): batch 1 stale; a fresh batch read saw the new file.
  - `parquet_cached`: stale.
  - Earlier confounded runs (`r05_stream_static.py`, `r05b_…`) are kept for the record. In `r05`, same-session Delta writes refreshed the cached Delta DataFrame. Overwriting a Parquet directory under an uncached static read failed with `SparkFileNotFoundException … It is possible the underlying files have been updated`.
- `r09_stream_stream_join.py`: watermarked stream-stream inner join with a one-hour time-range condition. Order 11 at 12:35 matched both the Silver (12:00) and Platinum (12:30) tier rows. State operator `symmetricHashJoin`. Update mode raised `AnalysisException: Join between two streaming DataFrames/Datasets is not supported in Update output mode, only in Append output mode`.
- `r06_change_keys.py`: stateful query changes restarted on the same checkpoint.
  - Adding a filter before the same aggregation worked.
  - Swapping `groupBy("city")` for `groupBy("country")` restarted **without error** and output `[('Delhi', 2), ('IN', 1)]`: the old city state was reused.
  - `groupBy("city","country")` failed with `StateSchemaNotCompatible … Provided key schema: StructType(StructField(city,StringType,true),StructField(country,StringType,true)) - Existing key schema: StructType(StructField(city,StringType,true))`.
  - `count()` changed to `sum("amount")` failed with `StateSchemaNotCompatible … Provided value schema: StructType(StructField(sum,LongType,true)) - Existing value schema: StructType(StructField(count,LongType,false))`.
- `r07_continuous.py`: continuous trigger and deprecated `once`.
  - Rate source (`rowsPerSecond=5`, `numPartitions=1`) filter into a memory sink under `trigger(continuous="1 second")` ran for ~8 s: 19 rows. `lastProgress` was `None` and `recentProgress` empty. The checkpoint held `commits`, `metadata`, `offsets` (epochs 0–9).
  - An aggregation failed with `AnalysisException: Continuous processing does not support Aggregate operations.`; a file source failed with `… does not support StreamingRelation operations.`
  - `trigger(once=True)` printed no Python warning.
- `r08_dedup_rocksdb.py`: `RocksDBStateStoreProvider`, events `a@12:00, b@12:01 | a@12:03, c@12:30 | a@12:31`.
  - `dropDuplicatesWithinWatermark(["guid"])` (10-minute delay) emitted `[a,b]`, `[c]`, `[a]`. At watermark 12:20 it removed 2 state rows (`numRowsRemoved=2`, operator `dedupeWithinWatermark`).
  - Plain `dropDuplicates(["guid"])` emitted `[a,b]`, `[c]`, `[]`, and `numRowsTotal` stayed at 3 with nothing removed.
  - `state/0/<partition>/` held `N.zip`, `SSTs/*.sst`, and `_metadata/schema`. `customMetrics` exposed `rocksdb*` counters.

**Limits**

- Kafka source and sink behavior (offsets per partition, no offset commits to Kafka, `failOnDataLoss`, at-least-once writes) is documentation-reviewed only; no broker was run.
- `mapGroupsWithState` and `flatMapGroupsWithState` output-mode rules, asynchronous progress tracking, and multiple-watermark policy behavior are documentation-reviewed only.
- Continuous-mode at-least-once semantics under failure, and the "no automatic task retry" caveat, were not exercised; only successful runs and analysis-time rejections were observed.
- The stream-static results cover Delta Lake 3.2.1 path reads and local-filesystem Parquet directories. Catalog tables, other Delta versions, and managed runtimes may resolve static snapshots differently. The Delta documentation page (`docs.delta.io/delta-streaming/`) is unversioned; the `txnAppId`/`txnVersion` behavior it describes was checked against the 3.2.1 runtime.
- The latency figures (~100 ms micro-batch, ~1 ms continuous) are quoted from the guide, not measured.
- Batch numbers in examples include engine-scheduled no-data batches; treat them as observed on this runtime rather than guaranteed.

## Count the jobs, stages, and tasks — 2026-09-15

### Content

- Added the practice lesson `count-spark-work` ("Count the jobs, stages, and tasks"). It has five sections: baseline, setup, input tasks, read-time jobs, and a counting method. It links eight exercises and eight exercise-linked question cards.
- Exercises: `count-csv-read-write`, `count-parquet-filter-sql`, `count-repartition-groupby`, `count-join-show`, `count-cache-reuse`, `count-rdd-groupbykey`, `count-rdd-map-filter`, `count-json-agg-write`.
- Question cards: `practice-count-csv-read-write`, `practice-count-parquet-filter-sql`, `practice-count-repartition-groupby`, `practice-count-join-show`, `practice-count-cache-reuse`, `practice-count-rdd-groupbykey`, `practice-count-rdd-map-filter`, `practice-count-json-agg-write`. All are `origin: "practice"`.
- Provenance: ten prompts from a supplied, ChatGPT-generated study sheet ("Metrics Based — Spark Jobs, Stages, Tasks"). Questions 1 and 8 are merged, as are questions 2 and 10. S3 paths are replaced with small local files written by the setup. The sheet's answers were not available and were not used. Every answer was derived from Spark 3.5.7 source and docs, then measured.
- Source review corrected these assumptions from the working notes:
  - `executeTake`'s scale-up factor is `max(spark.sql.limit.scaleUpFactor, 2)`, default 4. `spark.sql.limit.initialNumPartitions` (default 1, internal) was added in 3.4.0.
  - CSV inference runs `RDD.aggregate` over the sampled input, which is all rows at `samplingRatio` 1.0. The first-line `take(1)` job runs even without `inferSchema`.
  - JSON inference submits a fold-like `runJob`, not `treeAggregate`.
  - Parquet without `mergeSchema` still reads its single footer through `mergeSchemasInParallel`: a one-task job, not a driver-side read.
  - Under AQE, `TableCacheQueryStageExec` materializes a cache with a no-op `submitJob` over every cached partition, not with a count.
  - The `DataFrame.cache` API page does not say caching is lazy. The lesson rests that on the observed zero jobs instead.
  - The web UI docs mention job groups only in the SQL tab section.

### Runtime evidence

Environment: local PySpark 3.5.7 on JDK 17 (private runtime), Python 3.9.6, macOS, `local[4]` (`sc.defaultParallelism` 4). Defaults were unchanged except where stated: `spark.sql.shuffle.partitions` 200, `spark.sql.files.maxPartitionBytes` 128 MB, `spark.sql.autoBroadcastJoinThreshold` 10 MB.

Each exercise ran in a fresh application (`spark.stop()` then a new session), once with `spark.sql.adaptive.enabled=true` and once with `false`. Jobs were tagged with `setJobGroup`, and counts came from the live Spark UI REST API: `/jobs`, `/stages/<id>`, and `/stages/<id>/<attempt>/taskList`. Raw `/jobs`, `/stages`, and `/sql?details=true&planDescription=true` JSON for every run is in `runs/raw/`.

Measurement scripts and their results:
- `runs/measure.py`, rounds 1 and 2. Runs the published setup, each exercise, and its verify block.
  - The only change to the published code is `BASE` pointing at the workstream data folder.
  - Results are in `runs/summary-run1.json` and `runs/summary-run2.json`, with logs `measure-run1.log` and `measure-run2.log`.
  - Every group had the same stage statuses, task counts, and attempt counts in both rounds, and printed results were identical.
- `runs/check_published.py`. Executes setup, all eight exercise and verify blocks exactly as published (AQE on), then the lesson practice code.
  - Result: all OK. The lesson output is recorded verbatim in `check-published.log`.
- `runs/side_reads.py`, rounds 1 and 2. Measures input partitions and read-time jobs.
  - Results: `side-run1.json` and `side-run2.json`, identical.
- `runs/partition_rows.py`. Counts rows per post-shuffle partition with AQE off and replays `executeTake(21)` on those counts.
  - The replay reproduced the observed round sizes: 1, 4, 20, 75, 8 for the 40-user aggregates; 1, 4, 2 for `repartition(10)`; 1 for the sort-merge join.
- `runs/followups.py`, rounds 1 and 2. Evidence for each follow-up answer.
  - Results: `followups-run1.json` and `followups-run2.json`, identical apart from IDs.

Inputs as written on disk:

| Path | Files | Bytes | Rows |
|---|---|---|---|
| orders_csv | 4 | 23,480 | 2,000 |
| orders_parquet | 4 | 21,575 | 2,000 |
| customers_parquet | 1 | 1,695 | 50 |
| events_parquet | 4 | 15,702 | 2,000 |
| sessions_json | 4 | 59,128 | 2,000 |

Observed counts per exercise and configuration, from REST data identical in two runs. Cells read jobs · stages run · stages skipped · tasks. "Tasks per job" lists each job in brackets: `skip×N` means N skipped stages, and `4+1` means stages of 4 and 1 tasks. Task attempts equaled tasks in every run.

| Exercise | Action (job group) | AQE on: jobs · stages run · skipped · tasks | AQE on: tasks per job | AQE off: jobs · stages run · skipped · tasks | AQE off: tasks per job |
|---|---|---|---|---|---|
| count-csv-read-write | csv-read | 2 · 2 · 0 · 5 | [1] [4] | 2 · 2 · 0 · 5 | [1] [4] |
| count-csv-read-write | csv-count | 2 · 2 · 1 · 5 | [4] [skip×1 + 1] | 1 · 2 · 0 · 5 | [4+1] |
| count-csv-read-write | csv-write | 1 · 1 · 0 · 4 | [4] | 1 · 1 · 0 · 4 | [4] |
| count-csv-read-write | **total** | **5 · 5 · 1 · 14** | attempts 14 | **4 · 5 · 0 · 14** | attempts 14 |
| count-parquet-filter-sql | parquet-read | 1 · 1 · 0 · 1 | [1] | 1 · 1 · 0 · 1 | [1] |
| count-parquet-filter-sql | filter-show | 1 · 1 · 0 · 1 | [1] | 1 · 1 · 0 · 1 | [1] |
| count-parquet-filter-sql | sql-show | 2 · 2 · 1 · 5 | [4] [skip×1 + 1] | 5 · 6 · 4 · 112 | [4+1] [skip×1 + 4] [skip×1 + 20] [skip×1 + 75] [skip×1 + 8] |
| count-parquet-filter-sql | **total** | **4 · 4 · 1 · 7** | attempts 7 | **7 · 8 · 4 · 114** | attempts 114 |
| count-repartition-groupby | repartition-read | 1 · 1 · 0 · 1 | [1] | 1 · 1 · 0 · 1 | [1] |
| count-repartition-groupby | repartition-show | 4 · 4 · 3 · 11 | [4] [skip×1 + 1] [skip×1 + 4] [skip×1 + 2] | 3 · 4 · 2 · 11 | [4+1] [skip×1 + 4] [skip×1 + 2] |
| count-repartition-groupby | **total** | **5 · 5 · 3 · 12** | attempts 12 | **4 · 5 · 2 · 12** | attempts 12 |
| count-join-show | join-read | 2 · 2 · 0 · 2 | [1] [1] | 2 · 2 · 0 · 2 | [1] [1] |
| count-join-show | join-broadcast | 2 · 2 · 0 · 2 | [1] [1] | 2 · 2 · 0 · 2 | [1] [1] |
| count-join-show | join-shuffle | 3 · 3 · 2 · 6 | [4] [1] [skip×2 + 1] | 1 · 3 · 0 · 6 | [4+1+1] |
| count-join-show | **total** | **7 · 7 · 2 · 10** | attempts 10 | **5 · 7 · 0 · 10** | attempts 10 |
| count-cache-reuse | cache-read | 1 · 1 · 0 · 1 | [1] | 1 · 1 · 0 · 1 | [1] |
| count-cache-reuse | cache-count | 3 · 3 · 1 · 9 | [4] [4] [skip×1 + 1] | 1 · 2 · 0 · 5 | [4+1] |
| count-cache-reuse | cache-filter-count | 2 · 2 · 1 · 5 | [4] [skip×1 + 1] | 1 · 2 · 0 · 5 | [4+1] |
| count-cache-reuse | **total** | **6 · 6 · 2 · 15** | attempts 15 | **3 · 5 · 0 · 11** | attempts 11 |
| count-rdd-groupbykey | rdd-groupbykey | 1 · 2 · 0 · 6 | [3+3] | 1 · 2 · 0 · 6 | [3+3] |
| count-rdd-groupbykey | **total** | **1 · 2 · 0 · 6** | attempts 6 | **1 · 2 · 0 · 6** | attempts 6 |
| count-rdd-map-filter | rdd-map-filter | 1 · 1 · 0 · 2 | [2] | 1 · 1 · 0 · 2 | [2] |
| count-rdd-map-filter | **total** | **1 · 1 · 0 · 2** | attempts 2 | **1 · 1 · 0 · 2** | attempts 2 |
| count-json-agg-write | json-read | 1 · 1 · 0 · 4 | [4] | 1 · 1 · 0 · 4 | [4] |
| count-json-agg-write | json-show | 2 · 2 · 1 · 5 | [4] [skip×1 + 1] | 5 · 6 · 4 · 112 | [4+1] [skip×1 + 4] [skip×1 + 20] [skip×1 + 75] [skip×1 + 8] |
| count-json-agg-write | json-write | 2 · 2 · 1 · 5 | [4] [skip×1 + 1] | 1 · 2 · 0 · 204 | [4+200] |
| count-json-agg-write | **total** | **5 · 5 · 2 · 14** | attempts 14 | **7 · 9 · 4 · 320** | attempts 320 |

Input partitions by file layout: full CSV scan with a supplied schema, `noop` write.

| Input | maxPartitionBytes | Scan tasks |
|---|---|---|
| 4 small files (23,480 bytes) | 128 MB | 4 |
| 1 small file (23,405 bytes) | 128 MB | 1 |
| 1 file, 78,223,899 bytes | 128 MB | 4 |
| same file | 16m | 5 |
| same file | 2m | 38 |

These match `min(maxPartitionBytes, max(openCostInBytes, (bytes + 4 MB per file) / 4))` and the splitting and packing in `FilePartition.scala`.

Read-time jobs, with no action after the read:

| Reader | Jobs (tasks) |
|---|---|
| CSV header only | 1 (1) |
| CSV no header + inferSchema (sheet question 1) | 2 (1, 4) |
| CSV header + inferSchema (sheet question 8) | 2 (1, 4) |
| CSV, JSON, or Parquet with a supplied schema | 0 |
| JSON inferred | 1 (4) |
| Parquet, 1 file | 1 (1) |
| Parquet, 4 files | 1 (1) |
| Parquet, 4 files, mergeSchema | 1 (4) |

Follow-up measurements. AQE off unless stated; identical in two runs.
- SQL `GROUP BY ... collect()`: 1 job, stages of 4 and 200 tasks.
- The same query with `show(5)`: 3 jobs; stages of 4 + 1, then skip + 3, then skip + 12 (20 tasks).
- `repartition(10, "order_id").groupBy("customer_id")`: two Exchanges. 4 jobs, 6 stages run, 6 skipped, 100 tasks.
- No repartition: 4 jobs, 90 tasks.
- AQE on with `autoBroadcastJoinThreshold=-1` and `spark.sql.adaptive.autoBroadcastJoinThreshold=10MB`:
  - The final plan was `BroadcastHashJoin BuildLeft` over `AQEShuffleRead`.
  - 4 jobs: 4 tasks; 1 task; skip + 1 task; skip + 1 task.
- No cache, two counts: each 1 job of 4 + 1 tasks. The filtered count's scan read 2,000 records and 25,324 bytes of Parquet again.
- `groupByKey(2)`: 1 job, 3 + 2 tasks.
- RDD `take(3)`: 2 jobs of 1 task each; result `[12, 14, 16]`.
- Cached JSON aggregate, AQE off: `show()` ran 5 jobs and 112 tasks. The write ran 1 job with 1 skipped stage and 200 tasks.
- Cached JSON aggregate, AQE on: `show()` ran 7 jobs and 312 tasks, including a 200-task job that built the cache. The write ran 1 job with 1 skipped stage and 200 tasks.

Hypotheses from the earlier session:
- **Held:** with AQE on, each shuffle map stage is submitted as its own job, and the result job lists it as skipped. Seen for count, SQL group-by, the JSON aggregate, and both sides of the shuffle join.
  - New: with AQE on, a not-yet-built cache is also materialized as its own job (`TableCacheQueryStage`).
- **Held:** `show()`/`take` scan partitions in rounds, one job per round.
  - AQE off, 40 keys in 200 partitions: 5 jobs.
  - `repartition(10)`: 3 jobs with AQE off, 4 with AQE on (AQE does not coalesce `REPARTITION_BY_NUM`).
  - Filtered `show()` and broadcast join `show()`: a single job, because the first partition had enough rows.
- **Held:** a CSV read runs a one-task first-line job, plus a full inference job when `inferSchema` is set. Header-only reads run just the first job.
- **Held:** a JSON read without a schema scans for the schema, one job over all input partitions.
- **Held, with a correction:** a Parquet schema read runs a small job even for a single file with `mergeSchema` off, one task. The alternative "single footer read on the driver" failed. `mergeSchema` reads every footer (4 tasks here). A supplied schema starts no job.
- **Held for AQE off:** `count()` is one job with two stages (4 + 1) around an Exchange SinglePartition. With AQE on it is two jobs.
- **Held:** in question 3, `repartition(10, "customer_id")` satisfies the aggregate's clustering, so there is one Exchange and no second shuffle.
- **Held for AQE off:** a shuffle join `show()` is one job with three stages (4, 1, 1). With AQE on it is three jobs with the same six tasks.
- **Held:** broadcast collection is its own one-task job before the `show()` job, under both settings.
- **Held within an action:** skipped stages appear when a shuffle is reused by a later job of the same action.
- **Failed across uncached actions:** `show()` then `write` on the same uncached aggregate reran the map stage, with no skipped stage.
- **Held across cached actions:** with the aggregate cached, the write skipped the map stage.

### Limits

- Local mode only: one JVM, no remote executors, locality, dynamic allocation, speculation, or retries. Task attempts equaled tasks. Retry and speculation behavior is documentation-reviewed only.
- Counts are specific to Spark 3.5.7, classic PySpark, these tiny inputs, and these settings. `show()` round sizes depend on how rows hash into partitions. Other versions differ; for example, `spark.sql.limit.initialNumPartitions` exists only from 3.4.0, and AQE cache stages are recent.
- Spark Connect and managed runtimes were not tested.
- Job names such as `$anonfun$withThreadLocalCaptured$1` for the broadcast collection are observed call-site labels, not documented names.
- Configuration coverage of follow-ups:
  - AQE off only: `collect()`/`show(5)`, `repartition` by another column or none, and the no-cache counts.
  - AQE on only: the runtime-broadcast conversion.
  - Both settings: the cached JSON aggregate.
  - The RDD follow-ups (`groupByKey(2)`, `take(3)`) do not involve AQE.
- Source-reviewed, not measured:
  - The effect of setting `spark.default.parallelism` on `groupByKey` (`rdd.py`).
  - The two-job shape of an uncached Parquet `count()` with AQE on, stated by analogy with the measured CSV count.
- File counts were checked after the AQE-off runs only: 38 part files for the JSON aggregate write, 4 for the CSV-to-Parquet write. With AQE on, the aggregate write ran a single task.
- The published setup writes under `tempfile.gettempdir()`. The measurements substituted a workstream data folder for `BASE`, and nothing else changed.
- The sheet's original answers were not compared, by design.

## PySpark coding-round lesson and questions — 2026-09-15

### Content

- Added the practice lesson "The PySpark coding round: six patterns" (slug `coding-round`, chapter `PRACTICE`). An opening section covers how to work the round: grain, keys, ties, nulls, time zones, a tiny input, expected output, then code and cost. Six problem sections follow: deduplicate to the latest row per key, sessionize with a 30-minute gap, a running 7-day active user count, SCD Type 2 with a Delta MERGE, top N per group, and flattening nested JSON. Each problem section has the statement, an inline input, a PySpark DataFrame solution, the observed output, the cost and shuffle discussion, and the common wrong answer. There is no diagram. The lesson has seven sections, one more than the usual 4–6, because the brief asked for an opening section plus one per problem.
- Added six senior-bank `Coding` cards (`coding-dedup-latest`, `coding-sessionize`, `coding-rolling-active-users`, `coding-scd2-merge`, `coding-top-n-per-group`, `coding-flatten-nested-json`), each pointing to the lesson for the full solution. The guide group "Coding round" indexes the seven bank prompts in bank order; "Join a stream to a slowly changing dimension" links to `coding-stream-scd-join`, owned by the streaming workstream.
- Corrections to the supplied draft bank:
  - "`dropDuplicates` + ordering caveat" is not an alternative to `row_number`. A sort before `dropDuplicates` does not choose the survivor: Spark 3.5.7 rewrites deduplication into a `first()` aggregate (`ReplaceDeduplicateWithAggregate`) that is combined after a shuffle. On a two-executor local cluster with AQE disabled it kept a non-latest row for 29,351 and 19,926 of 40,000 keys, and for none in `local[2]`.
  - "Top N efficiently / `orderBy().limit()` is wrong" is right about semantics, but the cost is not a full global sort: `orderBy().limit(n)` planned as `TakeOrderedAndProject`. The efficient per-group form is a ranking window with a limit filter, which Spark 3.5.7 optimizes with `WindowGroupLimit` before and after the shuffle.
  - "Running 7-day active user count" had no caveat. A distinct count over a window frame fails with `DISTINCT_WINDOW_FUNCTION_UNSUPPORTED`. Summing daily active users is wrong with a rows frame (gaps) and with a range frame (users active on several days).
  - Sessionizing with `lag` and a cumulative sum is batch-only; on a streaming DataFrame it fails with `NON_TIME_WINDOW_NOT_SUPPORTED_IN_STREAMING`, and `session_window` is the streaming form.
  - The SCD Type 2 example in the Delta Lake documentation compares attributes with `<>`, which misses changes to or from null, and it checks `current = true` only in the update condition, not in the match condition. The lesson uses `<=>` and adds `is_current` to the match condition so closed history rows never match.
- Sources: Spark 3.5.7 SQL window reference; PySpark API pages for `Window`, `Window.rangeBetween`, `DataFrame.dropDuplicates`, `max_by`, `session_window`, `explode_outer`, and `inline_outer`; the Structured Streaming guide (session windows); the JSON data source guide; the versioned `Optimizer.scala` (`ReplaceDeduplicateWithAggregate`), `InferWindowGroupLimit.scala`, and `error-classes.json` sources; and the Delta Lake v3.2.1 documentation source `docs/source/delta-update.md` (merge, SCD Type 2, performance tuning). Every URL returned HTTP 200. Docstring claims were matched against the v3.5.7 Python source and the rendered pages. The versioned paths `docs.delta.io/3.2.0/` and `docs.delta.io/3.1.0/` return 404, so Delta is cited through the tagged GitHub documentation source; `docs.delta.io/latest/delta-update.html` carries the same SCD example.

### Runtime evidence

Environment: PySpark 3.5.7, JDK 17, `local[2]`, `spark.sql.session.timeZone=UTC`, `spark.sql.shuffle.partitions=4`, AQE at its default (enabled) unless stated. Delta Lake 3.2.1 for the SCD scripts, loaded from local jars. Every published block is a file in `runs/blocks/`, executed unchanged by `runs/run_block.py`. `runs/build_lesson.py` inserts the block text and the log output into `lesson.json`, so neither was retyped.

- `blocks/a_dedup.py` → the window and struct-max versions printed identical rows: customer 1 `a@new.example`, customer 2 `b@two.example` (tie broken by `ingest_id` 202), customer 3 `c@only.example` with a NULL timestamp.
- `blocks/a2_dropdup_demo.py`: `local[2]` → `keys: 40000 | dropDuplicates kept a non-latest row for: 0`. On `local-cluster[2,1,1024]`, run 1 → `29351` and run 2 → `19926`. Exploratory variants: `explore_dedup.py` (local[2], AQE on and off) gave 0 mismatches. `explore_dedup_cluster.py` (local-cluster) gave 40000 and 19922 with AQE off, and 0 and 0 with AQE on. The plan shows `Sort` → `partial_first` → `Exchange hashpartitioning(key)` → `first`.
- `blocks/b_sessionize.py` → sessions `u1-1` (events 1–3, including the exactly-30-minute gap), `u1-2`, `u2-1`, and `u2-2`. `session_window` returned 10:00–11:20 (3 events), 11:30–12:00, 10:05–10:35, and 12:00–12:30. `explore_windows.py` confirmed that events at 10:00 and 10:30 merged and 11:00:01 opened a new session.
- `blocks/c_active_7d.py` → `[DISTINCT_WINDOW_FUNCTION_UNSUPPORTED] Distinct window functions are not supported: "count(DISTINCT user_id) OVER (ORDER BY d ASC NULLS FIRST ROWS BETWEEN -6 FOLLOWING AND CURRENT ROW)".` Correct `active_7d` for 09-01..09-10: 2,2,2,2,3,3,3,2,2,4. `rows_sum` on 09-09 and 09-10: 5 and 8. `range_sum`: 2 and 5, plus 3 on 09-02. The `collect_set` range version matched on active days. The log contains `WARN WindowExec: No Partition Defined for Window operation! Moving all data to a single partition, this can cause serious performance degradation.`
- `blocks/d_scd2.py` (Delta) → final table: (1, Austin, current), (2, Denver, closed 2026-09-10), (2, Boston, current), (3, Chicago, current). History inserted/updated counts: v1 MERGE 2/0, v2 MERGE 2/1, v3 (replay) 0/0. `check_scd_dupes.py` → `[DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE] Cannot perform Merge as multiple source rows matched and attempted to modify the same…`.
- `blocks/e_topn.py` → east: row_number 1,2,3,4; rank 1,1,3,4; dense_rank 1,1,2,3. The top-2 filter kept ann, bo, ed, and fay; `orderBy().limit(2)` returned `west/ed/95` and `east/ann/90`. The plan has `WindowGroupLimit … Partial` below `Exchange hashpartitioning(region)` and `Final` above it.
- `blocks/f_json.py` → four flattened rows (orders 2 and 3 kept with NULLs), `explode rows: 2 | explode_outer rows: 4`, `inline_outer` rows, and the `customer.*` expansion.
- `check_plans.py` → window dedup: `WindowGroupLimit` Partial and Final around the Exchange. `max(struct)` and `max_by`: `SortAggregate` with a partial aggregate before the Exchange. Lag and sum: one Exchange, one Sort, one Window. Explode plus distinct count: two aggregation Exchanges, on (d, k) and on d. Unpartitioned `collect_set` window: `Exchange SinglePartition`. `orderBy().limit(2)`: `TakeOrderedAndProject`. `explode_outer`: `Generate` with no Exchange. With a tie on the ordering value, `max_by` returned `y`; this is not published as a rule.
- `check_struct_nulls_stream_lag.py` → `max(struct)` picked the row with a real timestamp over the null one, and `min` picked the null one. `lag` on a rate stream raised `NON_TIME_WINDOW_NOT_SUPPORTED_IN_STREAMING`.

### Limits

- The "two-executor" evidence comes from Spark's `local-cluster` master on one machine, not a multi-node cluster. The claim that the winner depends on shuffle read order is inferred from the plan and source, not traced.
- MERGE's internal cost (full target search by default; narrowing with partition predicates) is documentation-reviewed from the Delta Lake 3.2.1 docs source, not measured. The late-batch guard in the SCD section is design advice and was not run.
- `session_window` streaming limitations (Update mode unsupported, extra grouping column) are documentation-reviewed; only the batch semantics and the streaming `lag` error were run.
- The tumbling-window and hourly-`groupBy` wrong answers for sessionization, `approx_count_distinct`, and `arrays_zip` are explained, not run. The `windowGroupLimitThreshold` default is read from `SQLConf.scala` (v3.5.7), where it is an internal setting.
- The JSON block reads from an RDD of strings (`spark.sparkContext.parallelize`), which is classic PySpark; Spark Connect sessions have no `sparkContext`, and would read from a path instead.

## Pipeline design lesson and senior design questions — 2026-09-15

**Content**

- Added lesson `pipeline-design` (chapter `DESIGN`), "Designing data pipelines: the senior round", with six sections: a repeatable answer shape (requirements and SLAs, data contract, write path, read path, failure and recovery, observability, trade-offs, plus what Spark does and does not enforce for access control); idempotent writes (dynamic partition overwrite, Delta `replaceWhere`, Delta `txnAppId`/`txnVersion`, MERGE from a deterministic source); CDC ordering, tombstones, and schema drift; data quality (constraints, quarantine, write-audit-publish, metrics); recovery (time travel, RESTORE, VACUUM, replay from raw); and incident stories in STAR form. Cross-page links: `delta-lake.html`, `structured-streaming.html`, `spark-ui.html`, `joins-skew.html` (page only). No diagram.
- Added seven `senior-de` Design questions from bank section 11: `design-cdc-mongodb`, `design-slow-nightly`, `design-freshness-5min`, `design-dq-loud`, `design-multitenant-acl`, `design-backfill`, `design-corrupt-bronze`.
- Added three `senior-de` Design cards for section 12: `story-skew-fix`, `story-cost-runtime`, `story-correctness-bug`. Each gives the structure, the numbers to gather, and the probes to expect, and tells the reader to fill in a real incident of their own. No personal anecdotes were invented.
- Added two guide groups: "Design and scenario" (seven items, bank order) and "Prep: incident stories" (three items).
- Corrections and omissions relative to the supplied bank:
  - Section 11 has no "core of a good answer" column; all answers were derived from the Spark 3.5.7 and Delta Lake 3.2.1 docs and the runs below.
  - "Your RBAC work is directly usable here" (section 11) is a personal reference and was omitted.
  - Section 12's claim about how one named employer's interview loop is weighted is unverifiable and names an employer; it was not published. Only the generic advice (STAR stories with numbers) was kept.
  - Multi-tenant access control: the prompt implies a Spark design. Spark 3.5.7 provides authentication, encryption, and Web UI ACLs (none on by default) but no table-, row-, or column-level data permissions. Those come from catalogs or platforms (Unity Catalog, Apache Ranger, AWS Lake Formation), which are labeled as outside Spark.
  - MongoDB CDC: capture from MongoDB's change stream is a connector concern outside Spark; the answer covers only the Spark/Delta apply side.
  - Bank section 7 says VACUUM "breaks time travel beyond" retention. The run refines this: after VACUUM, `RESTORE` and `collect()` on the old version fail, but `count()` on the old version still succeeded because Delta answered it from log statistics. A count is not proof that a version is readable.
  - Delta docs say a write is ignored when `txnVersion` is "less than" the last recorded value; the run showed an *equal* version is ignored too. That is consistent with the docs' requirement that the next version be higher. A date-derived `txnVersion` silently skips older-date backfills.
  - Senior skew story: AQE skew-join handling in Spark 3.5.7 applies to sort-merge joins and shuffled hash joins (the tuning guide names sort-merge join; `OptimizeSkewedJoin.scala` at v3.5.7 matches both `SortMergeJoinExec` and `ShuffledHashJoinExec`), not to skewed aggregations. Coordinator correction during review.
- Delta Lake doc citations use `https://github.com/delta-io/delta/blob/v3.2.1/docs/source/*.md` because `https://docs.delta.io/3.2.1/...` returned 404. The v3.2.1 Markdown sources were read directly, and each quoted claim was found there (also cross-checked against `docs.delta.io/latest`).

**Runtime evidence** (local PySpark 3.5.7, `local[2]`, JDK 17, Delta Lake 3.2.1, `spark.sql.shuffle.partitions=4`; scripts and logs in the local run folder)

- `overwrite_modes.py` → `overwrite_modes.log`:
  - Session default: `partitionOverwriteMode default: STATIC`.
  - Parquet, three days, then overwrite with two rows for 2026-09-02: `parquet static overwrite -> [(datetime.date(2026, 9, 2), 2)]`; `parquet dynamic overwrite -> [(datetime.date(2026, 9, 1), 2), (datetime.date(2026, 9, 2), 2), (datetime.date(2026, 9, 3), 1)]`; rerun with the same input gave the same result.
  - Delta with writer option `partitionOverwriteMode=dynamic`: `delta dynamic overwrite -> [('2026-09-01', 2), ('2026-09-02', 2), ('2026-09-03', 1)]`.
  - Delta `replaceWhere day = '2026-09-02'`: `[('2026-09-01', 2), ('2026-09-02', 2), ('2026-09-03', 1)]`; with a 2026-09-03 row: `AnalysisException [DELTA_REPLACE_WHERE_MISMATCH] Written data does not conform to partial table overwrite condition or constraint 'day = '2026-09-02''.`; table unchanged afterwards.
  - Delta `txnAppId=orders-loader`: `attempt 1 with txnVersion=7 -> rows: 3`, `attempt 2 with txnVersion=7 -> rows: 3`, `older txnVersion=6 -> rows: 3`, `new txnVersion=8 -> rows: 5`; `history: [(0, 'WRITE'), (1, 'WRITE'), (2, 'WRITE')]` (skipped writes created no commit).
- `quality_restore.py` → `quality_restore.log`:
  - CHECK constraint: `DeltaInvariantViolationException: [DELTA_VIOLATE_CONSTRAINT_WITH_VALUES] CHECK constraint amount_non_negative (amount >= 0) violated by row with values: - amount : -1.0`; `rows after rejected batch: 2` (the two valid rows in the batch were not committed).
  - NOT NULL: `DeltaInvariantViolationException: [DELTA_NOT_NULL_CONSTRAINT_VIOLATED] NOT NULL constraint violated for column: order_id.`
  - Adding a constraint that an existing row violates: `AnalysisException | [DELTA_NEW_CHECK_CONSTRAINT_VIOLATION] 1 rows in delta.`…`orders` violate the new CHECK constraint (amount < 6)`.
  - Quarantine split: `orders rows: 4 quarantine rows: [Row(order_id=4, amount=-1.0, reason='amount_non_negative')]`.
  - Schema drift: appending an extra column without `mergeSchema` raised `AnalysisException | [_LEGACY_ERROR_TEMP_DELTA_0007] A schema mismatch detected when writing to the Delta table (Table ID: …). To enable schema migration using DataFrameWriter or DataStreamWriter, please set: '.option("mergeS…` (truncated by the script); with `mergeSchema`: `[Row(id=1, name='a', email=None), Row(id=2, name='b', email='x@y')]`; int→string with `mergeSchema`: `AnalysisException | [DELTA_FAILED_TO_MERGE_FIELDS] Failed to merge fields 'id' and 'id'`.
  - RESTORE: `after bad overwrite rows: [Row(id=9, amount=-1.0)]`; `restore metrics: {'table_size_after_restore': 2133, 'num_of_files_after_restore': 3, 'num_removed_files': 1, 'num_restored_files': 3, 'removed_files_size': 711, 'restored_files_size': 2133}`; `after restore rows: [1, 2, 3]`; `history: [(0, 'WRITE'), (1, 'WRITE'), (2, 'WRITE'), (3, 'RESTORE')]`.
  - VACUUM: `RETAIN 0 HOURS` with the safety check on raised `IllegalArgumentException | requirement failed: Are you sure you would like to vacuum files with such a low retention period?…`; after disabling `spark.databricks.delta.retentionDurationCheck.enabled`, VACUUM printed `Deleted 7 files and directories in a total of 1 directories.` and `RESTORE … TO VERSION AS OF 1` raised `IllegalArgumentException | Not all files from version 1 are available in file system. Missed files (top 100 files): …`. In this script, `count()` on version 1 still printed `3`; see the recheck below.
- `cdc_merge.py` → `cdc_merge.log`:
  - MERGE with two source rows for one key: `UnsupportedOperationException | [DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE] Cannot perform Merge as multiple source rows matched and attempted to modify the same target row…`.
  - Arrival-order `dropDuplicates` + unguarded MERGE + hard deletes: `after batch1: [(1, 30, 'shipped', False), (3, 15, 'new', False)]` (`dropDuplicates` happened to keep seq 30 here; it is not guaranteed); `after late batch2 (unguarded): [(1, 22, 'paid-late', False), (2, 12, 'resurrected', False), (3, 15, 'new', False)]`.
  - Latest-per-key `row_number` + `s.seq > t.seq` guard + soft deletes: `after batch1: [(1, 30, 'shipped', False), (2, 25, 'new', True), (3, 15, 'new', False)]`; `after late batch2 (guarded):` identical; `replay batch1 again (guarded):` identical; `current view (not deleted): [1, 3]`.
- `published_blocks.py` → `published_blocks.log` (exit 0): executes the published files `block_replacewhere.py` (section code block) and `lesson_code.py` (lesson `code`) verbatim via `exec`, with the setup prefix stated in the lesson (Delta table `orders_by_day` partitioned by `day` with counts 2/1/1).
  - Section block, first run and retry, both printed the table `2026-09-01 | 2`, `2026-09-02 | 2`, `2026-09-03 | 1`.
  - Lesson code printed `| 1| 30|shipped| false|`, `| 2| 25| new| true|`, `| 3| 15| new| false|` (the lesson `output` field has the full table).
  - Date-derived txnVersion: `rows after backfill of 2026-09-01 with txnVersion=20260901: [('2026-09-03', 1)]`, `history: [(0, 'WRITE')]`.
  - VACUUM recheck: `v0 before vacuum collect: [1, 2]`; after a zero-hour VACUUM `v0 count after vacuum: 2`, but `v0 collect after vacuum raised: … SparkFileNotFoundException: File file:/…/silver_vacuum/part-00001-….snappy.parquet does not exist`.
- `build_drafts.py` generates the three JSON files from the verified text. It checks answer word counts, source anchors, ID uniqueness against `existing-questions.txt`, Python syntax of the code, that the escaped code block round-trips to the executed file, and that plain-text fields contain no markup.

**Sources checked** (all resolved on 2026-09-15)

- Spark 3.5.7: `configuration.html` (exact `spark.sql.sources.partitionOverwriteMode` text: default STATIC, dynamic behavior, writer option precedence, Hive serde tables always dynamic); `security.html` ("Security features like authentication are not enabled by default"; UI ACLs; `spark.acls.enable` default false; no data-level permissions described); `structured-streaming-programming-guide.html` (micro-batch latencies as low as 100 ms with exactly-once; continuous processing experimental, ~1 ms, at-least-once; default trigger; AvailableNow; foreachBatch sink guarantee "depends on the implementation"); `web-ui.html`; `sql-performance-tuning.html` (skew join "dynamically handles skew in sort-merge join").
- Delta Lake v3.2.1 docs source: `delta-batch.md` (replaceWhere validation and `spark.databricks.delta.replaceWhere.constraintCheck.enabled`; "Delta Lake 2.0 and above supports dynamic partition overwrite" (the source uses a product-name placeholder); conflict with replaceWhere; recommendation to use replaceWhere; `txnAppId`/`txnVersion` rules and the same-options-different-data warning; data retention: 30-day log, 7-day deleted-file defaults; mergeSchema/autoMerge); `delta-update.md` (multiple-source-row failure and preprocessing advice; CDC latest-change-per-key example; idempotent merge inside foreachBatch; autoMerge required for MERGE schema evolution); `delta-constraints.md` (InvariantViolationException; ADD CONSTRAINT verifies existing rows); `delta-utility.md` (7-day VACUUM default; retention check; RESTORE creates a commit and fails when files were vacuumed; `spark.sql.files.ignoreMissingFiles` for partial restore); `delta-streaming.md` (txnAppId/txnVersion in foreachBatch; new appId after replacing the checkpoint); `PROTOCOL.md` (transaction identifiers: appId, version, lastUpdated).

**Limits**

- Not run locally, documentation-reviewed only: Structured Streaming triggers and end-to-end latency (no streaming query was run for this lesson), foreachBatch with txnAppId, MERGE schema evolution with `autoMerge`, and `spark.sql.files.ignoreMissingFiles` partial restore.
- Vendor or project products outside Spark, labeled and not verified: MongoDB change streams and CDC connectors, Kafka as a landing layer, Unity Catalog, Apache Ranger, AWS Lake Formation, row filters and column masks.
- Design reasoning not tied to one API (write-audit-publish as a pattern, quarantine tables, alerting on ratios, the debugging order for a slowed job, storage-credential bypass of SQL-layer grants, incident-story structure) is presented as practice guidance, not as a documented Spark behavior.
- The `count()`-after-VACUUM observation reflects Delta Lake 3.2.1 answering counts from log statistics on this local run; other versions or configurations may differ.
- The 500 GB/day ≈ under 6 MB/s figure is simple arithmetic on the daily average (500×10^9 bytes / 86,400 s ≈ 5.8 MB/s); real peaks must be measured.

## Gap sweep: common Spark interview topics — 2026-09-15

Baseline: Apache Spark 3.5.7 (PySpark 3.5.7 pip package, JDK 17, local mode, `local[1]` or `local[2]`). No Delta Lake. All scripts and logs are in the local run folder. Reference URLs were checked for HTTP 200 with curl, and `#anchor` IDs were confirmed in the fetched HTML. Page claims were checked with WebFetch or by text extraction. Some API reference pages render their content client-side; for those, the wording was checked against the docstrings in the installed 3.5.7 package, which is the same release.

### Content

Sixteen authored practice cards (`origin: practice`, no `collection`, `source`: "Authored practice question; not a reported interview question."), each mapped to an existing lesson slug:

- Broadcast variables vs broadcast joins: `gap-broadcast-variable-vs-join`, `gap-broadcast-lifecycle` (architecture).
- Unit-testing PySpark: `gap-pyspark-unit-test`, `gap-assert-dataframe-equal` (dataframes).
- Managed vs external tables and the default catalog: `gap-managed-external-table`, `gap-local-catalog-tables` (storage-formats).
- Malformed records: `gap-malformed-read-modes`, `gap-corrupt-record-queries` (dataframes).
- Serialization: `gap-kryo-vs-java` (executor-memory), `gap-pyspark-pickling` (partitions-shuffles).
- Configuration: `gap-config-precedence`, `gap-static-runtime-config` (architecture).
- Output layout: `gap-range-sort-partitionby`, `gap-files-per-partition-dir` (partitions-shuffles).
- Extra, absent high-frequency topics:
  - `gap-temp-global-views` (dataframes). "Temp view vs global temp view vs table" is a staple interview question, and no existing card covers view scope or lifetime.
  - `gap-mappartitions-connections` (architecture). "Opening a database connection per row vs per partition" is a staple scenario; existing cards cover map/flatMap and closures only indirectly. It also reuses the pickling evidence.
  - A third extra was considered and skipped. Candidates were `explain` modes, storage levels, window ties, and dynamic allocation (already present); schema-inference jobs (job-counting workstream); and nested JSON and dedup (coding-round workstream). Nothing else high-frequency was clearly absent.

Corrections and qualifications made explicit in the cards (these are corrections to common claims and to documentation wording, not to the senior bank, which these cards do not use):

- `pyspark.sql.functions.broadcast` is a plan hint that returns a DataFrame. It is not a `Broadcast` variable, and you never call `.value` on it.
- A large PySpark closure is not simply "shipped with every task". PySpark 3.5.7 moves a pickled command above 1 MiB (`PythonUtils.getBroadcastThreshold`) into an internal broadcast, so no task-size warning appears. You still cannot reuse or release that copy.
- `assertDataFrameEqual` is less strict than its name suggests. It ignores nullability, compares data types by `typeName()` only (decimal precision and map key/value types are not checked), and skips the schema check entirely when `expected` is a list of Rows.
- The load/save guide says `saveAsTable` "will create a default local Hive metastore (using Derby)". That describes a Hive-enabled session. A plain `SparkSession.builder` session uses the `in-memory` catalog, so tables vanish between runs while their managed files remain. The `pyspark` shell, by contrast, defaults to Hive when the Hive classes are present.
- `badRecordsPath` is a Databricks option, not an Apache Spark 3.5.7 JSON/CSV option.
- The CSV guide says "A record with less/more tokens than schema is not a corrupted record to CSV". In this 3.5.7 run, when all columns were requested, short and long rows populated `_corrupt_record` in PERMISSIVE mode and were dropped by DROPMALFORMED. This is kept out of the published answers as an observation only (see Limits).
- "Kryo speeds up shuffles" does not hold for DataFrame shuffles, which use `UnsafeRowSerializer`. `spark.serializer` still matters for serialized DataFrame cache blocks: in PySpark, `StorageLevel.MEMORY_ONLY` is a serialized level.
- `spark.conf.set` on a core key such as `spark.executor.memory` raises an error (since 3.0). A misspelled SQL key is accepted silently.

Follow-up answers (for the coordinator's check; not published):

- broadcast-variable-vs-join: run `explain()` and look for `BroadcastExchange` with `BroadcastHashJoin` (or `BroadcastNestedLoopJoin`). With AQE, check the final plan after an action or in the SQL tab.
- broadcast-lifecycle: PySpark already converts the pickled command above 1 MiB into a broadcast, so the serialized task stays small.
- pyspark-unit-test: JVM and SparkContext startup dominate test time. Leaked state includes temp views, `spark.conf` changes, cached tables, and registered UDFs, so reset them in teardown or use unique names.
- assert-dataframe-equal: compare `df.schema` with an expected `StructType` using `==` (which includes nullability), or assert `field.nullable` directly.
- managed-external-table: external datasource tables with a `path` do not gather partition metadata by default, so `MSCK REPAIR TABLE` syncs it. The load/save guide states this.
- local-catalog-tables: `metastore_db` in the current directory, with the warehouse at `spark.sql.warehouse.dir` (default `spark-warehouse` in the current directory). The Hive tables guide states this.
- malformed-read-modes: PERMISSIVE nulls only the fields that fail to parse. Observed: `(2, None, '{"id": 2, "amount": "oops"}')`.
- corrupt-record-queries: store the raw text, source file (`input_file_name()` or the `_metadata` column), load timestamp, schema version, and parse mode, all taken from a persisted parse.
- kryo-vs-java: DataFrame shuffles use `UnsafeRowSerializer`, but serialized in-memory cache stores `DefaultCachedBatch` objects through `spark.serializer`, and that class was not registered.
- pyspark-pickling: the RDD guide says Python stored objects are always pickled, so a serialized level makes no difference.
- config-precedence: the Spark UI Environment tab (or the History Server) for the running application.
- static-runtime-config: check `spark.conf.isModifiable`, validate keys against a known list in config-loading code, or read the value back and assert on it.
- range-sort-partitionby: range boundaries come from sampling, controlled by `spark.sql.execution.rangeExchange.sampleSizePerPartition`.
- files-per-partition-dir: repartition by `day` plus a bounded salt or bucket expression, or keep `repartition("day")` and set `maxRecordsPerFile` so one task splits a large day into several files.
- temp-global-views: a global temp view in `global_temp`. It dies with the application, and any session can replace it.
- mappartitions-connections: `coalesce` (or `repartition`) to the desired count right before the side-effecting stage, a client-side pool or semaphore per executor, or fewer executor cores.

### Runtime evidence

Environment: PySpark 3.5.7 venv (Python 3.9, NumPy 2.0.2, pandas 2.3.3, PyArrow 21.0.0), JDK 17, `local[1-2]`, `spark.driver.memory=1g`.

- `broadcast_vars.py`:
  - `type: Broadcast len(value) on driver: 50000`; the map via `bv.value` returned `['name-0', …, 'name-7']`.
  - After `unpersist()`, reuse returned `['name-0', 'name-1']`.
  - After `destroy()`: `SparkException: [INTERNAL_ERROR_BROADCAST] Attempted to use Broadcast(0) after it was destroyed`.
  - With `autoBroadcastJoinThreshold=-1` plus `F.broadcast(dim)`: `BroadcastHashJoin [k#2L], [k#7L], Inner, BuildRight` over `BroadcastExchange HashedRelationBroadcastMode(...)`, and `join rows: 100000`.
- `broadcast_closure.py`: `pickled closure bytes: 9874662`, `PythonUtils broadcast threshold: 1048576`, `result: [2000000, 2000001, 2000002, 2000003]`. The log has no "very large size" task warning.
- `testing_import_numpy2.log`: `AttributeError: np.NaN was removed in the NumPy 2.0 release`, raised from `pyspark.testing` → `pandasutils` → `pyspark.pandas.strings` (line 1332, `na: Any = np.NaN`). `testing_utils.py` and `test_transform_example.py` add a one-line `np.NaN = np.nan` shim for this environment only.
- `testing_utils.py`:
  - Row order: reordered rows `PASS` by default; with `checkRowOrder=True`, `[DIFFERENT_ROWS] ( 100.00000 % )`.
  - Accepted: list of Rows as expected `PASS`; float within rtol `PASS`.
  - Type and count mismatches: int vs bigint `[DIFFERENT_SCHEMA]`; duplicate counts differ `[DIFFERENT_ROWS] ( 33.33333 % )`.
  - `assertSchemaEqual`: nullable vs not null `PASS`; decimal(10,2) vs decimal(38,0) `PASS`; swapped column order `[DIFFERENT_SCHEMA]`; map<string,int> vs map<string,string> `PASS`.
  - DataFrames with decimal(10,2) vs decimal(38,0) and the same values: `PASS`.
- `test_transform_example.py`: the fixture-shaped `test_add_total` passed with reordered expected rows (`test_add_total PASS`).
- `tables.py`:
  - `catalogImplementation: in-memory`. `DESCRIBE TABLE EXTENDED` Type was `MANAGED` for `orders_managed` and `EXTERNAL` for `orders_external`.
  - Before drop, each of the three locations held 2 Parquet files.
  - After drop: `managed dir exists False`, `external files 2`. Re-registering the external path returned `5 rows; type EXTERNAL`.
  - New application: `new session tables: []`, `survivor files on disk: 2`. Recreating the table failed with `[LOCATION_ALREADY_EXISTS] Cannot name the managed table as spark_catalog.default.survivor, as its associated location ... already exists`.
- `shell_catalog.log` (`pyspark` shell, `-i` with a probe script): `SHELL catalogImplementation= hive`.
- `corrupt.py`, JSON (4 lines: good, type error, syntax error, good):
  - PERMISSIVE with `_corrupt_record`: `[(1, 10.5, None), (2, None, '{"id": 2, "amount": "oops"}'), (None, None, '{"id": 3, "amount": 7.0'), (4, 1.25, None)]`.
  - PERMISSIVE without the column: `[(1, 10.5), (2, None), (None, None), (4, 1.25)]`.
  - DROPMALFORMED: collect `[(1, 10.5), (4, 1.25)]`, `count() -> 3`.
  - FAILFAST: reading returned a `DataFrame`; collect failed with `[MALFORMED_RECORD_IN_PARSING.WITHOUT_SUGGESTION] ... Parse Mode: FAILFAST`.
  - A custom `columnNameOfCorruptRecord` of `bad` gave the same capture.
  - An INT corrupt column raised `AnalysisException: The field for corrupt records must be string type and nullable.`
  - Filtering or selecting only `_corrupt_record` raised `AnalysisException: Since Spark 2.3, the queries from raw JSON/CSV files are disallowed when the referenced columns only include the internal corrupt record column`.
  - `id` plus `_corrupt_record` returned `[(None, '{"id": 3, "amount": 7.0')]`; the same filter on the cached DataFrame returned `2`.
  - With an inferred schema, the columns were `['_corrupt_record', 'amount', 'id']`.
- `corrupt.py`, CSV (`1,10.5` / `2,oops` / `3` / `4,1.25,extra` / `5,2.0`):
  - PERMISSIVE: `[(1, 10.5, None), (2, None, '2,oops'), (3, None, '3'), (4, 1.25, '4,1.25,extra'), (5, 2.0, None)]`.
  - DROPMALFORMED: collect `[(1, 10.5), (5, 2.0)]`, `count() -> 5`, select id only `[(1,), (2,), (3,), (4,), (5,)]`.
- `serialization.py`:
  - With `spark.serializer=KryoSerializer` and `spark.kryo.registrationRequired=true`: DataFrame groupBy `[(0, 334), (1, 333), (2, 333)]` and join `500` succeeded.
  - PySpark `reduceByKey` returned the same totals, and `sc.serializer` was `AutoBatchedSerializer(CloudPickleSerializer())`.
  - A closure capturing `threading.Lock` raised `PicklingError: Could not serialize object: TypeError: cannot pickle '_thread.lock' object`.
  - Its second session inherited Kryo because PySpark's builder options persist within one Python process, so the default was re-checked in a fresh process.
- `serialization_default.py` (fresh process): `spark.serializer ... <unset>`; `JVM SparkEnv serializer class: org.apache.spark.serializer.JavaSerializer`.
- `serialization2.py`: the sort-merge join (broadcast disabled) and the broadcast hash join both returned `100000` under Kryo with required registration. Its persist tests were invalid (identical plans reused one cache: `Asked to cache already cached data`) and were redone.
- `serialization3.py` (distinct plans):
  - `MEMORY_AND_DISK_DESER` returned `(1001, 'Disk Memory Deserialized 1x Replicated')`.
  - `MEMORY_ONLY` (`deserialized=False`) and `DISK_ONLY` both raised `Class is not registered: org.apache.spark.sql.execution.columnar.DefaultCachedBatch`.
  - Direct Kryo serialization of `java.util.ArrayList` and `java.util.Date` raised `Class is not registered`, confirming that the registration requirement was active.
- `configs.py`:
  - `isModifiable`: shuffle.partitions `True`, spark.sql.extensions `False`, spark.executor.memory `False`.
  - Setting shuffle.partitions to 8 gave `8`.
  - Setting `spark.sql.extensions` raised `AnalysisException: Cannot modify the value of a static config: spark.sql.extensions.`; `spark.sql.warehouse.dir` raised the same error.
  - `spark.executor.memory` through `spark.conf.set` and through `SET` both raised `[CANNOT_MODIFY_CONFIG] Cannot modify the value of the Spark config: "spark.executor.memory"`.
  - The custom key `spark.myapp.flag` was accepted (`on`).
  - `getOrCreate()` logged `WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.`, returned the same session object, applied `shuffle.partitions 16`, and left `SparkContext executor.memory <unset>`.
- `config_typo.py`: `typo key accepted: 3 | real key still: 200`.
- `precedence_app.py` via `spark-submit`, with `SPARK_CONF_DIR` whose `spark-defaults.conf` sets 11:
  - `defaults` → `shuffle.partitions= 11 myapp.where= defaults`.
  - Adding `--conf ...=22` → `22 ... submit`.
  - Adding builder `.config(...33)` → `33 ... code`.
- `layout.py` (AQE off, 1,000 ids in 4 partitions, 3 days):
  - `repartitionByRange(3, id)`: `[(0, 0, 330, 331), (1, 331, 668, 338), (2, 669, 999, 331)]`, while hash `repartition(3, id)` spread ids 0–999 across every partition.
  - File counts per day directory: `partitionBy` only → 4; `repartition(day)` + `partitionBy` → 1; `repartitionByRange(2, day)` + `sortWithinPartitions` + `partitionBy` → 1; `maxRecordsPerFile=50` → 8.
  - The file schema inside a day directory was `['id']`.
  - This script's first explain calls were on `id`, which `Range` already orders, so the optimizer removed the sort. They were redone on a hashed column.
- `layout_plans.py`:
  - `sortWithinPartitions(v)` → `*(1) Sort [v#2 ASC NULLS FIRST], false, 0` with no Exchange.
  - `orderBy(v)` → `Sort ... true` over `Exchange rangepartitioning(v#2 ASC NULLS FIRST, 4), ENSURE_REQUIREMENTS`.
  - `repartitionByRange(3, v).sortWithinPartitions(v)` → `Sort ... false` over `Exchange rangepartitioning(..., 3), REPARTITION_BY_NUM`.
  - Its last line (`rdd.getNumPartitions` with AQE on) is not used as evidence.
- `views.py`:
  - Same-session temp view returned `5`. From `spark.newSession()`, the temp view and the unqualified global view raised `[TABLE_OR_VIEW_NOT_FOUND]`, while `global_temp.orders_g` returned `3`.
  - `listTables` showed `('orders_v', True, 'TEMPORARY')`; `sparkContext shared -> True`.
  - `CREATE VIEW perm_v` over the temp view raised `[INVALID_TEMP_OBJ_REFERENCE]`.
  - The `rand()` re-execution check printed `False` because the seed is fixed in the plan. It is not used as evidence.
- `views_plan.py`: the temp view over a table counted `5` before and `6` after `INSERT INTO t_src`, and its plan is a `FileScan parquet spark_catalog.default.t_src`.
- `mappartitions.py`: `map: client constructions = 1000`; `mapPartitions: client constructions = 4`; the captured driver socket raised `PicklingError: ... cannot pickle 'socket' object`; `DataFrame.foreachPartition calls: 3 partitions: 3`.
- `mappartitions_lazy.py`: lazy generator returned after close → `RuntimeError("client already closed")`; generator with `try/finally` → `[0, 10, 20, …, 90]`.

Source lines checked at v3.5.7 (raw GitHub and the installed package):

- `python/pyspark/rdd.py:5253-5255`: broadcast of pickled commands above the threshold; `:3897-3898`: `PairwiseRDD` / `PythonPartitioner` in `partitionBy`.
- `python/pyspark/testing/utils.py:350, 586, 611`, plus the signature defaults `checkRowOrder=False, rtol=1e-5, atol=1e-8`.
- `python/pyspark/sql/session.py:1133-1135`: the shell uses Hive by default.
- `ShuffleExchangeExec.scala`: `new UnsafeRowSerializer(child.output.size, longMetric("dataSize"))`.
- `BroadcastExchangeExec.scala:140, 173`: `child.executeCollectIterator()` collects the build side on the driver, then `sparkContext.broadcastInternal(relation, serializedOnly = true)` broadcasts it.

### Limits

- The CSV short/long-row behavior contradicts the CSV options page wording. It was observed once, with a user schema that includes `_corrupt_record` (PERMISSIVE) and without it (DROPMALFORMED). It is not published as a rule; recheck before adding it to a lesson.
- The JSON `count()` versus `collect()` difference under DROPMALFORMED (3 versus 2) is observed behavior. The docs only describe column pruning for CSV, so the JSON number is presented as an observation.
- PySpark's internal closure broadcast is source-reviewed (`rdd.py`); the run showed only that no task-size warning appeared and the job succeeded. Executor-side memory use of broadcast copies was not measured.
- Kryo evidence is local mode only. On a cluster, broadcast and shuffle fetches cross the network, but the serializer choice for DataFrame shuffles is fixed in `ShuffleExchangeExec` (source-reviewed).
- The `in-memory` versus Hive catalog finding covers a pip-installed PySpark with Hive jars. Managed platforms (Databricks, EMR, Dataproc, Glue) configure their own catalogs; that is documentation-reviewed only and not claimed.
- `badRecordsPath` was not run. It is mentioned only as a Databricks option absent from the Apache 3.5.7 JSON and CSV option tables.
- The `pyspark.testing` import failure is specific to NumPy 2.x with PySpark 3.5.7 in this environment. No supported-NumPy range is claimed.
- The precedence test ran `spark-submit` in local mode; cluster-manager-specific resource flags were not exercised.
- `RuntimeConfig.isModifiable` has no standalone 3.5.7 API page (404), so it is cited through runtime evidence only.

## Checks (integrated site)

- `npm run build` and `npm run check`: 24 pages, 1,537 local links/assets, 20 lesson schemas and examples, 53 Python code blocks parsed, 145 questions, 11 exercises; JavaScript syntax pass; `git diff --check` clean.
- `python3 scripts/browser_test.py`: 84 checks pass, including every lesson diagram loading, runtime notes on observed lessons, observed counts on every counting exercise, the Scenario, Concept, Coding, and Design filters, title-first search for the groupBy exercise, and no horizontal overflow at 320, 390, 768, and 1280 CSS pixels with every disclosure open.
- The first integrated runs found overflow from long configuration keys and error names in plain-text answers, pitfalls, and headings, and a five-button filter row at 320 px; wrapping rules fixed them. They also found that the search index carried code-block type syntax (`STRUCT<...>`), now excluded from lesson search text.
- axe-core 4.13.0 on the homepage, questions page, and the eight new or changed lessons: zero violations at 1280 and 390 CSS pixels with disclosures open. Diagrams, grouped navigation, observed-count blocks, the senior guide, and phone-width filters and outputs were inspected in screenshots.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.

## Publication check (complete senior-bank coverage)

- Implementation commit `212ebb7` pushed to `origin/main`; local and remote commit IDs matched.
- [GitHub Pages deployment 34937919819](https://github.com/anchitgupt/learn-spark/actions/runs/34937919819) completed successfully (build and deploy jobs).
- All 40 public build files returned HTTP 200 and matched the local build byte for byte on the first pass after deployment.
- Live pages include https://anchitgupt.github.io/learn-spark/structured-streaming.html, https://anchitgupt.github.io/learn-spark/count-spark-work.html, and https://anchitgupt.github.io/learn-spark/questions.html

# Q&A sheet — 2026-09-15

## Content and implementation

- Added `qa.html`, a Q&A sheet generated from `content/questions.json`: all 145 questions in lesson order, each with its answer and follow-up visible at rest (exercise-linked cards also show the follow-up answer), its type and provenance badges, a "Ran on PySpark 3.5.7" badge where the card or exercise records a local run, and a link to its card for sources and review notes. Each lesson section links to the lesson.
- `assets/qa.js` adds search, type filters, a quiz mode that hides answers until revealed, "Only run on Spark", and browser-local "Can answer" marks with per-lesson counts in the sidebar and a "Hide answered" filter. Marks use their own storage key (`spark-fieldnotes-qa-v1`), so the notebook's storage, export, and import format are unchanged. Without JavaScript the sheet stays fully readable and the controls are hidden.
- The sidebar links the sheet under "Put it into practice"; the questions page intro links to it. The page reuses the lesson layout, with a lessons sidebar on desktop and a "Jump to a lesson" list at phone width.

## Checks

- `npm run build` and `npm run check`: 25 pages, 1,799 local links/assets, 20 lesson schemas and examples, 53 Python blocks, 145 questions, 11 exercises; the checker now requires every question on the sheet; JavaScript syntax pass (including `assets/qa.js`, also added to the Pages workflow); `git diff --check` clean.
- `python3 scripts/browser_test.py`: 93 checks pass, adding the sheet's question and section counts, the Design filter, search hiding empty lessons, quiz mode and single-answer reveal, a "Can answer" mark persisting across reload with the lesson count, "Hide answered", and no-JavaScript reading, plus the overflow sweep at 320, 390, 768, and 1280 CSS pixels.
- The first browser run found the three study toggles squeezed onto the filter row and overflowing under the lessons sidebar, which intercepted clicks; the control groups now stack as full-width rows.
- axe-core 4.13.0 on `qa.html` (normal and quiz mode) and `questions.html`: zero violations at 1280 and 390 CSS pixels. Desktop and phone screenshots were inspected; they showed lesson labels inheriting the article paragraph size, fixed with a more specific rule.

Publication status is recorded by the GitHub Actions deployment run; live assets are checked against the generated build after deployment.
