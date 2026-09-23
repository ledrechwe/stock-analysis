import yfinance as yf
import matplotlib.pyplot as plt

# Stock we want to analyze
ticker = "JPM"

# Download the last year of stock data
stock = yf.download(ticker, period="1y")

# Calculate daily returns
stock["Daily Return"] = stock["Close"].pct_change()

# Calculate moving averages
stock["50 Day MA"] = stock["Close"].rolling(window=50).mean()
stock["200 Day MA"] = stock["Close"].rolling(window=200).mean()

# Display basic information
print(f"Stock Analysis: {ticker}")
print("-------------------------")
print(f"Starting Price: ${stock['Close'].iloc[0].item():.2f}")
print(f"Ending Price: ${stock['Close'].iloc[-1].item():.2f}")

total_return = (
    (stock["Close"].iloc[-1].item() / stock["Close"].iloc[0].item()) - 1
) * 100

print(f"1-Year Return: {total_return:.2f}%")

# Create stock price chart
plt.figure(figsize=(12, 6))

plt.plot(stock.index, stock["Close"], label="Closing Price")
plt.plot(stock.index, stock["50 Day MA"], label="50-Day Moving Average")
plt.plot(stock.index, stock["200 Day MA"], label="200-Day Moving Average")

plt.title(f"{ticker} Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.grid(True)

plt.show()
