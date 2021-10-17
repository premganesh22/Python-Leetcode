# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val
            val+=carry
            if val>9:
                carry= 1
                val=val%10
            else:
                carry = 0
            res.next = ListNode(val)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            print(val,carry)
            val+=carry
            if val>9:
                carry= 1
                val=val%10
            else:
                carry = 0
            res.next = ListNode(val)
            res = res.next
            l1 = l1.next
        while l2:
            val = l2.val
            val+=carry%10
            if val>9:
                carry= 1
                val=val%10
            else:
                carry = 0
            res.next = ListNode(val)
            res= res.next
            l2 = l2.next
        if carry:
            res.next = ListNode(carry)
            carry = 0
            
            
        return head.next