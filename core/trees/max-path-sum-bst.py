# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float("-inf")
        self.maxPathSumHelper(root)
        return self.result
    
    def maxPathSumHelper(self,node):
        if not node:
            return 0
        
        left = self.maxPathSumHelper(node.left)
        right = self.maxPathSumHelper(node.right)
        
        max_straight = max(max(left,right) + node.val, node.val)
        max_with_root = max(max_straight, left+right + node.val)
        self.result = max(max_with_root,self.result)
                            
        return max_straight
                            
        
