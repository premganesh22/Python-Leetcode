class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        hmap = {0:1}
        global_output = 0
        for num in range(len(nums)):
            prefix_sum+=nums[num]
            prefix_sum%=k
            if prefix_sum  in hmap:
                global_output+=hmap[prefix_sum]
            
            if prefix_sum in hmap:
                hmap[prefix_sum]+=1
            else:
                hmap[prefix_sum] = 1
        return global_output
        
        