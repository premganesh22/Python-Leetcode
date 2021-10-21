# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root.left,root.right)]
        
        while stack:
            val = stack.pop()
            left,right = val[0],val[1]
            
            if not left and not right:
                continue

            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left,right.right))
                stack.append((left.right,right.left))
            else:
                return False
        return True