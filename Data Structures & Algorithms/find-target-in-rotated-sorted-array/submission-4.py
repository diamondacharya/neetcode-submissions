class Solution:
    # [1, 2, 3, 4, 5, 6, 7] -- > [4, 5, 6, 7, 1, 2, 3]
    # in the left section
        # if target > nums[-1] and < nums[mid]: search to the left 
        # else search to the right
    # in the right section
        # if target > nums[mid] and < nums[-1]: search to the right
        # else search to the left 
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: 
            mid = l + (r - l) // 2
            if target == nums[mid]: 
                return mid
            elif nums[mid] > nums[-1]:  # in the left section
                if target > nums[-1] and target < nums[mid]: 
                    r = mid - 1
                else: 
                    l = mid + 1
            else: 
                if target > nums[mid] and target <= nums[-1]: 
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1

            

