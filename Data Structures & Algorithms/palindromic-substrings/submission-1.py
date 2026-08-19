class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for ind in range(len(s)): 
            i, j = ind, ind
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                res += 1
                i -=1
                j += 1
        for ind in range(len(s)): 
            i, j = ind, ind + 1
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                res += 1
                i -=1
                j += 1
        return res