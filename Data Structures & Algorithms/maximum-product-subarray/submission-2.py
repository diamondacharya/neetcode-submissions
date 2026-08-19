class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)): 
            for j in range(i, len(nums)): 
                subarr = nums[i:j + 1]
                prod = 1
                for item in subarr: 
                    prod *= item
                if prod > res: 
                    res = prod
        return res