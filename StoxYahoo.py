import yfinance as yf

def get_stoxx600_index():
    # Define the ticker symbol
    tickerSymbol = 'STOXX50E.FGI'

    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d')

    # Get the latest Close price
    latest_close_price = tickerDf['Close'][0]

    return latest_close_price

stoxx600_index = get_stoxx600_index()
print(stoxx600_index)