# streamlit_app.py
# An optional Streamlit web application for the Text Summarizer!

import streamlit as st
from transformers import pipeline

# We use st.cache_resource so that the model is only loaded ONCE 
# when the app starts, rather than every time the user clicks a button.
@st.cache_resource
def load_summarizer():
    return pipeline("summarization")

st.title("📝 AI Text Summarizer")
st.write("Welcome to your first LLM app! Paste a long article below and the AI will summarize it for you.")

# Load the model and show a spinner while it loads
with st.spinner("Loading AI model..."):
    summarizer = load_summarizer()

# Create a text area for the user to paste their content
user_input = st.text_area("Enter your text here:", height=200)

# Create a button to trigger the summarization
if st.button("Summarize!"):
    if len(user_input.strip()) > 0:
        with st.spinner("Generating summary..."):
            try:
                # Generate the summary
                summary_result = summarizer(user_input, max_length=60, min_length=15, do_sample=False)
                summary = summary_result[0]["summary_text"]
                
                # Display it nicely
                st.success("Summary Generated!")
                st.write(summary)
            except Exception as e:
                st.error(f"Error generating summary. Make sure the text is long enough! Details: {e}")
    else:
        st.warning("Please enter some text first.")
