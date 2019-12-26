# Given an array, return triplets that add up to the target sum
# Idea: three pointers, let i = beggining of array, left = i + 1,
# right = len(array) - 1, sum all three and find sum == target, if not
# then increase left pointer if targetSum is greater, right pointer if 
# targetSum is less
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    # need this to be preformed on a sorted array
    array.sort()
    triplets = []
    # iterate through array - 2 b/c we are comparing 3 values
    for i in range(len(array) - 2):
        # Define left and right pointers
        left = i + 1
        right = len(array) - 1
        # Until array overlaps do this
        while left < right:
            # Calculate current sum from values of three pointers
            currentSum = array[i] + array[left] + array[right]
            # if triplets are a match append to output, array, update both pointers
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            # if our currentSum is more than target, increase only rright pointer and try again
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets
