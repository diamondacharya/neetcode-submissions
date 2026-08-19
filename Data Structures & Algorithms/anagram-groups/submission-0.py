from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs: 
            count_arr = [0] * 25
            for c in s: 
                count_arr[ord(c) - ord('a')] += 1 
            d[tuple(count_arr)].append(s)
        return d.values()
         