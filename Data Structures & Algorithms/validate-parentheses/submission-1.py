class Solution:
    def isValid(self, s: str) -> bool:
       stack = [] 
       d = {')': '(', '}': '{', ']': '['} # close to open
       for char in s: 
            if char in d: # closing parenthesis
                if len(stack) == 0 or stack[-1] != d[char]: 
                    return False
                else: 
                    stack.pop(); 
            else: 
                stack.append(char)
       return len(stack) == 0

