class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height) # stores max height to the left (including current bar)
        right = [0] * len(height) # stores max height to the right (including current bar)
        leftMax = float('-inf')
        rightMax = float('-inf')
        res = 0
        for i in range(len(height)): 
            leftMax = max(leftMax, height[i])
            left[i] = leftMax
        for i in range(len(height) - 1, -1, -1): 
            rightMax = max(rightMax, height[i])
            right[i] = rightMax
        for i in range(len(height)): 
            res += (min(left[i], right[i]) - height[i])
        return res

