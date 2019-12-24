# O(n) time | O(n) space
# Basically fully explore left and right subtrees first before printing out node
def postOrderTraverse(tree, array):
    if tree is not None:
        # First explore left
        postOrderTraverse(tree.left, array)
        # Then explore right
        postOrderTraverse(tree.right, array)
        # Finally append array value
        array.append(tree.value)
    # return output array once built
    return array

