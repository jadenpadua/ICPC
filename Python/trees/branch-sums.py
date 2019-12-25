# A branch is a path that goes from the root node to leaf node
# Idea: calculate branch sums of the "rooted" node of a particular branch
# But keep a running sum of the total branch sum

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Method returns a list of sums of all branches in tree
def branchSums(root):
    sums = [] # init our sums list
    # Call calculate branch sums, pass in running sum and sums list
    calculateBranchSums(root, 0, sums)
    return sums
# O(n) time | O(n) space, we have to traverse through all elements in the list
# Also we are returning all branches in a tree which is equal to all the lead nodes in BST, so 1/2N = N
def calculateBranchSums(node, runningSum, sums):
    # Case where we recurse and a node has one child, if we go into a none Node return nothing
    if node is None:
        return

    # Calculate current running sum of that particular branch
    newRunningSum = runningSum + node.value
    # Case where we are at a leaf node, no more children so just return the running sum here
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    # Now depth first search, explore all neighbors and add to running some until we find leafs
    calculateBranchSums(node.left, newRunningSum,sums)
    calculateBranchSums(node.right, newRunningSum, sums)
