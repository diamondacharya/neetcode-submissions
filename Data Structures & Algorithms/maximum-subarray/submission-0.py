class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        running_sum = 0
        for num in nums: 
            running_sum += num
            maximum = max(maximum, running_sum)
            if running_sum < 0: 
                running_sum = 0
        return maximum