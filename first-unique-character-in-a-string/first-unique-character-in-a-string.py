class Solution(object):
    def firstUniqChar(self, a):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in a:
            dic[i] = dic.get(i,0)+1
        for i in range(len(a)):
            if dic[a[i]] == 1:
                return i
        return -1
