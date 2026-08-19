import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)        
        for s in strs: 
            counter = [0] * 26
            for char in s: 
                counter[ord(char) - ord('a')] += 1
            d[tuple(counter)].append(s)
        return list(d.values())