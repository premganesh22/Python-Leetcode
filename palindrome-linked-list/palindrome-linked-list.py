# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, node):
        prev = None
        while node:
            cur = node
            node = node.next
            cur.next = prev
            prev = cur
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow_p = head
        fast_p = head
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        
        copy = slow_p
        reversed_c = self.reverse(slow_p)
        pointer = head
        
        while reversed_c:
            print(reversed_c.val,pointer.val)
            if reversed_c.val != pointer.val:
                return False
            reversed_c = reversed_c.next
            pointer = pointer.next
        return True