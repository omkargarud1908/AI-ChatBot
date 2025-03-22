import streamlit as st
import uuid
import json
from datetime import datetime
from api.mistral_api import get_mistral_response
from database.chat_operations import save_conversation

def show_chat_ui():
    st.title("🤖 AI Chatbot")
    st.markdown("Ask me anything!")

    # Prebuilt Questions Section (Leave this untouched)
    st.subheader("Quick Questions")
    prebuilt_questions = [
        "What are the top IT careers in 2025?",
        "How do I start a career in AI and Machine Learning?",
        "What programming languages should I learn for web development?",
        "How to prepare for technical interviews?",
        "What are the latest trends in software development?",
    ]

    # Display prebuilt questions in columns (Leave this untouched)
    cols = st.columns(len(prebuilt_questions))
    for i, question in enumerate(prebuilt_questions):
        if cols[i].button(question):
            # Simulate user input with the prebuilt question
            handle_user_query(question)

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Debug: Print the chat history structure
    print("DEBUG: chat_history structure ->", st.session_state.chat_history)

    if not isinstance(st.session_state.chat_history, list):
        try:
            st.session_state.chat_history = json.loads(st.session_state.chat_history)
        except:
            st.session_state.chat_history = []
            
    # Display chat history
    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            if isinstance(message, dict) and "role" in message and "content" in message:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            else:
                st.error(f"Invalid message format: {message}")
    else:
        st.info("No chat history available. Start a new conversation!")

    # Handle user input
    user_query = st.chat_input("Type your question here...")
    if user_query:
        handle_user_query(user_query)

def handle_user_query(user_query):
    """Handle user queries (both manual input and prebuilt questions)"""
    # Generate a new conversation ID if none exists
    if not st.session_state.current_conversation_id:
        st.session_state.current_conversation_id = str(uuid.uuid4())
        print("DEBUG: Generated new conversation ID ->", st.session_state.current_conversation_id)

    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = get_mistral_response(st.session_state.chat_history)
            st.write(response)

    # Add AI response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Save conversation
    conversation = {
        "id": st.session_state.current_conversation_id,
        "username": st.session_state.username,
        "title": user_query[:30] + ("..." if len(user_query) > 30 else ""),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": json.dumps(st.session_state.chat_history)  # Serialize to JSON string
    }
    print("DEBUG: Saving conversation ->", conversation)  # Debugging line
    save_conversation(conversation)
    st.toast("Conversation saved!")