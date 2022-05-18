class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            while nums[i] != i+1:
                d = nums[i] - 1
                if nums[i] != nums[d]:
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        output = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                output.append(nums[i])
        return output
        