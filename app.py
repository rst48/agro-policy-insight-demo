import streamlit as st
from pathlib import Path

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(page_title="Agro Policy Insight", page_icon="🌾", layout="wide")

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

ARTICLES = [
    {
        "id": "A01",
        "title_id": "Analisis leading indicator sektor pertanian di Indonesia tahun 2004-2022",
        "title_en": "Leading indicator analysis of the agricultural sector in Indonesia in 2004-2022",
        "authors": "I Kadek Mira Merta Ningsih, Erni Tri Astuti",
        "pages": "151–175",
    },
    {
        "id": "A02",
        "title_id": "Menelisik masa depan kakao berkelanjutan: menjembatani kesenjangan kesediaan membayar konsumen di Indonesia",
        "title_en": "Exploring sustainable cocoa futures: bridging the consumer willingness-to-pay gap in Indonesia",
        "authors": "Wednes Aria Yuda, Adi Djoko Guritno, Atris Suyantohadi",
        "pages": "177–194",
    },
    {
        "id": "A03",
        "title_id": "Pengaruh status penguasaan lahan dan adopsi teknologi terhadap produksi padi sawah di provinsi sentra padi di Indonesia",
        "title_en": "The influence of land tenure and technology adoption on lowland rice production in central rice-producing provinces in Indonesia",
        "authors": "Mewa Ariani, Herlina Tarigan, Sri Hastuti Suhartini, Ening Ariningsih, Sumedi, Sheila Savitri, Erma Suryani, Sudi Mardianto, Sunarsih",
        "pages": "195–216",
    },
    {
        "id": "A04",
        "title_id": "Dampak pencabutan subsidi pupuk terhadap kinerja usaha tani dan efisiensi komoditas non-subsidi: studi kasus komoditas kentang dan wortel",
        "title_en": "The impact of fertilizer subsidy removal on farm performance and efficiency of non-subsidized commodities: a case study of potatoes and carrots commodities",
        "authors": "Widyadhari Febriani Setyaningrum, Sumedi, Rangga Ditya Yofa",
        "pages": "217–229",
    },
    {
        "id": "A05",
        "title_id": "Efektivitas kebijakan pemerintah daerah dalam pengembangan kelembagaan agribisnis lokal domba di Kabupaten Sukabumi, Jawa Barat",
        "title_en": "The effectiveness of local government policies in developing local sheep agribusiness institutions in Sukabumi Regency, West Java",
        "authors": "Supardi Rusdiana, Diky Ramdani, Unang Yunasaf, Chalid Talib, Cut Rabiatul Adawiyah, Amam",
        "pages": "231–247",
    },
    {
        "id": "A06",
        "title_id": "Pola dan perilaku konsumsi daging ayam ras rumah tangga peserta Program Keluarga Harapan Kota Pekanbaru, Provinsi Riau",
        "title_en": "Patterns and behavior of broiler chicken meat consumption in households participating in the Program Keluarga Harapan in Pekanbaru City, Riau Province",
        "authors": "Vilandra Oktavia, Djaimi Bakce, Jumatri Yusri",
        "pages": "249–264",
    },
    {
        "id": "A07",
        "title_id": "Factors that play a role in building resilience, autonomy, and sustainability of smallholder coconut farming in Aceh Province",
        "title_en": "Faktor-faktor yang berperan dalam membangun resiliensi, kemandirian, dan keberlanjutan usaha kelapa rakyat di Provinsi Aceh",
        "authors": "Henny Sulistyorini, Sumardjo, Anna Fatchiya, Ninuk Purnaningsih, Destika Cahyana",
        "pages": "265–286",
    },
]

# ============================================================
# THEME (Orange + Dark Turquoise)
# ============================================================
THEME = {
    "primary": "#006D6F",      # dark turquoise
    "primary_2": "#146C7A",    # lighter turquoise for gradient/hover
    "accent": "#F77F00",       # orange
    "border": "rgba(0,0,0,0.08)",
    "text_muted": "rgba(0,0,0,0.62)",
    "banner_grad_1": "#FFE8CC",  # soft orange
    "banner_grad_2": "#D9F2F1",  # soft turquoise
}

banner_path = Path("assets/banner.png")

