class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0 # max profit 
        minp = float('inf') # minimum price till now
        for price in prices: 
            minp = min(price, minp)
            maxp = max(maxp, price - minp)
        return maxp
