class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        for key, val in sc.items(): 
            if tc[key] != val: 
                return False
        return len(sc.keys()) == len(tc.keys()) 


