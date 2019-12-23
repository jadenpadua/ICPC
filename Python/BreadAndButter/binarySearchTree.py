# Implementation of a Binary Search Tree
class BST:
    # Constructor giving tree properties to object
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    # inserting a node into a BST
    def insert(self,value):
        # Need to keep track of where we are at
        currentNode = self
        while True:
            # if value is less we know we want to explore left
            if value < currentNode.val:
                # case where we hit the end of the tree, insert there
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
            # if there are still nodes to explore on left subtree keep iterating
                else:
                    currentNode = currentNode.left
            # Same logic but for right
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            return self
    # Checking if value is in tree
    # Average O(log(n)) time | O(1) space
    def contains(self, value):
        currentNode = self
        # iterate through tree
        while currentNode is not None:
            # now cuts tree in half based on comparision
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            # Case where we found the value when equal, return true
            else:
                return True
        return False

    # Removing a node from a binary search tree
    # Think of removal as a two step process, first find node you want to remove
    # Then go ahead and remove it
    def remove(self, value, parentNode = None):

        currentNode = self
        # finding our node to remove
        # We need to keep track of parent Node here because when we 
        # are removing a node, we need to reassign the child node of the parent
        # of the node we are removing
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode # parentNode becomes node we were just exploring
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            # Now hard part, case where we have found our node  
            else:
            # Within this case there are subcases
            # First subcase: removing a node with two children nodes

            # Dealing with first subcase:
            # if both children nodes do not have None values and are there
                if currentNode.left is not None and currentNode.right is not None:
                    # sets currentNode.value to smallest value of a given BST
                    # We are looking for the smallest leftmost value of the right subtree
                    # The smallesy value of that nodes right subtree is the only value that can fit 100% of time
                    currentNode.value = currentNode.right.getMinValue()
                    # Now we delete this smallest value from right subtree and recurse
                    currentNode.right.remove(currentNode.value, currentNode)

                # Now case where we do not have 2 child nodes present
                # We have two subcases for this case

                # One of these cases is if we are dealing with the root node
                elif parentNode is None:
                    # HEre w know our current node only has one child
                    if currentNode.left is not None:
                        # Manually replacing values with the left nodes values
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        # Assign left last here to prevent overwrite
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        # Assign right last here to prevent overwrite
                        currentNode.right = currentNode.right.right
                    # Edge case of parent only has one node with node
                    else:
                        currentNode.value = None

                # one of these two cases is if we are not dealing with the root node
                elif parentNode.left == currentNode:
                    # now check if it is a left child or a right child
                    # Reassigns it to left or right child
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                # make sure we make a break statement here when found
                break
            

            return self
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value




               
