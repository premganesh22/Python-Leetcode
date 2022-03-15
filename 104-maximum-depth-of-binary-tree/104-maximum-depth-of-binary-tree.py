# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global_max = [0]
        if not root:
            return 0
        def dfs(root,count):
            if not root.left and not root.right:
                count+=1
                global_max[0] = max(global_max[0],count)
                return
            count+= 1
            if root.left:
                dfs(root.left,count)
                
            if root.right:
                dfs(root.right,count)
            return
        dfs(root,0)
        return global_max[0]
        