# Gemini's solution
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1) # dp[i] stores no. of ways to decode first i chars
        dp[0] = 1  # Base case: empty string has one decoding
        for i in range(1, n + 1):
            # Single digit decode
            if s[i-1] != '0':        
                dp[i] += dp[i-1]
            # Two digit decode
            if i >= 2:               
                two_digit_num = int(s[i-2:i])
                if 10 <= two_digit_num <= 26:
                    dp[i] += dp[i-2]
        return dp[n]