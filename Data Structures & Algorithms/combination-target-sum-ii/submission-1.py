class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(path, total, start): 
            if total == target: 
                res.append(path[:])
                return
            if total > target: 
                return
            for i in range(start, len(candidates)): 
                if i > start and candidates[i] == candidates[i - 1]: # skip processing duplicate elem at the SAME level
                    continue 
                path.append(candidates[i])
                dfs(path, total + candidates[i], i + 1)
                path.pop()
        dfs([], 0, 0)
        return res