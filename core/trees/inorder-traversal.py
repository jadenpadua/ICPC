# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        return self.inorderTraversalHelper(root,res)
    
    def inorderTraversalHelper(self,node,res):
        if node is None:
            return
        self.inorderTraversalHelper(node.left,res)
        res.append(node.val)
        self.inorderTraversalHelper(node.right,res)
        return res
        
