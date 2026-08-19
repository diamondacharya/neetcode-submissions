class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # caches values for (i, total) keys so we don't recompute same subproblem 
        def dfs(i, total): 
            if (i, total) in cache: 
                return cache[(i, total)]
            if i == len(nums): 
                return total == target
            cache[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return cache[(i, total)]
        return dfs(0, 0) 

        