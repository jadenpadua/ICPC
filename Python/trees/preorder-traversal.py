#O(n) time | O(n) space
#Basically appends tree value first, then look left look right
def preOrderTraverse(tree, array):
    # keep traversing until tree is none
    if tree is not None:
        # Append tree value first
        array.append(tree,value)
        # Then look left
        preOrderTraverse(tree.left, array)
        # Finally look right
        preOrderTraverse(tree.right, array)
        # return output array at end
        return array
