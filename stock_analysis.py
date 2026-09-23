import yfinance as yf
import matplotlib.pyplot as plt

# Choose stock and benchmark
ticker = "JPM"
benchmark = "^GSPC"  # S&P 500

# Download one year of data
stock = yf.download(ticker, period="1y", auto_adjust=True)
sp500 = yf.download(benchmark, period="1y", auto_adjust=True)

# Get closing prices
close = stock["Close"].dropna()
sp500_close = sp500["Close"].dropna()

# Calculate moving averages
ma_50 = close.rolling(window=50).mean()
ma_200 = close.rolling(window=200).mean()

# Starting and ending prices
starting_price = float(close.iloc[0].iloc[0])
ending_price = float(close.iloc[-1].iloc[0])

# JPM return
total_return = ((ending_price / starting_price) - 1) * 100

# S&P 500 return
sp_start = float(sp500_close.iloc[0].iloc[0])
sp_end = float(sp500_close.iloc[-1].iloc[0])
sp_return = ((sp_end / sp_start) - 1) * 100

# 52-week high and low
high_52_week = float(close.max().iloc[0])
low_52_week = float(close.min().iloc[0])

# Annualized volatility
daily_returns = close.pct_change().dropna()
annualized_volatility = float(daily_returns.std().iloc[0]) * (252 ** 0.5) * 100

# Performance compared with benchmark
difference = total_return - sp_return

# Print results
print(f"Stock Analysis: {ticker}")
print("-------------------------")
print(f"Starting Price: ${starting_price:.2f}")
print(f"Ending Price: ${ending_price:.2f}")
print(f"1-Year Return: {total_return:.2f}%")
print(f"52-Week High: ${high_52_week:.2f}")
print(f"52-Week Low: ${low_52_week:.2f}")
print(f"Annualized Volatility: {annualized_volatility:.2f}%")

print("\nBenchmark Comparison")
print("-------------------------")
print(f"JPM Return: {total_return:.2f}%")
print(f"S&P 500 Return: {sp_return:.2f}%")
print(f"Difference: {difference:.2f} percentage points")

# JPM price chart
plt.figure(figsize=(12, 6))

plt.plot(close.index, close, label="JPM Closing Price")
plt.plot(ma_50.index, ma_50, label="50-Day Moving Average")
plt.plot(ma_200.index, ma_200, label="200-Day Moving Average")

plt.title("JPM Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.grid(True)

plt.show()
