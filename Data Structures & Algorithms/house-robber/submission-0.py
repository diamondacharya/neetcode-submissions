class Solution:
    def rob(self, nums: List[int]) -> int:
        p, pp = 0, 0 # prev and prev to prev
        for num in nums: 
            maxtillnow = max(num + pp, p)
            pp = p
            p = maxtillnow
        return p
        