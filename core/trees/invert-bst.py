# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        
        while len(queue):
            
            current = queue.pop(0)
            
            if current is None:
                continue
                
            self.swapLeftAndRight(current)
            
            queue.append(current.left)
            queue.append(current.right)
            
            
        return root
            
            
    def swapLeftAndRight(self,current):
        current.left,current.right = current.right, current.left
