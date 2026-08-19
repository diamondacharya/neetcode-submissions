class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j): # i is the ind in s and j the index in t
            if j == len(t): # subsequence found
                return 1
            if i == len(s): # s is exhausted, but not t (so no subsequence here)
                return 0
            if (i, j) in cache: 
                return cache[(i, j)]
            count = dfs(i + 1, j)
            if s[i] == t[j]: 
                count += dfs(i + 1, j + 1)
            cache[(i, j)] = count
            return count
        return dfs(0, 0)