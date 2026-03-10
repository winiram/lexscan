# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
python3 -m streamlit run app.py
```

The app runs in **demo mode** by default — no API key is needed. To enable live AI analysis, set `ANTHROPIC_API_KEY` in a `.env` file (see `.env.example`) and rewrite `utils/claude_client.py` to call the Anthropic SDK.

## Architecture

Single-page Streamlit app (`app.py`) with four utility modules under `utils/`:

| Module | Responsibility |
|--------|---------------|
| `claude_client.py` | Returns `{"summary": str, "risks": list[str]}`. Currently demo mode (fixed output + 2 s sleep). Swap internals here to go live. |
| `i18n.py` | All user-facing strings and demo content. `t(key, lang, **kwargs)` is the only translation helper. `UI` dict holds EN/TA/HI strings; `DEMO_SUMMARY` / `DEMO_RISKS` hold demo output. |
| `url_fetcher.py` | Fetches a URL → cleaned plain text. Has SSRF protection (`_validate_url` checks scheme whitelist + private IP blocking via `ipaddress`), 5 MB streaming cap, post-redirect re-validation. |
| `pdf_parser.py` | Extracts text from a PDF via `pdfplumber`. Enforces 100-page limit. |
| `chunker.py` | Token counting + splitting via `tiktoken` (`cl100k_base`, 140 K token chunks). Used for the preview caption and would be used for chunked analysis on long docs. |

### Input → session state flow

Three tabs each write into `st.session_state.extracted_text`:
- **Paste**: capped at 500 000 chars
- **URL**: `url_fetcher.fetch_clean_text()`
- **PDF**: `pdf_parser.extract_text()`, capped at 10 MB / 100 pages

"Analyze Document" calls `claude_client.analyze_document(text, lang)` → result stored in `st.session_state.analysis_result`.

### Results layout

Three columns `[0.3, 2.4, 1.8]`: narrow spacer | risk flags (center) | plain-English summary card (right).

Risk score = `(HIGH×3 + MEDIUM×2 + LOW×1) / (total×3) × 10` — thresholds: ≥7.5 Critical, ≥5.0 High, ≥3.0 Medium.

Risk severity detection works across all three languages because every translated risk item embeds the English keyword (`HIGH` / `MEDIUM` / `LOW`).

### Adding a language

1. Add the code + display name to `LANGUAGES` in `i18n.py`.
2. Add translations for every key in `UI`, `DEMO_SUMMARY`, and `DEMO_RISKS`.
3. Add a demo note string inside `demo_notes` in `claude_client.py`.

### Going live (replacing demo mode)

Rewrite `utils/claude_client.py` to call the Anthropic API. The function signature and return shape (`{"summary": str, "risks": list[str]}`) must stay the same. Use `utils/chunker.py`'s `split_into_chunks` for documents over 140 K tokens.

## Security Constraints

- All user content inserted into HTML must go through `html.escape()` (`import html as _html` is already at the top of `app.py`).
- `url_fetcher._validate_url()` must be called both before the request and after redirects — do not remove either call.
- Do not raise exceptions that include raw exception details (`str(e)`) in user-facing messages in `pdf_parser.py`.
