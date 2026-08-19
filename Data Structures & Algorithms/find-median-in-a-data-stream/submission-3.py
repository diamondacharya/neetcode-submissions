# ["MedianFinder", "addNum", "-1", "addNum", "-2", "findMedian", "addNum", "-3", "findMedian", "addNum", "-4", "findMedian", "addNum", "-5", "findMedian"]
# minheap = [-3, -1]
# maxheap = [2] (numbers are negated here)
import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []  # second portion
        self.maxheap = []  # first portion
        
    def addNum(self, num: int) -> None:
        if (self.maxheap and num >= -1 * self.maxheap[0]): 
            heapq.heappush(self.minheap, num)
        else: 
            heapq.heappush(self.maxheap, -1 * num)
        if len(self.minheap) - len(self.maxheap) > 1: 
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * popped)
        elif len(self.maxheap) - len(self.minheap) > 1:
            popped = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, popped)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap): 
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap): 
            return -1 * self.maxheap[0]
        else: 
            return (self.minheap[0] + (-1) * self.maxheap[0]) / 2
        