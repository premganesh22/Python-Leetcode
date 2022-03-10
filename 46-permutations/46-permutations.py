class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums,idx,slate,result):
            
            if len(nums) == idx:
                result.append(slate[:])
                return
            else:
                for i in range(idx,len(nums)):
                    nums[idx],nums[i] = nums[i],nums[idx]
                    slate.append(nums[idx])
                    helper(nums,idx+1,slate,result)
                    nums[idx],nums[i] = nums[i],nums[idx]
                    slate.pop()
                return result
        return helper(nums,0,[],[])
        