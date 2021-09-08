class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        
        for i in t:
            if i in dic:
                dic[i]-=1
            else:
                return i
        
        for key,value in dic.items():
            if value != 0:
                return key
        