class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        dic = {}
        count = 0
        for i in nums[::-1]:
            if i not in dic:
                dic[i] = 1
                count+=1
            if count == 3:
                return i
        return nums[-1]