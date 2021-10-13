class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    count+=1
            else:
                stack.append(c)
        return len(stack)+count
        