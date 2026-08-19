import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = collections.Counter(t)
        need = len(tcount.keys())
        have = 0 
        window = {}
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)): 
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in tcount and window[c] == tcount[c]: 
                have += 1
            while have == need: 
                if (r - l + 1 < resLen): 
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] = window[s[l]] - 1 
                if s[l] in tcount and window[s[l]] < tcount[s[l]]: 
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1]
            


        