class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for num in range(1,len(nums)):
            if nums[num] < nums[num-1]:
                return num-1
        return num