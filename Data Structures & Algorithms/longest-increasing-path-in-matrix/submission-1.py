class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {} # cache stores the longest path len from a (r, c) cell
        def dfs(row, col): 
            if (row, col) in cache: 
                return cache[(row, col)]
            length = 1
            for delx, dely in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
                nextRow = row + delx
                nextCol = col + dely
                if 0 <= nextRow <= len(matrix) - 1 and 0 <= nextCol <= len(matrix[0]) - 1  and matrix[nextRow][nextCol] > matrix[row][col]: 
                    length = max(length, 1 + dfs(nextRow, nextCol)) 
            cache[(row, col)] = length
            return length
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                dfs(row, col)
        return max(cache.values())