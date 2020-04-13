# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
            
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        return 1 + max(leftHeight,rightHeight)
    
    def getHeight(self,node):
        
        if node is None:
            return 0
        
        else:
            return 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        
