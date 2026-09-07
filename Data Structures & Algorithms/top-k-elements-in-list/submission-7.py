class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        farr = [[] for i in range(len(nums) + 1)] # frequency array
        res = []
        for key in counter: 
            farr[counter[key]].append(key)
        for i in range(len(nums), 0, -1): 
            items = farr[i]
            for item in items: 
                res.append(item)
                if len(res) == k: 
                    return res
