'''
1) Have max sum and temp sum
2) Iterate 


'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = float(-inf)
        for i in nums:
            cur_sum = max(cur_sum+i,i)
            max_sum = max(max_sum, cur_sum)
        
        return max(max_sum, cur_sum)