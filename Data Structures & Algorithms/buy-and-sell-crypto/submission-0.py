class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            buys = prices[:i]
            curr = min(buys)
            curr_profit = prices[i] - curr
            if curr_profit > profit:
                profit = curr_profit
        return profit

            



        