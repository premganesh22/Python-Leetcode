class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #Edge Case
        if len(nums) == 1:
            if nums[0] == target:
                return True
            return False
        
        #Move the start if start and last element is same. it will be difficult to find the #zone.
        for start in range(len(nums)):
            if nums[start] != nums[-1]:
                break
        
    
        end = len(nums)-1
        
        #Find zone
        zone = 'green' if target > nums[-1] else 'brown'
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return True
            
            if zone == 'brown' and nums[mid] > nums[-1]:
                start = mid+1
            
            elif zone == 'green' and nums[mid] <= nums[-1]:
                end = mid-1
            
            elif nums[mid] < target:
                start = mid+1
            
            else:
                end = mid-1
        return False
            
           
        