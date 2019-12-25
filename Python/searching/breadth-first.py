# Function that conducts breadth first search on a tree, navigating it from left to right
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        # init a queue with the root node
        queue = [self]
        # While there are still elements in the queue
        while len(queue ) > 0:
            # pop queue index of 0
            current = queue.pop(0)
            # Append current to array
            array.append(current.name)
            # Now append its children unto the queue
            for child in current.children:
                # After the children have been logged into the array, append the children of that child
                queue.append(child)
            # return output BFS array
            return array
