class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for x in path.split('/'):
            if x == '..':
                if stack:
                    stack.pop()
            elif x == '.' or not x:
                continue
            
            else:
                stack.append(x)
        return '/'+ '/'.join(stack)
            
        