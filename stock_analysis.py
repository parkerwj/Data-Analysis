import yfinance as yf
import matplotlib.pyplot as plt
import ta
from datetime import datetime, timedelta

def fetch_stock_data(stock_symbol, years):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years * 365)

    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

def get_company_name(stock_symbol):
    try:
        stock_info = yf.Ticker(stock_symbol)
        return stock_info.info['longName']
    except:
        return stock_symbol

def basic_stock_analysis(data):
    data['Daily Returns'] = data['Adj Close'].pct_change()
    data['50-Day SMA'] = data['Adj Close'].rolling(window=50).mean()
    data['50-Day STD'] = data['Adj Close'].rolling(window=50).std()
    return data

def advanced_stock_analysis(data):
    data['200-Day SMA'] = data['Adj Close'].rolling(window=200).mean()
    data['Upper Bollinger Band'] = data['50-Day SMA'] + 2 * data['50-Day STD']
    data['Lower Bollinger Band'] = data['50-Day SMA'] - 2 * data['50-Day STD']

    # Calculate 14-Day RSI using ta library
    data['RSI'] = ta.momentum.RSIIndicator(data['Adj Close'], window=14).rsi()

    return data

def calculate_var(data):
    # Calculate the daily returns
    data['Daily Returns'] = data['Adj Close'].pct_change()
    
    # Calculate VaR at a specified confidence level (e.g., 95%)
    confidence_level = 0.95
    var = data['Daily Returns'].quantile(1 - confidence_level)
    
    return var

def plot_stock_data(data, stock_name):
    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.plot(data.index, data['Adj Close'], label='Stock Price', color='blue')
    plt.plot(data.index, data['50-Day SMA'], label='50-Day SMA', color='orange')
    plt.fill_between(data.index, data['50-Day SMA'] - 2 * data['50-Day STD'],
                     data['50-Day SMA'] + 2 * data['50-Day STD'], color='lightgray', alpha=0.5)
    plt.title(f'Stock Price and 50-Day Simple Moving Average ({stock_name})')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(data.index, data['Daily Returns'], color='red')
    plt.axhline(0, color='black', linestyle='--')
    plt.title(f'Daily Returns ({stock_name})')
    plt.xlabel('Date')
    plt.ylabel('Returns')

    plt.subplot(3, 1, 3)
    plt.plot(data.index, data['RSI'], label='14-Day RSI', color='green')
    plt.axhline(30, color='red', linestyle='--', label='Oversold (30)')
    plt.axhline(70, color='blue', linestyle='--', label='Overbought (70)')
    plt.title(f'14-Day RSI ({stock_name})')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    stock_symbol = input("Enter the stock symbol: ")
    years = int(input("Enter the number of years for historical data retrieval: "))

    data = fetch_stock_data(stock_symbol, years)
    data = basic_stock_analysis(data)
    data = advanced_stock_analysis(data)
    
    var = calculate_var(data)
    
    stock_name = get_company_name(stock_symbol)

    # Print questions and answers
    print(f"Company Name: {stock_name}")
    print(f"Question 1: What is the historical stock price data for {stock_name} for the past {years} years?")
    print(data)

    print(f"Question 2: What is the 50-day simple moving average (SMA) of {stock_name}'s stock price?")
    print(data['50-Day SMA'])

    print(f"Question 3: What is the daily returns of {stock_name}'s stock during the specified date range?")
    print(data['Daily Returns'])

    print(f"Question 4: What is the 14-day relative strength index (RSI) for {stock_name} ({stock_symbol})?")
    print(data['RSI'])

    print(f"Question 5: Are there any overbought or oversold conditions for {stock_name} ({stock_symbol}) based on RSI?")
    print("The code plots horizontal lines at RSI values of 30 (indicating oversold conditions) and 70 (indicating overbought conditions) on the RSI chart.")
    
    print(f"Question 6: What is the Value at Risk (VaR) at a 95% confidence level for {stock_name} ({stock_symbol})?")
    print(f"Value at Risk (VaR) at 95% confidence level: {var * 100:.2f}%")

    # Plot the stock data with the stock name in the title
    plot_stock_data(data, stock_name)

if __name__ == "__main__":
    main()
