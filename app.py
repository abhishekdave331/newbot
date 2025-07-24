import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page setup
st.set_page_config(page_title="Google Chatbot", page_icon="🤖")
st.title("🤖 Google Chatbot")

# Initialize chat memory (Gemini chat model session)
if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel("gemini-1.5-flash").start_chat(history=[])

# Show chat history
for msg in st.session_state.chat.history:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        st.markdown(msg.parts[0].text)

# Input box
prompt = st.chat_input("Ask me anything...")

# If prompt is entered
if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to Gemini and get response
    response = st.session_state.chat.send_message(prompt)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response.text)
