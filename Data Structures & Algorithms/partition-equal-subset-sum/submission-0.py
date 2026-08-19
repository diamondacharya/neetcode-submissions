class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: # odd total, can't parition 
            return False
        s = {0} # set 
        for i in range(len(nums) - 1, -1, -1): 
            copy = set(s)
            for item in s: 
                if nums[i] + item == total // 2: 
                    return True
                copy.add(nums[i] + item)
            s = copy
        return False