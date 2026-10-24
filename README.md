# BeatBloom

BeatBloom is an accessible browser-based rhythm practice prototype for children, families, educators, and rehabilitation settings. It offers real-time early/late/together feedback, adjustable tempo and session length, gentle visuals, keyboard/touch input, and local-only progress history.

The current prototype also includes a personal device-offset estimate, a standardized one-minute baseline, timing bias and variability metrics, beginning/middle/end session summaries, stability-aware adaptive tempo, progress charts, and local CSV export. Calibration is an approximate personal correction, not clinical hardware calibration.

The evidence review and product rules are documented in [RESEARCH_NOTES.md](RESEARCH_NOTES.md). All 200 references from the supplied bibliography are indexed in `research_catalog.csv`; the extraction can be reproduced with `python scripts/build_research_catalog.py`.

## Run locally

Open `index.html` directly, or serve the directory with any static web server.

## Publish with GitHub Pages

This repository includes `.github/workflows/deploy-pages.yml`. It publishes the static application whenever a commit is pushed to the `main` branch.

1. Create a new GitHub repository. Use a public repository if you are using GitHub Free.
2. From this project directory, run:

   ```powershell
   git init
   git add .
   git commit -m "Create BeatBloom rhythm practice app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git push -u origin main
   ```

3. On GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Open the **Actions** tab and wait for “Deploy BeatBloom to GitHub Pages” to complete.
6. Return to **Settings → Pages** and select **Visit site**.

For a project repository, the address is normally `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`. A repository named `YOUR-USERNAME.github.io` is published at `https://YOUR-USERNAME.github.io/`.

Do not publish private participant or medical data in this repository. BeatBloom stores practice history only in each visitor's browser and does not upload it to GitHub.

## Important note

BeatBloom is an original educational prototype. It is not affiliated with Interactive Metronome®, is not a medical device, and is not intended to diagnose or treat any condition or replace care from a qualified professional.
