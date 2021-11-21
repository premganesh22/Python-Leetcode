class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = global_max = nums[0]
        for num in nums[1:]:
            temp = cur_max
            cur_max = max(cur_max*num,cur_min*num,num)
            cur_min = min(temp*num,cur_min*num,num)
            global_max = max(global_max,cur_max)
        return max(global_max,cur_max)
            
            
            
        