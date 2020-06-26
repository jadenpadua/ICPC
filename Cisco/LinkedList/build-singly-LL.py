class Node(object):
    def __init__(self,val,next=None)
        self.val = val
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_val(self):
        return self.val
    
    def set_next(self,next):
        self.next = next
    
    def set_val(self,val):
        self.val = val
    
class LinkedList(object):
    def __init__(self, root = None)
        self.root = root
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self,val):
        new_node = Node(val,self.root)
        self.root = new_node
        self.size += 1
    
    def remove(self,val):
        q = head
        p = head.next
        nodeToRemove = val
        
        if q.val == nodeToRemove:
            return head.next
        
        while p.val != nodeToRemove:
            p = q.next
            q = q.next
        
        if p.next == None:
            q.next = None
            p = None
            return head
        
        else:
            q.next = p.next
            p.next = None
    
    def find(self, val):
        cur = self.root
        while cur is not None:
            if cur.get_data() == val:
                return val
            elif cur.get_data() == None:
                return False
            else:
                cur = cur.get_next()
        
