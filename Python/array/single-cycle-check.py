# Given a list of integers, return a boolean whether this list has a single cycle
# A single cycle: Think of each integer representing the number of jumps in an array
# When we go out of bounds of the array we can wrap around the array
# A single cycle means that if we keep jumping around the array, we will visit
# every other number exactly once before returning to that original number

# Optimal Solution: O(n) time and O(1) space
def hasSingleCycle(array):
    # Keep track of our numElements visited and currentIdx, initialize
    numELementsVisited = 0
    # note, current index can start anywhere in the array, not just 0
    currentIdx = 0
    # We keep jumping through our elements so as long as the numElements Visted less than array len
    while numELementsVisited < len(array):
        # Case where elements visited is between start and end and we loop back to our starting, this is bad
        if numELementsVisited > 0 and currentIdx == 0:
            # dealing with multiple cycles
            return False
        # increment numElements
        numELementsVisited += 1
        # change index position
        currentIdx = getNextIdx(currentIdx, array)
    # Returns true if cycle is complete and we are back where we started
    return currentIdx == 0
# method that will change our index position, how many indexes do we need to move
def getNextIdx(currentIdx, array):
    # gathers info on how many jumps we need to make based on array index
    jump = array[currentIdx]
    # now calculates current index, moddin array so we wrap around the array
    nextIdx = (currentIdx + jump) % len(array)  
    # need to account for case with negative integers, if less than 0
    # we need to wrap around when nextidx < 0, so we add nextIdx + len(array)
    # for example, moving back -1 in a len 5 array is the same as moving forward 4
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
