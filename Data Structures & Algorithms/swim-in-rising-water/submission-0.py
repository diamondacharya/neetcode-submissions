class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [(grid[0][0], 0, 0)] # add first cell to minheap
        visited = set()
        while minheap: 
            weight, row, col = heapq.heappop(minheap) # weight is the max-height seen when node was put in minheap
            if (row, col) in visited: 
                continue
            if row == len(grid) - 1 and col == len(grid) - 1: # process bottom-right
                return weight
            visited.add((row, col))
            for delx, dely in [(1, 0), (0, 1), (-1, 0), (0, -1)]: 
                neiRow, neiCol = row + delx, col + dely
                if neiRow < 0 or neiRow >= len(grid) or neiCol < 0 or neiCol >= len(grid[0]) or grid[neiRow][neiCol] in visited: 
                    continue
                heapq.heappush(minheap, (max(grid[neiRow][neiCol], weight), neiRow, neiCol))



