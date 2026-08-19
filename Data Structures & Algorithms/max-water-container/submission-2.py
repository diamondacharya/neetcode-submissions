class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = float('-inf')
        while i < j: 
            vol = min(heights[i], heights[j]) * (j - i)            
            res = max(res, vol)
            if heights[i] < heights[j]: 
                i += 1
            else: 
                j -= 1
        return res