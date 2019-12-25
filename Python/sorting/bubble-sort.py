def bubbleSort(array):
    # Boolean value to tell whether array is sorted or not
    isSorted = False
    counter = 0
    # While array is not sorted
    while not isSorted:
        # Assume isSorted to be true, now prove false bt traversing array
        isSorted = True
        for i in range(len(array) - 1 - counter):
            # if array is not in current position
            if array[i] > array[i + 1]:
                # Swap values of array at that index position
                swap(i , i+1, array)
                # Reset array to false
                isSorted = False
        #Optimization, we are traversing twice by i and i + 1, so we actually need to increment by 2
        counter += 1
    # Return output sorted array
    return array
# Method to swap two variables
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
