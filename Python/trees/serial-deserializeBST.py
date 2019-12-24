class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
# Solution on how to serialize and deserialize a BST
class Solution:
    def serialize(self, root):
    # Calls helper method to get Serialization of tree
    serialize = self.serializeHelper(root)
    print("Serialized: " + serialized + "\n")
    # Now will deserialize tree after we print serialized tree
    self.deserialize(serialized)
    # Here we will use pre order traversal to help us with serialization
    def serializeHelper(self, node):
        # Case where we do not have node, just return X
        if node is None:
            return 'X,'
        # pre order traversal algorithm
        return str(node.val) + ',' + self.serializeHelper(node.left) + self.serializeHelper(node.right)
    # now turn back into a tree given a string with data
    def deserialize(self, data):
        serialized_split = data.split(',') # Now split data by comma delimeter
        q = queue.Queue() #Create queue object to place our string into q
        # Now all elements in string are placed within queue
        for i in range(len(serialized_split)):
            q = queue.Queue()
        # Pass in queue now here so we can build back up
        return self.deserializeHelper(q)
    
    def deserializeHelper(self,q):
        # Gets value of current node in queue
        valueForNode = q.get()
        # Do not build anything if we see an x on the string
        if valueForNode == 'X':
            return None
        # Now construct a tree node with that nodes value from quuee
        newNode = TreeNode(valueForNode)
        # Set the left children of this node
        newNode.left = self.deserializeHelper(q)
        # Set the right children of this node
        newNode.right = self.deserializeHelper(q)
        # Recurses back up and returns output tree when finished
        return newNode
