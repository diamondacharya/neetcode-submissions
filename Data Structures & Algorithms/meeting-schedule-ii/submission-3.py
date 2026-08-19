"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        sarr = [interval.start for interval in intervals]
        earr = [interval.end for interval in intervals]
        sarr.sort()
        earr.sort()
        i, j = 0, 0 
        count = 0
        while i < len(sarr) and j < len(earr): 
            if sarr[i] < earr[j]: 
               count += 1 
               res = max(res, count)
               i += 1
            else: 
                count -= 1
                j += 1
        return res