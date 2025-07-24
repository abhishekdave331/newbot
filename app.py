import streamlit as st

# Page config
st.set_page_config(page_title="Google Chatbot", page_icon="🤖")
st.title("🤖 Google Chatbot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
prompt = st.chat_input("Ask me anything...")

# Dummy response logic (replace with actual model call)
def get_bot_response(user_input):
    return f"You said: {user_input}"

# When user sends a message
if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and show bot response
    response = get_bot_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
