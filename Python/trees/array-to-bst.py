class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Class converts an array to a binary search tree
class Solution(object):
    # Takes in an array of nums and converts to a BST
    def arrayToBST(self, nums):
        # Array needs to be sorted, this is a MUST
        nums.sort()
        # Base case that handles when we have no more nums in our nums array
        if not nums:
            return None
        # Calculate midpoint of our current tree
        mid = len(nums) // 2
        # Create a root of that current tree, build a tree node object here
        root = TreeNode(nums[mid])
        # Now find all of the children of that root, (left and right)
        root.left = self.arrayToBST(nums[:mid]) # left children are all smaller so all numbers up to mid
        root.right = self.arrayToBST(nums[:mid]) # right children are all larger than mid, so mid + 1 to not include mid till the  end of array
        # Return our fully built root of the tree once all recursion is finished
        return root
