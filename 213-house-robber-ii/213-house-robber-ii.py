class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robbery(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            output = [0]*len(nums)
            output[0] = nums[0]
            output[1] = max(nums[0], nums[1])
        
            for n in range(2, len(nums)):
                output[n] = max(output[n-1], output[n-2]+nums[n])

            return output[-1]
        
        case1 = robbery(nums[2:len(nums)-1]) + nums[0]
        case2 = robbery(nums[1:])
        
        return max(case1, case2)