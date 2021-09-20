class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        x, m = 0, 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if i+1 in d:
                x = d[i] + d[i+1]
                if m < x:
                    m = x
            else:
                pass
        return m