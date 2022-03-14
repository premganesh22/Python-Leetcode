# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0
        def bottom_up_dfs(root):
            if not root.left and not root.right:
                return 0
            
            #Recursive
           
            local_max = 0
            lh,rh = 0,0
            if root.left:
                lh = bottom_up_dfs(root.left)
                local_max+=lh+1
            if root.right:
                rh = bottom_up_dfs(root.right)
                local_max+=rh+1
           
            self.global_max = max(local_max,self.global_max)
            return max(lh+1,rh+1)
        bottom_up_dfs(root)
        return self.global_max