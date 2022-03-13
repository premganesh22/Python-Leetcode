# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global_box = [False]
        if not root:
            return False
        
        def dfs(root,targetSum):
            #Constraint
            if global_box[0] == True:
                return
            #Base Case
            if not root.left and not root.right:
                if targetSum == root.val:
                    global_box[0] = True
                return 
            #Recursive Logic
            if root.left:
                dfs(root.left,targetSum-root.val)
            if root.right:
                dfs(root.right,targetSum-root.val)
            return 
        
        dfs(root,targetSum)
        return global_box[0]