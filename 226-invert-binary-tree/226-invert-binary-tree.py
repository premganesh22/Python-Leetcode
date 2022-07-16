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
            
        def dfs(node):
            
            if not node.left and not node.right:
                return
            
            node.left, node.right = node.right, node.left
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
        dfs(root)
        return root
        