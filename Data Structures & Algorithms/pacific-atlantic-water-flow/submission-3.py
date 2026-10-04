class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pv = set() # pacific visited
        av = set() # atlantic  visited
        result = []
        rowlen = len(heights)
        collen = len(heights[0])
        def dfs(row, col, visited, prev): 
            if row < 0 or row >= rowlen or col < 0 or col >= collen or (row, col) in visited: 
                return
            if heights[row][col] < prev: 
                return 
            visited.add((row, col))
            for delx, dely in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
                nextrow, nextcol = row + delx, col + dely
                dfs(nextrow, nextcol, visited, heights[row][col])
        for row in range(rowlen): 
            dfs(row, 0, pv, heights[row][0])
            dfs(row, collen - 1, av, heights[row][collen - 1])
        for col in range(collen): 
            dfs(0, col, pv, heights[0][col])
            dfs(rowlen - 1, col, av, heights[rowlen - 1][col])
        intersection = pv & av 
        for row, col in intersection: 
            result.append([row, col])
        return result

