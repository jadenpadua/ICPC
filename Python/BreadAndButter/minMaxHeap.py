# Class to construct a minimum heap
# Heaps are good to keep track of min or max value
# To access children nodes: let i be index of current node
# First child node: 2i + 1
# Second child node: 2i + 2
# To access parent nodes:
# Parent Node = floor((i- 1) / 2)
class minHeap:
    # init class sets the heap equal to buildHeap() of thay array passed in
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # runs in O(n) time | O(1) space
    # method that turns array into an array that satisfies heap properties
    def buildHeap(self, array):
        # Grab first parent node of the heap, basically parent node ofthe final node we pass in
        firstParentIdx = (len(array) - 2) // 2
        # Now go from the first parent idx and go backwards, starting and parent and building to the top
        for currentIdx in reversed(range(firstParentIdx + 1)):
            # Now call sift down, build all the nodes or children that parent has, and keep going until you reach the start of the array
            self.siftDown(currentIdx, len(array) -1, array)
        return array
    # Function that sifts down heap applying heap property 
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx: # run while loop while there still are children nodes
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            # if there is a child 2 and child 2 is smaller than child one
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]: # For max heap replace this with > sign
                # Now we know our second child is smallest so swap that
                 idxToSwp = childTwoIdx
            # Else just swap child one
            else:
                idxToSwap = childOneIdx
            # if our heap of our index to swap is less than the current index we are on,
            # Thid means the child is less than the parent, this is NOT okay
            if heap[idxToSwap] < heap[currentIdx]: # For max heap replace this with > sign
                # Here we swap our indexes
                self.swap(currentIdx, idxToSwap, heap)
                # Now sift and move that node down
                currentIdx = idxToSwap
                # Now recalculate child one idx
                childOneIdx = currentIdx * 2 + 1
            else:
                break # break when in correct position

    def siftUp(self, currentIdx, heap):
        # Formula that calculates our parent node
        parentIdx = (currentIdx - 1) // 2
        # While we are not at root and the property of a min heap is not satisfied
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx # now sets current index to parent index and goes up
            parentIdx = (currentIdx - 1) // 2 # Finds new parent index
        
    # Returns root node of the heap
    def peak(self):
        return self.heap[0]
    # Functionality for removing the ROOT node of the heap, good for keeping track of greatst or smallest value
    def remove(self):
        # Swap first index to last index
        swap(0, len(self.heap)-1, self.heap)
        # Now pop the last value, which is our root and remove it
        valueToRemove = self.heap.pop()
        # Sifting value that we swapped down to correct position
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove
    # Functionality for inserting a node in the heap
    # WHat we do is add that value to last index of heap
    # Now since that value isn't neccessarily in place, we need to make heap satisfy heap property
    # So we need to sift it up to the correct position
    # This method swaps the node with its parent until satisfies property
    def insert(self, value):
        # so append value to end of heap
        self.heap.append(value)
        # Now sift that value up
        self.siftUp(len(self.heap) - 1, self.heap)

    # function to swap indeces
    def swap(self, i,j, heap):
        heap[i], heap[j] = heap[j], heap[i]
