class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for i, query in enumerate(queries): 
            minSize = float('inf')
            for start, end in intervals: 
                if start <= query <= end and (end - start + 1) < minSize: 
                    minSize = end - start + 1
            if minSize == float('inf'): 
                output.append(-1)
            else: 
                output.append(minSize)
        return output