# Idea: Mark first element as unsorted, iterate through array, now grab that current
# element we are iterating are and insert it in correct position in sorted array, 
def insertionSort(array):
    # iterate through entire array, starting at index 1
    for i in range(1, len(array)-1):
        # Create var j to stay at index that i is on
        j = i
        # This is for iterating through the already sorted array, 
        # swap if value on left is greater else decrement j until 0
        while j > 0 and and array[j-1] > array[j]:
            swap(j,j-1,array)
            # decrement our j until reaches 0
            j -= 1
    return array

def swap(i,j,array):
    array[i],array[j] = array[j], array[i]
