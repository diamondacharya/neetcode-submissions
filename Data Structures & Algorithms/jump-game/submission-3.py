class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = float('-inf')
        for i in range(len(nums)): 
            maximum = max(maximum, i + nums[i])
            if maximum >= len(nums) - 1: 
                return True
            if maximum < i + 1: 
                return False