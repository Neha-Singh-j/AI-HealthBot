# this file is for streaming data from the model to the app
import streamlit as st
from chatbot.chatbot_logic import predict_disease, top_symptoms

st.set_page_config(page_title="Medical Chatbot", layout="centered")
st.title("🤖 Symptom Checker Chatbot")

with st.expander("🩺 Top Severe Symptoms"):
    st.write(", ".join(top_symptoms()))

user_input = st.text_input("Enter your symptoms (comma-separated)", "")

if st.button("Diagnose"):
    symptoms = [s.strip() for s in user_input.lower().split(',') if s.strip()]
    if symptoms:
        result = predict_disease(symptoms)
        st.subheader("Prediction")
        st.write(f"**Disease:** {result['Disease']}")
        st.write(f"**Description:** {result['Description']}")
        st.write("**Recommended Precautions:**")
        for i, precaution in enumerate(result['Precautions'], 1):
            if precaution:
                st.write(f"{i}. {precaution}")
    else:
        st.warning("Please enter at least one symptom.")
