import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = collections.Counter(s)
        st = collections.Counter(t)
        for char in sc.keys(): 
            if char not in st or sc[char] != st[char]: 
                return False
        for char in st.keys(): 
            if char not in sc or sc[char] != st[char]: 
                return False
        return True