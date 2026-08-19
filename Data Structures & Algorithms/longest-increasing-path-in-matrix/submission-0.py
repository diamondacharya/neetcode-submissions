class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        def dfs(row, col, length): 
            nonlocal res
            length += 1
            res = max(res, length)
            for delx, dely in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
                r = row + delx
                c = col + dely
                if 0 <= r <= len(matrix) - 1 and 0 <= c <= len(matrix[0]) - 1 and matrix[r][c] > matrix[row][col]: 
                    dfs(r, c, length)
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                dfs(row, col, 0)
        return res