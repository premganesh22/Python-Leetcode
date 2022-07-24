class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def helper(nums, slate):
            if len(nums) == 0:
                output.append(slate[:])
                return

            #Include
            slate.append(nums[0])
            helper(nums[1:], slate)
            slate.pop()

            #Exclude
            helper(nums[1:], slate)
                
                
        
        helper(nums, [])
        return output