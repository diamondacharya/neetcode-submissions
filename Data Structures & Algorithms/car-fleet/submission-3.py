class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed)) 
        zipped.sort(key = lambda x: x[0])
        stack = [] # stores the time it takes to reach the target 
        for i in range(len(zipped) - 1, -1, -1): 
            length = target - zipped[i][0]
            speed = zipped[i][1]
            time = length / speed 
            if len(stack) > 0: 
                rightTime = stack[-1]
                if time > rightTime: 
                    stack.append(time)
            else: 
                stack.append(time)
        return len(stack)

