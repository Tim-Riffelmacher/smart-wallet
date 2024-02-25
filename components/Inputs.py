import datetime
import streamlit as st
from zoneinfo import ZoneInfo
import time

def render_date_input(label, default_date, combined_time):
    """
    Renders date input field with the given label, default date and combined time.
    The combined time is attached to the selected date, 
    such that datetime is returned instead of only date type.
    """
    return datetime.datetime.combine(st.date_input(label, default_date), combined_time, ZoneInfo(time.tzname[0])).astimezone(datetime.timezone.utc)

def render_start_end_date_input(default_start_date, default_end_date):
    """
    Renders a date interval input field with the given default start and end date.
    Returns datetime instead of only date type.
    """
    date_input_cols = st.columns([1, 1])
    with date_input_cols[0]:
        selected_start_datetime = render_date_input("Start date", default_start_date, datetime.datetime.min.time())
    with date_input_cols[1]:
        selected_end_datetime = render_date_input("End date", default_end_date, datetime.datetime.max.time())
    return (selected_start_datetime, selected_end_datetime)
