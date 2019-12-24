# Program to find closest value in BST given a target
def findClosestValueInBst(tree, target):
    # helper method that also incorporates a closest target 
    return findClosestValueInBstHelper(tree,target, float("inf"))

# Running an average of O(log(n)) time | O(1) space due to dividing in half nature of tree
def findClosestValueInBstHelper(tree,target,closest):
    # Set current node equal to tree or root node passed in
    currentNode = tree
    # Iterate through tree until None value
    while currentNode is not None:
        # If distance between currentNode is less than update closest
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        # explore left of tree and disregard right
        if target < currentNode.value:
            currentNode = currentNode.left
        # explore right of tree and disregard lefts
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break # case where target is equal to closest
    return closest
