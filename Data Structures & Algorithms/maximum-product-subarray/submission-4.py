class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rmax = 1 # running max
        rmin = 1 # running min
        res = float('-inf')
        for num in nums: 
            temp = rmax * num
            rmax = max(rmax * num, rmin * num, num)
            rmin = min(temp, rmin * num, num)
            res = max(res, rmax, rmin)
        return res