"""
UNICEF Vocational Training — TPM Monitoring Dashboard (Streamlit)
Embeds the self-contained HTML dashboard (Aug 3 2026 data baked in).
Deploy: push this folder to GitHub → share on Streamlit Community Cloud,
with 'streamlit_app.py' as the main file.
"""
from pathlib import Path
import base64
import streamlit as st
import streamlit.components.v1 as components

# ---- page setup ----
st.set_page_config(
    page_title="UNICEF VT — TPM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Height of the embedded dashboard (px). The page is long; increase if the
# bottom (FGD / findings) gets cut off, decrease to trim empty space.
DASHBOARD_HEIGHT = 9800

# ---- strip default Streamlit chrome for a full-bleed dashboard ----
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {background: #eef2f7;}
      [data-testid="stHeader"] {height: 0;}
      div.stApp {background: #eef2f7;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- load and render the dashboard ----
html_path = Path(__file__).parent / "dashboard.html"
html = html_path.read_text(encoding="utf-8")
logo_path = Path(__file__).parent / "assets" / "ppc-logo.png"
logo_data = base64.b64encode(logo_path.read_bytes()).decode("ascii")
html = html.replace("{{PPC_LOGO_DATA_URI}}", f"data:image/png;base64,{logo_data}")
components.html(html, height=DASHBOARD_HEIGHT, scrolling=True)
