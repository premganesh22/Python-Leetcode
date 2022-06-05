class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        dic = {}
        stack = [[nums[-1], len(nums)-1]]
        
        for i in reversed(range(len(nums)-1)):
            if nums[i] < stack[-1][0]:
                dic[nums[i]] = stack[-1][1]
            elif nums[i] == stack[-1][0]:
                pass
            else:
                stack.pop()
                stack.append([nums[i],i])
        
        for i in range(len(nums)):
            if nums[i] in dic:
                change = dic[nums[i]]
                nums[i], nums[change] = nums[change], nums[i]
                break
        return int(''.join(nums))
        
        