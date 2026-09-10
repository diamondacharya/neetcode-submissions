class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        for r in range(len(s)): 
            while s[r] in sett: 
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            longest = max(longest, len(sett))
        return longest

