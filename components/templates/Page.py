import streamlit as st

def Page(title, sidebar_title, render):
    ###
    # HEADER & METADATA
    ###
    st.title(title)
    st.sidebar.title(sidebar_title)
    render()