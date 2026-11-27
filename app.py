import streamlit as st
import re
import math
import string
import hashlib

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NEXUS SHIELD | Password Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
    radial-gradient(ellipse at 10% 0%, rgba(88,65,190,0.16), transparent 35%),
    radial-gradient(ellipse at 90% 20%, rgba(0,150,255,0.10), transparent 35%),
    #080D19;
    color: #F3F5FC;
}

header, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1150px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

/* HEADER */

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 35px;
}

.brand-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg,#7047EA,#168BFF);
    font-size: 25px;
    box-shadow: 0 5px 25px rgba(83,89,255,.3);
}

.brand-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 23px;
    font-weight: 700;
    letter-spacing: 1px;
}

.brand-sub {
    color: #8994AB;
    font-size: 10px;
    letter-spacing: 2px;
}

/* HERO */

.hero {
    padding: 25px 0 35px;
    animation: appear .8s ease;
}

.eyebrow {
    display: inline-block;
    padding: 7px 13px;
    border: 1px solid rgba(123,100,255,.3);
    border-radius: 30px;
    background: rgba(105,79,255,.09);
    color: #A99BFF;
    font-size: 11px;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(36px,5vw,58px);
    font-weight: 700;
    line-height: 1.12;
    margin: 22px 0 15px;
}

