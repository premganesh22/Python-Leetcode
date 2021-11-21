class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for index in range(len(nums)-1):
            left.append(left[-1]*nums[index])
            
        for index in range(len(nums)-1,0,-1):
            right.append(right[-1]*nums[index])
        right = right[::-1]
        
        return [i*j for i,j in zip(left,right)]