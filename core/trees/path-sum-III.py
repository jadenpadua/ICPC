# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.numOfPaths = 0
        self.dfs(root,target)
        
        return self.numOfPaths
    
    def dfs(self,node,target):
        if node is None:
            return
        
        self.test(node,target)
        self.dfs(node.left,target)
        self.dfs(node.right,target)
    
    def test(self,node,target):
        if node is None:
            return
        
        if node.val == target:
            self.numOfPaths += 1
        
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
