class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        for k in range(1,len(arr)+1,2):
            start = 0
            end = 0
            temp_sum = 0
            for i in range(len(arr)):
                if end-start == k:
                    total+=temp_sum
                    temp_sum-=arr[start]
                    start+=1
                temp_sum+=arr[end]
                end+=1
            total+=temp_sum
        return total