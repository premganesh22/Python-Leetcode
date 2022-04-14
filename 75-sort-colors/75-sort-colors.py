class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        num = 0
        while num < len(nums):
            if nums[num] == 1:
                nums[num],nums[one] = nums[one],nums[num]
                one+=1
            elif nums[num] == 0:
                nums[num],nums[one] = nums[one],nums[num]
                nums[one],nums[zero] = nums[zero],nums[one]
                zero+=1
                one+=1
            num+=1
        
            