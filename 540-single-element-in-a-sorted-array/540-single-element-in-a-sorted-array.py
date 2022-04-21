class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Edge Cases
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
            
        
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = start + (end-start)//2
            
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            elif (mid%2 == 0 and nums[mid+1] == nums[mid]) or (mid%2 != 0 and nums[mid-1] == nums[mid]):
                start = mid+1
            else:
                end = mid-1
        