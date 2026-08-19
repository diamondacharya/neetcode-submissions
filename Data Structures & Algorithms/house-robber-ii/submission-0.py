class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i, j): 
            p, pp = 0, 0
            for ind in range(i, j + 1): 
                maxtillnow = max(nums[ind] + pp, p)
                pp = p
                p = maxtillnow
            return p
        if len(nums) == 1: 
            return nums[0]
        return max(helper(1, len(nums) - 1), helper(0, len(nums) - 2))