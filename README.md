# quant_models
A collection of Python programs to experiment with different quantitative trading methods and entry/exit methodologies.

# pair_trading.py

My first model, this is essentially a proof of concept and for me to understand the actual procedure behind a quant algorithm.

Strategy used: Pair trading BHP and RIO on ASX.
Signal: Ratio of stock prices being more than 1 standard deviation out.
Entry/exit strategy: Long on the lower stock, short on the higher stock. Entered into positions the opening of the next day and exited on the closing of the next day.
PnL: Generated returns of 0.7% over the time period (Start of 2025 until now), with 4/5 trades successful. Max drawdown of 0.017%.

Notes: Doesn't account for slippage and sizing is fixed, not dynamic. Assumes budget remains the same regardless of daily PnL.

## Strategy Used

Pair trading strategy on BHP and RIO on ASX.

## Signal

Signal is generated when the ratio of the two stock prices moves more than 1 standard deviation away from the historical mean (calculated over the whole time period).

## Entry/Exit Strategy

- **Entry**: Long on the stock with the lower price and short on the stock with the higher price, executed at the opening of the next day after the signal.
- **Exit**: Positions are exited at the close of the next day.

## Performance

- **PnL**: The model generated a return of 0.7% from the start of 2025 to the present.
- **Trade Success Rate**: 4 out of 5 trades were profitable.
- **Max Drawdown**: 0.17%.

## Additional Notes

- This model does not account for slippage, transaction costs and doesn't use dynamic position sizing.
- Position sizing is fixed, assuming a constant budget regardless of daily PnL.
- Daily closing prices used to calculate the stdev
- The standard deviation was calculated with data over the entire dataset, rather than using a rolling average for each day

## Improvements

- Modularise data analysis + signal function + entry + exit modules so I can test different strategies and combinations
- Use rolling average to calculate dataset statistics
- Create mock trade platform to input strategies into (paper testing, can test my strategies as I keep coming up with them over future datasets)
- Take repo private after coming up with alpha generating strategy #dollars
