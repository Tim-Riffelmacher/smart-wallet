import streamlit as st
from utils.Connection import sb_client
import datetime
from utils import Utils
import pandas as pd
import datetime
from components import Inputs
from components.templates.AuthenticatedPage import AuthenticatedPage
from zoneinfo import ZoneInfo
import time

def _render():
    ###
    # OVERVIEW AREA
    ###
    all_transaction_amounts = sb_client.table("transactions").select("amount, created_at").order("created_at", desc=False).execute()
    total_money = 0
    for transaction_amount in all_transaction_amounts.data:
        total_money += transaction_amount["amount"]
    st.subheader(f"Total money: {total_money / 100} $")

    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # FILTER AREA
    ###
    (selected_start_datetime, selected_end_datetime) = Inputs.render_start_end_date_input(datetime.date.today() - datetime.timedelta(days=30), datetime.date.today())

    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # SPENDINGS AREA
    ###
    st.subheader("Spendings")
    spending_area_tabs = st.tabs(["List", "Chart"])
    transactions = sb_client.table("transactions").select("*").gte("created_at", selected_start_datetime).lte("created_at", selected_end_datetime).order("created_at", desc=True).execute()
    with spending_area_tabs[0]:
        ###
        # NEW SPENDING SUBAREA
        ###
        new_spending_area_cols = st.columns([1, 1, 1])
        with new_spending_area_cols[0]:
            amount = st.number_input(label="Amount", step=0.01)
        with new_spending_area_cols[1]:
            reason = st.text_input(label="Reason", max_chars=250)
        with new_spending_area_cols[2]:
            selected_category = st.selectbox("Category", options=["Others", "Grocery", "Salary", "Entertainment", "Health", "Transport", "Insurance"])
        def _add_new_spending():
            sb_client.table("transactions").insert({"amount": int(amount * 100), "reason": None if reason.strip() == "" else reason.strip(), "category": selected_category }).execute()
            st.toast("New spending added", icon="✅")
        st.button("➕ Add", type="primary", use_container_width=True, on_click=_add_new_spending)

        ###
        # ALL SPENDINGS SUBAREA
        ###
        old_transaction_date = None
        for transaction in transactions.data:
            spending_day_divider_cols = st.columns([0.25, 1])
            next_transaction_date = Utils.supabase_timestamp_to_datetime(transaction["created_at"])
            if old_transaction_date == None or old_transaction_date.date() > next_transaction_date.date():
                with spending_day_divider_cols[0]:
                    st.markdown("")
                    st.text(f"{next_transaction_date.strftime('%a, %d %b')}")
                with spending_day_divider_cols[1]:
                    st.divider()
                old_transaction_date = next_transaction_date

            spending_expander = st.expander(f"**{'🟢' if transaction['amount'] >= 0 else '🔴'} {transaction['amount'] / 100}** $ for {transaction['category']} {Utils.map_transaction_category_to_emoji(transaction['category'])}")
            if transaction["reason"] != None:
                spending_expander.caption(transaction["reason"])
            def _remove_spending(_transaction=transaction):
                sb_client.table("transactions").delete().eq("id", _transaction["id"]).execute()
                st.toast("Removed spending", icon="✅")
            spending_expander.button(label="❌ Remove", key=f"key-remove-btn-{transaction['id']}", on_click=_remove_spending)
    with spending_area_tabs[1]:
        if len(all_transaction_amounts.data) != 0:
            total_money_course = pd.DataFrame(all_transaction_amounts.data)
            total_money_course["created_at"] = pd.to_datetime(total_money_course["created_at"]).dt.tz_convert(ZoneInfo(time.tzname[0])).dt.tz_localize(None).dt.tz_localize(datetime.timezone.utc)
            total_money_course.set_index("created_at", inplace=True)
            total_money_course["amount"] = total_money_course["amount"] / 100
            total_money_course["amount"] = total_money_course["amount"].cumsum()
            total_money_course = total_money_course[(total_money_course.index >= pd.to_datetime(selected_start_datetime)) & (total_money_course.index <= pd.to_datetime(selected_end_datetime))]
            total_money_course.rename(columns={ "amount": "Money in $" }, inplace=True)
            st.line_chart(total_money_course, y="Money in $")

AuthenticatedPage("Wallet", "Track your spendings", _render)