# .   .   .   .   1   
# .   .   .   .   1   
# .   .   .   3   1   
# .   .   .   2   1   
# 1   1   1   1   1   
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for row in reversed(range(m - 1)): 
            for col in reversed(range(n - 1)): 
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]