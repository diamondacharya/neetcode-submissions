class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26
        for char in s: 
            l1[ord(char) - ord('a')] += 1
        for char in t: 
            l2[ord(char) - ord('a')] += 1
        return l1 == l2 