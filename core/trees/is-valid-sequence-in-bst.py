# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        stack = []
        paths = []
        paths.append([])
        self.level = 0
        
        allPaths = self.isValidSequenceHelper(stack,root,paths)
        print(allPaths)
        
        return arr in allPaths

    
    
    def isValidSequenceHelper(self,stack,root,paths):
        if root == None:
            return None
        
        stack.append(root.val)
        
        if root.left == None and root.right == None:
            paths.append([])
            for i in range(len(stack)):
                paths[self.level].append(stack[i])
        
            self.level += 1
        
        
        self.isValidSequenceHelper(stack,root.left,paths)
        self.isValidSequenceHelper(stack,root.right,paths)
        stack.pop()
    
        return paths[:len(paths)-1]
