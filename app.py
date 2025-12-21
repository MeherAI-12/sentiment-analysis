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

