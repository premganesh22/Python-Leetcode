# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length+=1
        
        k = k % length
        
        #Make it circular linked list
        lastElement.next = head
       
        
        
        for i in range(length-k):
            lastElement = lastElement.next
            
        answer = lastElement.next
        lastElement.next = None
        return answer