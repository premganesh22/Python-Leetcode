class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i< len(nums):
            if nums[i] == i:
                i+=1
            elif nums[i] >= len(nums):
                i+=1
            else:
                temp = nums[i]
                nums[i],nums[temp] = nums[temp],nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i+1