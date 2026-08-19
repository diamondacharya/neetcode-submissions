class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char not in d: 
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != d[char]: 
                return False
        return len(stack) == 0
