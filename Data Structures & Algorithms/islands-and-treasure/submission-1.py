class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        d = deque()
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        for row in range(rowlen): 
            for col in range(collen): 
                if grid[row][col] == 0: 
                    d.append((row, col))
                    visited.add((row, col))
        dist = 0
        while d: 
            for _ in range(len(d)): 
                row, col = d.popleft()
                grid[row][col] = dist 
                for xdelta, ydelta in [(0, 1), (1, 0), (-1, 0), (0, -1)]: 
                    nextrow = row + xdelta
                    nextcol = col + ydelta
                    if nextrow >= 0 and nextrow < rowlen and nextcol >= 0 and nextcol < collen and grid[nextrow][nextcol] != -1 and (nextrow, nextcol) not in visited: 
                        visited.add((nextrow, nextcol))
                        d.append((nextrow, nextcol))
            dist += 1
        
