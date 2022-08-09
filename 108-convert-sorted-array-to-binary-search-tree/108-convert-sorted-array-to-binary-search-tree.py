# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(nums, start, end):
            if start > end:
                return None
            
            if start == end:
                return TreeNode(val = nums[start])
            
            mid = start + (end-start)//2
            
            root = TreeNode(val = nums[mid])
            root.left = dfs(nums, start, mid-1)
            root.right = dfs(nums, mid+1, end)
            
            return root
        
        return dfs(nums, 0, len(nums)-1)