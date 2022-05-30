class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stack = []
        for i in split_path:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or not i:
                continue
            else:
                stack.append(i)
        
        return '/' + '/'.join(stack)
        