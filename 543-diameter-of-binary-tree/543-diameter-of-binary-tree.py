# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        global_dia = [0]
        
        def dfs(node):
            
            if not node.left and not node.right:
                return 0
            
            lh, rh = 0,0
            if node.left:
                lh = 1+ dfs(node.left)
                
            if node.right:
                rh = 1+ dfs(node.right)
                
            global_dia[0] = max(global_dia[0], lh+rh)
            return max(lh,rh)
        
        dfs(root)
        return global_dia[0]