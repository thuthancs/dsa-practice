"""Buy and sell stock twice

Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.
The second buy must be made on another date after the first sale.

Example: A = [12, 11, 13, 9, 12, 8, 14, 13, 15]
The maximum profit that can be made by buying and selling a share at most twice is 10,
which means we can first buy a stock on day 4 and sell it on day 8 (15 - 12 = 3), then
we can buy a stock on day 5 and sell it on day 8 (15 - 8 = 7)

Thoughts:
- We can make use of the solution to the buy and sell stock once problem.
- First, we can compute the max profit we can earn if we sell stock on a specific day once
- Then, we do a second pass that computes the max profit we can earn if we sell stock after a day i
- We then add both arrays together and return the max value
"""


def buy_sell_stock_twice(arr):
    n = len(arr)
    first_buy_profit = [0] * n

    # Forward pass — max profit from one transaction up to day i
    min_price = arr[0]
    for i in range(1, n):
        min_price = min(min_price, arr[i])
        first_buy_profit[i] = max(first_buy_profit[i - 1], arr[i] - min_price)

    # Backward pass — max profit from one transaction after day i
    max_total_profit = 0
    max_price = arr[-1]
    for j in range(n - 2, -1, -1):
        max_price = max(max_price, arr[j])
        profit_if_sold_later = max_price - arr[j]
        max_total_profit = max(
            max_total_profit, profit_if_sold_later + first_buy_profit[j]
        )

    return max_total_profit


A = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_sell_stock_twice(A))
