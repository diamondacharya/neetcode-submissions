import heapq
class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if (self.large and self.large[0] <= num): 
            heapq.heappush(self.large, num)
        else: 
            heapq.heappush(self.small, -1 * num)
        if (len(self.large) - len(self.small) > 1): 
            item = heapq.heappop(self.large) 
            heapq.heappush(self.small, -1 * item)
        if (len(self.small) - len(self.large) > 1): 
            item = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, item)
        
    def findMedian(self) -> float:
        if (len(self.large) > len(self.small)): 
            return self.large[0]    
        elif (len(self.small) > len(self.large)): 
            return -1 * self.small[0]    
        else: 
            return (-1 * self.small[0] + self.large[0]) / 2
        