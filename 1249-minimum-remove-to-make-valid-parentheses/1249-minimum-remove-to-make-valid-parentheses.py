class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for par in range(len(s)):
            if s[par] == '(':
                stack.append(par)
            elif s[par] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(par)
        output = list(s)
        
        for par in stack:
            output[par] = ''
            
        return ''.join(output)
            