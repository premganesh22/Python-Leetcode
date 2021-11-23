class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = sum(nums)+1
        start = 0
        sums = 0
        for end in range(len(nums)):
            sums+=nums[end]
            while sums >= target:
                
                output = min(output,end-start+1)
                sums-=nums[start]
                start+=1
        
        return output if not output == sum(nums)+1 else 0
            
    