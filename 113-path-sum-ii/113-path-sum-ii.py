# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return []
        
        def dfs(root,targetSum,slate):
            if not root.left and not root.right:
                if targetSum == root.val:
                    slate.append(root.val)
                    result.append(slate[:])
                    slate.pop()
                return
            
            #REcursive case
            slate.append(root.val)
            if root.left:
                
                dfs(root.left,targetSum-root.val,slate)
                #slate.pop()
            if root.right:
                #slate.append(root.val)
                dfs(root.right,targetSum-root.val,slate)
            slate.pop()
            return
        
        dfs(root,targetSum,[])
        return result
        