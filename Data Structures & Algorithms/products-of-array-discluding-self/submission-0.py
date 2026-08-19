class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = 0  #count of zeros
        allprod = 1 
        for num in nums: 
            if num == 0: 
                zc += 1
        if zc == 0: 
            for num in nums: 
                allprod *= num
            for i, val in enumerate(nums): 
                nums[i] = int(allprod / nums[i])
            return nums
        elif zc == 1: 
            for num in nums: 
                if num != 0: 
                    allprod *= num
            for i, val in enumerate(nums): 
                if val != 0: 
                    nums[i] = 0
                else: 
                    nums[i] = allprod
            return nums
        else: # if zc is >1, all entries will be 0
            for i in range(len(nums)): 
                nums[i] = 0
            return nums