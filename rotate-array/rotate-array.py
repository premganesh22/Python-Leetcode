class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [1,2,3,4,5,6,7,8,9,10] k = 3
        [8,9,10,4,5,6,7,1,2,3]
        [10,9,8,4,5,6,7,1,2,3]
        [10,9,8,7,6,5,4,3,2,1]
        [1,2,3,4,5,6,7]
        [7,6,5,4,3,2,1]
        [7,6,5,1,2,3,4]
        
        
        """
        #1) [start: len(nums)-k] and [k:len(nums)] -->  [k:len(nums)] + [start: len(nums)-k]
        
        def helper(start,end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        
        if len(nums) < k:
            k %= len(nums)
        helper(0,len(nums)-1)
        helper(k,len(nums)-1)
        helper(0,k-1)
            
        
        
        