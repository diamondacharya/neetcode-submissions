class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(pos, spd) for pos, spd in zip(position, speed)]
        arr.sort(key = lambda x: x[0])
        stack = []
        for i in range(len(arr) - 1, -1, -1): 
            pos, spd = arr[i]
            currCarTime = (target - pos) / spd
            stack.append(currCarTime)
            if len(stack) >= 2: 
                rightCarTime = stack[-2]
                if currCarTime <= rightCarTime:  # they become fleet so pop currCarTime
                    stack.pop()
        return len(stack)
