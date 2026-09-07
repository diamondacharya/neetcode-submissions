class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        lefttallest = []
        righttallest = [0] * len(height)
        res = 0
        for h in height: 
            leftmax = max(leftmax, h)
            lefttallest.append(leftmax)
        for i in range(len(height) - 1, -1, -1):
            rightmax = max(rightmax, height[i])
            righttallest[i] = rightmax
        for i in range(len(height)):
            water = min(lefttallest[i], righttallest[i]) - height[i]
            res += water
        return res
        