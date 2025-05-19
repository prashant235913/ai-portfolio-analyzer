import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_generator import generate_feedback

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Resume Text")
    st.write(text)

    st.subheader("AI Feedback")
    feedback = generate_feedback(text)
    st.write(feedback)
