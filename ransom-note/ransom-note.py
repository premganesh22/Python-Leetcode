class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for char in magazine:
            if char in dic:
                dic[char]+=1
            else:
                dic[char] = 1
        
        for char in ransomNote:
            if char in dic:
                dic[char]-=1
                if dic[char] == 0:
                    del dic[char]
            else:
                return False
        return True