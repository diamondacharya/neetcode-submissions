import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # stores frequency tuple to string list
        def areAnagrams(s1, s2): 
            c1 = collections.Counter(s1)
            c2 = collections.Counter(s2)
            for i in range(26): 
                if c1[chr(ord('a') + i)] != c2[chr(ord('a') + i)]: 
                    return False
            return True
        for s in strs: 
            l = [0] * 26
            for c in s: 
                l[ord(c) - ord('a')] += 1 
            t = tuple(l)
            if t in d: 
                d[t].append(s)         
            else: 
                d[t] = [s]
        return list(d.values())
