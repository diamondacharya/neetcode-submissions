class Solution:
    # [1, 2, 3]
    # pre = [1, 1, 2, 6]
    # post = [6, 6, 3, 1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * (len(nums) + 1)
        post = [1] * (len(nums) + 1)
        res = [0] * len(nums)
        for i in range(1, len(pre)): 
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(post) - 2, -1, -1): 
            post[i] = post[i + 1] * nums[i]
        for i in range(len(nums)): 
            res[i] = pre[i] * post[i + 1]
        return res