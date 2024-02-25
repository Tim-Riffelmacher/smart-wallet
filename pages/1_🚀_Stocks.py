import streamlit as st
import yfinance as yf
import datetime
from components.templates.Page import Page
from utils.Utils import map_ticker_to_company_name, map_aggregation_to_label
from components.Inputs import render_start_end_date_input

def _render():
    ###
    # SEARCH AREA
    ###
    search_area_cols = st.columns([1, 1])
    with search_area_cols[0]:
        selected_ticker_name = st.selectbox(
            "Ticker",
            ("AAPL", "MSFT", "WMT", "SAP", "IBM"))
    with search_area_cols[1]:
        st.caption("Company Name")
        st.markdown(f"**{map_ticker_to_company_name(selected_ticker_name)}**")

    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # INFO AREA
    ###
    st.subheader("Info")
    selected_ticker = yf.Ticker(selected_ticker_name)
    info_area_cols = st.columns([1, 1])
    with info_area_cols[0]:
        st.caption("Identification")
        st.write(f"ISIN: **{selected_ticker.isin}**")
    with info_area_cols[1]:
        st.caption("Link")
        st.write(f"Website: **{selected_ticker.info['website']}**")

    info_area_cols = st.columns([1, 1])
    with info_area_cols[0]:
        st.caption("Location")
        st.write(f"Address: **{selected_ticker.info['address1']}**")
        st.write(f"City: **{selected_ticker.info['city']}** (**{selected_ticker.info['zip']}**)")
        st.write(f"State: **{selected_ticker.info['state'] if 'state' in selected_ticker.info else '-'}**")
        st.write(f"Country: **{selected_ticker.info['country']}**")
    with info_area_cols[1]:
        st.caption("Sector")
        st.write(f"Sector: **{selected_ticker.info['sector']}**")
        st.write(f"Industry: **{selected_ticker.info['industry']}**")


    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # MARKET AREA
    ###
    st.subheader("Market")

    ###
    # FILTER SUBAREA
    ###
    st.caption("Filter")
    filter_area_cols = st.columns([0.5, 1])
    with filter_area_cols[0]:
        selected_agg_method = filter_area_cols[0].selectbox(
            'Aggregation',
            ('Open', 'High', 'Low', 'Close'))
    with filter_area_cols[1]:
        (selected_start_date, selected_end_date) = render_start_end_date_input(datetime.datetime.today() - datetime.timedelta(days=30), datetime.datetime.today())

    ###
    # TRENDS SUBAREA
    ###
    st.caption("Trends")
    finance_data = selected_ticker.history(start=selected_start_date, end=selected_end_date)
    trend_option_cols = st.columns([0.1, 1])
    with trend_option_cols[0]:
        st.caption("⏵ Option:")
    with trend_option_cols[1]:
        trends_in_percentage = st.toggle("In %", False)
    if trends_in_percentage:
        perfomance_delta = (finance_data.iloc[len(finance_data.index) - 1][selected_agg_method] / finance_data.iloc[0][selected_agg_method] - 1) * 100
        traded_volume_delta = (finance_data.iloc[len(finance_data.index) - 1]['Volume'] / finance_data.iloc[0]['Volume'] - 1) * 100
    else:
        perfomance_delta = finance_data.iloc[len(finance_data.index) - 1][selected_agg_method] - finance_data.iloc[0][selected_agg_method]
        traded_volume_delta = finance_data.iloc[len(finance_data.index) - 1]['Volume'] - finance_data.iloc[0]['Volume']
    trend_cols = st.columns([1, 1])
    with trend_cols[0]:
        st.metric(label="Performance", value=f"{round(finance_data.iloc[0][selected_agg_method], 2)} $", delta=f"{round(perfomance_delta, 2)} {'%' if trends_in_percentage else '$'}")
    with trend_cols[1]:
        st.metric(label="Traded volume", value=f"{round(finance_data.iloc[0]['Volume'], 2)} $", delta=f"{round(traded_volume_delta, 2)} {'%' if trends_in_percentage else '$'}")

    ###
    # CHARTS SUBAREA
    ###
    st.caption("Stocks")
    chart_subarea_tabs = st.tabs(["Chart", "Table"])    
    with chart_subarea_tabs[0]:
        finance_data_for_chart = finance_data.copy()
        chart_option_cols = st.columns([0.1, 1])
        with chart_option_cols[0]:
            st.caption("⏵ Option:")
        with chart_option_cols[1]:
            if st.toggle("To baseline", True):
                for col in finance_data_for_chart.columns:
                    finance_data_for_chart[col] = finance_data_for_chart[col] - finance_data_for_chart.iloc[0][col]
        finance_data_for_chart.rename(columns=map_aggregation_to_label(), inplace=True)
        st.line_chart(finance_data_for_chart, y=map_aggregation_to_label(selected_agg_method))
    with chart_subarea_tabs[1]:
        st.write(finance_data)

    ###
    # DIVIDER
    ###
    st.divider()

    ###
    # NEWS AREA
    ###
    st.subheader("News")
    for news in selected_ticker.news:
        news_cols = st.columns([1, 1, 1])
        with news_cols[0]:
            if "thumbnail" in news:
                st.image(news['thumbnail']['resolutions'][0]["url"], width=150)
        with news_cols[1]:
            st.write(news['title'])
            st.write(f'by {news["publisher"]}')
        with news_cols[2]:
            st.write(news["link"])

Page("Stocks", "Get latest stock news", _render)