class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path): # takes the start index and the current path
            res.append(path[:]) # should append a copy of path since it'll be mutated constantly
            for i in range(start, len(nums)): 
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return res

        