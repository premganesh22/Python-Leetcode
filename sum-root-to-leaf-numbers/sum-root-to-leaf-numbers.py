# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,path):
            if root:
                if not root.left and not root.right:
                
                    path = path*10 + root.val
                    self.res+=path
                dfs(root.left,path*10+root.val)
                dfs(root.right,path*10+root.val)
            
        self.res = 0
        dfs(root,0)
        return self.res
        