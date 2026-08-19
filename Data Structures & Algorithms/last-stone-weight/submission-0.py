import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1: 
            heaviest = -1 * heapq.heappop(h)
            heaviest2 = -1 * heapq.heappop(h)
            if heaviest != heaviest2: 
                heapq.heappush(h, -1 * (heaviest - heaviest2))
        return -1 * h[0] if len(h) == 1 else 0
            
