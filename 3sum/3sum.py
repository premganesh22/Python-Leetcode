class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


# def two_sum(nums,i):
#     found = []
#     left=i+1
#     right=len(nums)-1
#     while left < right:
#         if nums[i] + nums[left] + nums[right] == 0:
#             found.append([nums[i], nums[left], nums[right]])
#             right-=1
#             left+=1
#             while left<right and nums[left] == nums[left-1]:
#                 left+=1
#         elif nums[i] + nums[left]+nums[right] > 0:
#             right-=1
#         else:
#             left+=1
#     return found
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         output = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 break
#             if nums[i] == 0 or nums[i-1] != nums[i]:
#                 found = two_sum(nums,i)
        
#                 if found:
#                     output.extend(found)
#         return output
        