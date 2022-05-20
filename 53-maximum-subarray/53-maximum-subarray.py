class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax = nums[0]
        globalmax = nums[0]
        
        for i in range(1,len(nums)):
            curmax = max(curmax+nums[i], nums[i]) #1; -2; 4; 3; 5; 6; 1
            globalmax = max(curmax, globalmax) #1; 1; 4; 4; 5; 6; 6
            
        return globalmax
        