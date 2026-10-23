class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
            maxProfit = max(profit, maxProfit)
        return maxProfit