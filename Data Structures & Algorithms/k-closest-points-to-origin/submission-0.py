import heapq

class Solution:
    # helper func to get distance from origin 
    def getDistance(self, point): 
        x, y = point
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points: 
            dist = self.getDistance(point)
            heapq.heappush(heap, (-1 * dist, (point[0], point[1])))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [tup[1] for tup in heap]