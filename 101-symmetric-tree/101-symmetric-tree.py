# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        while queue:
            start = 0
            end = len(queue)-1
           
            while start < end:
                if queue[start] and queue[end]:
                    if not queue[start].val == queue[end].val:
                        return False
                elif queue[start] or queue[end]:
                    return False
                start+=1
                end-=1
            
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        return True