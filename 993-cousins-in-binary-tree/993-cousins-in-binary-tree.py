# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = deque()
        queue.append(root)
        px = None
        py = None
        while queue:
            nums = len(queue)
            for i in range(nums):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if node.left.val == x:
                        px = node
                    if node.left.val == y:
                        py = node
                if node.right:
                    queue.append(node.right)
                    if node.right.val == x:
                        px = node
                    if node.right.val == y:
                        py = node
                if px and py and px!= py:
                    return True
            px, py = None, None
        return False
                    