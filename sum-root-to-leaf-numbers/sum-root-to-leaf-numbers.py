# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        self.output=0
        val = 0
        def helper(root,val):
            if not root:
                return None
            if not root.left and not root.right:
                self.output += (val*10+root.val)
                return None
            helper(root.left,(val*10)+root.val)
            helper(root.right,(val*10)+root.val)
            
        helper(root,0)
        return self.output