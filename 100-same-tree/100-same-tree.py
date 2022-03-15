# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global_result = [True]
        if not p and not q:
            return True
        if not p or not q:
            return False
        def dfs(p,q):
            if not p.left and not p.right and not q.left and not q.right:
                if p.val != q.val:
                    global_result[0] = False
                return

            if (not p.left and not p.right) or (not q.left and not q.right):
                global_result[0] = False
                return

            if p.left and q.left:
                if not p.left.val == q.left.val:
                    global_result[0] = False
                    
                dfs(p.left,q.left)

            elif p.left or q.left:
                global_result[0] = False

            if p.right and q.right:
                if not p.right.val == q.right.val:
                    global_result[0] = False
                dfs(p.right,q.right)
            elif p.right or q.right:
                global_result[0] = False
            return       
        dfs(p,q)
        return global_result[0]