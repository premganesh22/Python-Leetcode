# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow_p = head
        fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                break
        else:
            return None
        pointer = head
    
        while pointer != fast_p:
        
            pointer = pointer.next
            fast_p = fast_p.next
        return pointer
        