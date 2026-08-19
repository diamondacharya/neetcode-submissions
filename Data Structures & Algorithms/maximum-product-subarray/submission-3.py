class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        running_max = 1
        running_min = 1
        for num in nums: 
            temp = running_max * num
            running_max = max(running_max * num, running_min * num, num)
            running_min = min(temp, running_min * num, num)
            res = max(res, running_max)
        return res