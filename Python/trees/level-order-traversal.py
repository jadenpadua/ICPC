class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Solution to provide a level order traversal of a BST
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Driver code passes in helper that has our root node, res array, and level
        res = self.levelOrderHelper(root, [], 0)
        return res
    
    def levelOrderHelper(self,node,res,level):
        # Base case in recursion where we have hit the end of our leaves
        if node is None:
            return None
        # Used in order to decide to enter a new level index
        if len(res) < level + 1:
            res.append([])
        
        # Append current node value to the specific level the recursion is on
        res[level].append(node.val)
        # Depth first search, recurse through left and right neighbord
        self.levelOrderHelper(node.left, res, level+1)
        self.levelOrderHelper(node.right,res, level+1)
        # Now when recursion done return resulting 2d array
        return res

