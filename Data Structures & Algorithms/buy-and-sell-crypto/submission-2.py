class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices)):
            bestPrice = max(prices[i:]) - prices[i]
            print(bestPrice)
            if bestPrice > profit:
                profit = bestPrice
        return profit