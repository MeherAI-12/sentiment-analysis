import streamlit as st
from transformers import pipeline

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered"
)

# -------------------------------
# Custom CSS for Better UI
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f8fbff, #eef2f7);
}

h1 {
    color: #1f4fd8;
    text-align: center;
    font-weight: 700;
}

textarea {
    border-radius: 12px !important;
    border: 1px solid #d0d7e2 !important;
    font-size: 16px !important;
}

.stButton>button {
    background-color: #1f4fd8;
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #163bbf;
}

.stSuccess {
    background-color: #e6fffa;
    border-left: 6px solid #00b894;
}

.stError {
    background-color: #ffeaea;
    border-left: 6px solid #d63031;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Sentiment Model
# -------------------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_model = load_model()

# -------------------------------
# Header Card
# -------------------------------
st.markdown("""
<div style="
    background-color:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-align:center;
">
    <h2>💬 Sentiment Analysis Application</h2>
    <p style="font-size:16px;">
        Analyze text sentiment using <b>Hugging Face Transformers</b>
    </p>
    <p style="font-size:14px; color:gray;">
        Author: <b>Meher Kamdi</b>
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------
# User Input
# -------------------------------
text_input = st.text_area(
    "✍️ Enter your text below:",
    placeholder="Example: I don't like the game",
    height=120
)

# -------------------------------
# Centered Button
# -------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze = st.button("🔍 Analyze Sentiment")

# -------------------------------
# Sentiment Analysis Logic
# -------------------------------
if analyze:
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        result = sentiment_model(text_input)[0]
        label = result["label"]
        score = result["score"]

        st.subheader("📊 Sentiment Result")

        if label == "POSITIVE":
            st.success(f"😊 **Positive Sentiment**\n\nConfidence: `{score:.2f}`")
        else:
            st.error(f"😞 **Negative Sentiment**\n\nConfidence: `{score:.2f}`")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.caption("🚀 Built with Streamlit & Hugging Face Transformers | Author: Meher Kamdi")
