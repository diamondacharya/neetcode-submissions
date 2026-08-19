# amount = 10
# coint = [2, 3]

# To get to 10
# 1 + min no of coins req to get to 7
# 1 + min no of coins req to get to 8 

# To get to 7
# 1 + min no of coins to get to 4
# 1 + min no of coins to get to 5

# coins = [1, 2, 5]
# amount = 11
# dp = [0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1): 
            for coin in coins: 
                if (a - coin) >= 0: 
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return -1 if dp[amount] == float('inf') else dp[amount]

