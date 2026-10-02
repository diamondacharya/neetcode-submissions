class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap (stores the lower half)
        self.large = [] # min-heap (stores the upper half)
        

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]: 
            heapq.heappush(self.large, num)
        else: 
            heapq.heappush(self.small, -1 * num)
        if len(self.small) - len(self.large) > 1: 
            item = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * item)
        elif len(self.large) - len(self.small) > 1: 
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * item)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): 
            return -1 * self.small[0]
        elif len(self.large) > len(self.small): 
            return self.large[0]
        else: 
            return (-1 * self.small[0] + self.large[0]) / 2
        
        