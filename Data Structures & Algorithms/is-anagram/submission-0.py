class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        for char in s: 
            if char in d: 
                d[char] += 1
            else: 
                d[char] = 1
        for char in t: 
            if char in d2: 
                d2[char] += 1
            else: 
                d2[char] = 1
        for char in d.keys(): 
            if char not in d2 or d[char] != d2[char]: 
                return False
        for char in d2.keys(): 
            if char not in d or d[char] != d2[char]: 
                return False
        return True
        
