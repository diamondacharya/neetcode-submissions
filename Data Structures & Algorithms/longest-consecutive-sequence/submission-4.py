class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums: 
            if num - 1 in s: 
                continue
            copy = num
            count = 0
            while copy in s: 
                count += 1
                copy += 1
            res = max(res, count)
        return res
            