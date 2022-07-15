# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root):
            q = deque()
            q.append(root)
            condition = False
            while q:
                numnodes = len(q)
                
                for _ in range(numnodes):
                    node = q.popleft()
                    if node.left:
                        if condition:
                            return False
                        q.append(node.left)
                    else:
                        condition = True
                    
                    if node.right:
                        if condition:
                            return False
                        q.append(node.right)
                    else:
                        condition = True
            
            return True
        return bfs(root)            
                
        