"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: interval.start)
        for i in range(1, len(intervals)): 
            interval = intervals[i]
            start, end = interval.start, interval.end
            if start < intervals[i - 1].end: 
                return False
        return True


        