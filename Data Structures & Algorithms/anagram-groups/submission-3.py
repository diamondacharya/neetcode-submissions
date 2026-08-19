import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # stores frequency tuple to string list
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
