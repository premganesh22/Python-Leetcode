# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        
        self.output = 0
        if not root:
            return None
        def helper(root,status):
            if not root.left and not root.right:
                if status:
                    self.output+=root.val    
                else:
                    return 0
            if root.left:
                helper(root.left,True)
            if root.right:
                helper(root.right,False)
        
        helper(root,False)
        return self.output
        