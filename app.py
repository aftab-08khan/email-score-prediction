import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model/email_category_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

def predict_category(email_text):
    X = vectorizer.transform([email_text])
    prediction = model.predict(X)
    return prediction[0]

# Set page configuration
st.set_page_config(page_title="Email Description Category Predictor", page_icon="📧", layout="centered")

# Title for the app
st.title("Email Description Category Predictor")

# Input area for email description
email_description = st.text_area("Enter Email Description:", height=200)

# Button to trigger the prediction
if st.button("Check Category"):
    if email_description:
        category = predict_category(email_description)
        if category == 1:
            st.success("📌 Predicted Category: **Valid**")
        else:
            st.error("📌 Predicted Category: **Not Valid**")
    else:
        st.warning("Please enter an email description to check.")
