# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return None
        result = []
        
        def helper(node,slate):
            if not node.left and not node.right:
                result.append("->".join(slate))
            
            if node.left:
                slate.append(str(node.left.val))
                helper(node.left, slate)
            
            if node.right:
                slate.append(str(node.right.val))
                helper(node.right, slate)
            
            slate.pop()
        
        helper(root, [str(root.val)])
        return result
        
        