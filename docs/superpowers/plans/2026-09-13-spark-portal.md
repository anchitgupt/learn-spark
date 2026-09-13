# Spark Fieldnotes implementation plan

Goal: Build an accessible Spark fundamentals wiki and interview notebook for Anchit, ready for GitHub Pages.
Architecture: Python standard-library static generation from reviewed JSON lesson content; progressive JavaScript for search, local notes, progress, and a conceptual canvas lab. Relative links work under a project subpath. No server account or API key.
Design: Editorial field notebook, warm paper, ink typography, rust accents, numbered curriculum, sticky desktop navigation, narrow lesson measure, and a mobile topic drawer.

- [x] Author eight fundamentals lessons with explicit Spark 3.5.7 scope, original examples, interview prompts, and official source links. Put lesson data in content/lessons.json and reviewed practice prompts in content/questions.json. User-authored answers are drafts pending review.
- [x] Implement scripts/build.py, assets/styles.css, assets/app.js, and assets/lab.js. Generate _site/index.html, eight lesson pages, questions.html, lab.html, and notebook.html. All lessons and reviewed questions remain readable without JavaScript.
- [x] Add an accessible SVG architecture diagram and a canvas shuffle lab with step controls, pause, reduced-motion support, and equivalent explanatory text. Create a short local explainer video with a transcript.
- [x] Implement search, reading progress, notebook add/edit/delete, versioned JSON export/import with validation and deduplication. Treat user text as text, never HTML. Report persistence failure explicitly.
- [x] Add README editing/verification/deployment instructions and a GitHub Actions Pages workflow publishing only _site. No existing git repository or remote is present; prepare deployment without claiming publication.
- [x] Build, validate all local links and lesson metadata, syntax-check JavaScript, test desktop/mobile browser flows and JavaScript-disabled reading, and inspect screenshots. Preserve any unrelated files.
