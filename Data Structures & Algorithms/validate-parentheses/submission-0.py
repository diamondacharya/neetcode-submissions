class Solution:
    def isValid(self, s: str) -> bool:
       stack = [] 
       d = {')': '(', '}': '{', ']': '['}
       for char in s: 
            if len(stack) > 0 and char in d and stack[-1] == d[char]: 
                stack.pop(); 
            else: 
                stack.append(char)
       return len(stack) == 0

