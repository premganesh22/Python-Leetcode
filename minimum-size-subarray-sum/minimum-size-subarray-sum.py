class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        sums = 0
        count = len(nums)+5

        for end in range(len(nums)):
            sums+=nums[end]
            if sums >= target:
                while sums >= target:
                    count=min(count,end-start+1)
                    sums-=nums[start]
                    start+=1
        return 0 if count == len(nums)+5 else count