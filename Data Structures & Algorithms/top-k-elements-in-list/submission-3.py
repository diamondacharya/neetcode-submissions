class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        freqArr = [[] for i in range(len(nums) + 1)] # indices are frequencies and values the list of items with that freq
        res = []
        for key in counter.keys(): 
            freqArr[counter[key]].append(key)
        for i in range(len(freqArr) - 1, -1, -1): 
            for item in freqArr[i]: 
                res.append(item)
            if len(res) == k: 
                return res

        