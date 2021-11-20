class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        31432
        index = len(nums) -2
        while 0 <= index and nums[index] >= nums[index+1]:
            index-=1
        
        if index == -1:
            return nums.reverse()
            
        nums[index+1:] = sorted(nums[index+1:])
        
        
        data = index+1
        while data < len(nums):
            if nums[index] < nums[data]:
                nums[index], nums[data] = nums[data],nums[index]
                break
            data+=1
       
        
        
        