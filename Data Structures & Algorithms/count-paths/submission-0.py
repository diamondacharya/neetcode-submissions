class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        def dfs(row, col): 
            nonlocal res
            if row < 0 or row > m - 1 or col < 0 or col > n - 1: 
                return
            if row == m - 1 and col == n - 1: 
                res += 1
            dfs(row + 1, col)
            dfs(row, col + 1)
        dfs(0, 0) 
        return res