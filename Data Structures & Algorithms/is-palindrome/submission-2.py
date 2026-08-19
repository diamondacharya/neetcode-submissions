import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sett = set(string.ascii_lowercase + string.digits)
        i, j = 0, len(s) - 1
        while (i < j): 
            while(i < j and s[i].lower() not in sett): 
                i+= 1
            while(j > i and s[j].lower() not in sett): 
                j-= 1
            if s[i].lower() != s[j].lower(): 
                return False
            i+=1
            j-=1
        return True

