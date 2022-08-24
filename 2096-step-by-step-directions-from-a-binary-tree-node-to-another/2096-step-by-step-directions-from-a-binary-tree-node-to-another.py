# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        
        '''
        Build directions for both start and destination from the root.
        Say we get "LLRRL" and "LRR".
        Remove common prefix path.
        We remove "L", and now start direction is "LRRL", and destination - "RR"
        Replace all steps in the start direction to "U" and add destination direction.
        The result is "UUUU" + "RR".
        
        '''
        global_val = [[], []]
        
        def helper(node, findValue, path, val):
      
            if node.val == findValue:
                if not global_val[val]:
                    global_val[val].extend(path)
                return
            
            if not node.left and not node.right:
                return
        
            if node.left:
                path.append('L')
                helper(node.left, findValue,path , val)
                path.pop()
             
            if node.right:
                path.append('R')
                helper(node.right, findValue,path , val)
                path.pop()
        
        helper(root, startValue, [], 0)
        helper(root, destValue, [], 1)
        
        
        while global_val[0] and global_val[1] and global_val[0][0] == global_val[1][0]:
            global_val[0].pop(0)
            global_val[1].pop(0)
            
        return 'U'*len(global_val[0])+''.join(global_val[1]) 
         