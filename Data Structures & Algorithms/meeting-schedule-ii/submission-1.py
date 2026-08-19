"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

sarr = [0, 5, 15]
earr = [10, 20, 40]

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        sarr = [item.start for item in sorted(intervals, key = lambda interval: interval.start)] # start array
        earr = [item.end for item in sorted(intervals, key = lambda interval: interval.end)] # end array
        s, e = 0, 0
        while s < len(sarr) and e < len(earr): 
            if sarr[s] < earr[e]: 
                count += 1
                res = max(res, count)
                s += 1
            else: 
                count -= 1
                e += 1
        return res 


