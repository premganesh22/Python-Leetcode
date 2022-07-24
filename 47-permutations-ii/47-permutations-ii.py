class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(nums, slate):
            if len(nums) == 0:
                output.append(slate[:])
            
            d = set()
            for i in range(len(nums)):
                if nums[i] not in d:
                    d.add(nums[i])
                    slate.append(nums[i])
                    helper(nums[:i]+nums[i+1:], slate)
                    slate.pop()
                
        helper(nums,[])
        return output