class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def divide_posible(mid):
            cur_val = 0
            count = 1
            for w in weights:
                cur_val+=w
                if cur_val > mid:
                    cur_val = w
                    count+=1
            return count <= days 
        
        
        left, right = max(weights), sum(weights)
        
        
        
        while left < right:
            mid = left + (right-left)//2
            
            if divide_posible(mid):
                right = mid
                
            else:
                left = mid+1
            
        return right