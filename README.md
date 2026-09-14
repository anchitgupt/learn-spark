# Spark Fieldnotes

A reading-first Spark fundamentals wiki and interview notebook for Anchit Gupta. Static HTML, CSS, and progressive JavaScript; designed for GitHub Pages under a repository subpath.

## Preview locally

Requires Python 3.9+; Node.js is optional for the npm shortcuts and JavaScript syntax checks. Building and previewing need no npm packages or installation step; the optional browser checks need a one-time Playwright install.

```sh
python3 scripts/build.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory _site
```

Open http://127.0.0.1:4173. Alternatively, `npm run dev` builds and serves the site. Rebuild after changing source content or assets, then refresh. Use an HTTP server: browser storage and search are not guaranteed on `file://` URLs.

### Optional browser checks

Kept out of CI. The script serves the built `_site` itself and exercises the interactive behaviour: progress, disclosures, search, notebook export/import, filters, the walkthrough, the lab, mobile navigation, the no-JavaScript fallback, and responsive overflow.

```sh
python3 -m pip install playwright        # once
python3 -m playwright install chromium   # once, or rely on an installed Chrome
python3 scripts/browser_test.py          # or: npm run test:browser
```

## What's included

- Twelve linked lessons: ten fundamentals, the complete execution-flow capstone, and a prediction practice lesson.
- Original small PySpark examples, expected results, pitfalls, and interview explanations.
- Seventeen interview prompts: one question reported by Anchit and sixteen authored practice prompts, clearly labeled with their provenance.
- Three prediction exercises: filter/count, groupBy/write, and broadcast join/aggregate. Each has native answer reveals, a task-flow diagram, plan/UI checks, a spoken answer, and a follow-up. A separate AQE comparison explores how the baseline can change.
- A six-phase interactive execution walkthrough with a full static reading fallback and a diagram separating resource allocation, task dispatch, and data movement.
- SVG architecture and partition diagrams; a canvas shuffle/filter walkthrough; an original 12-second H.264 explainer with captions and a transcript.
- Search, completion tracking, and a personal interview notebook with add/edit/delete and JSON import/export.
- Readable static lessons and questions when JavaScript is disabled; mobile navigation and keyboard controls.

## Add or change content

Edit `content/lessons.json` for the published curriculum. Each les; for interactive changes, also run `python3 scripts/browser_test.py` (optional, local only)son has a stable `slug`, `title`, `dek`, `minutes` (reading plus practice estimate), `idea`, `sections`, `code`, `output`, `pitfall`, `question`, `answer`, `sources`, `reviewed`, and `version`.

- Section `body` is trusted HTML maintained in the repository. Keep it semantic: paragraphs, lists, inline code, and links. Do not insert unreviewed third-party HTML.
- `code` is a plain-text PySpark snippet; the generator escapes it automatically.
- Add source title/URL pairs, the Spark runtime version, and the actual review date. Do not advance the review date without checking the explanation.
- Overview, sidebar, question, and progress totals are derived from content. Preserve existing slugs so links and saved notes remain valid. Sections may specify stable `id` values; sources may specify `id` values for inline source references.
- Prediction exercises live in `content/predictions.json` and render through `scripts/predictions.py`. The lesson references their stable IDs in `exercises`; each record supplies code, prompts, reasoning, a flow, expected output, verification code/steps, spoken answer, follow-up, and source IDs from the lesson. Search links directly to each exercise. Keep setup and configuration assumptions consistent with the lesson.
- The capstone phase summaries live in `content/execution-phases.json` and render through `scripts/flow.py`. Each phase links to a full lesson section.
- Question `origin` is `reported` only for a user-reported interview question; otherwise use `practice`. Adding authored follow-ups does not make them reported questions.
- `content/questions.json` holds published practice questions. Each question references a lesson slug and has a stable ID, type, question, answer, follow-up, and provenance.
- Run `python3 scripts/build.py` and `npm run check` after changes. `_site/` is generated output, not the authoring source.

For a new interview question, use **My notebook**. Saved questions are browser-local drafts, marked **Needs verification**. Export a JSON backup and provide the question and answer for review. Once reviewed, promote a corrected version into the published JSON with sources. The website itself has no AI verifier or GitHub write access.

## Verification policy

