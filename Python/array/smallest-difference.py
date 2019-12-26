# Function takes two arrays, computes smallest difference between two arrays
# Idea: Sort both arrays, two pointers at both starts the both arrays,
# if array[idxOne] is greater than array[idxTwo], we know to increase second number
# likewise if array2[idx] is greater, we need to increase first number
# O(nlog(n) + mlog(n)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # make sure both arrays are sorted first
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0 # create start pointers for both array's
    # Now now create our current difference and a running  total of smallest difference
    smallest = float("inf")
    current = float("inf")
    smallestPair = [] # running pair of smallest pair
    # While both of the two pointers do not reach the end of both arrays
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        # calculate the numbers at these index positions
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        # Case when second num is greater than first num, we increment first number to get a smaller difference
        if firstNum < secondNum:
            # Calculate our current 
            current = secondNum - firstNum
            # increment our first index
            idxOne += 1
        # Case where first num is greater than second num, we increment second num to get a smaller difference
        elif secondNum < firstNum:
            # calculate our current
            current = firstNum - secondNum
            idxTwo += 1
            # Else is when first num == second num, this by default is the smallest pair
        else:
            return [firstNum, secondNum]
        # Check if our current is less than our global smallest 
        if smallest > current:
            # if so set smallest equal to that, and also the smallest pair equal to the indexes
            smallest = current
            smallestPair = [firstNum, secondNum]
    # now return smallest pair possible
    return smallestPair
