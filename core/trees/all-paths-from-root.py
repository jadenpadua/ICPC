# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        stack = []
    
        paths = []
        
        paths.append([])
        self.level = 0
        
        return self.getAllPaths(stack,root,paths)
     
        
    def getAllPaths(self,stack,root,paths):
        
        if root == None:
            return
        
        stack.append(root.val)
        
        if root.left == None and root.right == None:
            paths.append([])
            print(self.level)
            for i in range(len(stack)):
                paths[self.level].append(stack[i])
                
            self.level += 1        
            
        self.getAllPaths(stack,root.left,paths)
        self.getAllPaths(stack,root.right,paths)
        stack.pop()
        
        return paths[:len(paths)-1]
