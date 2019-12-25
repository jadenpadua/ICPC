# method to search element in array running in O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    # init left and right pointers
    return binarySearchHelper(array, target, 0, len(array) -1)

def binarySearchHelper(array, target, left, right):
    # While pointers to not overlap
    while left <= right:
        # Calculate middle index and map to array
        middle = (left + right) // 2
        potentialMatch = array[middle]
        # Return index where target was found
        if target == potentialMatch:
            return middle
        # if our target is less than our current midpoint, we must cut out the valus to the right
        elif target < potentialMatch:
            right = middle - 1
        # if our target is greater than ourcurrent midpoint, we must cut out values to the left
        else:
            left = middle + 1
    return -1
