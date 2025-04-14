import yfinance as yf
import math

tickers = ['BHP.AX', 'RIO.AX']
bhp_data = yf.Ticker('BHP.AX')
rio_data = yf.Ticker('RIO.AX')

bhp_open = bhp_data.history(start="2025-01-01", end="2025-04-09", interval="1d")[["Open", "Close"]]
rio_open = rio_data.history(start="2025-01-01", end="2025-04-09", interval="1d")[["Open", "Close"]]

# # Write to text files
# with open("BHP.txt", "w") as bhp_file:
#     bhp_open.to_csv("BHP.csv", header=True)

# with open("RIO.txt", "w") as rio_file:
#     rio_open.to_csv("RIO.csv", header=True)

bhp_tuples = list(zip(bhp_open.index, bhp_open["Open"], bhp_open["Close"]))
rio_tuples = list(zip(rio_open.index, rio_open["Open"], rio_open["Close"]))

# Now need to process data and calculate information
# I want the average ratio of stock prices, as well as a chart over time

highest_ratio = 0
sum_ratio = 0
lowest_ratio = bhp_tuples[0][1]/rio_tuples[0][1]

i = 0
while i < len(bhp_tuples):
    ratio = bhp_tuples[i][1]/rio_tuples[i][1]
    if (ratio > highest_ratio):
        highest_ratio = ratio
    if (ratio < lowest_ratio):
        lowest_ratio = ratio
    sum_ratio += ratio
    i += 1

average_ratio = sum_ratio/len(bhp_tuples)

# next - stdev calculations

deviation_sum = 0
i = 0
while i < len(bhp_tuples):
    deviation = pow((average_ratio - (bhp_tuples[i][1]/rio_tuples[i][1])), 2)
    deviation_sum += deviation
    i += 1

variance = deviation_sum/len(bhp_tuples)
stdev = math.sqrt(variance)

print(f"Highest ratio: {round(highest_ratio, 3)}")
print(f"Lowest ratio: {round(lowest_ratio, 3)}")
print(f"Average ratio: {round(average_ratio, 3)}")
print(f"Standard deviation: {round(stdev, 5)}")

# flagging all the days where the ratio was off by more than a standard deviation
# executing trades on these days

i = 0
anomaly_days = 0
profit = 0
budget = 20000
while i < len(bhp_tuples):
    if ((abs(bhp_tuples[i][1]/rio_tuples[i][1]) - average_ratio) > stdev):
        anomaly_days += 1
        print(f"On {bhp_tuples[i][0]}, the ratio between the pairs was more than 1 stdev out from the average: {bhp_tuples[i][1]/rio_tuples[i][1]}")
        # now simulating the purchase order
        # day after, buy at the open, sell at the close
        if (bhp_tuples[i][1] > rio_tuples[i][1]):
            # short bhp, long rio
            # enter into short position by shorting at the next day's open price with cash available
            bhp_short_position = (budget/2)/bhp_tuples[i + 1][1]
            bhp_pnl = bhp_short_position*bhp_tuples[i + 1][2] - (budget/2)
            rio_long_position = (budget/2)/rio_tuples[i + 1][1]
            rio_pnl = (budget/2) - rio_long_position*rio_tuples[i + 1][2]
            profit += bhp_pnl
            profit += rio_pnl
            print(f"The total pnl the day after is: {profit}")
        if (bhp_tuples[i][1] < rio_tuples[i][1]):
            # long bhp, short rio
            bhp_long_position = (budget/2) / bhp_tuples[i + 1][1]
            bhp_pnl = (budget/2) - bhp_long_position * bhp_tuples[i + 1][2]
            rio_short_position = (budget/2) / rio_tuples[i + 1][1]
            rio_pnl = rio_short_position * rio_tuples[i + 1][2] - (budget/2)
            profit += bhp_pnl
            profit += rio_pnl
            print(f"The total pnl the day after is: {profit}")
    i += 1

print(f"{anomaly_days} out of {len(bhp_tuples)} were more than 1 stdev out.")
print(f"Profit using a budget of ${budget} for this strategy was: ${round(profit, 3)}")