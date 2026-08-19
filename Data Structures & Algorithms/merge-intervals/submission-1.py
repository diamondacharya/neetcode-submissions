class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # sort by start time first 
        output = []
        prev = intervals[0]
        i = 1
        while i < len(intervals): 
            start, end = intervals[i]
            prevStart, prevEnd = prev
            if start <= prevEnd: 
                prev = [min(start, prevStart), max(end, prevEnd)]
            else: 
                output.append(prev)
                prev = intervals[i]
            i += 1
        output.append(prev)
        return output
        
            