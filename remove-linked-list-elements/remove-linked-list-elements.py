# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        curnode = head
        while curnode and curnode.next:
            while curnode.next and curnode.next.val == val:
                curnode.next = curnode.next.next
            curnode = curnode.next
        return head
        