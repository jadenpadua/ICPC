# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Codec:

    def serialize(self, root):
        return self.serializeHelper(root)
        

    def deserialize(self, data):
        serialized_arr = data.split(',')
        print(serialized_arr)
        q = queue.Queue()
        for i in range(len(serialized_arr)):
            q.put(serialized_arr[i])
            
        return self.deserializeHelper(q)
    
    def deserializeHelper(self,q):
        nodeValue = q.get()
        
        if nodeValue == 'X':
            return None
        
        newNode = TreeNode(nodeValue)
        newNode.left = self.deserializeHelper(q)
        newNode.right = self.deserializeHelper(q)
        
        return newNode
    
    def serializeHelper(self,node):
        if node is None:
            return 'X'
        return str(node.val) + ',' + self.serializeHelper(node.left) + ',' + self.serializeHelper(node.right)
        
        
            
        
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
