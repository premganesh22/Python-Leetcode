class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums)
        
        while start <= end:
            mid = start + (end-start)//2
            
            #left portion
            if nums[-1] < nums[mid]:
                start = mid+1
            
            #right portion
            else:
                end = mid-1
        
        return nums[start]