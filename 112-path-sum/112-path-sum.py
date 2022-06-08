# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return None
        result = [False]
        
        def helper(node, targetSum):
            if not node.left and not node.right:
                if targetSum == 0:
                    result[0] = True
            
            if node.left:
                helper(node.left, targetSum-node.left.val)
            
            if node.right:
                helper(node.right, targetSum-node.right.val)
        
        helper(root, targetSum-root.val)
            
        return result[0]