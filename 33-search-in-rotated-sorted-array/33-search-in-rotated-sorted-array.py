class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        
        zone = 'white' if nums[0] < nums[-1] else ('green' if target <= nums[-1] else 'brown')
        
        while start <= end:
            mid = start + (end-start)//2
            
            if target == nums[mid]:
                return mid
            
            #Being in Wrong zone
            if zone == 'green' and nums[-1] <= nums[mid]:
                start = mid+1
                
            elif zone == 'brown' and nums[-1] > nums[mid]:
                end = mid-1
                
            
            #Normal binary search
            
            elif nums[mid] < target:
                start+=1
            else:
                end-=1
                
        return -1
                