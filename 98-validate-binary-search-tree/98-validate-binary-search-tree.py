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
        global_ans = [True]
        
        def dfs(node):
            
            if not node.left and not node.right:
                return [node.val, node.val]
                
            smallest, largest = node.val, node.val
            isbst = True
            if node.left:
                l_smallest, l_largest = dfs(node.left)
                smallest = min(smallest, l_smallest)
                largest = max(largest, l_largest)
                if l_largest >= node.val:
                    isbst = False
            
                            
            if node.right:
                r_smallest, r_largest = dfs(node.right)
                largest = max(r_largest, largest)
                smallest = min(r_smallest, smallest)
                if r_smallest <= node.val:
                    isbst = False

            if not isbst:
                global_ans[0] = False
                
            return [smallest, largest]
            
        
        dfs(root)
        return global_ans[0]
                
            
        