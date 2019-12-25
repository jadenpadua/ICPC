# Given a number, move all instances of that number to end of array
# We have to do this in place
# Also, so as long as the elements are at the end of the array, the non
# instances of that element can be in any order

# Idea: keep track of two pointers, one at the beggining of array and one at end of array
# need this because this is how we are swapping values, check if j is num we want to remove, 
# if it is then we want to shift j to the left

# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # two pointers, one at start one at end
    i = 0
    j = len(array) - 1
    # When pointers overlap, that means array is fully traversed
    while i < j:
        # Case where we do not need to move an element already at the end, so decrement j
        # need bounds checking here so pointer j does not keep decrementing after array was traversed
        while i < j and array[j] == toMove:
            j -= 1
        # if the start pointer is equal to our target value, then we can swap bc our array[j] is not a target value
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        # Now increment i b/c all possible was done in this case
        i += 1
    # now return output array
    return array