.gradient-text {
    background: linear-gradient(90deg,#A68BFF,#48B9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #8995AD;
    font-size: 15px;
    max-width: 570px;
    line-height: 1.8;
}

/* CARDS */

.panel {
    background: linear-gradient(145deg,rgba(24,32,54,.94),rgba(14,21,37,.96));
    border: 1px solid rgba(139,157,200,.12);
    border-radius: 19px;
    padding: 25px;
    height: 100%;
    transition: .3s ease;
    box-shadow: 0 12px 35px rgba(0,0,0,.12);
}

.panel:hover {
    border-color: rgba(117,126,255,.38);
    transform: translateY(-3px);
}

.panel-title {
    font-family: 'Space Grotesk',sans-serif;
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 8px;
}

.panel-description {
    color: #8995AD;
    font-size: 12px;
    margin-bottom: 22px;
}

/* INPUT */

.stTextInput input {
    background: #0A1121 !important;
    border: 1px solid #28344E !important;
    border-radius: 11px !important;
    color: white !important;
    padding: 15px !important;
    height: 52px;
}

.stTextInput input:focus {
    border-color: #8870FF !important;
    box-shadow: 0 0 0 2px rgba(136,112,255,.12) !important;
}

/* BUTTON */

.stButton button {
    width: 100%;
    background: linear-gradient(100deg,#754BEA,#247DFA);
    color: white;
    border: none;
    border-radius: 11px;
    height: 47px;
    font-weight: 700;
    transition: .25s ease;
}

.stButton button:hover {
    box-shadow: 0 5px 24px rgba(91,105,255,.35);
    transform: translateY(-2px);
    color: white;
}

/* METRICS */

.metric-card {
    background: #10192B;
    border: 1px solid #26344E;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 12px;
}

.metric-label {
    font-size: 11px;
    color: #8995AD;
    letter-spacing: 1px;
}

.metric-value {
    font-family: 'Space Grotesk',sans-serif;
    font-size: 23px;
    font-weight: 700;
    margin-top: 7px;
}

.progress-bg {
    height: 9px;
    border-radius: 20px;
    background: #25314A;
    overflow: hidden;
    margin: 15px 0;
}

.progress-fill {
    height: 100%;
    border-radius: 20px;
    transition: width 1s ease;
}

/* SUGGESTIONS */

.suggestion {
    padding: 12px 14px;
    border-radius: 10px;
    background: rgba(255,255,255,.025);
    border: 1px solid rgba(255,255,255,.07);
    margin: 9px 0;
    font-size: 13px;
}

.good {
    color: #55DDAA;
}

.bad {
    color: #FF8998;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #64718A;
    font-size: 11px;
    padding-top: 45px;
    letter-spacing: 1px;
}

.developer-name {
    display: inline-block;
    color: #B8A8FF;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 17px;
    font-weight: 800;
    font-style: italic;
    letter-spacing: 1px;
    margin-top: 5px;
    transition: .3s ease;
}

.developer-name:hover {
    color: #55B9FF;
    text-shadow: 0 0 15px rgba(120,110,255,.5);
}

@keyframes appear {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

@media(max-width:700px) {
    .hero h1 {font-size: 37px;}
    .panel {padding: 18px;}
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="brand">
    <div class="brand-icon">🛡️</div>
    <div>
        <div class="brand-name">NEXUS SHIELD</div>
        <div class="brand-sub">PERSONAL SECURITY LAB</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">
    <span class="eyebrow">● PASSWORD SECURITY ANALYZER</span>
    <h1>Make your passwords<br>
    <span class="gradient-text">hard to break.</span></h1>
    <p>
    Understand your password security through intelligent
    analysis, strength estimation and practical recommendations.
    Your password is processed locally within this application.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- PASSWORD ANALYSIS ----------------

def analyze_password(password):

    score = 0
    suggestions = []

    length = len(password)

    checks = {
        "Length": length >= 12,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Numbers": bool(re.search(r"[0-9]", password)),
        "Symbols": bool(re.search(r"[^a-zA-Z0-9]", password))
    }

    score += sum(checks.values()) * 20

    if length < 8:
        suggestions.append("Use at least 12 characters for better security.")

    if not checks["Uppercase"]:
        suggestions.append("Add uppercase letters (A-Z).")

    if not checks["Lowercase"]:
        suggestions.append("Include lowercase letters (a-z).")

    if not checks["Numbers"]:
        suggestions.append("Include numbers (0-9).")

    if not checks["Symbols"]:
        suggestions.append("Add special characters like @, #, or !.")

    common = [
        "password", "123456", "qwerty",
        "admin", "welcome", "letmein"
    ]

    if password.lower() in common:
        score = 0
        suggestions.append("Avoid commonly used passwords.")

    if re.search(r"(.)\1{2,}", password):
        score -= 15
        suggestions.append("Avoid repeating the same character.")

    if re.search(r"1234|abcd|qwerty", password.lower()):
        score -= 15
        suggestions.append("Avoid predictable sequences.")

    score = max(0, min(score, 100))

    if score < 40:
        strength = "Weak"
        color = "#FF657A"
    elif score < 80:
        strength = "Moderate"
        color = "#F6B84B"
    else:
        strength = "Strong"
        color = "#36D6A0"

    return score, strength, color, checks, suggestions


# ---------------- INTERFACE ----------------

left, right = st.columns([1.15, 0.85], gap="large")

with left:

    st.markdown("""
    <div class="panel">
        <div class="panel-title">🔐 Password inspection</div>
        <div class="panel-description">
        Enter a password to evaluate its security characteristics.
        </div>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input(
        "Your password",
        type="password",
        placeholder="Enter your password here...",
        key="password_input"
    )

    analyze = st.button("Analyze password →")

    if analyze:
        if password:
            st.session_state["analyzed"] = True
            st.session_state["password"] = password
        else:
            st.warning("Please enter a password first.")

    if "analyzed" not in st.session_state:
        st.markdown("""
        <div class="panel" style="margin-top:15px;">
            <div class="panel-title">Ready for inspection</div>
            <p style="color:#8995AD;font-size:13px;line-height:1.8;">
            Your security report will appear here after analysis.
            Use a sample password rather than a password you currently
            use for an important account.
            </p>
        </div>
        """, unsafe_allow_html=True)


with right:

    st.markdown("""
    <div class="panel">
        <div class="panel-title">📡 Security overview</div>
        <div class="panel-description">
        What makes a password more resilient?
        </div>
    </div>
    """, unsafe_allow_html=True)

    features = [
        ("01", "Length matters", "Longer passwords are generally harder to guess."),
        ("02", "Character diversity", "Mix letters, numbers and special characters."),
        ("03", "Avoid patterns", "Predictable sequences reduce security."),
        ("04", "Stay unique", "Never reuse passwords across accounts.")
    ]

    for number, title, desc in features:
        st.markdown(f"""
        <div class="metric-card">
            <span style="color:#8F7BFF;font-size:11px;">{number}</span>
            <div style="font-weight:600;margin-top:5px;">{title}</div>
            <div style="font-size:12px;color:#8995AD;margin-top:5px;">
            {desc}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- RESULTS ----------------

if st.session_state.get("analyzed"):

    password = st.session_state["password"]

    score, strength, color, checks, suggestions = analyze_password(password)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Space Grotesk';font-size:23px;
    font-weight:700;margin-bottom:17px;">
    Security analysis report
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="panel">
            <div class="metric-label">PASSWORD STRENGTH</div>
            <div class="metric-value" style="color:{color};">
            {strength}
            </div>
            <div class="progress-bg">
                <div class="progress-fill"
                style="width:{score}%;background:{color};"></div>
            </div>
            <div style="font-size:12px;color:#8995AD;">
            Security score: {score}/100
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        entropy_pool = (
            (26 if checks["Lowercase"] else 0) +
            (26 if checks["Uppercase"] else 0) +
            (10 if checks["Numbers"] else 0) +
            (32 if checks["Symbols"] else 0)
        )

        entropy = (
            round(len(password) * math.log2(entropy_pool), 1)
            if entropy_pool > 0 else 0
        )

        st.markdown(f"""
        <div class="panel">
            <div class="metric-label">ESTIMATED ENTROPY</div>
            <div class="metric-value">{entropy} bits</div>
            <p style="color:#8995AD;font-size:12px;">
            Approximate theoretical character-space entropy.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    a, b = st.columns(2)

    with a:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">Composition analysis</div>
            <div class="panel-description">
            Password security characteristics
            </div>
        """, unsafe_allow_html=True)

        for name, result in checks.items():
            icon = "✓" if result else "✕"
            css = "good" if result else "bad"

            st.markdown(f"""
            <div class="suggestion">
                <span class="{css}">{icon}</span>
                &nbsp; {name}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">Security recommendations</div>
            <div class="panel-description">
            Actions to improve your password
            </div>
        """, unsafe_allow_html=True)

        if suggestions:
            for suggestion in suggestions:
                st.markdown(f"""
                <div class="suggestion">
                <span style="color:#F6B84B;">→</span>
                &nbsp; {suggestion}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="suggestion good">
            ✓ All basic security checks passed.
            </div>
            <div class="suggestion">
            Consider using a unique, randomly generated password.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    NEXUS SHIELD &nbsp; • &nbsp; BUILT FOR A SAFER DIGITAL WORLD
    <br><br>
    EDUCATIONAL SECURITY TOOL | VERSION 1.0
    <br><br>
    <strong>
        <em class="developer-name">
            Anmol Pandey
        </em>
    </strong>
</div>
""", unsafe_allow_html=True)