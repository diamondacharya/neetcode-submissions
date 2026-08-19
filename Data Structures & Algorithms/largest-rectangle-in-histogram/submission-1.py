class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i, height in enumerate(heights): 
            while stack and heights[stack[-1]] > height: 
                poppedHeight = heights[stack.pop()]
                if stack: 
                    length = i - stack[-1] - 1
                else: 
                    length = i
                res = max(res, poppedHeight * length)
            stack.append(i)
        return res