class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = [0] * 26
        s2counter = [0] * 26
        for char in s1: 
            s1counter[ord(char) - ord('a')] += 1
        for char in s2[:len(s1)]: 
            s2counter[ord(char) - ord('a')] += 1
        if s1counter == s2counter: 
            return True
        for i in range(len(s1), len(s2)): 
            toAdd = s2[i]
            toRemove = s2[i - len(s1)]
            s2counter[ord(toAdd) - ord('a')] += 1
            s2counter[ord(toRemove) - ord('a')] -= 1
            if s1counter == s2counter: 
                return True
        return False



