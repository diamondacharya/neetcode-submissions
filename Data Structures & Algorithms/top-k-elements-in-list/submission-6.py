class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = collections.Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for item in countArr: 
            freq[countArr[item]].append(item)
        ret = []
        for i in range(len(freq) - 1, 0, -1): 
            items = freq[i]
            for item in items: 
                ret.append(item)
                if len(ret) == k: 
                    return ret