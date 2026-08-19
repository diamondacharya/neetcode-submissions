class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # monotonically decreasing (non-increasing) stack
        for i in range(len(temperatures)): 
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]: 
                poppedIndex = stack.pop()
                res[poppedIndex] = i - poppedIndex
            stack.append(i)
        return  res