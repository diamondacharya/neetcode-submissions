class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = [] # stores (idx, height) tuples
        res = 0
        for i in range(len(heights)): 
            currentHeight = heights[i]
            while len(stack) > 0 and currentHeight < stack[-1][1]: 
                poppedIdx, poppedHeight = stack.pop()
                length = 0
                if len(stack) > 0:
                    leftIdx = stack[-1][0]
                    length = i - leftIdx - 1 
                    area = length * poppedHeight 
                    res = max(res, area)
                else: 
                    length = i
                    area = length * poppedHeight
                    res = max(res, area)
            stack.append((i, currentHeight))
        return res
