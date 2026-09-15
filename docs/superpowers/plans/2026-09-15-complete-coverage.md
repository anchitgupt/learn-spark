# Complete senior-bank coverage — implementation plan

Goal: Cover every section of the supplied senior DE interview bank and the deferred jobs/stages/tasks question sheet, give lesson-less question topics real lessons, close common interview gaps, and publish it.

Design: Keep the reading-first Fieldnotes layout and stable slugs. Group the sidebar by chapter as the path grows past thirteen lessons. New lessons: Catalyst & AQE, PySpark UDFs, Delta Lake, Structured Streaming (fundamentals and lakehouse/streaming chapters), counting Spark work (practice exercises), coding-round patterns (practice), and pipeline design (design). Questions for bank sections 7, 8, 10, 11, and 12 join `collection: "senior-de"` and the senior guide in bank order. Existing Catalyst/AQE and UDF cards move to their new lessons without changing IDs.

Verification: Examples and behavioral claims run on a local PySpark 3.5.7 runtime (JDK 17, delta-spark 3.2.1) installed outside the repository. Lessons and cards record observed runs separately from documentation review. Delta Lake claims cite Delta Lake documentation and protocol, not the Spark baseline. Observed job, stage, and task counts come from the local Spark REST API with the environment stated.

- [x] Install the runtime outside the repo; smoke-test Spark, Delta, streaming, and pandas UDFs.
- [x] Draft lessons, questions, guide groups, diagrams, and verification notes in parallel workstreams; run every published snippet.
- [x] Generalize the generator: lesson diagrams from content, runtime notes for lessons, cards, and exercises, several exercise lessons, chapter-grouped navigation, Coding and Design question filters.
- [x] Extend the checker: Delta sources, runtime metadata, Python syntax for every lesson code block, exercise references across lessons, guide coverage.
- [x] Review every draft against its sources and runtime logs; integrate content, retire the placeholder topic labels, reorder the guide to bank order.
- [x] Build, check, run browser tests at phone and desktop widths, inspect screenshots, update README and verification notes.
- [ ] Commit, push, wait for Pages, and verify live files match the local build.

Validation commands: `npm run build`, `npm run check`, `python3 scripts/browser_test.py`, `git diff --check`.
