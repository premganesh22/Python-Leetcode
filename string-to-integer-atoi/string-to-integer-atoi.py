class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        negative = 1
        res = 0
        max_int = (2 ** 31) - 1
        min_int = -(2 ** 31)

        while i < len(s) and s[i] == ' ':
            i+=1
        
        while i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                i+=1
                negative*=-1
                
            elif s[i] == '+':
                i+=1
            break
        cheaker = set('0123456789')
        while i < len(s) and s[i] in cheaker:
            res= (res*10) + ord(s[i])-48
            i+=1

        if negative == -1:
            res = res*negative

            return max(min_int,res)
        return min(max_int,res)