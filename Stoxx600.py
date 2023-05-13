import requests
import json

# Function to retrieve stock data for a given symbol
def get_stock_data(api_key, symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if "Global Quote" in data:
        return data["Global Quote"]
    else:
        return None

# Function to calculate the STOXX 600 index value
def calculate_stoxx600_index(api_key, constituent_stocks):
    total_weight = 0
    index_value = 0

    for stock in constituent_stocks:
        stock_data = get_stock_data(api_key, stock["symbol"])
        
        if stock_data:
            price = float(stock_data["05. price"])
            weight = float(stock["weight"])
            total_weight += weight
            index_value += price * weight
    
    if total_weight > 0:
        index_value /= total_weight
    
    return index_value

# Replace with your Alpha Vantage API key
api_key = "NT8JWQKCAEKFXBEF"

# Replace with the constituent stocks and their weights in the STOXX 600 index
constituent_stocks = [
    {"symbol": "STOCK1", "weight": 0.3},
    {"symbol": "STOCK2", "weight": 0.5},
    {"symbol": "STOCK3", "weight": 0.2},
]

stoxx600_index = calculate_stoxx600_index(api_key, constituent_stocks)
print(stoxx600_index)