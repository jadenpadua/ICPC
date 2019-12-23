class Node(object):
    # Sets our node constructor, sets data and next in the node init
    def __init__(self,d, n=None):
        self.data = d
        self.next = n
    #Returns next node in the Linked List
    def get_next(self):
        return self.next
    # Sets our next node equal to n
    def set_next(self,n):
        self.next = n
    #Returns data in our node
    def get_data(self):
        return self.data
    # Sets data in our node object
    def set_data(self,d):
        self.data = d

class LinkedList(object):
    # Constructs a new LL with a root or head node equal to None
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    #Adds a node from linked list
    def add(self,d):
        # Creates a new node object
        new_node = Node(d,self.root)
        # Sets the root to the new node
        self.root = new_node
        self.size += 1
    # Remove a node from a linked list
    def remove(self,d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                    self.size -= 1
                    return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data == d:
                return d
            elif this_node.get_data == None:
                return False
            else:
                this.node = this_node.get_next()
