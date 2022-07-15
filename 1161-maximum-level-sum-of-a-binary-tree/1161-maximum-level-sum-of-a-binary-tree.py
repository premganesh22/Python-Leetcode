# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        def bfs(root):
            q = deque([[root]])
            max_val = root.val-1
            max_level = 0
            step = 0
            while q:
                nodes = q.popleft()
                temp = []
                level_sum = 0
                step+=1
                for node in nodes:
                    level_sum+=node.val
                    if node.left:
                        temp.append(node.left)
                
                    if node.right:
                        temp.append(node.right)
                if temp:
                    q.append(temp)
                
                if max_val < level_sum:
                    max_val = level_sum
                    max_level = step   
                
            return max_level 
        return bfs(root)
 
                