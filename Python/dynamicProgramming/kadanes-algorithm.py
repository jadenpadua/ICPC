# Write a function that contains the max sum that can be obatined by
# summing up all the numbers in a non empty subarray (adjacent nums)

#Idea: use DP to get max of subarrays of each index then expand index by one
# until we get to the end
def kadanesAlgorithm(array):
    # init maxSoFar and maxEndingHere as base case
    maxEndingHere = array[0]
    maxSoFar = array[0]
    # Start with array index 1 in array
    for i in range(1, len(array)):
        num = array[i]
        # Our current max ending is the max between all the other elements leading 
        # up to and including num, or num itself
        maxEndingHere = max(num, maxEndingHere + num)
        # Running max Counter that returns the max sum when summing subarray elements
        # of an array, its either the current max so far or the new max ending here calculated,
        # like a global counter
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
