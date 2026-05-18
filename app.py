import streamlit as st
from transformers import pipeline

st.title("Basic AI Chatbot")
st.write("Ask anything below")

# Load AI model
chatbot = pipeline("text-generation", model="gpt2")

user_input = st.text_input("Enter your question")

if st.button("Generate"):
    if user_input:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        st.write(response[0]['generated_text'])