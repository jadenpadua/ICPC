class Node:
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ht = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.ht:
            n = self.ht[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.ht:
            self._remove((self.ht[key]))
        
        n = Node(key, value)
        self._add(n)
        self.ht[key] = n
        
        if len(self.ht) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.ht[n.key]
    
    
    
    
    def _remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
            
    
    def _add(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
