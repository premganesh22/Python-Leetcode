# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,data,res):
        if data:
            if data.left:
                self.helper(data.left,res)
            res.append(data.val)
            if data.right:
                self.helper(data.right,res)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res)
        return res