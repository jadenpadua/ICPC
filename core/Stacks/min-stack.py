class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.stack = []

    def push(self, x: int) -> None:
        newMin = {"min": x}
        if len(self.minStack):
            lastMin = self.minStack[len(self.minStack)-1]
            newMin["min"] = min(lastMin["min"],x)
        self.minStack.append(newMin)
        self.stack.append(x)

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]["min"]
        
