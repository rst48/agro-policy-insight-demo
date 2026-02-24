import streamlit as st
from datetime import date

# ============================================================
# CONFIG
# ============================================================
st.set_page_config(
    page_title="Agro Policy Insight",
    page_icon="🌾",
    layout="wide",
)

# ============================================================
# CONTENT (FULL DESCRIPTION FROM USER)
# ============================================================
FULL_DESCRIPTION = """
Agro Policy Insight merupakan kumpulan policy brief di bidang sosial ekonomi pertanian yang disusun sebagai bahan analisis dan rekomendasi kebijakan dalam mendukung pembangunan pertanian yang inklusif, berdaya saing, dan berkelanjutan. Setiap policy brief mengangkat isu-isu strategis di bidang pertanian khususnya sosial ekonomi pertanian yang dianalisis secara ringkas berbasis data dan temuan lapangan. Melalui penyajian rekomendasi kebijakan yang aplikatif dan berorientasi pada pengambilan keputusan, publikasi ini diharapkan dapat menjadi rujukan bagi para pemangku kepentingan dalam merumuskan kebijakan sosial ekonomi pertanian yang responsif terhadap tantangan aktual dan mampu mendorong transformasi sektor pertanian secara berkelanjutan.
""".strip()

# Dummy issues & articles (frontend-only)
ISSUES = [
    {
        "id": "2026-1",
        "title": "Vol. 1 No. 1 (2026)",
        "published": "January 2026",
        "theme": "Inklusivitas & ketahanan pangan",
        "desc": "Edisi pembuka membahas isu harga pangan, akses petani, dan efektivitas intervensi kebijakan.",
        "articles": [
            {
                "id": "API-001",
                "title": "Stabilisasi Harga Pangan: Kombinasi Intervensi yang Tepat Sasaran",
                "authors": "Tim Agro Policy Insight",
                "abstract": "Policy brief ini merangkum opsi kebijakan stabilisasi harga pangan berbasis data, mengkaji trade-off, serta menawarkan rekomendasi operasional untuk pengambilan keputusan cepat.",
                "keywords": ["harga", "stabilisasi", "pangan"],
                "category": "Policy Brief",
            },
            {
                "id": "API-002",
                "title": "Meningkatkan Akses Pembiayaan Petani: Skema yang Lebih Inklusif",
                "authors": "Tim Agro Policy Insight",
                "abstract": "Analisis ringkas atas hambatan pembiayaan di level petani, berbasis temuan lapangan, dan rancangan rekomendasi agar skema pembiayaan lebih inklusif dan berkelanjutan.",
                "keywords": ["pembiayaan", "inklusi", "petani"],
                "category": "Policy Brief",
            },
            {
                "id": "API-003",
                "title": "Produktivitas dan Daya Saing: Paket Kebijakan Berbasis Bukti",
                "authors": "Tim Agro Policy Insight",
                "abstract": "Policy brief ini menyusun paket rekomendasi peningkatan produktivitas dan daya saing melalui prioritisasi program, indikator kinerja, serta mitigasi risiko implementasi.",
                "keywords": ["produktivitas", "daya saing", "evidence-based"],
                "category": "Policy Brief",
            },
        ],
    },
    {
        "id": "2025-2",
        "title": "Vol. 0 No. 2 (2025)",
        "published": "December 2025",
        "theme": "Transformasi sektor pertanian",
        "desc": "Edisi pilot dengan topik transformasi rantai nilai, data & digitalisasi, dan penguatan kelembagaan.",
        "articles": [
            {
                "id": "API-004",
                "title": "Digitalisasi Data Pertanian: Fondasi Kebijakan Responsif",
                "authors": "Tim Agro Policy Insight",
                "abstract": "Merangkum prinsip tata kelola data pertanian dan langkah implementasi yang realistis agar kebijakan lebih responsif terhadap tantangan aktual.",
                "keywords": ["data", "digitalisasi", "tata kelola"],
                "category": "Policy Brief",
            },
            {
                "id": "API-005",
                "title": "Hilirisasi Komoditas: Menjaga Nilai Tambah Tetap Inklusif",
                "authors": "Tim Agro Policy Insight",
                "abstract": "Analisis ringkas tentang hilirisasi yang berkeadilan, fokus pada peran petani, UMKM, dan desain insentif agar manfaat tersebar lebih merata.",
                "keywords": ["hilirisasi", "nilai tambah", "UMKM"],
                "category": "Policy Brief",
            },
        ],
    },
]

PAGES = ["Home", "Current", "Archives", "About", "Contact", "Search"]

