import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('AAPL','2020-01-01','2023-01-01')

print(data)


data.Close.plot()
plt.show()

    def calculate_returns(ticker, investment, purchase_date, sell_date):
        data = yf.download(ticker, purchase_date, sell_date)
        purchase_price = data.iloc[0]['Close']
        sell_price = data.iloc[-1]['Close']

        shares_bought = investment / purchase_price
        investment_value = shares_bought * sell_price

        return investment_value

    #This function downloads the data and tracks the returns. Number of shares can be found by a basic division.git status -s main.py



