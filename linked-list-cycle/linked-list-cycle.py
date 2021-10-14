# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        if not head or not head.next:
            return False
        fast_p = head.next
        while slow_p and fast_p:
            if slow_p == fast_p:
                return True
            slow_p = slow_p.next
            fast_p = fast_p.next
            if fast_p and fast_p.next:
                fast_p = fast_p.next
            else:
                return False
            
        return False
        