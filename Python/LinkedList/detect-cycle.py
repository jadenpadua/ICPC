# Given a list, check if that list has a cycle or not (goes on in an infinite loop)
def hasCycle(head):
    # return false if no list 
    if head is None:
        return False
    # now init two pointers that will traverse list @ diff speeds
    fast = head.next
    slow = head
    # while fast.next pointer is not at end of list and slow is not at end keep iterating
    while fast is not None and fast.next is not None and slow is not None:
        # inifinite loop when these nodes at diff speeds go in a circle and eventually meet
        if fast == slow:
            return True
        # iterate two nodes
        fast = fast.next.next
        # iterate one node
        slow = slow.next
    # False return if nodes reach the end
    return False

