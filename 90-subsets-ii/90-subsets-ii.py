class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,slate,result):
            if len(nums) == 0:
                result.append(slate[:])
                return
            else:
                count = 0
                cur_num = nums[0]
                for i in range(len(nums)):
                    if cur_num == nums[i]:
                        count+=1
                
                #Exclude
                helper(nums[count:],slate,result)
                for i in range(count):
                    #Include
                    slate.append(nums[i])
                    helper(nums[count:],slate,result)
                
                for i in range(count):
                    slate.pop()
                
                return result
        return helper(sorted(nums),[],[])
        