# Given an array of integers, numbers largest range of subsequent numbers in the array
# Runs in O(n) time and O(n) space
def largestRange(array):
    # used to gather global best range variable
    bestRange = []
    # gathers longest length which is used to count the # of subsequent ranges
    longestLength = 0
    # ht of nums which will map each value to the array
    nums = {}
    # Traverse every num in input array
    for num in array:
        # Map each value to the num value in a hashtable and map it to true
        nums[num] = True
    # now retraverse through input array
    for num in array:
        # if number if value has been previously visited by past iteration then continue
        if not nums[num]:
            # Then skip that number
            continue
        # Else we would now set this value to visited    
        nums[num] = False
        # now init our current length to 1
        currentLength = 1
        # now we can expand the numbers to the left and right of our num and see if those values are present in ht
        left = num - 1
        right = num + 1
        # while our left num is still in our ht
        while left in nums:
            # flag that value to false and increment our current length
            nums[left] = False
            currentLength += 1
            # now travel left again
            left -= 1
        # while our right num is still in our ht, do same logic
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1

        # check if currentLength > LongestLength
        if currentLength > longestLength:
            longestLength = currentLength
            # now we put left and right indexes respectively into our best range
            bestRange = [left + 1, right - 1]
            
    return bestRange
