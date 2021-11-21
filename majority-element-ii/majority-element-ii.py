class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        candidate1 = candidate2 = "test"
        for i in nums:
            if i == candidate1:
                count1+=1
            elif i == candidate2:
                count2+=1
            
            elif count1 == 0:
                count1+=1
                candidate1 = i
            elif count2 == 0:
                count2+=1
                candidate2 = i
                
            else:
                count1-=1
                count2-=1
        output = []
        print(candidate1,candidate2)
        for i in [candidate1,candidate2]:
            if nums.count(i) > len(nums)//3:
                output.append(i)
        return output