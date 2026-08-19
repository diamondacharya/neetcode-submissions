class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        visited = set()
        def dfs(): 
            if len(path) == len(nums): 
                res.append(path[:]) # make sure to append a COPY
                return
            for i in range(len(nums)): 
                if nums[i] not in visited: 
                    visited.add(nums[i])
                    path.append(nums[i])
                    dfs()
                    popped = path.pop()
                    visited.remove(popped)
        dfs()
        return res