class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        for n in range(len(nums)):
            if nums[n] in dic:
                dic[nums[n]].append(n)
            else:
                dic[nums[n]] = [n]
        
        maxi = 0
        for key, values in dic.items():
            maxi = max(maxi,len(values))
        
        mini = len(nums)
        for key,values in dic.items():
            if len(values) == maxi:
                mini = min(mini,values[-1]-values[0]+1)
        return mini
        