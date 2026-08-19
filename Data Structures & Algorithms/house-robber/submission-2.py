    # [1, 2, 3, 4, 5, 6, 7] --> nums
# [0,0,0, 0, 0, 0, 0, 0, 0] --> dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        pp, p = 0, 0
        for num in nums: 
            currMax = max(num + pp, p)
            pp = p 
            p = currMax
        return p