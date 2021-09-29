class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_sum = 0
        convert = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                if convert < k:
                    convert+=1
                else:
                    max_sum = max(max_sum,end-start)
                    while nums[start] != 0:
                        start+=1
                    start+=1
        
        return max(max_sum,end-start+1)
        