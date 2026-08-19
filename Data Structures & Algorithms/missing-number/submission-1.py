class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualSum = sum(nums)
        expSum = 0
        for i in range(len(nums) + 1): 
            expSum += i
        return expSum - actualSum