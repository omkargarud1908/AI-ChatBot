import streamlit as st
from ui.login_ui import show_login_ui
from ui.chat_ui import show_chat_ui
from ui.sidebar_ui import show_sidebar_ui
from database.db_connection import initialize_database

# Initialize database
initialize_database()

# Streamlit Page Configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "current_conversation_id" not in st.session_state:
    st.session_state.current_conversation_id = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "history_data" not in st.session_state:
    st.session_state.history_data = {"conversations": []}

# Show Login UI if not logged in
if not st.session_state.logged_in:
    show_login_ui()
    st.stop()

# Show Chat UI and Sidebar if logged in
show_sidebar_ui()
show_chat_ui()