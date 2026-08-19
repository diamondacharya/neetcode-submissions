class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums: 
            if num - 1 not in s: # start of a sequence
                length = 0
                while num in s: 
                    length += 1
                    num += 1
                res = max(res, length)
        return res
                
        