class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {}
        prefix_map[0] = 1
        prefix_sum = 0
        output = 0
        for num in nums:
            prefix_sum+=num
           
            if prefix_sum-k in prefix_map:
                output+= prefix_map[prefix_sum-k]
            
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum]+=1
            
            else:
                prefix_map[prefix_sum] = 1
        
        return output
            