class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Edge Case
        if len(nums) == 1:
            return nums[0]
        
        #Move the start to the index where it didn't match with end
        for start in range(len(nums)):
            if nums[start] != nums[-1]:
                break
        
        end = len(nums)-1
        
        if start == end:
            return nums[start]
        
        while start <= end:
            mid= start + (end-start)//2
            if nums[mid] > nums[-1]:
                start = mid+1
                
            else:
                end = mid-1
        if start < len(nums):
            return nums[start]
        else:
            return nums[end]