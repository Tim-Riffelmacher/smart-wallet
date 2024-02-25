import streamlit as st

def Page(title, sidebar_title, render):
    """
    Builds a normal page with the given title, sidebar title and render callback.
    """
    ###
    # HEADER & METADATA
    ###
    st.title(title)
    st.sidebar.title(sidebar_title)
    render()