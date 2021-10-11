class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        max_len = 0
        for i,j in dic.items():
            max_len = max(max_len,len(j))
        
        min_distance = len(nums)
        for i,j in dic.items():
            if len(j) == max_len:
                min_distance = min(min_distance, j[-1]-j[0]+1)
        return min_distance
        