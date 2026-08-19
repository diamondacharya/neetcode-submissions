import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = collections.Counter(nums)
        countArr = [[] for i in range(len(nums) + 1)]
        for num, count in c.items(): 
            countArr[count].append(num)
        for l in reversed(countArr): 
            for item in l: 
                res.append(item)
            if len(res) == k: 
                return res
        