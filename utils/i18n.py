"""
Translations for the Legal Document Simplifier app.
Supported languages: English (en), Tamil (ta), Hindi (hi).
"""

LANGUAGES = {
    "en": "English",
    "ta": "தமிழ்",
    "hi": "हिन्दी",
}

UI = {
    # ── Page ──────────────────────────────────────────────────────────────────
    "page_title": {
        "en": "Legal Document Simplifier",
        "ta": "சட்ட ஆவண எளிமைப்படுத்தி",
        "hi": "कानूनी दस्तावेज़ सरलीकरण",
    },
    "page_caption": {
        "en": "Paste a legal document, enter a URL, or upload a PDF — get a plain-English summary and flagged risks in seconds.",
        "ta": "சட்ட ஆவணத்தை ஒட்டவும், URL உள்ளிடவும் அல்லது PDF பதிவேற்றவும் — எளிய மொழியில் சுருக்கம் மற்றும் அபாயங்களை நொடியில் பெறுங்கள்.",
        "hi": "कानूनी दस्तावेज़ चिपकाएं, URL दर्ज करें, या PDF अपलोड करें — सेकंड में सरल भाषा में सारांश और जोखिम पाएं।",
    },
    "demo_banner": {
        "en": "Running in **demo mode** — analysis uses realistic sample output, not a live AI model.",
        "ta": "**டெமோ பயன்முறையில்** இயங்குகிறது — பகுப்பாய்வு உண்மையான AI மாதிரியை அல்ல, மாதிரி வெளியீட்டை பயன்படுத்துகிறது.",
        "hi": "**डेमो मोड** में चल रहा है — विश्लेषण एक लाइव AI मॉडल की बजाय नमूना आउटपुट का उपयोग करता है।",
    },
    # ── Tabs ──────────────────────────────────────────────────────────────────
    "tab_paste": {
        "en": "📋 Paste Text",
        "ta": "📋 உரையை ஒட்டு",
        "hi": "📋 टेक्स्ट चिपकाएं",
    },
    "tab_url": {
        "en": "🌐 URL",
        "ta": "🌐 URL",
        "hi": "🌐 URL",
    },
    "tab_pdf": {
        "en": "📄 Upload PDF",
        "ta": "📄 PDF பதிவேற்று",
        "hi": "📄 PDF अपलोड करें",
    },
    # ── Paste tab ─────────────────────────────────────────────────────────────
    "paste_label": {
        "en": "Paste your legal document here",
        "ta": "உங்கள் சட்ட ஆவணத்தை இங்கே ஒட்டவும்",
        "hi": "अपना कानूनी दस्तावेज़ यहाँ चिपकाएं",
    },
    "paste_placeholder": {
        "en": "Terms of Service, contract, privacy policy…",
        "ta": "சேவை விதிமுறைகள், ஒப்பந்தம், தனியுரிமைக் கொள்கை…",
        "hi": "सेवा की शर्तें, अनुबंध, गोपनीयता नीति…",
    },
    # ── URL tab ───────────────────────────────────────────────────────────────
    "url_label": {
        "en": "Document URL",
        "ta": "ஆவண URL",
        "hi": "दस्तावेज़ URL",
    },
    "url_placeholder": {
        "en": "https://example.com/terms-of-service",
        "ta": "https://example.com/terms-of-service",
        "hi": "https://example.com/terms-of-service",
    },
    "fetch_btn": {
        "en": "Fetch",
        "ta": "பெறு",
        "hi": "प्राप्त करें",
    },
    "url_empty_warning": {
        "en": "Please enter a URL.",
        "ta": "தயவுசெய்து URL உள்ளிடவும்.",
        "hi": "कृपया URL दर्ज करें।",
    },
    "fetching_spinner": {
        "en": "Fetching page…",
        "ta": "பக்கத்தை பெறுகிறது…",
        "hi": "पृष्ठ प्राप्त हो रहा है…",
    },
    "fetch_success": {
        "en": "Fetched {n:,} characters.",
        "ta": "{n:,} எழுத்துகள் பெறப்பட்டன.",
        "hi": "{n:,} अक्षर प्राप्त हुए।",
    },
    # ── PDF tab ───────────────────────────────────────────────────────────────
    "pdf_label": {
        "en": "Upload a PDF",
        "ta": "PDF பதிவேற்றவும்",
        "hi": "PDF अपलोड करें",
    },
    "pdf_spinner": {
        "en": "Extracting text from PDF…",
        "ta": "PDF இலிருந்து உரை பிரித்தெடுக்கிறது…",
        "hi": "PDF से टेक्स्ट निकाला जा रहा है…",
    },
    "pdf_success": {
        "en": "Extracted {n:,} characters from {name}.",
        "ta": "{name} இலிருந்து {n:,} எழுத்துகள் பிரித்தெடுக்கப்பட்டன.",
        "hi": "{name} से {n:,} अक्षर निकाले गए।",
    },
    # ── Preview ───────────────────────────────────────────────────────────────
    "preview_caption": {
        "en": "**{chars:,} characters · ~{tokens:,} tokens** — {preview}…",
        "ta": "**{chars:,} எழுத்துகள் · ~{tokens:,} டோக்கன்கள்** — {preview}…",
        "hi": "**{chars:,} अक्षर · ~{tokens:,} टोकन** — {preview}…",
    },
    # ── Analyze button ────────────────────────────────────────────────────────
    "analyze_btn": {
        "en": "Analyze Document",
        "ta": "ஆவணத்தை பகுப்பாய்வு செய்",
        "hi": "दस्तावेज़ विश्लेषण करें",
    },
    "analyze_btn_help": {
        "en": "Paste, fetch, or upload a document first.",
        "ta": "முதலில் ஆவணத்தை ஒட்டவும், பெறவும் அல்லது பதிவேற்றவும்.",
        "hi": "पहले कोई दस्तावेज़ चिपकाएं, प्राप्त करें या अपलोड करें।",
    },
    "analyze_spinner": {
        "en": "Analyzing document…",
        "ta": "ஆவணத்தை பகுப்பாய்வு செய்கிறது…",
        "hi": "दस्तावेज़ का विश्लेषण हो रहा है…",
    },
    # ── Results ───────────────────────────────────────────────────────────────
    "results_summary_header": {
        "en": "Plain English Summary",
        "ta": "எளிய மொழி சுருக்கம்",
        "hi": "सरल भाषा में सारांश",
    },
    "results_risks_header": {
        "en": "Risk Flags",
        "ta": "அபாய குறிகள்",
        "hi": "जोखिम संकेत",
    },
    "no_risks": {
        "en": "No specific risks were flagged.",
        "ta": "எந்த குறிப்பிட்ட அபாயங்களும் கண்டறியப்படவில்லை.",
        "hi": "कोई विशेष जोखिम नहीं पाया गया।",
    },
    # ── Language selector ─────────────────────────────────────────────────────
    "lang_label": {
        "en": "Language",
        "ta": "மொழி",
        "hi": "भाषा",
    },
    # ── Risk score ────────────────────────────────────────────────────────────
    "risk_score_label": {
        "en": "Overall Risk Score",
        "ta": "ஒட்டுமொத்த அபாய மதிப்பெண்",
        "hi": "समग्र जोखिम स्कोर",
    },
    "risk_level_critical": {
        "en": "CRITICAL RISK",
        "ta": "மிக அதிக அபாயம்",
        "hi": "गंभीर जोखिम",
    },
    "risk_level_high": {
        "en": "HIGH RISK",
        "ta": "அதிக அபாயம்",
        "hi": "उच्च जोखिम",
    },
    "risk_level_medium": {
        "en": "MEDIUM RISK",
        "ta": "நடுத்தர அபாயம்",
        "hi": "मध्यम जोखिम",
    },
    "risk_level_low": {
        "en": "LOW RISK",
        "ta": "குறைந்த அபாயம்",
        "hi": "कम जोखिम",
    },
}


