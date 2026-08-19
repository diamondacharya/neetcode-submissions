class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1: # no need to jump from last index
            farthest = 0 # farthest ind reacheable from this level
            for i in range(l, r + 1): 
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest 
            res += 1
        return res