# ============================================================
# STYLES (Modern, elegant, OJS-like layout)
# ============================================================
st.markdown(
    """
<style>
/* Layout */
.block-container { padding-top: 1.2rem; padding-bottom: 2.2rem; max-width: 1200px; }
section[data-testid="stSidebar"] { border-right: 1px solid rgba(0,0,0,0.06); }

/* Typography */
h1, h2, h3 { letter-spacing: -0.02em; }
.small-muted { color: rgba(0,0,0,0.56); font-size: 0.92rem; }

/* Top header */
.topbar {
  display:flex; align-items:center; justify-content:space-between;
  padding: 0.9rem 1.0rem; border: 1px solid rgba(0,0,0,0.08);
  border-radius: 16px; background: rgba(255,255,255,0.8);
  backdrop-filter: blur(8px);
}
.brand { display:flex; align-items:center; gap: 12px; }
.brand .title { font-size: 1.15rem; font-weight: 700; margin: 0; }
.brand .tagline { margin-top: 2px; }

.nav {
  display:flex; gap: 14px; flex-wrap: wrap; justify-content:flex-end;
  font-size: 0.95rem;
}
.nav a { text-decoration:none; color: rgba(0,0,0,0.76); }
.nav a:hover { text-decoration: underline; }

.pill {
  display:inline-flex; align-items:center; gap: 6px;
  padding: 6px 10px; border-radius: 999px;
  border: 1px solid rgba(0,0,0,0.10);
  font-size: 0.88rem; color: rgba(0,0,0,0.75);
}

/* Cards */
.card {
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 16px;
  padding: 16px;
  background: #fff;
  box-shadow: 0 10px 24px rgba(0,0,0,0.04);
}
.card + .card { margin-top: 12px; }
.article-title { font-size: 1.05rem; font-weight: 700; margin-bottom: 0.2rem; }
.meta { color: rgba(0,0,0,0.55); font-size: 0.9rem; }
.badge {
  display:inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,0.10);
  font-size: 0.82rem;
  margin-right: 6px;
}
hr.soft { border: none; border-top: 1px solid rgba(0,0,0,0.06); margin: 1rem 0; }

/* Sidebar widgets */
.sidebox {
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 16px;
  padding: 14px;
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(8px);
}
.sidebox h4 { margin: 0 0 10px 0; }
.kv { display:flex; justify-content:space-between; gap: 10px; }
.kv span { color: rgba(0,0,0,0.60); font-size: 0.92rem; }
.kv b { font-weight: 650; }

/* Buttons spacing */
div.stButton>button {
  border-radius: 12px;
  padding: 0.55rem 0.85rem;
}
</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# SIMPLE ROUTING (session state)
# ============================================================
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "selected_issue" not in st.session_state:
    st.session_state.selected_issue = ISSUES[0]["id"]
if "selected_article" not in st.session_state:
    st.session_state.selected_article = None

def goto(page: str):
    st.session_state.page = page
    st.session_state.selected_article = None

def select_issue(issue_id: str):
    st.session_state.selected_issue = issue_id
    st.session_state.selected_article = None

def select_article(article_id: str):
    st.session_state.selected_article = article_id

def get_issue(issue_id: str):
    return next(x for x in ISSUES if x["id"] == issue_id)

def find_article(article_id: str):
    for issue in ISSUES:
        for a in issue["articles"]:
            if a["id"] == article_id:
                return issue, a
    return None, None

# ============================================================
# TOPBAR (OJS-like)
# ============================================================
left_logo, right_nav = st.columns([1.25, 2.75])

with left_logo:
    # Optional local logo if exists
    # If you add assets/logo.png it will show; otherwise fallback emoji
    try:
        st.image("assets/logo.png", width=70)
    except Exception:
        st.markdown("<div class='pill'>🌾 Agro Policy Insight</div>", unsafe_allow_html=True)

with right_nav:
    st.markdown(
        f"""
<div class="topbar">
  <div class="brand">
    <div>
      <div class="title">Agro Policy Insight</div>
      <div class="small-muted tagline">Policy brief sosial ekonomi pertanian berbasis data & temuan lapangan</div>
    </div>
  </div>
  <div style="display:flex; align-items:center; gap:12px;">
    <div class="nav">
      <a href="#">Current</a>
      <a href="#">Archives</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
      <a href="#">Search</a>
    </div>
    <div class="pill">Register</div>
    <div class="pill">Login</div>
  </div>
</div>
""",
        unsafe_allow_html=True
    )

st.write("")  # spacing

# ============================================================
# SIDEBAR NAV (real interaction)
# ============================================================
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", PAGES, index=PAGES.index(st.session_state.page))
if page != st.session_state.page:
    goto(page)

st.sidebar.markdown("---")
st.sidebar.subheader("Issues")
for issue in ISSUES:
    if st.sidebar.button(issue["title"], use_container_width=True, key=f"sb_issue_{issue['id']}"):
        select_issue(issue["id"])
        goto("Current")

st.sidebar.markdown("---")
st.sidebar.subheader("Information")
st.sidebar.caption("Frontend-only demo (tanpa backend).")
st.sidebar.write("• Editorial Team (dummy)")
st.sidebar.write("• Author Guidelines (dummy)")
st.sidebar.write("• Privacy Statement (dummy)")

# ============================================================
# MAIN LAYOUT (content + right sidebar like OJS)
# ============================================================
content_col, side_col = st.columns([3, 1])

with side_col:
    st.markdown("<div class='sidebox'>", unsafe_allow_html=True)
    st.markdown("#### Journal Info")
    st.markdown(
        """
<div class="kv"><span>Type</span><b>Policy Brief</b></div>
<div class="kv"><span>Scope</span><b>Sosial Ekonomi</b></div>
<div class="kv"><span>Format</span><b>Ringkas & Aplikatif</b></div>
<div class="kv"><span>Updated</span><b>""" + date.today().strftime("%d %b %Y") + """</b></div>
""",
        unsafe_allow_html=True
    )
    st.markdown("<hr class='soft'/>", unsafe_allow_html=True)
    st.markdown("#### Quick Links")
    st.write("• Template (dummy)")
    st.write("• Etika Publikasi (dummy)")
    st.write("• Panduan Penulis (dummy)")
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# RENDER PAGES
# ============================================================
with content_col:
    # Article detail overlay (like clicking article title)
    if st.session_state.selected_article:
        issue, a = find_article(st.session_state.selected_article)

        st.markdown(f"## {a['title']}")
        st.markdown(
            f"<div class='meta'><span class='badge'>{a['category']}</span>"
            f"<b>{a['authors']}</b> · {issue['title']} · Published {issue['published']}</div>",
            unsafe_allow_html=True
        )
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        st.markdown("### Abstract")
        st.write(a["abstract"])

        st.markdown("### Keywords")
        st.write(", ".join(a["keywords"]))

        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)
        st.button("← Back to issue", on_click=lambda: st.session_state.update({"selected_article": None}))
        st.stop()

    if st.session_state.page == "Home":
        # Hero
        st.markdown("## Agro Policy Insight")
        st.markdown(
            "<div class='small-muted'>Kumpulan policy brief sosial ekonomi pertanian untuk analisis dan rekomendasi kebijakan.</div>",
            unsafe_allow_html=True
        )
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        st.markdown("### Tentang Publikasi")
        st.write(FULL_DESCRIPTION)

        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        # Highlight current issue (latest by order)
        latest = ISSUES[0]
        st.markdown("### Current Issue")
        st.markdown(
            f"<div class='card'>"
            f"<div class='article-title'>{latest['title']}</div>"
            f"<div class='meta'>Published: {latest['published']} · Theme: {latest['theme']}</div>"
            f"<p style='margin-top:10px;'>{latest['desc']}</p>"
            f"</div>",
            unsafe_allow_html=True
        )

        st.markdown("### Articles")
        for a in latest["articles"]:
            st.markdown(
                f"<div class='card'>"
                f"<div class='article-title'>{a['title']}</div>"
                f"<div class='meta'>{a['authors']} · <span class='badge'>{a['category']}</span></div>"
                f"<p style='margin-top:8px;'>{a['abstract']}</p>"
                f"</div>",
                unsafe_allow_html=True
            )
            st.button("View", key=f"home_view_{a['id']}", on_click=select_article, args=(a["id"],))

    elif st.session_state.page == "Current":
        issue = get_issue(st.session_state.selected_issue)
        st.markdown(f"## {issue['title']}")
        st.markdown(
            f"<div class='meta'>Published: {issue['published']} · Theme: {issue['theme']}</div>",
            unsafe_allow_html=True
        )
        st.write(issue["desc"])
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        st.markdown("### Articles")
        for a in issue["articles"]:
            st.markdown(
                f"<div class='card'>"
                f"<div class='article-title'>{a['title']}</div>"
                f"<div class='meta'>{a['authors']} · <span class='badge'>{a['category']}</span></div>"
                f"<p style='margin-top:8px;'>{a['abstract']}</p>"
                f"</div>",
                unsafe_allow_html=True
            )
            st.button("Read more", key=f"cur_read_{a['id']}", on_click=select_article, args=(a["id"],))

    elif st.session_state.page == "Archives":
        st.markdown("## Archives")
        st.markdown(
            "<div class='small-muted'>Kumpulan edisi (dummy) untuk demo frontend-only.</div>",
            unsafe_allow_html=True
        )
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        for issue in ISSUES:
            st.markdown(
                f"<div class='card'>"
                f"<div class='article-title'>{issue['title']}</div>"
                f"<div class='meta'>Published: {issue['published']} · Theme: {issue['theme']}</div>"
                f"<p style='margin-top:8px;'>{issue['desc']}</p>"
                f"</div>",
                unsafe_allow_html=True
            )
            cols = st.columns([1, 1, 4])
            with cols[0]:
                st.button("Open", key=f"arch_open_{issue['id']}",
                          on_click=lambda x=issue["id"]: (select_issue(x), goto("Current")))
            with cols[1]:
                st.button("Set as current", key=f"arch_set_{issue['id']}",
                          on_click=lambda x=issue["id"]: select_issue(x))

    elif st.session_state.page == "About":
        st.markdown("## About Agro Policy Insight")
        st.markdown(
            "<div class='small-muted'>Publikasi policy brief sosial ekonomi pertanian.</div>",
            unsafe_allow_html=True
        )
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        st.write(FULL_DESCRIPTION)

        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)
        st.markdown("### Focus & Scope")
        st.write(
            "Kumpulan policy brief di bidang sosial ekonomi pertanian yang menganalisis isu strategis secara ringkas berbasis data dan temuan lapangan."
        )

        st.markdown("### Tujuan")
        st.markdown(
            """
- Mendukung pembangunan pertanian yang **inklusif**, **berdaya saing**, dan **berkelanjutan**
- Menyajikan rekomendasi kebijakan yang **aplikatif** dan **berorientasi pada pengambilan keputusan**
- Menjadi rujukan pemangku kepentingan untuk kebijakan sosial ekonomi pertanian yang **responsif terhadap tantangan aktual**
"""
        )

        st.markdown("### Target Pembaca")
        st.markdown(
            """
- Pengambil kebijakan (pusat/daerah)
- Analis kebijakan & peneliti
- Akademisi
- Pelaku usaha/UMKM terkait sektor pertanian
- Organisasi masyarakat sipil
"""
        )

    elif st.session_state.page == "Contact":
        st.markdown("## Contact")
        st.markdown("<div class='small-muted'>Form kontak dummy untuk demo UI.</div>", unsafe_allow_html=True)
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        with st.container(border=True):
            st.text_input("Nama")
            st.text_input("Email")
            st.text_area("Pesan", height=140, placeholder="Tulis pesan Anda di sini...")
            st.button("Kirim (dummy)")

        st.info("Catatan: pada frontend-only demo, form ini tidak mengirim email / menyimpan data.")

    elif st.session_state.page == "Search":
        st.markdown("## Search")
        st.markdown("<div class='small-muted'>Pencarian frontend-only pada data dummy.</div>", unsafe_allow_html=True)
        st.markdown("<hr class='soft'/>", unsafe_allow_html=True)

        query = st.text_input("Search by title / author / keywords", placeholder="contoh: hilirisasi, data, pembiayaan")
        results = []

        if query.strip():
            q = query.lower()
            for issue in ISSUES:
                for a in issue["articles"]:
                    hay = " ".join([a["title"], a["authors"], " ".join(a["keywords"]), issue["title"], issue["theme"]]).lower()
                    if q in hay:
                        results.append((issue, a))

        if query.strip() and not results:
            st.warning("No results found.")

        for issue, a in results:
            st.markdown(
                f"<div class='card'>"
                f"<div class='article-title'>{a['title']}</div>"
                f"<div class='meta'>{a['authors']} · {issue['title']} · <span class='badge'>{a['category']}</span></div>"
                f"<p style='margin-top:8px;'>{a['abstract']}</p>"
                f"</div>",
                unsafe_allow_html=True
            )
            st.button("View", key=f"sr_view_{a['id']}", on_click=select_article, args=(a["id"],))

# Footer
st.markdown("<hr class='soft'/>", unsafe_allow_html=True)
st.caption("© Agro Policy Insight — Demo frontend-only (Streamlit). Register/Login/Submission belum diaktifkan.")