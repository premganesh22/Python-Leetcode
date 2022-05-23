class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        output = []
        for num in nums:
            prefix_sum+=num
            output.append(prefix_sum)
            
        return output