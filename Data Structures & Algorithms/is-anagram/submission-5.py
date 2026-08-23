class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = collections.Counter(s)
        tcounter = collections.Counter(t)
        for char, freq in scounter.items(): 
            if tcounter[char] != freq: 
                return False
        return len(s) == len(t)