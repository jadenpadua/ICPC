# O(n) time | O(n) space
# Function that basically prints nodes in order
def inOrderTraverse(tree, array):
    # Keep traversing until tree is none
    if tree is not None:
        # Explore all the way to the leftmost part of tree
        inOrderTraverse(tree.left,array)
        # Now append tree values after exploring left
        array.append(tree.value)
        # Explore all the way to rightmost part of tree
        inOrderTraverse(tree.right, array)
    # Return output array
    return array
