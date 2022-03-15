# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return False
        global_list = [False]
        def dfs(root,subRoot):
            if sametree(root,subRoot):
                global_list[0] = True
                return
            if root.left:
                dfs(root.left,subRoot)
            if root.right:
                dfs(root.right,subRoot)
            return
        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val == q.val:
                if not sametree(p.left,q.left):
                    return False
                if not sametree(p.right,q.right):
                    return False
            else:
                return False
            return True
        dfs(root,subRoot)
        return global_list[0]