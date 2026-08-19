class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumsmall = sum(nums)
        sumbig = 0
        for num in range(len(nums) + 1):
            sumbig += num 
        return sumbig - sumsmall


        