class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        rsum = 0
        for num in nums: 
            if rsum < 0: 
                rsum = 0
            rsum += num
            res = max(res, rsum)
        return res
            