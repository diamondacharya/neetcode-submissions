# 0 --> 0
# 1 --> 1
# 2 --> 10    * 
# 3 --> 11
# 4 --> 100    * 
# 5 --> 101
# 6 --> 110 
# 7 --> 111
# 8 --> 1000      * 
# 9 --> 1001
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1): 
            if i == offset * 2: 
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
