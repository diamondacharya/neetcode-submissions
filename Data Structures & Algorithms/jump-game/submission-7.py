class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd = -1
        for i in range(len(nums)): 
            maxInd = max(maxInd, i + nums[i])
            if maxInd >= len(nums) - 1:
                return True
            elif maxInd <= i: 
                return False