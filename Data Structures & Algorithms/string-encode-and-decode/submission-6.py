class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for s in strs: 
            lst.append(str(len(s)) + '|' + s)
        return ''.join(lst)

    "5|Hello5|World"
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s): 
            while s[j] != '|': 
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
            j = i
        return res
