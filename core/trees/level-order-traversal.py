# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = self.levelOrderHelper(root,[],0)
        return res
    
    
    def levelOrderHelper(self,node,res,level):
        if node is None:
            return None
        
        if len(res) < level + 1:
            res.append([])
            
        res[level].append(node.val)
        
        self.levelOrderHelper(node.left,res,level+1)
        self.levelOrderHelper(node.right,res,level+1)
        
        return res
