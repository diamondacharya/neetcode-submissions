class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [] # will store the indices 
        res = 0
        for i in range(len(heights)): 
            while stack and heights[stack[-1]] > heights[i]: 
                poppedIndex = stack.pop()
                if stack: 
                    length = i - stack[-1] - 1 
                else: 
                    length = i
                h = heights[poppedIndex]
                area = length * h
                res = max(area, res)
            stack.append(i)
        return res