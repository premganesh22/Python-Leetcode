


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        target = 0
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if nums[i] > 0:
                return output

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val > target:
                    right-=1
                elif val < target:
                    left+=1
                else:
                    output.append([nums[i], nums[left], nums[right]])
        
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        print(left)
                        left+=1
        return output
