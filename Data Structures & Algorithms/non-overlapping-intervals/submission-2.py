class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0]) # sort by start time
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)): 
            start, end = intervals[i]
            if start >= prevEnd: 
                prevEnd = end
            else: 
                prevEnd = min(end, prevEnd)
                res += 1
        return res