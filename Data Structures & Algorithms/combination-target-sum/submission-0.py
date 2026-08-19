class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(comb, total, start): 
            if total == target: 
                res.append(list(comb))
                return
            if total > target: 
                return
            for i in range(start, len(nums)): 
                comb.append(nums[i])
                dfs(comb, total + nums[i], i)
                comb.pop()
        dfs([], 0, 0)
        return res