def map_transaction_category_to_emoji(category = None):
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
    mappings = {
        "Open": "Price in $ (Open)",
        "High": "Price in $ (High)",
        "Low": "Price in $ (Low)",
        "Close": "Price in $ (Close)"
    }
    if aggregation == None:
        return mappings
    return mappings[aggregation]