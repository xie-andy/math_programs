# math_programs

- This repo is a collection of Python programs to experiment with different quantitative trading methods and entry/exit methodologies and also general math programs.

- To run quant models on your own computer, clone the repo, install yfinance and then execute the relevant script.

# pair_trading.py

My first model, this is essentially a proof of concept and for me to understand the actual procedure behind a quant algorithm.

## Strategy Used

Pair trading strategy on BHP and RIO on ASX.

## Signal

Signal is when the ratio of the two stock prices moves more than 1 standard deviation away from the historical mean (calculated over the whole time period).

## Entry/Exit Strategy

- **Entry**: Long on the stock with the lower price and short on the stock with the higher price, 50/50 budget split on the positions, trade executed at the opening of the next day after the signal.
- **Exit**: Positions are exited at the close of the next day.

## Performance

- **PnL**: +0.7% over time period (1 Jan 25 - 9 Apr 25).
- **Success Rate**: 4 out of 5 trades profitable.
- **Max Drawdown**: -0.17%.

## Notes

- Model does not account for slippage or transaction costs and doesn't use dynamic position sizing.
- Position sizing is fixed, assuming a constant budget regardless of daily PnL.
- Daily closing prices used to calculate the stdev
- The standard deviation was calculated with data over the entire dataset, rather than using a rolling average for each day

## Improvements

- Modularise data analysis + signal function + entry + exit modules so I can test different combinations
- Use rolling average to calculate dataset statistics
- Create mock trade platform to input strategies into (paper testing, can test my strategies as I keep coming up with them over future datasets)
- Take repo private after coming up with mad alpha generating strategy #dollarbills
