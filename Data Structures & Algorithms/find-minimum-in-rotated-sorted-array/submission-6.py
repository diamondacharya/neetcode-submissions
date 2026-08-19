# [4, 5, 0, 1, 2, 3]
# -------------- l = 0, r = 5 --------------------
# mid = 0 + 2 = 2
# nums[mid] = 0
# -------------- l = 0, r = 2 --------------------
# mid = 0 + 2 // 2 = 1
# nums[mid] = 5
# # -------------- l = 1, r = 2 --------------------
# mid = 1 + 1//2 = 1
# nums[mid] = 5
# -------------- l = 1, r = 2 --------------------
 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r: 
            mid = l + (r - l) // 2 
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]: 
                return nums[mid]
            if nums[mid] > nums[len(nums) - 1]: # search to the right
                l = mid + 1
            elif nums[mid] < nums[len(nums) - 1]: # search to the left
                r = mid - 1
        return nums[0]