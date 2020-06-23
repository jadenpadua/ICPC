# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        c = 0
        self.kthLargestHelper(root,k,c)
    
    def kthLargestHelper(self,root,k,c):
        if root is None or c >= k:
            return 
        
        self.kthLargestHelper(root.right, k,c)
        c += 1
        
        if c == k:
            print("K'th largest element is" + str(root.val))
            return
        
        self.kthLargestHelper(root.left,k,c)
        
