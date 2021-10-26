# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        direction = 1
        while stack:
            temp = []
            for i in range(len(stack)):
                data = stack.pop(0)
                temp.append(data.val)
                if data.left:
                    stack.append(data.left)
                if data.right:
                    stack.append(data.right)
            if direction % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
            direction+=1
                
        return res