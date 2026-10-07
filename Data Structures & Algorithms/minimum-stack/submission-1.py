class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.currMin:
            self.currMin.append(min(val, self.currMin[-1]))
        else:
            self.currMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.currMin.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.currMin[-1] if self.currMin else None
