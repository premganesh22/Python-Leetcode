class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = Counter(magazine)
        for i in ransomNote:
            if dic[i] <= 0:
                return False
                
            dic[i]-=1
        return True
        