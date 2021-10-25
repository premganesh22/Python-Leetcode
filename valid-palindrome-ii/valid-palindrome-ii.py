class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def ispali(string):
            return string == string[::-1]
        
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return ispali(s[left+1:right+1]) or ispali(s[left:right])
        return True