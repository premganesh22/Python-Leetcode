# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        lista  = [0]
        if not root:
            return 0
        
        def helper(node,flag):
            if not node.right and not node.left:
                if flag:
                    lista[0]+=node.val
                else:
                    return 0
            if node.left:
                helper(node.left,True)
            if node.right:
                helper(node.right,False)
            
        helper(root,False)
        return lista[0]
        