class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Function that validates if a BST abides to the property of a BST or not
# Runs in O(n) time where n is the total number of nodes in the BST
# Takes up O(d) space where d is the max depth of the BST
# Idea: Validate the tree we are on then validate subtrees of that tree,
# When exploring left we need to update our max value to be the current node we are on
# When exploring right we need to update our min value to be the current node we are on
def validateBST(tree):
    # Returns a helper method passing in both min and max params, this will be our parent node
    return validateBSTHelper(tree, float("-inf"), float("inf"))
# Helper method checks if tree and all subtrees of that initial tree abide to BST properties
def validateBSTHelper(tree, minValue, maxValue):
    # Base case where wehit the leaves to the tree
    if tree is None:
        return True
    # if exploring right and our tree value is less than min 
    # or if exploring left and our tree is greater than our maxValue
    # we know these cases invalidate BST so return false
    if tree.value < minValue or tree.value >= maxValue:
        return False
    # explore left passing in current tree value as max value next node can be
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    # explore right passing in current tree value as min value next node can be
    rightIsValid = validateBSTHelper(tree.right, tree.value, maxValue)
    # only return true if both BST's are validated
    return leftIsValid and rightIsValid
