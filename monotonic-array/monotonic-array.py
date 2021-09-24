class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        bigger = False
        smaller = False
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                if smaller:
                    return False
                bigger = True
            elif nums[i-1] > nums[i]:
                if bigger:
                    return False
                smaller = True
        return True