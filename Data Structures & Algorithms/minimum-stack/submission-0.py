class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.minStack and self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        
