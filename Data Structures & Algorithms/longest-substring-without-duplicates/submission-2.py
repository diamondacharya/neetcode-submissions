class Solution:
    # "pwwkew" 
        # i, j --> 0, 2
        # sett --> (p, w)
        # maxlen --> 2
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        maxLength = 0
        i, j = 0, 0
        for j in range(len(s)): 
            while(s[j] in sett): 
                sett.remove(s[i])
                i += 1
            sett.add(s[j])
            maxLength = max(maxLength, j - i + 1)
        return maxLength

            

