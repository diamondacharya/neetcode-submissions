class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): 
            if (n >> i & 1 == 1): 
                res += 2 ** (31 - i)
        return res