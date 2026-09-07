class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for price in prices: 
            profit = price - minPrice 
            maxProfit = max(profit, maxProfit)
            minPrice = min(minPrice, price)
        return maxProfit 