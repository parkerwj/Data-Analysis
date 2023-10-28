# Overview

This Python script leverages the `yfinance` library to fetch historical stock data from Yahoo Finance, analyze it with basic and advanced metrics, and create insightful visualizations. The analysis includes computing indicators like moving averages and the Relative Strength Index (RSI). Users can interactively input a stock symbol and the number of years for data retrieval, and the script dynamically generates answers to predefined questions about the stock's performance, with real-time data. It's a versatile tool for software engineers seeking hands-on experience in financial data analysis and visualization.

## Data Set Description

I analyzed historical stock data, and the data was obtained from Yahoo Finance using the [yfinance library](https://pypi.org/project/yfinance/).

## Purpose

The purpose of this software is to analyze historical stock data, answer specific questions about the stock's performance, and visualize the results. By doing this, I aim to enhance my skills as a software engineer in data analysis and data visualization within the financial domain.

## Software Demo Video

You can watch a 4-5 minute demonstration of this project in action on [YouTube](https://youtu.be/1hWMBlLd-9U).

# Data Analysis Results

The responses to these questions dynamically adjust as the data is sourced live from Yahoo Finance. The code includes variables that will generate and display the answers when executed

- **Company Name**: [Company Name]
- **Question 1**: What is the historical stock price data for [Company Name] for the past [years] years?
  [Historical stock price data]

- **Question 2**: What is the 50-day simple moving average (SMA) of [Company Name]'s stock price?
  [50-Day SMA data]

- **Question 3**: What is the daily returns of [Company Name]'s stock during the specified date range?
  [Daily Returns data]

- **Question 4**: What is the 14-day relative strength index (RSI) for [Company Name] ([Stock Symbol])?
  [14-Day RSI data]

- **Question 5**: Are there any overbought or oversold conditions for [Company Name] ([Stock Symbol]) based on RSI?
  The code plots horizontal lines at RSI values of 30 (indicating oversold conditions) and 70 (indicating overbought conditions) on the RSI chart.
- **Question 6**: What is the Value at Risk (VaR) at a 95% confidence level for [stock_name] [stock_symbol]?
    Value at Risk (VaR) at 95% confidence level: {var * 100:.2f}%

# Development Environment

I developed this software using the following tools and programming languages:

- Python 3.11.5
- [yfinance](https://pypi.org/project/yfinance/) library
- [matplotlib](https://matplotlib.org/) for data visualization
- [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/) library for calculating technical indicators
- [datetime](https://docs.python.org/3/library/datetime.html) for handling date and time data

# Useful Websites

I found the following websites helpful in this project:

- [Yahoo Finance](https://finance.yahoo.com/)
- [yfinance Python library documentation](https://pypi.org/project/yfinance/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

# Future Work

In the future, I plan to work on the following improvements and additions to this project:

- Item 1: Add more technical indicators and analysis methods.
- Item 2: Enhance data visualization by creating interactive plots.
- Item 3: Implement a user-friendly interface for input and interaction.

