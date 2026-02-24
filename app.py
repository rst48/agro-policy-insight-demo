import streamlit as st
from pathlib import Path
from datetime import date

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(page_title="Agro Policy Insight", page_icon="🌾", layout="wide")
st.markdown("""
<style>
h1, h2, h3 { margin-top: 0 !important; }
.block-container > div:first-child { display:none; }
</style>
""", unsafe_allow_html=True)
# ============================================================
# CONTENT
# ============================================================
FULL_DESCRIPTION = """
Agro Policy Insight merupakan kumpulan policy brief di bidang sosial ekonomi pertanian yang disusun sebagai bahan analisis dan rekomendasi kebijakan dalam mendukung pembangunan pertanian yang inklusif, berdaya saing, dan berkelanjutan. Setiap policy brief mengangkat isu-isu strategis di bidang pertanian khususnya sosial ekonomi pertanian yang dianalisis secara ringkas berbasis data dan temuan lapangan. Melalui penyajian rekomendasi kebijakan yang aplikatif dan berorientasi pada pengambilan keputusan, publikasi ini diharapkan dapat menjadi rujukan bagi para pemangku kepentingan dalam merumuskan kebijakan sosial ekonomi pertanian yang responsif terhadap tantangan aktual dan mampu mendorong transformasi sektor pertanian secara berkelanjutan.
""".strip()

CURRENT_ISSUE = {
    "title": "Vol. 1 No. 1 (2026): Agro Policy Insight",
    "published": "31-01-2026",
}

# ============================================================
# THEME (indigo/navy)
# ============================================================
THEME = {
    "primary": "#1f2a44",      # navbar
    "primary_2": "#2f3f63",
    "accent": "#ff7a00",       # CTA button
    "border": "rgba(0,0,0,0.08)",
    "text_muted": "rgba(0,0,0,0.62)",
    "banner_grad_1": "#e8efff",
    "banner_grad_2": "#d6f5ff",
}

# ============================================================
# ASSETS (optional)
# ============================================================
banner_path = Path("assets/banner.png")
logo_path = Path("assets/logo.png")

