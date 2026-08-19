class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {i: [] for i in range(len(points))} # nodes indexed by their position in the input list
        # create an ajdList with edges from each node to every other node (we'll need to consider them all)
        for i in range(len(points)): 
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                weight = abs(x2 - x1) + abs (y2 - y1)
                adjList[i].append((weight, j))
                adjList[j].append((weight, i))
        minheap = [(0, 0)]
        visited = set()
        mstWeight = 0
        while minheap: 
            weight, node = heapq.heappop(minheap)
            if node in visited: 
                continue
            visited.add(node)
            mstWeight += weight
            for neiWeight, nei in adjList[node]: 
                if nei not in visited: 
                    heapq.heappush(minheap, (neiWeight, nei))
        return mstWeight
            
        

