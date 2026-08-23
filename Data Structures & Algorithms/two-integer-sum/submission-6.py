class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d={1:0, 3:1, 4:2, 2:3}
        d = {}
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in d: 
                return [d[diff], i]
            d[num] = i
        
        