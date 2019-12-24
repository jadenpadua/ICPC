class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Class that finds the sum of all values in BST that fall within a range
class Solution:
    def rangeSumBST(self, root: TreeNode, L:int, R: int) -> int:
        # Returns helper method that passes in an addtioanlly, param, our range sum
        return self.rangeSumBSTHelper(root,L,R,0)

    def rangeSumBSTHelper(self,node,L,R,rangeSum):
        # init our range sum
        rangeSum = 0
        # Base case where we encounter None nodes
        if not node:
            return 0
        # init right and left values
        rangeSum = right = left = 0
        # if node val falls into range, set rangeSum to node val
        if L <= node.val <= R:
            rangeSum = node.val
        # if our value is less than left range, we must explore right
        if node.val < L:
            rangeSum += self.rangeSumBSTHelper(node.right,L,R,rangeSum)
        # elif our node value is greater than right range, we must explore left
        elif node.val > R:
            rangeSum += self.rangeSumBSTHelper(node.left,L,R,rangeSum)
        # Case where our range sum is within the range, now we must explore left AND right
        else:
            rangeSum += self.rangeSumBSTHelper(node.left,L,R,rangeSum) + self.rangeSumBSTHelper(node.right,L,R,rangeSum)
        
