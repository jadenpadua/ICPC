# Idea, iterate through an array with a pointer on each index, find min element and swap with that index
# O(n^2) time | O(1) space
def selectionSort(array):
    # Idx that will iterate through our array
    currentIdx = 0
    # Breaks when array is fully traversed
    while currentIdx < len(array) - 1:
        # At each iteration, initially smallest idx to current idx
        smallestIdx = currentIdx
        # Now iterate from our pointer index to the end of the array
        for i in range(currentIdx + 1, len(array)):
            # Update value of smallestIdx when we encounter a smaller element
            if array[smallestIdx] > array[i]:
                smallestIdx = i
            # Now after smallestIdx is found, prform a swap
            swap(currentIdx, smallestIdx, array)
            # Increment our pointer for current index
            currentIdx += 1
    return array
