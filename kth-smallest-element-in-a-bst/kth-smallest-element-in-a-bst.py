# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        
        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            inorder.append(root.val)
            in_order(root.right)
        in_order(root)
        return inorder[k-1]