class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # helper func
        def visitNeighbor(row, col): 
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == -1: 
                return
            q.append((row, col))
            visited.add((row, col))
        q = deque()
        visited = set()
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == 0: 
                    q.append((row, col))
                    visited.add((row, col))
        dist = 0
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                grid[row][col] = dist
                visitNeighbor(row + 1, col)
                visitNeighbor(row - 1, col)
                visitNeighbor(row, col + 1)
                visitNeighbor(row, col - 1)
            dist += 1
