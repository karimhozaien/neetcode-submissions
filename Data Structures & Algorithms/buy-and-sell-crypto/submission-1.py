class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        for i in range(len(prices)):
            buy = prices[i]
            sell = max(prices[i:])
            profit = sell - buy
            print(buy, sell, profit, max_profit)
            max_profit = max(profit,max_profit)

        return max_profit