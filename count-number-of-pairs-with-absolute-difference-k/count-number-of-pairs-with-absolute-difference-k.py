class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        count = 0
        for i in nums:
            temp1, temp2 = i+k, i-k
            if temp1 in dic:
                count+=dic[temp1]
            if temp2 in dic:
                count+=dic[temp2]
            dic[i]=dic.get(i,0)+1
        return count
        