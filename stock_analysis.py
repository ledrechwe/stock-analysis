import yfinance as yf
import matplotlib.pyplot as plt

# Choose the stock
ticker = "JPM"

# Download one year of JPM stock data
stock = yf.download(ticker, period="1y", auto_adjust=True)

# Get closing prices and remove missing values
close = stock["Close"].dropna()

# Calculate moving averages
ma_50 = close.rolling(window=50).mean()
ma_200 = close.rolling(window=200).mean()

# Get starting and ending prices
starting_price = float(close.iloc[0].iloc[0])
ending_price = float(close.iloc[-1].iloc[0])

# Calculate one-year return
total_return = ((ending_price / starting_price) - 1) * 100

# Print results
print(f"Stock Analysis: {ticker}")
print("-------------------------")
print(f"Starting Price: ${starting_price:.2f}")
print(f"Ending Price: ${ending_price:.2f}")
print(f"1-Year Return: {total_return:.2f}%")

# Create the chart
plt.figure(figsize=(12, 6))

plt.plot(close.index, close, label="Closing Price")
plt.plot(ma_50.index, ma_50, label="50-Day Moving Average")
plt.plot(ma_200.index, ma_200, label="200-Day Moving Average")

plt.title(f"{ticker} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.grid(True)

plt.show()
