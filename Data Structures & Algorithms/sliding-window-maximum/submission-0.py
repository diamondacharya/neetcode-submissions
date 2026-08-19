from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # stores indices such that their values are in monotonically inc. order (MIO)
        res = []
        for i, num in enumerate(nums): 
            while queue and queue[0] <= i - k:  # remove indices that are out of the current window
                queue.popleft()
            while queue and nums[queue[-1]] <= num:  # remove smaller values from the back (maintains MIO)
                queue.pop()
            queue.append(i) # add current index
            if i >= k - 1: 
                res.append(nums[queue[0]])
        return res




