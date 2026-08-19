class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        l = [0] * (n + 1)
        l[1] = 1
        l[2] = 2
        for i in range(3, len(l)): 
            l[i] = l[i - 1] + l[i - 2]
        return l[n]
