class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # stores the minimum till that index
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minstack) == 0):  
            self.minstack.append(val)
        else: 
            self.minstack.append(min(self.minstack[-1], val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        if (len(self.stack) > 0): 
            return self.stack[-1]
        else: 
            return None
        
    def getMin(self) -> int:
        if (len(self.minstack) > 0): 
            return self.minstack[-1]
        else: 
            return None
        
