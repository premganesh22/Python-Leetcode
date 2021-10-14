# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
                head1 = head
                curnode = head
                #10,10,20,20,30,30
                while curnode and curnode.next:

                    if curnode.val == curnode.next.val:

                        curnode.next = curnode.next.next
                    else:
                        curnode = curnode.next
                return head1