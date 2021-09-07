class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in s[::-1]:
            if i != " ":
                result+=1
            elif result:
                return result
        return result