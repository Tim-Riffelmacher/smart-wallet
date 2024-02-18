import streamlit as st
from components.templates.AuthenticatedPage import AuthenticatedPage
from streamlit_app import sb_client

def _render():
    ###
    # INPUT AREA
    ###
    input_area_cols = st.columns([1, 1, 1])
    with input_area_cols[1]:
        st.text_input("Email", sb_client.auth.get_user().user.email, disabled=True)
        profile = sb_client.table("profiles").select("*").eq("fk_user_id", sb_client.auth.get_user().user.id).execute()
        
        first_name = st.text_input("First name", max_chars=50, value="" if len(profile.data) == 0 else profile.data[0]["first_name"])
        last_name = st.text_input("Last name", max_chars=50, value="" if len(profile.data) == 0 else profile.data[0]["last_name"])

        def _save_profile():
            profile_data = {
                "first_name": None if first_name.strip() == "" else first_name.strip(), 
                "last_name": None if last_name.strip() == "" else last_name.strip(),
            }
            if len(profile.data) != 0:
                profile_data["id"] = profile.data[0]["id"]
            sb_client.table("profiles").upsert(profile_data).execute()
            st.toast("Profile updated", icon="✅")
        def _is_save_btn_disabled():
            if len(profile.data) == 0:
                return first_name == "" and last_name == ""
            else:
                return first_name == profile.data[0]["first_name"] and last_name == profile.data[0]["last_name"]
        st.button("Save", type="primary", on_click=_save_profile, use_container_width=True, disabled=_is_save_btn_disabled())

AuthenticatedPage("Profile", "Configure your public profile", _render)
