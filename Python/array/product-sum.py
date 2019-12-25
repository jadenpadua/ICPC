# Function that takes sin an array, add elements, however if array is in another array,
# increase multiplier, multiply that inner array by that multiplier and add that

#O(n) time | O(d) space - where n is total num of array elements, O(d) space
# is the call stack in the recursion that is the greatest depth we need to recurse through
# init array with multiplier to 1
def productSum(array, multiplier=1):
    # running counter of our total sum
    prodSum = 0
    # Iterate through every element within array
    for element in array:
        # Checking if we must apply our prod sum rule here
        if type(element) is list:
            # now recurse into that inner array, increasing our multiplier
            prodSum += productSum(element, multiplier + 1)
            # else just simply increment running prodSum
        else:
            prodSum += element
    # Now at the end mult sum by the multiplier, in case we recurse deeper this is what we must return when
    # we bubbly back up to the top
    return prodSum * multiplier
