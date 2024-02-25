import datetime

def map_transaction_category_to_emoji(category = None):
    """
    Maps the given transaction category to the corresponding emoji.
    If no category is provided the whole map is returned.
    """
    mappings = {
        "Others": "❔",
        "Grocery": "🥑",
        "Salary": "💶",
        "Entertainment": "📱",
        "Health": "🏥",
        "Transport": "🚗",
        "Insurance": "🛟"
    }
    if category == None:
        return mappings
    return mappings[category]

def map_ticker_to_company_name(ticker = None):
    """
    Maps the given ticker to the corresponding company name.
    If no ticker is provided the whole map is returned.
    """
    mappings = {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "WMT": "Walmart",
        "SAP": "SAP",
        "IBM": "IBM"
    }
    if ticker == None:
        return mappings
    return mappings[ticker]

def map_aggregation_to_label(aggregation = None):
    """
    Maps the aggregation type to the corresponding label.
    If no aggregation is provided the whole map is returned.
    """
    mappings = {
        "Open": "Price in $ (Open)",
        "High": "Price in $ (High)",
        "Low": "Price in $ (Low)",
        "Close": "Price in $ (Close)"
    }
    if aggregation == None:
        return mappings
    return mappings[aggregation]

def supabase_timestamp_to_datetime(timestamp):
    """
    Converts timestamp recieved from supabase into usable datetime object.
    """
    return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f+00:00").replace(tzinfo=datetime.timezone.utc)