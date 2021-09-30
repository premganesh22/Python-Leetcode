class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        start = 0
        output = []
        for end in range(len(nums)):
            if end-start == k-1:
                temp = nums[start:end+1]
                temp.sort()
                if len(temp)%2 == 0:
                    median = (temp[len(temp)//2] + temp[(len(temp)//2)-1])/2
                else:
                    median = temp[len(temp)//2]
                output.append(median)
                start+=1
        return output
        