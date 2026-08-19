class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, path): # takes the start index and the current path
            res.append(path[:]) # append a COPY
            for i in range(start, len(nums)): 
                if i > start and nums[i] == nums[i - 1]: # skip duplicate at SAME recursion level
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return res