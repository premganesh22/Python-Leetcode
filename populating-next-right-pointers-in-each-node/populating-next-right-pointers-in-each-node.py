"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                stack.append(node.left)
                stack.append(node.right)
                
        return root