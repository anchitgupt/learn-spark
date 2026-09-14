# Predict what Spark will do — implementation plan

Goal: Implement the approved predict, reveal, verify, and explain-back learning format for filter/count, groupBy/write, and join/aggregate, then publish it.

Design: Append a tenth lesson to the established learning path. Use native HTML disclosures with readable task-flow diagrams. Keep exercise records in `content/predictions.json`, rendering in `scripts/predictions.py`, and shared setup/source metadata in the lesson. No additional browser state or JavaScript is needed. Existing lesson IDs and notebook storage remain compatible.

The baseline is classic PySpark 3.5.7 with a separate SQL session, four Range partitions, four configured shuffle partitions, AQE disabled, and no cache/retries. Task counts are source-reviewed predictions, not runtime observations. The write exercise uses a fresh scratch destination and error-if-exists mode. Cluster users must choose shared storage.

- [x] Review versioned official APIs, count/aggregation source, UI evidence, and join assumptions.
- [x] Author three exercises with code, prediction prompts, answer disclosures, conceptual flows, evidence steps, spoken answers, and follow-ups.
- [x] Integrate lesson navigation, homepage/capstone/lab links, search anchors, notebook topic, and authored question provenance.
- [x] Extend content validation to exercise references, IDs, sources, and all new Python snippets. Check small-input arithmetic independently.
- [x] Check disclosures with mouse/keyboard and JavaScript disabled; search; old progress/notes; mobile navigation; all pages at phone and desktop widths. Inspect screenshots.
- [x] Record local verification, commit and push, then confirm GitHub Pages success and live asset equality.

Validation commands: `npm run build`, `npm run check`, `git diff --check`. Browser checks run through Playwright CLI against a local HTTP preview; screenshots and one-off scripts stay in ignored `output/playwright/`. No successful Spark execution will be claimed without running the examples on Spark 3.5.7.
