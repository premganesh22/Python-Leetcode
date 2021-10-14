# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        test = ListNode()
        curnode = test
        first = l1
        second = l2
        while True:
            if not first:
                curnode.next = second
                break
            elif not second:
                curnode.next = first
                break
            elif first.val < second.val:
                curnode.next = first
                first = first.next
                curnode = curnode.next
            else:
                curnode.next = second
                second = second.next
                curnode = curnode.next
        return test.next