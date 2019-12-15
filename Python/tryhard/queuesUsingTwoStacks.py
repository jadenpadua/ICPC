class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # intialize the two stacks and size of queue
        self.pushStack = []
        self.popStack = []
        self.size = 0
        
    # push element to push stack and increase size of queue
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        pushStack.push(x)
    # 
    def pop(self) -> int:
        # If stack we need to pop items from is empty we need to populate it
        self.ensureItemsInPopStack();
        
        """
        Removes the element from in front of queue and returns that element.
        """
        # Keep drawing from our pop stack if the pop stack is not empty
        if popStack.isEmpty == False:
            return popStack.pop()
        
        return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        # Ensure that their are items in pop stack to follow correct order
        self.ensureItemsInPopStack();
        
        # If we have elements in pop stack draw from their
        if popStack.isEmpty == False:
            return popStack.peek()
        
        return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # if both stacks are empty only then do we know our queue is empty
        return pushStack.isEmpty() and popStack.isEmpty()
        
    def ensureItemsInPopStack(self):
        # We need to keep the pop stack being populated to follow correct queue order
        if popStack.isEmpty():
            self.populatePopStack()
    
    def populatePopStack(self):
        # Now we push into the pop stack what we popped from the push stack
        while pushStack.isEmpty == False:
            popStack.push(pushStack.pop())
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
