# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = []
        level = 0
        ht = dict()
        self.isCousinsHelper(root,level,x,y,ht)
        
        if len(ht) != 2:
            return False
        
        arr = []
        for value in ht.values():
            arr.append(value)
            
        if arr[0] == arr[1]:
            return True
        
        return False
    
    def isCousinsHelper(self,node,level,x,y,ht):
        if node is None:
            return
        
        if node.left is not None:
            if node.left.val == x:
                ht[node.val] = level
                
            elif node.left.val == y:
                ht[node.val] = level
        
        if node.right is not None:
                
            if node.right.val == x:
                ht[node.val] = level
            
            elif node.right.val == y:
                ht[node.val] = level
    
        self.isCousinsHelper(node.left,level+1,x,y,ht)
        self.isCousinsHelper(node.right,level+1,x,y,ht)
