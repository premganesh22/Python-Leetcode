class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        output = [0]*len(nums)
        
        output[0] = nums[0]
        output[1] = max(nums[0], nums[1])
        
        for n in range(2, len(nums)):
            output[n] = max(output[n-1], output[n-2]+nums[n])
            
        return output[-1]