# ============================================================
# STYLES
# ============================================================
st.markdown(
    f"""
<style>
/* Naikkan layout */
.block-container {{
  max-width: 1200px;
  padding-top: 0rem !important;
  padding-bottom: 2rem;
}}
header[data-testid="stHeader"] {{ height: 0 !important; }}
div[data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stAppViewContainer"] {{ padding-top: 0rem !important; }}

/* Wrapper */
.ojs-wrap {{
  border: none;
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
}}

/* Banner (gambar saja supaya tidak dobel) */
.banner-box {{
  border: none;
  border-radius: 12px 12px 0 0;
  overflow: hidden;
}}
.banner-fallback {{
  height: 220px;
  background: linear-gradient(90deg, {THEME["banner_grad_1"]}, {THEME["banner_grad_2"]});
}}

/* Navbar */
.navbar {{
  background: linear-gradient(90deg, {THEME["primary"]}, {THEME["primary_2"]});
  padding: 10px 14px;
  display:flex; align-items:center; justify-content:space-between;
  gap: 12px; flex-wrap: wrap;
}}
.navlinks {{ display:flex; gap: 14px; flex-wrap: wrap; }}
.navlinks a {{
  color: rgba(255,255,255,0.93);
  text-decoration:none;
  font-size: 0.95rem;
  font-weight: 600;
}}
.navlinks a:hover {{
  text-decoration: underline;
  text-decoration-color: {THEME["accent"]};
}}
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
.h2 {{ font-size: 20px; font-weight: 900; margin: 0 0 10px 0; color: rgba(0,0,0,0.85); }}
.p {{ color: rgba(0,0,0,0.74); line-height: 1.65; font-size: 0.98rem; }}
.hr {{ border-top: 1px solid {THEME["border"]}; margin: 16px 0; }}

/* Article cards */
.article {{
  border: 1px solid {THEME["border"]};
  border-radius: 12px;
  padding: 14px;
  background: #fff;
  box-shadow: 0 10px 22px rgba(0,0,0,0.04);
  margin-bottom: 10px;
}}
.article-title {{
  font-weight: 900;
  font-size: 1.02rem;
  margin: 0 0 6px 0;
  color: {THEME["primary"]};
}}
.article-sub {{
  color: rgba(0,0,0,0.62);
  font-size: 0.95rem;
  margin: 0 0 8px 0;
}}
.article-meta {{
  color: rgba(0,0,0,0.58);
  font-size: 0.9rem;
}}
.tag {{
  display:inline-block;
  border: 1px solid rgba(0,0,0,0.10);
  border-radius: 999px;
  padding: 3px 10px;
  font-size: 0.82rem;
  margin-right: 8px;
  color: rgba(0,0,0,0.65);
}}
.tag-orange {{
  border-color: rgba(247,127,0,0.35);
  color: rgba(247,127,0,0.95);
}}

/* Right Sidebar */
.sidebarbox {{
  border: 1px solid {THEME["border"]};
  border-radius: 12px;
  padding: 14px;
  background: #fff;
  box-shadow: 0 10px 24px rgba(0,0,0,0.04);
}}
.sidebarbox + .sidebarbox {{ margin-top: 12px; }}
.sb-title {{ font-weight: 900; margin-bottom: 10px; color: rgba(0,0,0,0.85); }}
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
/* make PDF dummy button look like outline */
.pdf-btn div.stButton>button {{
  background: white !important;
  color: {THEME["primary"]} !important;
  border: 1px solid rgba(15,76,92,0.35) !important;
}}
.pdf-btn div.stButton>button:hover {{
  border: 1px solid rgba(247,127,0,0.65) !important;
  color: rgba(247,127,0,1) !important;
}}
</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# SHELL
# ============================================================
st.markdown("<div class='ojs-wrap'>", unsafe_allow_html=True)

# Banner (gambar saja)
st.markdown("<div class='banner-box'>", unsafe_allow_html=True)
if banner_path.exists():
    st.image(str(banner_path), use_container_width=True)
else:
    st.markdown("<div class='banner-fallback'></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Navbar
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

main_col, right_col = st.columns([3, 1], gap="large")

with main_col:
    st.markdown("<div class='page'>", unsafe_allow_html=True)

    st.markdown("<div class='h2'>About the Publication</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'>{FULL_DESCRIPTION}</div>", unsafe_allow_html=True)

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.markdown("<div class='h2'>Current Issue</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'><b>{CURRENT_ISSUE['title']}</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='p'><b>Published:</b> {CURRENT_ISSUE['published']}</div>", unsafe_allow_html=True)

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    st.markdown("<div class='h2'>Articles</div>", unsafe_allow_html=True)

    for a in ARTICLES:
        st.markdown(
            f"""
<div class="article">
  <div class="article-title">{a["title_id"]}</div>
  <div class="article-sub">{a["title_en"]}</div>
  <div class="article-meta"><span class="tag tag-orange">Pages {a["pages"]}</span>{a["authors"]}</div>
</div>
""",
            unsafe_allow_html=True
        )
        st.markdown("<div class='pdf-btn'>", unsafe_allow_html=True)
        st.button("PDF (dummy)", key=f"pdf_{a['id']}")
        st.markdown("</div>", unsafe_allow_html=True)

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

