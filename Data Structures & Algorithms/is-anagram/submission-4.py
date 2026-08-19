class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = Counter(s)
        tcounter = Counter(t)
        if len(scounter.keys()) != len(tcounter.keys()): 
            return False
        for key in scounter.keys(): 
            if scounter[key] != tcounter[key]: 
                return False
        return True
