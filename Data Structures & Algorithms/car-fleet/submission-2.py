class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(pos, spd) for pos, spd in zip(position, speed)] 
        arr.sort(key = lambda x: x[0])
        stack = []
        for i in range(len(arr) - 1, -1, -1): 
            pos, spd = arr[i]
            time = (target - pos) / spd
            if len(stack) == 0: 
                stack.append(time)
            else: 
                rightCarTime = stack[-1]
                if time <= rightCarTime: 
                    pass
                else: 
                    stack.append(time)
        return len(stack)