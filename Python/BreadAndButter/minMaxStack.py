# Class of stack that supports finding min max of stack
# All operations here are O(1) time | O(1) space
class MinMaxStack:
    # The key here is to create two stacks
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
    # peek elements from stack
    # O(1) time | O(1) space
    def peek(self):
        # Return top of stack
        return self.stack[len(self.stack)-1]
    # pop element from top of BOTH stacks
    def pop(self):
        # must pop min max stack
        self.minMaxStack.pop()
        return self.stack.pop()
    # Push element to stack, also to minMaxStack
    def push(self,number):
        # Create new ht entry with a min and a max to the number
        newMinMax = {"min": number, "max": number}
        # if there is a last entry to compare in min max stack
        if len(self.minMaxStack):
            # our last min max numbers to compare
            lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
            # new min and max updated values after comparison
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max", number])
        # Append updated minMax ht entry to our stack,
        self.minMaxStack.append(newMinMax)
        # now push regular number to a stack
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["min"]
    
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
