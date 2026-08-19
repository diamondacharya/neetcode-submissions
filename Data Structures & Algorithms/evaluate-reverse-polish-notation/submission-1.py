class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token == '+': 
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == '*': 
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif token == '-': 
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '/': 
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: 
                stack.append(int(token))
        return stack[-1]

            