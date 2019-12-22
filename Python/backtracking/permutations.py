# Time Complexity: n factorial permutations where n is the number of integers in the list, but every permutation has n numbers,
# so TC would be O(n*n!) 
# Space Complexity: also O(n*n!) elements in the storage array
# This is because pos 1: 1/n possibilities * pos 2: 1/(n-1) possibilities * pos 3: 1/(n-2) possibilities
def getPermutations(array):
    permutations = [] # Resultant permutation array
    permutationsHelper(array, [], permutations) # Driver code to kick off our backracking
    return permutations # Return resultant permutation

def permutationsHelper(array, currentPermutation, permutations):
    #If resulting array is None and we have a current permutation len, we know to append to output
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    
    else:
        #Iterate through array and all subarrays, exhaust all possibilities
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:] # temporaily take out array[i]
            newPermutation = currentPermutation + [array[i]] # append the cut out part to our new perm
            permutationsHelper(newArray, newPermutation, permutations)
            # Now we recurse deeper, our newArr becomes the currrent array we draw from, our new perm gets the
            # current perm, and we pass in our resulting permutations array
