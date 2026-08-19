class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for row in range(m - 2, -1, -1): 
            for col in range(n - 2, -1, -1): 
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]

