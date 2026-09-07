class Solution:
    # [1, 2, 4, 6]
    # prearr = [1, 1, 2, 8]
    # postarr = [48, 24, 6, 1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preArr = [1] * len(nums)
        postArr = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)): 
            preArr[i] = preArr[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1): 
            postArr[i] = postArr[i + 1] * nums[i + 1]
        for i in range(len(nums)): 
            res[i] = preArr[i] * postArr[i]
        return res

