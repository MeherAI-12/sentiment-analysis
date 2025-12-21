import streamlit as st
from transformers import pipeline
# -------------------------------
# Custom CSS for Better UI
# -------------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(to right, #f8fbff, #eef2f7);
}

/* Title styling */
h1 {
    color: #1f4fd8;
    text-align: center;
    font-weight: 700;
}

/* Text area styling */
textarea {
    border-radius: 12px !important;
    border: 1px solid #d0d7e2 !important;
    font-size: 16px !important;
}

/* Button styling */
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
    color: white;
}

/* Result boxes */
.stSuccess {
    background-color: #e6fffa;
    border-left: 6px solid #00b894;
}

.stError {
    background-color: #ffeaea;
    border-left: 6px solid #d63031;
}

/* Footer */
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered"
)

# -------------------------------
# Load Sentiment Model
# -------------------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_model = load_model()

# -------------------------------
# App Title & Description
# -------------------------------
st.title("💬 Sentiment Analysis Application")
st.write(
    """
    This application uses **Hugging Face Transformers** to analyze the  
    **sentiment of a given text** and classify it as **Positive or Negative**.
    """
)

st.divider()

# -------------------------------
# User Input
# -------------------------------
text_input = st.text_area(
    "✍️ Enter your text below:",
    placeholder="Example: I don't like the game",
    height=120
)

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🔍 Analyze Sentiment"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        result = sentiment_model(text_input)[0]

        label = result["label"]
        score = result["score"]

        # -------------------------------
        # Display Result
        # -------------------------------
        st.subheader("📊 Analysis Result")

        if label == "POSITIVE":
            st.success(f"😊 **Sentiment:** {label}")
        else:
            st.error(f"😞 **Sentiment:** {label}")

        st.write(f"**Confidence Score:** `{score:.2f}`")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.caption("🚀 Built with Streamlit & Hugging Face Transformers | Author: Meher Kamdi")

