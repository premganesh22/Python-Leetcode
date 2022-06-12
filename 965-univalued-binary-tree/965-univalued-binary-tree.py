# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if not node.left and not node.right:
                #global_count[0]+=1
                return True
            left, right = None, None
            if node.left:
                left = dfs(node.left)
    
            if node.right:
                right = dfs(node.right)
                
            if left == False or right == False:
                return False
            
            condition = False
            if node.left:
                if node.val == node.left.val:
                    condition = True
                else:
                    return False
            if node.right:
                if node.val == node.right.val:
                    condition = True
                else:
                    return False
            return condition
        
        
        return dfs(root)