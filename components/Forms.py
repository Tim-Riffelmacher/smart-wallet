import streamlit as st
from utils.Connection import sb_client

def render_login_register_form():
    if sb_client.auth.get_session() != None:
        return

    if "show_login_form" not in st.session_state:
        st.session_state["show_login_form"] = True

    st.markdown(f"<span style='display: flex; justify-content: center; font-size: 2rem; margin-top: 6rem;'>You need to {'login' if st.session_state['show_login_form'] else 'register'} to access this page 🔒</span>", unsafe_allow_html=True)

    def _show_login_form(show):
        st.session_state["show_login_form"] = show
    login_area_columns = st.columns([1, 1, 1])
    with login_area_columns[1]:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        st.text("") 
        if st.session_state["show_login_form"]:
            def _login():
                try:
                    sb_client.auth.sign_in_with_password({
                        "email": email,
                        "password": password,
                    })
                except Exception:
                    st.toast("The credentials are incorrect", icon="❌")
            st.button("Login", type="primary", use_container_width=True, on_click=_login)
            st.button("No account yet?", use_container_width=True, on_click=_show_login_form, args=(False,))
        else:
            def _register():
                try:
                    sb_client.auth.sign_up({
                        "email": email,
                        "password": password,
                    })
                except Exception:
                    st.toast("Your email needs to be valid and your password must contain at least 6 characters", icon="❌")
            st.button("Register", type="primary", use_container_width=True, on_click=_register)
            st.button("Already have an account?", use_container_width=True, on_click=_show_login_form, args=(True,))
    
    st.stop()