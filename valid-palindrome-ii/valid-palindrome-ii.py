class Solution(object):
    def checker(self,l,r,s):
            while l<r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return self.checker(l+1,r,s) or self.checker(l,r-1,s)
        return True