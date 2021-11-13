'''
# iterante and Copy each number to Dictionary --> o(n) o(n)
# iterate from 1 to length of the array --> o(n)
# Find the missing # in dictionary and store it in array. 0(n-1)
# return the array


Sorting

# Sort the array
# iterate from 1 to length of the array --> o(n)
# Find the missing # in the index  and store it in array. 0(n-1)
# return the array

# Iterate all the elements
# swap the element with the index of the element. 
if element == nums[element+1]


'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        index = 0
        while index < len(nums):
            find_val = nums[index]-1
            if not nums[index] == nums[find_val]:
                nums[index],nums[find_val] = nums[find_val],nums[index]
            else:
                index+=1
        print(nums)
        for i in range(0,len(nums)):
            if nums[i] != i+1:
                output.append(i+1)
                
        return output
            
        