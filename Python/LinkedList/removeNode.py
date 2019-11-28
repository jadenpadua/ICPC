class Solution:
    def removeNode(self, head: ListNode,target) -> ListNode:
        q = head
        p = head.next
        nodeToRemove = target
        
        if q.val == nodeToRemove:
            head = p
            q = None
            return head
            
        while p.val != nodeToRemove:
            p = p.next
            q = q.next
            
        if p.next == None:
            q.next = None
            p = None
            return head
        
        else:
            q.next = p.next
            p = None
