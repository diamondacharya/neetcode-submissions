import collections
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for _, val in c.items(): 
            if val > 1: 
                return True
        return False
