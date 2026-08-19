class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = 0  
        for num in nums: 
            if num == 0: 
                zc+= 1
        allprod = 1
        if (zc == 0): 
            for num in nums: 
                allprod *= num
            for i in range(len(nums)): 
                nums[i] = int(allprod / nums[i])
            return nums
        elif (zc == 1): 
            for num in nums: 
                if num != 0: 
                    allprod *= num
            for i in range(len(nums)): 
                if nums[i] == 0: 
                    nums[i] = allprod
                else: 
                    nums[i] = 0
            return nums
        else: 
            for i in range(len(nums)): 
                nums[i] = 0
            return nums
        