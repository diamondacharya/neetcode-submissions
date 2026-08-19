class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max(nums)
        def findmax(i, j): 
            pp, p = 0, 0
            for ind in range(i, j + 1): 
                currMax = max(nums[ind] + pp, p)
                pp = p
                p = currMax
            return p
        excludeFirst = findmax(1, len(nums) - 1)
        excludeLast = findmax(0, len(nums) - 2)
        return max(excludeFirst, excludeLast)