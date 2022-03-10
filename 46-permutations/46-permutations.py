class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums,slate,result):
            
            if len(nums) == 0:
                result.append(slate[:])
                return
            else:
                for i in range(len(nums)):
                    slate.append(nums[i])
                    helper(nums[:i]+nums[i+1:],slate,result)
                    slate.pop()
                return result
        return helper(nums,[],[])
        