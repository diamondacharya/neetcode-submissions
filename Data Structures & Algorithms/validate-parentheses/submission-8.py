class Solution:
    def isValid(self, s: str) -> bool:
        d = {']': '[', ')': '(', '}': '{'}
        stack = []
        for char in s: 
            if char in d: 
                if len(stack) == 0 or (len(stack) > 0 and stack.pop() != d[char]): 
                    return False
            else: 
                stack.append(char)
        return len(stack) == 0
            