class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # key = (i, buyMode); val = max_profit from that ind in that mode 
        def dfs(i, buyMode): 
            if i >= len(prices): 
                return 0
            if (i, buyMode) in cache: 
                return cache[(i, buyMode)]
            if buyMode:  # can buy or cooldown
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, buyMode)
                cache[(i, buyMode)] = max(buy, cooldown)
            else: # should sell or cooldown
                sell = dfs(i + 2, True) + prices[i] # i + 2 to give a day for cooldown
                cooldown = dfs(i + 1, buyMode)
                cache[(i, buyMode)] = max(sell, cooldown)
            return cache[(i, buyMode)]
        return dfs(0, True)
