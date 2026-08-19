class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minimum_stack or self.minimum_stack[-1] >= value:
            self.minimum_stack.append(value)


    def pop(self) -> None:
        if self.stack:
            value = self.stack.pop()
        if value == self.minimum_stack[-1]:
            self.minimum_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.minimum_stack[-1] if self.minimum_stack else None
        