class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1: 
            if n in seen: 
                return False
            seen.add(n)
            sum = 0
            copy = n
            while copy: 
                sum += (copy % 10) * (copy % 10)
                copy = copy // 10
            n = sum
        return True