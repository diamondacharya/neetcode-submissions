class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * weight for weight in stones]
        heapq.heapify(heap)
        while len(heap) > 1: 
            one = -1 * heapq.heappop(heap)
            two = -1 * heapq.heappop(heap)
            if abs(one - two) > 0: 
                heapq.heappush(heap, -1 * abs(one - two))
        return 0 if len(heap) == 0 else -1 * heap[0]

