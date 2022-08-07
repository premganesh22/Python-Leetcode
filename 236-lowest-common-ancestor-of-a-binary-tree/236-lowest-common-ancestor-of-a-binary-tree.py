# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        global_output = [-1]
        def dfs(node):
            p_found = False
            q_found = False
            if node == p:
                p_found = True
            elif node == q:
                q_found = True
                
            if not node.left and not node.right:
                return [p_found, q_found]
            
            if node.left:
                left_val, right_val = dfs(node.left)
                p_found = p_found or left_val
                q_found = q_found or right_val
            if node.right:
                left_val, right_val = dfs(node.right)
                p_found = p_found or left_val
                q_found = q_found or right_val
                
            if p_found and q_found and global_output[0] == -1:
                global_output[0] = node
            
            return [p_found, q_found]
        dfs(root)
        return global_output[0]
            