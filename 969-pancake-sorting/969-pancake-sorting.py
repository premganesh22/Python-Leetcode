class Solution:
    
    def pancakeSort(self, nums: List[int]) -> List[int]:
        
        def helper(arr):
            max_index = 0 
            max_val = 0
            for i in range(len(arr)):
                if arr[i] > max_val:
                    max_index = i
                    max_val = arr[i]
            return max_index
        output = []
        for i in range(len(nums)):
            max_index = helper(nums[0:len(nums)-i])
            if len(nums)-i-1 == max_index:
                continue
            nums[0:max_index+1] = nums[0:max_index+1][::-1]
            output.append(max_index+1)
            nums[0:len(nums)-i] = nums[0:len(nums)-i][::-1]
            output.append(len(nums)-i)
        return output