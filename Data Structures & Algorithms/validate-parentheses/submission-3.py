class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s: 
            if char in d: 
                if (len(stack) == 0): 
                    return False
                if (stack[-1] != d[char]): 
                    return False 
                stack.pop()
            else: 
                stack.append(char)
        return len(stack) == 0