# ── Demo content ──────────────────────────────────────────────────────────────

DEMO_SUMMARY = {
    "en": """\
- This is a Terms of Service agreement between you and the company.
- Using the service means you accept these terms — no signature needed.
- You must be of legal age and use the service lawfully.
- The company can change, suspend, or delete the service anytime.
- The company can rewrite these terms at any time without asking you.
- Your subscription auto-renews. Cancel before the renewal date to avoid charges.
- Refunds are generally not available.
- Content you upload can be used by the company to run and improve the service.
- Disputes go to arbitration — not regular court.
- You cannot join a class action lawsuit against the company.""",

    "ta": """\
- இது நிறுவனத்திற்கும் உங்களுக்கும் இடையேயான சேவை விதிமுறை ஒப்பந்தம்.
- சேவையை பயன்படுத்துவதன் மூலம் விதிமுறைகளை ஏற்கிறீர்கள் — கையொப்பம் தேவையில்லை.
- நீங்கள் சட்ட வயதுடையவராக இருக்க வேண்டும்; சட்டப்பூர்வமாக மட்டுமே பயன்படுத்தவும்.
- நிறுவனம் எந்த நேரத்திலும் சேவையை மாற்றவோ நிறுத்தவோ செய்யலாம்.
- நிறுவனம் உங்கள் அனுமதியின்றி எந்த நேரத்திலும் விதிமுறைகளை மாற்றலாம்.
- உங்கள் சந்தா தானாகவே புதுப்பிக்கப்படும். கட்டணம் தவிர்க்க முன்பே ரத்து செய்யுங்கள்.
- பொதுவாக பணம் திரும்ப வழங்கப்படாது.
- நீங்கள் பதிவேற்றும் உள்ளடக்கத்தை நிறுவனம் பயன்படுத்தலாம்.
- தகராறுகள் நடுவர் மன்றம் மூலம் மட்டுமே தீர்க்கப்படும்.
- நிறுவனத்திற்கு எதிராக வகுப்பு வழக்கில் நீங்கள் சேர முடியாது.""",

    "hi": """\
- यह आपके और कंपनी के बीच सेवा की शर्तें समझौता है।
- सेवा का उपयोग करने से आप शर्तें स्वीकार करते हैं — हस्ताक्षर जरूरी नहीं।
- आपकी कानूनी आयु होनी चाहिए और सेवा का कानूनी उपयोग करें।
- कंपनी कभी भी सेवा को बदल, रोक या बंद कर सकती है।
- कंपनी आपसे पूछे बिना कभी भी शर्तें बदल सकती है।
- सदस्यता स्वतः नवीनीकृत होती है। शुल्क से बचने के लिए पहले रद्द करें।
- आमतौर पर धनवापसी उपलब्ध नहीं है।
- आपकी अपलोड की गई सामग्री कंपनी उपयोग कर सकती है।
- विवाद केवल मध्यस्थता के माध्यम से सुलझाए जाएंगे।
- आप कंपनी के खिलाफ क्लास एक्शन मुकदमे में शामिल नहीं हो सकते।""",
}

