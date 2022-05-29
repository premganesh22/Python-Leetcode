class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(string):
            return string == string[::-1]
        
        left = 0 
        right = len(s)-1
        
        while left < right:
            if not s[left] == s[right]:
                return check_palindrome(s[0:right]+s[right+1:]) or check_palindrome(s[0:left]+s[left+1:])
            left+=1
            right-=1
        
        return True
        