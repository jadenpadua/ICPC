# Brute force approach, TC: O(n^2) SC: O(1)
def twoSum1(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []



# Most Time efficient approach, use hashtable
# O(n) time | O(n) space
def twoSum2(array, targetSum):
    nums = {} # ht to store our seen solutions
    for num in array:
        potentialMatch = targetSum - num # map our potential matches to the difference
        if potentialMatch in nums: # if the potential match is in our hashtable, we know we have a pair that matches the sum
            return [potentialMatch, num]   
        # Else map the value to the ht
        else:
            nums[num] = True
    return []

# Most space efficent approach, but tradeoff of time
# O(nlogn) time | O(1) space
def twoSum3(array, targetSum):
    # sort array and two smart pointer approach
    array.sort()
    left = 0 # init right and left pointers
    right = len(array) - 1

    while left < right: # While pointers do not collide
        currentSum = array[left] + array[right] # now sum both ends of array
        if currentSum == targetSum:
            return [array[left], array[right]] # if equal return indeces

        elif currentSum < targetSum: # if targetSum is greater we know we need to move left pointer up
            left += 1
        
        elif currentSum > targetSum: # Same logic
            right += 1
    
    return []



print(twoSum1([3,5,-4,8,11,1,-1,6], 10))
print(twoSum2([3,5,-4,8,11,1,-1,6], 10))
print(twoSum3([3,5,-4,8,11,1,-1,6], 10))
