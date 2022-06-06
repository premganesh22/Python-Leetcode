class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zeros = 0
        max_one = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros+=1
                if zeros > k:
                    max_one = max(max_one, end-start)
                    while not zeros == k:
                        if nums[start] == 0:
                            zeros-=1
                        start+=1
            
        return max(max_one, end-start+1)