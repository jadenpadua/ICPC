# Given root node of singly linked list, and int value k, remove kth 
# node from the end of the list
# Idea: two pointer approach at different places in linked list
# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    # init both pointers, counte rto keep track of how many nodes traversed
    counter = 1
    first = head
    second = head
    # Keep moving counter until matches k, tells second how many jumps to make
    while counter <= k:
        second = second.next
        counter += 1
    # Once second pointer is k nodes ahead of first, two cases
    # Case where node to remove is your head node if scond pointer already points to none
    if second is None:
        # update so we can properly remove head
        head.value = head.next.value
        head.next = head.next.next
        return 
    # afte accounting for edge case, normal case this will happen
    # When we break out of loop, our second pointer points to final value in LL NOT the null value
    while second.next is not None:
        second = second.next
        first = first.next
    # now our first.next is pointing to node we want to remove, so update that value with next.next
    first.next = first.next.next
