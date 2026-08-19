class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # sorts on start by default, breaks ties on end
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)): 
            start, end = intervals[i]
            if start >= prevEnd: # non-overlapping
                prevEnd = end
            else: 
                prevEnd = min(prevEnd, end)
                res += 1
        return res

