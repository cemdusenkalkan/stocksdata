import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('AAPL','2020-01-01','2023-01-01')

print(data)


data.Close.plot()
plt.show()

