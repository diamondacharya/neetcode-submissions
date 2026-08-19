import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = collections.Counter(t) # t counter
        wc = {} # window counter
        i, j = 0, 0
        need = len(tc.values())
        have = 0
        resLen = float('inf')
        resIndices = [0, 0]
        while j < len(s): 
            wc[s[j]] = wc.get(s[j], 0) + 1
            if wc[s[j]] == tc[s[j]]: 
                have += 1
            if have < need: 
                j += 1
                continue
            else: 
                while have == need: 
                    if (j - i + 1) < resLen: 
                        resLen = j - i + 1
                        resIndices = [i, j]
                    wc[s[i]] -= 1
                    if wc[s[i]] == tc[s[i]] - 1: 
                        have -= 1
                    i += 1
                j += 1
        left, right = resIndices
        return s[left:right+1] if resLen < float('inf') else "" # return "" is no sol exists


