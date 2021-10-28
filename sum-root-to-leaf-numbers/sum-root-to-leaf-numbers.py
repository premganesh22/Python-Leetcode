# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,path):
            if root:
                
                if not root.left and not root.right:
                    self.res+=path
                    return None
                if root.left:
                    dfs(root.left,path*10+root.left.val)
                if root.right:
                    dfs(root.right,path*10+root.right.val)
                
        dfs(root,root.val)
        return self.res