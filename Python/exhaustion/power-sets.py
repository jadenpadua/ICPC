# Given a set of type array, find the power set of that set, a powerset
# is a set of all subsets of thats set
# TC: O(2^n) | SC: O(2^n)
def powerset(array):
    # init our subset array to hold bsae case, which is our empty set
    subsets = [[]]
    # for every element we have in our array
    for element in array:
        # now iterate through our subsets array
        for i in range(len(subsets)):
            # Append [element] + currentSubset to create new subset
            currentSubset = subsets[i]
            subsets.append(currentSubset + [element])
    # Return finished subsets array when done
    return subsets
