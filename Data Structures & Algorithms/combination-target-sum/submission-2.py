            # 2                   5,          6,              9
            # 2,   5,  6,9        2,5,6,9
            #    2,5,6,7            
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, path): # preorder dfs (pass sum down to children)
            if total > target: 
                return     
            if total == target: 
                res.append(list(path))
                return
            for j in range(i, len(nums)): 
                path.append(nums[j])
                dfs(j, total + nums[j], path)
                path.pop()
        dfs(0, 0, [])
        return res
        