class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums: 
            if (num - 1) not in s: 
                length = 1 
                while (num + 1) in s: 
                    length += 1
                    num += 1
                longest = max(length, longest)
        return longest