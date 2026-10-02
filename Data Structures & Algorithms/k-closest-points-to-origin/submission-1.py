class Solution:
    def getDistance(point): 
        x, y = point
        return math.sqrt(x**2 + y**2)
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # stores (dist, point) tuples
        for point in points: 
            dist = Solution.getDistance(point)
            heapq.heappush(heap, (-1 * dist, point))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [point for dist, point in heap]
