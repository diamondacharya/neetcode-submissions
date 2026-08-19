# 1   1   0   1
# 1   0   0   1
# 0   0   1   1
# 0   0   1   2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCount = 0
        for row in range(len(grid)): 
            for col in range(len(grid[0])):
                if grid[row][col] == 1: 
                    freshCount += 1
                elif grid[row][col] == 2: 
                    q.append((row, col))
        time = 0
        while q and freshCount > 0: # no need to get in if all fresh fruits are now gone 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  
                    nextRow, nextCol = row + i, col + j
                    # only do bfs on fresh fruits (and if it's within bounds)
                    if 0 <= nextRow < len(grid) and 0 <= nextCol < len(grid[0]) and grid[nextRow][nextCol] == 1: 
                        grid[nextRow][nextCol] = 2 # mark as rotten (visited)
                        freshCount -= 1
                        q.append((nextRow, nextCol))
            time += 1
        return time if freshCount == 0 else -1
