# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        global_node = [None]
        def dfs(node):
            
            p_f, q_f = False, False
            if node == p:
                p_f = True
            if node == q:
                q_f = True
            
            if node.left:
                lp, lq = dfs(node.left)
                p_f = p_f or lp
                q_f = q_f or lq
            if node.right:
                rp, rq = dfs(node.right)
                p_f = p_f or rp
                q_f = q_f or rq
            
            
            if p_f and q_f and not global_node[0]:
                global_node[0] = node
            
            return [p_f, q_f]
        
        dfs(root)
        return global_node[0]
            