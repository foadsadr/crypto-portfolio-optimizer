# Crypto Portfolio Optimizer
Cryptocurrencies portfolio optimizer and simulator (useful for investors and holders)

## Description
Welcome to the Cryptocurrency Portfolio Optimizer – a dynamic tool designed for investors stepping into the world of cryptocurrencies. This project is an essential guide for those uncertain about which assets to include in their portfolio. By leveraging a powerful simulation (backtest) mechanism, provides a data-driven approach to asset allocation.

## Key Features
- Personalized Portfolio Simulation: Input your candidate cryptocurrencies and a specific time interval, and our tool will simulate (backtest) how these coins have performed historically.

- Optimal Allocation Strategies: Through a comprehensive analysis, the tool suggests optimal percentage allocations for each asset in your portfolio, ensuring a balanced and diversified investment strategy.

- Brute-Force Algorithm for Precision: At its core, the project utilizes a brute-force (backtrack) algorithm. This technique meticulously tests various portfolio combinations to find the most effective one for your goals.

- Focus on Minimizing Drawdowns: A key objective of our tool is to minimize the drawdown in your wealth chart over time, enhancing the stability and reliability of your investments.

## What is Drawdown?
Drawdown in finance refers to the peak-to-trough decline during a specific recorded period of an investment, a trading account, or a fund. It is usually quoted as the percentage between the peak and the subsequent trough. If a trading account has $10,000 at the peak and then drops to $9,000 before rising again, the drawdown is 10%. Drawdowns are important for measuring the historical risk of different investments, comparing fund performance, or monitoring personal trading performance. A key goal in finance is to minimize drawdowns to preserve capital and ensure a smoother investment growth trajectory.

## Why Use This Tool?
Investing in cryptocurrencies can be daunting due to their volatile nature. This tool empowers you to make informed decisions based on historical performance and robust analysis, thus helping to demystify the process of crypto investment and asset allocation. Whether you're a seasoned investor or new to the crypto world, our Portfolio Optimizer is your companion in building a resilient and potentially profitable crypto portfolio.

## Installation
First, clone the repository and then run the following command.

```pip3 install -r requirements.txt```

## Usage
Just run the following command.

```python3 main.py```

## Config
You can change the `config.py` file to change the simulation parameters.
- `CANDIDATE_COINS` is a list of coins that you want to buy. 
- `WEIGHTS_STEP_PRECISION_PERCENT`: if you set you set it to 20, your portfolio might be something like this: 20% BTC, 40% ETH, 60% ETH (each weight will be a factor of 20%)
- `SIMULATION_START_DATE` indicates the start time interval of the simulation.
- `SIMULATION_END_DATE` indicates the end time interval of the simulation.
- `START_WALLET_SIZE_USD` indicates the total amount of money (in the US Dollars) you want to invest.
