    # [1, 2, 3, 4, 5, 6, 7] --> nums
# [0,0,0, 0, 0, 0, 0, 0, 0] --> dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)): 
            dp[i + 2] = max(nums[i] + dp[i], dp[i + 1])
        return dp[-1]