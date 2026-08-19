"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        sarr = sorted([i.start for i in intervals]) # start array
        earr = sorted([i.end for i in intervals]) # end array
        s, e = 0, 0
        while s < len(sarr): 
            if sarr[s] < earr[e]: 
                count += 1
                res = max(res, count)
                s += 1
            else: 
                count -= 1
                e += 1
        return res 


