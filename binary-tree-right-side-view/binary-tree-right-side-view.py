# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        res = []
        stack = [root]
        while stack:
            temp = []
            for i in range(len(stack)):
                node = stack.pop(0)
                if i == 0:
                    res.append(node.val)

                if node.right:
                    temp.append(node.right)

                if node.left:
                    temp.append(node.left)
            stack = temp
        return res