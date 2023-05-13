#necessary libraries
import requests
import json

def get_stoxx600_index(api_key):
    symbol='STOXX'
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if "Global Quote" in data:
        stoxx600_index = data["Global Quote"]["05. price"]
        return stoxx600_index
    else:
        return None

api_key = "NT8JWQKCAEKFXBEF"  # replace with your actual API key
stoxx600_index = get_stoxx600_index(api_key)
print(stoxx600_index)