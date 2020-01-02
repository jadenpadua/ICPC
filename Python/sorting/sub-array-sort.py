# Write a function that takes returns the indeces of the smallest subarray in an input array
# that needs to be sorted in place in order for the entire input array to be sorted
# TC: O(n) b/c we have to traverse all nums in array | SC: O(1) b/c in place not allocating any space
def subarraySort(array):
    # init our min and max unsorted numbers so we can use them later
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    # now go through our entire input array
    for i in range(len(array)):
        num = array[i]
        # check if this current number is out of order in regards to its left and right nums
        if isOutOfOrder(i ,num,array):
            # if the number is out of order we update our min and max out of order variablesx
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    # if the values remain infinity we know array was sorted already
    if minOutOfOrder == float("inf"):
        return [-1,-1]
    #  now we need to look left and find where minOutOfOrder belongs in input array
    subarrayLeftIdx = 0
    # keeps incrementing our left idx until we get  to correct sorted position in input array
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    
    subarrayRightIdx = len(array) - 1
    # same logic but for right index
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    # return array of the indeces of the correct positions of the min and max order array, everything in between is the subarray that needs to be sorted
    return [subarrayLeftIdx,subarrayRightIdx]

# compare num to its two adjacent numbers
def isOutOfOrder(i, num, array):
    #case where its the first num in array
    if i == 0:
        return num > array[i+1]
    # case where its the last number in the array
    if i == len(array) - 1:
        return num < array[i-1]
    
    # case where we are returning two adjacent numbers
    # if num is greater than leading num or smaller than trailing num we know its out of order
    return num > array[i + 1] or num < array[i - 1]
