class Solution:
    # [2, 5, 6, 9] target - 9
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def helper(start, comb, sum): 
            if (sum == target): 
                res.append(comb[:])
                return
            if (sum > target): 
                return
            for i in range(start, len(nums)): 
                comb.append(nums[i])
                helper(i, comb, sum + nums[i])
                comb.pop()
        helper(0, comb, 0)
        return res

            #         comb --> [2, 2, 2, ]
            #         sum --> 6
            #                                 []
            #                             //      \\
            #                 2           5           6           9
            #             / \ \  \      
            #            2  5  6  9      
            #          //\\
            #        2,5,6,9
            #     //\\
            #   2,5,6,9