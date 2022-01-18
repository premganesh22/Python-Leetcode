class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        length = len(nums)
        
        for i in range(len(nums)*2-1):
            while stack and nums[stack[-1]] < nums[i%length]:
                res[stack.pop()] = nums[i%length]
                
            stack.append(i%length)

        return res