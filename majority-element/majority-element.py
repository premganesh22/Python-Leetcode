class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        max_num = 0
        
        for num in nums:
            if count == 0:
                max_num = num
                count+=1
            else:
                if count > 0:
                    if max_num == num:
                        count+=1
                    else:
                        count-=1
        return max_num
        