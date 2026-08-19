class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in reversed(range(m - 1)): 
            for j in reversed(range(n - 1)): 
                dp[j] = dp[j] + dp[j + 1] # dp[j] is the bottom val and dp[j + 1] the right val
        return dp[0]

