class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_swap = -1

        for i in range(len(nums)):
            if nums[i] != 0 and zero_swap > -1:
                nums[i],nums[zero_swap] = nums[zero_swap],nums[i]
                zero_swap+= 1
            elif nums[i] == 0 and zero_swap == -1:
                zero_swap = i
        