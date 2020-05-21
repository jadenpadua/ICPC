# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 0
        self.k = k
        self.res = 0
        self.inOrder(root)
        return self.res
    
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            self.inOrder(node.right)
    
