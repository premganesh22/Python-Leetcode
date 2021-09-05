class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_element = min(nums)
        output = 0
        for i in nums:
            output+=i-min_element
        return output