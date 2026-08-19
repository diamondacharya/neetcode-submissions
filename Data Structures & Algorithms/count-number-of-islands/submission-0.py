class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        count = 0
        def dfs(row, col): 
            if not 0 <= row < R or not 0 <= col < C or grid[row][col] == '0': 
                return 
            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        for row in range(R): 
            for col in range(C): 
                if grid[row][col] == '1': 
                    dfs(row, col)
                    count += 1
        return count