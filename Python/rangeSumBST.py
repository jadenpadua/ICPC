# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.rangeSumBSTHelper(root,L,R,0)
    
    
    def rangeSumBSTHelper(self,node,L,R,rangeSum):
        rangeSum = 0
        if not node:
            return 0
        
        rangeSum = right = left = 0
        
        if L <= node.val <= R:
            rangeSum = node.val
        
        if node.val < L:
            rangeSum += self.rangeSumBSTHelper(node.right,L,R,rangeSum)
        elif node.val > R:
            rangeSum += self.rangeSumBSTHelper(node.left,L,R,rangeSum)
        else:
            rangeSum += self.rangeSumBSTHelper(node.left,L,R,rangeSum) +  self.rangeSumBSTHelper(node.right,L,R,rangeSum)
        
        return rangeSum
            
