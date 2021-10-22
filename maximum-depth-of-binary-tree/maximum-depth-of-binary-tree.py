# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            length = len(queue)
            level+=1
            for i in range(length):
                val = queue.popleft()
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
        return level