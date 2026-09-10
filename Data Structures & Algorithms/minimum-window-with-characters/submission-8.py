class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = collections.Counter(t)
        wincount = {}
        need = len(tcount.keys())
        have = 0
        l = 0
        resLeft, resRight = 0, 0
        shortest = float('inf')
        for r in range(len(s)): 
            wincount[s[r]] = wincount.get(s[r], 0) + 1
            if s[r] in tcount and wincount[s[r]] == tcount[s[r]]: 
                have += 1
            while need == have: 
                length = r - l + 1     
                if length < shortest: 
                    shortest = min(shortest, length)
                    resLeft = l
                    resRight = r
                if s[l] in tcount and wincount[s[l]] == tcount[s[l]]: 
                    have -= 1
                wincount[s[l]] -= 1
                l += 1
        return "" if shortest == float('inf') else s[resLeft: resRight + 1]
