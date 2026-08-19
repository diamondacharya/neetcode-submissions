class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        print(counter)
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in counter.items(): 
            freq[val].append(key)
        ret = []
        for i in range(len(nums), 0, -1): 
            for item in freq[i]: 
                ret.append(item)
                if (len(ret) == k): 
                    return ret 
