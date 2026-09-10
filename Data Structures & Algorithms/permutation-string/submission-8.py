class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1freq = [0] * 26
        for char in s1: 
            s1freq[ord(char) - ord('a')] += 1
        winfreq = [0] * 26
        for i in range(len(s1)): 
            winfreq[ord(s2[i]) - ord('a')] += 1
        if s1freq == winfreq: 
            return True
        for i in range(len(s2) - len(s1)): 
            winfreq[ord(s2[i]) - ord('a')] -= 1
            winfreq[ord(s2[i + len(s1)]) - ord('a')] += 1
            if s1freq == winfreq: 
                return True
        return False



            