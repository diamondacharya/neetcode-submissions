class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        leftMax, rightMax = height[i], height[j]
        res = 0
        while i < j: 
            if leftMax <= rightMax: 
                i += 1
                leftMax = max(leftMax, height[i])
                res += leftMax - height[i] # no need to handle for negative coz leftMax includes current bar too!
            else: 
                j -= 1
                rightMax = max(rightMax, height[j])
                res += rightMax - height[j]
        return res
