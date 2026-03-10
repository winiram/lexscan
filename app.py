import html as _html
import streamlit as st

from utils.pdf_parser import extract_text
from utils.url_fetcher import fetch_clean_text
from utils.chunker import count_tokens
from utils.i18n import LANGUAGES, t

_MAX_PASTE_CHARS = 500_000   # ~140 K tokens — same as chunker limit
_MAX_PDF_MB = 10

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LexScan — Legal Document Simplifier",
    page_icon="⚖️",
    layout="wide",
)

# ── Global CSS — dark theme + dot-grid background ─────────────────────────────
st.markdown(
    """
    <style>
    /* ── Background — muted dark-gray/blue grid ───────────────────────── */
    .stApp {
        background-color: #0d1117;
        background-image:
            /* fine grid lines */
            linear-gradient(rgba(56,96,140,0.07) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56,96,140,0.07) 1px, transparent 1px),
            /* coarser accent grid */
            linear-gradient(rgba(56,96,140,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56,96,140,0.04) 1px, transparent 1px),
            /* soft top glow */
            radial-gradient(ellipse 70% 38% at 50% 0%, rgba(30,64,110,0.30) 0%, transparent 70%),
            /* subtle corner accent */
            radial-gradient(ellipse 40% 25% at 92% 95%, rgba(40,50,90,0.22) 0%, transparent 60%);
        background-size:
            60px 60px, 60px 60px,
            12px 12px, 12px 12px,
            100% 100%, 100% 100%;
        color: #e2e8f0;
    }

    /* ── Layout ───────────────────────────────────────────────────────── */
    section[data-testid="stSidebar"] { display: none; }

    /* Make Streamlit's sticky header bar transparent so the pattern shows through */
    [data-testid="stHeader"],
    .stAppHeader,
    header[data-testid="stHeader"] {
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }

    /* Push content down past the now-transparent header */
    .block-container { max-width: 1240px; padding-top: 3.5rem; padding-bottom: 3rem; }

    /* ── Typography ───────────────────────────────────────────────────── */
    h1, h2, h3 { color: #e2e8f0 !important; font-weight: 700 !important; }
    .stMarkdown p, .stMarkdown li { color: #94a3b8 !important; }

    /* ── Logo ─────────────────────────────────────────────────────────── */
    .logo-wrap {
        display: flex; align-items: center; gap: 14px;
        padding: 12px 0 22px;
    }
    .logo-name {
        font-size: 1.65rem; font-weight: 800; letter-spacing: -0.5px;
        background: linear-gradient(135deg, #63b3ed 0%, #9f7aea 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .logo-tag {
        font-size: 0.63rem; color: rgba(226,232,240,0.35);
        text-transform: uppercase; letter-spacing: 2.5px; margin-top: -4px;
    }

    /* ── Tabs ─────────────────────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.025) !important;
        border: 1px solid rgba(99,179,237,0.1) !important;
        border-radius: 10px !important;
        gap: 6px !important;
        padding: 6px !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: rgba(226,232,240,0.5) !important;
        border-radius: 7px !important;
        padding: 8px 22px !important;
        font-size: 0.92rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(99,179,237,0.15) !important;
        color: #63b3ed !important; font-weight: 600 !important;
    }
    /* breathing room below the tab bar */
    .stTabs [data-baseweb="tab-panel"] { padding-top: 18px !important; }

    /* ── Text inputs ──────────────────────────────────────────────────── */
    .stTextArea textarea, .stTextInput input {
        background: rgba(255,255,255,0.035) !important;
        border: 1px solid rgba(99,179,237,0.18) !important;
        color: #e2e8f0 !important; border-radius: 10px !important;
    }
    .stTextArea textarea::placeholder, .stTextInput input::placeholder {
        color: rgba(226,232,240,0.28) !important;
    }

    /* ── File uploader ────────────────────────────────────────────────── */
    [data-testid="stFileUploader"] section {
        background: rgba(255,255,255,0.025) !important;
        border: 1px dashed rgba(99,179,237,0.22) !important; border-radius: 10px !important;
    }

    /* ── Analyze button ───────────────────────────────────────────────── */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4299e1 0%, #805ad5 100%) !important;
        border: none !important; border-radius: 10px !important;
        font-weight: 600 !important; letter-spacing: 0.4px !important;
        padding: 0.55rem 2rem !important;
        box-shadow: 0 4px 16px rgba(66,153,225,0.28) !important;
        transition: opacity 0.2s, box-shadow 0.2s !important;
    }
    .stButton > button[kind="primary"]:hover {
        opacity: 0.87 !important;
        box-shadow: 0 6px 22px rgba(66,153,225,0.42) !important;
    }

    /* ── Risk score card ──────────────────────────────────────────────── */
    .risk-score-card {
        background: linear-gradient(145deg, rgba(20,27,45,0.94) 0%, rgba(12,18,32,0.97) 100%);
        border: 1px solid rgba(99,179,237,0.18); border-radius: 18px;
        padding: 28px 20px 22px; text-align: center; margin-bottom: 22px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.04);
    }
    .rs-label {
        font-size: 0.7rem; color: rgba(226,232,240,0.4);
        text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 10px;
    }
    .rs-num { font-size: 4.5rem; font-weight: 900; line-height: 1; letter-spacing: -3px; }
    .rs-den { font-size: 1.3rem; color: rgba(226,232,240,0.3); }
    .rs-badge {
        display: inline-block; padding: 5px 20px; border-radius: 999px;
        font-size: 0.7rem; font-weight: 700; letter-spacing: 2px;
        text-transform: uppercase; margin-top: 12px;
    }

    /* ── Summary card ─────────────────────────────────────────────────── */
    .summary-card {
        background: linear-gradient(145deg, rgba(20,27,45,0.88) 0%, rgba(12,18,32,0.92) 100%);
        border: 1px solid rgba(159,122,234,0.18); border-radius: 18px;
        padding: 24px 22px;
        box-shadow: 0 6px 24px rgba(0,0,0,0.4);
    }

    /* ── Alert boxes ──────────────────────────────────────────────────── */
    .stAlert { border-radius: 10px !important; }

    /* ── Misc ─────────────────────────────────────────────────────────── */
    hr { border-color: rgba(99,179,237,0.1) !important; }
    .stCaption, [data-testid="stCaptionContainer"] { color: rgba(148,163,184,0.7) !important; }
    div[data-testid="stSelectbox"] label {
        color: rgba(226,232,240,0.65) !important; font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Logo SVG (scales of justice) ──────────────────────────────────────────────
_LOGO = """\
<svg xmlns="http://www.w3.org/2000/svg" width="52" height="52" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#63b3ed"/>
      <stop offset="100%" stop-color="#9f7aea"/>
    </linearGradient>
  </defs>
  <circle cx="50" cy="50" r="47" fill="#080f1e" stroke="url(#lg)" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="40" fill="rgba(99,179,237,0.03)"/>
  <!-- pillar -->
  <rect x="48.5" y="22" width="3" height="55" rx="1.5" fill="url(#lg)"/>
  <!-- crossbar -->
  <rect x="22" y="32" width="56" height="3.5" rx="1.75" fill="url(#lg)"/>
  <!-- left chains -->
  <line x1="30" y1="35.5" x2="25" y2="51" stroke="url(#lg)" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="30" y1="35.5" x2="35" y2="51" stroke="url(#lg)" stroke-width="1.8" stroke-linecap="round"/>
  <!-- right chains -->
  <line x1="70" y1="35.5" x2="65" y2="51" stroke="url(#lg)" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="70" y1="35.5" x2="75" y2="51" stroke="url(#lg)" stroke-width="1.8" stroke-linecap="round"/>
  <!-- left pan -->
  <path d="M17 51 Q30 64 43 51" stroke="url(#lg)" stroke-width="2.2"
        fill="rgba(99,179,237,0.08)" stroke-linecap="round"/>
  <!-- right pan (slightly lower) -->
  <path d="M57 53 Q70 66 83 53" stroke="url(#lg)" stroke-width="2.2"
        fill="rgba(99,179,237,0.08)" stroke-linecap="round"/>
  <!-- base -->
  <rect x="38" y="76" width="24" height="3.5" rx="1.75" fill="url(#lg)"/>
  <rect x="30" y="78.5" width="40" height="2.5" rx="1.25" fill="rgba(99,179,237,0.3)"/>
</svg>"""


# ── Helper functions ──────────────────────────────────────────────────────────
def _compute_risk_score(risks: list) -> float:
    high = sum(1 for r in risks if "HIGH" in r.upper())
    medium = sum(1 for r in risks if "MEDIUM" in r.upper())
    total = len(risks) or 1
    low = max(total - high - medium, 0)
    return round(min((high * 3 + medium * 2 + low) / (total * 3) * 10, 10.0), 1)


def _score_style(score: float):
    """Returns (number_color, badge_bg, badge_fg)."""
    if score >= 7.5:
        return "#ff4560", "rgba(255,69,96,0.15)", "#ff8095"
    if score >= 5.0:
        return "#ff7b44", "rgba(255,123,68,0.15)", "#ffaa88"
    if score >= 3.0:
        return "#ffc107", "rgba(255,193,7,0.15)", "#ffe082"
    return "#22d3a5", "rgba(34,211,165,0.15)", "#86efcb"


def _score_label(score: float, lang: str) -> str:
    if score >= 7.5:
        return t("risk_level_critical", lang)
    if score >= 5.0:
        return t("risk_level_high", lang)
    if score >= 3.0:
        return t("risk_level_medium", lang)
    return t("risk_level_low", lang)


def _summary_html(text: str, header: str) -> str:
    """Convert bullet-point markdown summary to a styled dark card."""
    lines = text.strip().split("\n")
    items, footer = [], ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("*"):
            escaped = _html.escape(line.replace("*", "").strip())
            footer = (
                f'<p style="margin-top:14px;font-size:0.75rem;'
                f'color:rgba(148,163,184,0.4);font-style:italic;">'
                f'{escaped}</p>'
            )
        elif line.startswith("- "):
            escaped = _html.escape(line[2:])
            items.append(
                f'<li style="color:#94a3b8;margin-bottom:10px;line-height:1.55;">'
                f'<span style="color:#63b3ed;margin-right:9px;">▸</span>{escaped}</li>'
            )
        else:
            escaped = _html.escape(line)
            items.append(f'<li style="color:#94a3b8;margin-bottom:10px;">{escaped}</li>')

    safe_header = _html.escape(header)
    return (
        f'<div class="summary-card">'
        f'<div style="font-size:0.7rem;color:rgba(226,232,240,0.38);text-transform:uppercase;'
        f'letter-spacing:2.5px;margin-bottom:14px;padding-bottom:12px;'
        f'border-bottom:1px solid rgba(159,122,234,0.15);">{safe_header}</div>'
        f'<ul style="list-style:none;padding:0;margin:0;">{"".join(items)}</ul>'
        f'{footer}</div>'
    )


# ── Language setup ────────────────────────────────────────────────────────────
lang_names = list(LANGUAGES.values())   # ["English", "தமிழ்", "हिन्दी"]
lang_codes = list(LANGUAGES.keys())     # ["en", "ta", "hi"]

if "lang_select" not in st.session_state:
    st.session_state.lang_select = lang_names[0]
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

lang = lang_codes[lang_names.index(st.session_state.lang_select)]


def _on_lang_change():
    new_lang = lang_codes[lang_names.index(st.session_state.lang_select)]
    text = st.session_state.get("extracted_text", "")
    if text and st.session_state.get("analysis_result") is not None:
        from utils.claude_client import analyze_document
        st.session_state.analysis_result = analyze_document(text, lang=new_lang)


# ── Header: logo + language selector ─────────────────────────────────────────
logo_col, _, lang_col = st.columns([3, 2, 1])
with logo_col:
    st.markdown(
        f'<div class="logo-wrap">{_LOGO}'
        f'<div><div class="logo-name">LexScan</div>'
        f'<div class="logo-tag">Legal Intelligence Platform</div></div></div>',
        unsafe_allow_html=True,
    )
with lang_col:
    st.selectbox(
        "🌐 " + t("lang_label", lang),
        options=lang_names,
        key="lang_select",
        on_change=_on_lang_change,
    )

# ── Page header ───────────────────────────────────────────────────────────────
st.title(t("page_title", lang))
st.caption(t("page_caption", lang))
st.info(t("demo_banner", lang))

# ── Input tabs ────────────────────────────────────────────────────────────────
tab_paste, tab_url, tab_pdf = st.tabs([
    t("tab_paste", lang),
    t("tab_url", lang),
    t("tab_pdf", lang),
])

with tab_paste:
    pasted = st.text_area(
        t("paste_label", lang),
        height=260,
        placeholder=t("paste_placeholder", lang),
        key="paste_input",
    )
    pasted_stripped = pasted.strip()
    if pasted_stripped:
        if len(pasted_stripped) > _MAX_PASTE_CHARS:
            st.error(
                f"Input is too large ({len(pasted_stripped):,} characters). "
                f"Please paste no more than {_MAX_PASTE_CHARS:,} characters."
            )
        elif pasted_stripped != st.session_state.extracted_text:
            st.session_state.extracted_text = pasted_stripped
            st.session_state.analysis_result = None

with tab_url:
    url_input = st.text_input(
        t("url_label", lang),
        placeholder=t("url_placeholder", lang),
        key="url_input",
    )
    if st.button(t("fetch_btn", lang), key="fetch_btn"):
        if not url_input.strip():
            st.warning(t("url_empty_warning", lang))
        else:
            with st.spinner(t("fetching_spinner", lang)):
                try:
                    fetched = fetch_clean_text(url_input.strip())
                    st.session_state.extracted_text = fetched
                    st.session_state.analysis_result = None
                    st.success(t("fetch_success", lang, n=len(fetched)))
                except ValueError as e:
                    st.error(str(e))

with tab_pdf:
    uploaded_file = st.file_uploader(
        t("pdf_label", lang),
        type=["pdf"],
        key="pdf_input",
    )
    if uploaded_file is not None:
        file_mb = uploaded_file.size / (1024 * 1024)
        if file_mb > _MAX_PDF_MB:
            st.error(
                f"File is too large ({file_mb:.1f} MB). "
                f"Please upload a PDF smaller than {_MAX_PDF_MB} MB."
            )
        else:
            with st.spinner(t("pdf_spinner", lang)):
                try:
                    pdf_text = extract_text(uploaded_file)
                    st.session_state.extracted_text = pdf_text
                    st.session_state.analysis_result = None
                    st.success(t("pdf_success", lang, n=len(pdf_text), name=uploaded_file.name))
                except ValueError as e:
                    st.error(str(e))
                    st.session_state.extracted_text = ""

# ── Preview ───────────────────────────────────────────────────────────────────
text = st.session_state.extracted_text
if text:
    token_count = count_tokens(text)
    preview = text[:200].replace("\n", " ")
    st.caption(t("preview_caption", lang, chars=len(text), tokens=token_count, preview=preview))

st.divider()

# ── Analyze button ────────────────────────────────────────────────────────────
can_analyze = len(text) > 50
if st.button(
    t("analyze_btn", lang),
    type="primary",
    disabled=not can_analyze,
    help=t("analyze_btn_help", lang) if not can_analyze else None,
):
    from utils.claude_client import analyze_document
    with st.spinner(t("analyze_spinner", lang)):
        result = analyze_document(text, lang=lang)
    st.session_state.analysis_result = result

# ── Results ───────────────────────────────────────────────────────────────────
result = st.session_state.analysis_result
if result:
    risks = result.get("risks", [])

    # Compute overall risk score
    score = _compute_risk_score(risks)
    num_color, badge_bg, badge_fg = _score_style(score)
    level = _score_label(score, lang)

    # Layout: small left buffer | risk flags (center) | summary (right corner)
    _, col_risks, col_summary = st.columns([0.3, 2.4, 1.8], gap="large")

    with col_risks:
        # ── Risk score card ────────────────────────────────────────────────
        st.markdown(
            f'<div class="risk-score-card">'
            f'<div class="rs-label">{t("risk_score_label", lang)}</div>'
            f'<div>'
            f'<span class="rs-num" style="color:{num_color};">{score}</span>'
            f'<span class="rs-den">&thinsp;/10</span>'
            f'</div>'
            f'<div>'
            f'<span class="rs-badge" style="background:{badge_bg};color:{badge_fg};'
            f'border:1px solid {badge_fg}55;">{level}</span>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # ── Risk flags ────────────────────────────────────────────────────
        st.subheader(t("results_risks_header", lang))
        if not risks:
            st.info(t("no_risks", lang))
        else:
            for risk in risks:
                risk_upper = risk.upper()
                if "HIGH" in risk_upper:
                    st.error(risk)
                elif "MEDIUM" in risk_upper:
                    st.warning(risk)
                else:
                    st.info(risk)

    with col_summary:
        # ── Plain-language summary card ───────────────────────────────────
        st.markdown(
            _summary_html(result["summary"], t("results_summary_header", lang)),
            unsafe_allow_html=True,
        )
