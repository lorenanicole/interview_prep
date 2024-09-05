"""
Your algorithms have become so good at predicting the market that you now know what the share price of Silly Purple Toothpicks Inc. 
(SPT) will be for a number of minutes going forward. Each minute, your high frequency trading platform allows you to either buy one 
share of SPT, sell any number of shares of SPT that you own, or not make any transaction at all. Find the maximum profit you can obtain 
with an optimal trading strategy. Purchases are negative and sales are positive cash flows in the following equations. For example, 
if predicted prices over the next n = 6 minutes are prices = [3, 4, 5, 3, 5, 2], one way to the best outcome is to purchase a share in each 
of the first 2 minutes for cash flows -3 + -4 = -7, then sell them at the third minute for 2 * 5 = 10. Purchase a share in the 4th minute for 
-3 and sell it in the 5th minute for 5. Total profits are -3 - 4 + 10 - 3 + 5 = 5. Another way to the same outcome is to purchase a share in 
each of the 1st, 2nd and 4th minutes for -3 - 4 - 3 = -10, do nothing at minute 2 then sell all three shares at 5 (total 3 * 5 = 15) on the 5th 
minute, again for a total profit of -10 + 15 = 5. There is no reason to purchase in the last minute as there is no time to sell.
"""

def stockmax(prices):
    if not prices:
        return 0

    max_price = prices[-1]
    profit = 0

    # iterate prices from the found highest max most recently in time (e.g. at the end of prices 
    # list) at len(prices)-1 as max_price already set to max val
    profit = 0
    current_max = prices[-1]
    for i in range(len(prices)-1, -1, -1):
        if prices[i] >= current_max:
            current_max = prices[i]
        
        profit += current_max - prices[i]
        print(f'Current profit {profit} when subtract {prices[i]}, current max {current_max}')
    return profit

    

def stockmax(prices):
    maximum_profit = 0
    for val in range([prices::-1]):
        if prices[val] >= maximum_profit:
            maximum_profit = prices[val]
        profit += maximum_profit - prices[val]

# print(stockmax([5, 3, 2]) == 0)
# print(stockmax([1, 2, 100]) == 197)
print(stockmax([1, 3, 1, 2]) == 3)

# print(stockmax([3,4,5,3,5,2]))