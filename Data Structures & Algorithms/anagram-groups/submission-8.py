class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs: 
            arr = [0] * 26
            for char in s: 
                arr[ord(char) - ord('a')] += 1
            d[tuple(arr)].append(s)
        return list(d.values())