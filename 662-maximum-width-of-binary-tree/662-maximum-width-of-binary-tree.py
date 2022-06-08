# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 1])
        
        max_width = 0
        while queue:
            first, last = None, None
            length = len(queue)
            for i in range(length):
                node, val = queue.popleft()
                if node.left:
                    queue.append([node.left, val*2])
                if node.right:
                    queue.append([node.right, (val*2)+1])
                if first is None:
                    first = val
            last = val
            max_width = max(max_width, last-first+1)
        
        return max_width
            
            
        