class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        hmap = {0:0}
        total = 0
        for num in range(len(nums)):
            if nums[num] == 0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            
            if prefix_sum in hmap:
                total = max(total, num+1 - hmap[prefix_sum])
                
            else:
                hmap[prefix_sum] = num+1 
        return total
            