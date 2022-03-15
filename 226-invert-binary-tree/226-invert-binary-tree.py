# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def dfs(root):
            if not root.left and not root.right:
                return root
            
            root.left,root.right = root.right,root.left
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
            
            return root
        return dfs(root)
        