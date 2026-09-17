# UNICEF VT — TPM Monitoring Dashboard (Streamlit)

Interactive third-party-monitoring dashboard for the ADB-funded Vocational Training
project in Afghanistan. Data extract: **3 August 2026** (baked in).

Covers Centre Readiness, Midline Satisfaction, Classroom Observation, Pre/Post-test
knowledge, coverage & demographics, and qualitative FGD findings — with KPI cards,
an indicator scorecard vs targets, filters (region / province / IP / gender) and
tool-level key findings.

## Files
| File | Purpose |
|------|---------|
| `streamlit_app.py` | Streamlit entry point — embeds the dashboard |
| `dashboard.html` | Self-contained dashboard (charts + data baked in) |
| `requirements.txt` | Python dependencies (`streamlit`) |
| `.streamlit/config.toml` | Theme + server settings |

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Then open http://localhost:8501

## Deploy on Streamlit Community Cloud (free)
1. Create a **public or private GitHub repo** and push the *contents of this folder*
   to the repo root (so `streamlit_app.py` sits at the top level).
2. Go to https://share.streamlit.io → **New app** → sign in with GitHub.
3. Select the repo/branch, set **Main file path** = `streamlit_app.py`, click **Deploy**.
4. First build takes ~1–2 minutes. You'll get a shareable `*.streamlit.app` URL.

> Note: the charts load Chart.js from a CDN, so the deployment host needs internet
> (Streamlit Cloud does). For a fully offline build, ask for a version with Chart.js
> inlined.

## Updating the data
This build has the 3 Aug 2026 figures baked into `dashboard.html`. To refresh with a
new round, replace `dashboard.html` with the regenerated file and redeploy (or ask for
a live-data version that reads the Kobo exports at runtime).

## Adjusting layout
If the bottom of the page is cut off or there's extra whitespace, change
`DASHBOARD_HEIGHT` near the top of `streamlit_app.py`.
