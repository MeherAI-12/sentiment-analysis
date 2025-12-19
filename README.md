# sentiment-analysis

live project : https://sentiment-analysis-ildpbrtjhrm94srmrlmy6b.streamlit.app/

Below is a **clear, standard, and exam/interview-ready description** of your **Streamlit Sentiment Analysis application code**, written in **simple English** so everyone can understand it easily.

---

## 📌 Description of the Sentiment Analysis Streamlit Code

This code implements a **Sentiment Analysis web application** using **Streamlit** and **Hugging Face Transformers**. The application allows users to enter text and automatically determines whether the sentiment expressed in the text is **Positive or Negative**, along with a confidence score.

---

### 1️⃣ Importing Required Libraries

```python
import streamlit as st
from transformers import pipeline
```

* `streamlit` is used to create an interactive web-based user interface.
* `pipeline` from `transformers` loads a pre-trained sentiment analysis model.

---

### 2️⃣ Page Configuration

```python
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="💬",
    layout="centered"
)
```

* Sets the web page title, icon, and layout.
* Makes the application look professional and user-friendly.

---

### 3️⃣ Loading the Sentiment Analysis Model

```python
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")
```

* Loads a pre-trained sentiment analysis model.
* `@st.cache_resource` ensures the model is loaded **only once**, improving performance.

```python
sentiment_model = load_model()
```

* Stores the loaded model for reuse during predictions.

---

### 4️⃣ Application Title and Description

```python
st.title("💬 Sentiment Analysis Application")
st.write(...)
```

* Displays the main title of the app.
* Explains the purpose of the application to the user.

---

### 5️⃣ User Input Section

```python
text_input = st.text_area(...)
```

* Provides a text box for the user to enter a sentence.
* Includes placeholder text for guidance.
* Accepts multi-line input.

---

### 6️⃣ Sentiment Analysis Trigger

```python
if st.button("🔍 Analyze Sentiment"):
```

* Executes sentiment analysis when the button is clicked.
* Prevents automatic execution before user action.

---

### 7️⃣ Input Validation

```python
if text_input.strip() == "":
    st.warning("⚠️ Please enter some text to analyze.")
```

* Checks if the input is empty.
* Displays a warning message if no text is entered.

---

### 8️⃣ Performing Sentiment Prediction

```python
result = sentiment_model(text_input)[0]
```

* Sends user input to the model.
* Returns sentiment label and confidence score.

---

### 9️⃣ Extracting Results

```python
label = result["label"]
score = result["score"]
```

* `label` shows whether the sentiment is **POSITIVE** or **NEGATIVE**.
* `score` indicates the confidence level of the prediction.

---

### 🔟 Displaying Results

```python
if label == "POSITIVE":
    st.success(...)
else:
    st.error(...)
```

* Shows results with visual indicators:

  * Green for positive sentiment 😊
  * Red for negative sentiment 😞
* Improves user experience and clarity.

```python
st.write(f"**Confidence Score:** `{score:.2f}`")
```

* Displays prediction confidence rounded to two decimal places.

---

### 1️⃣1️⃣ Footer Section

```python
st.caption("🚀 Built with Streamlit & Hugging Face Transformers")
```

* Adds a professional footer to the application.

---

## ✅ Summary

* The application uses a **pre-trained NLP model** for sentiment analysis.
* Streamlit provides an **interactive and attractive UI**.
* The code is optimized for **performance, readability, and deployment**.
* Suitable for **academic projects, interviews, and real-world applications**.

---

Sure 👍
Here is the **author attribution** you can use for this project.

---

## 👤 Author Information

**Author Name:** Meher Kamdi

---

### 📌 How to Add It in Your Code (Recommended)

You can include the author name in the **footer section** of your Streamlit app for a professional touch:

```python
st.caption("🚀 Built with Streamlit & Hugging Face Transformers | Author: Meher Kamdi")
```

---

### 📘 Author Line for Project Report / Documentation

> **Author:** Meher Kamdi
>
> This project demonstrates the deployment of a Sentiment Analysis application using Hugging Face Transformers and Streamlit, enabling users to analyze textual sentiment in an interactive web interface.

---

### 🎓 Author Line for Academic Submission

> **Developed by:** Meher Kamdi
>
> **Technology Used:** Python, Streamlit, Hugging Face Transformers
>
> **Application:** Sentiment Analysis using Natural Language Processing (NLP)





