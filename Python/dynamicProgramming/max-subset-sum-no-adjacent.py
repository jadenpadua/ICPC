# Function to find the max sum of a subset in a list when there are no adjacent elemnts
# Idea: Dynamic programming, where at each index in the array we store
# all the possible combinations obtained from that given array index, for example
# index of 2 in our memoized array will store the max non adjacent sum between thre index
# Now keep repeating process until we find optimal sum
# Runs in O(n) time and O(n) space
def maxSubsetSumNoAdjacent(array):
    # Case where we return 0 here if the array is empty
    if not len(array):
        return 0
    # Case where only one element in array so sum is that element
    elif len(array) == 1:
        return array[0]
    # Creates our max sum array which makes it identical to array passed in
    # The values in this array will be updated though
    maxSums = array[:]
    # We do not have to alter array of 0 all possible combinations at that index
    # is just the first number in original array
    # Now intuitively, max sums of 1 is just the max between index 0 and 1,
    # this is because the arrays are right next to each other, we cannot add them 
    maxSums[1] = max(array[0], array[1])
    # Now that we dealt with our base cases, we traverse our original array and update max sums array
    for i in range(2, len(array)):
        # Here is the meat of our algo, we see here that we must compare, what we must
        # compare is, is our maxSums[i - 1] greater than if we add the non adjacent elements together
        # for example, consider array [75,105,120], i is 120, so is 105 > 120 + 75?
        # it is not so we need to update our max sum at that position with the sum of i and i -2 
        # since element is non adjacent
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    # Finally return last index of memoized array to get answer
    return maxSums[-1]