# ============================================================
# STYLES (Fix: remove top gap, remove banner border, no extra header)
# ============================================================
st.markdown(
    f"""
<style>
/* 1) Naikkan layout (hilangkan space kosong atas) */
.block-container {{
  max-width: 1200px;
  padding-top: 0rem !important;
  padding-bottom: 2rem;
}}
header[data-testid="stHeader"] {{ height: 0 !important; }}
div[data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stAppViewContainer"] {{ padding-top: 0rem !important; }}

/* 2) Wrapper tanpa border */
.ojs-wrap {{
  border: none;
  border-radius: 10px;
  overflow: hidden;
  background: #fff;
}}

/* 3) Banner lebih modern + tanpa border hitam bawah */
.banner {{
  position: relative;
  height: 120px;
  border-bottom: none;
}}
.banner img {{
  width: 100%;
  height: 120px;
  object-fit: cover;
  display: block;
}}
.banner-fallback {{
  height: 120px;
  background: linear-gradient(90deg, {THEME["banner_grad_1"]}, {THEME["banner_grad_2"]});
}}

/* Overlay */
.banner-overlay {{
  position: absolute; inset: 0;
  display: flex; align-items: center; gap: 14px;
  padding: 14px 22px;
  background: linear-gradient(90deg, rgba(255,255,255,0.90), rgba(255,255,255,0.35));
}}
.brandlogo {{
  width: 58px; height: 58px;
  border-radius: 10px;
  background: rgba(255,255,255,0.92);
  border: 1px solid rgba(0,0,0,0.10);
  display:flex; align-items:center; justify-content:center;
  font-weight: 900; color:{THEME["primary"]};
  letter-spacing: 0.04em;
}}
.brandtitle {{
  margin: 0;
  font-size: 22px;
  letter-spacing: -0.02em;
  color: {THEME["primary"]};
  font-weight: 900;
}}
.brandmeta {{
  margin-top: 4px;
  color: {THEME["text_muted"]};
  font-size: 0.95rem;
}}

/* Navbar */
.navbar {{
  background: {THEME["primary"]};
  padding: 10px 14px;
  display:flex; align-items:center; justify-content:space-between;
  gap: 12px; flex-wrap: wrap;
}}
.navlinks {{ display:flex; gap: 14px; flex-wrap: wrap; }}
.navlinks a {{
  color: rgba(255,255,255,0.93);
  text-decoration:none;
  font-size: 0.95rem;
}}
.navlinks a:hover {{ text-decoration: underline; }}
.navright {{ display:flex; gap: 10px; align-items:center; }}
.navpill {{
  color: rgba(255,255,255,0.92);
  border: 1px solid rgba(255,255,255,0.25);
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 0.88rem;
}}

/* Content */
.page {{ padding: 18px 18px 8px 18px; }}
.h2 {{ font-size: 20px; font-weight: 900; margin: 0 0 10px 0; }}
.p {{ color: rgba(0,0,0,0.74); line-height: 1.65; font-size: 0.98rem; }}
.hr {{ border-top: 1px solid {THEME["border"]}; margin: 16px 0; }}

/* Right Sidebar */
.sidebarbox {{
  border: 1px solid {THEME["border"]};
  border-radius: 12px;
  padding: 14px;
  background: #fff;
  box-shadow: 0 10px 24px rgba(0,0,0,0.04);
}}
.sidebarbox + .sidebarbox {{ margin-top: 12px; }}
.sb-title {{ font-weight: 900; margin-bottom: 10px; }}
.sb-muted {{
  color: {THEME["text_muted"]};
  font-size: 0.92rem;
  line-height: 1.45;
}}

/* Buttons */
div.stButton>button {{
  width: 100%;
  border-radius: 10px;
  padding: 0.6rem 0.85rem;
}}
.primary-btn div.stButton>button {{
  background: {THEME["accent"]} !important;
  color: white !important;
  border: 1px solid rgba(0,0,0,0.10) !important;
}}
</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# OJS-like Shell
# ============================================================
st.markdown("<div class='ojs-wrap'>", unsafe_allow_html=True)

# ---------------- Banner ----------------
st.markdown("<div class='banner'>", unsafe_allow_html=True)
if banner_path.exists():
    st.image(str(banner_path), use_container_width=True)
else:
    st.markdown("<div class='banner-fallback'></div>", unsafe_allow_html=True)

st.markdown("<div class='banner-overlay'>", unsafe_allow_html=True)
if logo_path.exists():
    st.image(str(logo_path), width=58)
else:
    st.markdown("<div class='brandlogo'>API</div>", unsafe_allow_html=True)

st.markdown(
    """
<div>
  <div class="brandtitle">AGRO POLICY INSIGHT</div>
  <div class="brandmeta">Berbasis data, berorientasi solusi, untuk transformasi pertanian berkelanjutan.</div>
</div>
""",
    unsafe_allow_html=True
)
st.markdown("</div></div>", unsafe_allow_html=True)  # end overlay + banner

# ---------------- Navbar ----------------
st.markdown(
    """
<div class="navbar">
  <div class="navlinks">
    <a href="#">Home</a>
    <a href="#">Aims and Scope</a>
    <a href="#">Issues</a>
    <a href="#">Announcements</a>
    <a href="#">Editorial Team</a>
    <a href="#">Reviewer</a>
    <a href="#">Contact Us</a>
  </div>
  <div class="navright">
    <span class="navpill">🔎 Search</span>
    <span class="navpill">Register</span>
    <span class="navpill">Login</span>
  </div>
</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# Main content + right sidebar (no extra title/logo below banner)
# ============================================================
main_col, right_col = st.columns([3, 1], gap="large")

with main_col:
    st.markdown("<div class='page'>", unsafe_allow_html=True)

    st.markdown("<div class='h2'>About the Publication</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'>{FULL_DESCRIPTION}</div>", unsafe_allow_html=True)

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.markdown("<div class='h2'>Current Issue</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'><b>{CURRENT_ISSUE['title']}</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'><b>Published:</b> {CURRENT_ISSUE['published']}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown("<div class='sidebarbox'>", unsafe_allow_html=True)
    st.markdown("<div class='sb-title'>Ready to submit?</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='sb-muted'>Start a new submission or continue a submission in progress (demo).</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='primary-btn'>", unsafe_allow_html=True)
    st.button("Go to Submission", key="submit_btn")
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.button("Author Guidelines", key="guidelines_btn")
    st.button("Article Template", key="template_btn")
    st.button("Publication Ethics", key="ethics_btn")
    st.button("Reference Manager", key="ref_btn")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # end wrapper
st.caption("Demo frontend-only (Streamlit). Semua tombol/tautan masih dummy.")

