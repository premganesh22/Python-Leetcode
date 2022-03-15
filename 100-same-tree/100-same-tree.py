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
            if not p and not q:
                return
            if not p or not q:
                global_result[0] = False
                return
            if p.val == q.val:
                dfs(p.left,q.left)
                dfs(p.right,q.right)
            else:
                global_result[0] = False
            return
        dfs(p,q)
        return global_result[0]