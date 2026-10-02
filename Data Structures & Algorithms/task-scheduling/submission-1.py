class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [-1 * val for val in counter.values()] # invariant: heap will always store freqs for tasks ELIGIBLE to run
        heapq.heapify(heap)
        t = 0
        d = deque() # stores freqs with their next eligible run time
        while heap or d: 
            if len(heap) > 0: 
                freq = -1 * heapq.heappop(heap)
                if freq >= 2: 
                    d.append((freq - 1, t + n + 1))
            if len(d) > 0 and d[0][1] == t + 1: 
                heapq.heappush(heap, -1 * d.popleft()[0])
            t += 1
        return t
        

