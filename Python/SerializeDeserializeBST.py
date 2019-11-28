# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue 
class Codec:

    def serialize(self, root):
        serialized = self.serializeHelper(root)
        print("Serialized: " + serialized + "\n")
        self.deserialize(serialized)
    
    
    def serializeHelper(self,node):
        if node is None:
            return 'X,' 
        
        return str(node.val) + ',' + self.serializeHelper(node.left) + self.serializeHelper(node.right)
    
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        serialized_split = data.split(',')
        q = queue.Queue()
        
        for i in range(len(serialized_split)):
            q.put(serialized_split[i])
        
        return self.deserializeHelper(q)
    
    def deserializeHelper(self,q):
        valueForNode = q.get()
        if valueForNode == 'X':
            return None
        newNode = TreeNode(valueForNode)
        newNode.left = self.deserializeHelper(q)
        newNode.right = self.deserializeHelper(q)
        
        print(newNode)
        return newNode
            
