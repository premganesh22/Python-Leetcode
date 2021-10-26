class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        
        
        
        stack = []
        count = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                stack.append(count)
                count = 0
            count+=1
        stack.append(count)
        ans = 0
        for val in range(1,len(stack)):
            ans+=min(stack[val],stack[val-1])
        return ans