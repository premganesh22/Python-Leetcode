# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        count = [0]
        def inorder(root):
            if count[0] >= k:
                return 
            if root.left:
                inorder(root.left)
            if count[0] < k:
                output.append(root.val)
                count[0]+=1
                if root.right:
                    inorder(root.right)
            return 
        inorder(root)
        print(output)
        return output[-1]