class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        freshFruitCount = 0
        for row in range(rowlen): 
            for col in range(collen): 
                if grid[row][col] == 1: 
                    freshFruitCount += 1
                if grid[row][col] == 2: 
                    q.append((row, col))
                    visited.add((row, col))
        if freshFruitCount == 0: 
            return 0
        dist = -1
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]: 
                    nextrow, nextcol = row + x, col + y
                    if nextrow >= 0 and nextrow < rowlen and nextcol >= 0 and nextcol < collen and grid[nextrow][nextcol] == 1 and (nextrow, nextcol) not in visited: 
                        q.append((nextrow, nextcol))
                        visited.add((nextrow, nextcol))
                        freshFruitCount -= 1
            dist += 1
        return dist if freshFruitCount == 0 else -1
        


