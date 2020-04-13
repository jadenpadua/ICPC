# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        
        # three scenarios
        return max(leftHeight + rightHeight, max(leftDiameter,rightDiameter))
        
    def getHeight(self,root):
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        
