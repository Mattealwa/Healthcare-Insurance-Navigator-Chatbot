import streamlit as st
from gemini import model, insurance_data

st.set_page_config(page_title="Health Insurance Chatbot", page_icon="🩺", layout="centered")

st.title("🩺 Health Insurance Chatbot")
st.markdown("Let's find the best insurance plan for you!")

# User input fields
age = st.number_input("Your Age", min_value=0, max_value=120, step=1)
condition = st.text_input("Medical Conditions", placeholder="e.g. diabetes")
budget = st.number_input("Monthly Budget (₹)", min_value=100, max_value=10000, step=100)

if st.button("Find Best Plan"):
    if age and condition and budget:
        prompt = f"""
You're a health insurance expert chatbot.
Based on the following data: {insurance_data},
recommend the best plan for a {age}-year-old with {condition}, under ₹{budget}/month.
Be detailed, compare if needed, and make it beginner-friendly.
"""
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
        st.subheader("✨ Recommended Plan")
        st.markdown(response.text)
    else:
        st.warning("Please fill out all fields.")
