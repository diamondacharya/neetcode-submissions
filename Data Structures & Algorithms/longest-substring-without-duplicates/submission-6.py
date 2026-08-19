class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sett = set()
        i, j = 0, 0                
        while j < len(s): 
            if s[j] not in sett: 
                sett.add(s[j])
                res = max(res, j - i + 1)
            else: 
                while s[i] != s[j]: 
                    sett.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return res
                
