# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        dummy.next = head
        
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = dummy.next.next
            dummy.next = b
            a.next = b.next
            b.next = a
            dummy = dummy.next.next
        return temp.next