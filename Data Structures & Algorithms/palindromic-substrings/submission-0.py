class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # handle odd lengthed palindromes
        for ind in range(len(s)): 
            i, j = ind, ind
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                count += 1
                i -= 1
                j += 1
        # handle even lengthed palindromes
        for ind in range(len(s)): 
            i, j = ind, ind + 1
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]: 
                count += 1
                i -= 1
                j += 1
        return count
            
