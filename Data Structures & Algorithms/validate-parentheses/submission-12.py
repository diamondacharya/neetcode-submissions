class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}': '{', ']': '[', ')': '('}
        for char in s: 
            if char not in d: # opening brace 
                stack.append(char)
            elif len(stack) == 0 or (len(stack) > 0 and stack.pop() != d[char]): 
                    return False
        return len(stack) == 0
