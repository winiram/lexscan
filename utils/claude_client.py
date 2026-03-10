import re

import google.generativeai as genai
import streamlit as st

from utils.chunker import split_into_chunks

MODEL = "gemini-2.0-flash"

_SYSTEM = (
    "You are an expert legal analyst who translates complex legal language into "
    "plain, simple language for non-lawyers. Be concise, accurate, and objective."
)

_USER_TMPL = {
    "en": """\
Analyze the following legal document and respond in English with exactly two sections:

## PLAIN ENGLISH SUMMARY
Write 300-500 words organized into clear paragraphs explaining what this document says in plain English. Focus on what the user is agreeing to, their rights, and the company's rights.

## RISK FLAGS
List every significant risk or one-sided clause. For each one:
- Quote the relevant clause (in italics)
- Explain in plain English what it means
- End with **Severity: HIGH**, **Severity: MEDIUM**, or **Severity: LOW**

Number each risk flag starting from 1.

DOCUMENT:
{text}""",

    "ta": """\
பின்வரும் சட்ட ஆவணத்தை பகுப்பாய்வு செய்து தமிழில் சரியாக இரண்டு பிரிவுகளுடன் பதிலளிக்கவும்:

## PLAIN ENGLISH SUMMARY
இந்த ஆவணம் என்ன சொல்கிறது என்பதை 300-500 வார்த்தைகளில் தெளிவான பத்திகளில் விளக்கவும்.

## RISK FLAGS
ஒவ்வொரு குறிப்பிடத்தக்க அபாயம் அல்லது ஒருதலைப்பட்ச விதிகளை பட்டியலிடவும். ஒவ்வொன்றிற்கும்:
- தொடர்புடைய விதியை மேற்கோள் காட்டவும்
- அது என்னவென்று எளிய மொழியில் விளக்கவும்
- **Severity: HIGH**, **Severity: MEDIUM**, அல்லது **Severity: LOW** என்று முடிக்கவும்

ஒவ்வொரு அபாய குறியையும் 1 முதல் எண்ணிடவும்.

ஆவணம்:
{text}""",

    "hi": """\
निम्नलिखित कानूनी दस्तावेज़ का विश्लेषण करें और हिंदी में ठीक दो अनुभागों के साथ उत्तर दें:

## PLAIN ENGLISH SUMMARY
इस दस्तावेज़ में क्या लिखा है, इसे 300-500 शब्दों में स्पष्ट पैराग्राफ में समझाएं।

## RISK FLAGS
हर महत्वपूर्ण जोखिम या एकतरफा खंड की सूची बनाएं। प्रत्येक के लिए:
- संबंधित खंड को उद्धृत करें
- सरल भाषा में समझाएं
- **Severity: HIGH**, **Severity: MEDIUM**, या **Severity: LOW** से समाप्त करें

प्रत्येक जोखिम संकेत को 1 से शुरू करके क्रमांकित करें।

दस्तावेज़:
{text}""",
}

_REDUCE_TMPL = {
    "en": """\
The following are analyses of different sections of the same legal document.
Merge them into a single cohesive response with:

## PLAIN ENGLISH SUMMARY
A unified 300-500 word summary covering the whole document.

## RISK FLAGS
A deduplicated, numbered list of all risk flags across all sections, each with severity.

SECTION ANALYSES:
{text}""",

    "ta": """\
பின்வருபவை ஒரே சட்ட ஆவணத்தின் வெவ்வேறு பகுதிகளின் பகுப்பாய்வுகள்.
அவற்றை ஒரே ஒருங்கிணைந்த பதிலாக இணைக்கவும்:

## PLAIN ENGLISH SUMMARY
முழு ஆவணத்தை உள்ளடக்கிய 300-500 வார்த்தை சுருக்கம்.

## RISK FLAGS
அனைத்து பிரிவுகளிலும் உள்ள அனைத்து அபாய குறிகளின் நகல் நீக்கப்பட்ட, எண்ணிடப்பட்ட பட்டியல்.

பிரிவு பகுப்பாய்வுகள்:
{text}""",

    "hi": """\
निम्नलिखित एक ही कानूनी दस्तावेज़ के विभिन्न अनुभागों के विश्लेषण हैं।
इन्हें एक एकीकृत प्रतिक्रिया में मिलाएं:

## PLAIN ENGLISH SUMMARY
पूरे दस्तावेज़ को कवर करने वाला 300-500 शब्दों का सारांश।

## RISK FLAGS
सभी अनुभागों के सभी जोखिम संकेतों की डुप्लीकेट-रहित, क्रमांकित सूची।

अनुभाग विश्लेषण:
{text}""",
}


def _get_model():
    api_key = st.secrets.get("GOOGLE_API_KEY") or None
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. Add it to your Streamlit secrets."
        )
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=MODEL,
        system_instruction=_SYSTEM,
    )


def _call(model, user_prompt: str) -> str:
    response = model.generate_content(user_prompt)
    return response.text


def _parse(response: str) -> dict:
    """Split the model response into summary + list of risk strings."""
    parts = re.split(r"##\s*RISK FLAGS", response, maxsplit=1)
    summary = parts[0].replace("## PLAIN ENGLISH SUMMARY", "").strip()

    risks = []
    if len(parts) > 1:
        risk_text = parts[1].strip()
        items = re.split(r"\n(?=\d+\.)", risk_text)
        risks = [item.strip() for item in items if item.strip()]

    return {"summary": summary, "risks": risks}


def analyze_document(text: str, lang: str = "en") -> dict:
    """Analyze a legal document with Gemini. Returns {"summary": str, "risks": list[str]}."""
    model = _get_model()
    chunks = split_into_chunks(text)
    tmpl = _USER_TMPL.get(lang, _USER_TMPL["en"])

    if len(chunks) == 1:
        response = _call(model, tmpl.format(text=chunks[0]))
    else:
        chunk_analyses = [_call(model, tmpl.format(text=chunk)) for chunk in chunks]
        reduce_tmpl = _REDUCE_TMPL.get(lang, _REDUCE_TMPL["en"])
        combined = "\n\n---\n\n".join(chunk_analyses)
        response = _call(model, reduce_tmpl.format(text=combined))

    return _parse(response)
