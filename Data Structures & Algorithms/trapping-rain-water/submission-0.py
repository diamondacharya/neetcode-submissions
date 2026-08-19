class Solution:
    def trap(self, height: List[int]) -> int:
        leftTallest = [0] * len(height)
        rightTallest = [0] * len(height)
        leftMax = 0
        rightMax = 0
        res = 0
        for i in range(1, len(height)): 
            leftMax = max(leftMax, height[i - 1])
            leftTallest[i] = leftMax
        for i in range(len(height) - 2, -1, -1): 
            rightMax = max(rightMax, height[i + 1])
            rightTallest[i] = rightMax
        for i, h in enumerate(height): 
            toAdd = min(leftTallest[i], rightTallest[i]) - h
            toAdd = max(0, toAdd) # handling case for when current bar is taller
            res += toAdd
        return res