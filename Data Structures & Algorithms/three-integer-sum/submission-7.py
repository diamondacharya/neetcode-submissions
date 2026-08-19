class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi: 
                total = nums[i] + nums[lo] + nums[hi] 
                if total < 0: 
                    lo += 1
                elif total > 0: 
                    hi -= 1
                else: 
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < len(nums) - 1 and nums[lo] == nums[lo + 1]: 
                        lo += 1
                    lo += 1
                    hi -= 1
        return res
