import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float('inf')
        tcounter = collections.Counter(t)
        win = collections.defaultdict(int)
        l = 0
        have = 0
        need = len(tcounter.keys())
        for r in range(len(s)): 
            win[s[r]] += 1
            if (s[r] in t and win[s[r]] == tcounter[s[r]]): 
                have += 1
            while have == need: 
                if (r - l + 1 < resLen): 
                    res = [l, r]
                    resLen = r - l + 1
                win[s[l]] -= 1
                if (s[l] in tcounter and win[s[l]] < tcounter[s[l]]): 
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1]


        