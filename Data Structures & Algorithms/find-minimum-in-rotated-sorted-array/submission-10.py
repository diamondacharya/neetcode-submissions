class Solution:
    # [1, 2, 3, 4, 5, 6, 7] --> [5, 6, 7, 1, 2, 3, 4]
    def findMin(self, nums: List[int]) -> int:
        l, r, = 0, len(nums) - 1
        while l <= r: 
            mid = l + (r - l) // 2
            if mid >= 1 and nums[mid] < nums[mid - 1]: 
                return nums[mid]
            elif nums[mid] < nums[-1]: 
                r = mid - 1
            else: 
                l = mid + 1
        return nums[0]
            

            

        