"""Buy and sell a stock once

Design an algorithm that determines the maximum profit that could have been made by buying and then selling a single share over a given day range,
subject to the constraint that we must buy before sell.

Example: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] (stock prices). The max profit that can be made with one buy and one sell
is 30 - buy at 260 and sell at 290.

Brainstorm:
- max_profit = float('-inf')
- min_price_so_far = A[0]
- for price in A:
    - max_profit_today = price - min_price_so_far
    - max_profit = max(max_profit, max_profit_today)
    - min_price = min(min_price_so_far, price)
"""


def buy_sell_stock_once(arr):
    max_profit = float("-inf")
    min_price = arr[0]
    for price in arr:
        profit_today = price - min_price
        max_profit = max(max_profit, profit_today)
        min_price = min(min_price, price)

    return max_profit


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_sell_stock_once(A))
