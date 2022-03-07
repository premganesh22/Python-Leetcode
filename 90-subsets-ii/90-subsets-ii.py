class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def sub(nums,slate,result):
            if len(nums) == 0:
                result.append(slate.copy())
                return result
            else:
                cur_index = nums[0]
                count = 0
                for index in range(len(nums)):
                    if cur_index == nums[index]:
                        count+=1
                #Include
                for i in range(count):
                    slate.append(nums[i])
                    sub(nums[count:],slate,result)
                for i in range(count):
                    slate.pop()
                #Exclude
                sub(nums[count:],slate,result)
                return result
        nums.sort()
        return sub(nums,[],[])
        