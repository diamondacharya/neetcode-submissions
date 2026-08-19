class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n): 
            if x == 0: 
                return 0
            if n == 0: 
                return 1
            res = helper(x, n//2) 
            res = res * res
            return res if n % 2 == 0 else x * res # handle odd/even case
        output = helper(x, abs(n))  # make sure to pass in the abs val
        return output if n >= 0 else 1/output