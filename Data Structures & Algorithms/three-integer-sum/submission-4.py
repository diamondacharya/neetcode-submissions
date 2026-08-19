class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            p = i + 1
            q = len(nums) - 1
            while p < q: 
                summ = nums[i] + nums[p] + nums[q]
                if summ < 0: 
                    p += 1
                elif summ > 0: 
                    q -= 1 
                else: 
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    while p < q and nums[p] == nums[p - 1]: 
                        p += 1
            i += 1   
            while i < len(nums) and nums[i] == nums[i - 1]: 
                i += 1
        return res

