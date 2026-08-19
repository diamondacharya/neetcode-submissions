class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0
        for ind in range(len(s)): 
            i, j = ind, ind
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                if (j - i + 1) > (r - l + 1): 
                    l = i
                    r = j
                i -= 1
                j +=1 
        for ind in range(len(s)): 
            i, j = ind, ind + 1
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                if (j - i + 1) > (r - l + 1): 
                    l = i
                    r = j
                i -= 1
                j +=1 
        return s[l:r+1]
            

