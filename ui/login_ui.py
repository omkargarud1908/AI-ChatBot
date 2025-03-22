import streamlit as st
from auth.auth_utils import handle_login, handle_signup

def show_login_ui():
    st.title("🔐 Login or Signup")
    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            if handle_login(login_username, login_password):
                st.session_state.logged_in = True
                st.session_state.username = login_username
                st.success("✅ Login successful! Redirecting...")
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    with tab2:
        signup_username = st.text_input("Choose a Username", key="signup_username")
        signup_password = st.text_input("Choose a Password", type="password", key="signup_password")
        if st.button("Signup"):
            if handle_signup(signup_username, signup_password):
                st.success("✅ Signup successful! Please login.")
            else:
                st.error("❌ Username already taken. Try another one.")