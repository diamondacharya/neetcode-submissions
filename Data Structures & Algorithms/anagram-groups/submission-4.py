class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs: 
            l = [0] * 26
            for char in s:
                l[ord(char) - ord('a')] += 1  
            d[tuple(l)].append(s)
        return list(d.values())