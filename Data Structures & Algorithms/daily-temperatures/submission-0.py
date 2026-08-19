class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores (temp, ind) pairs in monotonically non-increasing order or temp
        for ind, temp in enumerate(temperatures): 
            while stack and stack[-1][0] < temp: 
                poppedTemp, poppedInd = stack.pop() # process item when popped
                res[poppedInd] = ind - poppedInd
            stack.append((temp, ind))
        return res