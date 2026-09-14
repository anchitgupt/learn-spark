# Full Spark execution flow

Goal: Turn Anchit's reported interview question and supplied draft answer into a verified, reusable learning walkthrough, then publish it to the existing GitHub Pages site.

Design: Preserve the reading-first Fieldnotes layout. Add a capstone lesson after the eight fundamentals, with six navigable phases and a full static reading fallback. Teach startup separately from query execution. Retain an explicit classic PySpark / Spark 3.5.7 scope. Add a reported question and clearly distinguish authored follow-ups. Keep existing notes and completion IDs compatible.

- [x] Verify startup, planning, scheduling, task sizing, exchanges, AQE, failure, and output claims against versioned official docs and source.
- [x] Author the complete flow lesson, original small example, interview answer, source-linked corrections, and practice follow-ups.
- [x] Add a six-phase interactive walkthrough and a diagram distinguishing resource allocation, task dispatch, and data movement.
- [x] Derive topic/question/progress counts from content; link the walkthrough from the homepage, related lessons, question bank, and lab. Preserve current storage schema and slugs.
- [x] Check generated pages and links, browser step controls, phone reading, no-JS fallback, search, question provenance, and old notebook data. Record verification limits.
- [ ] Commit, push, wait for Pages, and verify live files match the local build.
