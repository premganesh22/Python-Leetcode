class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        left = 0
        right = 1
        nums.sort()
        ans=0
        while left<len(nums) and right < len(nums):
            if nums[right]-nums[left] < k or left == right:
                right+=1
            elif abs(nums[left] - nums[right]) > k:
                left+=1
            else:
                left+=1
                right+=1
                ans+=1
                while left<len(nums) and nums[left] == nums[left-1]:
                    left+=1
        return ans
        
        