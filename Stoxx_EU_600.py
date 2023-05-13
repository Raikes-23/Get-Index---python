import requests
import json

#set API key (necessary que acess information)
api_key = 'API_Key'

#symbol of the index we want to know
symbol = '^STOXX'

#Set API URL
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'

#Comunication with the web
r = requests.get(url)
print(r) #if this value is 200, it works and communication was set

data = json.loads(r.text)

print(data)