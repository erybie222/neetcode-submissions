class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.stack:
            if val == self.minVal:
                self.minVal = min(self.stack)
        else:
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal

