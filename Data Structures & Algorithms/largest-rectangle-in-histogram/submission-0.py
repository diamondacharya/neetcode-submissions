class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [] # monotonically increasing (non-decreasing)
        max_area = 0
        for i, curr_height in enumerate(heights): 
            while(stack and curr_height < heights[stack[-1]]): 
                height = heights[stack.pop()]
                if stack: 
                    length = i - stack[-1] - 1
                else: 
                    length = i
                area = height * length
                max_area = max(max_area, area)
            stack.append(i) 
        return max_area