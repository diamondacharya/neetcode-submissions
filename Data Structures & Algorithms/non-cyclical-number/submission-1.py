class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num): 
            output = 0
            while num: 
                digit = num % 10
                square = digit * digit 
                output += square
                num = num // 10
            return output
        seen = set()
        while n != 1: 
            if n in seen: 
                return False
            seen.add(n)
            n = sumOfSquares(n)
        return True
