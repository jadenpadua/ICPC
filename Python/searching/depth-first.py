#Constructing our node class
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    # Method conducts depth first search on a tree / graph
    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        # Append name here to output array
        array.append(self.name)
        # Iterate through all child objects
        for child in self.children:
            # Now call depth first search on every one of those children
            child.depthFirstSearch(array)
