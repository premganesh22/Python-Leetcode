# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        global_var = [True]
        def dfs(root):
            smallest,largest,isBST = root.val,root.val,True 
            if not root.left and not root.right:
                return (smallest,largest) 
            if root.left:
                s,l = dfs(root.left)
                smallest = min(smallest,s)
                largest = max(largest,l)
                if l >= root.val:
                    isBST = False

            if root.right:
                s,l = dfs(root.right)
                smallest = min(smallest,s)
                largest = max(largest,l)
                if s <= root.val:
                    isBST = False
            if not isBST:
                global_var[0] = False
            return (smallest,largest)
        dfs(root)
        return global_var[0]
