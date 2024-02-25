import streamlit as st
from utils.Connection import sb_client
from components.templates.AuthenticatedPage import AuthenticatedPage
from utils.Connection import sb_client
from utils import Utils
from zoneinfo import ZoneInfo
import time
import pytz

def _render():
    ask_area_cols = st.columns([0.1, 0.3, 1, 0.2])
    with ask_area_cols[0]:
        st.caption("Channel")
    with ask_area_cols[1]:
        selected_channel = st.selectbox("", options=["Stocks", "News", "Investments", "Crypto", "Resources"], label_visibility="collapsed")
        st.session_state["selected_channel"] = selected_channel
    with ask_area_cols[2]:
        content = st.text_input("", placeholder="Write something about finances", max_chars=1000, label_visibility="collapsed")
    with ask_area_cols[3]:
        def _send_messsage():
            sb_client.table("messages").insert({
                "content": content,
                "channel": selected_channel
            }).execute()
        st.button("Send", type="primary", on_click=_send_messsage)

    ###
    # CHAT AREA
    ###
    chat_area_tabs = st.tabs(["Chat", "Saved messages"])
    saved_message_refs = sb_client.table("saved_messages").select("*").execute()
    mapped_saved_message_refs = { saved_message["fk_message_id"] for saved_message in saved_message_refs.data }
    with chat_area_tabs[0]:
        refresh_btn_cols = st.columns([1, 0.5, 1])
        with refresh_btn_cols[1]:
            def _refresh_page():
                st.session_state["latest_messages"] = sb_client.table("messages").select("*").eq("channel", selected_channel).order("created_at", desc=True).limit(7).execute()
            st.button("🆕 Refresh", on_click=_refresh_page, use_container_width=True)

        st.session_state["latest_messages"] = sb_client.table("messages").select("*").eq("channel", selected_channel).order("created_at", desc=True).limit(7).execute()
        message_counter = 0
        for latest_message in st.session_state["latest_messages"].data:
            message_counter += 1
            if message_counter >= 7:
                st.text("...")
                break

            chat_message = st.chat_message("user")
            chat_message_cols = chat_message.columns([0.025, 1, 0.15])
            with chat_message_cols[1]:
                st.write(latest_message["content"])
                def _toggle_saved_message(_latest_message=latest_message):
                    if _latest_message["id"] in mapped_saved_message_refs:
                        sb_client.table("saved_messages").delete().eq("fk_message_id", _latest_message["id"]).execute()
                        st.toast("Removed from saved messages", icon="✅")
                    else:
                        sb_client.table("saved_messages").insert({ "fk_message_id": _latest_message["id"] }).execute()
                        st.toast("Message saved", icon="✅")
                chat_message_action_cols = st.columns([0.1, 1])
                with chat_message_action_cols[0]:
                    st.button("★" if (latest_message["id"] in mapped_saved_message_refs) else "✩", on_click=_toggle_saved_message, key=f"key-save-btn-0-${latest_message['id']}")
                with chat_message_action_cols[1]:
                    if latest_message["fk_user_id"] == sb_client.auth.get_user().user.id:
                        def _remove_message(_latest_message=latest_message):
                            sb_client.table("messages").delete().eq("id", _latest_message["id"]).execute()
                            st.toast("Removed message from chat", icon="✅")
                        st.button("❌ Remove", on_click=_remove_message, key=f"key-remove-btn-${latest_message['id']}")
            with chat_message_cols[2]:
                st.text(Utils.supabase_timestamp_to_datetime(latest_message['created_at']).astimezone(ZoneInfo(time.tzname[0])).strftime('%H::%M'))
                profiles = sb_client.table("profiles").select("first_name").eq("fk_user_id", latest_message["fk_user_id"]).execute()
                if len(profiles.data) != 0:
                    st.text(f"({profiles.data[0]['first_name']})")
                else:
                    st.text("(Unknown)")
    with chat_area_tabs[1]:
        saved_messages = sb_client.table("messages").select("*").in_("id", mapped_saved_message_refs).eq("channel", selected_channel).order("created_at", desc=True).execute()
        for saved_message in saved_messages.data:
            chat_message = st.chat_message("user")
            chat_message_cols = chat_message.columns([0.025, 1, 0.1])
            with chat_message_cols[1]:
                st.write(saved_message["content"])
                def _remove_saved_message(_saved_message=saved_message):
                    sb_client.table("saved_messages").delete().eq("fk_message_id", _saved_message["id"]).execute()
                    st.toast("Removed from saved messages", icon="✅")
                st.button("❌ Remove", on_click=_remove_saved_message, key=f"key-save-btn-1-${saved_message['id']}")
            with chat_message_cols[2]:
                st.text(Utils.supabase_timestamp_to_datetime(saved_message['created_at']).astimezone(ZoneInfo(time.tzname[0])).strftime('%H:%M'))

AuthenticatedPage("Network", "Ask the globe about finances", _render)
