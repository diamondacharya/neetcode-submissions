class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1) 
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)): 
            m = min(dp[i - 1], dp[i - 2])
            dp[i] = m + cost[i] if i < len(cost) else m
        return dp[-1]
