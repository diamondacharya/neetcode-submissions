import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        for i in range(26): 
            char = chr(ord('a') + i)
            if (c1[char] != c2[char]): 
                return False
        return True