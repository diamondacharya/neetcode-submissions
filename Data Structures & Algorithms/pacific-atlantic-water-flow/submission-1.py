class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set()
        res = []
        def dfs(row, col, visited, parentVal): 
            if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]) or (row, col) in visited: 
                return
            if heights[row][col] < parentVal: 
                return 
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
        for col in range(len(heights[0])): 
            dfs(0, col, pset, -1)
            dfs(len(heights) - 1, col, aset, -1)
        for row in range(len(heights)): 
            dfs(row, 0, pset, -1)
            dfs(row, len(heights[0]) - 1, aset, -1)
        for row in range(len(heights)): 
            for col in range(len(heights[0])): 
                if (row, col) in pset and (row, col) in aset: 
                    res.append([row, col])
        return res