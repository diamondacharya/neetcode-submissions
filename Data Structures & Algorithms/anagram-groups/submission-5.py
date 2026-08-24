class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for str in strs: 
            countArr = [0] * 26
            for char in str: 
                countArr[ord(char) - ord('a')] += 1
            d[tuple(countArr)].append(str)
        return list(d.values())