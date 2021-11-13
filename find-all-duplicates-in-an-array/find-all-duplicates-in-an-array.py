class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] < 0:
                output.append(abs(nums[i]))
            else:
                nums[val]*=-1
        return output
                
            
            
        