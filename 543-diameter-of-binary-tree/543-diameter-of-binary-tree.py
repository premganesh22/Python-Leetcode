# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global_val = [0]
        def dfs(root):
            if not root.left and not root.right:
                return 0
            local = 0
            lh,rh = 0,0
            if root.left:
                lh = dfs(root.left)
                lh+=1
                local+=lh
            if root.right:
                rh = dfs(root.right)
                rh+=1
                local+=rh
            global_val[0] = max(global_val[0],local)
            return max(lh,rh)
        dfs(root)
        return global_val[0]
