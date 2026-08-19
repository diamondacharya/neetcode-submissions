class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False                
        s1Counter = [0] * 26
        s2Counter = [0] * 26
        for char in s1: 
            s1Counter[ord(char) - ord('a')] += 1
        for char in s2[:len(s1)]: 
            s2Counter[ord(char) - ord('a')] += 1
        if s1Counter == s2Counter: 
            return True
        for i in range(len(s1), len(s2)): 
            s2Counter[ord(s2[i]) - ord('a')] += 1 # shift right pointer to right
            s2Counter[ord(s2[i - len(s1)]) - ord('a')] -=1 # shift left pointer to right so window becomes valid size again 
            if s1Counter == s2Counter: 
                return True
        return False
        


        
        