DEMO_RISKS = {
    "en": [
        """\
1. **Automatic Renewal Without Reminder** — *"Your subscription will automatically renew at the end of each billing period. You authorize us to charge your payment method on file."*

**What it means:** The company will keep charging your card every month/year indefinitely unless you actively cancel. You won't get a reminder email before each charge.

**Severity: HIGH**""",
        """\
2. **Binding Arbitration & Class Action Waiver** — *"Any dispute arising from these Terms shall be resolved exclusively through binding arbitration. You waive your right to a jury trial and to participate in any class action lawsuit."*

**What it means:** If the company wrongs you, you can't sue them in regular court and you can't join other affected users in a class action. Arbitration typically favors corporations.

**Severity: HIGH**""",
        """\
3. **Liability Capped at $10** — *"Our total liability shall not exceed $10.00 under any circumstances."*

**What it means:** Even if the company loses all your data, leaks your private information, or causes you significant harm, the most they legally owe you is $10.

**Severity: HIGH**""",
        """\
4. **Data Sold to Third Parties** — *"Your data, including browsing history and usage patterns, may be shared with or sold to third-party partners for advertising and analytics purposes."*

**What it means:** Your personal information can be sold to advertisers or data brokers. You have little control over where it ends up.

**Severity: MEDIUM**""",
        """\
5. **Termination Without Notice or Refund** — *"We may terminate or suspend your account at any time, for any reason, without prior notice and without refund."*

**What it means:** The company can delete your account and keep any money you've paid, instantly, for any reason — including reasons not specified in the agreement.

**Severity: MEDIUM**""",
        """\
6. **Unilateral Term Changes** — *"We reserve the right to modify these Terms at any time. Continued use of the service constitutes acceptance of the new Terms."*

**What it means:** The company can change the rules whenever they want. Just by continuing to use the app, you automatically agree to whatever the new terms say.

**Severity: LOW**""",
    ],

    "ta": [
        """\
1. **தானியங்கி புதுப்பிப்பு — அறிவிப்பு இல்லாமல்** — *"உங்கள் சந்தா ஒவ்வொரு கட்டண காலத்தின் முடிவிலும் தானாகவே புதுப்பிக்கப்படும். கோப்பில் உள்ள உங்கள் கட்டண முறையில் கட்டணம் வசூலிக்க நீங்கள் அதிகாரம் வழங்குகிறீர்கள்."*

**அர்த்தம்:** நீங்கள் தீவிரமாக ரத்து செய்யாவிட்டால் நிறுவனம் ஒவ்வொரு மாதம்/ஆண்டும் உங்கள் கார்டில் தொடர்ந்து கட்டணம் வசூலிக்கும். ஒவ்வொரு கட்டணத்திற்கு முன்னரும் நினைவூட்டல் மின்னஞ்சல் வராது.

**தீவிரம்: அதிகம் (HIGH)**""",
        """\
2. **கட்டாய நடுவர் மன்றம் & வகுப்பு வழக்கு தள்ளுபடி** — *"இந்த விதிமுறைகளிலிருந்து எழும் எந்த தகராறும் கட்டாய நடுவர் மன்றம் மூலம் மட்டுமே தீர்க்கப்படும். நடுவர் மன்ற சோதனைக்கான உங்கள் உரிமையையும் வகுப்பு வழக்கில் பங்கேற்கும் உரிமையையும் நீங்கள் விட்டுவிடுகிறீர்கள்."*

**அர்த்தம்:** நிறுவனம் உங்களுக்கு தவறு செய்தால், வழக்கமான நீதிமன்றத்தில் வழக்கிட முடியாது மற்றும் பாதிக்கப்பட்ட மற்ற பயனர்களுடன் வகுப்பு வழக்கில் சேர முடியாது. நடுவர் மன்றம் பொதுவாக நிறுவனங்களுக்கு சாதகமாக இருக்கும்.

**தீவிரம்: அதிகம் (HIGH)**""",
        """\
3. **பொறுப்பு $10க்கு மட்டுப்படுத்தப்பட்டது** — *"எந்த சூழ்நிலையிலும் எங்கள் மொத்த பொறுப்பு $10.00 ஐ தாண்டாது."*

**அர்த்தம்:** நிறுவனம் உங்கள் அனைத்து தரவையும் இழந்தாலும், உங்கள் தனிப்பட்ட தகவலை கசியவிட்டாலும் அல்லது உங்களுக்கு குறிப்பிடத்தக்க தீங்கு விளைவித்தாலும், அவர்கள் சட்டரீதியாக $10 மட்டுமே கடமைப்பட்டுள்ளனர்.

**தீவிரம்: அதிகம் (HIGH)**""",
        """\
4. **தரவு மூன்றாம் தரப்பினருக்கு விற்கப்படுகிறது** — *"உங்கள் உலாவல் வரலாறு மற்றும் பயன்பாட்டு வடிவங்கள் உட்பட உங்கள் தரவு, விளம்பர மற்றும் பகுப்பாய்வு நோக்கங்களுக்காக மூன்றாம் தரப்பு பங்காளிகளுடன் பகிரப்படலாம் அல்லது விற்கப்படலாம்."*

**அர்த்தம்:** உங்கள் தனிப்பட்ட தகவல்கள் விளம்பரதாரர்கள் அல்லது தரவு தரகர்களுக்கு விற்கப்படலாம். அது எங்கே போகிறது என்பதில் உங்களுக்கு குறைந்த கட்டுப்பாடே உள்ளது.

**தீவிரம்: நடுத்தரம் (MEDIUM)**""",
        """\
5. **அறிவிப்பு அல்லது திரும்பப் பெறுதல் இல்லாமல் நிறுத்தம்** — *"எந்த நேரத்திலும், எந்த காரணத்திற்காகவும், முன் அறிவிப்பு இல்லாமல் மற்றும் திரும்பப் பெறாமல் உங்கள் கணக்கை நிறுத்தவோ இடைநிறுத்தவோ நாங்கள் உரிமை கொண்டுள்ளோம்."*

**அர்த்தம்:** நிறுவனம் உங்கள் கணக்கை உடனடியாக நீக்கலாம் மற்றும் நீங்கள் செலுத்திய எந்த பணத்தையும் வைத்துக்கொள்ளலாம் — ஒப்பந்தத்தில் குறிப்பிடப்படாத காரணங்களுக்காகவும்.

**தீவிரம்: நடுத்தரம் (MEDIUM)**""",
        """\
6. **ஒருதலைப்பட்ச விதிமுறை மாற்றங்கள்** — *"எந்த நேரத்திலும் இந்த விதிமுறைகளை மாற்றும் உரிமையை நாங்கள் கொண்டுள்ளோம். சேவையை தொடர்ந்து பயன்படுத்துவது புதிய விதிமுறைகளை ஏற்றுக்கொண்டதாக கருதப்படும்."*

**அர்த்தம்:** நிறுவனம் விரும்பும்போது விதிகளை மாற்றலாம். செயலியை தொடர்ந்து பயன்படுத்துவதன் மூலம், புதிய விதிமுறைகள் என்னவாக இருந்தாலும் நீங்கள் தானாகவே ஒப்புக்கொள்கிறீர்கள்.

**தீவிரம்: குறைவு (LOW)**""",
    ],

    "hi": [
        """\
1. **बिना सूचना के स्वतः नवीनीकरण** — *"आपकी सदस्यता प्रत्येक बिलिंग अवधि के अंत में स्वतः नवीनीकृत होगी। आप हमें बिना किसी सूचना के आपके भुगतान विधि पर शुल्क लगाने का अधिकार देते हैं।"*

**मतलब:** जब तक आप सक्रिय रूप से रद्द नहीं करते, कंपनी हर महीने/साल आपके कार्ड से शुल्क लेती रहेगी। प्रत्येक शुल्क से पहले कोई रिमाइंडर ईमेल नहीं आएगा।

**गंभीरता: उच्च (HIGH)**""",
        """\
2. **बाध्यकारी मध्यस्थता और क्लास एक्शन छूट** — *"इन शर्तों से उत्पन्न कोई भी विवाद विशेष रूप से बाध्यकारी मध्यस्थता के माध्यम से हल किया जाएगा। आप जूरी ट्रायल और किसी भी क्लास एक्शन मुकदमे में भाग लेने के अपने अधिकार को छोड़ देते हैं।"*

**मतलब:** यदि कंपनी आपके साथ गलत करती है, तो आप सामान्य अदालत में उन पर मुकदमा नहीं कर सकते और अन्य प्रभावित उपयोगकर्ताओं के साथ क्लास एक्शन में शामिल नहीं हो सकते। मध्यस्थता आमतौर पर कंपनियों के पक्ष में होती है।

**गंभीरता: उच्च (HIGH)**""",
        """\
3. **देनदारी $10 तक सीमित** — *"किसी भी परिस्थिति में हमारी कुल देनदारी $10.00 से अधिक नहीं होगी।"*

**मतलब:** भले ही कंपनी आपका सारा डेटा खो दे, आपकी निजी जानकारी लीक कर दे, या आपको महत्वपूर्ण नुकसान पहुंचाए, कानूनी रूप से वे केवल $10 के लिए जिम्मेदार हैं।

**गंभीरता: उच्च (HIGH)**""",
        """\
4. **डेटा तृतीय पक्षों को बेचा जाएगा** — *"आपका डेटा, जिसमें ब्राउज़िंग इतिहास और उपयोग पैटर्न शामिल हैं, विज्ञापन और विश्लेषण उद्देश्यों के लिए तृतीय-पक्ष भागीदारों के साथ साझा या बेचा जा सकता है।"*

**मतलब:** आपकी व्यक्तिगत जानकारी विज्ञापनदाताओं या डेटा दलालों को बेची जा सकती है। यह कहाँ जाती है, इस पर आपका बहुत कम नियंत्रण है।

**गंभीरता: मध्यम (MEDIUM)**""",
        """\
5. **बिना सूचना या धनवापसी के समाप्ति** — *"हम किसी भी समय, किसी भी कारण से, पूर्व सूचना के बिना और बिना धनवापसी के आपके खाते को समाप्त या निलंबित कर सकते हैं।"*

**मतलब:** कंपनी तुरंत आपका खाता हटा सकती है और आपके द्वारा भुगतान की गई कोई भी राशि रख सकती है — समझौते में निर्दिष्ट नहीं किए गए कारणों से भी।

**गंभीरता: मध्यम (MEDIUM)**""",
        """\
6. **एकतरफा शर्तों में बदलाव** — *"हम किसी भी समय इन शर्तों को संशोधित करने का अधिकार सुरक्षित रखते हैं। सेवा का निरंतर उपयोग नई शर्तों की स्वीकृति माना जाएगा।"*

**मतलब:** कंपनी जब चाहे नियम बदल सकती है। ऐप का उपयोग जारी रखने से, आप स्वतः नई शर्तों से सहमत हो जाते हैं — चाहे वे कुछ भी हों।

**गंभीरता: कम (LOW)**""",
    ],
}


def t(key: str, lang: str, **kwargs) -> str:
    """Return the translated string for key in lang, with optional format args."""
    text = UI[key].get(lang) or UI[key]["en"]
    return text.format(**kwargs) if kwargs else text
