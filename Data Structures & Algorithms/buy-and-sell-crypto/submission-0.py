class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # tracks the maximum profit

        # initial the first price of the 
        # first day to be the starting price
        buy_price = prices[0]
        for index in range(1, len(prices)):
            profit = prices[index] - buy_price

            # set max_profit if profit is greater 
            max_profit = max(max_profit, profit)
            # obtain lowest buy_price
            buy_price = min(buy_price, prices[index])

        return max_profit