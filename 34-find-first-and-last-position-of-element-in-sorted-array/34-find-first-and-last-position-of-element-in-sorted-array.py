class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid= start + (end-start)//2
            
            if nums[mid] < target:
                start = mid+1
            
            else:
                end = mid-1
        
        #Elemeent not found
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        
        leftmost = start
        end = len(nums)-1
        
        while start <= end:
            mid= start + (end-start)//2
            
            if nums[mid] <= target:
                start = mid+1
            
            else:
                end = mid-1
        return [leftmost,end]