class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 1
        for i in nums[1:]:
            if candidate == i:
                count+=1
            elif count == 0:
                candidate = i
                count+=1
            else:
                count-=1
        return candidate
