class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1 # product excluding zeroes 
        zeroCount = 0
        for num in nums: 
            if num == 0: 
                zeroCount += 1
            else: 
                prod *= num
        res = [0] * len(nums)
        for i, num in enumerate(nums): 
            if zeroCount == 0: 
                res[i] = int(prod / num)
            elif zeroCount == 1: 
                res[i] = 0 if num != 0 else prod
            else: 
                res[i] = 0
        return res
            
        
        