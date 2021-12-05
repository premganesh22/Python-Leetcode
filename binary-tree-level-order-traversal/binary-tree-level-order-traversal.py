# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        
        res = []
        if not root:
            return res
        stack = [root]
        
        while stack:
            output = []
            temp = []
            length = len(stack)
            for i in range(length):
                data = stack.pop(0)
                output.append(data.val)
                if data.left:
                    temp.append(data.left)
                if data.right:
                    temp.append(data.right)
            stack.extend(temp)
            res.append(output)
        return res
        