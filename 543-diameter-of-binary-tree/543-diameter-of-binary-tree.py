# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(node):
            if not node.left and not node.right:
                return 0
            
            hl = 0
            hr = 0
            dia = 0
            
            if node.left:
                hl = 1+dfs(node.left)
                
            if node.right:
                hr = 1+dfs(node.right)
            
            dia = hl+ hr
            diameter[0] = max(diameter[0],dia)
            
            return max(hl,hr)
        dfs(root)
        
        return diameter[0]
        