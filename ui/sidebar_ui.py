import streamlit as st
from database.chat_operations import delete_conversation, load_conversation_by_id, load_conversations

def show_sidebar_ui():
    st.sidebar.title("📜 Conversation History")

    if st.sidebar.button("➕ New Conversation"):
        st.session_state.current_conversation_id = None
        st.session_state.chat_history = []
        st.rerun()

    if "username" in st.session_state:
        conversations = load_conversations(st.session_state.username)
        if not conversations:
            st.sidebar.info("No conversations found. Start a new one!")
        else:
            for conv in conversations:
                with st.sidebar.expander(f"{conv.get('title', 'Untitled')} - {conv['date']}"):
                    if st.button("Load", key=f"load_{conv['id']}"):
                        conversation = load_conversation_by_id(conv['id'])
                        if conversation:
                            # Assign deserialized messages to chat_history
                            st.session_state.chat_history = conversation["messages"]
                            st.session_state.current_conversation_id = conv['id']
                            st.rerun()
                        else:
                            st.error("Failed to load conversation.")
                    if st.button("Delete", key=f"delete_{conv['id']}"):
                        delete_conversation(conv['id'])
                        st.rerun()