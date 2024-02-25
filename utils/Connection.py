import streamlit as st
from supabase import create_client

@st.cache_resource
def init_connection():
    """
    Sets up connection to Supabase.
    Therefore it uses the credentials provided by Streamlit environment.
    """
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

sb_client = init_connection()
