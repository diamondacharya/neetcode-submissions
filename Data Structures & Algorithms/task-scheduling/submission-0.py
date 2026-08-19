class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)        
        maxHeap = [-count for count in counter.values()] # max-heap stores tasks eligible to run now
        heapq.heapify(maxHeap)
        q = collections.deque() # deque stores (freq, next_eligible_time) tuples for currently ineligible tasks
        t = 0 # tracks time
        while maxHeap or q: 
            if maxHeap: 
                count = heapq.heappop(maxHeap) + 1 # run task and decrement count (we increment coz we store -ve)
                if count != 0: # the task needs to run more times
                    q.append((count, t + n + 1)) # appends (new_count, next_eligible_time)
            if q: 
                next_eligible_time = q[0][1] # next_eligible time for leftmost item in deque
                if next_eligible_time == t + 1: # if item is eligible to run in the next round
                    heapq.heappush(maxHeap, q.popleft()[0]) # pop from deque and push count to heap
            t += 1
        return t