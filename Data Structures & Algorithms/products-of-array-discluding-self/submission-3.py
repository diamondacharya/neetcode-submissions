class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # nums -->   [6, 2, 3, 4, 5]
        # prefix --> [1, 6, 12, 36, 144]
        # suffix --> [120, 60, 20, 5, 1]
        
        for i in range(len(nums)):
            if i != 0: 
                prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1): 
            if i != (len(nums) - 1): 
                suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(len(nums)): 
            nums[i] = prefix[i] * suffix[i]
        return nums
        
        

