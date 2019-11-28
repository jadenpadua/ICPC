# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        
        middle = count // 2
        for i in range(middle):
            head = head.next
    
        return head
