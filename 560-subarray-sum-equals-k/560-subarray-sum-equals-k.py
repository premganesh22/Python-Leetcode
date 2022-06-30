class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hmap = {0:1}
        global_output = 0
        for i in range(len(nums)):
            prefix+= nums[i]
            if prefix-k in hmap:
                global_output+= hmap[prefix-k]
            
            if prefix in hmap:
                hmap[prefix]+=1
            else:
                hmap[prefix] = 1
        return global_output