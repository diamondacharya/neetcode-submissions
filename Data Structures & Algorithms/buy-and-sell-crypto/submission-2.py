class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = float('-inf')
        for price in prices: 
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        return maxProfit
