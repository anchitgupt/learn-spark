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
