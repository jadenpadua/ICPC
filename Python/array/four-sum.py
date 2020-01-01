# Calculate 4 numbers in an array that add up to a target sum
# Avg: TC (O(n^2)) because one for loop iterating through all values in array, two other for loops, one iterating after 
# and another iterating before current number, so O(n^2) + O(n^2) = O(2n^2) = O(n^2) b/c drop the constant
# SC: O(n^2) due to the hastable you are storing, storing roughly O(n^2) sums
    
def fourSum(array, targetSum):
    # hashtable stores sums of every pair in the array
    allPairSums = {}
    # holds every single quadruplets array that sums up to the target sum
    quadruplets = []
    # iterate through entire array, we can skip first value in array b/c no values before first value
    # can skip last array value b/c no values after it, slight optimization
    for i in range(1,len(array)-1):
        # iterate through all numbers after our current number
        for j in range(i+1, len(array)):
            # grab current sum (pair) from the two indeces
            currentSum = array[i] + array[j]
            # now apply difference, same logic for two sum here
            difference = TargetSum - currentSum
            # if difference is in our hashtable we know that the two indeces should be added to all arrays in that entry
            if difference in allPairSums:
                # for every pair in that key's values which are arrays, we append
                for pair in allPairSums[difference]:
                    # append preexisting pair and the two new index values into our ouput quadruplets array
                    quadruplets.append(pair + [array[i], array[j]])
        # now look at all numbers before current num
        for k in range(0, i):
            currentSum = array[i] + array[k]
            # now we create new key value pair if not in allPairSums hashtable
            if currentSum not in allPairSums:
                # create new key value pair entry 
                allPairSums[currentSum] = [[array[k], array[j]]]
            # if current Sum already a valid entry in ht, we can append this to preexisting key
            else:
                allPairSums[currentSum].append([array[k], array[i]])
        # return quadruplets output
        return quadruplets
