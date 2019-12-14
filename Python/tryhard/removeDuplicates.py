def removeDuplicates(arr):
    uniques = []
    for i in range(len(arr)):
        if arr[i] not in uniques:
            uniques.append(arr[i])
    return uniques

print(removeDuplicates([1,2,2,3,4,5,6,6,6,7,8,89,345,34,43,34]))
