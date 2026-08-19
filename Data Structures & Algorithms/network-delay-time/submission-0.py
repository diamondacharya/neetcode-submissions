class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for u, v, weight in times: 
            adjList[u].append((weight, v)) # append tuples of (weight, dest_node)
        minheap = [(0, k)] # initialize min heap with source node
        dist = {} # stores shortest distances to each node
        while minheap: 
            distance, node = heapq.heappop(minheap)
            if node in dist: 
                continue
            dist[node] = distance
            for weight, neighbor in adjList[node]: 
                if neighbor not in dist: 
                    heapq.heappush(minheap, (distance + weight, neighbor))
        if len(dist) != n: # disjoint, so not possible to reach all nodes
            return -1
        return max(dist.values())


        