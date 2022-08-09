# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def helper(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(val = head.val)
            
            fast = head
            slow = head
            prev = None
            
            while fast.next and fast.next.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
                
            root = TreeNode(val = slow.val)
            
            if prev:
                prev.next = None
                root.left = helper(head)
            
            root.right = helper(slow.next)
            
            return root
        
        return helper(head)
        