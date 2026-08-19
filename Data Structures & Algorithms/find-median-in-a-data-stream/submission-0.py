class MedianFinder:

    def __init__(self):
        self.small = [] # max heap (need to negate when pushing and revert when popping)
        self.large = [] # min heap

    # invariants to maintain 
        # all elem in small <= all elem in large
        # abs(len(small) - len(large)) <= 1
    def addNum(self, num: int) -> None:
        if (self.large and num >= self.large[0]): 
            heapq.heappush(self.large, num)
        else: 
            heapq.heappush(self.small, -1 * num)
        if (len(self.large) - len(self.small) > 1): # move smallest from large to small
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * item)
        if (len(self.small) - len(self.large) > 1): # move largest from small to large
            item = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, item)

    def findMedian(self) -> float:
        if (len(self.small) > len(self.large)): 
            return -1 * self.small[0]
        if (len(self.large) > len(self.small)): 
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
        