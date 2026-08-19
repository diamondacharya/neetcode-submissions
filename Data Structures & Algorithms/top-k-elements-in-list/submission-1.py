import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]
        for item, freq in counter.items(): 
            arr[freq].append(item)
        ret = []
        for i in range(len(nums), 0, -1): 
            for item in arr[i]: 
                ret.append(item)
                if len(ret) == k: 
                    return ret
            
