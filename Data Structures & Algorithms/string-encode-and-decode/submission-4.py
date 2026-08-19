class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            res.append(str(len(s)))
            res.append('|')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s): # check back on the condition
            while s[j] != '|': 
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            j = i
        return res

