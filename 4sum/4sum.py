class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        print(nums)
        i=0
        while i < len(nums)-3:
            j=i+1
            while j < len(nums)-2:
                left = j+1
                right = len(nums)-1
                while left<right:
                    val = nums[i] + nums[j]+ nums[left] + nums[right]
                    if val > target:
                        right-=1
                    elif val < target:
                        left+=1
                    else:
                        output.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                j+=1
                while j < len(nums)-2 and nums[j] == nums[j-1]:
                    j+=1
            i+=1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i+=1

        return output