class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for s in strs: 
            l.append(str(len(s)) + '|' + s)
        return ''.join(l)

    # 21|
    def decode(self, s: str) -> List[str]:
        ret = []
        i = j = 0
        while i < len(s): 
            j = i 
            while s[j] != '|': 
                j += 1
            length = int(s[i:j])
            ret.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ret
