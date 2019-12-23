class Node:
    # Construction of our Node 
    def __init__(self, value):
        self.value = Value
        self.prev = None
        self.next = None
# Construction of a DoublyLinkedList
class DoublyLinkedList:
    # Init head and tail pointers of list
    def __init__self(self):
        self.head = None
        self.tail = None 
    # Sets head of our list given a node
    def setHead(self, node):
        # If not head in the first place set head and tail to node
        if self.head is None:
            self.head = node
            self.tail = node
            return
        #Else call our method to insert a node before another node
        self.insertBefore(self.head, node)
    # Sets tail of our linkedlist given a node:
    def setTail(self, node):
        # Case where there is no tail, then we have to just set one node
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # method to insert a node before another node
    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # Case where we are inserting something already at head/tail so do nothing
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # Now proceed to remove the node we want to insert from the list
        self.remove(nodeToInsert)
        # Now set the pointers of node we want to insert to prev and next
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node # Notice how its insert before, so set next to the node
        # Now readjust pointets so nodeToInsert fits in LL
        # Case where we know our node to insert is our head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            # Else set the prev node next pointer to the node we want to insert
            node.prev.next = nodeToInsert
        
        #Finally remove value of prev node and replace it
        node.prev = nodeToInsert
    # MEthod to insert a node after another node
    def insertAfter(self, node, nodeToInsert):
        # if only one node then do nothing
        if node nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # Now update prev and next of node to insert
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        # Case where next node is tail
        if node.next is None:
            self.tail = nodeToInsert
        else:
            # Else adjust node bindings in next node
            node.next.prev = nodeToInsert
        # Finally remove next node and replace it
        node.next = nodeToInsert
    # method to remove a given node
    def remove(self, node):
        # Case where our node is the head node
        if node == self.head:
            self.head = self.head.next
        # Case where our node is the tail node
        if node == self.tail:
            self.tail = self.tai.prev
        # Else our node is nested within the middle, so remove Node Bindings
        self.removeNodeBindings(node)

    # Method to remove node bindings of a given node
    def removeNodeBindings(self, node):
        # Sets prev.next to the next node and removes binding from current node
        if node.prev is not None:
            node.prev.next = node.next
        # Sets next.prrev node to prev node and removes binding from current node
        if node.next is not None:
            node.next.prev = node.prev
        #Now we can free the original pointers of our node
        node.prev = None
        node.next = None

    # Method to insert a node at a position
    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        # let one reflect a position at the head
        if position == 1:
            self.setHead(nodeToInsert) # now just invoke set head and insert their
            return
        # if not then iterate through list until we find it
        node = self.head
        currentPosition = 1
        # Either we hit None value or we find pos we want to insert
        while node is not None and currentPosition != position:
            # keep iterating through and updating current position
            node = node.next
            currentPosition += 1
        # Case where we found matching position
        if node is not None:
            # Insert node
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert) # Else insert node at tail
    # O(n) time | O(1) space
    # method to remove a node from LL given a value
    def removeNodesWithValue(self,value):
        # iterate through LL
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            # proceed to remove node if value matches
            if node.nodeToRemove == value:
                self.remove(nodeToRemove)
    # Method to check if LL contains node with value
    def containsNodeWithValue(self, value):
        node = self.setHead
        # iterate until end or value matches
        while node is not None and node.value != value:
            node = node.next
        # CHeck whether node is none or not will determine if it has the value in LL
        return node is not None
