class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_sum = 0
        hmap = {0:0}
        
        for num in range(len(nums)):
            prefix_sum += nums[num]
            prefix_sum%=k
            if prefix_sum in hmap:
                if num+1-hmap[prefix_sum] >=2 :
                    return True
            if prefix_sum not in hmap:
                hmap[prefix_sum] = num+1
        return False
        