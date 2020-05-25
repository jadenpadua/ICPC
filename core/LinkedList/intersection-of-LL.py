# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ht = dict()
        while headA:
            ht[headA] = True
            headA = headA.next
        while headB:
            if headB in ht:
                return headB
            headB = headB.next
        return None
        
        
