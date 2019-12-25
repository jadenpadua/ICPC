# Keep dividing into halves until we get one element in each subarray,
# Then bubble back up and merge and sort subarrays, eventually building
# back up to a full sorted array
# Dividing the subarrays is an O(n) operation
# Now merging them together and adding them up is also an O(n) operation
# These operations above are for first array (creating first two and sorting and merging)
# Now all of the other sub arrays would take O(log(n)) time to creat and merge back together
# Both operations together would become an O(nlog(n)) operation for both time and space
def mergeSort(array):
    # Base case where a subarray is of length 1, so bubble back up
    if len(array) == 1:
        return array
    # Calculate middle index of current array and round down
    middleIdx = len(array) // 2
    # Slice left and right halves of the array
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    # Now we want to further divide these two halves so call helper method
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))
# Takes the two individually sorted arrays and merges them into one
def mergeSortedArrays(leftHalf, rightHalf):
    # Build up to this array and populate expected length with none values
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    # k is pointer for sortedArray, i is pointer for left, j is pointer for right
    k = i = j = 0
    # While left half still has a pointer and right half still has a pointer
    while i < len(leftHalf) and j < len(rightHalf):
        # Now if index is less in left half 
        if leftHalf[i] <= rightHalf[j]:
            # Set k idx to left half
            sortedArray[k] = leftHalf[i]
            # Increment left half
            i += 1
        else:
            # Else is when right half smaller, so similiar logic
            sortedArray[k] = rightHalf[j]
            j += 1
        # increment k pointer
        k += 1
    # if there are extra elements in left half
    while i < len(leftHalf):
        # Append remaining elements into sorted array
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    # same case but for right half
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[i]
        j += 1
        k += 1
    # Return sorted version of sorted array to bubble back up and sort again
    return sortedArray
