class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rowlen = len(grid)
        collen = len(grid[0])
        def dfs(row, col): 
            if row < 0 or row >= rowlen or col < 0 or col >= collen or grid[row][col] == 0: 
                return 0
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        for row in range(rowlen): 
            for col in range(collen): 
                if grid[row][col] == 1: 
                    res = max(res, dfs(row, col)) 
        return res