class Solution:
    # stack = [(0, 30),]
    # res = [0, 0, 0, 0, 0, 0, 0]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores (idx, temp) tuples
        res = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            temp = temperatures[i]
            while len(stack) > 0 and temp > stack[-1][1]: 
                lastInd, lastTemp =  stack.pop()
                res[lastInd] = i - lastInd
            stack.append((i, temp))
        return res