The initial content uses **Apache Spark 3.5.7 as an explicit reference baseline**, not as a claim about the newest release. Each lesson records its review date. The original fundamentals were checked on 2026-09-13; the complete-flow and prediction lessons were checked against official documentation and versioned Apache Spark source on 2026-09-14. Other Spark releases, Spark Connect, and managed distributions can behave differently.

PySpark examples are syntax-checked, with expected results reasoned from their small inputs. They have **not been executed in a Spark runtime** on this machine. Before promoting new code as runtime-verified, run it on the stated version and record the observed result. The lab and video are conceptual models, not a real scheduler or a performance benchmark.

For each new claim:

1. State the runtime and assumptions.
2. Check the official API/guide and link the relevant source.
3. Run a minimal reproduction when the claim depends on execution behavior.
4. Record expected versus observed results and any version caveats.
5. Check that the interview answer preserves those qualifications.

The private ChatGPT conversation URL supplied at project creation was not accessible. Its contents have not been imported or invented.

## Format for interview walkthroughs

Use the complete-flow capstone as the model for future questions: state the scope, give a concise spoken answer, trace the steps with component responsibilities and data location, work one small example, explain the assumptions, and link evidence. Distinguish a logical/physical query plan from scheduler jobs, stages, and task attempts. Include a concrete Spark UI observation when the answer depends on runtime behavior.

Treat pasted AI answers as drafts to verify. Preserve the question's provenance, correct oversimplifications explicitly, and never imply that source review is a successful runtime test.

## Notebook backups and limitations

Notes and completion are stored under `spark-fieldnotes-v1` in localStorage. The JSON export includes a schema version, completed lesson slugs, and notes. It is not uploaded or synced. Other applications on the same GitHub Pages origin can technically access browser storage; this is a personal study notebook, not secure document storage.

- Export before clearing browser data or switching devices.
- Imports validate structure, lengths, IDs, known topics, and http/https reference URLs. Files above 5 MB and notebooks above 1,000 notes are rejected.
- Exact duplicates are skipped. Different content with an existing ID is skipped with a conflict count; the existing note is preserved. Import does not overwrite notes.
- Untrusted notebook text is inserted with `textContent`, never HTML.
- If storage fails, changes remain only in the current page until navigation/reload. Export before leaving.
- If another tab changes the saved notebook, a stale tab refuses to overwrite it and retains its changes in memory for export. Edit in one tab at a time. localStorage is not a transactional multi-user database.
- Personal drafts never receive a verified badge simply because a URL was entered.

## Publish to GitHub Pages

Repository: https://github.com/anchitgupt/learn-spark

GitHub Pages destination: https://anchitgupt.github.io/learn-spark/

The workflow below publishes the site from the default branch. Check the repository's Actions tab for the current deployment status.

To configure or repeat deployment:

1. Commit and push this source tree to its default branch (`main` or `master`).
2. In the repository, open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. Run **Build and deploy Spark Fieldnotes** from the Actions tab, or push a new commit.
4. The workflow builds, validates, and deploys only `_site/`. Pull requests run the build/check job without deployment.
5. Confirm the deployment job succeeds and open its reported URL. For a repository named `learn-spark` under `anchitgupt`, the expected URL is `https://anchitgupt.github.io/learn-spark/`.

All site links and asset paths are relative. No custom domain, API key, database, or SPA fallback is needed. Google Fonts is optional; fallback fonts keep content readable if that network request fails.

## Checks

```sh
npm run build
npm run check
```

`check.py` validates local links, anchors, image alt attributes, one H1 per page, source metadata, unique content IDs, question-topic relationships, search destinations, exercise references and source anchors, and Python example syntax (including every setup/exercise/verification block in the prediction lesson). It does not execute Spark or fetch remote links.

Browser review covers search, filters, disclosure controls, note CRUD and persistence, import/export and malicious-input handling, completion, video playback, the lab, phone navigation, blocked storage, and JavaScript-disabled reading. Screenshots and test exports live in ignored `output/playwright/`.

## Recreate the video

The generated video and poster are included, so normal builds need no video tooling. To recreate them, install Pillow and ffmpeg, then run:

```sh
python3 scripts/create_video.py
python3 scripts/build.py
```

`assets/shuffle.vtt` contains captions. The full text transcript is in the lab page template in `scripts/build.py`.
