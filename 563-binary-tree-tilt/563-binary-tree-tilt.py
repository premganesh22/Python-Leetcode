# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        global_val = [0]
        
        def dfs(node):
            
            if not node.left and not node.right:
                return node.val
            
            left, right = 0, 0
            
            if node.left:
                left = dfs(node.left)
            
            if node.right:
                right = dfs(node.right)
                
            global_val[0]+= abs(right-left)
            
            return node.val + left + right
        
        dfs(root)
        return global_val[0]
        