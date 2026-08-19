class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcounter = collections.Counter(t)
        need = len(tcounter.keys())
        have = 0
        l = 0
        d = {}
        res = float('inf')
        resLeft, resRight = 0, 0
        for r in range(len(s)): 
            d[s[r]] = d.get(s[r], 0) + 1
            if s[r] in tcounter and d[s[r]] == tcounter[s[r]]: 
                have += 1
            while have >= need: 
                if (r - l + 1) < res: 
                    res = r - l + 1
                    resLeft = l
                    resRight = r
                if s[l] in tcounter and d[s[l]] == tcounter[s[l]]: 
                    have -= 1
                d[s[l]] -= 1
                l += 1
        return "" if res == float('inf') else s[resLeft: resRight + 1]
