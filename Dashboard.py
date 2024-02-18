import streamlit as st
from components.templates.Page import Page

def _render():
    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # DASHBOARD AREA
    ###
    dashboard_area_cols = st.columns([1, 1, 1, 1])
    with dashboard_area_cols[0]:
        st.subheader("🚀 Stocks")
        st.page_link("pages/1_🚀_Stocks.py", label="⏵ Investigate", use_container_width=True)
    with dashboard_area_cols[1]:
        st.subheader("💰 Wallet")
        st.page_link("pages/2_💰_Wallet.py", label="⏵ Check out", use_container_width=True)
    with dashboard_area_cols[2]:
        st.subheader("🌍 Network")
        st.page_link("pages/3_🌍_Network.py", label="⏵ Chat", use_container_width=True)
    with dashboard_area_cols[3]:
        st.subheader("👤 Profile")
        st.page_link("pages/4_👤_Profile.py", label="⏵ Configure", use_container_width=True)

    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # OTHERS AREA
    ###
    others_area_cols = st.columns([1, 1, 1, 1])
    with others_area_cols[0]:
        st.subheader("📘 Docs")
        st.page_link("https://github.com/Tim-Riffelmacher/Pathing-Sandbox/blob/master/README.md", label="⏵ Read", use_container_width=True)

Page("Dashboard", "Navigate to all pages", _render)