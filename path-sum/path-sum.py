# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root,targetSum):
            if not root:
                return False
            if not root.left and not root.right:
                return root.val == targetSum

            return helper(root.left,targetSum-root.val) or helper(root.right,targetSum-root.val)
        
        return helper(root,targetSum)
        
        