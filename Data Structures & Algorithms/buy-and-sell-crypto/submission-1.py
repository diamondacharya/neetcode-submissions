class Solution:
    # [7,1,5,3,6,4]
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i, price in enumerate(prices): 
            if (i != 0): 
                profit = price - minprice
                maxprofit = max(profit, maxprofit)
                minprice = min(price, minprice)
        return maxprofit