import streamlit as st
from utils.Connection import sb_client
import asyncio

def AuthenticatedPage(title, sidebar_title, render, rerender = None, rerender_timeout = 5):
    """
    Builds an authenticated page with the given title, sidebar title and render callback.
    If the user is not logged in it shows the login/register form instead of the actual page.
    A rerender callback can also be specified that is called every x seconds according to the rerender timeout.
    It indicates whether the page should be reloaded due to new data available.
    """
    ###
    # HEADER & METADATA
    ###
    st.title(title)
    st.sidebar.title(sidebar_title)

    if sb_client.auth.get_session() == None:
        ###
        # LOGIN & REGISTER AREA
        ###
        if "show_login_form" not in st.session_state:
            st.session_state["show_login_form"] = True

        st.markdown(f"<span style='display: flex; justify-content: center; font-size: 2rem; margin-top: 5rem;'>You need to {'login' if st.session_state['show_login_form'] else 'register'} to access this page 🔒</span>", unsafe_allow_html=True)

        def _show_login_form(show):
            st.session_state["show_login_form"] = show
        login_area_columns = st.columns([1, 1, 1])
        with login_area_columns[1]:
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            st.markdown("") 
            if st.session_state["show_login_form"]:
                def _login():
                    try:
                        sb_client.auth.sign_in_with_password({
                            "email": email,
                            "password": password,
                        })
                        st.toast("You are logged in now", icon="✅")
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
                        st.toast("You are registered now", icon="✅")
                        _show_login_form(True)
                    except Exception:
                        st.toast("Your email needs to be valid and your password must contain at least 6 characters", icon="❌")
                st.button("Register", type="primary", use_container_width=True, on_click=_register)
                st.button("Already have an account?", use_container_width=True, on_click=_show_login_form, args=(True,))
    else:
        ###
        # PAGE AREA
        ###
        render()

        ###
        # DIVDER
        ###
        st.divider()
        
        ###
        # LOGOUT AREA
        ###
        st.button("Logout", on_click=lambda: sb_client.auth.sign_out())

    if rerender != None:
        async def _rerender_wrapper():
            while True:
                if rerender():
                    st.rerun()
                await asyncio.sleep(rerender_timeout)
        asyncio.run(_rerender_wrapper())