class Solution:
    def threeSumClosest(self, listb: List[int], target: int) -> int:
        listb.sort()
        small_difference = 1000000
        for i in range(len(listb)):
            left = i+1
            right = len(listb)-1
            while(left < right):
                value = listb[i] + listb[left] + listb[right]
                
                if  value == target:
                    return value 
                if abs(value-target) < abs(small_difference-target):
                    small_difference = value

                if value > target:
                    right-=1
                else:
                    left+=1
        return small_difference
        