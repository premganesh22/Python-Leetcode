class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prev = self.countAndSay(n-1)
        count = 1
        i = 0
        res = ''
        while i < len(prev)-1:
            if prev[i] == prev[i+1]:
                count+=1
            else:
                res+=str(count)+str(prev[i])
                count=1
            i+=1
        res+=str(count)+str(prev[i])
        return res
             
        