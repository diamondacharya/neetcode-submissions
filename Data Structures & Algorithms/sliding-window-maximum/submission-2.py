class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(k): 
            heapq.heappush(heap, (-nums[i], i))
        for i in range(k, len(nums)): 
            res.append(-heap[0][0])
            heapq.heappush(heap, (-nums[i], i))
            # remove elements outside the window 
            while heap[0][1] <= i - k: 
                heapq.heappop(heap)
        res.append(-heap[0][0])
        return res
